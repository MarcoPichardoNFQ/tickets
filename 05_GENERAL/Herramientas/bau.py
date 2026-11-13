#!/usr/bin/env python3
"""`bau`: el pulso del día en el terminal, y la línea de estado de Claude Code.

Uso: python3 05_GENERAL/Herramientas/bau.py              tabla de abiertos por estado, con colores
     python3 05_GENERAL/Herramientas/bau.py --statusline  una línea: "BAU: 7 abiertos · 2 esperando a NTT · 1 vencido"
     python3 05_GENERAL/Herramientas/bau.py --aviso       foto del día para Google Chat (siempre hay texto)
"""
# Compatible con Python 3.9 (el del sistema en Mac, que es el que ve Obsidian):
# las anotaciones no se evalúan al importar.
from __future__ import annotations

import datetime
import sys

from vault import de_guardia, dias_desde, hoy, listas, tickets

ROJO, AMARILLO, VERDE, GRIS, FIN = "\033[31m", "\033[33m", "\033[32m", "\033[90m", "\033[0m"
ESPERA_NTT = ("Pendiente despliegue UAT", "Pendiente despliegue PRD")
ESPERA_CLIENTE = ("Revisión cliente", "Pruebas cliente UAT")
# El plazo mide la primera respuesta: vence si nadie lo ha asumido (sigue Abierto) a tiempo.
# En curso, esperando al cliente o a NTT ya no vence: alguien lo tiene entre manos.
SIN_ASUMIR = ("Abierto",)
DIAS_AVISO = 3      # a partir de aquí una espera se marca en rojo y entra en el aviso


def resumen():
    """Clasifica los abiertos: lista de (ruta, fm, vencido, días en estado)."""
    hoy_ = hoy()
    filas = []
    for p, fm in tickets(incluir_archivo=False):
        if fm.get("estado") == "Resuelto":
            continue
        limite = fm.get("fecha_limite", "")
        vencido = bool(limite) and fm.get("estado") in SIN_ASUMIR and datetime.date.fromisoformat(limite) < hoy_
        filas.append((p, fm, vencido, dias_desde(fm.get("actualizado", "")) or 0))
    return filas


def contadores(filas):
    """Números para la línea de estado y el aviso."""
    return {
        "abiertos": len(filas),
        "ntt": sum(1 for _, fm, _, _ in filas if fm.get("estado") in ESPERA_NTT),
        "cliente": sum(1 for _, fm, _, _ in filas if fm.get("estado") in ESPERA_CLIENTE),
        "vencidos": sum(1 for _, _, v, _ in filas if v),
        "esperas_largas": [(p, fm, d) for p, fm, _, d in filas
                           if fm.get("estado") in ESPERA_NTT + ESPERA_CLIENTE and d >= DIAS_AVISO],
    }


def tabla(filas):
    """Tabla en el terminal agrupada por estado, en el orden del circuito."""
    if not filas:
        print(f"{VERDE}Sin tickets abiertos.{FIN}")
        return
    for estado in listas()["estado"]:
        grupo = [f for f in filas if f[1].get("estado") == estado]
        if not grupo:
            continue
        print(f"\n{estado} ({len(grupo)})")
        for p, fm, vencido, dias in grupo:
            color = ROJO if vencido or (estado in ESPERA_NTT + ESPERA_CLIENTE and dias >= DIAS_AVISO) \
                else AMARILLO if dias >= 1 else GRIS
            asunto = p.stem.split(" — ", 2)[-1][:50]
            print(f"  {color}{p.stem[:11]}{FIN}  {fm.get('prioridad', '-'):5}  {fm.get('responsable', '-')[:18]:18}  "
                  f"{color}{dias:>2}d{FIN}  {'VENCIDO ' if vencido else ''}{asunto}")
    c = contadores(filas)
    print(f"\n{c['abiertos']} abiertos · {c['ntt']} esperando a NTT · {c['cliente']} esperando al cliente · "
          f"{ROJO if c['vencidos'] else ''}{c['vencidos']} vencidos{FIN}")


def statusline(filas):
    """Una línea sin colores para la barra de Claude Code."""
    c = contadores(filas)
    print(f"BAU: {c['abiertos']} abiertos · {c['ntt']} esperando a NTT · {c['vencidos']} vencido(s)")


def aviso(filas):
    """Foto del día para Google Chat: siempre sale (la Action la manda a las tres horas).

    Abiertos por responsable y por estado, creados y resueltos de ayer, responsable de
    guardia, y solo si los hay, vencidos y esperas de más de DIAS_AVISO días.
    """
    from collections import Counter
    c = contadores(filas)
    ayer = (hoy() - datetime.timedelta(days=1)).isoformat()
    por_resp = Counter(fm.get("responsable") or "sin responsable" for _, fm, _, _ in filas)
    por_estado = Counter(fm.get("estado") for _, fm, _, _ in filas)
    todos = list(tickets())
    creados = sum(1 for _, fm in todos if fm.get("fecha_apertura") == ayer)
    resueltos = sum(1 for _, fm in todos if fm.get("fecha_resolucion") == ayer)
    lineas = ["*Vault BAU, foto del día*",
              f"Abiertos: {c['abiertos']}. " + ", ".join(f"{r} {n}" for r, n in por_resp.most_common()) + ".",
              "Por estado: " + ", ".join(f"{e} {por_estado[e]}" for e in listas()["estado"] if por_estado[e]) + ".",
              f"Ayer: {creados} creado(s), {resueltos} resuelto(s).",
              f"De guardia: {de_guardia()}." if de_guardia() else "Sin responsable de guardia para los tickets nuevos: elígelo en el Dashboard."]
    # Solo el id: el nombre completo del fichero hace ilegible el mensaje en Chat
    vencidos = [p.stem[:11] for p, _, v, _ in filas if v]
    if vencidos:
        lineas.append(f"Vencidos ({len(vencidos)}): " + ", ".join(vencidos) + ".")
    lineas += [f"Espera: {p.stem[:11]}, {d} días en {fm.get('estado')}" for p, fm, d in c["esperas_largas"]]
    print("\n".join(lineas))


if __name__ == "__main__":
    filas = resumen()
    {"--statusline": statusline, "--aviso": aviso}.get(sys.argv[1] if len(sys.argv) > 1 else "", tabla)(filas)

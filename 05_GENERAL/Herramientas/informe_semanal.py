#!/usr/bin/env python3
"""Informe semanal en 05_GENERAL/Informes/<desde> a <hasta>.md: la última semana completa de
domingo a sábado. Lo ejecuta la Action de los lunes; también vale a mano. Es la agenda de la
reunión con el cliente. La semana en curso se ve en vivo en el Dashboard.

Contenido: abiertos por estado, creados y resueltos en la semana, esperas a NTT y
al cliente con días, rechazos de la semana, tiempo medio en cada estado de espera
(calculado del historial de estados que estampa el hook), y un gráfico Mermaid.

Uso: python3 05_GENERAL/Herramientas/informe_semanal.py [--semanas 1]
"""
# Compatible con Python 3.9 (el del sistema en Mac, que es el que ve Obsidian):
# las anotaciones no se evalúan al importar.
from __future__ import annotations

import datetime
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from vault import RAIZ, hoy, listas, tickets

INFORMES = RAIZ / "05_GENERAL/Informes"
ESPERAS = ("Revisión cliente", "Pendiente despliegue UAT", "Pruebas cliente UAT", "Pendiente despliegue PRD")
LINEA_HISTORIAL = re.compile(r"^- (\d{4}-\d{2}-\d{2} \d{2}:\d{2}) — (.+?) → (.+?) — ")


def transiciones(texto: str):
    """Lista de (fecha_hora, estado_anterior, estado_nuevo) del historial de estados."""
    return [(datetime.datetime.fromisoformat(m.group(1)), m.group(2), m.group(3))
            for linea in texto.splitlines() if (m := LINEA_HISTORIAL.match(linea))]


def tiempos_en_espera(todos):
    """Horas pasadas en cada estado de espera, por ticket, a partir de las transiciones."""
    horas = defaultdict(list)
    for _, _, texto in todos:
        t = transiciones(texto)
        for (f1, _, entra), (f2, _, _) in zip(t, t[1:]):
            if entra in ESPERAS:
                horas[entra].append((f2 - f1).total_seconds() / 3600)
    return {e: sum(h) / len(h) / 24 for e, h in horas.items()}      # media en días


def informe(desde: datetime.date, hasta: datetime.date) -> str:
    """Texto Markdown completo del informe para el periodo [desde, hasta]."""
    todos = [(p, fm, p.read_text(encoding="utf-8")) for p, fm in tickets()]
    en = lambda f: f and desde.isoformat() <= f[:10] <= hasta.isoformat()
    abiertos = [(p, fm) for p, fm, _ in todos if fm.get("estado") != "Resuelto"]
    creados = [p for p, fm, _ in todos if en(fm.get("fecha_apertura", ""))]
    resueltos = [(p, fm) for p, fm, _ in todos if en(fm.get("fecha_resolucion", ""))]
    rechazos = sum(t.count("— RECHAZO") for p, fm, t in todos
                   if any(en(m.group(1)) for m in re.finditer(r"- (\d{4}-\d{2}-\d{2})[^\n]*RECHAZO", t)))
    por_estado = Counter(fm.get("estado", "?") for _, fm in abiertos)
    esperas = sorted(((p, fm) for p, fm in abiertos if fm.get("estado") in ESPERAS),
                     key=lambda x: x[1].get("actualizado", ""))
    medias = tiempos_en_espera(todos)

    L = ["---", f"desde: {desde}", f"hasta: {hasta}", "tags: [informe, bau]", "---", "",
         f"# Informe semanal BAU · del domingo {desde} al sábado {hasta}", "",
         "## En una línea", "",
         f"{len(abiertos)} abiertos · {len(creados)} creados · {len(resueltos)} resueltos · {rechazos} rechazos del cliente"
         f" · {sum('Sala' in (fm.get('categoria') or []) for _, fm in resueltos)} salas atendidas", "",
         "## Abiertos por estado", "", "```mermaid", "pie showData", f'    title Abiertos por estado ({len(abiertos)})']
    L += [f'    "{e}" : {n}' for e, n in por_estado.items()] + ["```", ""]
    L += ["| Estado | Tickets |", "|---|---|"] + [f"| {e} | {por_estado.get(e, 0)} |" for e in listas()["estado"] if e != "Resuelto"] + [""]

    L += ["## Esperas en curso", ""]
    if esperas:
        L += ["| Ticket | Estado | Desde | Días |", "|---|---|---|---|"]
        for p, fm in esperas:
            act = fm.get("actualizado", "")[:10]
            dias = (hasta - datetime.date.fromisoformat(act)).days if act else "?"
            L.append(f"| [{p.stem[:11]}]({p.relative_to(RAIZ).as_posix().replace(' ', '%20')}) | {fm.get('estado')} | {act} | {dias} |")
    else:
        L.append("Nadie espera a nadie.")
    L += ["", "## Tiempo medio en cada espera (histórico completo)", ""]
    L += [f"- {e}: {medias[e]:.1f} días" for e in ESPERAS if e in medias] or ["Aún no hay transiciones registradas."]

    L += ["", "## Resueltos esta semana", ""]
    L += [f"- [{p.stem[:11]}]({p.relative_to(RAIZ).as_posix().replace(' ', '%20')}): {fm.get('sintoma') or p.stem.split(' — ', 2)[-1]} → {fm.get('solucion_corta') or 'sin solución corta'}"
          for p, fm in resueltos] or ["Ninguno."]
    L += ["", "## Creados esta semana", ""]
    L += [f"- [{p.stem[:11]}]({p.relative_to(RAIZ).as_posix().replace(' ', '%20')}): {p.stem.split(' — ', 2)[-1]}" for p in creados] or ["Ninguno."]

    # Foto para el cliente: dos tablas planas (id, asunto, tiempo), para copiar en un correo
    def dias(a, b):
        try:
            return (datetime.date.fromisoformat(b[:10]) - datetime.date.fromisoformat(a[:10])).days
        except ValueError:
            return "?"
    L += ["", "## Foto para el cliente", "", "### Resueltos", "", "| Id | Asunto | Resuelto el | Días |", "|---|---|---|---|"]
    L += [f"| {p.stem[:11]} | {p.stem.split(' — ', 2)[-1]} | {fm.get('fecha_resolucion', '')} | {dias(fm.get('fecha_apertura', ''), fm.get('fecha_resolucion', ''))} |"
          for p, fm in resueltos] or ["| — | Ninguno | | |"]
    L += ["", "### Pendientes a " + hasta.isoformat(), "", "| Id | Asunto | Estado | Días abierto |", "|---|---|---|---|"]
    L += [f"| {p.stem[:11]} | {p.stem.split(' — ', 2)[-1]} | {fm.get('estado', '')} | {dias(fm.get('fecha_apertura', ''), hasta.isoformat())} |"
          for p, fm in sorted(abiertos, key=lambda x: x[1].get('fecha_apertura', ''))] or ["| — | Ninguno | | |"]
    return "\n".join(L) + "\n"


def semana_anterior(referencia: datetime.date):
    """Última semana completa de domingo a sábado anterior a `referencia` (decisión del 2026-10-16).

    Si hoy es lunes 12, devuelve (domingo 4, sábado 10). Si se ejecuta en domingo, la semana
    que acaba de terminar es la del sábado anterior (ayer)."""
    sabado = referencia - datetime.timedelta(days=(referencia.weekday() + 2) % 7 or 7)
    return sabado - datetime.timedelta(days=6), sabado


if __name__ == "__main__":
    semanas = int(sys.argv[sys.argv.index("--semanas") + 1]) if "--semanas" in sys.argv else 1
    desde, hasta = semana_anterior(hoy())
    desde = hasta - datetime.timedelta(days=7 * semanas - 1)
    INFORMES.mkdir(exist_ok=True)
    destino = INFORMES / f"{desde} a {hasta}.md"            # nombre con fechas: el corte no es la semana ISO
    destino.write_text(informe(desde, hasta), encoding="utf-8")
    print(destino.relative_to(RAIZ))

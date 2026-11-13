#!/usr/bin/env python3
"""Convierte lo que Studio extrae de un correo en un ticket nuevo o en una entrada
del histórico de un ticket abierto. Lo ejecuta la Action correo.yml.

Entrada: JSON en la variable de entorno CORREO con las claves que produce Gemini:
  asunto   asunto del correo tal cual (es la referencia_origen)
  sintoma  una línea en español
  resumen  dos o tres líneas en español, sin datos de contacto
  fecha    opcional, AAAA-MM-DD del correo
  entorno, categoria, prioridad   opcionales; solo se usan si el valor está en listas.json
  detalles opcional, datos técnicos del correo y de sus capturas (texto libre)
  adjuntos opcional, lista con los nombres de los ficheros adjuntos (la pone el .gs)

Regla de respuesta vs nuevo (diseño §14.15):
  - si el asunto contiene NFQBAU-NNNN, o coincide (sin RE:/RES:/FW:/ENC:) con la
    referencia_origen de un ticket, y ese ticket está vivo → entrada en su histórico;
  - si el ticket del hilo está Resuelto → ticket NUEVO enlazado al anterior. Un ticket
    cerrado nunca se reabre automáticamente; reabrir es una acción humana;
  - si no hay ticket del hilo → ticket nuevo: origen email, prioridad la que diga Gemini
    (o Media) y responsable el de guardia (05_GENERAL/Guardia-de-tickets.md), si lo hay.

Salas (SALA): cada correo sin Re: es una llamada y un ticket nuevo ya Resuelto, categoría Sala;
un Re: a una sala de hoy o ayer va a su histórico aunque esté Resuelta (es la misma llamada).

Estado por correo (EVENTOS): en un hilo vivo, el `evento` de Gemini mueve el estado solo desde el
estado esperado, nunca a Resuelto, y pone el prefijo fijo en el histórico.

Imprime tres líneas: la ruta del fichero tocado; `nuevo`, `sala`, `respuesta`, `estado` o `prd`;
y el detalle ("Pruebas cliente UAT → Pendiente despliegue PRD") o vacía (para los avisos). No commitea ni escanea: eso lo hace la Action.
Sale con código 3 si Gemini marcó es_ticket=false y no hay ticket vivo del hilo (la Action
termina sin crear ni avisar). Con ticket vivo, la respuesta siempre va a su histórico.
"""
# Compatible con Python 3.9: las anotaciones no se evalúan al importar.
from __future__ import annotations

import datetime
import json
import os
import re
import sys

from vault import ABIERTOS, ARCHIVO, RAIZ, ahora, de_guardia, frontmatter, hoy, listas, poner_campo
from nuevo_ticket import crear

PREFIJOS = re.compile(r"^(?:\s*(?:(?:re|res|fw|fwd|enc|rv)\s*:|\[ext(?:ernal)?\])\s*)+", re.I)
# Petición de entrar en una sala (P0, P1, sala de projetos): cada una es un ticket ya Resuelto
# de categoría Sala, para contar las llamadas atendidas. Comprobado con los asuntos de 2026-10/11.
SALA = re.compile(r"sala de projetos|\bWR\s*P\d\b|\bP[01]\b", re.I)
AUTOR = "Correo automático"
# Estado por correo: `evento` de Gemini -> (prefijo del histórico, {estado de partida: destino}).
# Solo avanza desde el estado esperado y nunca a Resuelto: cerrar es siempre de una persona.
# El prefijo se escribe aunque el estado no cuadre: es un hecho del hilo y el informe lo cuenta.
EVENTOS = {
    "aprobacion": ("APROBACIÓN", {"Revisión cliente": "Pendiente despliegue UAT"}),
    "desplegado_uat": ("", {"Pendiente despliegue UAT": "Pruebas cliente UAT"}),
    "aprobacion_uat": ("APROBACIÓN UAT", {"Pruebas cliente UAT": "Pendiente despliegue PRD"}),
    "aprobacion_prd": ("APROBACIÓN PRD", {"Pruebas cliente UAT": "Pendiente despliegue PRD"}),
    "desplegado_prd": ("", {}),                 # no cambia: avisa para que una persona lo cierre
    "rechazo": ("RECHAZO", {"Revisión cliente": "En curso", "Pruebas cliente UAT": "En curso"}),
}      # tiene ficha en 04_PERSONAS para pasar el escáner


def normalizar(asunto: str) -> str:
    """Sin prefijos de respuesta, sin fecha final entre paréntesis, sin comillas, sin dobles espacios, en minúsculas."""
    s = re.sub(r"[\"'\\]", "", asunto or "")   # comillas antes que prefijos: '"RES: Re: X' partía el hilo
    s = PREFIJOS.sub("", s)                     # Re:, RES:, FW:... y las etiquetas [EXT] / [EXTERNAL]
    s = re.sub(r"\s*\(\d{4}-\d{2}-\d{2}\)\s*$", "", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def ticket_del_hilo(asunto: str):
    """Ticket al que pertenece el correo, busque donde busque (Abiertos y Archivo), o None.

    Devuelve (ruta, frontmatter). Quien llama decide: si está vivo, se añade al
    histórico; si está Resuelto, se crea uno nuevo enlazado. Un ticket cerrado
    nunca se reabre automáticamente (diseño §14.15, regla 3).
    """
    m = re.search(r"NFQBAU-\d+", asunto or "")
    clave = normalizar(asunto)
    candidatos = []
    for carpeta in (ABIERTOS, ARCHIVO):
        for p in sorted(carpeta.glob("NFQBAU-*.md"), reverse=True):
            fm = frontmatter(p.read_text(encoding="utf-8"))
            if (m and p.name.startswith(m.group() + " ")) or (clave and normalizar(fm.get("referencia_origen", "")) == clave):
                candidatos.append((p, fm))
    vivos = [c for c in candidatos if c[1].get("estado") != "Resuelto"]
    return (vivos or candidatos or [None])[0]


def extras(d: dict, sep: str = " · ") -> str:
    """'Detalles: ... · Adjuntos del correo: a.png, b.xlsx' con lo que traiga el correo, o cadena vacía."""
    partes = []
    if str(d.get("detalles") or "").strip():
        partes.append("Detalles: " + str(d["detalles"]).strip())
    adj = d.get("adjuntos") or []
    if isinstance(adj, list) and adj:
        partes.append("Adjuntos del correo: " + ", ".join(str(a) for a in adj))
    return sep.join(partes)


def en_lista(d: dict, campo: str):
    """Valor de `campo` si Gemini lo dio y está en listas.json; si no, None (nunca se inventa)."""
    v = str(d.get(campo) or "").strip()
    return v if v in listas()[campo] else None


def entrada_historico(p, resumen: str, extra: str = "", prefijo: str = "") -> None:
    """Añade una línea al final de `## Histórico de interacciones`, con prefijo fijo si lo hay."""
    t = p.read_text(encoding="utf-8")
    linea = (f"- {ahora()} — {AUTOR} — " + (f"{prefijo} — " if prefijo else "")
             + f"Correo nuevo en el hilo: {resumen.strip()}" + (f" {extra}" if extra else ""))
    partes = t.split("\n## Paquete de despliegue", 1)
    partes[0] = partes[0].rstrip("\n") + "\n" + linea + "\n"
    p.write_text("\n## Paquete de despliegue".join(partes), encoding="utf-8")


def sala_de_la_llamada(asunto: str, hilo) -> bool:
    """True si el correo responde (Re:, RES:...) a una sala abierta hoy o ayer: es la misma llamada.
    Un correo sin prefijo es una llamada nueva aunque el asunto se repita ("Entrar em P0")."""
    if not (hilo and PREFIJOS.match(asunto or "") and "Sala" in (hilo[1].get("categoria") or [])):
        return False
    return str(hilo[1].get("fecha_apertura") or "") >= (hoy() - datetime.timedelta(days=1)).isoformat()


def ticket_nuevo(d: dict, anterior=None, sala: bool = False):
    """Crea el ticket con nuevo_ticket.crear y rellena lo que trae el correo.
    Si `anterior` es un ticket cerrado del mismo hilo, lo enlaza en resumen e histórico.
    Una sala nace Resuelta y con categoría Sala: es registro de la llamada, no se trabaja."""
    asunto, sintoma, resumen, fecha = d.get("asunto", ""), d.get("sintoma", ""), d.get("resumen", ""), d.get("fecha", "")
    titulo = re.sub(r"\s+", " ", PREFIJOS.sub("", asunto)).strip()[:80] or "Correo sin asunto"
    p = crear(titulo, en_lista(d, "prioridad") or "Media", "email")    # la prioridad fija la fecha límite
    t = p.read_text(encoding="utf-8")
    for campo in ("entorno", "categoria"):                              # listas: [Producción], [Rundeck]
        if en_lista(d, campo):
            t = poner_campo(t, campo, f"[{en_lista(d, campo)}]")
    if sala:
        t = poner_campo(t, "categoria", "[Sala]")
        t = poner_campo(t, "estado", "Resuelto")
    if de_guardia():                                                    # responsable de guardia vigente
        t = poner_campo(t, "responsable", de_guardia())
    # Si el ticket nace de una respuesta, la referencia no arrastra los "Re:": es el asunto del hilo
    ref = PREFIJOS.sub("", asunto).strip() + (f" ({fecha})" if fecha else "")
    t = poner_campo(t, "referencia_origen", json.dumps(ref, ensure_ascii=False))
    if sintoma:
        t = poner_campo(t, "sintoma", json.dumps(sintoma.strip(), ensure_ascii=False))
    if anterior is not None:
        pa, fa = anterior
        enlace = f"[{pa.name[:11]}](../{pa.relative_to(RAIZ / '02_TICKETS').as_posix().replace(' ', '%20')})"
        resumen = f"Continúa el hilo del {enlace}, cerrado el {fa.get('fecha_resolucion') or '?'}: no se reabre, se crea este. " + resumen.strip()
    cuerpo = resumen.strip() + (f"\n\n{extras(d, chr(10))}" if extras(d) else "")
    t = t.replace("## Resumen\n\n", f"## Resumen\n\n{cuerpo}\n\n", 1)
    t = re.sub(r"- \d{4}-\d{2}-\d{2} \d{2}:\d{2} — Nombre Apellido — \n",
               f"- {ahora()} — {AUTOR} — {resumen.strip()}\n", t, count=1)
    p.write_text(t, encoding="utf-8")
    return p


def campos_a_mano(crudo: str) -> dict:
    """Recompone asunto, sintoma, resumen y fecha cuando el JSON no se puede leer.

    Gemini escribe un campo por línea: `"clave": "valor",`. Si el valor lleva comillas
    sin escapar (un asunto como `Item compartilhado: "duplicados"`), json.loads falla.
    Aquí se toma, por línea, lo que hay entre la primera `: "` y la última `"`.
    """
    d = {}
    for linea in crudo.splitlines():
        m = re.match(r'\s*"(asunto|sintoma|resumen|fecha|motivo|entorno|categoria|prioridad|detalles|evento)"\s*:\s*"(.*)"\s*,?\s*$', linea)
        if m:
            d[m.group(1)] = m.group(2).replace('\\"', '"')
        b = re.match(r'\s*"es_ticket"\s*:\s*(true|false)', linea, re.I)
        if b:
            d["es_ticket"] = b.group(1).lower() == "true"
    return d if d.get("resumen") else {}


def asunto_de(texto: str) -> str:
    """Solo el asunto, para los avisos; vale aunque el JSON venga roto."""
    m = re.search(r'"asunto"\s*:\s*"(.*)"\s*,?\s*$', texto, re.M)
    return m.group(1) if m else ""


def main() -> int:
    """Lee CORREO, decide nuevo o respuesta, escribe y devuelve la ruta."""
    try:
        d = json.loads(os.environ.get("CORREO", "{}"))
    except json.JSONDecodeError:
        print("CORREO no es JSON válido", file=sys.stderr)
        return 1
    # Desde la hoja de cálculo llega {"texto": "<salida de Gemini>"}: puede venir como
    # JSON limpio o envuelto en ```json ... ```. Se limpia y se vuelve a interpretar.
    if isinstance(d, dict) and "texto" in d and isinstance(d["texto"], str):
        crudo = re.sub(r"^\s*```(?:json)?\s*|\s*```\s*$", "", d["texto"].strip())
        try:
            d = json.loads(crudo)
        except json.JSONDecodeError:
            d = campos_a_mano(crudo)          # asuntos con comillas sin escapar, etc.
            if not d:
                print("La salida de Gemini no es JSON: " + crudo[:120].replace("\n", " "), file=sys.stderr)
                return 1
    if not isinstance(d, dict):
        print("Carga inesperada: " + str(d)[:120], file=sys.stderr)
        return 1
    asunto, resumen = d.get("asunto", ""), d.get("resumen", "")
    if not resumen:
        print("El correo llegó sin resumen; no se crea nada", file=sys.stderr)
        return 1
    # es_ticket (lo decide Gemini) solo dice si se ABRE un ticket. Un hilo con ticket vivo se
    # actualiza siempre: una respuesta informativa ("estoy haciendo la recarga") es historial.
    es_ticket = d.get("es_ticket", True)
    if isinstance(es_ticket, str):
        es_ticket = es_ticket.strip().lower() not in ("false", "no", "0")
    hilo = ticket_del_hilo(asunto)
    sala = bool(SALA.search(asunto or ""))
    detalle = ""
    if hilo and hilo[1].get("estado") != "Resuelto":
        p, tipo, estado = hilo[0], "respuesta", hilo[1].get("estado")
        evento = str(d.get("evento") or "").strip().lower()
        prefijo, destinos = EVENTOS.get(evento, ("", {}))
        entrada_historico(p, resumen, extras(d), prefijo)
        if destinos.get(estado):                # el hook apunta la transición en el historial
            p.write_text(poner_campo(p.read_text(encoding="utf-8"), "estado", destinos[estado]), encoding="utf-8")
            tipo, detalle = "estado", f"{estado} → {destinos[estado]}"
        elif evento == "desplegado_prd" and estado == "Pendiente despliegue PRD":
            tipo, detalle = "prd", "NTT confirma el despliegue en PRD"
    elif sala and sala_de_la_llamada(asunto, hilo):
        p, tipo = hilo[0], "respuesta"
        entrada_historico(p, resumen, extras(d))
    elif sala:                                  # llamada nueva: aunque Gemini diga que no es ticket
        p, tipo = ticket_nuevo(d, sala=True), "sala"
    elif not es_ticket:
        # sin ticket vivo del hilo y Gemini dice que no es ticket: nada que abrir. Código 3 = descartado.
        print("Descartado (no es ticket y no hay hilo vivo): " + str(d.get("motivo", ""))[:160], file=sys.stderr)
        return 3
    else:
        p, tipo = ticket_nuevo(d, anterior=hilo), "nuevo"
    print(p.relative_to(RAIZ))
    print(tipo)
    print(detalle)
    return 0


if __name__ == "__main__":
    if sys.argv[1:2] == ["--probar"]:     # el correo nunca cierra y solo usa estados y prefijos de la lista
        L = listas()
        for prefijo, destinos in EVENTOS.values():
            assert "Resuelto" not in destinos.values() and set(destinos) | set(destinos.values()) <= set(L["estado"])
            assert prefijo in L["prefijos_historico"] + [""]
        assert SALA.search("RE: Entrar em P0") and not SALA.search("Erro na carga P10")
        print("ok")
        sys.exit(0)
    if len(sys.argv) > 1 and sys.argv[1] == "--asunto":      # lo usa la Action para los avisos
        try:
            print(asunto_de(json.loads(os.environ.get("CORREO", "{}")).get("texto", "")))
        except (json.JSONDecodeError, AttributeError):
            print("")
        sys.exit(0)
    sys.exit(main())

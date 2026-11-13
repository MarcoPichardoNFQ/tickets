#!/usr/bin/env python3
"""Crea un ticket nuevo en 02_TICKETS/Abiertos con el siguiente NFQBAU-NNNN.

Uso: python3 05_GENERAL/Herramientas/nuevo_ticket.py "Asunto breve" [prioridad] [origen]
     prioridad: Alta | Media | Baja (por defecto Media)
     origen:    email | reunión | llamada (por defecto email)

- El id es max(ids existentes en 02_TICKETS/) + 1, empezando en 1500. No hay
  fichero contador: así Obsidian Git nunca genera conflictos por él.
- fecha_limite se calcula con dias_limite de listas.json según la prioridad.
"""
# Compatible con Python 3.9 (el del sistema en Mac, que es el que ve Obsidian):
# las anotaciones no se evalúan al importar.
from __future__ import annotations

import datetime
import re
import sys

from vault import ABIERTOS, RAIZ, TICKETS, ahora_dt, controles_ticket, hoy, listas, poner_campo

PLANTILLA = RAIZ / "05_GENERAL/Plantillas/Ticket.md"
INICIO = 1500


def siguiente_id() -> int:
    """Mayor NFQBAU-NNNN presente en Abiertos y Archivo, más uno."""
    ids = [int(m.group(1)) for p in TICKETS.rglob("NFQBAU-*.md")
           if (m := re.match(r"NFQBAU-(\d+)", p.name))]
    return max(ids, default=INICIO - 1) + 1


def crear(asunto: str, prioridad: str = "Media", origen: str = "email"):
    """Rellena la plantilla y escribe el fichero. Devuelve la ruta."""
    L = listas()
    if prioridad not in L["prioridad"] or origen not in L["origen"]:
        sys.exit(f"prioridad debe ser {L['prioridad']} y origen {L['origen']}")
    hoy_ = hoy()
    limite = hoy_ + datetime.timedelta(days=L["dias_limite"][prioridad])
    ident = f"NFQBAU-{siguiente_id()}"
    asunto = re.sub(r'[\\/:*?"<>|]', "", asunto).strip()           # caracteres prohibidos en nombres
    destino = ABIERTOS / f"{ident} — {hoy_.isoformat()} — {asunto}.md"

    # Sustituciones sobre la plantilla: id, fechas y campos elegidos
    cuerpo = (PLANTILLA.read_text(encoding="utf-8")
              .replace("NFQBAU-NNNN", ident)
              .replace("{{date}}", hoy_.isoformat())
              .replace("{{time}}", ahora_dt().strftime("%H:%M"))
              .replace("{{controles}}", controles_ticket()))       # barra Meta Bind
    for clave, valor in (("fecha_limite", limite.isoformat()), ("prioridad", prioridad), ("origen", origen)):
        cuerpo = poner_campo(cuerpo, clave, valor)
    destino.write_text(cuerpo, encoding="utf-8")
    return destino


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    print(crear(*sys.argv[1:4]))

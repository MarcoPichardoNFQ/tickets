#!/usr/bin/env python3
"""Mueve a 02_TICKETS/Archivo los tickets con estado Resuelto y 7 días o más
desde fecha_resolucion. Lo ejecuta la Action diaria (archivo.yml); también vale a mano.

Uso: python3 05_GENERAL/Herramientas/archivar.py [--dias 7]
"""
# Compatible con Python 3.9 (el del sistema en Mac, que es el que ve Obsidian):
# las anotaciones no se evalúan al importar.
from __future__ import annotations

import sys

from vault import ARCHIVO, dias_desde, tickets


def main(dias: int) -> int:
    """Recorre Abiertos y mueve los que cumplen. Avisa si falta fecha_resolucion."""
    movidos = 0
    for p, fm in tickets(incluir_archivo=False):
        if fm.get("estado") != "Resuelto":
            continue
        edad = dias_desde(fm.get("fecha_resolucion", ""))
        if edad is None:
            print(f"AVISO {p.name}: Resuelto sin fecha_resolucion, no se archiva")
        elif edad >= dias:
            p.rename(ARCHIVO / p.name)
            print(f"archivado {p.name}")
            movidos += 1
    return movidos


if __name__ == "__main__":
    n = int(sys.argv[sys.argv.index("--dias") + 1]) if "--dias" in sys.argv else 7
    print(f"{main(n)} ticket(s) archivado(s)")

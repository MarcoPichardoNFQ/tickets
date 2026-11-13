#!/usr/bin/env python3
"""Guardia de la zona protegida. Evita que Claude Code, en el uso normal, cambie
la infraestructura del vault "de paso" mientras resuelve un ticket.

Zona protegida: todo lo que no es trabajo diario (herramientas, plantillas,
listas, hooks, Actions, configuración, manuales, diseño, referencia técnica,
submódulos). El trabajo diario (01_ a 04_ e Informes) nunca se bloquea.

Llave: el fichero .claude/mantenimiento. Solo lo crea una persona a mano
(`touch .claude/mantenimiento`); mientras existe, la guardia deja pasar.
No se versiona. Claude tiene prohibido crearlo.

Uso desde Claude Code (PreToolUse en .claude/settings.json): recibe el JSON
de la llamada por stdin y sale con código 2 para bloquear, 0 para dejar pasar.
Uso desde el hook de Git: `guardia.py --git ruta...` sale 1 si alguna ruta
está protegida (el hook decide según la rama).
"""
# Compatible con Python 3.9 (el del sistema en Mac, que es el que ve Obsidian):
# las anotaciones no se evalúan al importar.
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
LLAVE = RAIZ / ".claude/mantenimiento"

# --- Zona protegida: prefijos relativos a la raíz del vault -----------------
PROTEGIDOS = (
    ".githooks/", ".github/", ".claude/", ".obsidian/",
    "05_GENERAL/Herramientas/", "05_GENERAL/Plantillas/", "05_GENERAL/Diagramas/",
    "05_GENERAL/listas.json", "05_GENERAL/Tickets.base", "05_GENERAL/Dashboard.md",
    "05_GENERAL/Manual-", "05_GENERAL/Diseno-",
    "CLAUDE.md", "README.md", "CODEOWNERS", ".gitattributes", ".gitmodules", ".gitignore",
    "00_REFERENCIA_TECNICA/", "06_CODIGO_VERSIONADO/",
)
# Bash: un comando se considera escritura solo dentro del tramo (entre ; && || | o salto
# de línea) donde aparece un token de escritura. Así `python3 script.py && sed -i x ticket`
# no bloquea por el script, y `>/dev/null`, `2>&1` o `>&2` no cuentan como escritura.
ESCRITURA_BASH = re.compile(
    r"(?<![<|\d&=\-])>(?!&|/dev/null)|\bsed\s+-i|\brm\b|\bmv\b|\bcp\b|\btee\b|\bchmod\b|\btouch\b|\bmkdir\b"
    r"|git\s+(checkout|restore|rm|mv)\b|\bpython3?\s+-\s*<<")
SEPARADOR_BASH = re.compile(r"\s*(?:;|&&|\|\||\||\n)\s*")


def protegido(ruta: str) -> bool:
    """True si la ruta (absoluta o relativa al vault) cae en la zona protegida."""
    p = Path(ruta)
    try:
        rel = (p.resolve() if p.is_absolute() else (RAIZ / p).resolve()).relative_to(RAIZ).as_posix()
    except ValueError:                       # fuera del vault: no es asunto de esta guardia
        return False
    return any(rel.startswith(x) for x in PROTEGIDOS)


def rutas_en_bash(comando: str) -> list[str]:
    """Rutas protegidas que aparecen en un tramo del comando que además escribe."""
    malas = set()
    for tramo in SEPARADOR_BASH.split(comando):
        if not ESCRITURA_BASH.search(tramo):
            continue
        candidatos = re.findall(r"[\w./\-]+(?:/[\w.\-]+)+|CLAUDE\.md|README\.md|CODEOWNERS|\.git(?:attributes|modules|ignore)", tramo)
        malas.update(c for c in candidatos if protegido(c))
    return sorted(malas)


# Lo que Obsidian escribe solo con el uso normal (ajustes, vistas .base, el
# Dashboard) y lo que una persona puede tocar sin querer al leer (la referencia
# técnica: el plugin de tablas la reformatea al abrirla) no puede bloquear el
# commit de las personas en main. Sigue protegido frente a Claude; solo se
# exime en el hook de Git. Decisión del 2026-10-08.
LIBRE_EN_GIT = (".obsidian/", "05_GENERAL/Tickets.base", "05_GENERAL/Dashboard.md", "00_REFERENCIA_TECNICA/")


def protegido_en_git(ruta: str) -> bool:
    """Como protegido(), pero sin lo que Obsidian toca por sí mismo."""
    rel = Path(ruta).as_posix()
    return protegido(ruta) and not any(rel.startswith(x) for x in LIBRE_EN_GIT)


def main() -> int:
    """Modo Git (--git rutas) o modo Claude Code (JSON por stdin)."""
    if len(sys.argv) > 1 and sys.argv[1] == "--git":
        malos = [r for r in sys.argv[2:] if protegido_en_git(r)]
        print("\n".join(malos))
        return 1 if malos else 0

    if LLAVE.exists():                       # modo mantenimiento: todo permitido
        return 0
    try:
        llamada = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    tool, entrada = llamada.get("tool_name", ""), llamada.get("tool_input", {})
    afectadas = []
    if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        ruta = entrada.get("file_path", "") or entrada.get("notebook_path", "")
        if ruta and protegido(ruta):
            afectadas = [ruta]
    elif tool == "Bash":
        afectadas = rutas_en_bash(entrada.get("command", ""))
    if not afectadas:
        return 0
    print("BLOQUEADO por la guardia de la zona protegida:", *afectadas, sep="\n  ", file=sys.stderr)
    print("Esto es infraestructura del vault, no trabajo diario. No la cambies para salir de un problema puntual.\n"
          "Resuelve el ticket con lo que hay y, si de verdad hace falta un cambio, proponlo y pide a la persona\n"
          "que active el modo mantenimiento: `touch .claude/mantenimiento` (y luego rama mantenimiento/... + PR).\n"
          "Nunca crees ese fichero tú.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())

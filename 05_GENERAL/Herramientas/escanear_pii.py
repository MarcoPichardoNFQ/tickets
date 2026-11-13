#!/usr/bin/env python3
"""Red de seguridad del vault. Sale con código 1 si encuentra:

- datos personales: emails, teléfonos, DNI/NIE, IBAN;
- credenciales con forma reconocible: password=valor, token: valor, cadenas de
  conexión completas, claves privadas;
- valores fuera de las listas cerradas de listas.json (estado, prioridad...);
- responsable o actualizado_por que no existan como ficha en 04_PERSONAS;
- ids de ticket duplicados.

Uso: python3 05_GENERAL/Herramientas/escanear_pii.py [fichero ...]
Sin argumentos escanea 01_ a 05_. Se excluyen siempre 00_REFERENCIA_TECNICA
(verificada limpia) y 06_CODIGO_VERSIONADO (submódulos). Los nombres de
personas están permitidos; no se buscan.
"""
# Compatible con Python 3.9 (el del sistema en Mac, que es el que ve Obsidian):
# las anotaciones no se evalúan al importar.
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

from vault import RAIZ, TICKETS, frontmatter, listas, personas

ZONAS = ["01_DECISIONES", "02_TICKETS", "03_PROVEEDORES", "04_PERSONAS", "05_GENERAL"]
EXCLUIDAS = ("00_REFERENCIA_TECNICA", "06_CODIGO_VERSIONADO", ".obsidian", ".git")

# --- Patrones ---------------------------------------------------------------
PATRONES = {
    "email": re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"),
    "telefono": re.compile(r"(?<![\w/.-])(?:\+34[\s-]?)?[6789]\d{2}[\s.-]?\d{3}[\s.-]?\d{3}(?![\w/-])"),
    "dni": re.compile(r"\b\d{8}[- ]?[A-HJ-NP-TV-Z]\b"),
    "nie": re.compile(r"\b[XYZ]\d{7}[- ]?[A-HJ-NP-TV-Z]\b"),
    "iban": re.compile(r"\bES\d{2}(?:[\s-]?\d{4}){5}\b"),
    # credenciales: clave seguida de un valor literal (no $VARIABLE ni <marcador>)
    "credencial": re.compile(r"(?i)\b(password|passwd|pwd|contraseña|token|api[_-]?key|secret)\s*[:=]\s*(?![\$<{*x])[^\s'\"]{4,}"),
    "cadena_conexion": re.compile(r"(?i)\b(?:jdbc:|postgres(?:ql)?://|mysql://|mongodb://|Server=)[^\s]*(?:password|pwd)=[^\s;]+"),
    "clave_privada": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
}
PERMITIDOS = ("noreply@anthropic.com", "@example.com", "@users.noreply.github.com")

# --- Campos con lista cerrada: (campo, clave en listas.json, ¿es lista?) -----
CAMPOS_LISTA = [("estado", "estado", False), ("prioridad", "prioridad", False),
                ("categoria", "categoria", True), ("entorno", "entorno", True), ("origen", "origen", False)]


def en_alcance(p: Path) -> bool:
    """Solo .md de las zonas activas; diseño y manuales quedan fuera (hablan de PII)."""
    rel = p.resolve().relative_to(RAIZ).parts
    return p.suffix == ".md" and rel[0] not in EXCLUIDAS and not p.name.startswith("Diseno-") \
        and not p.name.startswith("Manual-")


def escanear_texto(p: Path, texto: str) -> list[str]:
    """Patrones de datos personales y credenciales, línea a línea."""
    hallazgos = []
    for n, linea in enumerate(texto.splitlines(), 1):
        for tipo, rx in PATRONES.items():
            for m in rx.finditer(linea):
                if not any(ok in m.group() for ok in PERMITIDOS):
                    hallazgos.append(f"{p.relative_to(RAIZ)}:{n}: {tipo}: {m.group()[:60]}")
    return hallazgos


def validar_frontmatter(p: Path, texto: str) -> list[str]:
    """Valores fuera de lista y personas inexistentes, solo en tickets."""
    if not p.name.startswith("NFQBAU-") or "02_TICKETS" not in p.parts:
        return []
    fm, L, nombres, problemas = frontmatter(texto), listas(), personas(), []
    for campo, clave, es_lista in CAMPOS_LISTA:
        valores = fm.get(campo, [] if es_lista else "")
        for v in (valores if es_lista else [valores]):
            if v and v not in L[clave]:
                problemas.append(f"{p.relative_to(RAIZ)}: {campo} '{v}' no está en listas.json {L[clave]}")
    for campo in ("estado", "prioridad"):
        if not fm.get(campo):
            problemas.append(f"{p.relative_to(RAIZ)}: {campo} vacío; un ticket siempre lleva {campo}")
    for campo in ("responsable", "actualizado_por"):
        if fm.get(campo) and fm[campo] not in nombres:
            problemas.append(f"{p.relative_to(RAIZ)}: {campo} '{fm[campo]}' no tiene ficha en 04_PERSONAS")
    return problemas


def ids_duplicados() -> list[str]:
    """Dos ficheros con el mismo NFQBAU-NNNN (dos personas creando a la vez)."""
    ids = Counter(m.group() for p in TICKETS.rglob("NFQBAU-*.md") if (m := re.match(r"NFQBAU-\d+", p.name)))
    return [f"id duplicado: {i}" for i, c in ids.items() if c > 1]


def main(args: list[str]) -> int:
    """Escanea los ficheros dados o, sin argumentos, todas las zonas activas."""
    if args:
        ficheros = [p for a in args if (p := Path(a).resolve()).exists() and en_alcance(p)]
    else:
        ficheros = [p for z in ZONAS for p in (RAIZ / z).rglob("*.md") if en_alcance(p)]
    problemas = []
    for p in ficheros:
        texto = p.read_text(encoding="utf-8", errors="ignore")
        problemas += escanear_texto(p, texto) + validar_frontmatter(p, texto)
        if re.search(r"^(<<<<<<<|>>>>>>>) ", texto, re.M):   # conflicto sin resolver: Obsidian no lee la nota
            problemas.append(f"{p.relative_to(RAIZ)}: marcas de conflicto de Git sin resolver (<<<<<<< / >>>>>>>)")
    problemas += ids_duplicados()
    print("\n".join(problemas) or f"OK: {len(ficheros)} fichero(s) sin datos personales ni valores fuera de lista")
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

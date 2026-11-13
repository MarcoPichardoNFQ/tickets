#!/usr/bin/env python3
"""Copia un vault Obsidian a 00_REFERENCIA_TECNICA convirtiendo [[wikilinks]] en
enlaces Markdown relativos y quitando acentos de los nombres de carpeta.
Los ficheros conservan su nombre. Se saltan bloques de código (``` y `inline`).

Uso: python3 05_GENERAL/Herramientas/migrar_referencia.py ORIGEN [DESTINO]
"""
# Compatible con Python 3.9 (el del sistema en Mac, que es el que ve Obsidian):
# las anotaciones no se evalúan al importar.
from __future__ import annotations

import re
import shutil
import sys
import unicodedata
from pathlib import Path
from urllib.parse import quote

RAIZ = Path(__file__).resolve().parents[2]
WIKI = re.compile(r"\[\[([^\]|#]+)(#[^\]|]*)?(?:\|([^\]]*))?\]\]")
CODIGO = re.compile(r"(```.*?```|`[^`\n]*`)", re.S)


def sin_acentos(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def destino_de(origen: Path, p: Path, dst: Path) -> Path:
    rel = p.relative_to(origen)
    return dst.joinpath(*[sin_acentos(x) for x in rel.parts[:-1]], rel.name)


def main(origen: Path, dst: Path) -> None:
    ficheros = [p for p in origen.rglob("*") if p.is_file()
                and ".obsidian" not in p.parts and p.name != ".DS_Store"]
    mapa = {p.stem: destino_de(origen, p, dst) for p in ficheros if p.suffix == ".md"}
    rotos = set()

    def enlace(m, desde):
        nombre, ancla, alias = m.group(1).strip(), m.group(2) or "", m.group(3)
        if nombre not in mapa:
            rotos.add(nombre)
            return m.group(0)
        rel = Path(*(["."] if mapa[nombre].parent == desde.parent else [])) / \
              Path(*([".."] * len(desde.parent.relative_to(dst).parts))) / mapa[nombre].relative_to(dst)
        return f"[{alias or nombre}]({quote(rel.as_posix())}{ancla})"

    for p in ficheros:
        d = destino_de(origen, p, dst)
        d.parent.mkdir(parents=True, exist_ok=True)
        if p.suffix != ".md":
            shutil.copy2(p, d)
            continue
        trozos = CODIGO.split(p.read_text(encoding="utf-8"))
        texto = "".join(t if i % 2 else WIKI.sub(lambda m: enlace(m, d), t) for i, t in enumerate(trozos))
        d.write_text(texto, encoding="utf-8")
    print(f"{len(ficheros)} ficheros migrados a {dst.relative_to(RAIZ)}")
    if rotos:
        print("enlaces sin destino (se dejan como estaban):", *sorted(rotos), sep="\n  ")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else RAIZ / "00_REFERENCIA_TECNICA")

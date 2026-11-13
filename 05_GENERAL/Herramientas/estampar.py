#!/usr/bin/env python3
"""Estampado automático en cada commit. Lo llama .githooks/pre-commit.

Para cada nota preparada (staged) de 01_DECISIONES, 02_TICKETS y 03_PROVEEDORES, y la nota de guardia:
1. escribe `actualizado: AAAA-MM-DD HH:MM` y `actualizado_por: <git user.name>`;
2. si es un ticket y `estado` cambió respecto a la versión anterior en Git,
   añade una línea bajo `## Historial de estados`; y según el estado completa
   `entorno` (UAT en los estados de UAT, Producción en el de PRD; solo añade);
3. vuelve a preparar el fichero para que el commit lleve los cambios.

Y antes de todo eso, ids únicos: un ticket NUEVO cuyo NFQBAU-NNNN ya existe en
origin/main con otro nombre (otra persona o el correo automático lo crearon en el
mismo tramo de 5 minutos) se renumera al siguiente libre, fichero y campo `id`.
Consulta GitHub con un `git fetch` de 5 s como máximo; sin red, no bloquea nada.

Uso: python3 05_GENERAL/Herramientas/estampar.py fichero [fichero ...]   (pre-commit)
     python3 05_GENERAL/Herramientas/estampar.py --push                  (pre-push: lo mismo
     sobre los tickets commiteados que aún no están en origin; si renumera, commitea y
     devuelve 1 para cancelar ese push; el siguiente ciclo de Obsidian Git lo sube limpio)
     python3 05_GENERAL/Herramientas/estampar.py --fusionar MIO SUYO   (merge driver de la
     nota de guardia, lo llama Git a través de .githooks/fusionar-guardia)
     python3 05_GENERAL/Herramientas/estampar.py --fusionar-ticket BASE MIO SUYO   (merge driver
     de los tickets, .githooks/fusionar-ticket: conserva las líneas de historial de los dos)
"""
# Compatible con Python 3.9 (el del sistema en Mac, que es el que ve Obsidian):
# las anotaciones no se evalúan al importar.
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

from vault import GUARDIA, RAIZ, TICKETS, ahora, frontmatter, poner_campo

ZONAS_ESTAMPADAS = ("01_DECISIONES", "02_TICKETS", "03_PROVEEDORES")


def git(*args: str) -> str:
    """Ejecuta git en la raíz del vault y devuelve la salida (vacía si falla)."""
    # quotePath=false: sin él, Git devuelve las rutas con acentos entre comillas y escapadas.
    # encoding utf-8: en Windows Python leería en cp1252, el "—" de los nombres no coincidiría
    # con el fichero de origin y renumeraría tickets ajenos (pasó el 2026-11-06: 1625-1636).
    r = subprocess.run(["git", "-c", "core.quotePath=false", *args], cwd=RAIZ, capture_output=True, text=True, encoding="utf-8")
    return r.stdout if r.returncode == 0 else ""


# --- Ids únicos frente a origin/main ------------------------------------------------
ID = re.compile(r"NFQBAU-(\d+)")


def ids_en_origin() -> dict:
    """{id: nombre de fichero} de los tickets en origin/main tras un fetch corto. {} sin red."""
    try:
        subprocess.run(["git", "fetch", "-q", "origin", "main"], cwd=RAIZ, capture_output=True,
                       timeout=5, env={**os.environ, "GIT_TERMINAL_PROMPT": "0"})
    except (subprocess.TimeoutExpired, OSError):
        return {}
    salida = git("ls-tree", "-r", "--name-only", "origin/main", "--", "02_TICKETS")
    return {int(m.group(1)): l for l in salida.splitlines() if (m := ID.match(Path(l).name))}


def renumerar(rutas, solo_presentes: bool = False) -> list:
    """Renumera los tickets de `rutas` cuyo id ya está en origin/main en OTRO fichero.
    Devuelve [(ruta vieja, ruta nueva)].

    No es colisión: el mismo fichero ya en origin; o un ticket que yo he renombrado
    (el fichero de origin con ese id estaba en mi HEAD y ya no está en mi árbol).
    Sí lo es: el otro fichero está en mi árbol (ya hice pull) o nunca lo tuve (aún no).
    En el pre-push (`solo_presentes`) Obsidian Git ya ha hecho pull: solo cuenta el
    otro fichero si está en mi árbol; así un renombrado mío ya commiteado no se toca.
    """
    origen = ids_en_origin()
    if not origen:
        return []
    usados = set(origen) | {int(m.group(1)) for q in TICKETS.rglob("NFQBAU-*.md") if (m := ID.match(q.name))}
    cambios = []
    for p in rutas:
        m = ID.match(p.name)
        otro = origen.get(int(m.group(1))) if m else None
        if not otro or otro == p.relative_to(RAIZ).as_posix():
            continue
        if not (RAIZ / otro).exists() and (solo_presentes or git("ls-tree", "HEAD", "--", otro).strip()):
            continue                                       # lo renombré yo: no es otro ticket
        nuevo = max(usados) + 1
        usados.add(nuevo)
        destino = p.with_name(p.name.replace(m.group(), f"NFQBAU-{nuevo}", 1))
        texto = p.read_text(encoding="utf-8").replace(f"id: {m.group()}", f"id: NFQBAU-{nuevo}", 1)
        git("mv", "--", p.relative_to(RAIZ).as_posix(), destino.relative_to(RAIZ).as_posix())
        destino.write_text(texto, encoding="utf-8")
        git("add", "--", destino.relative_to(RAIZ).as_posix())
        print(f"{m.group()} ya existe en GitHub ({Path(otro).name}): renumerado a NFQBAU-{nuevo}")
        cambios.append((p, destino))
    return cambios


def fusionar(mio: str, suyo: str) -> int:
    """Merge driver de Git para la nota de guardia: gana la marca `actualizado` más reciente.
    Git llama con las rutas de mi versión y la remota; el resultado se escribe en la mía."""
    a, b = Path(mio), Path(suyo)
    ta, tb = a.read_text(encoding="utf-8"), b.read_text(encoding="utf-8")
    if frontmatter(tb).get("actualizado", "") > frontmatter(ta).get("actualizado", ""):
        a.write_text(tb, encoding="utf-8")
    return 0


MARCA = re.compile(r"(actualizado|actualizado_por):")
LINEA_HIST = re.compile(r"- \d{4}-\d{2}-\d{2} \d{2}:\d{2} — ")
CONFLICTO = re.compile(r"<<<<<<< mio\n(.*?)=======\n(.*?)>>>>>>> suyo\n", re.S)


def fusionar_ticket(base: str, mio: str, suyo: str) -> int:
    """Merge driver de Git para los tickets: dos personas tocan el mismo ticket a la vez.

    Fusión a tres bandas normal (git merge-file) y, de los trozos en conflicto, resuelve solo
    los que no pierden nada: la marca `actualizado` (gana la más reciente) y las líneas de
    historial o histórico (se conservan todas, ordenadas por fecha). Cualquier otro conflicto,
    por ejemplo dos resúmenes distintos, se deja con sus marcas para que lo resuelva una persona.
    Devuelve 0 si quedó limpio, 1 si quedan conflictos (Git lo marca como tal).
    """
    r = subprocess.run(["git", "merge-file", "-p", "-L", "mio", "-L", "base", "-L", "suyo", mio, base, suyo],
                       capture_output=True, text=True, encoding="utf-8")
    if r.returncode < 0:
        return 1
    texto, quedan = r.stdout, False

    def resolver(m):
        nonlocal quedan
        a, b = m.group(1), m.group(2)
        lineas = (a + b).splitlines()
        if lineas and all(MARCA.match(l) for l in lineas):
            marca = lambda s: next((l for l in s.splitlines() if l.startswith("actualizado:")), "")
            return a if marca(a) >= marca(b) else b
        if lineas and all(LINEA_HIST.match(l) for l in lineas):
            return "\n".join(sorted(set(lineas))) + "\n"
        quedan = True
        return m.group(0)

    texto = CONFLICTO.sub(resolver, texto) if r.returncode else texto
    Path(mio).write_text(texto, encoding="utf-8")
    return 1 if quedan else 0


def push() -> int:
    """Modo pre-push: tickets locales que no están en origin por nombre. Si renumera, commitea y cancela el push."""
    en_origin = set(ids_en_origin().values())
    if not en_origin:
        return 0
    locales = [q for q in TICKETS.rglob("NFQBAU-*.md") if q.relative_to(RAIZ).as_posix() not in en_origin]
    if renumerar(locales, solo_presentes=True):
        git("commit", "-q", "-m", "Tickets renumerados: el id ya existía en GitHub")
        print("Push cancelado para que suba el número nuevo; el siguiente ciclo de Obsidian Git lo sube.")
        return 1
    return 0


def estado_anterior(rel: str) -> str:
    """`estado` del fichero en HEAD; 'nuevo' si el fichero no existía; '(vacío)' si existía sin estado."""
    anterior = git("show", f"HEAD:{rel}")
    if not anterior:
        return "nuevo"
    return frontmatter(anterior).get("estado", "") or "(vacío)"


def estampar(p: Path, autor: str) -> bool:
    """Aplica los estampados a un fichero. Devuelve True si lo modificó."""
    rel = p.relative_to(RAIZ).as_posix()
    # Fuera de las zonas solo se estampa la nota de guardia: su marca es lo que da validez al dato
    if (rel.split("/")[0] not in ZONAS_ESTAMPADAS and p != GUARDIA) or not p.name.endswith(".md"):
        return False
    original = texto = p.read_text(encoding="utf-8")
    if not texto.startswith("---"):
        return False
    # La guardia solo se estampa si cambió el responsable: Obsidian reescribe la nota al
    # abrirla y cada estampado de más es un conflicto más entre puestos.
    if p == GUARDIA and frontmatter(texto).get("responsable") == frontmatter(git("show", f"HEAD:{rel}") or "").get("responsable"):
        return False
    marca = ahora()
    texto = poner_campo(texto, "actualizado", marca)
    texto = poner_campo(texto, "actualizado_por", autor)

    # Historial de estados: solo tickets, solo cuando el estado cambia.
    # Al pasar a Resuelto, fecha_resolucion = hoy si nadie la puso (el archivador la necesita).
    if p.name.startswith("NFQBAU-"):
        fm = frontmatter(texto)
        nuevo, viejo = fm.get("estado", ""), estado_anterior(rel)
        if nuevo == "Resuelto" and not fm.get("fecha_resolucion"):
            texto = poner_campo(texto, "fecha_resolucion", marca[:10])
        # Entorno según el circuito: los estados de UAT añaden UAT; el de PRD añade Producción.
        # Solo añade, nunca quita: lo que pusieron Gemini o la persona se respeta.
        ent = list(fm.get("entorno") or [])
        if nuevo in ("Pendiente despliegue UAT", "Pruebas cliente UAT", "Pendiente despliegue PRD") and "UAT" not in ent:
            ent.append("UAT")
        if nuevo == "Pendiente despliegue PRD" and "Producción" not in ent:
            ent.append("Producción")
        if ent != list(fm.get("entorno") or []):
            texto = poner_campo(texto, "entorno", "[" + ", ".join(ent) + "]")
        if nuevo and nuevo != viejo:
            linea = f"- {marca} — {viejo} → {nuevo} — {autor}"
            if "## Historial de estados" not in texto:
                texto = texto.rstrip("\n") + "\n\n## Historial de estados\n"
            texto = texto.rstrip("\n") + "\n" + linea + "\n"

    if texto != original:
        p.write_text(texto, encoding="utf-8")
        git("add", "--", rel)
    return texto != original


def main(ficheros: list[str]) -> int:
    """Exige nombre en Git (lo pide el diseño §14.5) y estampa cada fichero."""
    autor = git("config", "user.name").strip()
    if not autor:
        print("Falta git config user.name \"Nombre Apellido\". Sin eso no se puede registrar quién modifica.")
        return 1
    rutas = [p for f in ficheros if (p := (RAIZ / f).resolve() if not Path(f).is_absolute() else Path(f)).exists()]
    # Ids únicos: solo los tickets nuevos en este commit (los que HEAD no conoce)
    nuevos = [p for p in rutas if p.name.startswith("NFQBAU-") and not git("show", f"HEAD:{p.relative_to(RAIZ).as_posix()}")]
    renombrados = dict(renumerar(nuevos))
    for p in rutas:
        estampar(renombrados.get(p, p), autor)
    return 0


if __name__ == "__main__":
    if sys.argv[1:] == ["--push"]:
        sys.exit(push())
    if sys.argv[1:2] == ["--fusionar"]:
        sys.exit(fusionar(sys.argv[2], sys.argv[3]))
    if sys.argv[1:2] == ["--fusionar-ticket"]:
        sys.exit(fusionar_ticket(sys.argv[2], sys.argv[3], sys.argv[4]))
    sys.exit(main(sys.argv[1:]))

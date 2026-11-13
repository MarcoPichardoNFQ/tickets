#!/usr/bin/env python3
"""Utilidades comunes de las herramientas del vault.

Todos los scripts importan de aquí para no repetir la lectura de frontmatter,
las listas cerradas ni la localización de tickets. Solo stdlib.
"""
# Compatible con Python 3.9 (el del sistema en Mac, que es el que ve Obsidian):
# las anotaciones no se evalúan al importar.
from __future__ import annotations

import datetime
import json
import re
from pathlib import Path

# --- Rutas del vault -------------------------------------------------------
RAIZ = Path(__file__).resolve().parents[2]          # carpeta del vault
TICKETS = RAIZ / "02_TICKETS"
ABIERTOS = TICKETS / "Abiertos"
ARCHIVO = TICKETS / "Archivo"
PERSONAS = RAIZ / "04_PERSONAS"
PROVEEDORES = RAIZ / "03_PROVEEDORES"
LISTAS = RAIZ / "05_GENERAL/listas.json"


def listas() -> dict:
    """Listas cerradas (estado, prioridad, categoría...) desde listas.json."""
    return json.loads(LISTAS.read_text(encoding="utf-8"))


GUARDIA = RAIZ / "05_GENERAL/Guardia-de-tickets.md"
HORAS_GUARDIA = 12


def de_guardia() -> str:
    """Responsable de guardia vigente, o cadena vacía.

    Lee `responsable` y `actualizado` de la nota de guardia (el hook estampa la marca
    al elegir el nombre). Vale HORAS_GUARDIA horas desde esa marca: así los tickets
    nuevos no se asignan a quien ya no los atiende. `nadie` o vacío = sin guardia.
    """
    if not GUARDIA.exists():
        return ""
    fm = frontmatter(GUARDIA.read_text(encoding="utf-8"))
    quien, marca = fm.get("responsable", ""), fm.get("actualizado", "")
    if not quien or quien == "nadie" or quien not in personas() or not marca:
        return ""
    desde = datetime.datetime.strptime(marca[:16], "%Y-%m-%d %H:%M").replace(tzinfo=ahora_dt().tzinfo)
    return quien if ahora_dt() - desde <= datetime.timedelta(hours=HORAS_GUARDIA) else ""


def personas() -> set[str]:
    """Nombres válidos para responsable y actualizado_por: los ficheros de 04_PERSONAS."""
    return {p.stem for p in PERSONAS.glob("*.md")}


# --- Frontmatter -----------------------------------------------------------
def frontmatter(texto: str) -> dict:
    """Lee el frontmatter YAML de una nota con un parser mínimo.

    Soporta lo que usan las plantillas: `clave: valor`, `clave: [a, b]`,
    listas con `- item` y comentarios `# ...`. Devuelve strings o listas.
    No es YAML completo a propósito: así no hace falta dependencia.
    """
    m = re.match(r"^---\n(.*?)\n---", texto, re.S)
    if not m:
        return {}
    datos, clave = {}, None
    for linea in m.group(1).splitlines():
        if not linea.strip() or linea.lstrip().startswith("#"):
            continue
        if linea.startswith(" ") and clave:                    # elemento de lista en bloque
            item = linea.strip()
            if item.startswith("- ") and isinstance(datos.get(clave), list):
                datos[clave].append(item[2:].strip().strip('"'))
            continue
        if ":" not in linea:
            continue
        clave, _, valor = linea.partition(":")
        clave, valor = clave.strip(), valor.split("#", 1)[0].strip()
        if valor.startswith("[") and valor.endswith("]"):     # lista en línea
            datos[clave] = [_sin_comillas(v) for v in valor[1:-1].split(",") if v.strip()]
        elif valor == "":
            datos[clave] = [] if clave in ("categoria", "entorno") else ""
        else:
            datos[clave] = _sin_comillas(valor)
    return datos


def _sin_comillas(valor: str) -> str:
    """Quita las comillas YAML de un valor y deshace sus escapes.

    json.dumps escribe "texto con \"comillas\""; Obsidian, al reescribir el frontmatter
    (cambiar estado con el desplegable), lo pasa a 'texto con "comillas"' y dobla las
    simples internas (''). Sin esto, un asunto con comillas nunca coincidía consigo mismo
    y cada respuesta del hilo abría un ticket nuevo (17 duplicados el 2026-10-21).
    """
    v = valor.strip()
    if len(v) >= 2 and v[0] == v[-1] == '"':
        return v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    if len(v) >= 2 and v[0] == v[-1] == "'":
        return v[1:-1].replace("''", "'")
    return v


def poner_campo(texto: str, clave: str, valor: str) -> str:
    """Escribe `clave: valor` en el frontmatter, sustituyendo o añadiendo la línea."""
    patron = re.compile(rf"^{clave}:[^\n]*$", re.M)
    if patron.search(texto):
        return patron.sub(f"{clave}: {valor}", texto, count=1)
    return texto.replace("\n---", f"\n{clave}: {valor}\n---", 1)   # antes del cierre


# --- Tickets ---------------------------------------------------------------
def tickets(incluir_archivo: bool = True):
    """Genera (ruta, frontmatter) de cada ticket, en Abiertos y opcionalmente Archivo."""
    carpetas = [ABIERTOS] + ([ARCHIVO] if incluir_archivo else [])
    for carpeta in carpetas:
        for p in sorted(carpeta.glob("NFQBAU-*.md")):
            yield p, frontmatter(p.read_text(encoding="utf-8"))


def id_de(ruta: Path) -> str:
    """'NFQBAU-1523' a partir del nombre de fichero."""
    m = re.match(r"NFQBAU-\d+", ruta.name)
    return m.group() if m else ""


def dias_desde(fecha: str) -> int | None:
    """Días transcurridos desde 'AAAA-MM-DD' o 'AAAA-MM-DD HH:MM'. None si no hay fecha."""
    if not fecha:
        return None
    return (hoy() - datetime.date.fromisoformat(fecha[:10])).days


def _zona():
    """Zona horaria del vault (listas.json). Si el sistema no trae la base de datos
    de zonas (Windows sin tzdata), respaldo con el desplazamiento fijo."""
    L = listas()
    try:
        from zoneinfo import ZoneInfo
        return ZoneInfo(L.get("zona_horaria", "UTC"))
    except Exception:                                   # ponytail: respaldo fijo; vale para São Paulo (sin horario de verano)
        return datetime.timezone(datetime.timedelta(hours=L.get("desplazamiento_horas", 0)))


def ahora_dt() -> datetime.datetime:
    """Fecha y hora actuales en la zona del vault."""
    return datetime.datetime.now(_zona())


def ahora() -> str:
    """Marca 'AAAA-MM-DD HH:MM' en la zona del vault, para estampados e histórico."""
    return ahora_dt().strftime("%Y-%m-%d %H:%M")


def hoy() -> datetime.date:
    """Fecha de hoy en la zona del vault. Todos los scripts la usan en vez de date.today()."""
    return ahora_dt().date()


# --- Barra de controles (plugin Meta Bind) ----------------------------------
def _opciones(valores) -> str:
    """option('a'),option('b') con comillas simples, que es lo que admite Meta Bind."""
    return ",".join("option('" + v.replace("'", "\\'") + "')" for v in valores)


def controles_ticket() -> str:
    """Markdown de la barra de desplegables y botones que va al principio de un ticket.

    Los desplegables escriben directamente en el frontmatter (estado, prioridad,
    responsable, categoría, entorno) con los valores de listas.json y las fichas
    de 04_PERSONAS. Los botones lanzan los comandos de Templater y Homepage.
    Misma barra que genera la plantilla Templater; si cambias una, cambia la otra.
    """
    L = listas()
    return "\n".join([
        "> [!abstract] Controles",
        "> Estado `INPUT[inlineSelect(" + _opciones(L["estado"]) + "):estado]` · "
        "Prioridad `INPUT[inlineSelect(" + _opciones(L["prioridad"]) + "):prioridad]` · "
        "Responsable `INPUT[inlineSelect(" + _opciones(sorted(personas())) + "):responsable]`",
        "> Categoría `INPUT[inlineListSuggester(" + _opciones(L["categoria"]) + "):categoria]` · "
        "Entorno `INPUT[inlineListSuggester(" + _opciones(L["entorno"]) + "):entorno]`",
        "> `BUTTON[bau-ntt, bau-dashboard]`",
    ])


# Los botones se definen una sola vez en la configuración de Meta Bind (buttonTemplates)
# y se referencian por id desde cualquier nota. No hace falta nada más en el ticket.
BOTONES_TICKET = ""

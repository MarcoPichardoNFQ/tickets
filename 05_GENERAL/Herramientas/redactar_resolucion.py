#!/usr/bin/env python3
"""Redacta la resolución de los tickets Resueltos que nadie documentó. Lo ejecuta la Action
nocturna (resolucion.yml); también vale a mano con GEMINI_API_KEY en el entorno.

Para cada ticket Resuelto con `solucion_corta` vacía y los cinco bloques de `## Resolución`
vacíos, pide a Gemini un borrador a partir del resumen y del histórico (ya anonimizados) y
rellena solo lo vacío: `solucion_corta` y los bloques. Referencias técnicas no: Gemini no ve
00_REFERENCIA_TECNICA. Deja una línea en el histórico para que la persona lo revise. Lo que
no se deduzca del histórico queda como "No consta en el histórico", nunca inventado.

Uso: python3 05_GENERAL/Herramientas/redactar_resolucion.py [--max 20]
Imprime una ruta por ticket modificado. Sale 0 aunque Gemini falle: lo que no se pudo se
intenta la noche siguiente.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

from vault import ahora, frontmatter, poner_campo, tickets

AUTOR = "Correo automático"
# Flash Lite: 500 peticiones/día en el plan gratuito; los Flash (20/día) quedan para el correo
MODELOS = os.environ.get("MODELO_RESOLUCION", "gemini-3.5-flash-lite, gemini-3.1-flash-lite")
BLOQUES = {
    "que_se_hizo": "### Qué se hizo",
    "como_se_comprobo": "### Cómo se comprobó",
    "con_quien": "### Con quién se habló",
    "servicios": "### Servicios, jobs o tablas tocados",
}
NO_CONSTA = "No consta en el histórico."

PROMPT = """Eres el asistente de un equipo de soporte. Te paso un ticket ya cerrado: su resumen y su
histórico de interacciones. Devuelve SOLO un JSON con cinco campos, en español, sacados del texto:
- "solucion_corta": una línea, qué resolvió el problema (máximo 20 palabras).
- "que_se_hizo": 1 a 4 frases con lo que hizo el equipo, en orden.
- "como_se_comprobo": cómo se confirmó que quedó bien (quién validó, qué prueba).
- "con_quien": personas y áreas que intervinieron, tal como aparecen en el texto ("Nombre I., rol").
- "servicios": funciones, jobs, tablas, informes o entornos tocados, separados por comas.
Usa solo lo que dice el texto: no digas que algo se corrigió o se validó si no consta. Si un campo no se deduce, escribe exactamente "%s".
No incluyas emails, teléfonos, rutas de servidor, hosts ni credenciales.

""" % NO_CONSTA


def seccion(texto: str, titulo: str) -> str:
    """Contenido de una sección `## titulo` hasta la siguiente `## `."""
    m = re.search(rf"^## {re.escape(titulo)}\n(.*?)(?=^## |\Z)", texto, re.S | re.M)
    return m.group(1).strip() if m else ""


def bloques_vacios(texto: str) -> bool:
    """True si los cinco ### de `## Resolución` están vacíos."""
    res = seccion(texto, "Resolución")
    return bool(res) and not any(b.strip() for b in re.split(r"^### .*$", res, flags=re.M)[1:])


def pendientes() -> list:
    """Tickets Resueltos sin documentar, los más recientes primero."""
    lista = []
    for p, fm in tickets(incluir_archivo=True):
        if fm.get("estado") != "Resuelto" or fm.get("solucion_corta") or "Sala" in (fm.get("categoria") or []):
            continue
        if bloques_vacios(p.read_text(encoding="utf-8")):
            lista.append((str(fm.get("fecha_resolucion") or ""), p))
    return [p for _, p in sorted(lista, reverse=True)]


def gemini(prompt: str) -> dict | None:
    """JSON de Gemini recorriendo los modelos. None si ninguno responde (sin cuota o caído)."""
    clave = os.environ.get("GEMINI_API_KEY", "")
    if not clave:
        return None
    cuerpo = json.dumps({"contents": [{"parts": [{"text": prompt}]}],
                         "generationConfig": {"responseMimeType": "application/json", "temperature": 0.2}}).encode()
    for modelo in [m.strip() for m in MODELOS.split(",") if m.strip()]:
        for intento in range(3):
            req = urllib.request.Request(
                f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent",
                data=cuerpo, headers={"Content-Type": "application/json", "x-goog-api-key": clave})
            try:
                with urllib.request.urlopen(req, timeout=60) as r:
                    texto = json.load(r)["candidates"][0]["content"]["parts"][0]["text"]
                return json.loads(texto)
            except urllib.error.HTTPError as e:
                if e.code == 503 and intento < 2:      # alta demanda: esperar y repetir
                    time.sleep(2 ** (intento + 1))
                    continue
                break                                  # 429 u otro: siguiente modelo
            except (urllib.error.URLError, KeyError, IndexError, ValueError, TimeoutError):
                break
    return None


def texto_campo(d: dict, clave: str) -> str:
    """Valor limpio de un campo del JSON; NO_CONSTA si viene vacío."""
    v = d.get(clave)
    if isinstance(v, list):    # frases sueltas: se unen como prosa; nombres o servicios, con comas
        v = " ".join(str(x).strip() for x in v) if any(str(x).rstrip().endswith(".") for x in v) else ", ".join(map(str, v))
    v = str(v or "").strip()
    return v or NO_CONSTA


def sin_contenido(d: dict) -> bool:
    """True si Gemini no sabe qué lo resolvió: mejor dejarlo vacío para una persona."""
    return texto_campo(d, "solucion_corta") == NO_CONSTA


def aplicar(texto: str, d: dict) -> str:
    """Rellena solucion_corta, los cuatro bloques y la línea del histórico. No toca lo escrito."""
    texto = poner_campo(texto, "solucion_corta", json.dumps(texto_campo(d, "solucion_corta").splitlines()[0], ensure_ascii=False))
    for clave, titulo in BLOQUES.items():
        texto = re.sub(rf"^{re.escape(titulo)}\n+(?=### |## |\Z)", f"{titulo}\n\n{texto_campo(d, clave)}\n\n",
                       texto, count=1, flags=re.M)
    linea = f"- {ahora()} — {AUTOR} — Resolución redactada automáticamente a partir del histórico; revisar."
    return re.sub(r"(^## Histórico de interacciones\n.*?)\n*(?=^## )", lambda m: m.group(1).rstrip("\n") + "\n" + linea + "\n\n",
                  texto, count=1, flags=re.S | re.M)


def main(maximo: int) -> int:
    # ponytail: los que Gemini no sabe resolver se reintentan cada noche; los nuevos tienen fecha
    # posterior y van antes, así que no los tapan. Marcarlos como intentados si algún día se nota en la cuota.
    for p in pendientes()[:maximo]:
        texto = p.read_text(encoding="utf-8")
        fm = frontmatter(texto)
        entrada = (f"Asunto: {fm.get('referencia_origen', '')}\nSíntoma: {fm.get('sintoma', '')}\n\n"
                   f"Resumen:\n{seccion(texto, 'Resumen')}\n\nHistórico:\n{seccion(texto, 'Histórico de interacciones')}")
        d = gemini(PROMPT + entrada[:30000])
        if d is None:
            print(f"AVISO sin respuesta de Gemini; se para hasta la próxima noche", file=sys.stderr)
            break
        if sin_contenido(d):
            print(f"AVISO {fm.get('id')}: el histórico no dice qué lo resolvió; queda para documentar a mano", file=sys.stderr)
            continue
        p.write_text(aplicar(texto, d), encoding="utf-8")
        print(p.relative_to(p.parents[2]).as_posix())
    return 0


if __name__ == "__main__":
    if sys.argv[1:2] == ["--probar"]:
        # Comprobación sin red: un ticket de muestra y una respuesta falsa de Gemini
        muestra = ("---\nid: NFQBAU-1\nestado: Resuelto\nsolucion_corta:\n---\n\n## Resumen\n\nAlgo.\n\n"
                   "## Histórico de interacciones\n\n- 2026-11-01 10:00 — Correo automático — Pide X.\n\n"
                   "## Paquete de despliegue\n\n- Update: \n\n## Resolución\n\n### Qué se hizo\n\n### Cómo se comprobó\n\n"
                   "### Con quién se habló\n\n### Servicios, jobs o tablas tocados\n\n### Referencias técnicas usadas y por qué\n\n"
                   "## Vencimiento\n\n## Historial de estados\n- 2026-11-01 10:00 — nuevo → Abierto — Correo automático\n")
        assert bloques_vacios(muestra)
        r = aplicar(muestra, {"solucion_corta": "Se ajustó la función", "que_se_hizo": "Se compiló en UAT.",
                              "como_se_comprobo": "", "con_quien": ["Thiago A., PR Serviços"], "servicios": "function_x"})
        assert 'solucion_corta: "Se ajustó la función"' in r
        assert "### Qué se hizo\n\nSe compiló en UAT.\n\n### Cómo se comprobó\n\nNo consta en el histórico.\n\n### Con" in r
        assert "### Con quién se habló\n\nThiago A., PR Serviços\n\n" in r
        assert "### Referencias técnicas usadas y por qué\n\n## Vencimiento" in r
        assert "Pide X.\n- " in r and "revisar.\n\n## Paquete de despliegue" in r
        assert not bloques_vacios(r)
        assert sin_contenido({"solucion_corta": NO_CONSTA}) and sin_contenido({}) and not sin_contenido({"solucion_corta": "x"})
        assert texto_campo({"q": ["Se pidió A.", "Se hizo B."]}, "q") == "Se pidió A. Se hizo B."
        assert texto_campo({"q": ["Ana B., cliente", "Luis C., NFQ"]}, "q") == "Ana B., cliente, Luis C., NFQ"
        print("ok")
        sys.exit(0)
    n = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 20
    sys.exit(main(n))

# Prompt de Gemini para el correo automático

> Desde el plan C (2026-10-16) el prompt vive dentro de `correo_puente.gs`, en la constante `PROMPT`, y Gemini se llama por API con salida JSON estricta. Este fichero se conserva como referencia legible de la versión de Studio (seis campos); el prompt vigente del `.gs` pide diez (además `entorno`, `categoria`, `prioridad` y `detalles`) y recibe las capturas y los PDF del correo.

## Versión anterior, para el paso de Gemini en Workspace Studio (retirado)

Copiar en el paso **Preguntar a Gemini** del flujo. Los marcadores `{{asunto}}`, `{{remitente}}`, `{{fecha}}` y `{{cuerpo}}` se **borran** y en su lugar se inserta con "+variables" el campo correspondiente del correo (Studio no sustituye texto). Fuentes: Workspace, no web. Formato de respuesta: texto. La salida debe ser solo el JSON; si Gemini lo envuelve en ```json, la Action lo limpia.

```
Eres el asistente de un equipo de soporte. Recibes un correo, casi siempre en portugués de Brasil, y devuelves SOLO un JSON con seis campos, en español:

- "asunto": el asunto del correo tal cual, sin cambiarlo.
- "sintoma": una sola línea que diga cómo se manifiesta el problema (qué informe, job, tabla o pantalla falla y cómo). Sin nombres de personas.
- "resumen": dos o tres líneas con qué pide el remitente, qué ha pasado y desde cuándo. Refiérete a las personas por su nombre de pila, la inicial de su primer apellido y su rol o empresa: "José Carlos N., contabilidad de fondos del cliente", "Ricardo C., responsable del Proyecto Apollo". Nunca el apellido completo. No incluyas direcciones de correo, teléfonos, enlaces, direcciones postales, claves de reunión ni firmas. Si hay adjuntos, di solo "adjunta capturas" o "adjunta un fichero".
- "fecha": la fecha del correo en formato AAAA-MM-DD.
- "es_ticket": true si el correo es una incidencia, un error, una petición o una consulta de un cliente o de un proveedor dirigida al equipo de soporte; false si es una notificación automática de un sistema (Drive, calendario, alertas, Jira), una newsletter, un acuse de recibo, un reenvío sin petición, o una conversación interna sin nada que resolver. En caso de duda, true.
- "motivo": una línea que explique por qué es o no es ticket.

Si el correo es una respuesta dentro de un hilo, resume solo lo nuevo que aporta.

Asunto: {{asunto}}
Fecha: {{fecha}}
Remitente: {{remitente}}
Cuerpo:
{{cuerpo}}
```

Ejemplo de salida esperada:

```json
{"asunto": "RES: ETF - Relatório de Operações RF", "sintoma": "informe de operaciones de RF del Portal sin lucro/perjuicio en ventas de fondos MEGARA", "resumen": "Ricardo C., responsable del Proyecto Apollo en el cliente, resume dos fallos de los informes de renta fija del Portal tras la reunión del 10/08 y pide análisis y próximos pasos. Adjunta capturas.", "fecha": "2026-08-10", "es_ticket": true, "motivo": "el cliente reporta un fallo en un informe y pide análisis"}
```

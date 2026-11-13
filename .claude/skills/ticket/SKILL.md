---
name: ticket
description: Gestiona tickets del vault BAU. Modos - nuevo (alta desde email o llamada, con búsqueda de similares y confirmación de campos), actualizar (nueva interacción anonimizada), resolver (cierre en cinco bloques), consultar (qué se hizo otras veces con un síntoma), redactar (correo recurrente al cliente o a NTT). Usa cuando el usuario diga /ticket, "abre un ticket", "actualiza el NFQBAU-...", "cierra el ticket", "¿qué hicimos con...?" o "redacta el correo de...".
---

# /ticket

Comando del vault BAU. Sintaxis: `/ticket <modo> [NFQBAU-NNNN | "síntoma"]`. Sin modo, pregunta cuál.

Reglas que valen para todos los modos:

- **Propón, no escribas.** Muestra lo que vas a poner y espera confirmación con AskUserQuestion. Solo tras el ok tocas ficheros.
- **Listas cerradas.** Los valores de `estado`, `prioridad`, `categoria`, `entorno` y `origen` salen de `05_GENERAL/listas.json`. `responsable` es un nombre de fichero de `04_PERSONAS/`. Ofrece opciones, nunca texto libre para estos campos.
- **Anonimiza antes de escribir.** Emails, teléfonos, DNI, IBAN, direcciones y credenciales no entran. Las personas del correo, como nombre e inicial del apellido más su rol: "José Carlos N., contabilidad de fondos del cliente". Nunca el apellido completo. Si el usuario pega un correo, guarda un resumen de dos o tres líneas, nunca el texto.
- **No estampes.** `actualizado`, `actualizado_por` y `## Historial de estados` los pone el hook en el commit.
- Formato de entrada del histórico: `- AAAA-MM-DD HH:MM — Nombre Apellido — texto`. Fecha y hora actuales; nombre = `git config user.name`.
- Rutas: tickets en `02_TICKETS/Abiertos/` y `Archivo/`; referencia técnica en `00_REFERENCIA_TECNICA/`; proveedor en `03_PROVEEDORES/`.

## nuevo

1. Pide al usuario el correo pegado o el relato de la llamada, si no lo dio ya.
2. **Busca similares** antes de proponer nada: `grep -ril` sobre `02_TICKETS/` por las palabras clave del síntoma, y por `sintoma:`/`solucion_corta:` en el frontmatter; también en `00_REFERENCIA_TECNICA/` por el nombre del job, tabla, informe o interfaz. Muestra hasta cinco coincidencias con una línea cada una: id, síntoma, solución corta o ficha.
3. Propón los campos: asunto breve (≤ 60 caracteres), `prioridad`, `origen`, `referencia_origen` (asunto del correo tal cual o "reunión X AAAA-MM-DD"), `responsable`, `categoria`, `entorno`, `sintoma` (una línea) y el texto del `## Resumen` y de la primera entrada del histórico, ya anonimizados. Pregunta con AskUserQuestion; los campos de lista como opciones.
4. Tras confirmar: `python3 05_GENERAL/Herramientas/nuevo_ticket.py "Asunto" <prioridad> <origen>` y rellena en el fichero creado los campos confirmados con Edit. En `referencias_tecnicas` pon las fichas de `00_` que salieron en la búsqueda si son relevantes.
5. Ejecuta `python3 05_GENERAL/Herramientas/escanear_pii.py "<fichero>"` y muestra la ruta. No commitees: lo hace Obsidian Git.

## actualizar NFQBAU-NNNN

1. Localiza el fichero en `Abiertos/` o `Archivo/`. **Si está Resuelto, no lo reabras**: propón crear un ticket nuevo enlazado al anterior ("continúa el NFQBAU-NNNN, cerrado el día X") y solo reabre si la persona lo pide con esas palabras.
2. Pide la nueva interacción. Resúmela y anonimízala. Si es una aprobación o un rechazo del cliente, usa el prefijo fijo: `APROBACIÓN UAT`, `APROBACIÓN PRD` o `RECHAZO — motivo`.
3. Propón: la entrada del histórico, y si procede cambio de `estado` (según el circuito: RECHAZO → En curso; APROBACIÓN en Revisión cliente → Pendiente despliegue UAT; NTT confirma UAT → Pruebas cliente UAT; APROBACIÓN PRD → Pendiente despliegue PRD; NTT confirma PRD → sigue en ese estado hasta cerrar), cambio de `responsable`, y si hay que tocar la nota de proveedor `03_PROVEEDORES/NTT — NFQBAU-NNNN.md` (Solicitado / Ticket NTT / Desplegado).
4. Tras confirmar, edita. Escanea el fichero.

## resolver NFQBAU-NNNN

1. Lee el ticket. Si tiene `## Paquete de despliegue` con Update relleno y Rollback vacío, para: el rollback es obligatorio.
2. Pregunta los cinco bloques uno a uno, admitiendo que el usuario pegue la query o el comando tal cual: Qué se hizo · Cómo se comprobó · Con quién se habló (por rol) · Servicios, jobs o tablas tocados · Referencias técnicas usadas y por qué. Anonimiza.
3. Propón `sintoma` (si estaba vacío) y `solucion_corta`: una línea cada uno, en lenguaje llano, pensadas para que se encuentren dentro de seis meses. Propón `referencias_tecnicas` y `codigo_relacionado.version` si hubo tag.
4. Tras confirmar: escribe los bloques, `fecha_resolucion` = hoy, `estado: Resuelto`. Si hay nota de proveedor, `estado: Resuelto` también ahí. Escanea.

## consultar "síntoma"

Sin crear ni modificar nada. Para quien tiene poca experiencia y tiene que actuar.

1. Busca por las palabras del síntoma en `02_TICKETS/` (frontmatter `sintoma`, `solucion_corta`, `categoria`, y texto) y en `00_REFERENCIA_TECNICA/`. Usa varios sinónimos y el nombre técnico si lo reconoces (job, tabla, interfaz, informe).
2. Lee los tickets resueltos que encajen (máximo cinco) y las fichas relevantes.
3. Responde en lenguaje llano y en este orden: qué se hizo otras veces, con qué query o comando se comprobó (cópialo tal cual), con quién hubo que hablar (por rol), qué ficha de la referencia lo explica, y qué haría primero si fuera el usuario. Enlaza cada ticket y ficha con ruta relativa.
4. Si no hay nada parecido, dilo y sugiere por dónde empezar en la referencia técnica.

## redactar NFQBAU-NNNN

1. Lee el ticket y deduce del `estado` qué correo toca, o pregunta: **envío del paquete al cliente** (En curso → Revisión cliente), **solicitud de despliegue a NTT** (UAT o PRD), **listo para pruebas** (Pruebas cliente UAT), **cierre** (Resuelto).
2. Redacta el correo **siempre en portugués de Brasil**, al cliente y a NTT, sin preguntar idioma: asunto con `referencia_origen` y el id del ticket, cuerpo breve, sin datos de contacto, con lo que el destinatario tiene que hacer y para cuándo. Para NTT: entorno, paquete (update, rollback, informe), ventana propuesta. **Sin firma**: termina en "Atenciosamente,"; cada persona añade la suya al enviar.
3. Muéstralo en un bloque de código para copiar. No lo guardes en el vault salvo que el usuario lo pida, y entonces como entrada resumida del histórico, no el correo entero.

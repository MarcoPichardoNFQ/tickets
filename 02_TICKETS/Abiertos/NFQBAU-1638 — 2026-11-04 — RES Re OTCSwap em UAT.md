---
id: NFQBAU-1638
fecha_apertura: 2026-11-04
fecha_limite: 2026-11-04
fecha_resolucion: 2026-11-06
estado: Resuelto
prioridad: Alta
responsable: Matheus Fransoni
origen: email
referencia_origen: '"RES: Re: OTCSwap em UAT (2026-11-04)'
categoria:
  - BBDD
entorno:
  - UAT
sintoma: Confirmación y coordinación para las entregas del XSD de OTCSwap, ajuste de tabla y soporte de migración en UAT.
solucion_corta: "Duplicado: el hilo se sigue en NFQBAU-1637"
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-06 13:22
actualizado_por: Ricardo Reyes
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marco P., consultor de NFQ, responde a Fernando M., de S3 Caceis, confirmando la disponibilidad total del equipo para cumplir con la entrega de OTCSWAP antes de las 14h.
Asimismo, confirma que darán soporte en el ajuste de Portafolio (Card 6) y apoyarán a Thiago A. durante la tarde en la sala de proyectos.
Adjunta capturas.

Detalles: Entrega del nuevo XSD de OTCSwap programada antes de las 14:00h (horario Brasil); Portfólio (Card 6) - TIPO CLIENTE con requerimiento de ajuste en la tabla Investment_Company_Institute (crear patrón string / número); Corrección del Fundo Abertura para cambio de indexed_price; Elementos impeditivos/bloqueantes para la migración del fin de semana
Adjuntos del correo: image001.png, image002.png, image003.png

## Histórico de interacciones

- 2026-11-04 19:51 — Correo automático — Marco P., consultor de NFQ, responde a Fernando M., de S3 Caceis, confirmando la disponibilidad total del equipo para cumplir con la entrega de OTCSWAP antes de las 14h.
Asimismo, confirma que darán soporte en el ajuste de Portafolio (Card 6) y apoyarán a Thiago A. durante la tarde en la sala de proyectos.
Adjunta capturas.
- 2026-11-05 14:28 — Correo automático — Correo nuevo en el hilo: Marco P., Senior Consultant de NFQ, informa a Fernando M. y al equipo que los ajustes para OTCSwap en el entorno de desarrollo han sido completados con éxito. Se enviarán los objetos necesarios para su ejecución en UAT en la próxima hora. Adjunta capturas. Detalles: Ajustes finalizados en ambiente DEV para OTCSwap; Se enviarán objetos para ejecución en UAT en la próxima hora; Relacionado con la actualización del nuevo XSD de OTCSwap. · Adjuntos del correo: image001.png, image003.png, image002.png
- 2026-11-05 14:29 — Correo automático — Correo nuevo en el hilo: Fernando M., de S3 Caceis, agradece el mensaje de respuesta y propone hacer el seguimiento de la homologación en la sala de Proyectos junto a Marcos M. Adjunta capturas. Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-05 16:11 — Correo automático — Correo nuevo en el hilo: Fernando M. pregunta a Marco P. si el OTCSWAP ya está liberado para que Marcos M. pueda avanzar con las pruebas en UAT. Marco P. había informado previamente que los ajustes en DEV estaban listos y que enviarían los objetos para UAT en la siguiente hora. Adjunta capturas. Detalles: El componente OTCSWAP necesita ser liberado para pruebas en UAT. Los ajustes en el ambiente DEV ya fueron finalizados y los objetos necesarios para la ejecución en UAT serían enviados en la próxima hora. · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-05 16:17 — Correo automático — Correo nuevo en el hilo: Marcos M., tecnología de PRServiços, pregunta a Marco P., senior consultant de NFQ, por la previsión de liberación del OTCSwap en UAT. Fernando M., de S3 Caceis, había preguntado previamente si ya estaba liberado, a lo que Marco P. había respondido que los ajustes en DEV estaban listos y que los objetos para UAT se enviarían en la siguiente hora. El remitente adjunta capturas. Detalles: Se requiere la liberación del OTCSwap en UAT para que Marcos M. pueda avanzar con las pruebas; Los ajustes en DEV ya fueron finalizados y se esperaba el envío del conjunto de objetos necesarios para la ejecución en UAT; La liberación es un impedimento para la migración del fin de semana; Se menciona un nuevo XSD de OTCSwap; Se adjuntan capturas. · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-05 18:27 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador del proveedor, informa que la tarea de OTCSwap en UAT es compleja debido al volumen de cambios en tablas, funciones y jobs, y solicita una extensión del plazo de entrega hasta mañana adjunta capturas. Detalles: Interfaz OTCSwap; 4 campos nuevos en OTC; afectación en 20 tablas; alteración de lógicas de funciones para persistencia en trf; prueba de carga desde XML a través de 10 jobs diferentes; scripts construidos para 20 tablas y mapeo; actualización de archivos XML y XSD en entorno de prueba; 5 jobs probados en UAT; pendientes 4 jobs en TRF y envío a UAT; adjunta capturas image001.png, image002.png, image003.png · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-05 18:31 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador de NFQ, rectifica en este correo que los tests de los jobs se realizaron en el entorno STG en lugar de UAT. Además, solicita una ampliación del plazo de entrega para el día siguiente debido a la complejidad de la tarea. Detalles: Se han construido scripts para alteración en 20 tablas y para inserción de datos en tablas de mapeo; actualización de archivos XML y XSD; pendiente prueba de 4 jobs en TRF y envío para ejecución en UAT; adjunta capturas. · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-06 05:28 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, solicita aprobación a Marcos M. y Fernando M., responsables del proyecto en el cliente, para ejecutar cambios en UAT referentes a OTCSwap. Requiere actualizar el fichero XSD en el servidor y aplicar un script SQL en la base de datos. Adjunta capturas y ficheros. Detalles: Actualización de archivo: /nfq/XMLconversor/xsd/OTCSwap.xsd en UAT (requiere hacer copia de seguridad del fichero existente); Script SQL a ejecutar: UPDATE FULL query_otcswap.sql; Host BBDD: psqlcerdatahub01.postgres.database.cloud.corp; Objetivo: Añadir nuevos campos en tablas vinculadas a OTCSwap · Adjuntos del correo: image001.png, image002.png, image003.png, OTCSwap.xsd, UPDATE FULL query_otcswap.sql
- 2026-11-06 06:43 — Correo automático — Correo nuevo en el hilo: Kleverson B., de S3 Caceis, solicita al equipo de soporte/operaciones executar los cambios aprobados para OTCSwap en UAT. Previamente, Marco P., consultor de NFQ, solicitó la aprobación para actualizar el archivo XSD y ejecutar un script SQL tras los trabajos de desarrollo. Adjunta capturas. Detalles: Actualizar archivo OTCSwap.xsd en la ruta /nfq/XMLconversor/xsd/ en ambiente UAT (haciendo backup del existente); Ejecución de código SQL para añadir campos nuevos en 20 tablas relacionadas con OTCSwap; Host: psqlcerdatahub01.postgres.database.cloud.corp · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-06 09:08 — Correo automático — Correo nuevo en el hilo: Fernando A., S3 Caceis informa que ha pedido prioridad para la solicitud de OTCSwap y que NTT confirmó que ya está actuando en ello. Adjunta capturas. Detalles: Host BBDD: psqlcerdatahub01.postgres.database.cloud.corp; Actualización del archivo OTCSwap.xsd en la ruta /nfq/XMLconversor/xsd/; Ejecución de script SQL para adición de campos en 20 tablas relacionadas con OTCSwap · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-06 09:57 — Correo automático — Correo nuevo en el hilo: Marcos M., tecnología, informa que NTT ha realizado con éxito la actualización en el entorno UAT a las 09:37. Esta respuesta da seguimiento a la solicitud previa para aplicar cambios en esquemas y tablas de OTCSwap. Adjunta capturas. Detalles: Actualización en UAT ejecutada por NTT a las 09:37 · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-06 10:51 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador de NFQ, solicita la ejecución de un script SQL para corregir las tablas que no reflejaron los cambios durante las pruebas.
El problema se identificó tras una ejecución previa del script en el entorno de UAT.
Adjunta capturas y un fichero. Detalles: Script SQL adjunto: UPDATE FULL query_otcswap_v2.sql; Módulo/Interfaz: OTCSwap; Servidor PostgreSQL referenciado: psqlcerdatahub01.postgres.database.cloud.corp · Adjuntos del correo: image001.png, image002.png, image003.png, UPDATE FULL query_otcswap_v2.sql
- 2026-11-06 10:57 — Correo automático — Correo nuevo en el hilo: Matheus D. F., Developer III de NFQ, solicita la ejecución de un script adjunto en el ambiente UAT para corregir un problema donde las alteraciones de un script previamente ejecutado no se reflejaron en algunas tablas. Fernando A. M. J., de S3 Caceis, pide prioridad para esta solicitud. Adjunta capturas. Detalles: Se solicita ejecutar un script adjunto en UAT para corregir la falta de reflejo de cambios en tablas; Previamente, se había solicitado actualizar el archivo OTCSwap.xsd en la ruta /nfq/XMLconversor/xsd/ y ejecutar un código SQL adjunto para añadir nuevos campos en tablas relacionadas con OTCSwap; El host de la base de datos es psqlcerdatahub01.postgres.database.cloud.corp; Los cambios implican añadir 4 campos nuevos en OTC, afectando a 20 tablas, insertando datos de mapeo y alterando lógicas de funciones; Se deben probar las cargas de información desde XML a través de 10 jobs diferentes; Las capturas adjuntas son logos/firmas y no aportan detalles técnicos relevantes. · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-06 12:46 — Correo automático — Correo nuevo en el hilo: Ivan R., analista de soporte de NTT DATA, informa que se ha actualizado el archivo OTCSwap.xsd y se ha ejecutado un script SQL, como parte de la resolución del ticket S3C-23096. Adjunta capturas. Detalles: Archivo OTCSwap.xsd actualizado en la ruta /nfq/XMLconversor/xsd/; Script SQL ejecutado con éxito; Host de BBDD: psqlcerdatahub01.postgres.database.cloud.corp; Se adjuntan capturas de la actualización del archivo y la ejecución del script. · Adjuntos del correo: image001.png, image003.png, image004.png, image005.png, image006.png, image007.png
- 2026-11-06 13:12 — Ricardo Reyes — Mismo hilo que [NFQBAU-1637](../Abiertos/NFQBAU-1637%20—%202026-11-04%20—%20OTCSwap%20em%20UAT.md) ("OTCSwap em UAT"): el correo automático lo separó por el asunto. Se seguirá en el 1637.
- 2026-11-06 13:22 — Ricardo Reyes — Cerrado como duplicado del [NFQBAU-1637](../Abiertos/NFQBAU-1637%20—%202026-11-04%20—%20OTCSwap%20em%20UAT.md); el hilo sigue allí.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Se cierra como duplicado de [NFQBAU-1637](../Abiertos/NFQBAU-1637%20—%202026-11-04%20—%20OTCSwap%20em%20UAT.md). Es el mismo hilo ("OTCSwap em UAT"); el correo automático lo separó porque el asunto llegó como '"RES: Re: ...' y la comilla impedía quitar el prefijo. Corregido en correo_a_ticket.py (PR #72): las siguientes respuestas van al 1637.

### Cómo se comprobó

Mismo asunto normalizado, mismas personas y misma demanda (nuevo XSD de OTCSwap en UAT) en los dos tickets.

### Con quién se habló

Nadie: cierre administrativo del vault.

### Servicios, jobs o tablas tocados

Ninguno.

### Referencias técnicas usadas y por qué

Ninguna.

## Vencimiento

## Historial de estados
- 2026-11-04 19:52 — nuevo → Abierto — Correo automático
- 2026-11-05 12:24 — Abierto → En curso — Marco Pichardo
- 2026-11-06 05:27 — En curso → Revisión cliente — Marco Pichardo
- 2026-11-06 12:14 — nuevo → Revisión cliente — Matheus Fransoni
- 2026-11-06 13:22 — Revisión cliente → Resuelto — Ricardo Reyes

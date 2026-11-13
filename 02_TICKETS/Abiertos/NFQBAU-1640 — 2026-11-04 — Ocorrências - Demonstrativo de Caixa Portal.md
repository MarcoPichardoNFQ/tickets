---
id: NFQBAU-1640
fecha_apertura: 2026-11-04
fecha_limite: 2026-11-05
fecha_resolucion:
estado: Pendiente despliegue UAT
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: Ocorrências - Demonstrativo de Caixa Portal (2026-11-04)
categoria:
  - Qlik
entorno: [Producción, UAT]
  - Producción
sintoma: Christian S. confirma la integridad de los datos de los informes "Demonstrativo de Caixa Portal" y pregunta por los próximos pasos para la implantación en HML y PRD.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-09 20:06
actualizado_por: Correo automático
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Continúa el hilo del [NFQBAU-1535](../Abiertos/NFQBAU-1535%20—%202026-10-19%20—%20Ocorrências%20-%20Demonstrativo%20de%20Caixa%20Portal.md), cerrado el 2026-11-04: no se reabre, se crea este. Christian S., tecnología de S3CACEIS, confirma que los datos de los informes están íntegros según los tests enviados. Pregunta a Marco P., consultor de NFQ, cuáles son los próximos pasos y cuándo se puede coordinar la implantación en los entornos de homologación y producción. Marco P. había creado previamente un informe "espejo" del "Demonstrativo de Caixa" y adjuntó los resultados de los tests para su validación. Adjunta capturas.

Detalles: Informe afectado: "Demonstrativo de Caixa Portal", "relatório 'espelho' do Demonstrativo de Caixa"; Clientes de prueba: CUST4823, CUST4408, RCUS0517, CUST4903; Periodos de prueba: CUST4823: 2026-01-02 a 2026-01-30 y 2026-09-01 a 2026-09-30; CUST4408: 2026-03-01 a 2026-03-31 y 2026-10-01 a 2026-10-21; RCUS0517: 2026-05-04 a 2026-05-31 y 2026-10-01 a 2026-10-21; CUST4903: 2026-10-01 a 2026-10-21; Capturas de pantalla muestran "Progreso de carga de datos" en Qlik; Una muestra un tiempo transcurrido de 00:23:08, recuperando 9,771 líneas de `sac_qlik_cart_estat_clibas_v` y 97,716 líneas de `VistaFondos`; Otra muestra un tiempo transcurrido de 00:02:21, recuperando 5,066,874 líneas de `FATO << Demonstrativo`, 11,386,107 líneas de `FATO << Saldoss__`, 9,771 líneas de `sac_qlik_cart_estat_clibas_v` y 97,716 líneas de `VistaFondos`; Otra captura muestra una tabla con columnas "DATA", "MOMENTO EN QUE LLEGO A ALDRIN", "SALDO" con datos de ejemplo.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png

## Histórico de interacciones

- 2026-11-04 20:36 — Correo automático — Continúa el hilo del [NFQBAU-1535](../Abiertos/NFQBAU-1535%20—%202026-10-19%20—%20Ocorrências%20-%20Demonstrativo%20de%20Caixa%20Portal.md), cerrado el 2026-11-04: no se reabre, se crea este. Christian S., tecnología de S3CACEIS, confirma que los datos de los informes están íntegros según los tests enviados. Pregunta a Marco P., consultor de NFQ, cuáles son los próximos pasos y cuándo se puede coordinar la implantación en los entornos de homologación y producción. Marco P. había creado previamente un informe "espejo" del "Demonstrativo de Caixa" y adjuntó los resultados de los tests para su validación. Adjunta capturas.
- 2026-11-04 20:51 — Correo automático — Correo nuevo en el hilo: Marco P. de NFQ informa que la implantación de una optimización para el informe "Demonstrativo de Caixa Portal" tomará 10 minutos, durante los cuales el informe estará indisponible. Propone una llamada para alinear los detalles de la ejecución. Christian S. de Tecnología ya ha validado que los datos de prueba están íntegros. Adjunta capturas. Detalles: La optimización es para el informe "Demonstrativo de Caixa Portal"; La implantación durará 10 minutos y el informe estará indisponible durante ese tiempo; Los datos de prueba han sido validados como íntegros; La implantación se realizará en los ambientes de HML y PRD; Se menciona la vista `sac_qlik_cart_estat_clibas_v` y `VistaFondos` en las capturas de pantalla; Las capturas muestran el progreso de carga de datos con tiempos de 00:23:08 y 00:02:21, y una tabla de datos con fechas de 2026-10-06 a 2026-10-19 para los clientes CUST4823, CUST4408, RCUS0517, CUST4903. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image010.png, image009.png
- 2026-11-05 13:51 — Correo automático — Correo nuevo en el hilo: Christian S., tecnología, responde a Marco J.P., consultor de NFQ, proponiendo una reunión a las 18h en la sala P0 para coordinar la implantación de una optimización en el informe "Demonstrativo de Caixa Portal". Marco J.P. había solicitado una llamada para alinear los detalles de la implantación, que tomará 10 minutos y dejará el informe indisponible temporalmente. Christian S. había confirmado previamente la integridad de los datos de los tests y preguntado por los próximos pasos para la implantación en HML y PRD. Adjunta capturas. Detalles: Reporte afectado: "Demonstrativo de Caixa Portal"; Se está coordinando la implantación de una optimización; La implantación causará una indisponibilidad del reporte de 10 minutos; Los entornos de implantación son HML y PRD; Las capturas de pantalla muestran el "Progreso de carga de datos" con la finalización exitosa de la carga, tiempos de 00:23:08 y 00:02:21, y referencias a sac_qlik_cart_estat_clibas_v (QVD) y VistaFondos; Una captura muestra una tabla de datos con columnas 'DATA', 'MOMENTO EN QUE LLEGO A ALDRIN' y 'SALDO' para el periodo del 2026-10-06 al 2026-10-19; El proceso de carga de datos se completó sin errores. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png
- 2026-11-05 13:51 — Correo automático — Correo nuevo en el hilo: Christian S., tecnología de S3 Caceis, propone reunirse a las 18h para alinear los detalles de la implantación de la optimización del Demonstrativo de Caixa.
Esta reunión se agenda tras haber validado que los datos de las pruebas son íntegros.
Adjunta capturas. Detalles: Informe Demonstrativo de Caixa Portal; Vista sac_qlik_cart_estat_clibas_v; Tablas FATO, Saldoss_, VistaFondos; Captura 1 muestra log de carga de Qlik finalizada en 23:08 minutos procesando 12,032,571 líneas en FATO; Captura 2 muestra optimización de carga de Qlik finalizada en 02:21 minutos; Captura 3 muestra tabla de datos con columnas DATA, MOMENTO EN QUE LLEGO A ALDRIN y SALDO · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png
- 2026-11-05 18:46 — Correo automático — Correo nuevo en el hilo: Christian S., del equipo de tecnología del cliente, solicita agendar un horario de llamada para alinear los detalles de la implantación de la optimización en el informe Demonstrativo de Caixa Portal. La solicitud se realiza tras no haber logrado hablar durante la jornada. Adjunta capturas. Detalles: Informe affected: Demonstrativo de Caixa Portal; Vista/QVD: sac_qlik_cart_estat_clibas_v; Las capturas muestran logs de carga de Qlik Sense comparando tiempos de ejecución (23:08 min vs 02:21 min) para cargas de FATO (11.386.107 líneas), Calendar_tmp y VistaFondos (97.716 líneas); Se muestra tabla de resultados con columnas DATA, MOMENTO EN QUE LLEGO A ALDRIN y SALDO para fechas de octubre de 2026 · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png
- 2026-11-09 15:17 — Correo automático — Correo nuevo en el hilo: Christian S., del equipo de Tecnología de S3 Caceis, solicita una reunión para hoy a las 18:00 con Marco P., consultor sénior de NFQ, con el fin de coordinar la subida del cambio. Se trata del seguimiento a la optimización validada del Demonstrativo de Caixa. Detalles: Informe Demonstrativo de Caixa Portal; reunión propuesta a las 18:00 h para tratar la subida del cambio · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png
- 2026-11-09 16:42 — Correo automático — Correo nuevo en el hilo: Marco P., Senior Consultant de NFQ, confirma su disponibilidad para una reunión solicitada por Christian S., Tecnología de S3 Caceis, para hablar sobre el despliegue de una optimización. Adjunta capturas. Detalles: Adjunta capturas de pantalla de 'Progreso de carga de datos' mostrando la finalización exitosa de la carga para `sac_qlik_cart_estat_clibas_v` (9.771 líneas) y `FATO` (11.386.107 líneas), con tiempos de 00:23:08 y 00:02:21; también incluye una tabla con datos de `DATA`, `MOMENTO EN QUE LLEGÓ A ALDRIN` y `SALDO` para el periodo de 2026-10-06 a 2026-10-19, con un saldo de 5.000,01 para el 2026-10-13. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image010.png, image009.png
- 2026-11-09 16:52 — Correo automático — Correo nuevo en el hilo: Silvia A., servicios y soporte, pregunta a Christian S., tecnología, la fecha de la subida de la optimización del informe tras los correos previos sobre la validación. Adjunta capturas. Detalles: adjunta capturas; informe Demonstrativo de Caixa Portal · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png
- 2026-11-09 18:06 — Correo automático — Correo nuevo en el hilo: Marco P. de NFQ confirma a Christian S. de Tecnología su disponibilidad para una llamada sobre la subida de una optimización. Christian S. había solicitado una reunión para hablar sobre el despliegue de una solución en los entornos de HML y PRD, tras la aprobación de los tests. Marco P. había informado que la implantación de la optimización del informe 'Demonstrativo de Caixa' tardaría 10 minutos y el informe estaría indisponible. Adjunta capturas. Detalles: Se trata de una optimización para el 'Demonstrativo de Caixa Portal'. La implantación durará 10 minutos y el informe estará indisponible durante ese tiempo. Las capturas muestran el 'Progreso de carga de datos' para `sac_qlik_cart_estat_clibas_v` y `VistaFondos`, con tiempos de carga de 00:23:08 y 00:02:21, lo que sugiere una mejora de rendimiento. Una captura muestra datos de 'SALDO' con fechas. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png
- 2026-11-09 18:16 — Correo automático — APROBACIÓN — Correo nuevo en el hilo: Christian S., de Tecnología de S3 Caceis, autoriza el despliegue de una optimización en el entorno de UAT para el informe 'Demonstrativo de Caixa Portal'. Informa que realizará las pruebas en UAT y planea la subida a Producción para el miércoles de esta semana. Adjunta capturas. Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png
- 2026-11-09 18:31 — Correo automático — Correo nuevo en el hilo: Christian S., tecnología de S3 Caceis, informa a Silvia L. que el proveedor NFQ publicará hoy en UAT, realizarán pruebas mañana y esperan actualizar en Producción el miércoles, combinando la subida con el cliente para el próximo fin de semana por seguridad. Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png
- 2026-11-09 20:06 — Correo automático — Correo nuevo en el hilo: Marco P. de NFQ informa que el despliegue en UAT del informe 'Demonstrativo de Caixa Portal' comenzará en 30 minutos, tras la resolución de un incidente prioritario. Christian S. de Tecnología validará la generación del informe en UAT, y la implementación en producción está agendada para mañana por la noche. Adjunta capturas. Detalles: El deploy en UAT del informe 'Demonstrativo de Caixa Portal' se iniciará en 30 minutos; Christian C. realizará la validación de la generación del informe en UAT; La implantación en producción (PRD) está agendada para la noche de mañana; La actividad se retrasa por la resolución de un incidente prioritario en P0. Las capturas muestran el progreso de carga de datos para 'sac_qlik_cart_estat_clibas_v' y 'VistaFondos', con la carga finalizada y la app guardada con éxito; También se muestra una tabla con la columna 'dat_qlikupdate: timestamp'. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image009.png, image010.png, image008.png, image006.png, image007.png

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

### Cómo se comprobó

### Con quién se habló

### Servicios, jobs o tablas tocados

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-11-04 20:36 — nuevo → Abierto — Correo automático
- 2026-11-05 17:43 — Abierto → Revisión cliente — Marco Pichardo
- 2026-11-06 12:14 — nuevo → Revisión cliente — Matheus Fransoni
- 2026-11-09 18:16 — Revisión cliente → Pendiente despliegue UAT — Correo automático

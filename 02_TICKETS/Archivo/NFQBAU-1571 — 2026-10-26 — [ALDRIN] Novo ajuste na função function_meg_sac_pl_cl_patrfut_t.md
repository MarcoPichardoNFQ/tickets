---
id: NFQBAU-1571
fecha_apertura: 2026-10-26
fecha_limite: 2026-10-27
fecha_resolucion: 2026-10-29
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: "[ALDRIN] Novo ajuste na função function_meg_sac_pl_cl_patrfut_t (2026-10-26)"
categoria:
  - BBDD
entorno:
  - UAT
sintoma: Solicitud de validación del código ajustado de la función function_meg_sac_pl_cl_patrfut_t.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-29 10:19
actualizado_por: Matheus Fransoni
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Continúa el hilo del [NFQBAU-1524](../Abiertos/NFQBAU-1524%20—%202026-10-16%20—%20[ALDRIN]%20Novo%20ajuste%20na%20função%20function_meg_sac_pl_cl_patrfut_t.md), cerrado el 2026-10-26: no se reabre, se crea este. Marco P., consultor senior de NFQ, envía el ajuste solicitado para la función de base de datos y consulta a Thiago A. si el código cumple con lo requerido. Adjunta un fichero.

Detalles: Función: function_meg_sac_pl_cl_patrfut_t; Ficheros adjuntos: AJUSTE_function_meg_sac_pl_cl_patrfut_t.sql, BKP_function_meg_sac_pl_cl_patrfut_t.sql
Adjuntos del correo: image001.png, AJUSTE_function_meg_sac_pl_cl_patrfut_t.sql, BKP_function_meg_sac_pl_cl_patrfut_t.sql

## Histórico de interacciones

- 2026-10-26 14:47 — Correo automático — Continúa el hilo del [NFQBAU-1524](../Abiertos/NFQBAU-1524%20—%202026-10-16%20—%20[ALDRIN]%20Novo%20ajuste%20na%20função%20function_meg_sac_pl_cl_patrfut_t.md), cerrado el 2026-10-26: no se reabre, se crea este. Marco P., consultor senior de NFQ, envía el ajuste solicitado para la función de base de datos y consulta a Thiago A. si el código cumple con lo requerido. Adjunta un fichero.
- 2026-10-26 15:26 — Correo automático — Correo nuevo en el hilo: Thiago A., de desarrollo, informa a Marco J. P., consultor senior, que falta una parte del group by en la función function_meg_sac_pl_cl_patrfut_t. Marco J. P. había enviado una validación previa. Thiago A. adjunta capturas. Detalles: Función afectada: function_meg_sac_pl_cl_patrfut_t; La captura de pantalla muestra la cláusula group by; Los campos que faltan en el group by son: DAT_VALUAT, DES_OWNER, cod_dmasse, des_counter, cod_valprocs, dat_assepr · Adjuntos del correo: image001.png, image002.png
- 2026-10-26 15:31 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, pregunta a Thiago A., de PR Serviços, si el código adjunto, que contiene un ajuste a la función function_meg_sac_pl_cl_patrfut_t, atiende su solicitud. Adjunta capturas y un fichero. Detalles: Función afectada: function_meg_sac_pl_cl_patrfut_t; Problema: La función no utiliza el número de procesamiento, sino la fecha y hora, generando diferencias de segundos dentro del mismo procesamiento; Cambios solicitados: Modificar la subconsulta de trf_s3.sss_position_t para incluir cod_valprocs y dat_assepr en el SELECT y GROUP BY; Actualizar la condición ON del LEFT JOIN con trf_s3.sss_prices_t para usar pri.cod_dmasse = val.cod_dmasse AND pri.dat_price = val.dat_assepr; Thiago A. solicitó específicamente añadir DAT_VALUAT, DES_OWNER, cod_dmasse, des_counter, cod_valprocs, dat_assepr al GROUP BY; Adjunta el fichero AJUSTE_function_meg_sac_pl_cl_patrfut_t.sql con el código modificado. · Adjuntos del correo: image001.png, image002.png, AJUSTE_function_meg_sac_pl_cl_patrfut_t.sql
- 2026-10-26 15:37 — Correo automático — Correo nuevo en el hilo: Thiago A. de PR Serviços ha validado el ajuste en la función function_meg_sac_pl_cl_patrfut_t que había solicitado previamente. Marco P. de NFQ había pedido la validación del código. La solicitud original de Thiago A. era para corregir un problema en producción relacionado con una diferencia de segundos en el procesamiento, cambiando cómo se obtiene el número de procesamiento. Adjunta capturas. Detalles: Función afectada: function_meg_sac_pl_cl_patrfut_t; Problema original: diferencia de segundos dentro del mismo procesamiento; Cambio: la función ahora toma el número de procesamiento en lugar de la fecha y hora de procesamiento; Tablas involucradas: trf_s3.sss_position_t, trf_s3.sss_prices_t; Campos modificados en el group by y select de la subconsulta 'val': se reemplaza DAT_UPDATE por cod_valprocs y dat_assepr; Campo modificado en el left join: pri.dat_price = val.dat_valuat cambia a pri.dat_price = val.dat_assepr · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-10-26 15:56 — Correo automático — Correo nuevo en el hilo: Marco P., Senior Consultant de NFQ, pregunta si se debe enviar a UAT el ajuste de la función function_meg_sac_pl_cl_patrfut_t. Thiago A., de PR Serviços, había validado previamente el código. Detalles: Se solicita ajustar la función function_meg_sac_pl_cl_patrfut_t para que tome el número de procesamiento en lugar de la fecha y hora de procesamiento. La modificación implica cambiar la cláusula GROUP BY y la condición de JOIN en las tablas trf_s3.sss_position_t y trf_s3.sss_prices_t. Específicamente, se reemplaza DAT_UPDATE por cod_valprocs y dat_assepr en el GROUP BY, y dat_price = val.dat_valuat por pri.dat_price = val.dat_assepr en el JOIN. Se adjuntan capturas. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-10-26 16:11 — Correo automático — Correo nuevo en el hilo: Thiago A., de PR Serviços, confirma que la validación del ajuste de la función ha sido exitosa y solicita que se suba a UAT. Marco P., consultor, había preguntado previamente si el código cumplía con la solicitud y si se podía enviar a UAT. Detalles: Función afectada: function_meg_sac_pl_cl_patrfut_t; La alteración debe usar el número de procesamiento en lugar de la fecha y hora de procesamiento; Se identificó que faltaba parte del group by; Los campos del group by que se debían incluir son: DAT_VALUAT, DES_OWNER, cod_dmasse, des_counter, cod_valprocs, dat_assepr; Tablas involucradas: trf_s3.sss_position_t, trf_s3.sss_prices_t; adjunta capturas. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-10-26 17:56 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, solicita ayuda para compilar en UAT un script de ajuste para una función de base de datos. Señala que Marcos M., de PR Servicios, puede autorizar la ejecución según las directrices establecidas. Adjunta capturas y ficheros. Detalles: Función: function_meg_sac_pl_cl_patrfut_t; Host: psqlcerdatahub01.postgres.database.cloud.corp; Archivos adjuntos: AJUSTE_function_meg_sac_pl_cl_patrfut_t.sql y BKP_function_meg_sac_pl_cl_patrfut_t.sql; La captura de pantalla muestra un correo que confirma que miembros del equipo s3 (Meneses, Ado, Ricardo o David) pueden aprobar despliegues a UAT · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image.png, BKP_function_meg_sac_pl_cl_patrfut_t.sql, AJUSTE_function_meg_sac_pl_cl_patrfut_t.sql
- 2026-10-26 21:21 — Correo automático — Correo nuevo en el hilo: Reinaldo R., del equipo de soporte de NTT Data, notifica la referencia del ticket S3C-22930 para aplicar el ajuste de una función en el entorno UAT.
Se indica la validación previa del script y se adjunta capturas de la ejecución en la base de datos. Detalles: Ticket S3C-22930; Función: trf_s3.function_meg_sac_pl_cl_patrfut_t(); Host: psqlcerdatahub01.postgres.database.cloud.corp; Captura muestra ejecución exitosa de CREATE OR REPLACE FUNCTION en 616 ms · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image.png, image.png, image.png
- 2026-10-28 16:12 — Correo automático — Correo nuevo en el hilo: Thiago A., de PR Serviços, solicita la promoción a Producción de la función `function_meg_sac_pl_cl_patrfut_t` tras haber sido validada en UAT. Anteriormente, Marco P., de NFQ, había solicitado la compilación del código en UAT. El correo adjunta capturas. Detalles: Nombre de la función: `function_meg_sac_pl_cl_patrfut_t`; Host de BBDD: `psqlcerdatahub01.postgres.database.cloud.corp`; Se adjunta captura de pantalla mostrando la ejecución exitosa de `DROP OR REPLACE FUNCTION trf_s3.function_meg_sac_pl_cl_patrfut_t()` en PostgreSQL; Se adjunta captura de pantalla con dos tablas de datos (`cod_cli`, `dat_calc_patr`, `dat_futiv`, `amt_cotac`, `amt_prec_ment`, `amt_valor`); Se adjunta un email de Kleverson B. indicando que Marcos M., Ado G., Ricardo R. o David pueden aprobar ejecuciones en UAT. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png
- 2026-10-28 20:15 — Correo automático — Correo nuevo en el hilo: Deborah B., desarrolladora de NFQ, añade al equipo de soporte a la conversación y envía el código de la función modificada. No realiza una petición adicional más allá de incorporar al equipo al seguimiento del pase. Adjunta un fichero. Detalles: Sistema ALDRIN; Función: trf_s3.function_meg_sac_pl_cl_patrfut_t(); Motivo: ajuste por diferencia de segundos dentro del mismo procesamiento; Host PRD: psqlprddatahub03.postgres.database.cloud.corp; Host UAT: psqlcerdatahub01.postgres.database.cloud.corp; Tickets de referencia: NFQBAU1571, S3C-22930; Ficheros: AJUSTE_function_meg_sac_pl_cl_patrfut_t.sql, BKP_function_meg_sac_pl_cl_patrfut_t.sql · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, BKP_function_meg_sac_pl_cl_patrfut_t.sql, AJUSTE_function_meg_sac_pl_cl_patrfut_t.sql
- 2026-10-29 08:46 — Correo automático — Correo nuevo en el hilo: Kleverson B., de Tecnología en S3 Caceis, da su aprobación para ejecutar el cambio SQL en el entorno de producción.
Responde a la solicitud de autorización para aplicar el ajuste en la función tras haber sido validada previamente en UAT. Detalles: Host: psqlprddatahub03.postgres.database.cloud.corp; Sistema: ALDRIN; Función: function_meg_sac_pl_cl_patrfut_t(); Ticket ID: NFQBAU1571 (referencia previa S3C-22930); Motivo: ajuste de la diferencia de segundos dentro del mismo procesamiento; Esquema: trf_s3; Tiempo estimado de rollback: 30 minutos mediante script ROLLBACK · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png, image011.png
- 2026-10-29 08:47 — Correo automático — Correo nuevo en el hilo: Kleverson B., del área de Tecnología de S3 Caceis, da su conformidad formal para proceder con la ejecución del script en producción. Esta aprobación autoriza la subida del ajuste técnico en base de datos previamente validado en UAT. Detalles: Host: psqlprddatahub03.postgres.database.cloud.corp; Sistema: ALDRIN; Función: function_meg_sac_pl_cl_patrfut_t; Tickets asociados: NFQBAU1571, S3C-22930; Motivo del cambio: corregir diferencia de segundos dentro del mismo procesamiento; Plan de rollback: ejecución de script que recompila la versión anterior (tiempo estimado 30 min); Adjunta capturas que muestran la comparativa de datos de las tablas sss_position_t(+) y sac_pl_cl_patrfut_t en UAT, la compilación correcta de la función trf_s3.function_meg_sac_pl_cl_patrfut_t() en PostgreSQL y un correo sobre el circuito de aprobaciones · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png, image011.png
- 2026-10-29 08:47 — Correo automático — Correo nuevo en el hilo: Kleverson B., del área de Tecnología de S3 Caceis, da su visto bueno formal ("De acordo") para proceder con la ejecución del script SQL en el entorno de producción. Esto autoriza el despliegue del ajuste de base de datos previamente solicitado y validado. Detalles: Host: psqlprddatahub03.postgres.database.cloud.corp; Función: function_meg_sac_pl_cl_patrfut_t; Sistema: ALDRIN; Ticket ID: NFQBAU1571; Ticket UAT: S3C-22930; Esquema: trf_s3; Se menciona la ejecución del archivo UPDATE y plan de contingencia mediante ROLLBACK; Las capturas muestran consultas comparativas en tablas sac_pl_cl_patrfut_t y sss_position_t, y la compilación exitosa de la función en PostgreSQL · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png, image011.png

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
- 2026-10-26 14:47 — (vacío) → Abierto — Correo automático
- 2026-10-26 17:26 — Abierto → Pendiente despliegue UAT — Marco Pichardo
- 2026-10-29 10:19 — Pendiente despliegue UAT → Resuelto — Matheus Fransoni

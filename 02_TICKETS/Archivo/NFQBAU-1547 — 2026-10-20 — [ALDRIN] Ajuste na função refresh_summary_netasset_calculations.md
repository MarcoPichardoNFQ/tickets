---
id: NFQBAU-1547
fecha_apertura: 2026-10-20
fecha_limite: 2026-10-21
fecha_resolucion: 2026-10-26
estado: Resuelto
prioridad: Media
responsable: Deborah Bertoldo
origen: email
referencia_origen: '[ALDRIN] Ajuste na função "refresh_summary_netasset_calculations" (2026-10-20)'
categoria:
  - BBDD
entorno: []
sintoma: La función de base de datos 'refresh_summary_netasset_calculations' necesita ser modificada para incluir nuevos campos en la tabla 'summary_netasset_calculations'.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-26 17:25
actualizado_por: Marco Pichardo
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marcos M., Tecnología, solicita un ajuste en la función 'refresh_summary_netasset_calculations' para incorporar cuatro nuevos campos en la tabla 'NFQ' que serán utilizados por una API para SAM. Deborah Y., Matheus D., y Marco P. están informados. Marcela Y. está relacionada con el ajuste de la tabla. Adjunta capturas.

Detalles: Función a ajustar: 'trf_s3.refresh_summary_netasset_calculations'; Tabla afectada: 'trf_s3.summary_netasset_calculations'; Nuevos campos a añadir: 'vl_cotas_resgatar_mx', 'vl_cotas_emitir_mx', 'vl_pl_bruto_mx', 'vl_cota_bruta_mx'; El correo incluye el código SQL completo para la nueva versión de la función; La captura de pantalla muestra una consulta SQL con los nuevos campos y sus valores (15.487.787, 500, 51.226.736.497,95, 13.480,72013104 respectivamente) para 'cod_fund' CUST3458 y 'dat_generation' 2026-07-16; Las tablas 'trf_s3.SSS_NETASSET_VALUE_T' y 'trf_s3.SSS_NETASSETVALUE_GA_T' son utilizadas en la función; La tabla 'SAC_CL_PATR' es mencionada como la tabla de NFQ a ser utilizada en el mapeo.
Adjuntos del correo: image005.png, image006.png, image007.png, image001.png

## Histórico de interacciones

- 2026-10-20 15:50 — Correo automático — Marcos M., Tecnología, solicita un ajuste en la función 'refresh_summary_netasset_calculations' para incorporar cuatro nuevos campos en la tabla 'NFQ' que serán utilizados por una API para SAM. Deborah Y., Matheus D., y Marco P. están informados. Marcela Y. está relacionada con el ajuste de la tabla. Adjunta capturas.
- 2026-10-20 22:16 — Correo automático — Correo nuevo en el hilo (era el NFQBAU-1552): Marco Jesus P., consultor senior en NFQ, pregunta si el código implementado en la función cumple con la solicitud de ajuste. Adjunta capturas y un fichero.
- 2026-10-21 11:41 — Correo automático — Correo nuevo en el hilo (era el NFQBAU-1556): Marcos M., de Tecnología, confirma que el código ha sido validado correctamente. Solicita a Deborah Yohana B. y Marco P. pedir a NTT la actualización en el entorno de UAT.
- 2026-10-21 16:26 — Correo automático — Correo nuevo en el hilo (era el NFQBAU-1557): Marco P. de NFQ solicita al equipo de soporte que compile un código SQL adjunto en el entorno UAT para la función 'refresh_summary_netasset_calculations'. Marcos M. de PR Serviços ha validado el código y Kleverson B. de S3 ha indicado que Marcos M. puede aprobar las ejecuciones en UAT. Adjunta capturas y un fichero.
- 2026-10-21 17:01 — Correo automático — Correo nuevo en el hilo (era el NFQBAU-1560): Reinaldo R. de NTT DATA reenvía la solicitud de Marco J. P. de NFQ para compilar un código adjunto en UAT, confirmando el ticket S3C-22839. El código, que ajusta la función refresh_summary_netasset_calculations, ya fue validado por Marcos M. de PR Serviços. Se adjuntan capturas.
- 2026-10-21 17:46 — Correo automático — Correo nuevo en el hilo (era el NFQBAU-1561): Marcos M., Tecnología, informa que la prueba de la función "refresh_summary_netasset_calculations" ha sido exitosa en UAT. Solicita la aprobación y actualización de esta función en Producción. Adjunta capturas.
- 2026-10-21 17:51 — Correo automático — Correo nuevo en el hilo (era el NFQBAU-1562): Marco P. de NFQ solicita la aprobación para desplegar un ajuste en la función `refresh_summary_netasset_calculations` en Producción. El ajuste fue solicitado por Marcos M. de S3 y ya fue probado con éxito en UAT. El cambio es para añadir 4 campos nuevos a una tabla utilizada por una API para SAM. Adjunta capturas y dos ficheros SQL.
- 2026-10-21 17:51 — Correo automático — Correo nuevo en el hilo (era el NFQBAU-1563): Kleverson B., del equipo de tecnología de S3 Caceis, da su conformidad para realizar el despliegue en producción solicitado previamente.

Nota: los tickets siguientes nacieron del mismo hilo por un fallo del emparejado (asuntos con comillas) y se han fusionado aquí.

**NFQBAU-1552** (fusionado el 2026-10-22):

Marco Jesus P., consultor senior en NFQ, pregunta si el código implementado en la función cumple con la solicitud de ajuste. Adjunta capturas y un fichero.

Detalles: Función: trf_s3.refresh_summary_netasset_calculations(); Tablas: trf_s3.summary_netasset_calculations, trf_s3.SSS_NETASSET_VALUE_T, trf_s3.sss_supervision_ex_t, trf_s3.SSS_NETASSETVALUE_GA_T; Campos nuevos para API SAM: vl_cotas_resgatar_mx, vl_cotas_emitir_mx, vl_pl_bruto_mx, vl_cota_bruta_mx; adjunta un fichero; adjunta capturas mostrando el resultado de la consulta SQL con los nuevos campos para cod_fund CUST3458 y dat_generation 2026-07-16.
Adjuntos del correo: image005.png, image006.png, image007.png, image001.png, ajuste_refresh_summary_netasset_calculations.sql

**NFQBAU-1556** (fusionado el 2026-10-22):

Marcos M., de Tecnología, confirma que el código ha sido validado correctamente. Solicita a Deborah Yohana B. y Marco P. pedir a NTT la actualización en el entorno de UAT.

Detalles: Función: trf_s3.refresh_summary_netasset_calculations(); Código validado con éxito; Se requiere solicitar a NTT la actualización en el entorno de UAT
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png

**NFQBAU-1557** (fusionado el 2026-10-22):

Marco P. de NFQ solicita al equipo de soporte que compile un código SQL adjunto en el entorno UAT para la función 'refresh_summary_netasset_calculations'. Marcos M. de PR Serviços ha validado el código y Kleverson B. de S3 ha indicado que Marcos M. puede aprobar las ejecuciones en UAT. Adjunta capturas y un fichero.

Detalles: Se adjunta el código SQL para la función `trf_s3.refresh_summary_netasset_calculations()`; El host de la base de datos es `psqlcerdatahub01.postgres.database.cloud.corpn`; La captura de pantalla muestra datos de la tabla `sss_netassetvalue_ga` para `CUST3458` con fecha `2026-07-16`, incluyendo valores de cotas y patrimonio; Otra captura de pantalla muestra un correo de Kleverson B. indicando que Marcos M., Ado, Ricardo o David pueden aprobar en UAT.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image.png, ajuste_refresh_summary_netasset_calculations.sql

**NFQBAU-1560** (fusionado el 2026-10-22):

Reinaldo R. de NTT DATA reenvía la solicitud de Marco J. P. de NFQ para compilar un código adjunto en UAT, confirmando el ticket S3C-22839. El código, que ajusta la función refresh_summary_netasset_calculations, ya fue validado por Marcos M. de PR Serviços. Se adjuntan capturas.

Detalles: La función a ajustar es trf_s3.refresh_summary_netasset_calculations; Implica truncar y rellenar la tabla trf_s3.summary_netasset_calculations; El host de la base de datos es psqlcerdatahub01.postgres.database.cloud.corpn; Se adjuntan capturas de pantalla que muestran el código SQL de la función, la ejecución exitosa de la creación de la función, y una tabla de resultados con datos como cod_fund, dat_generation, vl_cotas_resgatar_mx, vl_cotas_emitir_mx, vl_pl_bruto_mx, vl_cota_bruta_mx; Kleverson B. de S3 Caceis indica que Marcos M., Ado G., Ricardo o David pueden aprobar ejecuciones en UAT; El ticket asociado es S3C-22839.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image.png, image.png, image.png

**NFQBAU-1561** (fusionado el 2026-10-22):

Marcos M., Tecnología, informa que la prueba de la función "refresh_summary_netasset_calculations" ha sido exitosa en UAT. Solicita la aprobación y actualización de esta función en Producción. Adjunta capturas.

Detalles: Función afectada: refresh_summary_netasset_calculations; Host: psqlcerdatahub01.postgres.database.cloud.corpn; La función realiza un DROP FUNCTION, CREATE OR REPLACE FUNCTION, Truncate table trf_s3.summary_netasset_calculations y un Insert into trf_s3.summary_netasset_calculations; Las capturas muestran el código SQL de la función y una tabla con datos de sss_netassetvalue_uat_qr para CUST3458 con dat_generation 2026-07-16.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png

**NFQBAU-1562** (fusionado el 2026-10-22):

Marco P. de NFQ solicita la aprobación para desplegar un ajuste en la función `refresh_summary_netasset_calculations` en Producción. El ajuste fue solicitado por Marcos M. de S3 y ya fue probado con éxito en UAT. El cambio es para añadir 4 campos nuevos a una tabla utilizada por una API para SAM. Adjunta capturas y dos ficheros SQL.

Detalles: Host de Producción: `psqlprddatahub03.postgres.database.cloud.corp`; Sistema: ALDRIN; Función afectada: `refresh_summary_netasset_calculations`; Tablas relacionadas: `trf_s3_summary_netasset_calculations`, `SAC_CL_PATR`, `cart_pos_fu_t`; Motivo: Ajuste para grabar 4 campos nuevos que serán utilizados por API para SAM; Tipo de cambio: Lógica; Tiempo de rollback estimado: 30 minutos; Responsables de prueba: Marcos M. (S3) para funcional, Marcos M. (S3) y Marco P. (NFQ) para técnico; Plan de rollback: Ejecución de código de la versión anterior (adjunto `bkp_refresh_summary_netasset_calculations.sql`); Archivo para despliegue: `ajuste_refresh_summary_netasset_calculations.sql`; Captura `image001.png` muestra una consulta SQL de validación de datos para `CUST3458` con columnas como `vl_totfi`, `vl_cotas_resgatar_mx`, `vl_pl_bruto_mx`; Captura `image002.png` muestra la ejecución exitosa de un script SQL para `DROP FUNCTION`, `CREATE OR REPLACE FUNCTION trf_s3.refresh_summary_netasset_calculations()`, `Truncate table trf_s3.summary_netasset_calculations;` e `Insert into trf_s3.summary_netasset_calculations`; Captura `image003.png` muestra un correo de Kleverson B. indicando que Marcos M., Ado G., Ricardo C. o David pueden aprobar en UAT.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, ajuste_refresh_summary_netasset_calculations.sql, bkp_refresh_summary_netasset_calculations.sql

**NFQBAU-1563** (fusionado el 2026-10-22):

Kleverson B., del equipo de tecnología de S3 Caceis, da su conformidad para realizar el despliegue en producción solicitado previamente.
Adjunta capturas.

Detalles: HOST: psqlprddatahub03.postgres.database.cloud.corp; Función afectada: refresh_summary_netasset_calculations; Tabla: trf_s3.summary_netasset_calculations (cart_pos_fu_t); Modificación: grabar 4 campos nuevos para API SAM; Tiempo de rollback: 30 minutos
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png
- 2026-10-22 17:36 — Correo automático — Correo nuevo en el hilo: Marcos M., del área de tecnología, solicita la modificación de una función de base de datos. Requiere agregar el cálculo del campo 'vl_totoutros' en la tabla 'trf_s3.summary_netasset_calculations' para ser utilizado en el mapeo de SAC_CL_PATR. Adjunta capturas. Detalles: Función afectada: refresh_summary_netasset_calculations; Tabla a modificar: trf_s3.summary_netasset_calculations; Nuevo campo: vl_totoutros; Fórmulas/Lógica SQL: max(J. RECEIVABLE) - max(I. PAYABLE) + SUM(I6. FEES, I5. TAX, I11. PENDING CASH MOVEMENT, N. PFEE, O. PFEE ON REDEMPTION, L. ADJUSTMENT Type 2 si amt_tot < 0); Mapeo destino: SAC_CL_PATR; Captura de pantalla muestra consulta a la tabla/vista sss_netassetvalue_ga_t visualizando la columna vl_totoutros para el fondo CUST3458 · Adjuntos del correo: image002.png, image003.png, image004.png, image001.png
- 2026-10-22 19:01 — Correo automático — Correo nuevo en el hilo: Marco P., de NFQ, solicita compilar el código adjunto en UAT. Kleverson B. ha indicado que Marcos M. puede aprobar las ejecuciones en UAT. La petición original de Marcos M. es ajustar la función 'refresh_summary_netasset_calculations' para añadir la columna 'vl_totoutros' a la tabla 'trf_s3.summary_netasset_calculations'. Adjunta capturas y un fichero SQL. Detalles: Función afectada: 'refresh_summary_netasset_calculations'; Tabla afectada: 'trf_s3.summary_netasset_calculations'; Se añade la columna 'vl_totoutros' con una lógica de cálculo específica; Host: psqlcerdatahub01.postgres.database.cloud.corp; Adjunta el fichero 'UPDATE_REFRESH_SUMMARY.sql' con el código a compilar; Una captura muestra una tabla con la columna 'vl_totoutros' ya presente; Otra captura es un correo de Kleverson B. sobre el proceso de aprobación en UAT. · Adjuntos del correo: image002.png, image003.png, image004.png, image001.png, image.png, UPDATE_REFRESH_SUMMARY.sql
- 2026-10-22 19:31 — Correo automático — Correo nuevo en el hilo: Ado S. de PR Serviços confirma su acuerdo para la compilación en UAT. Previamente, Marco P. de NFQ y Enrique T. de NFQ solicitaron compilar el código adjunto en UAT, que ajusta la función 'refresh_summary_netasset_calculations' para añadir el campo 'vl_totoutros' en la tabla 'trf_s3.summary_netasset_calculations', según lo solicitado por Marcos M. Adjunta capturas. Detalles: Función a ajustar: 'refresh_summary_netasset_calculations'; Tabla afectada: 'trf_s3.summary_netasset_calculations'; Cambio: Añadir el campo 'vl_totoutros' en la tabla 'trf_s3.summary_netasset_calculations' y modificar la lógica de inserción para calcularlo; Host de la base de datos: 'psqlcerdatahub01.postgres.database.cloud.corp'; Código SQL para el cambio (se muestra la estructura 'Insert into ...' con la adición de 'vl_totoutros' y su cálculo); Aprobación: Kleverson B. indicó que Marcos M., Ado S., Ricardo o David pueden aprobar ejecuciones en UAT, y Ado S. ha dado su aprobación; Capturas: Una captura muestra una tabla con el campo 'vl_totoutros' ya presente y datos de ejemplo; otra captura es un correo de Kleverson B. explicando el proceso de aprobación para UAT. · Adjuntos del correo: image002.png, image003.png, image004.png, image001.png, image.png, image.png, image.png, image.png
- 2026-10-22 22:26 — Correo automático — Correo nuevo en el hilo: Luiz C., técnico de operaciones de NTT DATA, informa de que la compilación solicitada en el entorno de UAT ha sido ejecutada correctamente bajo la referencia S3C-22868. Adjunta capturas. Detalles: Ticket/referencia: S3C-22868; Función: refresh_summary_netasset_calculations; Host: psqlcerdatahub01.postgres.database.cloud.corp; Captura de pgAdmin/DBeaver en adminpsqlcerdatahub02@psqlcerdatahub01-admin ejecutando CREATE FUNCTION con mensaje 'Query returned successfully in 312 msec' · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png
- 2026-10-23 11:19 — Correo automático — Correo nuevo en el hilo: Marcos M., del área de Tecnología, consulta al equipo de soporte si hay alguna novedad respecto a la solicitud enviada por NFQ la noche anterior. Detalles: Función: refresh_summary_netasset_calculations · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png
- 2026-10-23 12:20 — Correo automático — Correo nuevo en el hilo: Marcos M., de tecnología del cliente, consulta si NFQ solicitó actualizar la función "function_meg_sac_cl_patr" el día anterior después de las 18:00h.
Esto surge tras recibir confirmación de la ejecución de un ajuste previo en la base de datos. Detalles: Función consultada: function_meg_sac_cl_patr; Función del hilo: refresh_summary_netasset_calculations; Host: psqlcerdatahub01.postgres.database.cloud.corp; Referencia de ejecución: S3C-22868; Tabla implicada en las capturas: trf_s3.SSS_NETASSETVALUE_GA_T; Código de fondo mostrado en captura: CUST3458 con fecha de generación 2026-07-16; Captura muestra ejecución exitosa de CREATE FUNCTION en 312 ms · Adjuntos del correo: image001.png, image002.png, image003.png, image006.png, image007.png, image008.png, image009.png
- 2026-10-23 12:31 — Correo automático — Correo nuevo en el hilo: Marcos M., del área de tecnología, agradece la información facilitada por Reinaldo A., de NTT Data. Indica que ha convocado a NFQ a la sala de proyectos para aclarar lo sucedido con las actualizaciones. Adjunta capturas. Detalles: Función trf_s3.function_meg_sac_cl_patr(); función refresh_summary_netasset_calculations; tickets S3C-22844 y S3C-22868; capturas muestran la compilación y ejecución de funciones en PostgreSQL en las instancias psqlprddatah03 y psqlcerdatahub02 · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png
- 2026-10-23 12:37 — Correo automático — Correo nuevo en el hilo: Marcos M., del equipo de tecnología, agradece la información recibida e indica que ha contactado a NFQ en la sala de proyectos para aclarar lo ocurrido. No solicita ninguna acción adicional. Detalles: Función mencionada en el asunto: refresh_summary_netasset_calculations · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png
- 2026-10-23 13:36 — Correo automático — Correo nuevo en el hilo: Reinaldo A., de NTT DATA, informa a Marcos M. que únicamente encontró evidencia de la función function_meg_sac_cl_patr el miércoles 21/10 en el entorno de producción. Aclara que no se halló ningún registro o cambio reciente del día anterior. Adjunta capturas. Detalles: Función consultada: function_meg_sac_cl_patr; Función del asunto: refresh_summary_netasset_calculations; Evidencia encontrada en PRD con fecha 21/10/2026; Capturas muestran ejecución de CREATE FUNCTION en PostgreSQL para la tabla trf_s3.SSS_NETASSETVALUE_GA_T, logs de ejecución SQL y notas de aprobación · Adjuntos del correo: image001.png, image002.png, image003.png, image006.png, image007.png, image008.png, image009.png, image.png, image.png
- 2026-10-23 15:16 — Correo automático — Correo nuevo en el hilo: Reinaldo A., de NTT Data, informa que el ajuste en la función ya fue ejecutado el día anterior. Previamente, Marcos M., de tecnología, consultaba sobre el estado del despliegue en UAT solicitado a soporte. Adjunta capturas. Detalles: Función: refresh_summary_netasset_calculations; Tabla: trf_s3.summary_netasset_calculations; Campo añadido: vl_totoutros; Host: psqlcerdatahub01.postgres.database.cloud.corp; Referencia de ejecución: S3C-22868; Las capturas muestran la ejecución correcta de la sentencia CREATE FUNCTION en PostgreSQL via pgAdmin y el resultado de la consulta en la tabla · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image.png, image.png

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
- 2026-10-20 15:50 — (vacío) → Abierto — Correo automático
- 2026-10-21 01:29 — Abierto → Revisión cliente — Marco Pichardo
- 2026-10-26 17:25 — Revisión cliente → Resuelto — Marco Pichardo

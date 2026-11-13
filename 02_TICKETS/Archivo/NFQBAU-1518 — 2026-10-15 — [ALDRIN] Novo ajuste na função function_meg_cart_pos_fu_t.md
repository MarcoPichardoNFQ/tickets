---
id: NFQBAU-1518
fecha_apertura: 2026-10-15
fecha_limite: 2026-10-16
fecha_resolucion: 2026-10-26
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: "Fwd: [ALDRIN] Novo ajuste na função function_meg_cart_pos_fu_t (2026-10-16)"
categoria: []
entorno:
  - UAT
sintoma: La función function_meg_cart_pos_fu_t en producción no carga ciertos datos debido a una discrepancia de segundos.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-26 13:53
actualizado_por: Ricardo Reyes
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Correo automático'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marco P., consultor senior, reenvía una solicitud de Thiago A. para registrar y atender la modificación urgente de una función en producción que presenta fallos de carga por diferencias de segundos.

## Histórico de interacciones

- 2026-10-15 20:45 — Correo automático — Marco P., consultor senior, reenvía una solicitud de Thiago A. para registrar y atender la modificación urgente de una función en producción que presenta fallos de carga por diferencias de segundos.
- 2026-10-16 11:12 — Correo automático — Correo nuevo en el hilo: Thiago A., desarrollo de aplicaciones, confirma a Marco P., consultor senior, que el código propuesto para ajustar la función "function_meg_cart_pos_fu_t()" atiende la solicitud. Adjunta capturas.
- 2026-10-20 19:36 — Correo automático — Correo nuevo en el hilo: Thiago A., del equipo de Sancac, solicita un ajuste en la función 'function_meg_cart_pos_fu_t ()'. La modificación consiste en utilizar el número de procesamiento en lugar de la fecha y hora de procesamiento para corregir diferencias de segundos. Adjunta un fichero. Detalles: Función a ajustar: 'function_meg_cart_pos_fu_t ()'; El cambio implica usar 'cod_valprocs' en lugar de 'DAT_UPDATE' para el número de procesamiento; Tablas involucradas: 'trf_s3.sss_position_t', 'trf_s3.SSS_ASSET_T'; Las condiciones de filtrado incluyen 'COD_TYPEAS in ('Future', 'Option')' y 'COD_FLAG_MAPEO is null'; Se modifica la cláusula 'group by' y la condición del 'inner join'; Se introduce una función 'row_number()' para seleccionar el registro más reciente por 'DES_OWNER, DAT_VALUAT'. · Adjuntos del correo: image001.png
- 2026-10-20 20:11 — Correo automático — Correo nuevo en el hilo: Thiago A., de PR Serviços, solicita un ajuste en la función function_meg_cart_pos_fu_t para corregir una diferencia de segundos en el procesamiento. Marco P., Senior Consultant de NFQ, confirma que la solicitud se tratará con el ticket NFQBAU1518. Adjunta capturas. Detalles: Se solicita ajustar la función function_meg_cart_pos_fu_t; La modificación implica cambiar la lógica de procesamiento para usar cod_valprocs en lugar de DAT_UPDATE para evitar diferencias de segundos; Se proporcionan los bloques de código SQL 'De:' y 'Para:' que afectan a las tablas trf_s3.sss_position_t y trf_s3.SSS_ASSET_T; La captura de pantalla adjunta no se describe en el cuerpo del correo. · Adjuntos del correo: image001.png
- 2026-10-20 20:21 — Correo automático — Correo nuevo en el hilo: Marco P., Senior Consultant de NFQ, adjunta un fichero SQL y una captura para que se valide si el código propuesto atiende la solicitud. La solicitud original de Thiago A., de PR Serviços, era ajustar la función function_meg_cart_pos_fu_t para usar el número de procesamiento en lugar de la fecha y hora, corrigiendo diferencias de segundos. El ticket asociado es NFQBAU1518. Detalles: La función a ajustar es function_meg_cart_pos_fu_t(); El cambio consiste en usar 'cod_valprocs' en lugar de 'DAT_UPDATE' para el procesamiento; Se adjunta el fichero function_meg_cart_pos_fu_t_20261020.sql con el código propuesto; Se adjunta una captura de pantalla que es un logo; La tabla afectada es trf_s3.sss_position_t; El ticket asociado es NFQBAU1518. · Adjuntos del correo: image001.png, function_meg_cart_pos_fu_t_20261020.sql
- 2026-10-20 20:32 — Correo automático — Correo nuevo en el hilo: Thiago A., del área de desarrollo de PR Servicios, responde confirmando que el código propuesto atiende correctamente su solicitud y agradece la atención. Adjunta capturas. Detalles: Función function_meg_cart_pos_fu_t; Ticket asociado NFQBAU1518; Tablas involucradas trf_s3.sss_position_t y trf_s3.SSS_ASSET_T; La captura adjunta muestra el bloque de código SQL validado con el uso de cod_valprocs y row_number() · Adjuntos del correo: image001.png, image002.png
- 2026-10-20 20:34 — Correo automático — Correo nuevo en el hilo: Marco P., Senior Consultant de NFQ, pregunta si se debe actualizar a UAT la función function_meg_cart_pos_fu_t, después de que Thiago A., de PR Serviços, confirmara que el ajuste propuesto cumple con su solicitud. La solicitud original de Thiago A. era ajustar la función para corregir diferencias de segundos. Adjunta capturas. Detalles: La función a ajustar es function_meg_cart_pos_fu_t; El cambio implica modificar la lógica para usar cod_valprocs en lugar de DAT_UPDATE en las cláusulas group by y inner join de la tabla trf_s3.sss_position_t; El ticket asociado es NFQBAU1518; Las capturas de pantalla muestran el código SQL propuesto para la modificación de la función. · Adjuntos del correo: image001.png, image002.png
- 2026-10-20 22:16 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, solicita al equipo de soporte compilar el código adjunto en el entorno UAT. Adjunta un fichero SQL. Detalles: Host: psqlcerdatahub01.postgres.database.cloud.corp; Función afectada: function_meg_cart_pos_fu_t; Adjunta un fichero: function_meg_cart_pos_fu_t_20261020.sql y capturas de pantalla de código SQL; adjunta capturas. · Adjuntos del correo: image001.png, image002.png, image.png, function_meg_cart_pos_fu_t_20261020.sql
- 2026-10-21 12:41 — Correo automático — Correo nuevo en el hilo: Reinaldo A. (NTT DATA) confirma la existencia del ticket S3C-22836 y que la solicitud es para el entorno UAT. Marco P. (NFQ) solicitó compilar un código adjunto en UAT, que fue aprobado por Thiago A. (PR Serviços). El código es un ajuste a la función `function_meg_cart_pos_fu_t` para que utilice el número de procesamiento en lugar de la fecha y hora, resolviendo una inconsistencia de segundos. Adjunta capturas. Detalles: La función a ajustar es `function_meg_cart_pos_fu_t`. La modificación consiste en cambiar la lógica de selección de datos para usar `cod_valprocs` en lugar de `DAT_UPDATE` en la tabla `trf_s3.sss_position_t`. El host de la base de datos es `psqlcerdatahub01.postgres.database.cloud.corp`. Las capturas muestran el código SQL propuesto para la función y una ejecución exitosa de `CREATE OR REPLACE FUNCTION trf_s3.function_meg_cart_pos_fu_t()` en PostgreSQL. Otra captura muestra que Kleverson B. (S3) indica que cualquier persona de S3 puede aprobar ejecuciones en UAT, mencionando a Marcos M., Ado G., Ricardo o David. · Adjuntos del correo: image001.png, image002.png, image.png, image.png, image.png
- 2026-10-21 14:17 — Correo automático — Correo nuevo en el hilo: Thiago A. solicita a Kleverson B. la aprobación para desplegar en Producción un ajuste en la función function_meg_cart_pos_fu_t. El código ya fue compilado y validado en UAT, según confirman Reinaldo R. y Thiago A. La solicitud original de Marco J. P. F. era compilar el código en UAT y Marcos A. B. M. podía aprobar las ejecuciones en UAT. Thiago A. adjunta capturas. Detalles: La función a ajustar es function_meg_cart_pos_fu_t(); La alteración consiste en tomar el número de procesamiento en lugar de la fecha y hora, para ajustar diferencias de segundos dentro del mismo procesamiento; El host de la base de datos es psqlcerdatahub01.postgres.database.cloud.corp; El código fue compilado en psqlcerdatahub02; Se menciona el ticket S3C-22836 y NFQBAU1518; Adjunta capturas que muestran la ejecución exitosa de CREATE OR REPLACE FUNCTION trf_s3.function_meg_cart_pos_fu_t() y una consulta a trf_s3.cart_pos_fu_t. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png
- 2026-10-21 14:27 — Correo automático — Correo nuevo en el hilo: Kleverson B. da su aprobación para subir a producción un ajuste en la función `function_meg_cart_pos_fu_t`. Thiago A. había confirmado la validación en UAT y solicitado la aprobación para el despliegue. Previamente, Marco P. pidió compilar el código en UAT, con la aprobación de Marcos A. M. Adjunta capturas. Detalles: Función: function_meg_cart_pos_fu_t; Host: psqlcerdatahub01.postgres.database.cloud.corp; Tickets relacionados: S3C-22836, NFQBAU1518; Captura 1: Muestra una consulta SQL 'select * from trf_s3.cart_pos_fu_t where cod_cli = 'CUST4537'' con resultados tabulares; Captura 2: Muestra la creación o reemplazo de la función trf_s3.function_meg_cart_pos_fu_t en postgres/adminsqlcerdatahub02/postgresqlcerdatahub01, con el mensaje 'Query returned successfully in 332 msec.'; Captura 3: Correo de Kleverson B. indicando que 'cualquier persona de s3 puede aprobar, pero necesitamos aprobación. Meneses, Ado, Ricardo o David pueden aprobar para UAT'. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png
- 2026-10-21 17:06 — Correo automático — Correo nuevo en el hilo: Marco P. de NFQ ha enviado los detalles para un ajuste en la función function_meg_cart_pos_fu_t, solicitado por Thiago A. de PRServicos. Este ajuste afecta a la tabla trf cart_pos_fu_t en el sistema ALDRIN. Adjunta capturas y ficheros SQL para la actualización y el rollback. Detalles: Host de la base de datos: psqlprddatahub03.postgres.database.cloud.corp; Función a ajustar: function_meg_cart_pos_fu_t; Tabla cargada por la función: trf cart_pos_fu_t; Sistema afectado: ALDRIN; Tipo de ajuste: Lógica; Fecha y hora de aplicación prevista: 2026-10-21 19:00; Impacto en cliente y otros sistemas: Sí; Tiempo de rollback estimado: 30 minutos; Plan de rollback: Ejecución de código que compila la versión anterior a la modificación (adjunta); No se espera indisponibilidad; Archivos SQL adjuntos para la actualización (function_meg_cart_pos_fu_t_20261020.sql) y rollback (bkpfunction_meg_cart_pos_rf_t_20261020.sql); Captura 1 (image001.png): Muestra una consulta SQL a la tabla cart_pos_fu_t para cod_cli = 'CUST4537', con datos desde 2025-12-19 hasta 2026-01-05; Captura 2 (image002.png): Muestra la ejecución exitosa de la sentencia CREATE OR REPLACE FUNCTION trf_s3.function_meg_cart_pos_fu_t() en un entorno PostgreSQL. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image.png, bkpfunction_meg_cart_pos_rf_t_20261020.sql, function_meg_cart_pos_fu_t_20261020.sql
- 2026-10-21 17:11 — Correo automático — Correo nuevo en el hilo: Thiago A., desarrollo de aplicaciones, envía los detalles del procedimiento para la implementación de un ajuste en la función function_meg_cart_pos_fu_t. El cambio ha sido validado en UAT y cuenta con la aprobación de Kleverson B. para su despliegue en producción. Adjunta capturas. Detalles: Descripción del cambio: Alteración de función de mapeo; Servicios afectados: Carga Megara - Aldrin; Fecha/Hora de inicio prevista: 2026-10-21 - 18:00; Plan de rollback: Volver a la versión anterior de la función; No habrá indisponibilidad; Captura 1: Muestra una consulta SQL a la tabla trf_s3.cart_pos_fu_t para el cliente 'CUST4537', con datos desde 2025-12-19 hasta 2026-01-05; Captura 2: Muestra la definición de la función trf_s3.function_meg_cart_pos_fu_t en PostgreSQL, incluyendo variables como v_dat_min, v_dat_max, v_fund, v_fund_desc, v_row_delete, v_row_count2, v_row_count_delete. · Adjuntos del correo: image002.png, image004.png, image007.png, image008.png, image009.png, image010.png
- 2026-10-21 17:31 — Correo automático — Correo nuevo en el hilo: Kleverson B., Tecnología, da su aprobación para subir a producción un ajuste en la función function_meg_cart_pos_fu_t. Thiago A., Desarrollo de Aplicaciones, había informado que la validación en UAT fue exitosa y solicitó esta aprobación. El cambio está previsto para el 21 de octubre de 2026 a las 18:00. Adjunta capturas. Detalles: Nombre de la función: function_meg_cart_pos_fu_t; Descripción del cambio: Alteración de función de mapeamento; Servicio afectado: Carga Megara - Aldrin; Fecha/Hora de inicio prevista: 2026-10-21 - 18:00; Plan de rollback: Volver a la versión anterior de la función; No habrá indisponibilidad; Área responsable: TI; Capturas muestran una consulta SELECT sobre la tabla trf_s3.cart_pos_fu_t con cod_cli = 'CUST4537' y la creación/reemplazo de la función trf_s3.function_meg_cart_pos_fu_t; Se menciona el ticket S3C-22836. · Adjuntos del correo: image001.png, image003.png, image005.png, image006.png, image011.png, image012.png, image013.png, image014.png, image015.png
- 2026-10-21 18:11 — Correo automático — Correo nuevo en el hilo: Reinaldo R., consultor de NTT Data, adjunta las evidencias de la ejecución y los datos para la implantación del ajuste en producción tras haber sido validado en UAT. Detalles: HOST: psqlprddatahub03.postgres.database.cloud.corp; Función: trf_s3.function_meg_cart_pos_fu_t; Tabla afectada: trf_s3.cart_pos_fu_t; Ticket: S3C-22841; adjunta capturas · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image.png, image.png, image.png
- 2026-10-21 18:51 — Correo automático — Correo nuevo en el hilo: Reinaldo R., consultor de NTT Data, pide que se rellenen los datos para el pase a producción de una función tras tener la aprobación de Kleverson B., cliente de S3 Caceis. Adjunta capturas. Detalles: Ticket asociado: S3C-22836; Función afectada: trf_s3.function_meg_cart_pos_fu_t; Host: psqlcerdatahub01.postgres.database.cloud.corp; Adjunta capturas con la ejecución exitosa de la función en la consola de PostgreSQL y el contenido de la tabla trf_s3.cart_pos_fu_t filtrado por el cliente CUST4537. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image.png
- 2026-10-26 13:32 — Correo automático — Correo nuevo en el hilo: Thiago A. solicita realizar un ajuste en la función de base de datos function_meg_cart_pos_fu_t para emplear la fecha de cotización correcta. Especifica los cambios a realizar en la subconsulta SQL sobre las tablas de posiciones y precios. Adjunta un fichero. Detalles: Función afectada: function_meg_cart_pos_fu_t(); Tablas afectadas: trf_s3.sss_position_t y trf_s3.sss_prices_t; Cambios requeridos: añadir campos cod_valprocs y dat_assepr a la subconsulta y al GROUP BY, y modificar la condición del INNER JOIN a 'pri.dat_price = val.dat_assepr' en lugar de 'val.dat_valuat'; Filtros aplicados: COD_TYPEAS in ('Future', 'Option'), COD_FLAG_MAPEO is null y des_provid = 'BOVESPA' · Adjuntos del correo: image001.png

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
- 2026-10-15 20:45 — (vacío) → Abierto — Correo automático
- 2026-10-17 11:51 — Abierto → En curso — Ricardo Reyes
- 2026-10-21 01:29 — En curso → Pendiente despliegue UAT — Marco Pichardo
- 2026-10-26 13:53 — Pendiente despliegue UAT → Resuelto — Ricardo Reyes

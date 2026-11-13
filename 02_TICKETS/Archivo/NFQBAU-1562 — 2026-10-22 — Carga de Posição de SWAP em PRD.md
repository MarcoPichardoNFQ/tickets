---
id: NFQBAU-1562
fecha_apertura: 2026-10-22
fecha_limite: 2026-10-23
fecha_resolucion: 2026-10-26
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: Carga de Posição de SWAP em PRD (2026-10-22)
categoria:
  - BBDD
entorno:
  - Producción
sintoma: La tabla TRF_S3.SSS_ADDL_DERIV_PRICE_T se encuentra vacía en PRD, impidiendo el funcionamiento del mapeo function_meg_cart_pos_sw_t.
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

Marco P., consultor de NFQ, incluye al equipo de soporte en una solicitud previa de Marcos M., tecnología.
Marcos M. solicita verificar si el mapeo function_meg_cart_pos_sw_t está activado en PRD y señala que requiere la carga de la tabla TRF_S3.SSS_ADDL_DERIV_PRICE_T.
Adjunta capturas.

Detalles: Mapeo: function_meg_cart_pos_sw_t; Tabla: TRF_S3.SSS_ADDL_DERIV_PRICE_T; La captura muestra una consulta SQL 'select * from TRF_S3.SSS_ADDL_DERIV_PRICE_T' en la base de datos con resultado 'Sem dados' (sin datos) ejecutada el 2026-10-22 a las 18:14:28
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png

## Histórico de interacciones

- 2026-10-22 18:26 — Correo automático — Marco P., consultor de NFQ, incluye al equipo de soporte en una solicitud previa de Marcos M., tecnología.
Marcos M. solicita verificar si el mapeo function_meg_cart_pos_sw_t está activado en PRD y señala que requiere la carga de la tabla TRF_S3.SSS_ADDL_DERIV_PRICE_T.
Adjunta capturas.
- 2026-10-22 18:37 — Correo automático — Correo nuevo en el hilo: Marco P., consultor sénior de NFQ, comunica que presenta problemas con su VDI pero que se encuentra realizando la validación solicitada. Adjunta capturas. Detalles: Problemas en la VDI del remitente; La captura muestra la ejecución de la consulta 'select * from TRF_S3.SSS_ADDL_DERIV_PRICE_T' sin resultados ('Sem dados') con fecha 2026-10-22 18:14:28 · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-10-22 18:56 — Correo automático — Correo nuevo en el hilo: Marco P., consultor senior de NFQ, responde al hilo de soporte sobre la carga de posición de SWAP. Confirma que el mapeo de la función en producción está activado. Adjunta capturas. Detalles: Mapeo: function_meg_cart_pos_sw_t; Tabla: TRF_S3.SSS_ADDL_DERIV_PRICE_T; La captura muestra la consulta 'select * from TRF_S3.SSS_ADDL_DERIV_PRICE_T' sin resultados el 2026-10-22 18:14:28; El remitente confirma que el mapeo está activado. · Adjuntos del correo: image001.png, image004.png, image002.png, image003.png
- 2026-10-22 19:26 — Correo automático — Correo nuevo en el hilo: Marco P. de NFQ adjunta evidencias de que la carga de posición de SWAP en Producción no está funcionando. Marcos M. de PR Serviços había solicitado verificar si el mapeo de la función `function_meg_cart_pos_sw_t` estaba activo y si la tabla `TRF_S3.SSS_ADDL_DERIV_PRICE_T` estaba siendo cargada, ya que se encontraba vacía. Detalles: Job de Rundeck: `mapeo_cart_pos_sw_t` (dentro de `00 - JOBS MEGARA Base/Main Job Megara`); Mensaje de error en log de Rundeck: `NOTICE: table "tem_meg_cart_pos_sw_t" does not exist, skipping`; Función afectada: `function_meg_cart_pos_sw_t`; Tabla `TRF_S3.SSS_ADDL_DERIV_PRICE_T` está vacía según consulta del 2026-10-22 a las 18:14:28; adjunta capturas de la tabla vacía y del log de Rundeck. · Adjuntos del correo: image001.png, image004.png, image002.png, image003.png, image.png
- 2026-10-22 19:32 — Correo automático — Correo nuevo en el hilo: Marcos M., tecnología de PRServicos, informa que la tabla TRF_S3.SSS_ADDL_DERIV_PRICE_T sigue sin datos, lo que impide que funcione el mapeo function_meg_cart_pos_sw_t para la carga de posición de SWAP en producción. Marco P., consultor de NFQ, adjunta capturas que muestran la ejecución de un job de Rundeck relacionado que falla por una tabla inexistente. El problema se reporta desde el 22 de octubre de 2026. Detalles: Tabla vacía: TRF_S3.SSS_ADDL_DERIV_PRICE_T; Mapeo afectado: function_meg_cart_pos_sw_t; Job de Rundeck: 00 - JOBS MEGARA Base/Main Job Megara > Archivos Flag > CargaInformacion > Mapeos > mapeo_cart_pos_sw_t; Mensaje de error del job: NOTICE: table "tem_meg_cart_pos_sw_t" does not exist, skipping; Fecha del problema: 22 de octubre de 2026; Captura 1 (image004.png): Muestra la ejecución del job de Rundeck mapeo_cart_pos_sw_t fallando con el error "table 'tem_meg_cart_pos_sw_t' does not exist"; Captura 2 (image005.png): Muestra el resultado de una consulta "select * from TRF_S3.SSS_ADDL_DERIV_PRICE_T" indicando "Sem dados" (sin datos). · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png
- 2026-10-22 19:32 — Correo automático — Correo nuevo en el hilo: Marco P., senior consultant de NFQ, informa que el análisis del problema de carga de posición de SWAP en producción está en curso y adjunta capturas de pantalla como evidencia. El problema se relaciona con la falta de datos en la tabla TRF_S3.SSS_ADDL_DERIV_PRICE_T, lo que impide el funcionamiento de una función de mapeo. Detalles: El job de Rundeck "00 - JOBS MEGARA Base/Main Job Megara" en el proyecto "Aldrin-Megara" ejecuta el paso "mapeo_cart_pos_sw_t"; Este paso ejecuta la función "trf_s3.function_meg_cart_pos_sw_t()"; La ejecución de la función falla con el mensaje "NOTICE: table "tem_meg_cart_pos_sw_t" does not exist, skipping"; La tabla "TRF_S3.SSS_ADDL_DERIV_PRICE_T" está vacía según una consulta realizada el 2026-10-22 a las 18:14:28; Se adjuntan capturas de pantalla de la ejecución de Rundeck y de la consulta a la base de datos. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png
- 2026-10-22 20:36 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, informa que la ausencia de datos se debe a que el sistema Megara no está enviando la interfaz asociada a la carga SSS, lo que resulta en la falta de registros para procesar. Adjunta capturas. Detalles: El sistema Megara no envía la interfaz asociada a la carga SSS; No existen registros disponibles para procesamiento; La tabla TRF_S3.SSS_ADDL_DERIV_PRICE_T está vacía; El job de Rundeck 'Aldrin-Megara / 00 - JOBS MEGARA Base/Main Job Megara' falla en el paso 'mapeo_cart_pos_sw_t'; Mensaje de error: 'NOTICE: table "tem_meg_cart_pos_sw_t" does not exist, skipping'; Se ejecuta la función 'function_meg_cart_pos_sw_t'; Las capturas muestran la ejecución del job en Rundeck y la tabla TRF_S3.SSS_ADDL_DERIV_PRICE_T vacía. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png
- 2026-10-22 20:41 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, informa que la ausencia de datos en la carga SSS se debe a que el sistema Megara no envía la interfaz asociada, por lo que no hay registros para procesar. Esto responde a la consulta de Marcos M., de Tecnología de PRServicos, sobre por qué la tabla TRF_S3.SSS_ADDL_DERIV_PRICE_T está vacía y si un mapeo estaba activo. El problema se detectó el 22 de octubre de 2026. Adjunta capturas. Detalles: La tabla TRF_S3.SSS_ADDL_DERIV_PRICE_T está vacía; El sistema Megara no envía la interfaz asociada a la carga SSS; El job de Rundeck '00 - JOBS MEGARA Base/Main Job Megara > CargaInformacion > Mapeos > mapeo_cart_pos_sw_t' (ejecución 10695756) muestra el error "table "tem_meg_cart_pos_sw_t" does not exist, skipping" al ejecutar function_meg_cart_pos_sw_t; Las capturas muestran el log de ejecución de Rundeck y la tabla TRF_S3.SSS_ADDL_DERIV_PRICE_T vacía. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png
- 2026-10-23 11:14 — Correo automático — Correo nuevo en el hilo: Marcos B., tecnología de PR Serviços, solicita a Ricardo C., de S3 Caceis, que pida al proveedor Vermeg activar la extracción en producción.
Esto ocurre tras identificarse que no existen registros a procesar porque Megara no remite la interfaz vinculada a la carga SSS.
Adjunta capturas. Detalles: Proveedor: Vermeg / Megara; Carga de posición de SWAP; Interfaz asociada a carga SSS ausente; Job Rundeck: mapeo_cart_pos_sw_t en proyecto Aldrin-Megara (ejecución 10695756); Ejecución: call exp_s3.fim_carga_mapeo_megara_indflag(0,118) y trf_s3.function_meg_cart_pos_sw_t(); Mensaje en Rundeck: NOTICE: table 'tem_meg_cart_pos_sw_t' does not exist, skipping; Consulta SQL a tabla TRF_S3.SSS_ADDL_DERIV_PRICE_T sin datos resultantes · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png
- 2026-10-23 12:36 — Correo automático — Correo nuevo en el hilo: Ricardo C., Proyecto Apollo, sugiere una reunión con Marcos M., Tecnología de PR Serviços, Oussema y Ado G. S., de PR Serviços, para resolver un problema con la carga de posición de SWAP en Producción. La extracción debería estar activa, pero hay una duda sobre el "Flag File" que Ado G. S. había planteado. Marcos M. había solicitado previamente activar la extracción en Producción. Adjunta capturas. Detalles: Rundeck job: `00 - JOBS MEGARA Base/Main Job Megara`; URL de ejecución de Rundeck: `https://rundeck.s3caceis.com.br:4443/project/Aldrin-Megara/execution/show/10695756`; Paso de Rundeck afectado: `mapeo_cart_pos_sw_t`; Mensaje de error literal: `NOTICE: table "tem_meg_cart_pos_sw_t" does not exist, skipping`; Función ejecutada: `SELECT trf_s3.function_meg_cart_pos_sw_t()`; Tabla afectada sin datos: `TRF_S3.SSS_ADDL_DERIV_PRICE_T`; Causa raíz identificada: "ausência de informações ocorre devido ao não envio, por parte do Megara, da interface associada à carga SSS"; Se menciona un "Flag File" como posible causa; Adjunta capturas de pantalla que muestran: la ejecución de un job en Rundeck con el error de tabla no existente; una consulta a la tabla `TRF_S3.SSS_ADDL_DERIV_PRICE_T` vacía; un documento de "Delivery Scope" con un "Problem Report" SC-9665 para "SWAP Prices". · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image001.png, image003.png, image004.png, image005.png, image006.gif, image007.png, image008.png, image009.png, image010.png, image011.png
- 2026-10-23 12:38 — Correo automático — Correo nuevo en el hilo: Ricardo C., Proyecto Apollo, sugiere una reunión con Oussema y Ado G. para revisar el problema de la carga de posición de SWAP en producción. Ado G. había cuestionado a Oussema sobre un "Flag File". Marco P., Senior Consultant, había informado previamente que la ausencia de datos se debe a que Megara no envía la interfaz SSS asociada a la carga, y que la extracción "está ligada". Marcos M., Tecnología, había solicitado activar la extracción en PRD. Adjunta capturas. Detalles: El job de Rundeck '00 - JOBS MEGARA Base/Main Job Megara' ejecuta 'mapeo_cart_pos_sw_t' (ejecución 10695756); El log del job muestra el error literal 'NOTICE: table "tem_meg_cart_pos_sw_t" does not exist, skipping'; La tabla 'TRF_S3.SSS_ADDL_DERIV_PRICE_T' está vacía ("Sem dados") a fecha 2026-10-22 18:14:28; El problema está relacionado con la ausencia de envío de la interfaz SSS por parte de Megara; Se adjunta un informe de problema SC-9665 para "SWAP Prices". · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image001.png, image003.png, image004.png, image005.png, image006.gif, image007.png, image008.png, image009.png, image010.png, image011.png
- 2026-10-23 15:17 — Correo automático — Correo nuevo en el hilo: Ado S., Tecnología, informa que la extracción "Additional Derivative Price" no está en producción o no está habilitada allí. Sin embargo, la encontró en pre-producción como MEGAACCOUNTING_ENDOFWEEK.FLAG. Adjunta capturas. Detalles: Extracción afectada: "Additional Derivative Price".; En Producción no se encuentra o no está habilitada.; En PRE PROD se encontró como MEGAACCOUNTING_ENDOFWEEK.FLAG.; Adjunta capturas de pantalla que muestran: un job de Rundeck con un error "table \"tem_meg_cart_pos_sw_t\" does not exist, skipping"; una consulta a la tabla TRF_S3.SSS_ADDL_DERIV_PRICE_T sin datos; y una interfaz de búsqueda de Innotech. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png
- 2026-10-23 15:21 — Correo automático — Correo nuevo en el hilo: Ado S., tecnología, informa que están revisando la carga en el Rundeck de Producción. Marcos M., tecnología, solicitó previamente activar la extracción en PRD tras detectar que no había datos procesados. Adjunta capturas. Detalles: Rundeck proyecto Aldrin-Megara ejecución 1069576 paso mapeo_cart_pos_sw_t; Ejecución call exp_s3.fim_carga_mapeo_megara_indflag(0,118) con NOTICE: table 'tem_meg_cart_pos_sw_t' does not exist, skipping; Consulta SELECT * FROM TRF_S3.SSS_ADDL_DERIV_PRICE_T sin datos; Extracción Additional Derivative Price configurada en Pre-Prod en MEGAACCOUNTING_ENDOFWEEK.FLAG · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png
- 2026-10-23 15:21 — Correo automático — Correo nuevo en el hilo: Marco P., consultor senior de NFQ, refuerza la necesidad de realizar una implantación coordinada en producción tan pronto como Vermeg libere la extracción correspondiente.
Advierte que la falta de coordinación causará un fallo crítico en la carga de datos debido a las validaciones de integridad de los archivos.
Adjunta capturas. Detalles: Proyecto Rundeck Aldrin-Megara; Job de mapeo mapeo_cart_pos_sw_t; Ejecución de la función trf_s3.function_meg_cart_pos_sw_t() emitiendo aviso NOTICE: table "tem_meg_cart_pos_sw_t" does not exist, skipping; Consulta SQL a la tabla TRF_S3.SSS_ADDL_DERIV_PRICE_T devuelve cero registros; Interfaz Innotech / Megara EndOfWeek; Flag de ejecución MEGAACCOUNTING_ENDOFWEEK.FLAG; Pendiente de liberación de la extracción Additional Derivative Price por parte de Vermeg · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png
- 2026-10-23 17:46 — Correo automático — Correo nuevo en el hilo: Marco P., consultor senior de NFQ, requiere con urgencia la presencia de NTT y de Ado S., de tecnología, en P0 tras una falta de coordinación en la implantación. Informa de una falla crítica activa en el proceso de producción que impide la carga. Adjunta capturas. Detalles: Proyecto Rundeck Aldrin-Megara (ejecución 10695766); mensaje de error: NOTICE: table "tem_meg_cart_pos_sw_t" does not exist, skipping en la función trf_s3.function_meg_cart_pos_sw_t(); consulta a la tabla TRF_S3.SSS_ADDL_DERIV_PRICE_T sin datos; falta el envío de la interfaz de carga SSS de Megara; flag MEGAACCOUNTING_ENDOFWEEK.FLAG localizado en PRE PROD pero no en Producción · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo
Vermeg activó la interfaz AdditionalDerivPrice
### Cómo se comprobó
Marcos hizo selct en la tabla de cart_pos_sw y en la tabla sss_Add_deriv_price_t
### Con quién se habló
Ado Meneses
### Servicios, jobs o tablas tocados

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-10-22 18:26 — nuevo → Abierto — Correo automático
- 2026-10-26 17:25 — Abierto → Resuelto — Marco Pichardo

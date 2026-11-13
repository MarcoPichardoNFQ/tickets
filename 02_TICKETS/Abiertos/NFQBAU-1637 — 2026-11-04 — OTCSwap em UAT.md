---
id: NFQBAU-1637
fecha_apertura: 2026-11-04
fecha_limite: 2026-11-05
fecha_resolucion: 2026-11-09
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: OTCSwap em UAT (2026-11-04)
categoria:
  - APIs
entorno:
  - UAT
sintoma: Se requiere la actualización del nuevo XSD de OTCSwap en el ambiente de UAT.
solucion_corta: "Se actualizó el archivo OTCSwap.xsd y se ejecutaron scripts SQL para corregir las tablas en el entorno UAT."
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-10 09:59
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

Marco P., consultor de NFQ, informa a Marcos M., de Tecnología, que la alteración de OTCSwap se implementará en UAT mañana para cumplir los plazos de validación de S3. Esta alteración se incluirá en el próximo paquete de liberación de Vermeg en producción durante el fin de semana. Adjunta capturas.

Detalles: Alteración de OTCSwap; Nuevo XSD de OTCSwap; Implementación en UAT mañana; Relacionado con el próximo paquete de liberación de Vermeg en producción; Validaciones correspondientes al S3.
Adjuntos del correo: image001.png, image002.png, image003.png

## Histórico de interacciones

- 2026-11-04 17:11 — Correo automático — Marco P., consultor de NFQ, informa a Marcos M., de Tecnología, que la alteración de OTCSwap se implementará en UAT mañana para cumplir los plazos de validación de S3. Esta alteración se incluirá en el próximo paquete de liberación de Vermeg en producción durante el fin de semana. Adjunta capturas.
- 2026-11-04 19:41 — Correo automático — Correo nuevo en el hilo: Fernando M., de S3 Caceis, solicita la entrega de OTCSWAP para el día siguiente a las 14:00h en el entorno UAT.
Además, pide soporte para dos tareas bloqueantes para la migración del fin de semana: el ajuste de tipo de cliente en la tabla de base de datos y la corrección de Fundo Abertura.
Adjunta capturas. Detalles: Entrega de OTCSWAP requerida para el día siguiente a las 14:00h (horario Brasil); Requerimiento Portfólio (Card 6) - TIPO CLIENTE con ajuste adicional en la tabla Investment_Company_Institute (crear patrón string / número); Corrección en Fundo Abertura para cambio de indexed_price; Ambas tareas son impeditivas para la migración del fin de semana · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-06 11:26 — Correo automático — Correo nuevo en el hilo: Marcos M., tecnología, informa que lo probado en UAT sigue sin funcionar y solicita a Matheus F., desarrollador de NFQ, volver a la sala de proyectos. Previamente se solicitó la ejecución de un script para actualizar las tablas relativas a OTCSwap. Adjunta capturas. Detalles: Servidor PostgreSQL: postgres/adminpsqlcerdatahub02@psqlcerdatahub01; Tablas afectadas en el script: STG_S3.PAR_LOAD_PLAN_T (COD_LOAD_PLAN 599 a 603) y stg_s3.par_maestro_columnas_t (cod_table = 599); Mensaje de error literal mostrado en la captura: 'ERROR: relation "cod_seq_otc_swap_leg" already exists'; SQL state: 42P07 · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png
- 2026-11-06 11:27 — Correo automático — Correo nuevo en el hilo: Matheus F., desarrollador de NFQ, informa que se está tratando el asunto en una sala abierta y envía un script SQL actualizado para aplicar las modificaciones necesarias en UAT. Adjunta un fichero y capturas. Detalles: Fichero adjunto: UPDATE FULL query_otcswap_v2.sql; Captura de PostgreSQL (adminpsqlcerdatahub02@psqlcerdatahub01) muestra consultas sobre STG_S3.PAR_LOAD_PLAN_T (COD_LOAD_PLAN 599 al 603) y stg_s3.par_maestro_columnas_t; Mensaje de error visualizado: ERROR: relation "cod_seq_otc_swap_leg" already exists (SQL state: 42P07). · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, UPDATE FULL query_otcswap_v2.sql
- 2026-11-06 11:32 — Correo automático — Correo nuevo en el hilo: Fernando A., de S3 Caceis, confirma su conformidad e informa de que se encuentran reunidos en una sesión conjunta de trabajo para revisar la ejecución de los scripts de OTCSwap.
Adjunta capturas. Detalles: Servidor/Instancia: postgres/adminpsqlcerdatahub02@psqlcerdatahub01; Tablas implicadas: STG_S3.PAR_LOAD_PLAN_T, stg_s3.par_maestro_columnas_t; Mensaje de error literal: ERROR: relation "cod_seq_otc_swap_leg" already exists; SQL state: 42P07; Operaciones en script: DELETE e INSERT para COD_LOAD_PLAN / cod_table = 599, 600, 601, 602, 603 · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png
- 2026-11-06 11:51 — Correo automático — Correo nuevo en el hilo: Reinaldo R., de NTT DATA, remite una solicitud para ejecutar un script de corrección en el ambiente de UAT. La petición surge tras detectar Matheus F., desarrollador, el 6 de noviembre que una actualización previa no aplicó los cambios esperados en las tablas. Adjunta capturas. Detalles: Ruta afectada: /nfq/XMLconversor/xsd/OTCSwap.xsd; Tablas SQL: STG_S3.PAR_LOAD_PLAN_T (COD_LOAD_PLAN 599 a 603) y stg_s3.par_maestro_columnas_t (cod_table = 599); Mensaje de error en captura: "ERROR: relation "cod_seq_otc_swap_leg" already exists" (SQL state: 42P07). · Adjuntos del correo: image001.png, image002.png, image003.png, image.png, image.png
- 2026-11-06 13:12 — Ricardo Reyes — Mismo hilo que [NFQBAU-1638](../Abiertos/NFQBAU-1638%20—%202026-11-04%20—%20RES%20Re%20OTCSwap%20em%20UAT.md) ("RES: Re: OTCSwap em UAT"): el correo automático lo separó por el asunto. Las novedades de ese hilo están en ese ticket.
- 2026-11-06 13:57 — Correo automático — Correo nuevo en el hilo: Reinaldo R. A. (NTT DATA) informa sobre una actividad realizada en una llamada y adjunta capturas. Marcos A. B. M. (PR Serviços) había reportado previamente que un script para 'OTCSwap' en UAT no funcionó, a pesar de las alteraciones proporcionadas por Matheus D. F. (NFQ). Fernando A. M. J. (S3 Caceis) ha solicitado prioridad en este pedido. El problema se está tratando desde el 6 de noviembre de 2026. Adjunta capturas. Detalles: Proceso afectado: OTCSwap; Mensaje de error literal: ERROR: relation "cod_seq_otc_swap_leg" already exists; Tablas involucradas: STG_S3.PAR_LOAD_PLAN_T, TRF_S3.Hist_sss_otc_swap_received_legs_t, TRF_S3.Hist_sss_otc_swap_pay_legs_t; Operaciones: DELETE, INSERT, ALTER TABLE; Valores de COD_LOAD_PLAN en DELETE/INSERT: 599, 600, 601, 602, 603; Captura 1 muestra la ejecución de sentencias DELETE e INSERT en STG_S3.PAR_LOAD_PLAN_T y el error 'relation "cod_seq_otc_swap_leg" already exists'; Captura 2 muestra la ejecución exitosa de sentencias ALTER TABLE para añadir columnas a TRF_S3.Hist_sss_otc_swap_received_legs_t y TRF_S3.Hist_sss_otc_swap_pay_legs_t. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image.png, image.png
- 2026-11-06 15:02 — Correo automático — Correo nuevo en el hilo: Matheus D., developer en NFQ, solicita actualizar el fichero OTCSwap.xsd en la ruta /nfq/XMLconversor/xsd/ y ejecutar un script en la base de datos para solucionar que los cambios no se reflejaron en algunas tablas durante las pruebas en UAT. Adjunta capturas y un fichero. Detalles: Host: psqlcerdatahub01.postgres.database.cloud.corp; Ruta: /nfq/XMLconversor/xsd/; Fichero adjunto: OTCSwap.xsd; adjunta capturas y un fichero. · Adjuntos del correo: image001.png, image002.png, image003.png, OTCSwap.xsd
- 2026-11-06 15:41 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador en NFQ, solicita al equipo de soporte una nueva actualización del fichero OTCSwap.xsd adjunto en la ruta especificada del entorno UAT, pidiendo realizar una copia de seguridad del fichero existente. Detalles: Fichero: OTCSwap.xsd; Ruta: /nfq/XMLconversor/xsd/; Host: psqlcerdatahub01.postgres.database.cloud.corp; adjunta un fichero · Adjuntos del correo: image001.png, image002.png, image003.png, OTCSwap.xsd
- 2026-11-06 15:42 — Correo automático — Correo nuevo en el hilo: Fernando Augusto M., del equipo de soporte, da el visto bueno y pide prioridad al equipo de cloud para atender la solicitud de actualización del archivo de configuración. Matheus Demelo F., desarrollador, solicita una nueva actualización del archivo OTCSwap.xsd en el entorno de UAT. Detalles: Archivo afectado: OTCSwap.xsd; Ruta: /nfq/XMLconversor/xsd/; Host: psqlcerdatahub01.postgres.database.cloud.corp; adjunta capturas · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-06 15:46 — Correo automático — Correo nuevo en el hilo: Marcos M., tecnología, solicita a Reinaldo R. que pida a Pedro que realice una nueva actualización del archivo OTCSwap.xsd en el entorno UAT. Esta petición se realiza después de que una actualización anterior no se haya reflejado correctamente o necesite ser repetida. Adjunta capturas. Detalles: Archivo afectado: OTCSwap.xsd; Ruta: /nfq/XMLconversor/xsd/; Host: psqlcerdatahub01.postgres.database.cloud.corp; Se solicita actualizar nuevamente el archivo. · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-06 15:51 — Correo automático — Correo nuevo en el hilo: Marcos M., tecnología de PR Serviços, aclara que se debe realizar de nuevo la actualización utilizando el mismo archivo XSD, ya que el archivo subido previamente por el equipo de soporte era erróneo. Se solicita volver a aplicar el cambio en UAT. Adjunta capturas. Detalles: Fichero: /nfq/XMLconversor/xsd/OTCSwap.xsd; Host: psqlcerdatahub01.postgres.database.cloud.corp; Acción: Replicar actualización con el mismo archivo XSD por haberse aplicado una versión errónea anteriormente. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-11-06 16:21 — Correo automático — Correo nuevo en el hilo: Pedro G., IT Support Analyst, informa que la actualización solicitada ya fue realizada. Menciona el ticket S3C-23107. Adjunta capturas. Detalles: Se solicitó la actualización del archivo OTCSwap.xsd en la ruta /nfq/XMLconversor/xsd/ para el ambiente UAT, en el host psqlcerdatahub01.postgres.database.cloud.corp; Posteriormente, se solicitó la ejecución de un script porque las alteraciones no se reflejaron en algunas tablas; Marcos M. confirmó la ejecución de la actualización a las 09:37; La actualización ya fue realizada; Ticket S3C-23107; Adjunta capturas de pantalla. · Adjuntos del correo: image001.png, image002.png, image003.png, image.png
- 2026-11-06 17:02 — Correo automático — Correo nuevo en el hilo: Pedro G., IT Support Analyst de NTT DATA, pregunta si se está utilizando el mismo archivo para la actualización. Anteriormente, Matheus D., Developer III de NFQ, solicitó una nueva actualización del archivo OTCSwap.xsd y la ejecución de un script en UAT, ya que las modificaciones previas no se reflejaron en algunas tablas. Marcos M., Tecnología de PR Serviços, pidió a Pedro que realizara la actualización nuevamente. Adjunta capturas. Detalles: Archivo: OTCSwap.xsd; Ruta: /nfq/XMLconversor/xsd/; Host: psqlcerdatahub01.postgres.database.cloud.corp; Problema: las alteraciones de un script no se reflejaron en algunas tablas; Se solicita hacer backup del archivo existente; Se adjuntan 4 capturas de pantalla. · Adjuntos del correo: image001.png, image002.png, image003.png, image.png
- 2026-11-06 19:36 — Correo automático — Correo nuevo en el hilo: Pedro H. G., analista de soporte de NTT Data, confirma que se ha completado la actualización solicitada en el hilo. Se refiere al ticket S3C-23107. Detalles: Ticket registrado: S3C-23107; adjunta capturas · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image.png
- 2026-11-10 09:58 — Correo automático — Resolución redactada automáticamente a partir del histórico; revisar.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Se realizaron múltiples intentos de actualización del archivo XSD y ejecución de scripts SQL. Se corrigieron errores de duplicidad en relaciones de base de datos mediante sentencias DELETE, INSERT y ALTER TABLE. Finalmente, se aplicó la versión correcta del archivo XSD tras realizar una copia de seguridad.

### Cómo se comprobó

No consta en el histórico.

### Con quién se habló

Marco P., consultor de NFQ; Marcos M., Tecnología; Fernando M., S3 Caceis; Matheus F., desarrollador de NFQ; Reinaldo R., NTT DATA; Marcos A. B. M., PR Serviços; Fernando A. M. J., S3 Caceis; Pedro G., IT Support Analyst.

### Servicios, jobs o tablas tocados

OTCSwap.xsd, STG_S3.PAR_LOAD_PLAN_T, stg_s3.par_maestro_columnas_t, TRF_S3.Hist_sss_otc_swap_received_legs_t, TRF_S3.Hist_sss_otc_swap_pay_legs_t, UAT

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-11-04 17:11 — nuevo → Abierto — Correo automático
- 2026-11-05 12:24 — Abierto → En curso — Marco Pichardo
- 2026-11-06 05:27 — En curso → Revisión cliente — Marco Pichardo
- 2026-11-06 12:14 — nuevo → Revisión cliente — Matheus Fransoni
- 2026-11-06 12:38 — Revisión cliente → Pruebas cliente UAT — Matheus Fransoni
- 2026-11-09 16:18 — Pruebas cliente UAT → Resuelto — Matheus Fransoni

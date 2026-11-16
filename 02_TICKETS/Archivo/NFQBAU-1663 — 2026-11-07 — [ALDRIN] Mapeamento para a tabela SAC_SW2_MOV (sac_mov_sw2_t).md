---
id: NFQBAU-1663
fecha_apertura: 2026-11-07
fecha_limite: 2026-11-10
fecha_resolucion: 2026-11-09
estado: Resuelto
prioridad: Baja
responsable: Matheus Fransoni
origen: email
referencia_origen: "[ALDRIN] Mapeamento para a tabela SAC_SW2_MOV (sac_mov_sw2_t) (2026-11-07)"
categoria:
  - BBDD
entorno: []
sintoma: No se reporta un fallo; se proporciona la consulta de mapeo para la función function_meg_sac_mov_sw2_t de operaciones de swap.
solucion_corta: "Se actualizó y ejecutó el mapeo de la función function_meg_sac_mov_sw2_t para la tabla SAC_SW2_MOV en UAT y Producción."
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-09 10:21
actualizado_por: Correo automático
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marcos M., del área de tecnología, remite a Matheus F. la consulta SQL correspondiente al mapeo de la función function_meg_sac_mov_sw2_t para operaciones de swap en la tabla SAC_SW2_MOV. Adjunta capturas.

Detalles: Función afectada: function_meg_sac_mov_sw2_t; Tabla destino: SAC_SW2_MOV (sac_mov_sw2_t); Tablas origen: trf_s3.sss_cus_com_ins_t y trf_s3.sss_asset_t; Condiciones del select: cod_dmasfm = 10, des_status <> 'CANCELLED' y cod_flag_mapeo IS NULL; Incluye transformación de tipos de movimiento (Buy->C, Sell->V, DF->R, RF->D), asignación fija de COD_SACBBDD='MEG' y concatenación de clave COD_ORD, DAT_MOV, COD_CLI y COD_SWCAD
Adjuntos del correo: image001.png, image002.png, image003.png

## Histórico de interacciones

- 2026-11-07 12:17 — Correo automático — Marcos M., del área de tecnología, remite a Matheus F. la consulta SQL correspondiente al mapeo de la función function_meg_sac_mov_sw2_t para operaciones de swap en la tabla SAC_SW2_MOV. Adjunta capturas.
- 2026-11-07 12:28 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador de NFQ, responde informando que la solicitud de mapeo recibida será atendida a través del ticket NFQBAU1663. Detalles: Ticket de atención: NFQBAU1663; Función afectada en el hilo: function_meg_sac_mov_sw2_t; Tabla destino: SAC_SW2_MOV (sac_mov_sw2_t) · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-07 12:39 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador de NFQ, envía una propuesta de código SQL y solicita validar si cubre la solicitud de mapeo requerida. Adjunta capturas y un fichero. Detalles: Fichero adjunto: UPDATE function_meg_sac_mov_sw2_t_20261107.sql; Función: function_meg_sac_mov_sw2_t; Tabla: SAC_SW2_MOV (sac_mov_sw2_t); Ticket asociado: NFQBAU1663 · Adjuntos del correo: image001.png, image002.png, image003.png, UPDATE function_meg_sac_mov_sw2_t_20261107.sql
- 2026-11-07 12:47 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador de NFQ, envía a Marcos M., del equipo de tecnología, la actualización acordada en la sala de proyectos para el mapeo de la función. Adjunta un fichero. Detalles: Fichero adjunto: UPDATE function_meg_sac_mov_sw2_t_20261107.sql; Función: function_meg_sac_mov_sw2_t; Tabla: SAC_SW2_MOV (sac_mov_sw2_t); Ticket de referencia: NFQBAU1663 · Adjuntos del correo: image001.png, image002.png, image003.png, UPDATE function_meg_sac_mov_sw2_t_20261107.sql
- 2026-11-07 13:03 — Correo automático — APROBACIÓN — Correo nuevo en el hilo: Marcos M., del área de Tecnología, informa de que el código ha sido validado con éxito. Pide a Matheus D., desarrollador de NFQ, solicitar a NTT la actualización en el entorno de UAT. Detalles: Tabla: SAC_SW2_MOV (sac_mov_sw2_t); Función: function_meg_sac_mov_sw2_t; Ticket relacionado: NFQBAU1663 · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-07 13:08 — Correo automático — Correo nuevo en el hilo: Matheus F., desarrollador de NFQ, solicita al equipo de soporte compilar un código SQL en el entorno de UAT.
Indica los responsables autorizados para aprobar el cambio tras haber sido validado previamente por Marcos M., de PR Servicios.
Adjunta un fichero y capturas. Detalles: Host: psqlcerdatahub01.postgres.database.cloud.corp; Tabla: SAC_SW2_MOV (sac_mov_sw2_t); Función: function_meg_sac_mov_sw2_t; Fichero adjunto: UPDATE function_meg_sac_mov_sw2_t_20261107.sql; Ticket referenciado: NFQBAU1663; La captura muestra un correo que define quiénes tienen permisos para autorizar ejecuciones en UAT · Adjuntos del correo: image001.png, image002.png, image003.png, image.png, UPDATE function_meg_sac_mov_sw2_t_20261107.sql
- 2026-11-07 13:36 — Correo automático — APROBACIÓN UAT — Correo nuevo en el hilo: Kleverson B., de S3 Caceis, da su conformidad ('De acordo') para avanzar con la solicitud de cambio en UAT. El mensaje responde al pedido de autorización para compilar el código del mapeo de la tabla SAC_SW2_MOV. Adjunta capturas. Detalles: Conformidad del cliente ('De acordo'); Ticket asociado NFQBAU1663; Cambios en mapeo para la tabla SAC_SW2_MOV (sac_mov_sw2_t); Host psqlcerdatahub01.postgres.database.cloud.corp; Función afectada function_meg_sac_mov_sw2_t · Adjuntos del correo: image001.png, image002.png, image003.png, image.png
- 2026-11-07 15:01 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, solicita al equipo de soporte la compilación de un archivo de código SQL en el entorno de UAT para la tabla SAC_SW2_MOV. Detalla quiénes pueden aprobar la ejecución e indica el plan de cambio y rollback. Adjunta un fichero y capturas. Detalles: Host: psqlcerdatahub01.postgres.database.cloud.corp; Tabla: SAC_SW2_MOV (sac_mov_sw2_t); Servicio afectado: Database; Fichero anexo: UPDATE function_meg_sac_mov_sw2_t_20261107.sql; La captura de pantalla muestra un mensaje de Kleverson B. indicando que personas de s3 (Meneses, Ado, Ricardo o David) pueden aprobar cambios para UAT · Adjuntos del correo: image001.png, image002.png, image003.png, image.png, image.png, UPDATE function_meg_sac_mov_sw2_t_20261107.sql
- 2026-11-07 15:51 — Correo automático — APROBACIÓN UAT — Correo nuevo en el hilo: Marcos Antonio M., del área de tecnología del cliente, informa que las pruebas en el entorno de UAT concluyeron con éxito. Solicita gestionar la aprobación y la ejecución de la actualización en el entorno de Producción. Adjunta capturas. Detalles: Tabla: SAC_SW2_MOV (trf_s3.sac_mov_sw2_t); Host: psqlcerdatahub01.postgres.database.cloud.corp; Función PostgreSQL: meg_sac_mov_sw2_t; Las capturas muestran la correcta ejecución de la función de base de datos y la consulta a la tabla sac_mov_sw2_t · Adjuntos del correo: image007.png, image008.png, image009.png, image010.png, image011.png, image012.png, image013.png
- 2026-11-07 15:56 — Correo automático — Correo nuevo en el hilo: Luiz C. F., técnico de operaciones de NTT, confirma que se ha creado lo solicitado. Anteriormente, Matheus D. F., desarrollador de NFQ, solicitó a NTT compilar un código adjunto en UAT para el mapeo de la tabla SAC_SW2_MOV, indicando que Marcos A. B. M., Ado G. S. y Ricardo C. pueden aprobar las ejecuciones en UAT, según Kleverson B. Adjunta capturas. Detalles: Host: psqlcerdatahub01.postgres.database.cloud.corp; Descripción de la cambio: Mapeamento para a tabela SAC_SW2_MOV (sac_mov_sw2_t); Servicios afectados: Database; Plan de rollback: Execução do arquivo ROLLBACK em anexo; Nivel e impacto al negocio: Inserção de informações no Aldrin; Ticket interno NTT: S3C-23133; Ticket NFQ: NFQBAU1663; Captura 1: Muestra una consulta SQL para crear la función 'function_meg_sac_mov_sw2_t' con un SELECT de la tabla 'DuplicatedRecordsCTE' y un RAISE NOTICE, ejecutada con éxito; Captura 2: Correo de Kleverson B. indicando que Marcos A. B. M., Ado G. S., Ricardo C. o David pueden aprobar para UAT. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png
- 2026-11-07 15:56 — Correo automático — APROBACIÓN PRD — Correo nuevo en el hilo: Marco P. solicita nuevamente la aprobación de Kleverson B., Mauricio R. y Fernando A. para ejecutar un código SQL adjunto en la base de datos de Producción. Este cambio es para ajustar el mapeo de la función "function_meg_sac_mov_sw2_t", dando continuidad a un acuerdo previo. Marcos M., de PR Serviços, había solicitado la actualización en PRD tras confirmar el éxito de las pruebas en UAT. Adjunta capturas y un fichero SQL. Detalles: Función afectada: "function_meg_sac_mov_sw2_t"; Tabla relacionada: SAC_SW2_MOV (sac_mov_sw2_t); Fichero SQL adjunto: UPDATE function_meg_sac_mov_sw2_t_20261107.sql; Host de Producción: psqlprddatahub03.postgres.database.cloud.corp; Sistema: ALDRIN; Impacto en cliente y otros sistemas: Sí, ALDRIN es un repositorio central de datos; Tiempo de rollback: 30 minutos; Responsable de prueba funcional y técnica: Meneses (S3) / Marco (NFQ); Las capturas muestran una consulta a la tabla sac_mov_sw2_t con la columna dat_qlikupdate y la creación exitosa de la función function_meg_sac_mov_sw2_t; Marcos M. confirmó "Teste realizado com sucesso em UAT"; Luiz C. de NTT Data confirmó "Executado conforme solicitado. S3C-23135" en UAT. · Adjuntos del correo: image007.png, image008.png, image009.png, image010.png, image011.png, image012.png, image013.png, UPDATE function_meg_sac_mov_sw2_t_20261107.sql
- 2026-11-07 16:02 — Correo automático — APROBACIÓN PRD — Correo nuevo en el hilo: Fernando A. da su conformidad para la ejecución en producción del código SQL que ajusta el mapeo de la tabla SAC_SW2_MOV. Previamente, Marcos A. B. había confirmado el éxito de las pruebas en UAT y solicitado la actualización en producción, después de que NTT desplegara el código en UAT. Adjunta capturas. Detalles: Se solicita la ejecución de un código SQL para la función "function_meg_sac_mov_sw2_t" que mapea la tabla "SAC_SW2_MOV" (sac_mov_sw2_t) en el sistema ALDRIN; El host de producción es "psqlprddatahub03.postgres.database.cloud.corp"; El host de UAT es "psqlcerdatahub01.postgres.database.cloud.corp"; Se adjunta el código SQL y un archivo de rollback; Las capturas muestran una consulta a "sac_mov_sw2_t" con "dat_qlikupdate" y la creación de la función "function_meg_sac_mov_sw2_t". · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png
- 2026-11-07 18:46 — Correo automático — Correo nuevo en el hilo: Luiz C. F., técnico de operaciones de NTT DATA, confirma que se ha ejecutado la compilación del código solicitado para el mapeo de la tabla SAC_SW2_MOV en UAT. Marco J. P. F., consultor de NFQ, había solicitado la compilación del código adjunto en UAT, siguiendo las instrucciones de Kleverson B., de S3CACEIS, y con la aprobación de Marcos A. B. M., Ado G. S. y Ricardo C. de PR Serviços/S3CACEIS. Adjunta capturas. Detalles: Host: psqlcerdatahub01.postgres.database.cloud.corp; Descripción del cambio: Mapeo para la tabla SAC_SW2_MOV (sac_mov_sw2_t); Servicios afectados: Database; Plan de rollback: Ejecución del archivo ROLLBACK adjunto; Impacto al negocio: Inserción de información en Aldrin; La captura de pantalla muestra la creación de una función SQL llamada 'meg_sac_mov_sw2_t' y una consulta 'SELECT' sobre 'DuplicatedRecordsCTE'. El código fue validado por Marcos A. B. M. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png
- 2026-11-09 09:53 — Correo automático — Correo nuevo en el hilo: Reinaldo A., de NTT DATA, confirma la ejecución del pase a producción correspondiente al ticket S3C-23153 tras las aprobaciones previas. Adjunta capturas de la ejecución realizada. Detalles: Ticket: S3C-23153; Host PRD: psqlprddatahub03.postgres.database.cloud.corp; Función: function_meg_sac_mov_sw2_t; Tabla: SAC_SW2_MOV (trf_s3.sac_mov_sw2_t); Sistema: ALDRIN · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image.png, image.png
- 2026-11-09 10:20 — Correo automático — Resolución redactada automáticamente a partir del histórico; revisar.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

El equipo de NFQ preparó una propuesta de código SQL para el mapeo. Se solicitó y obtuvo la compilación del código en el entorno de UAT a través de NTT, tras la aprobación de los responsables. Marcos M. validó las pruebas en UAT con éxito y solicitó la actualización en Producción. Finalmente, NTT ejecutó el pase a producción del código SQL.

### Cómo se comprobó

Marcos M. validó las pruebas en el entorno de UAT informando que concluyeron con éxito, y Reinaldo A., de NTT DATA, confirmó la ejecución del pase a producción mediante capturas.

### Con quién se habló

Marcos M., del área de tecnología; Matheus F., desarrollador de NFQ; Matheus D., desarrollador de NFQ; Kleverson B., de S3 Caceis; Marco P., consultor de NFQ; Marcos Antonio M., del área de tecnología del cliente; Luiz C. F., técnico de operaciones de NTT; Fernando A.; Marco J. P. F., consultor de NFQ; Reinaldo A., de NTT DATA

### Servicios, jobs o tablas tocados

function_meg_sac_mov_sw2_t, SAC_SW2_MOV, sac_mov_sw2_t, trf_s3.sss_cus_com_ins_t, trf_s3.sss_asset_t, Database, ALDRIN

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-11-07 12:17 — nuevo → Abierto — Correo automático
- 2026-11-09 09:59 — Abierto → Resuelto — Matheus Fransoni

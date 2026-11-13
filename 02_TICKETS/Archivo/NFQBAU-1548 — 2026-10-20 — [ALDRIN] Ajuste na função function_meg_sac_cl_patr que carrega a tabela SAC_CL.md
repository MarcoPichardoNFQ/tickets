---
id: NFQBAU-1548
fecha_apertura: 2026-10-20
fecha_limite: 2026-10-23
fecha_resolucion: 2026-10-26
estado: Resuelto
prioridad: Baja
responsable: Deborah Bertoldo
origen: email
referencia_origen: '[ALDRIN] Ajuste na função "function_meg_sac_cl_patr" que carrega a tabela SAC_CL_PATR (2026-10-20)'
categoria:
  - BBDD
entorno:
  - UAT
  - Producción
sintoma: Se requiere modificar la función de base de datos "function_meg_sac_cl_patr" para incluir cuatro nuevos campos en la carga de la tabla SAC_CL_PATR.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-26 17:32
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

Marcos M., del área de Tecnología, solicita actualizar la función que carga la tabla SAC_CL_PATR para agregar cuatro nuevos campos necesarios para una API hacia SAM. Pide actualizar las sentencias SELECT, INSERT y UPDATE de la función. Adjunta capturas.

Detalles: Función: function_meg_sac_cl_patr; Tabla: SAC_CL_PATR; Modificación de SELECT, INSERT y UPDATE para añadir los campos netasset.VL_COTAS_RESGATAR_MX as AMT_COTAS_RESGATAR_MX, netasset.VL_COTAS_EMITIR_MX as AMT_COTAS_EMITIR_MX, netasset.VL_PL_BRUTO_MX as AMT_PL_BRUTO_MX y netasset.VL_COTA_BRUTA_MX as AMT_COTA_BRUTA_MX; Los campos serán utilizados por API para SAM; La captura muestra el resultado de una consulta SQL con la CTE summary_netasset_calculations mostrando los valores de los cuatro nuevos campos calculados para el cliente CUST3458 con fecha de posición 2026-07-16
Adjuntos del correo: image002.png, image003.png, image004.png, image005.png

## Histórico de interacciones

- 2026-10-20 16:02 — Correo automático — Marcos M., del área de Tecnología, solicita actualizar la función que carga la tabla SAC_CL_PATR para agregar cuatro nuevos campos necesarios para una API hacia SAM. Pide actualizar las sentencias SELECT, INSERT y UPDATE de la función. Adjunta capturas.
- 2026-10-20 21:51 — Correo automático — Correo nuevo en el hilo (era el NFQBAU-1551): Marco J., consultor senior, pregunta si el código enviado adjunto cumple con la solicitud de ajuste en la función function_meg_sac_cl_patr.
- 2026-10-21 11:36 — Correo automático — Correo nuevo en el hilo (era el NFQBAU-1555): Marcos M., de Tecnología, confirma que el código ha sido validado correctamente. Solicita a Deborah B. y Marco P., del equipo de desarrollo, que pidan a NTT la actualización correspondiente en el entorno de UAT.
- 2026-10-21 16:27 — Correo automático — Correo nuevo en el hilo (era el NFQBAU-1558): Marco J. P., consultor de NFQ, solicita al equipo de soporte compilar un código SQL en UAT. El código, validado por Marcos M., tecnología de PR Serviços, ajusta una función para añadir nuevos campos a la tabla SAC_CL_PATR, que serán usados por una API. Adjunta capturas y un fichero.
- 2026-10-21 17:56 — Correo automático — Correo nuevo en el hilo (era el NFQBAU-1564): Marcos M., tecnología, notifica que las pruebas en UAT se han realizado con éxito adjuntando capturas y solicita la aprobación y actualización en PRD para la función y tabla correspondientes.
- 2026-10-21 18:01 — Correo automático — Correo nuevo en el hilo (era el NFQBAU-1565): Marco P., consultor de NFQ, solicita la aprobación para desplegar un ajuste en dos funciones de base de datos en el entorno de Producción. Marcos M., de S3, ya validó el código y solicitó la actualización en PRD tras realizar pruebas exitosas en UAT. El cambio fue solicitado por Thiago A. y Marcos M., ambos de PRServicos. Adjunta capturas y dos ficheros SQL.
- 2026-10-21 18:11 — Correo automático — Correo nuevo en el hilo (era el NFQBAU-1566): Fernando A., consultor en S3 Caceis, da su acuerdo al despliegue solicitado. Adjunta capturas.
- 2026-10-21 18:26 — Correo automático — Correo nuevo en el hilo (era el NFQBAU-1567): Reinaldo R. de NTT Data solicita la aprobación para el despliegue en Producción de un ajuste en una función de base de datos. Marcos A. de S3 Caceis ya ha confirmado el éxito de las pruebas en UAT. El cambio fue solicitado por Marcos A. y Thiago A. Adjunta capturas.
- 2026-10-21 18:36 — Correo automático — Correo nuevo en el hilo (era el NFQBAU-1568): Kleverson B., de tecnología en S3 CACEIS, da su conformidad para el despliegue en producción solicitado por Marco P., consultor de NFQ. El cambio aplica un ajuste a la función function_meg_sac_cl_patr para la tabla SAC_CL_PATR del sistema ALDRIN, previamente probado en UAT el 21/10/2026. Adjunta capturas.
- 2026-10-21 19:33 — Correo automático — Correo nuevo en el hilo (era el NFQBAU-1569): Marcos M., tecnología de PR Serviços, solicitó ajustar la función "function_meg_sac_cl_patr". Marco P., Senior Consultant de NFQ, pide compilar el código adjunto en UAT, indicando que Marcos M. puede aprobar la ejecución. Reinaldo A., de NTT DATA, confirma el ticket S3C-22840 y el entorno UAT. Adjunta capturas.
- 2026-10-21 21:52 — Correo automático — Correo nuevo en el hilo (era el NFQBAU-1569): Correo nuevo en el hilo: Luiz H. C., Operation Technician de NTT DATA, solicita abrir un ticket para ejecutar una tarea. Esta tarea consiste en un ajuste en la función "function_meg_sac_cl_patr" que carga la tabla "SAC_CL_PATR" en el sistema ALDRIN. Marco P., Senior Consultant de NFQ, había solicitado la aprobación para este despliegue en producción, después de que Marcos M., Tecnología de S3, confirmara pruebas exitosas en UAT. Kleverson B., Tecnología de S3 Caceis, ha dado su aprobación. Reinaldo A., de NTT DATA, ya había informado el número de ticket S3C-22840. Adjunta capturas.

Nota: los tickets siguientes nacieron del mismo hilo por un fallo del emparejado (asuntos con comillas) y se han fusionado aquí.

**NFQBAU-1551** (fusionado el 2026-10-22):

Marco J., consultor senior, pregunta si el código enviado adjunto cumple con la solicitud de ajuste en la función function_meg_sac_cl_patr.

Detalles: Función: function_meg_sac_cl_patr; Tabla afectada: SAC_CL_PATR; Campos a añadir en el SELECT, INSERT y UPDATE: AMT_COTAS_RESGATAR_MX, AMT_COTAS_EMITIR_MX, AMT_PL_BRUTO_MX, AMT_COTA_BRUTA_MX; adjunta capturas y un fichero SQL (ajutefunction_meg_sac_cl_patr_20261020.sql). Las capturas muestran la ejecución de la consulta con los nuevos campos de netasset para el cliente CUST3458 con fecha 2026-07-16.
Adjuntos del correo: image002.png, image003.png, image004.png, image005.png, ajustefunction_meg_sac_cl_patr_20261020.sql

**NFQBAU-1555** (fusionado el 2026-10-22):

Marcos M., de Tecnología, confirma que el código ha sido validado correctamente. Solicita a Deborah B. y Marco P., del equipo de desarrollo, que pidan a NTT la actualización correspondiente en el entorno de UAT.

Detalles: Ticket asociado: NFQBAU1548 (mencionado previamente como NFQBAU1248); Función: function_meg_sac_cl_patr; Tabla: SAC_CL_PATR; Campos involucrados: AMT_COTAS_RESGATAR_MX, AMT_COTAS_EMITIR_MX, AMT_PL_BRUTO_MX, AMT_COTA_BRUTA_MX; Petición de actualización en UAT a ser gestionada con NTT.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png

**NFQBAU-1558** (fusionado el 2026-10-22):

Marco J. P., consultor de NFQ, solicita al equipo de soporte compilar un código SQL en UAT. El código, validado por Marcos M., tecnología de PR Serviços, ajusta una función para añadir nuevos campos a la tabla SAC_CL_PATR, que serán usados por una API. Adjunta capturas y un fichero.

Detalles: Función afectada: "function_meg_sac_cl_patr"; Tabla afectada: SAC_CL_PATR; Host de la base de datos: psqlcerdatahub01.postgres.database.cloud.corp; El código adjunto es ajustefunction_meg_sac_cl_patr_20261020.sql; La modificación añade los campos AMT_COTAS_RESGATAR_MX, AMT_COTAS_EMITIR_MX, AMT_PL_BRUTO_MX, AMT_COTA_BRUTA_MX al SELECT y requiere actualizar el INSERT / UPDATE; Los nuevos campos se utilizarán por una API para SAM; La captura de pantalla image001.png muestra una consulta SQL con los nuevos campos amt_cotas_resgatar_mx, amt_cotas_emitir_mx, amt_pl_bruto_mx, amt_cota_bruta_mx y el inicio de la consulta with summary_netasset_calculations as (select CCOD_DMNWEX_B.cod; Marcos M. tiene autorización para aprobar ejecuciones en UAT.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image.png, ajustefunction_meg_sac_cl_patr_20261020.sql

**NFQBAU-1564** (fusionado el 2026-10-22):

Marcos M., tecnología, notifica que las pruebas en UAT se han realizado con éxito adjuntando capturas y solicita la aprobación y actualización en PRD para la función y tabla correspondientes.

Detalles: Ticket: S3C-22840; Función: function_meg_sac_cl_patr; Tabla: SAC_CL_PATR; Host: psqlcerdatahub01.postgres.database.cloud.corp; adjunta capturas.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png

**NFQBAU-1565** (fusionado el 2026-10-22):

Marco P., consultor de NFQ, solicita la aprobación para desplegar un ajuste en dos funciones de base de datos en el entorno de Producción. Marcos M., de S3, ya validó el código y solicitó la actualización en PRD tras realizar pruebas exitosas en UAT. El cambio fue solicitado por Thiago A. y Marcos M., ambos de PRServicos. Adjunta capturas y dos ficheros SQL.

Detalles: Se solicita el despliegue en el host psqlprddatahub03.postgres.database.cloud.corp de un ajuste en las funciones function_meg_sac_cl_patr y function_meg_cart_pos_fi_t que cargan las tablas SAC_CL_PATR y trf cart_pos_fi_t del sistema ALDRIN; El cambio es de tipo lógica y tiene impacto en cliente y otros sistemas; El tiempo de rollback es de 30 minutos; Marcos M. (S3) y Marco P. (NFQ) son los responsables de las pruebas; Se adjuntan 8 capturas de pantalla y 2 ficheros SQL (ajustefunction_meg_sac_cl_patr_20261020.sql, bkpfunction_meg_sac_cl_patr.sql); Las capturas muestran una consulta SQL a la tabla SAC_CL_PATR y la ejecución de un script para crear/reemplazar la función trf_s3.function_meg_sac_cl_patr en UAT (host psqlcerdatahub01); El código fue validado y probado con éxito en UAT por Marcos M. (S3); El ticket asociado es S3C-22840.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, ajustefunction_meg_sac_cl_patr_20261020.sql, bkpfunction_meg_sac_cl_patr.sql

**NFQBAU-1566** (fusionado el 2026-10-22):

Fernando A., consultor en S3 Caceis, da su acuerdo al despliegue solicitado. Adjunta capturas.

Detalles: Host: psqlprddatahub03.postgres.database.cloud.corp; Función: function_meg_sac_cl_patr; Tabla afectada: SAC_CL_PATR; Ticket: S3C-22840; adjunta capturas
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png

**NFQBAU-1567** (fusionado el 2026-10-22):

Reinaldo R. de NTT Data solicita la aprobación para el despliegue en Producción de un ajuste en una función de base de datos. Marcos A. de S3 Caceis ya ha confirmado el éxito de las pruebas en UAT. El cambio fue solicitado por Marcos A. y Thiago A. Adjunta capturas.

Detalles: Se solicita un ajuste en la función "function_meg_sac_cl_patr" que carga la tabla "SAC_CL_PATR" en el sistema ALDRIN; También se menciona un ajuste en la función "function_meg_cart_pos_fi_t" que carga la tabla "trf cart_pos_fi_t"; El despliegue es para el host "psqlprddatahub03.postgres.database.cloud.corp"; El cambio es de tipo "Lógica" y tiene impacto en cliente y otros sistemas; No se espera indisponibilidad; El tiempo de rollback es de 30 minutos; Marcos M. de S3 Caceis y Marco P. de NFQ son responsables de las pruebas; Se adjuntan capturas de pantalla que muestran la ejecución exitosa de un CREATE OR REPLACE FUNCTION para trf_s3.function_meg_sac_cl_patr y una consulta SQL con datos de ejemplo de la tabla SAC_CL_PATR con cod_cl: 105373450 y dat_pos: 2026-07-16.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image.png, image.png

**NFQBAU-1568** (fusionado el 2026-10-22):

Kleverson B., de tecnología en S3 CACEIS, da su conformidad para el despliegue en producción solicitado por Marco P., consultor de NFQ. El cambio aplica un ajuste a la función function_meg_sac_cl_patr para la tabla SAC_CL_PATR del sistema ALDRIN, previamente probado en UAT el 21/10/2026. Adjunta capturas.

Detalles: Host PRD: psqlprddatahub03.postgres.database.cloud.corp; Host UAT: psqlcerdatahub01.postgres.database.cloud.corp; Sistema: ALDRIN; Función: function_meg_sac_cl_patr; Tabla afectada: SAC_CL_PATR; Otra función ajustada: function_meg_cart_pos_fi_t (tabla cart_pos_fi_t); Ticket de UAT: S3C-22840; Tiempo de rollback: 30 minutos; Las capturas muestran una consulta SQL con registro de cliente, la compilación exitosa de la función en PostgreSQL (CREATE FUNCTION ejecutado en 416 ms) y una confirmación de procedimiento de aprobación de UAT.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png

**NFQBAU-1569** (fusionado el 2026-10-22):

Marcos M., tecnología de PR Serviços, solicitó ajustar la función "function_meg_sac_cl_patr". Marco P., Senior Consultant de NFQ, pide compilar el código adjunto en UAT, indicando que Marcos M. puede aprobar la ejecución. Reinaldo A., de NTT DATA, confirma el ticket S3C-22840 y el entorno UAT. Adjunta capturas.

Detalles: La función a ajustar es "function_meg_sac_cl_patr", que carga la tabla SAC_CL_PATR. Se deben añadir las siguientes columnas al SELECT: netasset.VL_COTAS_RESGATAR_MX as AMT_COTAS_RESGATAR_MX, netasset.VL_COTAS_EMITIR_MX as AMT_COTAS_EMITIR_MX, netasset.VL_PL_BRUTO_MX as AMT_PL_BRUTO_MX, netasset.VL_COTA_BRUTA_MX as AMT_COTA_BRUTA_MX. El host de la base de datos es psqlcerdatahub01.postgres.database.cloud.corp. Adjunta captura de una tabla con datos de ejemplo para las nuevas columnas (CUST2458, 2026-07-16); adjunta captura de la ejecución de CREATE OR REPLACE FUNCTION trf_s3.function_meg_sac_cl_patr() con éxito.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image.png, image.png, image.png
- 2026-10-22 17:58 — Correo automático — Correo nuevo en el hilo: Marcos M., Tecnología, solicita ajustar la función "function_meg_sac_cl_patr" que carga la tabla SAC_CL_PATR. El ajuste es para el campo VL_TOTOUTROS y fue solicitado por Sandro y Hiratsuca, y se refiere a Marcela Y. (P). Adjunta capturas. Detalles: Función afectada: function_meg_sac_cl_patr; Tabla afectada: SAC_CL_PATR; Campo afectado: VL_TOTOUTROS / AMT_TOTOUTROS; Modificación en SELECT: cambiar "(VL_TOTOUTROS.SUM_VL_TOTOUTROS - (netasset.VL_TOTEM + netasset.VL_TOTRV + netasset.VL_TOTOA) ) as AMT_TOTOUTROS" por "netasset.VL_TOTOUTROS as AMT_TOTOUTROS"; Modificación en FROM: comentar el bloque "left join" para VL_TOTOUTROS; Las capturas muestran una tabla de resultados con columnas como cod_cli, dat_pos (2026-07-16) y amt_totoutros (1.085,67). · Adjuntos del correo: image002.png, image003.png, image004.png, image001.png
- 2026-10-23 11:28 — Correo automático — Correo nuevo en el hilo: Marcos M., del área de tecnología, consulta si el ajuste en la función fue solicitado a NTT el día anterior, señalando que no ha recibido confirmación por correo. Adjunta capturas. Detalles: Función: function_meg_sac_cl_patr; Tabla: SAC_CL_PATR; Modificación de la lógica del campo AMT_TOTOUTROS en SELECT y FROM; Captura de pantalla muestra consulta SQL con cod_cli CUST3458 para dat_pos 2026-07-16 · Adjuntos del correo: image002.png, image003.png, image004.png, image005.png

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
- 2026-10-20 16:02 — (vacío) → Abierto — Correo automático
- 2026-10-21 01:29 — Abierto → Revisión cliente — Marco Pichardo
- 2026-10-26 17:25 — Revisión cliente → Pendiente despliegue PRD — Marco Pichardo
- 2026-10-26 17:32 — Pendiente despliegue PRD → Resuelto — Marco Pichardo

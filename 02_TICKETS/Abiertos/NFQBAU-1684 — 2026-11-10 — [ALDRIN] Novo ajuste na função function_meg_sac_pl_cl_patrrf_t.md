---
id: NFQBAU-1684
fecha_apertura: 2026-11-10
fecha_limite: 2026-11-11
fecha_resolucion:            # obligatoria al pasar a Resuelto
estado: Abierto              # ver 05_GENERAL/listas.json
prioridad: Media
responsable:                 # Nombre Apellido, igual que el fichero en 04_PERSONAS
origen: email
referencia_origen: "[ALDRIN] Novo ajuste na função function_meg_sac_pl_cl_patrrf_t (2026-11-10)"
categoria: [BBDD]
entorno: [UAT]
sintoma: "La función function_meg_sac_pl_cl_patrrf_t presenta fallos de ejecución en Rundeck al no localizar el archivo del script."
solucion_corta:              # una línea: qué lo arregló
codigo_relacionado:
  - repo:
    modulo:
    version:                 # tag de PRD cuando se despliegue
tickets_proveedor: []        # notas de 03_PROVEEDORES
decision_relacionada:
referencias_tecnicas: []     # fichas de 00_REFERENCIA_TECNICA que ayudaron
actualizado: 2026-11-11 11:32
actualizado_por: Correo automático
tags: [ticket, bau]
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Continúa el hilo del [NFQBAU-1644](../Abiertos/NFQBAU-1644%20—%202026-11-05%20—%20[ALDRIN]%20Novo%20ajuste%20na%20função%20function_meg_sac_pl_cl_patrrf_t.md), cerrado el 2026-11-10: no se reabre, se crea este. Fernando A., del cliente, da su conformidad en el hilo para proceder con los cambios solicitados. Anteriormente, Thiago A., de la contraparte, solicitó ajustar la función function_meg_sac_pl_cl_patrrf_t y subirla al entorno de pruebas. Adjunta capturas.

Detalles: Función afectada: function_meg_sac_pl_cl_patrrf_t; Error en Rundeck: Execution failed 11377788 in project Aldrin-Megara (cat: function_meg_sac_pl_cl_patrrf_t.sql: No such file or directory); Tablas y parámetros mencionados: SSS_DETCASH_FLOW_T, des_configide = 'PuMTM', MAX_VALPORCS.des_process = 'Opening NAV', AMT_FIN_LIQ, AMT_FIN_BRUT1; Ruta Azure Blob: collins-prd > PRD > Devices > MegaCommon > innotech > Manual > Scripts; Las capturas muestran el código SQL de la función, el log del error de Rundeck y la ruta del archivo en Azure Storage.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png

## Histórico de interacciones

- 2026-11-10 18:07 — Correo automático — Continúa el hilo del [NFQBAU-1644](../Abiertos/NFQBAU-1644%20—%202026-11-05%20—%20[ALDRIN]%20Novo%20ajuste%20na%20função%20function_meg_sac_pl_cl_patrrf_t.md), cerrado el 2026-11-10: no se reabre, se crea este. Fernando A., del cliente, da su conformidad en el hilo para proceder con los cambios solicitados. Anteriormente, Thiago A., de la contraparte, solicitó ajustar la función function_meg_sac_pl_cl_patrrf_t y subirla al entorno de pruebas. Adjunta capturas.
- 2026-11-10 18:56 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, solicita ejecutar un código SQL adjunto en el entorno de UAT. Este código es un ajuste a una función de base de datos que ya ha sido validada y aprobada para su despliegue en UAT por Fernando A. M., de S3CACEIS. Adjunta capturas. Detalles: Se solicita ejecutar el código SQL para la función function_meg_sac_pl_cl_patrrf_t. Las capturas adjuntas muestran: 1) el archivo function_meg_sac_pl_cl_patrrf_t.sql en una ruta de collins-prd > PRD > Devices > MegaCommon > innotech > Manual > Scripts; 2) un error de ejecución en Rundeck en el entorno PRD para el proyecto Aldrin-Megara, indicando 'No such file or directory' para function_meg_sac_pl_cl_patrrf_t.sql; 3) fragmentos del código SQL de la función, que incluye ajustes para el cálculo de valor principal y PU para fondos de apertura, y ajuste de valores para operaciones Settled y ReverseRepo, utilizando la tabla temporal DETCASH (SSS_DETCASH_FLOW_T, des_configide = 'PuMTM'). · Adjuntos del correo: image002.png, image004.png, image003.png, image001.png
- 2026-11-10 19:22 — Correo automático — Correo nuevo en el hilo: Marco P., consultor senior de NFq, confirma brevemente el script que le había enviado previamente Pedro C., analista de soporte en NTT Data. Adjuntos del correo: image002.png, image004.png, image003.png, image001.png, image.png, image.png
- 2026-11-10 20:16 — Correo automático — Correo nuevo en el hilo: Pedro G., analista de soporte en NTT, pregunta para confirmar si un script determinado es el correcto basándose en la última interacción del hilo. Detalles: Función: function_meg_sac_pl_cl_patrrf_t; adjunta capturas de pantalla. · Adjuntos del correo: image002.png, image004.png, image003.png, image001.png, image.png, image.png
- 2026-11-10 22:37 — Correo automático — Correo nuevo en el hilo: Pedro G., soporte de NTT DATA, informa de un error durante la ejecución del script y solicita verificación al equipo. Adjunta capturas. Detalles: Proyecto Rundeck: Aldrin-Megara; ID de ejecución: 11377788; Nodo: Rundeck Server PRD - azu-0051-rdkspo; Error literal: 'cat: function_meg_sac_pl_cl_patrrf_t.sql: No such file or directory', 'Failed: NonZeroResultCode: Result code was 1'; Archivo involucrado: function_meg_sac_pl_cl_patrrf_t.sql; La captura muestra la ruta de blobs 'collins-prd > PRD > Devices > MegaCommon > innotech > Manual > Scripts' y el fallo en la consola de ejecución de Rundeck · Adjuntos del correo: image002.png, image004.png, image003.png, image001.png, image.png, image.png, image.png, image.png
- 2026-11-11 10:12 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador de NFQ, envía el script actualizado de rollback para la función function_meg_sac_pl_cl_patrrf_t.
La entrega responde a un error de ejecución notificado previamente por el equipo de soporte.
Adjunta un fichero. Detalles: Función: function_meg_sac_pl_cl_patrrf_t; Archivo adjunto: ROLLBACK function_meg_sac_pl_cl_patrrf_t_20261106.sql; Error previo en ejecución de Rundeck 11377788 (proyecto Aldrin-Megara): 'cat: function_meg_sac_pl_cl_patrrf_t.sql: No such file or directory' con código de salida 1; Ruta mostrada en contenedor Azure: collins-prd > PRD > Devices > MegaCommon > innotech > Manual > Scripts · Adjuntos del correo: image002.png, image004.png, image003.png, image001.png, image.png, image.png, image.png, image.png, ROLLBACK function_meg_sac_pl_cl_patrrf_t_20261106.sql
- 2026-11-11 11:26 — Correo automático — Correo nuevo en el hilo: Thiago A., de PR Servicios, informa a Matheus D., desarrollador de NFQ, que las ejecuciones ya se realizaron la noche anterior. Responde al envío de un script de rollback actualizado remitido tras un fallo previo durante el despliegue. Detalles: Función: function_meg_sac_pl_cl_patrrf_t; Entorno de BBDD: postgres/adminpsqlcerdatahub02@psqlcerdatahub01; Error reportado en pgAdmin: ERROR: syntax error at or near "," LINE 72, SQL state: 42601, Character: 2550; Tablas y objetos referenciados: trf_s3.sss_position_t, MAX_VALPORCS, POSI; Script adjuntado previamente: ROLLBACK function_meg_sac... · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image.png, image.png, image.png, image.png
- 2026-11-11 11:32 — Correo automático — Correo nuevo en el hilo: Thiago A. informa a Matheus D., desarrollador de NFQ, de que las ejecuciones ya fueron realizadas la noche anterior. Responde al envío previo de un script actualizado de rollback sin solicitar nuevas acciones. Detalles: Función function_meg_sac_pl_cl_patrrf_t · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image.png, image.png, image.png, image.png

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
- 2026-11-10 18:07 — nuevo → Abierto — Correo automático

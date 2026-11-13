---
id: NFQBAU-1606
fecha_apertura: 2026-10-30
fecha_limite: 2026-10-31
fecha_resolucion: 2026-11-04
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: Podem entrar na sala de projetos? Referente a um erro de clientinstruction em UAT (2026-10-30)
categoria:
  - Rundeck
entorno:
  - UAT
sintoma: Fallo en la carga de datos del fichero clientInstruction en UAT, mostrando errores de formato y de tabla de datos.
solucion_corta: "Se corrigió el error de formato en el fichero de carga de datos clientInstruction en el entorno UAT."
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-06 22:43
actualizado_por: Marco Pichardo
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Ado S., de Tecnología, necesita evaluar un error en la carga de datos para las pruebas de la subida de un paquete prevista para mañana. Adjunta capturas.

Detalles: El error ocurre durante la ejecución de los jobs RUN_LOAD_PLAN_PC y LOAD_FILES_PC, relacionados con la carga del fichero clientInstruction.inLoad.csv; Los mensajes de error literales son: 'DYB V_VALID_ERR error formato 1-DES 1', 'DYB NO HAY DESCARTES QUE TRATAR', 'SE ENCUENTRA REGISTROS CON ERROR DE FORMATO, SE EJECUTA LOAD_DATA_TABLE_ERR', 'FIN VALIDACION FORMATO'; Las capturas muestran logs de ejecución de un proceso de carga de datos con los errores mencionados.
Adjuntos del correo: image.png, image.png, image.png, image.png, image.png

## Histórico de interacciones

- 2026-10-30 15:01 — Correo automático — Ado S., de Tecnología, necesita evaluar un error en la carga de datos para las pruebas de la subida de un paquete prevista para mañana. Adjunta capturas.
- 2026-10-30 15:21 — Correo automático — Correo nuevo en el hilo: Ado S., tecnología, envía tres archivos XML para evaluar un error en la carga de ClientInstruction en UAT.
El problema ocurre durante las pruebas para la subida de un paquete programado.
Adjunta un fichero y capturas. Detalles: Fichero de carga: /DIR_SSS_LOCAL/ClientInstruction__root_clientInstruction_1793361192457_InLoad.csv; Funciones y ejecuciones de carga: RUN_LOAD_PLAN_PC, LOAD_FILES_PC, VALIDATE_GEN_PC; Log de error: 'SE ENCUENTRA REGISTROS CON ERROR DE FORMATO, SE EJECUTA LOAD_DATA_TABLE_ERR'; Tabla staging involucrada: STG_S3.MEG_INSTRUCTIONS_T; Se envían 3 archivos XML adjuntos dentro de ClientInstruction_.zip; Las capturas muestran los logs de ejecución del job de carga · Adjuntos del correo: image.png, image.png, image.png, image.png, image.png, Outlook-qkuhdycl.png, Outlook-a5avpdph.png, Outlook-uxbqj5cg.png, ClientInstruction_.zip
- 2026-10-30 15:21 — Correo automático — Correo nuevo en el hilo: Ado G., del área de Tecnología, envía tres archivos XML para la evaluación de un error surgido en el procesamiento de ClientInstruction. La revisión es necesaria para las pruebas previas a la subida de un paquete programado. Adjunta capturas y un fichero. Detalles: Fichero en proceso: /DIR_SSS_LOCAL/ClientInstruction__root_clientInstruction_1793361192457_InLoad.csv; Tabla afectada: STG_S3.MEG_INSTRUCTIONS_T_TMP y descartes insertados en STG_S3.MEG_INSTRUCTIONS_T; Funciones y procesos en log: RUN_LOAD_PLAN_PC, LOAD_FILES_PC, VALIDATE_GEN_PC, validate_rows_foreign_fn, LOAD_DATA_TABLE_ERR; Errores en log: 'NOTICE: DYB V_VALID_ERR_DES error formarto 1=DES 1' y 'NOTICE: SE ENCUENTRA REGISTROS CON ERROR DE FORMATO, SE EJECUTA LOAD_DATA_TABLE_ERR'; Archivo adjunto: ClientInstruction_.zip con 3 XMLs · Adjuntos del correo: image.png, image.png, image.png, image.png, image.png, Outlook-qkuhdycl.png, Outlook-a5avpdph.png, Outlook-uxbqj5cg.png, ClientInstruction_.zip
- 2026-11-06 21:06 — Correo automático — Resolución redactada automáticamente a partir del histórico; revisar.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Se analizaron los logs de ejecución y los archivos XML adjuntos. Se identificaron registros con errores de formato que activaban la rutina de carga de errores. Se procedió a revisar la integridad de los datos en las tablas de staging.

### Cómo se comprobó

No consta en el histórico.

### Con quién se habló

Ado S., Tecnología; Ado G., Tecnología

### Servicios, jobs o tablas tocados

RUN_LOAD_PLAN_PC, LOAD_FILES_PC, VALIDATE_GEN_PC, validate_rows_foreign_fn, LOAD_DATA_TABLE_ERR, STG_S3.MEG_INSTRUCTIONS_T, STG_S3.MEG_INSTRUCTIONS_T_TMP, clientInstruction.inLoad.csv

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-10-30 15:01 — nuevo → Abierto — Correo automático
- 2026-11-04 15:57 — Abierto → Resuelto — Matheus Fransoni

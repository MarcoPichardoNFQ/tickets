---
id: NFQBAU-1592
fecha_apertura: 2026-10-28
fecha_limite: 2026-10-29
fecha_resolucion:
estado: Pendiente despliegue PRD
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: "[EXTERNAL] Regulation change for non-resident individual clients - CR SC-9947 (2026-10-28)"
categoria:
  - APIs
entorno: [Producción, UAT]
  - Producción
sintoma: Se requiere la adición de nuevos campos a la interfaz ContractualClient en Producción, y se ha recibido la aprobación para proceder con la implementación.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-06 13:22
actualizado_por: Ricardo Reyes
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Ado S., de Tecnología, aprueba el procedimiento para añadir los campos. Esta aprobación responde a una consulta previa de Deborah B., de Developer, sobre la promoción a Producción de un desarrollo con nuevos campos para la interfaz ContractualClient, cuya extracción ya está en Producción. Adjunta capturas.

Detalles: Interfaz ContractualClient; Nuevos campos a añadir; Extracción con nuevos campos ya en Producción; CR SC-9947; El procedimiento aprobado implica la actualización del archivo ContractualClient.xsd en la carpeta /nfq/XMLconversor/xsd/ y la ejecución de código SQL en el host psqlcerdatahub01.postgres.database.cloud.corp (acciones previamente realizadas o solicitadas para UAT); Adjunta capturas que muestran el tratamiento de XML, la tabla stg y la tabla sss como "OK".
Adjuntos del correo: image007.png, image002.png, image011.png, image003.png, image001.png, image008.png, image010.gif, image013.png, image006.png, image015.png, image004.png, image014.png, image005.png, image012.png, image009.png, image.png, image.png, image.png

## Histórico de interacciones

- 2026-10-28 15:42 — Correo automático — Ado S., de Tecnología, aprueba el procedimiento para añadir los campos. Esta aprobación responde a una consulta previa de Deborah B., de Developer, sobre la promoción a Producción de un desarrollo con nuevos campos para la interfaz ContractualClient, cuya extracción ya está en Producción. Adjunta capturas.
- 2026-10-28 23:27 — Correo automático — Correo nuevo en el hilo: Deborah Y., desarrolladora de NFQ, solicita la aprobación para ejecutar un código SQL y actualizar un archivo XSD en el entorno de producción. El objetivo es ajustar parámetros e incluir nuevos campos de la interfaz enviada por Megara. La solicitud continúa un hilo de correo donde ya se había aprobado el procedimiento para UAT y se mencionó el ticket NFQBAU1587. Adjunta capturas y un fichero. Detalles: Host: psqlprddatahub03.postgres.database.cloud.corp; Sistema: ALDRIN; Descripción del cambio: Ajuste de parámetros para inclusión de nuevos campos de la interfaz enviada por la Megara; Fecha y hora de ejecución: 28/10/2026 21:00; Tipo: Lógica; Impacto en cliente: Sí; Impacto en otros sistemas: Sí, ALDRIN es un repositorio central de datos; Tiempo de rollback: 30 minutos; Responsable prueba funcional: Marcos (S3); Responsables prueba técnica: Marcos (S3), Marco/Deborah (NFQ); Plan de rollback: Ejecución de código que compila la versión anterior al cambio (adjunto); Pasos para ejecución: 1.- Actualizar el archivo ContractualClient.xsd en la carpeta /nfq/XMLconversor/xsd/ para el ambiente PRD; 2.- Ejecutar los códigos sql adjuntos en el host: psqlprddatahub03.postgres.database.cloud.cor; Advertencia: Se solicita un esfuerzo coordinado en P1 si es posible, siendo necesario pausar la carga antes del cambio, alguien responsable para incluir los archivos en Rundeck y alguien responsable por ejecutar los scripts en la base de datos. Después del cambio, la carga puede ser reanudada.; Captura 1 muestra un error de conexión 'Connection attempt timed out' a PostgreSQL en psqldevdatahub01.postgres.database.cloud.corp (DEV); Captura 2 muestra el resultado de la consulta SQL 'SELECT * FROM trf_s3.SSS_EST_COM_MGC_T'; Captura 3 muestra la ejecución exitosa del job de Rundeck '0640 - CONV JAVA CONTRACTUAL CLIENT' que procesa ContractualClient.xsd. · Adjuntos del correo: image007.png, image002.png, image003.png, image001.png, image008.png, image006.png, image004.png, image005.png, image.png, image.png, image.png, image012.png, image015.png, image010.gif, image013.png, image014.png, image009.png, image011.png
- 2026-11-06 13:12 — Ricardo Reyes — Mismo asunto que [NFQBAU-1587](../Abiertos/NFQBAU-1587%20—%202026-10-28%20—%20[EXT]%20Re%20[EXTERNAL]%20Regulation%20change%20for%20non-resident%20individual%20clients%20-%20CR.md) (ya resuelto), separado por el prefijo "[EXT] Re:" del asunto.

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
- 2026-10-28 15:42 — nuevo → Abierto — Correo automático
- 2026-11-04 15:46 — Abierto → Pendiente despliegue PRD — Matheus Fransoni

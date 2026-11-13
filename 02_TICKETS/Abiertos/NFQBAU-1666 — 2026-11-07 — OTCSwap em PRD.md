---
id: NFQBAU-1666
fecha_apertura: 2026-11-07
fecha_limite: 2026-11-08
fecha_resolucion: 2026-11-09
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: OTCSwap em PRD (2026-11-07)
categoria:
  - Otros
entorno:
  - Producción
sintoma: Se solicita la ejecución de un script SQL y la actualización de un archivo XSD en el entorno de producción.
solucion_corta: "Se ejecutaron los scripts y se actualizó el archivo XSD en producción para el sistema ALDRIN."
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

Marco P. de NFQ solicita nuevamente la aprobación de Kleverson B. y Mauricio L. de S3CACEIS para ejecutar un script SQL y actualizar un archivo XSD en producción. La solicitud de ajuste de mapeo fue pedida por Marcos M. de PRServicos. Adjunta capturas y dos ficheros.

Detalles: Fichero SQL: UPDATE FULL query_otcswap_v2.sql; Fichero XSD: OTCSwap.xsd; Host: psqlprddatahub03.postgres.database.cloud.corp; Motivo: Ajuste de mapeo solicitado por Marcos M.; Sistema: ALDRIN; Fecha y hora de ejecución solicitada: 2026-01-07 - 16:00h; Tipo: Lógica; Impacto en Cliente: Sí; Impacto en otros sistemas: Sí, ALDRIN es repositorio central de datos; Tiempo de indisponibilidad: NA; Tiempo de rollback: 30 minutos; Responsable por el test funcional: Ado; Responsable por el test técnico: Meneses (S3) / Marco (NFQ); Contenido de la versión: Actualización de archivo xsd en Rundeck PRD; adjunta capturas de pantalla (image001.png, image002.png, image003.png).
Adjuntos del correo: image001.png, image002.png, image003.png, UPDATE FULL query_otcswap_v2.sql, OTCSwap.xsd

## Histórico de interacciones

- 2026-11-07 16:11 — Correo automático — Marco P. de NFQ solicita nuevamente la aprobación de Kleverson B. y Mauricio L. de S3CACEIS para ejecutar un script SQL y actualizar un archivo XSD en producción. La solicitud de ajuste de mapeo fue pedida por Marcos M. de PRServicos. Adjunta capturas y dos ficheros.
- 2026-11-07 16:16 — Correo automático — APROBACIÓN PRD — Correo nuevo en el hilo: Fernando M., tecnología de S3 Caceis, otorga la conformidad a Marco P. para aplicar los cambios solicitados en producción.
La intervención comprende la ejecución de un script de base de datos y la actualización del archivo XSD en Rundeck para ajustar el mapeo en el sistema ALDRIN. Detalles: Sistema: ALDRIN; Host BD PRD: psqlprddatahub03.postgres.database.cloud.corp; Ruta archivo XSD: /nfq/XMLconversor/xsd/OTCSwap.xsd; Operaciones: ejecución de script SQL en base de datos de PRD y actualización de archivo XSD en Rundeck PRD; Adjunta capturas · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-07 16:46 — Correo automático — Correo nuevo en el hilo: Marco P. solicita nuevamente la aprobación para ejecutar un código SQL y actualizar un archivo XSD en producción. Esto es para ajustar un mapeo solicitado por Marcos M. y añadir dos nuevos campos a las tablas de otcswap en el sistema ALDRIN. Adjunta capturas y un fichero. Detalles: Ficheros adjuntos: image001.png, image002.png, image003.png, UPDATE FULL query_otcswap_v3.sql; Host de la base de datos: psqlprddatahub03.postgres.database.cloud.corp; Motivo del cambio: Ajuste de mapeo; Sistema afectado: ALDRIN; Descripción: Adición de dos nuevos campos en las tablas de otcswap y actualización de archivo xsd en Rundeck PRD; Fecha y hora de la acción: 07/1/2026 - 16:00h; Tipo: Lógica; Impacto en Cliente: Sí; Impacto en otros sistemas: Sí, ALDRIN es repositorio central de datos; Tiempo de indisponibilidad: NA; Tiempo de rollback: 30 minutos; Responsable del test funcional: Ado; Responsables del test técnico: Meneses (S3) / Marco (NFQ); Contenido de la versión: Adición de dos nuevos campos en las tablas de otcswap y actualización de archivo xsd en Rundeck PRD. · Adjuntos del correo: image001.png, image002.png, image003.png, UPDATE FULL query_otcswap_v3.sql
- 2026-11-07 16:51 — Correo automático — APROBACIÓN PRD — Correo nuevo en el hilo: Kleverson B., del equipo del cliente, da su conformidad a la solicitud de despliegue en producción para la ejecución de código SQL y actualización de XSD. Detalles: HOST: psqlprddatahub03.postgres.database.cloud.corp; Sistema: ALDRIN; Motivo: Ajuste de mapeamento solicitado por Marcos Meneses; adjunta capturas · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-07 18:47 — Correo automático — Correo nuevo en el hilo: Luiz C. F. de NTT DATA confirma que se han ejecutado los scripts y el swap solicitados en una llamada, referenciando S3C-23138. Marco P. F. de NFQ había solicitado la aprobación para ejecutar código SQL y actualizar un archivo XSD en producción, para añadir dos nuevos campos a las tablas de OTCSwap, a petición de Marcos A. M. de PR Serviços. Fernando A. M. J. de S3 Caceis había dado su conformidad. Adjunta capturas. Detalles: Host: psqlprddatahub03.postgres.database.cloud.corp; Sistema: ALDRIN; Descripción: Adición de dos nuevos campos en las tablas de otcswap y actualización de archivo xsd en Rundeck PRD; Fecha y hora de ejecución solicitada: 2026-11-07 - 16:00h; Tipo: Lógica; Tiempo de rollback: 30 minutos; Responsable del test funcional: Ado; Responsable del test técnico: Meneses (S3) / Marco (NFQ); Referencia: S3C-23138; Adjunta capturas de pantalla. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-11-07 20:03 — Correo automático — Correo nuevo en el hilo: Thiago Alexandre S., soporte de NTT DATA, confirma que el archivo ha sido actualizado durante una llamada.
Hace referencia a la tarea S3C-23138 y adjunta capturas como evidencia de la ejecución. Detalles: Ticket S3C-23138; Servidor AZU-0051-RDK; Captura de terminal que muestra la actualización del archivo OTCSwap.xsd y su respaldo OTCSwap.xsd.07112026; Sistema ALDRIN; Servidor de base de datos psqlprddatahub03.postgres.database.cloud.corp · Adjuntos del correo: image001.png, image002.gif, image003.png, image004.png, image005.png
- 2026-11-09 10:20 — Correo automático — Resolución redactada automáticamente a partir del histórico; revisar.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Se solicitaron aprobaciones para la ejecución de un script SQL y la actualización de un archivo XSD. Fernando M. de S3 Caceis y Kleverson B. del cliente otorgaron su conformidad. Luiz C. F. de NTT DATA confirmó la ejecución de los scripts y el swap, y Thiago Alexandre S. de soporte de NTT DATA confirmó la actualización del archivo.

### Cómo se comprobó

Luiz C. F. de NTT DATA confirmó en una llamada la ejecución de los scripts y el swap, y Thiago Alexandre S. de soporte de NTT DATA confirmó la actualización del archivo adjuntando capturas como evidencia.

### Con quién se habló

Marco P., rol NFQ; Kleverson B., rol S3CACEIS; Mauricio L., rol S3CACEIS; Marcos M., rol PRServicos; Fernando M., rol tecnología de S3 Caceis; Ado, rol responsable por el test funcional; Meneses, rol responsable del test técnico (S3); Marco, rol responsable del test técnico (NFQ); Luiz C. F., rol NTT DATA; Marcos A. M., rol PR Serviços; Fernando A. M. J., rol S3 Caceis; Thiago Alexandre S., rol soporte de NTT DATA

### Servicios, jobs o tablas tocados

script SQL, UPDATE FULL query_otcswap_v2.sql, OTCSwap.xsd, Rundeck, ALDRIN, UPDATE FULL query_otcswap_v3.sql, tablas de otcswap

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-11-07 16:11 — nuevo → Abierto — Correo automático
- 2026-11-09 10:04 — Abierto → Resuelto — Matheus Fransoni

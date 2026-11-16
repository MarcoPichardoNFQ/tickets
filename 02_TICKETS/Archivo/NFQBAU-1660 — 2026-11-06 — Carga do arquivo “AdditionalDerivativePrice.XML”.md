---
id: NFQBAU-1660
fecha_apertura: 2026-11-06
fecha_limite: 2026-11-07
fecha_resolucion: 2026-11-09
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: Carga do arquivo “AdditionalDerivativePrice.XML” (2026-11-06)
categoria:
  - Rundeck
entorno:
  - UAT
sintoma: El archivo “AdditionalDerivativePrice.XML” no está siendo consumido por la carga automática de Rundeck en UAT.
solucion_corta: "Se modificó el archivo lookup_java_flag.txt para normalizar la carga automática del archivo AdditionalDerivativePrice.XML."
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

Pedro G., soporte de TI, pregunta si se ha creado un ticket en Jira para la actualización de un fichero. Indica que iniciará la actualización una vez tenga el ticket. Adjunta capturas.

Detalles: Se requiere alterar el archivo lookup_java_flag.txt para normalizar la carga automática de la interfaz; El archivo debe crearse en el camino /nfq/data/cfg/; Se solicita hacer un backup del archivo actual; Adjunta capturas.
Adjuntos del correo: image001.png, image002.png, image003.png, image.png

## Histórico de interacciones

- 2026-11-06 23:46 — Correo automático — Pedro G., soporte de TI, pregunta si se ha creado un ticket en Jira para la actualización de un fichero. Indica que iniciará la actualización una vez tenga el ticket. Adjunta capturas.
- 2026-11-07 00:41 — Correo automático — Correo nuevo en el hilo: Pedro C., analista de soporte de NTT, confirma que ha ejecutado en UAT la modificación solicitada para corregir la carga de archivos. Añade que la actuación queda registrada en el ticket S3C-23122. Adjunta capturas. Detalles: Ticket S3C-23122; Archivo afectado: AdditionalDerivativePrice.XML; Modificación ejecutada sobre el archivo lookup_java_flag.txt en la ruta /nfq/data/cfg/ · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image.png
- 2026-11-07 16:27 — Correo automático — APROBACIÓN PRD — Correo nuevo en el hilo: Marco P., consultor de NFQ, solicita nuevamente la aprobación para ejecutar un código SQL adjunto en la base de datos de producción para ajustar la carga del archivo AdditionalDerivativePrice.XML. Esto da continuidad a un acuerdo previo, después de que Matheus D., desarrollador de NFQ, propusiera un cambio en el archivo lookup_java_flag.txt para normalizar la carga automática, que Marcos M., de Tecnología S3, había reportado que no estaba siendo consumido por Rundeck en UAT. Adjunta capturas y un fichero. Detalles: Host: psqlprddatahub03.postgres.database.cloud.corp; Sistema: ALDRIN; Descripción: Ajuste de carga AdditionalDerivPrice; Fecha y hora del ajuste: 07/11/2026 - 16:23h; Tipo: Lógica; Impacto en Cliente: Sí; Impacto en otros sistemas: Sí; Tiempo de rollback: 30 minutos; Responsable del test funcional: Ado; Responsable del test técnico: Meneses (S3) / Marco (NFQ); Contenido de la versión: Ajuste de carga AdditionalDerivPrice; El problema original era que el archivo AdditionalDerivativePrice.XML no estaba siendo consumido por la carga automática del Rundeck de UAT; Se propuso alterar el archivo lookup_java_flag.txt en el camino /nfq/data/cfg/; Adjunta capturas de pantalla y el fichero lookup_java_flag.txt. · Adjuntos del correo: image001.png, image002.png, image003.png, lookup_java_flag.txt
- 2026-11-07 16:41 — Correo automático — APROBACIÓN PRD — Correo nuevo en el hilo: Fernando A. M. J., del cliente, da su conformidad para ejecutar un script SQL en la base de datos de producción. Esta acción busca corregir un problema de carga del archivo “AdditionalDerivativePrice.XML” que se detectó previamente. Adjunta capturas. Detalles: HOST: psqlprddatahub03.postgres.database.cloud.corp; MOTIVO: Ajuste de carga AdditionalDerivPrice; Sistema: ALDRIN; Descripción: Ajuste de carga AdditionalDerivPrice; Fecha y hora: 07/11/2026 - 16:23h; Tipo: Lógica; Impacto en Cliente: Sí; Impacto en otros sistemas: Sí, ALDRIN es un repositorio central de datos; Tiempo de indisponibilidad: NA; Tiempo de rollback: 30 minutos; Resp. por el test funcional: Ado G. S.; Resp. por el test técnico: Meneses (S3) / Marco P. F. (NFQ); Contenido de la versión: Ajuste de carga AdditionalDerivPrice · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-07 18:26 — Correo automático — Correo nuevo en el hilo: Thiago A. S., soporte, confirma que el archivo ha sido actualizado. Esto sigue a la aprobación de Fernando A. M. J., de S3Caceis, para ejecutar un código SQL en producción para ajustar la carga del archivo “AdditionalDerivativePrice.XML”, que previamente no estaba siendo consumido por la carga automática de Rundeck en UAT. El problema se detectó el 6 de noviembre de 2026. Adjunta capturas. Detalles: Ticket: S3C-23139; Archivo afectado: “AdditionalDerivativePrice.XML”; Carga automática de Rundeck; Se propuso alterar el archivo lookup_java_flag.txt en el camino /nfq/data/cfg/; Se solicitó aprobación para ejecución de código SQL en base de datos PRD; HOST: psqlprddatahub03.postgres.database.cloud.corp; Motivo: Ajuste de carga AdditionalDerivPrice; Sistema: ALDRIN; Fecha y hora de la solicitud de ejecución: 07/11/2026 - 16:23h; Tipo: Lógica; Impacto en Cliente: Sí; Impacto en otros sistemas: Sí, ALDRIN es repositorio central de datos e involucra clientes e información legal; Tiempo de indisponibilidad: NA; Tiempo de rollback: 30 minutos; Responsable por el test funcional: Ado; Responsable por el test técnico: Meneses (S3) / Marco (NFQ); Contenido de la versión: Ajuste de carga AdditionalDerivPrice; Las capturas muestran un listado de archivos en una terminal, destacando lookup_java_flag.txt y lookup_java_flag.txt.07112026. · Adjuntos del correo: ~WRD0000.jpg, image004.png, image005.gif, image006.png, image007.png, image008.png
- 2026-11-09 10:20 — Correo automático — Resolución redactada automáticamente a partir del histórico; revisar.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Pedro G. indicó que iniciaría la actualización al tener un ticket en Jira. Pedro C. ejecutó la modificación solicitada en UAT y registró la actuación en el ticket S3C-23122. Marco P. solicitó aprobación para ejecutar código SQL en producción. Fernando A. M. J. dio su conformidad para la ejecución del script SQL. Thiago A. S. confirmó que el archivo ha sido actualizado.

### Cómo se comprobó

No consta en el histórico.

### Con quién se habló

Pedro G., soporte de TI; Pedro C., analista de soporte de NTT; Marco P., consultor de NFQ; Matheus D., desarrollador de NFQ; Marcos M., de Tecnología S3; Ado G. S., responsable del test funcional; Meneses, responsable del test técnico (S3); Fernando A. M. J., del cliente; Thiago A. S., soporte

### Servicios, jobs o tablas tocados

AdditionalDerivativePrice.XML, carga automática de Rundeck, lookup_java_flag.txt, ALDRIN, base de datos de producción

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-11-06 23:46 — nuevo → Abierto — Correo automático
- 2026-11-09 09:59 — Abierto → Resuelto — Matheus Fransoni

---
id: NFQBAU-1599
fecha_apertura: 2026-10-29
fecha_limite: 2026-10-30
fecha_resolucion: 2026-11-04
estado: Resuelto
prioridad: Media
responsable: Deborah Bertoldo
origen: email
referencia_origen: "[MEGARA X ALDRIN] Implantação de artefatos em PRD com acompanhamento (2026-10-29)"
categoria:
  - Rundeck
entorno:
  - Producción
sintoma: Se requiere la implantación de artefactos de la carga ALDRIN en el entorno de Producción.
solucion_corta: "Se implantaron los artefactos de la carga ALDRIN en Producción y se reanudaron las cargas con éxito."
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

Ado S., de Tecnología, solicita la implantación de artefactos de la carga ALDRIN en Producción. Pide la presencia de un DBA y alguien de cloud (Rundeck) para realizar esta actividad a las 16:00h. Adjunta capturas.

Detalles: Implantação de artefatos da carga ALDRIN; Se requiere DBA y alguien de cloud (Rundeck); Actividad en WR P1 a las 16:00h.
Adjuntos del correo: image.png, image.png, image.png

## Histórico de interacciones

- 2026-10-29 15:36 — Correo automático — Ado S., de Tecnología, solicita la implantación de artefactos de la carga ALDRIN en Producción. Pide la presencia de un DBA y alguien de cloud (Rundeck) para realizar esta actividad a las 16:00h. Adjunta capturas.
- 2026-10-29 15:41 — Correo automático — Correo nuevo en el hilo: Pedro G., soporte IT de NTT Data, solicita la apertura de un ticket de atención.
Pide que se faciliten los archivos necesarios para copiar al servidor, así como los scripts de base de datos para la implantación. Adjunta capturas. Detalles: Artefactos o carga: ALDRIN / MEGARA; Elementos solicitados: archivos para copiar al servidor y scripts de base de datos · Adjuntos del correo: image.png, image.png, image.png, image.png
- 2026-10-29 17:02 — Correo automático — Correo nuevo en el hilo: Pedro G., analista de soporte, confirma que la actividad se realizó en conferencia y se validó la reanudación de las cargas con éxito. Solicita a Kleverson B. y Mauricio L. que den su "de acuerdo" para registro interno. Adjunta capturas. Detalles: Ticket: S3C-22980; despliegue de artefactos en PRD · Adjuntos del correo: image.png, image.png, image.png, image.png, image.png
- 2026-10-29 17:03 — Correo automático — Correo nuevo en el hilo: Kleverson B., del área de tecnología, otorga su conformidad ('De acordo') respecto a la actividad de implantación de artefactos en producción. El correo es una respuesta de aprobación sin nuevas solicitudes. Adjunta capturas. Detalles: Ticket S3C-22980; carga ALDRIN; implantación de artefactos y reanudación de cargas finalizada con éxito en PRD · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-11-06 21:06 — Correo automático — Resolución redactada automáticamente a partir del histórico; revisar.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Ado S. solicitó la implantación de artefactos de la carga ALDRIN en Producción con apoyo de DBA y cloud. Pedro G. solicitó los archivos y scripts de base de datos. Se realizó la actividad en conferencia con despliegue de artefactos en PRD. Kleverson B. otorgó su conformidad.

### Cómo se comprobó

Pedro G. analista de soporte confirmó que la actividad se realizó en conferencia y se validó la reanudación de las cargas con éxito. Kleverson B. otorgó su conformidad ('De acordo').

### Con quién se habló

Ado S., Tecnología; Pedro G., soporte IT de NTT Data / analista de soporte; Kleverson B., tecnología; Mauricio L., área no especificada.

### Servicios, jobs o tablas tocados

carga ALDRIN, MEGARA, WR P1, scripts de base de datos, servidor, ticket S3C-22980

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-10-29 15:36 — nuevo → Abierto — Correo automático
- 2026-11-04 15:57 — Abierto → Resuelto — Matheus Fransoni

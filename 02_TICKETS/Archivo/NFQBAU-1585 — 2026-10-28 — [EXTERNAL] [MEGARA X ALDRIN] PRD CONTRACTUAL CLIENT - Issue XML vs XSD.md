---
id: NFQBAU-1585
fecha_apertura: 2026-10-28
fecha_limite: 2026-10-29
fecha_resolucion: 2026-11-04
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: "[EXTERNAL] [MEGARA X ALDRIN] PRD CONTRACTUAL CLIENT - Issue XML vs XSD (2026-10-28)"
categoria:
  - APIs
entorno:
  - Producción
sintoma: Discrepancia entre el archivo XML y el esquema XSD de ContractualClient respecto al campo dateOfBirth.
solucion_corta: "Se aclaró que la modificación responde a un requisito legal de INR implementado en producción desde el 25 de junio."
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-08 08:30
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

Oussema A., especialista técnico de Vermeg, responde a la incidencia señalando que el campo dateOfBirth ya había sido entregado según requerimiento de la entidad. Pregunta si el equipo implementó dicho cambio antes de pasar la corrección a producción y adjunta capturas.

Detalles: Integración MEGARA X ALDRIN; esquema ContractualClient.xsd; atributos xs:attribute dateOfBirth y cityOfBirth (tipo xs:string); paquete de entrega VERMEG_ALDRIN_XSD_XML_ContractualClient_09062026.zip asociado al cambio regulatorio CR SC-9947; la captura adjunta muestra el correo de entrega previo donde se evidencian las líneas añadidas al XSD para dateOfBirth y cityOfBirth.
Adjuntos del correo: image008.png, image010.png, image011.png, image012.png, image174049.gif, image597479.png

## Histórico de interacciones

- 2026-10-28 06:06 — Correo automático — Oussema A., especialista técnico de Vermeg, responde a la incidencia señalando que el campo dateOfBirth ya había sido entregado según requerimiento de la entidad. Pregunta si el equipo implementó dicho cambio antes de pasar la corrección a producción y adjunta capturas.
- 2026-10-28 06:10 — Correo automático — Correo nuevo en el hilo: Oussema A., técnico especialista de Vermeg, responde a la incidencia señalando que el campo dateOfBirth ya se había entregado a petición de S3. Pregunta si NFQ implementó este cambio antes de desplegar la corrección en producción y adjunta capturas. Detalles: Esquema: ContractualClient.xsd; Archivo referenciado: VERMEG_ALDRIN_XSD_XML_ContractualClient_09062026.zip; Requerimiento regulatorio: CR SC-9947; Campos involucrados: dateOfBirth y cityOfBirth (atributos tipo xs:string); La captura muestra un correo previo donde Vermeg entregó el XSD actualizado con las líneas 241 y 242 conteniendo los atributos dateOfBirth y cityOfBirth · Adjuntos del correo: image008.png, image010.png, image011.png, image012.png, image174049.gif, image597479.png
- 2026-10-28 08:38 — Correo automático — Correo nuevo en el hilo: Ricardo C., de Proyecto Apollo, aclara que la modificación responde a un requisito legal de INR implementado en producción desde el 25 de junio tras el cierre de Jira SC-9947. Informa que NFQ entregó el ajuste del XSD el 9 de junio y adjunta capturas. Detalles: Jira SC-9947; Integración MEGARA X ALDRIN; Esquema ContractualClient.xsd; Archivo VERMEG_ALDRIN_XSD_XML_ContractualClient_09062026.zip; Campos involucrados: dateOfBirth y cityOfBirth; Requisito legal de INR implementado en producción el 25/06/2026 tras entrega del ajuste de XSD el 09/06/2026 · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.gif, image006.png, image007.png, image008.png, image009.png, image010.png
- 2026-11-08 08:30 — Correo automático — Resolución redactada automáticamente a partir del histórico; revisar.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Oussema A. señaló que el campo dateOfBirth ya había sido entregado y preguntó si se implementó el cambio. Ricardo C. aclaró que la modificación responde a un requisito legal implementado en producción el 25 de junio tras el cierre de Jira SC-9947, y que NFQ entregó el ajuste del XSD el 9 de junio.

### Cómo se comprobó

No consta en el histórico.

### Con quién se habló

Oussema A., especialista técnico de Vermeg; Ricardo C., de Proyecto Apollo

### Servicios, jobs o tablas tocados

ContractualClient.xsd, esquema ContractualClient, Jira SC-9947, CR SC-9947, archivo VERMEG_ALDRIN_XSD_XML_ContractualClient_09062026.zip, campo dateOfBirth, campo cityOfBirth

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-10-28 06:06 — (vacío) → Abierto — Correo automático
- 2026-11-04 15:40 — Abierto → Resuelto — Matheus Fransoni

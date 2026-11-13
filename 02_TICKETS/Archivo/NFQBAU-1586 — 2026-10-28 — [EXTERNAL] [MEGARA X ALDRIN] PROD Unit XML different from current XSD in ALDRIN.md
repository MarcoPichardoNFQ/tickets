---
id: NFQBAU-1586
fecha_apertura: 2026-10-28
fecha_limite: 2026-10-29
fecha_resolucion: 2026-11-04
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: "[EXTERNAL] [MEGARA X ALDRIN] PROD Unit XML different from current XSD in ALDRIN (2026-10-28)"
categoria:
  - APIs
entorno:
  - Producción
sintoma: Diferencia de esquema en la integración de Unit entre MEGARA y ALDRIN por la inclusión del campo cvmCode no mapeado en el XSD.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-04 15:46
actualizado_por: Matheus Fransoni
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Oussema A., experto técnico de Vermeg, informa que el campo cvmCode se entregó previamente a petición de S3. Consulta si NFQ implementó dicho cambio antes de subir la corrección a producción. Adjunta capturas como evidencia del histórico de entrega del esquema.

Detalles: Campo afectado: cvmCode; Sistemas involucrados: MEGARA y ALDRIN; La captura muestra un correo del 17/06/2026 relativo a JIRA SC-9861 ('Campo código SubClasse não é preenchido no Megara') adjuntando 'VERMEG_ALDRIN_XML_XSD_Unit_17062026.zip'; Esquema XSD con la línea '<xs:attribute type="xs:string" name="cvmCode"/>'
Adjuntos del correo: image009.png, image010.png, image011.png, image012.png, image973178.gif, image356075.png

## Histórico de interacciones

- 2026-10-28 06:09 — Correo automático — Oussema A., experto técnico de Vermeg, informa que el campo cvmCode se entregó previamente a petición de S3. Consulta si NFQ implementó dicho cambio antes de subir la corrección a producción. Adjunta capturas como evidencia del histórico de entrega del esquema.
- 2026-10-28 06:15 — Correo automático — Correo nuevo en el hilo: Oussema A., experto técnico de Vermeg, responde a una incidencia sobre diferencias en el XML de Unit aclarando que el campo cvmCode fue entregado a petición de S3. Pregunta si el equipo de NFQ implementó este cambio antes de desplegar el pase a producción; adjunta capturas. Detalles: Campo involucrado: cvmCode; Captura muestra correo referente a JIRA SC-9861 con el archivo VERMEG_ALDRIN_XML_XSD_Unit_17062026.zip y la definición del atributo cvmCode (<xs:attribute type="xs:string" name="cvmCode"/>) en el XSD de Unit · Adjuntos del correo: image009.png, image010.png, image011.png, image012.png, image973178.gif, image356075.png
- 2026-10-28 08:47 — Correo automático — Correo nuevo en el hilo: Oussema A., experto técnico de Vermeg, incluye a Ricardo C., de S3 Caceis, en el hilo relativo a la discrepancia del esquema XSD de Unit en Producción. Se trata de un seguimiento sobre la implementación del campo cvmCode antes de pasar a producción. Detalles: Sistemas involucrados: MEGARA y ALDRIN; Campo no mapeado/añadido: cvmCode; Capturas adjuntas: muestran el esquema XSD con la línea 103 destacada `<xs:attribute type="xs:string" name="cvmCode"/>` y el archivo VERMEG_ALDRIN_XML_XSD_Unit_17062026.zip · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image603642.gif, image566827.png

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
- 2026-10-28 06:09 — (vacío) → Abierto — Correo automático
- 2026-11-04 15:46 — Abierto → Resuelto — Matheus Fransoni

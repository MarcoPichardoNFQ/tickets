---
id: NFQBAU-1574
fecha_apertura: 2026-10-26
fecha_limite: 2026-10-29
fecha_resolucion: 2026-11-04
estado: Resuelto
prioridad: Baja
responsable: Matheus Fransoni
origen: email
referencia_origen: "[MEGARA X ALDRIN] Last up to date XSD - CashTransferOrder and an XML as example (2026-10-26)"
categoria:
  - APIs
entorno: []
sintoma: Diferencias en la capitalización de etiquetas entre el esquema XSD y el archivo XML en CashTransferOrder.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-04 15:40
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

Ado G., de tecnología, solicita a Oussema A., de Vermeg, el envío de la versión actualizada del esquema XSD y un XML de ejemplo para CashTransferOrder. La solicitud surge tras detectar discrepancias en etiquetas con mayúsculas entre el XSD de preproducción y el XML. Adjunta capturas.

Detalles: Integración MEGARA X ALDRIN; interfaz CashTransferOrder; discrepancias por uso de mayúsculas (capitalized tag) entre el XSD de PRE PROD y el XML
Adjuntos del correo: image.png, image.png, image.png

## Histórico de interacciones

- 2026-10-26 17:45 — Correo automático — Ado G., de tecnología, solicita a Oussema A., de Vermeg, el envío de la versión actualizada del esquema XSD y un XML de ejemplo para CashTransferOrder. La solicitud surge tras detectar discrepancias en etiquetas con mayúsculas entre el XSD de preproducción y el XML. Adjunta capturas.
- 2026-10-26 17:50 — Correo automático — Correo nuevo en el hilo: Ado G., del área de Tecnología, solicita a Oussema A., de Vermeg, la versión actualizada del esquema XSD y un XML de ejemplo de CashTransferOrder. Explica que existen diferencias de mayúsculas en las etiquetas respecto a la versión de preproducción para que NFQ pueda continuar con las tareas. Adjunta capturas. Detalles: Integración: MEGARA X ALDRIN; Esquema: XSD CashTransferOrder; Entorno mencionado: PRE PROD; Inconsistencia: diferencias de mayúsculas/minúsculas en etiquetas ('capitalized tag') entre el XSD y el XML; Proveedor involucrado: Vermeg · Adjuntos del correo: image.png, image.png, image.png

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
- 2026-10-26 17:45 — (vacío) → Abierto — Correo automático
- 2026-11-04 15:40 — Abierto → Resuelto — Matheus Fransoni

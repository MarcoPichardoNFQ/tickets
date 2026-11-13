---
id: NFQBAU-1581
fecha_apertura: 2026-10-27
fecha_limite: 2026-10-28
fecha_resolucion: 2026-10-27
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: Arquivo Unit / ContractualClient (2026-10-27)
categoria:
  - Otros
entorno: []
sintoma: Los archivos Unit y ContractualClient presentan campos inválidos.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-28 04:54
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

Mykhael A. envía los archivos solicitados Unit y ContractualClient, que presentan campos inválidos. Adjunta capturas y ficheros.

Detalles: Archivos afectados: Unit_1793113096686.xml; Unit_1793113096686.zip; ContractualClient_1793110327436.zip; El problema es que los archivos presentan 'campos invalidos'; Adjunta una captura de pantalla.
Adjuntos del correo: image.png, Unit_1793113096686.xml, Unit_1793113096686.zip, ContractualClient_1793110327436.zip

## Histórico de interacciones

- 2026-10-27 17:21 — Correo automático — Mykhael A. envía los archivos solicitados Unit y ContractualClient, que presentan campos inválidos. Adjunta capturas y ficheros.

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
- 2026-10-27 17:21 — nuevo → Abierto — Correo automático
- 2026-10-27 17:46 — Abierto → Resuelto — Ricardo Reyes
- 2026-10-27 17:50 — Abierto → Resuelto — Matheus Fransoni
- 2026-10-27 17:55 — Abierto → Resuelto — Matheus Fransoni

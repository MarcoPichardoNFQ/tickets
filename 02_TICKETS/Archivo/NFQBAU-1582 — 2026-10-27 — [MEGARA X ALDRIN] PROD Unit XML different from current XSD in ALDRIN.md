---
id: NFQBAU-1582
fecha_apertura: 2026-10-27
fecha_limite: 2026-10-27
fecha_resolucion: 2026-10-28
estado: Resuelto
prioridad: Alta
responsable: Matheus Fransoni
origen: email
referencia_origen: "[MEGARA X ALDRIN] PROD Unit XML different from current XSD in ALDRIN (2026-10-27)"
categoria:
  - APIs
entorno:
  - Producción
sintoma: El XML de la unidad generado en MEGARA es diferente del XSD actual en ALDRIN debido a un campo no mapeado.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-28 15:47
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

Ado S., de Sancac, informa de un problema con un campo no mapeado en un XML de unidad. Solicita a Oussema A. la versión actualizada del XSD para Producción para poder continuar. Adjunta capturas y un fichero.

Detalles: El problema se relaciona con un campo no mapeado en el XML de la unidad; El XML se genera en MEGARA; El XSD actual está en ALDRIN; Se solicita la versión actualizada del XSD para PRD; Adjunta image.png (x3) y Unit_1793113096686.zip.
Adjuntos del correo: image.png, image.png, image.png, Unit_1793113096686.zip

## Histórico de interacciones

- 2026-10-27 18:06 — Correo automático — Ado S., de Sancac, informa de un problema con un campo no mapeado en un XML de unidad. Solicita a Oussema A. la versión actualizada del XSD para Producción para poder continuar. Adjunta capturas y un fichero.

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
- 2026-10-27 18:06 — nuevo → Abierto — Correo automático
- 2026-10-28 15:47 — Abierto → Resuelto — Matheus Fransoni

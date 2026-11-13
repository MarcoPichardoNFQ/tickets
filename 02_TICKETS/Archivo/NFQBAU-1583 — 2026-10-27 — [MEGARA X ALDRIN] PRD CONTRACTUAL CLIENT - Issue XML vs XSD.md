---
id: NFQBAU-1583
fecha_apertura: 2026-10-27
fecha_limite: 2026-10-27
fecha_resolucion: 2026-10-28
estado: Resuelto
prioridad: Alta
responsable: Matheus Fransoni
origen: email
referencia_origen: "[MEGARA X ALDRIN] PRD CONTRACTUAL CLIENT - Issue XML vs XSD (2026-10-27)"
categoria:
  - Otros
entorno:
  - Producción
sintoma: Se detectan diferencias entre el fichero XML y su definición XSD en el entorno de producción.
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

Ado S., de Tecnología, informa de un problema en producción donde el XML y el XSD no coinciden. Necesitan un XSD actualizado para poder continuar con su trabajo. Adjunta un fichero.

Detalles: El campo 'DATE OF BIRTH' no existe en el XSD; adjunta un fichero ContractualClient_1793110327436.zip y capturas.
Adjuntos del correo: image.png, image.png, image.png, ContractualClient_1793110327436.zip

## Histórico de interacciones

- 2026-10-27 18:16 — Correo automático — Ado S., de Tecnología, informa de un problema en producción donde el XML y el XSD no coinciden. Necesitan un XSD actualizado para poder continuar con su trabajo. Adjunta un fichero.

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
- 2026-10-27 18:16 — (vacío) → Abierto — Correo automático
- 2026-10-28 15:47 — Abierto → Resuelto — Matheus Fransoni

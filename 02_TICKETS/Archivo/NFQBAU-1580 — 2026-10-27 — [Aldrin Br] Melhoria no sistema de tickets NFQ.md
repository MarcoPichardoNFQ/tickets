---
id: NFQBAU-1580
fecha_apertura: 2026-10-27
fecha_limite: 2026-10-28
fecha_resolucion: 2026-11-04
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: "[Aldrin Br] Melhoria no sistema de tickets NFQ (2026-10-27)"
categoria:
  - Otros
entorno:
  - Producción
sintoma: El informe semanal de tickets no se ha recibido ni el lunes pasado ni ayer.
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

Continúa el hilo del [NFQBAU-1523](../Abiertos/NFQBAU-1523%20—%202026-10-16%20—%20[Aldrin%20Br]%20Melhoria%20no%20sistema%20de%20tickets%20NFQ.md), cerrado el 2026-10-21: no se reabre, se crea este. Ricardo C. (Projeto Apollo) agradece la respuesta del equipo de soporte y confirma su disponibilidad para una reunión mañana de 15:30 a 16:00 (hora de Brasil), solicitando una invitación. La reunión es para discutir la mejora en el sistema de tickets y el envío del informe semanal que no ha recibido.

Adjuntos del correo: image001.png, image002.png, image003.png

## Histórico de interacciones

- 2026-10-27 16:31 — Correo automático — Continúa el hilo del [NFQBAU-1523](../Abiertos/NFQBAU-1523%20—%202026-10-16%20—%20[Aldrin%20Br]%20Melhoria%20no%20sistema%20de%20tickets%20NFQ.md), cerrado el 2026-10-21: no se reabre, se crea este. Ricardo C. (Projeto Apollo) agradece la respuesta del equipo de soporte y confirma su disponibilidad para una reunión mañana de 15:30 a 16:00 (hora de Brasil), solicitando una invitación. La reunión es para discutir la mejora en el sistema de tickets y el envío del informe semanal que no ha recibido.

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
- 2026-10-27 16:31 — (vacío) → Abierto — Correo automático
- 2026-10-27 17:50 — Abierto → En curso — Matheus Fransoni
- 2026-10-27 17:55 — Abierto → En curso — Matheus Fransoni
- 2026-10-28 04:54 — Abierto → En curso — Ricardo Reyes
- 2026-11-04 15:40 — En curso → Resuelto — Matheus Fransoni

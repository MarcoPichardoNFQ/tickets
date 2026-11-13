---
id: NFQBAU-1508
fecha_apertura: 2026-09-28
fecha_limite: 2026-09-28
fecha_resolucion: 2026-09-28
estado: Resuelto
prioridad: Alta
responsable: Ricardo Reyes
origen: reunión
referencia_origen:
categoria:
  - Rundeck
entorno:
  - Producción
sintoma:
solucion_corta: "ticket de prueba; sin acción"
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-09-28 16:25
actualizado_por: Ricardo Reyes
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Correo automático'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Se detectó que no estan llegando la mitad de las flags para iniciar el proceso
## Histórico de interacciones

- 2026-09-28 14:27 — Ricardo Reyes — 

- 2026-09-28 16:25 — Ricardo Reyes — Cerrado: prueba del sistema, sin acción.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Nada: ticket de prueba.

### Cómo se comprobó

### Con quién se habló

### Servicios, jobs o tablas tocados

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-09-28 14:28 — nuevo → Abierto — Ricardo Reyes
- 2026-09-28 14:33 — Abierto → En curso — Ricardo Reyes
- 2026-09-28 16:25 — En curso → Resuelto — Ricardo Reyes

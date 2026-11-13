---
id: NFQBAU-1516
fecha_apertura: 2026-10-15
fecha_limite: 2026-10-16
fecha_resolucion: 2026-10-21
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: "[Aldrin] - Valores no cargados Unit (2026-10-15)"
categoria: []
entorno: []
sintoma: Ausencia de valores en la base de datos de Aldrin en relación a la interfaz Unit.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-21 01:29
actualizado_por: Marco Pichardo
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Correo automático'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marco P., senior consultant, informa sobre la ausencia de valores en la base de Aldrin respecto a la interfaz Unit tras la carga de hoy y solicita subir a p0 para validar.

## Histórico de interacciones

- 2026-10-15 18:10 — Correo automático — Marco P., senior consultant, informa sobre la ausencia de valores en la base de Aldrin respecto a la interfaz Unit tras la carga de hoy y solicita subir a p0 para validar.

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
- 2026-10-15 18:10 — (vacío) → Abierto — Correo automático
- 2026-10-17 11:51 — Abierto → En curso — Ricardo Reyes
- 2026-10-21 01:29 — En curso → Resuelto — Marco Pichardo

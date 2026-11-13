---
id: NFQBAU-1501
fecha_apertura: 2026-09-27
fecha_limite: 2026-09-27
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
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-09-28 12:26
actualizado_por: Ricardo Reyes
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen
Llamada de soporte para verificar el desarrollo

## Histórico de interacciones

- 2026-09-27 10:53 — Ricardo Reyes — 

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
- 2026-09-27 10:56 — nuevo → Abierto — Ricardo Reyes
- 2026-09-28 12:26 — Abierto → Resuelto — Ricardo Reyes

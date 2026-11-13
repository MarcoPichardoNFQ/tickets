---
id: NFQBAU-1506
fecha_apertura: 2026-09-28
fecha_limite: 2026-09-29
fecha_resolucion: 2026-09-28
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: "RE: Migração das bases PostgreSQL para versão 18 (2026-09-23)"
categoria: []
entorno: []
sintoma: ningún error reportado, corresponde a una actualización del cronograma de migración de bases de datos
solucion_corta: "informativo: cronograma de migración de PostgreSQL a la versión 18; sin acción de soporte"
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-17 16:13
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

El responsable de tecnología del cliente comparte el cronograma actualizado para la migración de las bases de datos a la versión 18 de PostgreSQL, detallando las fechas previstas para las actualizaciones de los entornos de preproducción y producción.

## Histórico de interacciones

- 2026-09-28 12:05 — Correo automático — El responsable de tecnología del cliente comparte el cronograma actualizado para la migración de las bases de datos a la versión 18 de PostgreSQL, detallando las fechas previstas para las actualizaciones de los entornos de preproducción y producción.

- 2026-09-28 12:24 — Ricardo Reyes — Cerrado: informativo: cronograma de migración de PostgreSQL a la versión 18; sin acción de soporte.

- 2026-09-28 16:26 — Ricardo Reyes — Cerrado: prueba del sistema; el equipo empieza con las vistas limpias.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Nada: informativo: cronograma de migración de PostgreSQL a la versión 18; sin acción de soporte.

### Cómo se comprobó

### Con quién se habló

### Servicios, jobs o tablas tocados

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-09-28 12:05 — nuevo → Abierto — Correo automático
- 2026-09-28 12:24 — Abierto → Resuelto — Ricardo Reyes
- 2026-09-28 14:23 — Resuelto → En curso — Ricardo Reyes
- 2026-09-28 16:26 — En curso → Resuelto — Ricardo Reyes

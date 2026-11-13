---
id: NFQBAU-1510
fecha_apertura: 2026-09-28
fecha_limite: 2026-09-29
fecha_resolucion: 2026-10-08
estado: Resuelto
prioridad: Media
responsable: Ricardo Reyes
origen: email
referencia_origen: Comenzaron las cargas (2026-09-28)
categoria: []
entorno: []
sintoma: inicio de ejecución del job Aldrin-Megara STG StartOver
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-08 07:10
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

Notificación automática informando sobre el inicio de la ejecución del job Aldrin-Megara STG StartOver.

## Histórico de interacciones

- 2026-09-28 16:35 — Correo automático — Notificación automática informando sobre el inicio de la ejecución del job Aldrin-Megara STG StartOver.
- 2026-09-28 16:40 — Correo automático — Correo nuevo en el hilo: El sistema automatizado de alertas notifica el inicio de la ejecución del job Aldrin-Megara número 13930634 el 28 de septiembre de 2026 a las 16:37.
- 2026-09-28 16:50 — Correo automático — Correo nuevo en el hilo: El sistema automatizado de alertas notifica el inicio de la ejecución del job Aldrin-Megara #13931397 (STG StartOver) el 2026-09-28 a las 16:46:50 con una tasa de éxito del 100%.

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
- 2026-09-28 16:35 — nuevo → Abierto — Correo automático
- 2026-09-29 08:37 — Abierto → Pendiente despliegue UAT — Ricardo Reyes
- 2026-10-08 07:10 — Pendiente despliegue UAT → Resuelto — Ricardo Reyes

---
id: NFQBAU-1512
fecha_apertura: 2026-10-05
fecha_limite: 2026-10-06
fecha_resolucion: 2026-10-08
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: Entrar em P0 (2026-08-25)
categoria: [Sala]
entorno: []
sintoma: incidente en producción que requiere entrar en P0
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-06 22:44
actualizado_por: Marco Pichardo
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Correo automático'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marcela C., tecnología, notifica un incidente en producción y pide entrar en P0 de forma urgente.

## Histórico de interacciones

- 2026-10-05 09:40 — Correo automático — Marcela C., tecnología, notifica un incidente en producción y pide entrar en P0 de forma urgente.
- 2026-10-05 11:01 — Correo automático — Correo nuevo en el hilo: Marcela C., tecnología, comunica que existe un incidente en producción y solicita entrar en P0 para atenderlo.

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
- 2026-10-05 09:40 — nuevo → Abierto — Correo automático
- 2026-10-08 07:10 — Abierto → Resuelto — Ricardo Reyes

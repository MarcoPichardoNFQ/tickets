---
id: NFQBAU-1507
fecha_apertura: 2026-09-28
fecha_limite: 2026-09-29
fecha_resolucion: 2026-09-28
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: Prueba del aviso de ticket nuevo (2026-09-28)
categoria: []
entorno: []
sintoma: prueba del aviso en Google Chat
solucion_corta: ticket de prueba del aviso; sin acción
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

El responsable de pruebas comprueba que el aviso de ticket nuevo llega al espacio.

## Histórico de interacciones

- 2026-09-28 12:33 — Correo automático — El responsable de pruebas comprueba que el aviso de ticket nuevo llega al espacio.

- 2026-09-28 12:34 — Ricardo Reyes — Cerrado: prueba del aviso de ticket nuevo.

- 2026-09-28 16:26 — Ricardo Reyes — Cerrado: prueba del sistema; el equipo empieza con las vistas limpias.

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
- 2026-09-28 12:33 — nuevo → Abierto — Correo automático
- 2026-09-28 12:34 — Abierto → Resuelto — Ricardo Reyes
- 2026-09-28 14:23 — Resuelto → Revisión cliente — Ricardo Reyes
- 2026-09-28 16:26 — Revisión cliente → Resuelto — Ricardo Reyes

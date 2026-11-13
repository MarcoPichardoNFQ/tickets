---
id: NFQBAU-1504
fecha_apertura: 2026-09-27
fecha_limite: 2026-09-28
fecha_resolucion: 2026-09-28
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: "Relatório de posição não abre (2026-09-27)"
categoria: []                # Rundeck | BBDD | Qlik | APIs | Otros
entorno: []                  # Producción | UAT
sintoma: "el informe de posición del Portal no abre desde esta mañana"
solucion_corta: "ticket de prueba del correo automático; sin acción"
codigo_relacionado:
  - repo:
    modulo:
    version:                 # tag de PRD cuando se despliegue
tickets_proveedor: []        # notas de 03_PROVEEDORES
decision_relacionada:
referencias_tecnicas: []     # fichas de 00_REFERENCIA_TECNICA que ayudaron
actualizado: 2026-10-17 16:13
actualizado_por: Ricardo Reyes
tags: [ticket, bau]
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Correo automático'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

El responsable de operaciones del cliente avisa de que el informe de posición no abre desde esta mañana y pide revisión. Adjunta captura.

## Histórico de interacciones

- 2026-09-27 20:18 — Correo automático — El responsable de operaciones del cliente avisa de que el informe de posición no abre desde esta mañana y pide revisión. Adjunta captura.
- 2026-09-27 20:19 — Correo automático — Correo nuevo en el hilo: El cliente añade que en producción sí abre; el fallo es solo en UAT.

- 2026-09-28 12:24 — Ricardo Reyes — Cerrado: ticket de prueba del correo automático; sin acción.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Nada: ticket de prueba del correo automático; sin acción.

### Cómo se comprobó

### Con quién se habló

### Servicios, jobs o tablas tocados

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-09-27 20:18 — nuevo → Abierto — Correo automático
- 2026-09-28 12:24 — Abierto → Resuelto — Ricardo Reyes

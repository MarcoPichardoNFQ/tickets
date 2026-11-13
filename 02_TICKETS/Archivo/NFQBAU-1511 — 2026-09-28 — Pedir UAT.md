---
id: NFQBAU-1511
fecha_apertura: 2026-09-28
fecha_limite: 2026-09-29
fecha_resolucion: 2026-10-08
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: Pedir UAT (2026-09-28)
categoria: []
entorno: []
sintoma: petición de compilación de código adjunto en el entorno UAT para el host psqlcerdatahub01.postgres.database.cloud.corp
solucion_corta:
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

Marco P., Senior Consultant, solicita ayuda para compilar el código adjunto en el entorno UAT siguiendo las indicaciones de Kleverson K., e indica que Marcos Antonio B. puede aprobar las ejecuciones. Adjunta un fichero.

## Histórico de interacciones

- 2026-09-28 16:45 — Correo automático — Marco P., Senior Consultant, solicita ayuda para compilar el código adjunto en el entorno UAT siguiendo las indicaciones de Kleverson K., e indica que Marcos Antonio B. puede aprobar las ejecuciones. Adjunta un fichero.

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
- 2026-09-28 16:45 — nuevo → Abierto — Correo automático
- 2026-10-08 07:10 — Abierto → Resuelto — Ricardo Reyes

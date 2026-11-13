---
id: NFQBAU-1519
fecha_apertura: 2026-10-16
fecha_limite: 2026-10-17
fecha_resolucion: 2026-10-17
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: "[ALDRIN BR] Nuevos Duplicados - Incidências cargas PRD (2026-10-16)"
categoria:
  - BBDD
entorno:
  - Producción
sintoma: Se detectan nuevos registros duplicados en las tablas sac_pos_rv_em_rem_t y sac_stat_rv_em_pos_ta_re_t.
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
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Correo automático'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

El equipo de soporte de Sancac informa de nuevos registros duplicados en las tablas sac_pos_rv_em_rem_t y sac_stat_rv_em_pos_ta_re_t. Los duplicados se han encontrado con fechas desde el 2 de octubre de 2026 hasta el 15 de octubre de 2026.

## Histórico de interacciones

- 2026-10-16 06:47 — Correo automático — El equipo de soporte de Sancac informa de nuevos registros duplicados en las tablas sac_pos_rv_em_rem_t y sac_stat_rv_em_pos_ta_re_t. Los duplicados se han encontrado con fechas desde el 2 de octubre de 2026 hasta el 15 de octubre de 2026.
- 2026-10-16 10:12 — Correo automático — Correo nuevo en el hilo: El equipo de soporte de Sancac Brasil informa que se han encontrado nuevos registros duplicados en las tablas de producción. Los duplicados afectan a varias entradas y fechas, con incidencias desde principios de octubre hasta el 15 de octubre.

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
- 2026-10-16 06:47 — (vacío) → Abierto — Correo automático
- 2026-10-17 11:51 — Abierto → En curso — Ricardo Reyes
- 2026-10-17 16:10 — En curso → Resuelto — Ricardo Reyes

---
id: NFQBAU-1520
fecha_apertura: 2026-10-16
fecha_limite: 2026-10-17
fecha_resolucion: 2026-10-26
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: Nuevos Duplicados - Incidências cargas PRD (2026-10-16)
categoria: []
entorno: []
sintoma: Se detectan registros duplicados en las tablas sac_pos_rv_em_rem_t y sac_stat_rv_em_pos_ta_re_t.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-26 17:25
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

Ismael B., Developer I, informa de nuevos registros duplicados en las tablas sac_pos_rv_em_rem_t (145 duplicados) y sac_stat_rv_em_pos_ta_re_t (24 duplicados). Los duplicados se han encontrado con fechas entre el 2 y el 15 de octubre de 2026.

## Histórico de interacciones

- 2026-10-16 07:42 — Correo automático — Ismael B., Developer I, informa de nuevos registros duplicados en las tablas sac_pos_rv_em_rem_t (145 duplicados) y sac_stat_rv_em_pos_ta_re_t (24 duplicados). Los duplicados se han encontrado con fechas entre el 2 y el 15 de octubre de 2026.

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
- 2026-10-16 07:42 — nuevo → Abierto — Correo automático
- 2026-10-17 11:51 — Abierto → En curso — Ricardo Reyes
- 2026-10-21 01:29 — En curso → Revisión cliente — Marco Pichardo
- 2026-10-26 17:25 — Revisión cliente → Resuelto — Marco Pichardo

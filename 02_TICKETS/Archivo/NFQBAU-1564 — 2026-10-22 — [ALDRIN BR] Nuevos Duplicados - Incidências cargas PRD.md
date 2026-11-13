---
id: NFQBAU-1564
fecha_apertura: 2026-10-22
fecha_limite: 2026-10-23
fecha_resolucion: 2026-10-26
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: "[ALDRIN BR] Nuevos Duplicados - Incidências cargas PRD (2026-10-22)"
categoria:
  - BBDD
entorno:
  - Producción
sintoma: Detección de registros duplicados en varias tablas de la base de datos tras las cargas.
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
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Continúa el hilo del [NFQBAU-1519](../Abiertos/NFQBAU-1519%20—%202026-10-16%20—%20[ALDRIN%20BR]%20Nuevos%20Duplicados%20-%20Incidências%20cargas%20PRD.md), cerrado el 2026-10-17: no se reabre, se crea este. Marco P., consultor senior de Nfq, reporta la aparición de nuevos registros duplicados tras las cargas de producción.
Detalla las tablas y claves afectadas correspondientes a fechas entre el 14 y el 21 de octubre de 2026 para su revisión.

Detalles: Tabla cart_pos_rf_t: 8 duplicados (cod_cli CUST4951, cod_rfoper SCI002023043, dat_hist 2026-10-21); Tabla sac_pos_rv_em_rem_t: 411 duplicados (fechas entre 2026-10-14 y 2026-10-21); Tabla sac_stat_fu_ativo_t: 112 duplicados; Tabla sac_stat_fu_vcto_t: 112 duplicados; Tabla sac_stat_rv_em_pos_ta_re_t: 46 duplicados (fechas entre 2026-10-16 y 2026-10-21)

## Histórico de interacciones

- 2026-10-22 19:58 — Correo automático — Continúa el hilo del [NFQBAU-1519](../Abiertos/NFQBAU-1519%20—%202026-10-16%20—%20[ALDRIN%20BR]%20Nuevos%20Duplicados%20-%20Incidências%20cargas%20PRD.md), cerrado el 2026-10-17: no se reabre, se crea este. Marco P., consultor senior de Nfq, reporta la aparición de nuevos registros duplicados tras las cargas de producción.
Detalla las tablas y claves afectadas correspondientes a fechas entre el 14 y el 21 de octubre de 2026 para su revisión.
- 2026-10-22 20:21 — Correo automático — Correo nuevo en el hilo: Marco P., de NFQ.mx, informa que han aparecido nuevos registros duplicados en varias tablas de la base de datos. El problema se manifiesta con diferentes cantidades de duplicados por tabla y afecta a datos desde el 14 de octubre de 2026 hasta el 22 de octubre de 2026. Detalles: Tabla: cart_pos_rf_t (Qtde: 8), con cod_cli CUST4951, cod_rfoper SCI002023043, dat_hist 2026-10-21; Tabla: sac_pos_rv_em_rem_t (Qtde: 411), con cod_mov y dat_pos variados desde 2026-10-14 hasta 2026-10-21; Tabla: sac_stat_fu_ativo_t (Qtde: 216), con cod_ati variados; Tabla: sac_stat_fu_cotativo_t (Qtde: 4), con cod_fuvct X26, Z26, cod_fuvct_fuatv BOVOX26, BOVOZ26, dat_cot 2026-10-22; Tabla: sac_stat_fu_vcto_t (Qtde: 216), con cod_fuatv y cod_vcto variados; Tabla: sac_stat_rv_em_pos_ta_re_t (Qtde: 46), con cod_mov y dat_pos variados desde 2026-10-16 hasta 2026-10-21.
- 2026-10-26 13:47 — Correo automático — Correo nuevo en el hilo: Deborah Y., Developer de NFQ Advisory, informa de la aparición de nuevos registros duplicados en varias tablas de la base de datos de producción. El problema se ha detectado en datos desde el 15 de octubre de 2026 hasta el 23 de octubre de 2026. Detalles: Tabla: cart_pos_rf_t (Cantidad: 2); cod_cli: CUST4951; cod_rfoper: SCI002023043; dat_hist: 2026-10-21; Cantidad: 2; Tabla: sac_pos_rv_em_rem_t (Cantidad: 109); cod_mov: SCI001972478, SCI001977144, SCI001977164, SCI001977174, SCI001980284, SCI001993571, SCI001994221, SCI001994520, SCI001995065, SCI001995224, SCI001996727, SCI001997645, SCI002000845, SCI002001348, SCI002001364, SCI002004245, SCI002007028, SCI002007047, SCI002007063, SCI002013619, SCI002013642, SCI002018774, SCI002018850, SCI002018998, SCI002019020, SCI002021763, SCI002024640; dat_pos: desde 2026-10-15 hasta 2026-10-23; Cantidad: entre 2 y 6; Tabla: sac_stat_rv_em_pos_ta_re_t (Cantidad: 9); cod_mov: SCI002000845, SCI002001348, SCI002001364, SCI002007047; dat_pos: 2026-10-21; Cantidad: entre 2 y 3

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
- 2026-10-22 19:58 — (vacío) → Abierto — Correo automático
- 2026-10-26 17:25 — Abierto → Resuelto — Marco Pichardo

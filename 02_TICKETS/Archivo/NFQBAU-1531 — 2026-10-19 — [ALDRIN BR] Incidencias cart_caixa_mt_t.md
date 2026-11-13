---
id: NFQBAU-1531
fecha_apertura: 2026-10-19
fecha_limite: 2026-10-20
fecha_resolucion: 2026-10-20
estado: Resuelto
prioridad: Media
responsable: Deborah Bertoldo
origen: email
referencia_origen: "[ALDRIN BR] Incidencias cart_caixa_mt_t (2026-10-19)"
categoria:
  - BBDD
entorno: []
sintoma: La tabla cart_caixa_mt_t presenta registros con saldos duplicados para los mismos clientes y fechas.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-20 18:33
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

Deborah B., desarrolladora de NFQ, reporta la detección de saldos duplicados en la tabla cart_caixa_mt_t para clientes en un mismo día.
Señala que las duplicidades proceden tanto del origen SAC como de Megara y proporciona un listado de registros afectados para su revisión.

Detalles: Tabla afectada: cart_caixa_mt_t; Total de registros duplicados reportados: 43 (Qtde: 2 para cada combinación de cod_cli y dat_liq); Orígenes en conflicto: SAC y Megara; Clientes afectados: CUST4504, CUST2893, CUST1926, CUST3122, CUST3229, CUST3639, CUST4477, CUST4519, CUST2234, CUST3041, CUST4127, CUST3350, CUST4925, CUST4635, CUST4794, CUST4175; Fechas afectadas (dat_liq): entre junio de 2026 y diciembre de 2026, además de fechas 9996-12-30 y 9999-11-11

## Histórico de interacciones

- 2026-10-19 10:16 — Correo automático — Deborah B., desarrolladora de NFQ, reporta la detección de saldos duplicados en la tabla cart_caixa_mt_t para clientes en un mismo día.
Señala que las duplicidades proceden tanto del origen SAC como de Megara y proporciona un listado de registros afectados para su revisión.
- 2026-10-19 12:13 — Correo automático — Correo nuevo en el hilo: Deborah Y., Developer, informa que la tabla cart_caixa_mt_t tiene saldos duplicados para clientes en el mismo día, con orígenes tanto del SAC como de Megara. Adjunta una lista de los registros afectados. Detalles: Tabla: cart_caixa_mt_t; Saldo duplicado para clientes en el mismo día; Orígenes: SAC y Megara; Cantidad de registros afectados: 47; Ejemplos de clientes y fechas afectadas: CUST4504 (9999-11-11), CUST2893 (9996-12-30), CUST1926 (2026-12-31), CUST2234 (2026-10-16), CUST3350 (2026-10-14), CUST4175 (2026-06-09)
- 2026-10-19 13:07 — Correo automático — Correo nuevo en el hilo: Deborah B., desarrolladora de NFQ, informa sobre un problema en la tabla cart_caixa_mt_t.
Indica que se identificaron saldos duplicados para clientes en un mismo día con orígenes de SAC y Megara. Detalles: Tabla afectada: cart_caixa_mt_t; Error: saldos duplicados (Qtde: 2) para el mismo cliente (cod_cli) y fecha de liquidación (dat_liq) con orígenes SAC y Megara; Cantidad de registros afectados: 44

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
- 2026-10-19 10:16 — (vacío) → Abierto — Correo automático
- 2026-10-20 18:33 — Abierto → Resuelto — Marco Pichardo

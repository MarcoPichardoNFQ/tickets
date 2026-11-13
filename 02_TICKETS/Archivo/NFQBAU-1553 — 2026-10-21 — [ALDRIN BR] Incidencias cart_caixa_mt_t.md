---
id: NFQBAU-1553
fecha_apertura: 2026-10-21
fecha_limite: 2026-10-22
fecha_resolucion: 2026-10-26
estado: Resuelto
prioridad: Media
responsable: Antonio Montoro
origen: email
referencia_origen: "[ALDRIN BR] Incidencias cart_caixa_mt_t (2026-10-21)"
categoria:
  - BBDD
entorno: []
sintoma: La tabla cart_caixa_mt_t presenta registros de saldos duplicados para un mismo cliente y fecha.
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

Continúa el hilo del [NFQBAU-1531](../Abiertos/NFQBAU-1531%20—%202026-10-19%20—%20[ALDRIN%20BR]%20Incidencias%20cart_caixa_mt_t.md), cerrado el 2026-10-20: no se reabre, se crea este. Deborah B., desarrolladora de NFQ, notifica la detección de saldos duplicados en la tabla cart_caixa_mt_t para varios clientes en el mismo día.
Indica que las duplicidades provienen de cargas originadas tanto en SAC como en Megara.
Reporta 42 casos afectados con diversas fechas de liquidación.

Detalles: Tabla: cart_caixa_mt_t; Cantidad de registros/casos duplicados reportados: 42 (cada uno con Qtde: 2); Origen de los datos duplicados: SAC y Megara; Clientes afectados: CUST4504, CUST2893, CUST1926, CUST3122, CUST3229, CUST3639, CUST4477, CUST4519, CUST3041, CUST4127, CUST3350, CUST4925, CUST4635, CUST4794, CUST4175; Fechas de liquidación (dat_liq) afectadas: 9999-11-11, 9996-12-30, y fechas entre 2026-06-09 y 2026-12-31

## Histórico de interacciones

- 2026-10-21 09:46 — Correo automático — Continúa el hilo del [NFQBAU-1531](../Abiertos/NFQBAU-1531%20—%202026-10-19%20—%20[ALDRIN%20BR]%20Incidencias%20cart_caixa_mt_t.md), cerrado el 2026-10-20: no se reabre, se crea este. Deborah B., desarrolladora de NFQ, notifica la detección de saldos duplicados en la tabla cart_caixa_mt_t para varios clientes en el mismo día.
Indica que las duplicidades provienen de cargas originadas tanto en SAC como en Megara.
Reporta 42 casos afectados con diversas fechas de liquidación.

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
- 2026-10-21 09:46 — (vacío) → Abierto — Correo automático
- 2026-10-26 17:25 — Abierto → Resuelto — Marco Pichardo

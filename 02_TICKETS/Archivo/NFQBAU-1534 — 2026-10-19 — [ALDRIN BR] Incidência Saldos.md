---
id: NFQBAU-1534
fecha_apertura: 2026-10-19
fecha_limite: 2026-10-20
fecha_resolucion: 2026-10-26
estado: Resuelto
prioridad: Media
responsable: Deborah Bertoldo
origen: email
referencia_origen: "[ALDRIN BR] Incidência Saldos (2026-10-19)"
categoria:
  - BBDD
entorno: []
sintoma: Presencia de registros duplicados de saldos para un mismo cliente y fecha en la tabla cart_caixa_saldo_mt_t.
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

Deborah B., desarrolladora de NFQ, informa que se identificaron saldos duplicados referentes al mismo cliente y fecha provenientes tanto de Megara como de SAC.
Solicita la revisión de la inconsistencia detectada en la información de saldos desde el 2026-09-30.

Detalles: Tabla afectada: cart_caixa_saldo_mt_t; Inconsistencia: registros duplicados (Qtde: 2) provenientes de fuentes Megara y SAC; Clientes afectados: CUST4564, CUST3958, CUST3333, CUST3320, CUST1157, CUST4658, CUST4660; Rango de fechas liquidadas afectadas: 2026-09-30 a 2026-10-19; Total de registros duplicados reportados: 22

## Histórico de interacciones

- 2026-10-19 12:07 — Correo automático — Deborah B., desarrolladora de NFQ, informa que se identificaron saldos duplicados referentes al mismo cliente y fecha provenientes tanto de Megara como de SAC.
Solicita la revisión de la inconsistencia detectada en la información de saldos desde el 2026-09-30.
- 2026-10-19 13:08 — Correo automático — Correo nuevo en el hilo: Deborah B., desarrolladora de NFQ, reporta la presencia de saldos duplicados procedentes tanto de la fuente Megara como del SAC.
Solicita la revisión de esta inconsistencia detectada en los registros de saldos.
El problema afecta a varias fechas comprendidas entre el 30 de septiembre y el 14 de octubre de 2026. Detalles: Tabla afectada: cart_caixa_saldo_mt_t; Fuentes de origen con duplicados: Megara y SAC; Clientes afectados: CUST3320, CUST1157, CUST4658, CUST4660; Fechas afectadas (dat_liq): entre 2026-09-30 y 2026-10-14; Cantidad de registros mostrados: 19
- 2026-10-20 14:08 — Correo automático — Correo nuevo en el hilo: Deborah B., desarrolladora de NFQ, informa que se han identificado saldos duplicados para los mismos clientes en idénticas fechas, procedentes simultáneamente de Megara y de SAC. Proporciona el listado de casos afectados en la tabla de saldos entre el 2 y el 15 de octubre de 2026 para su revisión. Detalles: Tabla: cart_caixa_saldo_mt_t; Total registros afectados: 13; Fuentes: Megara y SAC; Clientes y fechas con duplicados: CUST3320 (2026-10-13, 2026-10-14, 2026-10-15), CUST4660 (2026-10-02, 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-08), CUST4658 (2026-10-02, 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-08)
- 2026-10-20 14:51 — Correo automático — Correo nuevo en el hilo: Marco P., consultor sénior de NFQ, informa sobre la detección de saldos duplicados procedentes de dos fuentes distintas (Megara y SAC) para los mismos clientes y fechas. Reporta registros afectados entre el 02-10-2026 y el 20-10-2026 en la tabla de saldos de caja. Detalles: Tabla: cart_caixa_saldo_mt_t; Total de registros afectados: 16 registros duplicados (Qtde: 2); Fuentes en conflicto: Megara y SAC; Clientes y fechas: CUST3320 (2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-19, 2026-10-20), CUST4660 (2026-10-02, 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-08), CUST4658 (2026-10-02, 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-08)
- 2026-10-26 15:41 — Correo automático — Correo nuevo en el hilo: Marco P., de NFQ.mx, informa que se han identificado saldos duplicados para el mismo cliente en la misma fecha, con datos de origen Megara y SAC. El problema afecta a la tabla cart_caixa_saldo_saldo_t. Detalles: Tabla afectada: cart_caixa_saldo_saldo_t; Se encuentran saldos duplicados para los clientes CUST3320, CUST4658 y CUST4660; Fechas afectadas: desde 2026-10-02 hasta 2026-10-21.

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
- 2026-10-19 12:07 — (vacío) → Abierto — Correo automático
- 2026-10-21 01:29 — Abierto → Revisión cliente — Marco Pichardo
- 2026-10-26 17:25 — Revisión cliente → Resuelto — Marco Pichardo

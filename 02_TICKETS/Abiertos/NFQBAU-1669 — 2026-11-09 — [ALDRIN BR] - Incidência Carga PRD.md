---
id: NFQBAU-1669
fecha_apertura: 2026-11-09
fecha_limite: 2026-11-09
fecha_resolucion:
estado: Revisión cliente
prioridad: Alta
responsable: Matheus Fransoni
origen: email
referencia_origen: "[ALDRIN BR] - Incidência Carga PRD (2026-11-09)"
categoria:
  - Rundeck
entorno:
  - Producción
sintoma: El job de carga en producción está experimentando una demora atípica en su ejecución.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-09 19:56
actualizado_por: Correo automático
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Matheus D., Developer III de NFQ, informa de una demora atípica en la ejecución de un job de carga en producción. El problema se identificó a las 11:47 y podría deberse a datos duplicados en el XML de CashBal. Están en P0 para un análisis más detallado y resolución del incidente.

Detalles: El job de carga se ejecuta en producción; la demora se identificó a las 11:47; el problema podría ser por datos duplicados en el xml de CashBal; están en P0 para análisis y resolución.

## Histórico de interacciones

- 2026-11-09 12:21 — Correo automático — Matheus D., Developer III de NFQ, informa de una demora atípica en la ejecución de un job de carga en producción. El problema se identificó a las 11:47 y podría deberse a datos duplicados en el XML de CashBal. Están en P0 para un análisis más detallado y resolución del incidente.
- 2026-11-09 14:12 — Correo automático — Correo nuevo en el hilo: Matheus D. de NFQ, junto con S3, ha identificado que el error en la carga de producción se debe a saldos múltiples para un mismo cliente. Tras hablar con Thiago, se ha determinado que el dato pertenece a un fondo de prueba y no requiere corrección en este momento. Detalles: Error por saldos múltiples para un mismo cliente en tres fechas en el XML de ClientBalance; el dato pertenece a un fondo de prueba y está en proceso de cambio, por lo que no requiere acción de corrección en este momento.
- 2026-11-09 16:28 — Correo automático — Correo nuevo en el hilo: Matheus D., Developer III de NFQ, sugiere una recarga a partir de las 11:00h de hoy porque hubo un error en un fondo de prueba del archivo ClientBalance, lo que impidió la carga de cualquier fondo de este archivo. Detalles: Se sugiere una recarga a partir de las 11:00h de hoy; Error en el fondo de prueba del archivo ClientBalance; Ningún fondo del archivo ClientBalance fue cargado para esta ejecución.
- 2026-11-09 17:41 — Correo automático — Correo nuevo en el hilo: Marco P., consultor senior de NFQ, pide a Thiago A., cliente de PR Serviços, que ayude a realizar lo antes posible la recarga indicada previamente por Matheus tras analizar la incidencia. Detalles: job de carga; archivo XML de ClientBalance; se requiere realizar una recarga a partir de las 11:00h; saldos múltiplos para un mismo cliente en tres fechas en el XML de ClientBalance correspondientes a un fondo de prueba.
- 2026-11-09 19:56 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, reitera y solicita con urgencia a Thiago A., de PR Servicios, ayuda para ejecutar una recarga (reload) lo antes posible. Detalles: Solicitud urgente de ejecución de recarga (reload) de la carga afectada en producción

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
- 2026-11-09 12:21 — nuevo → Abierto — Correo automático
- 2026-11-09 17:26 — Abierto → Revisión cliente — Matheus Fransoni

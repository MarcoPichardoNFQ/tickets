---
id: NFQBAU-1584
fecha_apertura: 2026-10-27
fecha_limite: 2026-10-28
fecha_resolucion: 2026-11-05
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: "[ALDRIN BR] Incidência Saldos (2026-10-27)"
categoria:
  - BBDD
entorno: []
sintoma: Presencia de registros duplicados de saldos para un mismo cliente y fecha en la tabla cart_caixa_saldo_t.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-06 22:43
actualizado_por: Marco Pichardo
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Continúa el hilo del [NFQBAU-1579](../Abiertos/NFQBAU-1579%20—%202026-10-27%20—%20[ALDRIN%20BR]%20Incidência%20Saldos.md), cerrado el 2026-10-27: no se reabre, se crea este. Deborah B., Developer de NFQ, reporta un problema con la presencia de saldos duplicados. Se han identificado registros para un mismo cliente y fecha procedentes tanto de fuentes Megara como de SAC.

Detalles: Tabla afectada: cart_caixa_saldo_t; Total registros reportados: 26 (Qtde = 2); Fuentes: Megara y SAC; Clientes afectados: CUST2122, CUST4245, CUST3320, CUST4658, CUST4660; Periodo afectado: de 2026-10-02 a 2026-10-28

## Histórico de interacciones

- 2026-10-27 22:11 — Correo automático — Continúa el hilo del [NFQBAU-1579](../Abiertos/NFQBAU-1579%20—%202026-10-27%20—%20[ALDRIN%20BR]%20Incidência%20Saldos.md), cerrado el 2026-10-27: no se reabre, se crea este. Deborah B., Developer de NFQ, reporta un problema con la presencia de saldos duplicados. Se han identificado registros para un mismo cliente y fecha procedentes tanto de fuentes Megara como de SAC.
- 2026-10-30 23:02 — Correo automático — Correo nuevo en el hilo: Deborah B., desarrolladora de NFQ, informa sobre la existencia de saldos duplicados para un mismo cliente en la misma fecha, procedentes de Megara y SAC.
El problema afecta a varios clientes con registros comprendidos entre el 02 y el 28 de octubre de 2026. Detalles: Tabla: cart_caixa_saldo_t; Cantidad de registros: 24; Fuentes en conflicto: Megara y SAC; Clientes afectados: CUST4245, CUST3320, CUST4658, CUST4660; Rango de fechas afectadas (dat_liq): 2026-10-02 a 2026-10-28

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
- 2026-10-27 22:11 — (vacío) → Abierto — Correo automático
- 2026-11-05 17:43 — Abierto → Resuelto — Marco Pichardo
- 2026-11-06 12:14 — Abierto → Resuelto — Matheus Fransoni

---
id: NFQBAU-1579
fecha_apertura: 2026-10-27
fecha_limite: 2026-10-28
fecha_resolucion: 2026-10-27
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: "[ALDRIN BR] Incidência Saldos (2026-10-27)"
categoria:
  - BBDD
entorno: []
sintoma: Duplicidad de saldos para un mismo cliente y fecha en la tabla cart_caixa_saldo_mt_t.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-28 04:54
actualizado_por: Ricardo Reyes
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Continúa el hilo del [NFQBAU-1534](../Abiertos/NFQBAU-1534%20—%202026-10-19%20—%20[ALDRIN%20BR]%20Incidência%20Saldos.md), cerrado el 2026-10-26: no se reabre, se crea este. Deborah B., desarrolladora de NFQ, reporta que han identificado la presencia de saldos duplicados para un mismo cliente en la misma fecha.
Indica que existen registros duplicados procedentes de dos fuentes distintas: Megara y SAC.

Detalles: Tabla afectada: cart_caixa_saldo_mt_t; Se observan 24 registros con duplicados (Qtde: 2) para combinaciones de cod_cli y dat_liq; Clientes afectados: CUST4245, CUST3320, CUST4658, CUST4660; Rango de fechas afectadas (dat_liq): 2026-10-02 a 2026-10-28; Fuentes de datos implicadas: Megara y SAC

## Histórico de interacciones

- 2026-10-27 14:26 — Correo automático — Continúa el hilo del [NFQBAU-1534](../Abiertos/NFQBAU-1534%20—%202026-10-19%20—%20[ALDRIN%20BR]%20Incidência%20Saldos.md), cerrado el 2026-10-26: no se reabre, se crea este. Deborah B., desarrolladora de NFQ, reporta que han identificado la presencia de saldos duplicados para un mismo cliente en la misma fecha.
Indica que existen registros duplicados procedentes de dos fuentes distintas: Megara y SAC.

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
- 2026-10-27 14:26 — nuevo → Abierto — Correo automático
- 2026-10-27 16:21 — Abierto → Resuelto — Matheus Fransoni
- 2026-10-27 16:26 — Resuelto → Abierto — Matheus Fransoni
- 2026-10-27 17:50 — Abierto → Resuelto — Matheus Fransoni
- 2026-10-27 17:55 — Abierto → Resuelto — Matheus Fransoni
- 2026-10-28 04:54 — Abierto → Resuelto — Ricardo Reyes

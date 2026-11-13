---
id: NFQBAU-1589
fecha_apertura: 2026-10-28
fecha_limite: 2026-10-29
fecha_resolucion: 2026-10-28
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: "[ALDRIN BR] Incidencias cart_caixa_mt_t (2026-10-28)"
categoria:
  - BBDD
entorno: []
sintoma: La tabla cart_caixa_mt_t presenta saldos duplicados para un mismo cliente y día.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-28 15:39
actualizado_por: Deborah Bertoldo
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Continúa el hilo del [NFQBAU-1553](../Abiertos/NFQBAU-1553%20—%202026-10-21%20—%20[ALDRIN%20BR]%20Incidencias%20cart_caixa_mt_t.md), cerrado el 2026-10-26: no se reabre, se crea este. Deborah Y., desarrolladora de NFQ, informa que se han detectado saldos duplicados en la tabla cart_caixa_mt_t para clientes en una misma fecha. Explica que estos duplicados provienen de las fuentes SAC y Megara y proporciona el listado de registros afectados para su revisión.

Detalles: Tabla afectada: cart_caixa_mt_t; Orígenes con conflicto: SAC y Megara; Cantidad total de casos duplicados: 43; Ejemplos de cod_cli y dat_liq afectados: CUST4504 (9999-11-11, 2026-09-24), CUST2893 (9996-12-30), CUST1926 (2026-12-31, 2026-09-21, 2026-09-08, 2026-09-04, 2026-09-03), CUST3122 (2026-12-31, 2026-09-09, 2026-09-08, 2026-09-04, 2026-09-03), CUST4175 (2026-07-09, 2026-07-02, 2026-06-22, 2026-06-10, 2026-06-09)

## Histórico de interacciones

- 2026-10-28 14:56 — Correo automático — Continúa el hilo del [NFQBAU-1553](../Abiertos/NFQBAU-1553%20—%202026-10-21%20—%20[ALDRIN%20BR]%20Incidencias%20cart_caixa_mt_t.md), cerrado el 2026-10-26: no se reabre, se crea este. Deborah Y., desarrolladora de NFQ, informa que se han detectado saldos duplicados en la tabla cart_caixa_mt_t para clientes en una misma fecha. Explica que estos duplicados provienen de las fuentes SAC y Megara y proporciona el listado de registros afectados para su revisión.

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
- 2026-10-28 14:56 — nuevo → Abierto — Correo automático
- 2026-10-28 15:39 — Abierto → Resuelto — Deborah Bertoldo

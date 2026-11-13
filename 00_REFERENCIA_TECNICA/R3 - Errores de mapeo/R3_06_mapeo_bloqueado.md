---
titulo: "R3.06 — Un mapeo bloqueado por otro proceso"
familia: R3
etapa: "Mapeos"
tipo: Runbook
tags:
  - familia/R3
  - etapa/mapeos
  - tipo/runbook
keywords: "bloqueo, lock, esperando, pg_blocking_pids, concurrencia, no avanza"
---

# R3.06 — Un mapeo bloqueado por otro proceso

**Etapa:** Mapeos
**Tipo:** Runbook
**Palabras clave:** bloqueo, lock, esperando, pg_blocking_pids, concurrencia, no avanza

## Síntoma

Un mapeo lleva mucho más tiempo del habitual sin terminar, y no hay error registrado.

## Bloqueo no es deadlock

| | Deadlock (`40P01`) | Bloqueo |
|---|---|---|
| Qué pasa | Dos transacciones se esperan mutuamente | Una espera a otra, sin ciclo |
| Quién lo resuelve | **PostgreSQL**, matando a una | Nadie: espera indefinidamente |
| Deja registro | Sí, en `s3_control_errores_mapeo` | **No** |
| Se reintenta | Sí, según `retry_deadlock` | No aplica |

El deadlock se autorresuelve. **El bloqueo no.** Por eso un mapeo bloqueado puede quedarse horas
sin que nada lo denuncie.

## Qué mirar

```sql
SELECT bloqueada.pid       AS pid_bloqueado,
       bloqueante.pid      AS pid_bloqueante,
       now() - bloqueada.query_start AS esperando,
       bloqueada.wait_event_type,
       left(bloqueada.query, 100)  AS consulta_bloqueada,
       left(bloqueante.query, 100) AS consulta_bloqueante,
       bloqueante.state    AS estado_bloqueante
FROM   pg_stat_activity bloqueada
JOIN   LATERAL unnest(pg_blocking_pids(bloqueada.pid)) AS b(pid) ON true
JOIN   pg_stat_activity bloqueante ON bloqueante.pid = b.pid
ORDER  BY esperando DESC;
```

Si `consulta_bloqueada` menciona una función `function_meg_*`, es un mapeo esperando.

## Causas probables, por orden

**1. Otro mapeo sobre la misma tabla.** Con decenas ejecutándose en paralelo es lo más frecuente.
Normalmente se resuelve solo en segundos.

**2. Un bloque de transformación todavía en curso.** El grafo del orquestador hace que los mapeos
esperen a tres ramas de bloques; si una se solapa, compiten por las mismas tablas de `trf_s3`.
Ver [G07_ciclo_completo_mapeos](../G%20-%20Mapeos/G07_ciclo_completo_mapeos.md).

**3. Una sesión `idle in transaction`.** El caso más dañino: alguien abrió transacción y no la
cerró —típicamente un cliente que se desconectó mal— y mantiene bloqueos indefinidamente.

```sql
SELECT pid, usename, state, now() - state_change AS lleva_asi, left(query, 80)
FROM   pg_stat_activity
WHERE  state = 'idle in transaction'
ORDER  BY state_change;
```

**4. Una consulta manual de diagnóstico.** Una consulta pesada lanzada durante el ciclo puede
bloquear. Merece comprobarse antes de buscar culpables externos.

## Acción

1. **Identifica al bloqueante** con la consulta de arriba.
2. Si el bloqueante es **otro mapeo o un bloque en curso**, espera: se resolverá solo.
3. Si es una sesión `idle in transaction` sin dueño identificable, es candidata a cancelarse:

```sql
SELECT pg_cancel_backend(:pid);      -- primero esto
SELECT pg_terminate_backend(:pid);   -- sólo si lo anterior no basta
```

**Antes de terminar cualquier sesión, mira qué ejecuta.** Matar un mapeo a mitad deja la tabla
destino parcialmente escrita y el contador sin decrementar, lo que complica el relanzamiento.

## Después

```sql
-- ¿Terminó el mapeo?
SELECT tabela_carga, control_carga, data_fim_upload
FROM   exp_s3.control_mapeio_t
WHERE  id = (SELECT last_value FROM exp_s3.cod_seq_control_mapeio)
  AND  lower(tabela_carga) = lower('<TABLA>');
```

Si el contador no llegó a cero, el mapeo quedó a medias. Ver [R3_09_contador_no_cero](../R3%20-%20Errores%20de%20mapeo/R3_09_contador_no_cero.md).

## Prevención

Un bloqueo puntual es normal con este nivel de concurrencia. **Un patrón que se repite a la misma
hora es un solape estructural** entre el ciclo de bloques y el de mapeos, y eso no se arregla
matando sesiones: se corrige en la planificación.

## Ver también

[R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md) · [D12_carga_colgada](../D%20-%20Carga%20STG/D12_carga_colgada.md) · [G07_ciclo_completo_mapeos](../G%20-%20Mapeos/G07_ciclo_completo_mapeos.md) · [R3_09_contador_no_cero](../R3%20-%20Errores%20de%20mapeo/R3_09_contador_no_cero.md) · [F13_bloque_lento](../F%20-%20Transformacion%20TRF/F13_bloque_lento.md)

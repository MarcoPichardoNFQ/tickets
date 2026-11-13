---
titulo: "D12 — La carga se quedó colgada o bloqueada"
familia: D
etapa: "Carga STG"
tipo: Runbook
tags:
  - familia/D
  - etapa/carga-stg
  - tipo/runbook
keywords: "colgado, bloqueo, lock, pg_locks, pg_stat_activity, lento, no avanza"
---

# D12 — La carga se quedó colgada o bloqueada

**Etapa:** Carga STG
**Tipo:** Runbook
**Palabras clave:** colgado, bloqueo, lock, pg_locks, pg_stat_activity, lento, no avanza

## Síntoma

Un job lleva mucho más tiempo del habitual sin terminar, o una tabla no se deja consultar.

## Qué mirar primero

```sql
-- Consultas activas ordenadas por antigüedad
SELECT pid, usename, state,
       now() - query_start AS duracion,
       wait_event_type, wait_event,
       left(query, 120) AS consulta
FROM   pg_stat_activity
WHERE  state <> 'idle'
ORDER  BY query_start;
```

```sql
-- Quién bloquea a quién
SELECT bloqueada.pid       AS pid_bloqueado,
       bloqueada.query     AS consulta_bloqueada,
       bloqueante.pid      AS pid_bloqueante,
       bloqueante.query    AS consulta_bloqueante,
       now() - bloqueada.query_start AS esperando_desde
FROM   pg_stat_activity bloqueada
JOIN   LATERAL unnest(pg_blocking_pids(bloqueada.pid)) AS b(pid) ON true
JOIN   pg_stat_activity bloqueante ON bloqueante.pid = b.pid
ORDER  BY esperando_desde DESC;
```

## Causas probables, por orden

**1. Los `UPDATE` de normalización.** `LOAD_FILES_PC` hace **dos pasadas completas por cada
columna** de la tabla: una para convertir vacíos en NULL y otra para recortar espacios. En una
tabla ancha con muchas filas son decenas de `UPDATE` sobre la tabla entera. No está colgado: está
trabajando. Ver [D06_load_files_pc](../D%20-%20Carga%20STG/D06_load_files_pc.md).

**2. Dos cargas de la misma tabla a la vez.** El `TRUNCATE` de `READ_HEADER_FN` necesita un bloqueo
exclusivo. Si otra sesión tiene la tabla abierta, se queda esperando indefinidamente. Síntoma:
`wait_event_type = 'Lock'` sobre una tabla `_TMP`.

**3. Un `TRUNCATE` esperando.** Igual que el anterior pero desde el lado del truncado de flujo
estricto.

**4. La validación de claves foráneas sobre tablas grandes.** `VALIDATE_ROWS_FOREIGN_FN` ejecuta
`count(*)` y `EXCEPT` sobre las tablas completas por cada relación declarada. Sin índices adecuados
en la tabla referenciada, escala mal.

**5. Un mapeo en paralelo compitiendo por las mismas tablas.** Ver [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md).

## Cómo distinguir «lento» de «bloqueado»

| Señal | Interpretación |
|---|---|
| `wait_event_type = 'Lock'` | **Bloqueado.** Hay otra sesión por medio |
| `wait_event_type = 'IO'` o vacío, y la consulta cambia | **Trabajando.** Lento, no colgado |
| `state = 'idle in transaction'` durante mucho rato | **Transacción abandonada.** Bloquea a otros y no avanza |

`idle in transaction` es el caso más dañino: una sesión que abrió transacción y no la cerró
—típicamente un cliente que se desconectó mal— mantiene bloqueos indefinidamente.

## Acción

1. Identifica si está bloqueado o trabajando con la tabla de arriba.
2. Si está **trabajando**, compara con la duración histórica de esa carga antes de tocar nada.
3. Si está **bloqueado**, identifica al bloqueante y decide cuál de los dos vale más.
4. Si el bloqueante es una sesión `idle in transaction` sin dueño identificable, es candidata a
   cancelarse:

```sql
SELECT pg_cancel_backend(:pid);      -- cancela la consulta, es lo primero que se prueba
SELECT pg_terminate_backend(:pid);   -- cierra la sesión entera, sólo si lo anterior no basta
```

**Antes de terminar cualquier sesión**, comprueba qué está ejecutando. Matar una carga a mitad deja
la tabla `_TMP` a medias y el fichero con nombre `_InLoad`, lo que exige limpieza manual después.
Ver [D08_gpg_historificacion](../D%20-%20Carga%20STG/D08_gpg_historificacion.md).

## Cuándo escalar

- Si el bloqueante es un proceso de negocio en marcha y no está claro cuál interrumpir.
- Si hay que terminar sesiones en producción: es una acción con efecto, mejor con testigo.
- Si el patrón se repite a diario a la misma hora: no es una incidencia puntual sino un solape
  estructural entre jobs, y eso se corrige en la planificación.

## Ver también

[D06_load_files_pc](../D%20-%20Carga%20STG/D06_load_files_pc.md) · [D04_read_header_fn](../D%20-%20Carga%20STG/D04_read_header_fn.md) · [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md) · [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md)

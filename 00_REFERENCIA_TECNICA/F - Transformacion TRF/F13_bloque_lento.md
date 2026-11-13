---
titulo: "F13 — Un bloque tardó muchísimo más de lo normal"
familia: F
etapa: "Transformación TRF"
tipo: Runbook
tags:
  - familia/F
  - etapa/transformacion-trf
  - tipo/runbook
keywords: "lento, duración, tarda, rendimiento, UPDATE por columna, volumen"
---

# F13 — Un bloque tardó muchísimo más de lo normal

**Etapa:** Transformación TRF
**Tipo:** Runbook
**Palabras clave:** lento, duración, tarda, rendimiento, UPDATE por columna, volumen

## Síntoma

Un bloque que suele terminar en minutos lleva horas, o el ciclo completo se ha desplazado.

## Qué mirar primero

```sql
-- ¿Está trabajando o esperando?
SELECT pid, state, now() - query_start AS duracion,
       wait_event_type, wait_event, left(query, 120)
FROM   pg_stat_activity
WHERE  state <> 'idle'
ORDER  BY query_start;
```

| Señal | Interpretación |
|---|---|
| `wait_event_type = 'Lock'` | **Bloqueado** por otra sesión → [D12_carga_colgada](../D%20-%20Carga%20STG/D12_carga_colgada.md) |
| Sin `wait_event` y la consulta cambia | **Trabajando**. Lento, no colgado |
| `idle in transaction` prolongado | Transacción abandonada que bloquea a otros |

## Causas probables, por orden

### 1. El acondicionamiento de `_TMP`

`LOAD_FILES_PC` recorre **cada columna dos veces**: una para convertir vacíos en NULL y otra para
recortar espacios. En una tabla ancha con muchas filas son decenas de `UPDATE` sobre la tabla
completa.

Es la causa número uno de lentitud en la etapa de carga, y escala con **columnas × filas**, no sólo
con filas. Ver [D06_load_files_pc](../D%20-%20Carga%20STG/D06_load_files_pc.md).

### 2. Volumen atípico

Contrasta con la historia del plan. No con la media —que en este sistema no significa gran cosa—
sino con las últimas cargas:

```sql
SELECT dat_load_date, amt_register_process
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_plan = :plan AND amt_register_process IS NOT NULL
ORDER  BY dat_load_date DESC LIMIT 20;
```

Recuerda que en la mayoría de los planes el máximo supera 50 veces la media: un pico de volumen
puede ser perfectamente normal. Ver [I15_volumetria_tipica](../I%20-%20Referencia%20de%20datos/I15_volumetria_tipica.md).

### 3. La validación de claves foráneas

`VALIDATE_ROWS_FOREIGN_FN` ejecuta `count(*)` y `EXCEPT` sobre las tablas completas **por cada
relación declarada**. Sin índices adecuados en la tabla referenciada, escala mal.

```sql
-- Cuántas relaciones se comprueban para esta tabla
SELECT count(*) FROM stg_s3.par_maestro_valid_t
WHERE  des_table = 'STG_S3.' || UPPER('<TABLA>') || ' A';
```

Ver [E05_par_maestro_valid_t](../E%20-%20Parametrizacion/E05_par_maestro_valid_t.md).

### 4. Concurrencia con los mapeos

Los mapeos corren decenas a la vez sobre las mismas tablas de `trf_s3`. Si un bloque coincide con la
ventana de mapeos, compiten. Ver [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md).

### 5. Un procedimiento con muchos joins

Algunas transformaciones y mapeos son grandes. `function_meg_cart_pos_rf_t` tiene 796 líneas con 26
joins; `sac_cl_patr`, 28 `INNER JOIN`. Ver [G06_catalogo_mapeos](../G%20-%20Mapeos/G06_catalogo_mapeos.md).

## Cómo saber qué es «normal» para ese bloque

No hay registro de duración por bloque en base de datos: **está en el histórico de ejecuciones de
Rundeck**. Compara la ejecución de hoy con las de los días anteriores del mismo job.

En base de datos, lo más aproximado es el reparto horario de las trazas:

```sql
SELECT cod_load_plan,
       min(dat_load_date) AS inicio,
       max(dat_load_date) AS fin,
       max(dat_load_date) - min(dat_load_date) AS duracion
FROM   stg_s3.aud_load_trace_t
WHERE  dat_load_date::date = CURRENT_DATE
GROUP  BY 1 ORDER BY 4 DESC NULLS LAST LIMIT 15;
```

Ojo con las horas: `LOG_TRACE` graba en `ADT` salvo en la ruta de excepción.
Ver [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md).

## Acción

1. Determina si está bloqueado o trabajando.
2. Si está **bloqueado**, identifica al bloqueante y decide. Ver [D12_carga_colgada](../D%20-%20Carga%20STG/D12_carga_colgada.md).
3. Si está **trabajando**, compara volumen y duración con días anteriores antes de tocar nada.
4. **No lo mates por impaciencia**: interrumpir una carga deja `_TMP` a medias y el fichero con
   nombre `_InLoad`, lo que exige limpieza manual después. Ver [D08_gpg_historificacion](../D%20-%20Carga%20STG/D08_gpg_historificacion.md).

## Cuándo escalar

- Si el retraso compromete la entrega del día.
- Si el patrón se repite a la misma hora: es un solape estructural entre jobs, y eso se corrige en
  la planificación, no relanzando.

## Ver también

[D12_carga_colgada](../D%20-%20Carga%20STG/D12_carga_colgada.md) · [D06_load_files_pc](../D%20-%20Carga%20STG/D06_load_files_pc.md) · [I15_volumetria_tipica](../I%20-%20Referencia%20de%20datos/I15_volumetria_tipica.md) · [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md) · [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md)

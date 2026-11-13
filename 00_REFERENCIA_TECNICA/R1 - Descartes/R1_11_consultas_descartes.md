---
titulo: "R1.11 — Consultas de diagnóstico de descartes"
familia: R1
etapa: "Validación"
tipo: Runbook
tags:
  - familia/R1
  - etapa/validacion
  - tipo/runbook
keywords: "consultas, SQL, diagnóstico, cuántos descartes, por tabla, por causa, copiar y pegar"
---

# R1.11 — Consultas de diagnóstico de descartes

**Etapa:** Validación
**Tipo:** Runbook
**Palabras clave:** consultas, SQL, diagnóstico, cuántos descartes, por tabla, por causa, copiar y pegar

## En una línea

Las consultas que resuelven el 90 % de las preguntas sobre descartes, listas para pegar.

## Panorama del día

```sql
-- ¿Qué se descartó hoy y por qué?
SELECT des_table_name,
       des_validate,
       count(*)                        AS filas,
       count(DISTINCT des_column_name) AS columnas,
       min(dat_load_date)              AS primera,
       max(dat_load_date)              AS ultima
FROM   stg_s3.aud_load_valid_trace_t
WHERE  dat_load_date::date = CURRENT_DATE
GROUP  BY 1,2
ORDER  BY filas DESC;
```

```sql
-- Estado de todas las cargas de hoy
SELECT cod_load_trace, cod_load_plan, dat_load_date,
       step_load, cod_status,
       amt_register_process    AS ok,
       amt_register_notprocess AS ko,
       des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  dat_load_date::date = CURRENT_DATE
ORDER  BY dat_load_date DESC;
```

`cod_status = -1` marca lo que se detuvo. `des_process_executed` narra el recorrido separado por `|`.

## Sobre una tabla concreta

```sql
-- Reparto por causa de una tabla
SELECT des_validate, des_column_name, count(*) AS filas
FROM   stg_s3.aud_load_valid_trace_t
WHERE  des_table_name = UPPER('<TABLA>_TMP')
  AND  dat_load_date::date = CURRENT_DATE
GROUP  BY 1,2
ORDER  BY filas DESC;
```

```sql
-- Cuánto hay apartado ahora mismo
SELECT 'ERR' AS destino, count(*) FROM stg_s3.<TABLA>_ERR
UNION ALL
SELECT 'DES',            count(*) FROM stg_s3.<TABLA>_DES
UNION ALL
SELECT 'T (bueno)',      count(*) FROM stg_s3.<TABLA>_T;
```

## Ver las filas concretas que fallaron

```sql
-- Cruza la traza con la tabla por el número de secuencia.
-- Sustituye COD_SEQ_XXX por la columna de secuencia real de la tabla.
SELECT v.des_row_number, v.des_validate, v.des_column_name, t.*
FROM   stg_s3.aud_load_valid_trace_t v
JOIN   stg_s3.<TABLA>_TMP t ON t.COD_SEQ_XXX = v.des_row_number
WHERE  v.cod_load_trace = :trace
ORDER  BY v.des_row_number
LIMIT  20;
```

```sql
-- ¿Cuál es la columna de secuencia de esta tabla?
SELECT c.des_column
FROM   stg_s3.par_maestro_columnas_t c
JOIN   stg_s3.par_maestro_tablas_t   t ON t.cod_table = c.cod_table
WHERE  t.des_table  = UPPER('<TABLA>')
  AND  c.des_column LIKE 'COD_SEQ_%';
```

## Tendencia: ¿esto es nuevo o de siempre?

```sql
SELECT dat_load_date::date AS dia, des_validate, count(*) AS filas
FROM   stg_s3.aud_load_valid_trace_t
WHERE  des_table_name = UPPER('<TABLA>_TMP')
  AND  dat_load_date >= CURRENT_DATE - 30
GROUP  BY 1,2
ORDER  BY 1 DESC, 3 DESC;
```

Serie plana → normalidad. Serie creciente → incidencia real. Ver [R1_10_descarte_correcto_sin_accion](../R1%20-%20Descartes/R1_10_descarte_correcto_sin_accion.md).

## Parametrización: qué se le exige a esta tabla

```sql
-- Comportamiento ante fallo: ¿tolerante o estricto?
SELECT cod_load_plan, des_procedure_run, valid_err_des, des_variation,
       des_separator, amt_num_columns, des_source_dir, des_destiny_dir
FROM   stg_s3.par_load_plan_t
WHERE  cod_load_plan = :plan;
```

```sql
-- Reglas por columna: obligatoriedad, clave, tipo, longitud y máscara
SELECT c.des_column, c.chk_null, c.chk_clave,
       c.data_type, c.data_length, c.amt_decimal,
       m.cod_mask, m.des_reg_exp
FROM   stg_s3.par_maestro_columnas_t c
JOIN   stg_s3.par_maestro_tablas_t   t ON t.cod_table = c.cod_table
LEFT   JOIN stg_s3.par_maestro_mask_t m ON m.cod_mask = c.cod_mask
WHERE  t.des_table = UPPER('<TABLA>')
ORDER  BY c.des_column;
```

```sql
-- Relaciones de integridad declaradas (ojo al formato del nombre: 'STG_S3.TABLA A')
SELECT des_table, des_column, des_table_fk, des_column_fk
FROM   stg_s3.par_maestro_valid_t
WHERE  des_table = 'STG_S3.' || UPPER('<TABLA>') || ' A';
```

## Traza detallada de ejecución

```sql
SELECT dat_load_date, cod_load_plan, step_load, cod_status, des_log
FROM   stg_s3.aud_log_trace_t
WHERE  cod_load_plan = :plan
  AND  dat_load_date >= CURRENT_DATE
ORDER  BY dat_load_date DESC
LIMIT  100;
```

Recuerda que estas marcas de tiempo están escritas con `AT TIME ZONE 'ADT'` salvo en la ruta de
excepción. Ver [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md) antes de correlacionar horas con otros sistemas.

## Ver también

[R1_03_identificar_validacion](../R1%20-%20Descartes/R1_03_identificar_validacion.md) · [R1_02_donde_cae_cada_cosa](../R1%20-%20Descartes/R1_02_donde_cae_cada_cosa.md) · [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md) · [R1_12_descarte_masivo_escalado](../R1%20-%20Descartes/R1_12_descarte_masivo_escalado.md)

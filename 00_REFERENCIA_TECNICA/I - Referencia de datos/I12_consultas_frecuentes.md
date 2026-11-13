---
titulo: "I12 — Consultas de diagnóstico frecuentes"
familia: I
etapa: "Transversal"
tipo: Runbook
tags:
  - familia/I
  - etapa/transversal
  - tipo/runbook
keywords: "consultas, SQL, copiar y pegar, diagnóstico, atajo, transversal"
---

# I12 — Consultas de diagnóstico frecuentes

**Etapa:** Transversal
**Tipo:** Runbook
**Palabras clave:** consultas, SQL, copiar y pegar, diagnóstico, atajo, transversal

## En una línea

Las consultas que se usan a diario, en un solo sitio.

## Estado general del día

```sql
SELECT 'errores de carga'      AS que, count(*) AS n
FROM   stg_s3.aud_load_trace_t
WHERE  cod_status = -1 AND dat_load_date::date = CURRENT_DATE
UNION ALL
SELECT 'errores tecnicos', count(*)
FROM   stg_s3.aud_log_trace_t
WHERE  cod_status = -1 AND dat_load_date >= CURRENT_DATE
UNION ALL
SELECT 'descartes hoy', count(*)
FROM   stg_s3.aud_load_valid_trace_t
WHERE  dat_load_date::date = CURRENT_DATE
UNION ALL
SELECT 'errores de mapeo', count(*)
FROM   trf_s3.s3_control_errores_mapeo
WHERE  dat_proc_exe::date = CURRENT_DATE
UNION ALL
SELECT 'interfaces que faltan', count(*)
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
  AND  NOT recebido;
```

Compara con ayer: **lo que importa es la variación**. Ver [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md).

## Recepción

```sql
-- El lote actual
SELECT last_value AS camda FROM exp_s3.controlflag_arquivos_cod_id_seq;

-- Qué falta
SELECT nome_flag_geral, nome_interface_base, recebido, track_status
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = :camda AND (NOT recebido OR NOT track_status);

-- Últimas llegadas por flag
SELECT nome_base, max(data_recebemento) AS ultima, max(id_camda) AS lote
FROM   stg_s3.controlflag_arquivos
WHERE  data > CURRENT_DATE - 30 GROUP BY 1 ORDER BY 2 DESC NULLS LAST;
```

## Carga

```sql
-- Cargas de hoy
SELECT cod_load_trace, cod_load_plan, dat_load_date, step_load, cod_status,
       amt_register_process, des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  dat_load_date::date = CURRENT_DATE ORDER BY dat_load_date DESC;

-- Reparto de una tabla
SELECT 'TMP' AS t, count(*) FROM stg_s3.<TABLA>_TMP
UNION ALL SELECT 'T',   count(*) FROM stg_s3.<TABLA>_T
UNION ALL SELECT 'ERR', count(*) FROM stg_s3.<TABLA>_ERR
UNION ALL SELECT 'DES', count(*) FROM stg_s3.<TABLA>_DES;
```

## Descartes

```sql
-- Qué se descartó y por qué
SELECT des_table_name, des_validate, des_column_name, count(*) AS filas
FROM   stg_s3.aud_load_valid_trace_t
WHERE  dat_load_date::date = CURRENT_DATE
GROUP  BY 1,2,3 ORDER BY filas DESC;

-- ¿Es nuevo o de siempre?
SELECT dat_load_date::date AS dia, des_validate, count(*)
FROM   stg_s3.aud_load_valid_trace_t
WHERE  des_table_name = UPPER('<TABLA>_TMP') AND dat_load_date >= CURRENT_DATE - 30
GROUP  BY 1,2 ORDER BY 1 DESC;
```

## Parametrización

```sql
-- Contrato de una tabla
SELECT c.cod_column, c.des_column, c.data_type, c.data_length,
       c.chk_null, c.chk_clave, c.cod_mask
FROM   stg_s3.par_maestro_columnas_t c
JOIN   stg_s3.par_maestro_tablas_t   t ON t.cod_table = c.cod_table
WHERE  t.des_table = UPPER('<TABLA>') ORDER BY c.cod_column;

-- Comportamiento ante fallo
SELECT cod_load_plan, des_procedure_run, valid_err_des, des_separator, amt_num_columns
FROM   stg_s3.par_load_plan_t WHERE cod_load_plan = :plan;
```

## Mapeos

```sql
-- Estado de un mapeo (todas sus funciones)
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio,
       activo_inactivo, is_fromtis, retry_deadlock, wait_deadlock_seconds
FROM   exp_s3.tablas_mapeio_t
WHERE  lower(nome_tabela_aldrin) = lower('<TABLA>');

-- Errores de mapeo con su mapeo asociado
SELECT e.dat_proc_exe, e.cod_sqlstate, e.des_func, e.des_sqlerrm, t.id_mapeo
FROM   trf_s3.s3_control_errores_mapeo e
LEFT   JOIN exp_s3.tablas_mapeio_t t ON lower(t.nome_fn_mapeio) = lower(e.des_func)
WHERE  e.dat_proc_exe::date = CURRENT_DATE ORDER BY e.dat_proc_exe DESC;

-- Duplicados apartados por un mapeo
SELECT count(*) FROM trf_s3.<TABLA>_err;
```

## Publicación

```sql
-- ¿Se publica este cliente?
SELECT cod_cli, dat_hr_nav, des_status, cod_error, des_error
FROM   trf_s3.s3_interface_control_xml_t
WHERE  cod_cli = '<CLIENTE>' ORDER BY dat_hr_nav DESC LIMIT 5;

-- ¿Se actualizó la tabla hoy?
SELECT max(dat_qlikupdate) FROM trf_s3.<TABLA>;
```

## Bloqueos

```sql
SELECT bloqueada.pid, bloqueante.pid AS bloqueante,
       now() - bloqueada.query_start AS esperando, left(bloqueada.query, 80)
FROM   pg_stat_activity bloqueada
JOIN   LATERAL unnest(pg_blocking_pids(bloqueada.pid)) AS b(pid) ON true
JOIN   pg_stat_activity bloqueante ON bloqueante.pid = b.pid
ORDER  BY esperando DESC;
```

## ⚠ Dos reglas al escribir consultas aquí

**`lower()` en los dos lados** al cruzar identificadores entre tablas de control: guardan el mismo
nombre con distinta caja. Ver [J10_trampas_conocidas](../J%20-%20Operacion/J10_trampas_conocidas.md).

**Filtra siempre por fecha** en las tablas de auditoría: crecen sin purga documentada.

## Ver también

[R1_11_consultas_descartes](../R1%20-%20Descartes/R1_11_consultas_descartes.md) · [R2_08_consultas_duplicados](../R2%20-%20Duplicados/R2_08_consultas_duplicados.md) · [R3_12_consultas_mapeos](../R3%20-%20Errores%20de%20mapeo/R3_12_consultas_mapeos.md) · [R4_10_consultas_que_falta](../R4%20-%20Sets%20incompletos/R4_10_consultas_que_falta.md) · [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md) · [I08_secuencias](../I%20-%20Referencia%20de%20datos/I08_secuencias.md)

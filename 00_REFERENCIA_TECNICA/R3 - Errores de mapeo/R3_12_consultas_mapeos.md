---
titulo: "R3.12 — Consultas de diagnóstico de mapeos"
familia: R3
etapa: "Mapeos"
tipo: Runbook
tags:
  - familia/R3
  - etapa/mapeos
  - tipo/runbook
keywords: "consultas, SQL, mapeos, copiar y pegar, id_mapeo, diagnóstico"
---

# R3.12 — Consultas de diagnóstico de mapeos

**Etapa:** Mapeos
**Tipo:** Runbook
**Palabras clave:** consultas, SQL, mapeos, copiar y pegar, id_mapeo, diagnóstico

## En una línea

Las consultas de la capa de mapeos, en el orden en que se usan.

## 1. Estado de un mapeo

```sql
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio,
       activo_inactivo, is_fromtis,
       retry_deadlock, wait_deadlock_seconds
FROM   exp_s3.tablas_mapeio_t
WHERE  nome_tabela_aldrin ILIKE '%<TABLA>%'
    OR id_mapeo = :id
ORDER  BY id_mapeo, nome_fn_mapeio;
```

Devuelve **todas** las funciones de ese mapeo: comprueba el estado de cada una.

## 2. Errores registrados

```sql
SELECT * FROM trf_s3.s3_control_errores_mapeo
WHERE  dat_proc_exe::date = CURRENT_DATE
ORDER  BY dat_proc_exe DESC;
```

```sql
-- Errores por hora, para ver si hubo una racha
SELECT date_trunc('hour', dat_proc_exe) AS hora, count(*)
FROM   trf_s3.s3_control_errores_mapeo
WHERE  dat_proc_exe > NOW() - INTERVAL '2 days'
GROUP  BY 1 ORDER BY 1 DESC;
```

Recuerda que el job de control sólo mira los últimos 30 minutos: esta consulta ve lo que él no ve.
Ver [G09_job_control_errores](../G%20-%20Mapeos/G09_job_control_errores.md).

## 3. Origen frente a destino

```sql
SELECT (SELECT count(*) FROM trf_s3.<TABLA_ORIGEN>)  AS origen,
       (SELECT count(*) FROM trf_s3.<TABLA_DESTINO>) AS destino;
```

## 4. Catálogo de mapeos

```sql
-- Activos
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio
FROM   exp_s3.tablas_mapeio_t WHERE activo_inactivo ORDER BY id_mapeo;

-- Desactivados: la respuesta preparada a "¿por qué no tengo datos de X?"
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio
FROM   exp_s3.tablas_mapeio_t WHERE NOT activo_inactivo ORDER BY id_mapeo;

-- Parcialmente activos: los que dan diagnósticos confusos
SELECT id_mapeo,
       count(*)                                AS funciones,
       count(*) FILTER (WHERE activo_inactivo) AS activas
FROM   exp_s3.tablas_mapeio_t
GROUP  BY 1
HAVING count(*) FILTER (WHERE activo_inactivo) BETWEEN 1 AND count(*) - 1;
```

## 5. Configuración de reintentos

```sql
-- Mapeos sin reintento: fallan al primer deadlock
SELECT id_mapeo, nome_tabela_aldrin, retry_deadlock, wait_deadlock_seconds
FROM   exp_s3.tablas_mapeio_t
WHERE  activo_inactivo AND coalesce(retry_deadlock, 0) = 0
ORDER  BY id_mapeo;
```

## 6. Leer la lógica de un mapeo

```sql
SELECT prosrc FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'exp_s3' AND p.proname = '<nome_fn_mapeio>';
```

```sql
-- Todas las funciones de mapeo que existen
SELECT p.proname
FROM   pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'exp_s3' AND p.proname ILIKE 'mapeo%'
ORDER  BY 1;
```

Cruzar esta lista con la tabla de control detecta funciones huérfanas y referencias rotas:

```sql
SELECT t.id_mapeo, t.nome_fn_mapeio,
       (SELECT count(*) FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
        WHERE n.nspname = 'exp_s3' AND p.proname = t.nome_fn_mapeio) AS existe
FROM   exp_s3.tablas_mapeio_t t
WHERE  t.activo_inactivo
ORDER  BY 3, 1;
```

Un `existe = 0` es un mapeo activo cuya función no está: fallará siempre.

## 7. Bloqueos en caliente

```sql
SELECT bloqueada.pid, bloqueante.pid AS bloqueante,
       now() - bloqueada.query_start AS esperando,
       left(bloqueada.query, 80)
FROM   pg_stat_activity bloqueada
JOIN   LATERAL unnest(pg_blocking_pids(bloqueada.pid)) AS b(pid) ON true
JOIN   pg_stat_activity bloqueante ON bloqueante.pid = b.pid
ORDER  BY esperando DESC;
```

```sql
SELECT deadlocks FROM pg_stat_database WHERE datname = current_database();
```

## 8. Claves del destino

Para saber cómo resuelve conflictos un mapeo:

```sql
SELECT conname, pg_get_constraintdef(oid)
FROM   pg_constraint
WHERE  conrelid = 'trf_s3.<TABLA_DESTINO>'::regclass AND contype IN ('p','u');
```

## Ver también

[R3_01_anatomia_fallo_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_01_anatomia_fallo_mapeo.md) · [G02_tablas_mapeio_activo](../G%20-%20Mapeos/G02_tablas_mapeio_activo.md) · [G09_job_control_errores](../G%20-%20Mapeos/G09_job_control_errores.md) · [R3_10_corrio_pero_no_llego](../R3%20-%20Errores%20de%20mapeo/R3_10_corrio_pero_no_llego.md)

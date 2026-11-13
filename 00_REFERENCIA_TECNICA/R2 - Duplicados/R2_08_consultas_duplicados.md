---
titulo: "R2.08 — Consultas de diagnóstico de duplicados"
familia: R2
etapa: "Transversal"
tipo: Runbook
tags:
  - familia/R2
  - etapa/transversal
  - tipo/runbook
keywords: "consultas, SQL, duplicados, copiar y pegar, diagnóstico, clave declarada"
---

# R2.08 — Consultas de diagnóstico de duplicados

**Etapa:** Transversal
**Tipo:** Runbook
**Palabras clave:** consultas, SQL, duplicados, copiar y pegar, diagnóstico, clave declarada

## En una línea

Las consultas para encontrar, clasificar y dimensionar duplicados, listas para pegar.

## Paso 1 — ¿Cuál es la clave de esta tabla?

Todo lo demás depende de esto. La clave «oficial» está en la parametrización, no en la base de datos
(las tablas de staging no tienen restricciones).

```sql
SELECT string_agg(c.des_column, ', ' ORDER BY c.cod_column) AS columnas_clave,
       count(*)                                              AS n_columnas
FROM   stg_s3.par_maestro_columnas_t c
JOIN   stg_s3.par_maestro_tablas_t   t ON t.cod_table = c.cod_table
WHERE  t.des_table = UPPER('<TABLA>') AND c.chk_clave = 1;
```

Si devuelve `n_columnas = 0`, la tabla no tiene clave declarada: nada de lo que sigue tiene sentido,
y además el reproceso de descartes está roto para ella. Ver [E03_par_maestro_tablas_columnas](../E%20-%20Parametrizacion/E03_par_maestro_tablas_columnas.md).

## Paso 2 — ¿Hay duplicados?

```sql
SELECT <col1>, <col2>, count(*) AS repeticiones
FROM   stg_s3.<TABLA>_T
GROUP  BY 1,2
HAVING count(*) > 1
ORDER  BY repeticiones DESC
LIMIT  20;
```

Y el resumen, más útil para dimensionar:

```sql
SELECT count(*)                            AS claves_duplicadas,
       sum(repeticiones)                   AS filas_implicadas,
       sum(repeticiones) - count(*)        AS filas_sobrantes,
       max(repeticiones)                   AS peor_caso
FROM  (SELECT <col1>, <col2>, count(*) AS repeticiones
       FROM   stg_s3.<TABLA>_T
       GROUP  BY 1,2 HAVING count(*) > 1) d;
```

## Paso 3 — ¿Dentro del fichero o entre cargas?

```sql
SELECT <col1>, <col2>,
       count(*)                       AS repeticiones,
       count(DISTINCT cod_load_trace) AS cargas,
       string_agg(DISTINCT cod_load_trace::text, ', ') AS traces
FROM   stg_s3.<TABLA>_T
GROUP  BY 1,2
HAVING count(*) > 1
ORDER  BY cargas DESC, repeticiones DESC
LIMIT  20;
```

`cargas = 1` → el origen mandó la fila repetida. `cargas > 1` → el proceso la metió dos veces.
Ver [R2_03_dentro_o_entre_cargas](../R2%20-%20Duplicados/R2_03_dentro_o_entre_cargas.md).

## Paso 4 — Reparto por carga

```sql
SELECT cod_load_trace, count(*) AS filas, min(dat_load_date) AS primera
FROM   stg_s3.<TABLA>_T t
LEFT   JOIN stg_s3.aud_load_trace_t a USING (cod_load_trace)
GROUP  BY 1 ORDER BY 1 DESC LIMIT 10;
```

Dos `cod_load_trace` con conteos idénticos el mismo día = carga repetida.

## Paso 5 — ¿Se propagó?

```sql
-- Capa de negocio
SELECT count(*) FROM trf_s3.<TABLA> WHERE <clave> = :valor;

-- Capa de salida
SELECT count(*) FROM trf_s3.<TABLA_DESTINO> WHERE <clave> = :valor;
```

Recuerda que en la tabla de salida del mapeo el duplicado puede haberse resuelto por `ON CONFLICT` y manifestarse como
un valor sobrescrito, no como filas de más. Ver [R2_06_duplicados_en_mapeos](../R2%20-%20Duplicados/R2_06_duplicados_en_mapeos.md).

## Barrido general: ¿qué tablas tienen duplicados ahora?

Consulta cara — no la lances en horario de carga. Recorre las tablas con clave declarada y cuenta
duplicados en cada una.

```sql
DO $$
DECLARE
    r     record;
    n     bigint;
    clave text;
BEGIN
    FOR r IN
        SELECT t.des_table,
               string_agg(c.des_column, ',' ORDER BY c.cod_column) AS cols
        FROM   stg_s3.par_maestro_tablas_t   t
        JOIN   stg_s3.par_maestro_columnas_t c ON c.cod_table = t.cod_table
        WHERE  c.chk_clave = 1
        GROUP  BY t.des_table
    LOOP
        clave := r.cols;
        BEGIN
            EXECUTE format(
              'SELECT count(*) FROM (SELECT %s FROM stg_s3.%I GROUP BY %s HAVING count(*)>1) x',
              clave, lower(r.des_table) || '_t', clave) INTO n;
            IF n > 0 THEN
                RAISE NOTICE '% -> % claves duplicadas', r.des_table, n;
            END IF;
        EXCEPTION WHEN OTHERS THEN
            RAISE NOTICE '% -> no evaluable (%)', r.des_table, SQLERRM;
        END;
    END LOOP;
END $$;
```

El bloque captura errores por tabla, así que una tabla inexistente o con nombre distinto no
interrumpe el barrido: sale como «no evaluable».

## Ver también

[R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md) · [R2_03_dentro_o_entre_cargas](../R2%20-%20Duplicados/R2_03_dentro_o_entre_cargas.md) · [R2_07_limpiar_sin_romper](../R2%20-%20Duplicados/R2_07_limpiar_sin_romper.md) · [R1_11_consultas_descartes](../R1%20-%20Descartes/R1_11_consultas_descartes.md)

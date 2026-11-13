---
titulo: "D05 — `RUN_LOAD_PLAN_PC`: el motor de la carga"
familia: D
etapa: "Carga STG"
tipo: Referencia
tags:
  - familia/D
  - etapa/carga-stg
  - tipo/referencia
keywords: "run_load_plan_pc, cod_load_trace, SEQ_COD_LOAD_TRACE, plan de carga, orquestador"
---

# D05 — `RUN_LOAD_PLAN_PC`: el motor de la carga

**Etapa:** Carga STG
**Tipo:** Referencia
**Palabras clave:** run_load_plan_pc, cod_load_trace, SEQ_COD_LOAD_TRACE, plan de carga, orquestador

## En una línea

Genera el `cod_load_trace`, lee el plan de carga, invoca dinámicamente el procedimiento que ese
plan indique y, si todo va bien, lanza las validaciones.

## Detalle

### Qué hace, en orden

```
1. cod_load_trace := nextval('stg_s3.SEQ_COD_LOAD_TRACE')
2. Lee la fila de PAR_LOAD_PLAN_T donde cod_load_plan = <parámetro>
3. call stg_s3.<DES_PROCEDURE_RUN>(13 parámetros)   ← normalmente LOAD_FILES_PC
4. Si el código de salida es 0 → VALIDATE_GEN_PC
   Si no                      → traza 'ERROR - STOP EJECUCION'
```

**El `cod_load_trace` nace aquí.** Es el identificador que después aparece en `AUD_LOAD_TRACE_T`,
en `AUD_LOAD_VALID_TRACE_T` y como columna en las propias tablas de datos. Es la unidad con la que
se rastrea todo. Si vas a diagnosticar una carga, éste es el número que necesitas.

### El procedimiento es dinámico

```sql
V_QUERY := 'call stg_s3.' || TRIM(V_DES_PROCEDURE_RUN) || '($1,...,$13);';
```

`DES_PROCEDURE_RUN` es una columna de `PAR_LOAD_PLAN_T`. En la práctica casi siempre vale
`LOAD_FILES_PC`, pero una carga podría apuntar a otro procedimiento. Antes de asumir qué corrió,
míralo:

```sql
SELECT cod_load_plan, des_procedure_run FROM stg_s3.par_load_plan_t
WHERE  cod_load_plan = :plan;
```

### Los 13 parámetros que recibe el procedimiento de carga

En este orden: código de proceso, tabla destino, fichero, directorio origen, separador, número de
columnas, directorio de procesados, líneas a borrar, columna a borrar, código de salida,
`cod_load_trace`, entidad geográfica (fijo a `2`), y tabla de secuencia.

Nota: la entidad geográfica se pasa **codificada en el propio código** como `2`, no desde la
columna `COD_ENT_GEO` del plan, que sí se lee pero no se usa en esa llamada.

### ⚠ La rama de error puede ser inalcanzable

El código de salida del procedimiento de carga se pasa como parámetro `INOUT` a través de
`EXECUTE ... USING`. En PL/pgSQL, `EXECUTE ... USING` **no devuelve los valores `INOUT` a las
variables del llamador**: `V_OUT_CODE` se queda con el valor que tenía antes, `0`.

Si eso es así en tu versión, la comparación `IF V_OUT_CODE = 0` siempre es cierta, y por tanto:

- La validación se ejecuta **siempre**, incluso si la carga a `_TMP` falló.
- La traza `'ERROR - STOP EJECUCION'` **nunca se escribe**.

Comprobación directa, y merece la pena hacerla una vez:

```sql
SELECT count(*), min(dat_load_date), max(dat_load_date)
FROM   stg_s3.aud_load_trace_t
WHERE  step_load = 'ERROR - STOP EJECUCION';
```

Si sale `0` filas en todo el histórico, la rama está muerta y **no puedes usar su ausencia como
prueba de que las cargas fueron bien**.

### Qué sí es fiable

- El `cod_load_trace` generado.
- La traza `'CARGA FICHERO'` que escribe `LOAD_FILES_PC` con el conteo de filas.
- Lo que escriban las validaciones en `des_process_executed`.

Ver [D06_load_files_pc](../D%20-%20Carga%20STG/D06_load_files_pc.md) para los matices de esa traza.

## Cómo verificarlo

```sql
-- Recorrido completo de una carga por su trace
SELECT * FROM stg_s3.aud_load_trace_t WHERE cod_load_trace = :trace;

-- Últimos valores de la secuencia (útil para saber qué trace es el de ahora)
SELECT last_value FROM stg_s3.seq_cod_load_trace;
```

## Ver también

[D01_mecanica_carga_copy](../D%20-%20Carga%20STG/D01_mecanica_carga_copy.md) · [D06_load_files_pc](../D%20-%20Carga%20STG/D06_load_files_pc.md) · [E02_par_load_plan_t](../E%20-%20Parametrizacion/E02_par_load_plan_t.md) · [E06_tablas_auditoria](../E%20-%20Parametrizacion/E06_tablas_auditoria.md) · [R1_01_descarte_vs_error](../R1%20-%20Descartes/R1_01_descarte_vs_error.md)

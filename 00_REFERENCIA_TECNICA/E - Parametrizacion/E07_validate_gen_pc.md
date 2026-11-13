---
titulo: "E07 — `VALIDATE_GEN_PC`: el orquestador de validaciones"
familia: E
etapa: "Validación"
tipo: Referencia
tags:
  - familia/E
  - etapa/validacion
  - tipo/referencia
keywords: "validate_gen_pc, orquestador, orden de validaciones, po_valid_result, flujo"
---

# E07 — `VALIDATE_GEN_PC`: el orquestador de validaciones

**Etapa:** Validación
**Tipo:** Referencia
**Palabras clave:** validate_gen_pc, orquestador, orden de validaciones, po_valid_result, flujo

## En una línea

Es el procedimiento que decide qué se valida, en qué orden y qué se hace con lo que falla — todo
condicionado por `VALID_ERR_DES`.

## Firma

```sql
stg_s3.validate_gen_pc(
    pi_des_table_name   varchar,   -- tabla, sin sufijo
    pi_cod_load_trace   numeric,   -- ejecución
    pi_cod_load_plan    numeric,   -- plan
    pi_des_variation    numeric,   -- tolerancia de volumen (no se usa)
    INOUT po_valid_result integer  -- resultado
)
```

Lo llama `RUN_LOAD_PLAN_PC` justo después de la carga a `_TMP`.

## El flujo tolerante — `VALID_ERR_DES = 1`

```
1. VALIDATE_ROWS_NULL_FN
     si falla → FN_LOAD_DATA_ERR(tabla_TMP, 'NULOS', 'ERR')  → filas a _ERR
                po_valid_result := 0     ← LA CARGA CONTINÚA
2. VALIDATE_ROWS_FORMAT_ENT_FN
     si falla → po_valid_result := 1
                (NO se mueven filas a ninguna tabla)
3. VALIDATE_ROWS_FOREIGN_FN                 ← se ejecuta falle o no el formato
     si falla → FN_LOAD_DATA_ERR(tabla, 'FOREIGN_KEY', 'DES')  → filas a _DES
                po_valid_result := 0     ← LA CARGA CONTINÚA
```

Nada aborta. Las filas malas se apartan y el resto sigue su camino.

## El flujo estricto — `VALID_ERR_DES ≠ 1`

```
1. VALIDATE_ROWS_NULL_FN
     si falla → po_valid_result := -1   ← ABORTA, sin apartar nada
2. VALIDATE_ROWS_FORMAT_ENT_FN
     si falla → po_valid_result := -1   ← ABORTA
3. VALIDATE_ROWS_FOREIGN_FN
     si falla → TRUNCATE TABLE stg_s3.<TABLA>
                po_valid_result := -1   ← ABORTA Y VACÍA LA TABLA
```

Mismo procedimiento, mismo dato, desenlace opuesto. Ver [R1_01_descarte_vs_error](../R1%20-%20Descartes/R1_01_descarte_vs_error.md).

## Lo que NO hace

Tres cosas que suelen darse por supuestas y no ocurren:

- **No comprueba duplicados.** `VALIDATE_ROWS_KEY_FN` existe pero no se invoca aquí.
- **No comprueba variación de volumen.** Recibe `pi_des_variation` y declara variables para ello, pero nunca llama a `VALIDATE_VARIATION_FN`.
- **No mueve las filas con formato inválido.** Sólo deja constancia en la traza; el dato malo se queda en la tabla.

## La narración que deja

A medida que avanza va concatenando `des_process_executed` en `AUD_LOAD_TRACE_T`. Los tramos
posibles son:

| Texto | Significa |
|---|---|
| `Fichero cargado correctamente en la tabla TMP` | La carga llegó a `_TMP` |
| `\|Errores en validación de nulos se inserta en tabla err` | Hubo nulos, filas a `_ERR` |
| `\|Errores en validación de formato se inserta en tabla err` | Hubo fallos de formato (aunque no se muevan filas) |
| `\|Errores en validación de FK se inserta en tabla desc` | Hubo huérfanas, filas a `_DES` |
| `\|Fichero cargado correctamente en la tabla T` | Llegó al final |

Leer esa cadena de izquierda a derecha es la forma más rápida de saber qué le pasó a una carga.

## Manejo de errores

Ante excepción no controlada escribe en `AUD_LOG_TRACE_T` con `cod_status = -1` y el texto
«Excepción no controlada. Consulte con el equipo de mantenimiento del aplicativo», seguido del
error real de PostgreSQL. **Ese mensaje sí contiene la causa técnica**: merece la pena leerlo entero
antes de escalar.

```sql
SELECT dat_load_date, cod_load_plan, des_log
FROM   stg_s3.aud_log_trace_t
WHERE  des_log LIKE '%Excepción no controlada%'
  AND  dat_load_date >= CURRENT_DATE - 1
ORDER  BY dat_load_date DESC;
```

## Cómo verificarlo

```sql
-- Recorrido de validación de una carga concreta
SELECT step_load, cod_status, des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_trace = :trace;
```

## Ver también

[R1_01_descarte_vs_error](../R1%20-%20Descartes/R1_01_descarte_vs_error.md) · [R1_03_identificar_validacion](../R1%20-%20Descartes/R1_03_identificar_validacion.md) · [E02_par_load_plan_t](../E%20-%20Parametrizacion/E02_par_load_plan_t.md) · [E06_tablas_auditoria](../E%20-%20Parametrizacion/E06_tablas_auditoria.md) · [D05_run_load_plan_pc](../D%20-%20Carga%20STG/D05_run_load_plan_pc.md)

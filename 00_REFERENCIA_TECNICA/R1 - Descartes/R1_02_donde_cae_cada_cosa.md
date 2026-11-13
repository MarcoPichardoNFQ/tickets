---
titulo: "R1.02 — Dónde cae cada cosa: `_DES`, `_ERR` y `AUD_LOAD_VALID_TRACE_T`"
familia: R1
etapa: "Validación"
tipo: Referencia
tags:
  - familia/R1
  - etapa/validacion
  - tipo/referencia
keywords: "_DES, _ERR, aud_load_valid_trace_t, fn_load_data_err, fn_merge_into_desc, dónde buscar"
---

# R1.02 — Dónde cae cada cosa: `_DES`, `_ERR` y `AUD_LOAD_VALID_TRACE_T`

**Etapa:** Validación
**Tipo:** Referencia
**Palabras clave:** _DES, _ERR, aud_load_valid_trace_t, fn_load_data_err, fn_merge_into_desc, dónde buscar

## En una línea

`AUD_LOAD_VALID_TRACE_T` dice **qué** falló y en **qué fila**; las tablas `_ERR` y `_DES` guardan
la fila entera; y cuál de las dos recibe la fila depende de la validación que falló.

## Detalle

### Las tres piezas

**1. `stg_s3.AUD_LOAD_VALID_TRACE_T` — el registro del diagnóstico**

Toda validación que encuentra un problema inserta aquí una fila:

| Columna | Contenido |
|---|---|
| `cod_load_trace` | Ejecución de carga afectada |
| `cod_load_plan` | Plan de carga |
| `dat_load_date` | Momento de la detección |
| `des_table_name` | Tabla, normalmente con sufijo `_TMP` |
| `des_column_name` | **La columna concreta que falló** |
| `des_validate` | **Qué validación falló** |
| `des_row_number` | Número de secuencia de la fila dentro del fichero |

Ésta es la tabla que responde «¿por qué se descartó?». Las otras dos sólo guardan la fila.

**2. `TABLA_ERR` — errores de nulos**

`FN_LOAD_DATA_ERR(..., 'NULOS', 'ERR')` copia la fila con `INSERT ... SELECT DISTINCT *` y la
borra de la tabla base. El nombre destino se calcula sustituyendo `TMP` por `ERR` en el nombre.

**3. `TABLA_DES` — descartes de integridad referencial**

`FN_LOAD_DATA_ERR(..., 'FOREIGN_KEY', 'DES')` llama a `FN_MERGE_INTO_DESC`, que hace un
`INSERT ... ON CONFLICT (clave primaria) DO UPDATE`. Después borra la fila **de `_TMP` y de la
tabla base**.

Consecuencia importante: **`_DES` no acumula duplicados**. Si la misma fila se descarta dos días
seguidos, la segunda vez actualiza la primera en lugar de añadirse. El conteo de `_DES` no es un
histórico, es una foto del estado actual.

### Tabla de correspondencia

| Validación | `des_validate` | Fila va a | ¿Sigue la carga? |
|---|---|---|---|
| Nulo obligatorio | `NULOS` | `_ERR` | Sí, si `VALID_ERR_DES = 1` |
| Longitud de texto | `FORMATO VAR` | Sólo traza | Sí |
| Formato numérico | `FORMATO NUM` | Sólo traza | Sí |
| Longitud numérica | `FORMATO LONG NUM` | Sólo traza | Sí |
| Clave foránea | `FOREIGN_KEY` | `_DES` | Sí, si `VALID_ERR_DES = 1` |
| Clave duplicada | `DUPLICADOS` | Sólo traza | Ver [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md) |

### Dos trampas de esta tabla

**Los fallos de formato no mueven la fila.** `validate_gen_pc` registra el fallo de formato en la
traza y marca el resultado, pero **no llama a `FN_LOAD_DATA_ERR` para formato**. La fila con
formato inválido se queda donde está. Si buscas en `_ERR` una fila con formato malo, no la vas a
encontrar: está en la traza y en la tabla normal.

**Los descartes de FK antiguos se renombran mal escritos.** Al empezar, `validate_rows_foreign_fn`
hace:

```sql
UPDATE stg_s3.AUD_LOAD_VALID_TRACE_T
SET    des_validate = 'FOREING_KEY_OLD'
WHERE  cod_load_plan = ... AND des_validate = 'FOREIGN_KEY';
```

Fíjate: **`FOREING_KEY_OLD`**, no `FOREIGN_KEY_OLD`. Si buscas el histórico con la ortografía
correcta no encuentras nada. Los registros del ciclo anterior están bajo el nombre mal escrito.

## Cómo verificarlo

```sql
-- Qué falló hoy, agrupado por validación y tabla
SELECT des_table_name, des_validate, des_column_name, count(*) AS filas
FROM   stg_s3.aud_load_valid_trace_t
WHERE  dat_load_date::date = CURRENT_DATE
GROUP  BY 1,2,3
ORDER  BY filas DESC;

-- Todos los valores de des_validate que existen (incluido el mal escrito)
SELECT des_validate, count(*)
FROM   stg_s3.aud_load_valid_trace_t
GROUP  BY 1 ORDER BY 2 DESC;
```

## Ver también

[R1_01_descarte_vs_error](../R1%20-%20Descartes/R1_01_descarte_vs_error.md) · [R1_03_identificar_validacion](../R1%20-%20Descartes/R1_03_identificar_validacion.md) · [R1_11_consultas_descartes](../R1%20-%20Descartes/R1_11_consultas_descartes.md) · [R1_09_reprocesar_descartes](../R1%20-%20Descartes/R1_09_reprocesar_descartes.md)

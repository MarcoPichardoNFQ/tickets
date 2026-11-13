---
titulo: "R1.06 — Descarte por integridad referencial"
familia: R1
etapa: "Validación"
tipo: Runbook
tags:
  - familia/R1
  - etapa/validacion
  - tipo/runbook
keywords: "FOREIGN_KEY, FK, PAR_MAESTRO_VALID_T, _DES, truncate, catálogo, orden de carga"
---

# R1.06 — Descarte por integridad referencial

**Etapa:** Validación
**Tipo:** Runbook
**Palabras clave:** FOREIGN_KEY, FK, PAR_MAESTRO_VALID_T, _DES, truncate, catálogo, orden de carga

## Síntoma

Filas en `TABLA_DES`, y en la traza `des_validate = 'FOREIGN_KEY'`.
En flujo estricto, el síntoma es peor: **la tabla `_T` aparece vacía**.

## Qué mirar primero

```sql
SELECT des_table_name, des_column_name, count(*) AS filas
FROM   stg_s3.aud_load_valid_trace_t
WHERE  des_validate = 'FOREIGN_KEY'
  AND  dat_load_date::date = CURRENT_DATE
GROUP  BY 1,2
ORDER  BY filas DESC;
```

## Cómo funciona

`validate_rows_foreign_fn()` lee las relaciones declaradas en `stg_s3.PAR_MAESTRO_VALID_T`. Para
cada pareja tabla → tabla referenciada compara dos conteos: cuántas filas tienen el valor no nulo,
y cuántas de ésas casan con la tabla referenciada. Si no coinciden, calcula la diferencia con un
`EXCEPT` y registra las filas huérfanas.

Después `validate_gen_pc()` decide:

- **Tolerante (`VALID_ERR_DES = 1`)**: `FN_LOAD_DATA_ERR(..., 'FOREIGN_KEY', 'DES')` mete las filas
  en `TABLA_DES` mediante `FN_MERGE_INTO_DESC` (upsert por clave primaria), las borra de `_TMP` y
  de la tabla base, y **la carga continúa**.
- **Estricto (`VALID_ERR_DES ≠ 1`)**: ejecuta `TRUNCATE TABLE stg_s3.<TABLA>` y aborta.

### ⚠ El truncado

En flujo estricto no se apartan las filas malas: **se vacía la tabla entera**. Una sola fila
huérfana borra la carga completa de esa tabla. Si te encuentras una `_T` a cero justo después de
una carga que «terminó», comprueba el `VALID_ERR_DES` de su plan antes que ninguna otra cosa.

### Dos rarezas de la parametrización

**El nombre de tabla lleva el alias dentro.** En `PAR_MAESTRO_VALID_T` la columna `DES_TABLE` no
guarda `TABLA`, guarda literalmente `STG_S3.TABLA A` — con el esquema delante y el alias `A`
detrás. Si buscas por el nombre limpio no encuentras la fila:

```sql
SELECT * FROM stg_s3.par_maestro_valid_t
WHERE  des_table = 'STG_S3.' || UPPER('<TABLA>') || ' A';
```

**Los descartes del ciclo anterior se renombran mal escritos.** Antes de validar, la función marca
los `FOREIGN_KEY` previos del mismo plan como `FOREING_KEY_OLD` (con la N y la G intercambiadas).
Búscalos con esa ortografía o no aparecerán.

## Causas probables, por orden

1. **Problema de orden, no de calidad.** La fila es correcta pero el catálogo al que apunta aún no
   se ha cargado. Es con diferencia la causa más frecuente y **se resuelve sola** en la siguiente
   carga si el insumo ya llegó. Candidato directo a reproceso: [R1_09_reprocesar_descartes](../R1%20-%20Descartes/R1_09_reprocesar_descartes.md).
2. **El catálogo referenciado falló su propia carga.** Mira si la tabla referenciada tiene errores
   o descartes en el mismo lote.
3. **Valor nuevo en origen** que todavía no existe en el maestro. Alta pendiente en el sistema de referencia.
4. **Relación mal declarada** en `PAR_MAESTRO_VALID_T`.

## Acción

1. Identifica la tabla referenciada y comprueba si tiene datos de hoy:

```sql
SELECT des_table, des_column, des_table_fk, des_column_fk
FROM   stg_s3.par_maestro_valid_t
WHERE  des_table = 'STG_S3.' || UPPER('<TABLA>') || ' A';
```

2. Si el catálogo llegó después → reproceso, y el descarte desaparece.
3. Si el catálogo no ha llegado → es un problema de set incompleto, familia `R4`.
4. Si el valor no existe en ningún sitio → alta pendiente en el maestro, escalar a negocio.

## Cuándo escalar

- Si el truncado ya ocurrió (flujo estricto): hay que recargar el fichero, no basta con reprocesar.
- Si el valor huérfano es legítimo y falta el alta en el catálogo maestro.

## Ver también

[R1_01_descarte_vs_error](../R1%20-%20Descartes/R1_01_descarte_vs_error.md) · [R1_09_reprocesar_descartes](../R1%20-%20Descartes/R1_09_reprocesar_descartes.md) · [R1_02_donde_cae_cada_cosa](../R1%20-%20Descartes/R1_02_donde_cae_cada_cosa.md) · [R1_10_descarte_correcto_sin_accion](../R1%20-%20Descartes/R1_10_descarte_correcto_sin_accion.md)

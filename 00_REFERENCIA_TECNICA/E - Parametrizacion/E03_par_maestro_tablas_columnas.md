---
titulo: "E03 — `PAR_MAESTRO_TABLAS_T` y `PAR_MAESTRO_COLUMNAS_T`"
familia: E
etapa: "Validación"
tipo: Referencia
tags:
  - familia/E
  - etapa/validacion
  - tipo/referencia
keywords: "par_maestro_tablas_t, par_maestro_columnas_t, chk_null, chk_clave, cod_column, contrato"
---

# E03 — `PAR_MAESTRO_TABLAS_T` y `PAR_MAESTRO_COLUMNAS_T`

**Etapa:** Validación
**Tipo:** Referencia
**Palabras clave:** par_maestro_tablas_t, par_maestro_columnas_t, chk_null, chk_clave, cod_column, contrato

## En una línea

Entre las dos definen el contrato de datos de cada interfaz: qué columnas hay, en qué orden, de qué
tipo, cuáles son obligatorias y cuáles forman la clave.

## `PAR_MAESTRO_TABLAS_T`

| Columna | Contenido |
|---|---|
| `cod_table` | Identificador. La llave con la que se enlaza casi todo |
| `des_table` | Nombre de la tabla, **en mayúsculas y sin sufijo** |
| `des_schema` | Esquema |
| `dat_insert` | Fecha de alta |

El nombre se guarda sin `_TMP`, `_T`, `_ERR` ni `_DES`: los procedimientos los añaden al vuelo. Por
eso las consultas siempre usan `UPPER('<TABLA>')` sin sufijo.

Una tabla que no esté aquí **no se puede cargar**. Varios procedimientos empiezan comprobando
`COUNT(cod_table) = 1` y, si no la encuentran, salen sin hacer nada y sin error visible. Si una
carga «no hace nada» sin quejarse, comprueba esto primero:

```sql
SELECT * FROM stg_s3.par_maestro_tablas_t WHERE des_table = UPPER('<TABLA>');
```

Cero filas, o más de una, rompe el flujo en silencio.

## `PAR_MAESTRO_COLUMNAS_T`

| Columna | Contenido |
|---|---|
| `cod_table` | Tabla a la que pertenece |
| `cod_column` | **Orden de la columna.** Determina el orden del `\COPY` |
| `des_column` | Nombre de la columna |
| `data_type` | Tipo declarado |
| `data_length` | Longitud máxima |
| `amt_decimal` | Número de decimales |
| `cod_mask` | Máscara de formato → `PAR_MAESTRO_MASK_T` |
| `chk_clave` | `1` si forma parte de la clave primaria |
| `chk_null` | `1` si es obligatoria |
| `dat_insert` | Fecha de alta |

### `cod_column` manda sobre el orden físico

La lista de columnas del `\COPY` se construye ordenando por `cod_column`, no por el orden de la
tabla en la base de datos ni por la cabecera del fichero. Si alguien reordena estos valores, el
fichero se carga con los datos cambiados de sitio sin que salte ningún error.
Ver [D04_read_header_fn](../D%20-%20Carga%20STG/D04_read_header_fn.md).

### `chk_null` — usado por la validación de nulos

Las columnas con `chk_null = 1` se comprueban en `VALIDATE_ROWS_NULL_FN`. Cuenta como vacío el NULL,
la cadena vacía y el texto literal `NULL`. Ver [R1_04_descarte_nulo_obligatorio](../R1%20-%20Descartes/R1_04_descarte_nulo_obligatorio.md).

### `chk_clave` — usado por tres cosas distintas

Es la columna más reutilizada del sistema. Marca qué columnas forman la clave, y de ahí beben:

1. **La detección de duplicados** — `VALIDATE_ROWS_KEY_FN` agrupa por ellas. Ver [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md).
2. **El upsert a descartes** — `FN_MERGE_INTO_DESC` construye su `ON CONFLICT` con ellas.
3. **El reproceso de descartes** — `FN_REPROCESO_DESCART` concatena esas columnas para comparar qué falta.

Consecuencia: **una clave mal declarada rompe las tres cosas a la vez**, y de formas que no se
parecen entre sí. Descartes que no se reprocesan, duplicados que no se detectan y upserts que
fallan pueden tener todos la misma causa.

```sql
-- ¿Qué clave tiene declarada esta tabla?
SELECT c.cod_column, c.des_column
FROM   stg_s3.par_maestro_columnas_t c
JOIN   stg_s3.par_maestro_tablas_t   t ON t.cod_table = c.cod_table
WHERE  t.des_table = UPPER('<TABLA>') AND c.chk_clave = 1
ORDER  BY c.cod_column;
```

Cero filas aquí es señal de alarma: sin clave declarada, el reproceso de descartes construye una
consulta inválida y el upsert no tiene sobre qué resolver conflictos.

### Las columnas de control no viajan en el fichero

`COD_SEQ_*`, `COD_ENT_GEO` y `COD_LOAD_TRACE` están declaradas aquí pero se excluyen de la lista
del `\COPY`. Las rellena `LOAD_FILES_PC` después. Ver [D06_load_files_pc](../D%20-%20Carga%20STG/D06_load_files_pc.md).

## Cómo verificarlo

```sql
-- Contrato completo de una interfaz
SELECT c.cod_column, c.des_column, c.data_type, c.data_length,
       c.amt_decimal, c.chk_null, c.chk_clave, c.cod_mask
FROM   stg_s3.par_maestro_columnas_t c
JOIN   stg_s3.par_maestro_tablas_t   t ON t.cod_table = c.cod_table
WHERE  t.des_table = UPPER('<TABLA>')
ORDER  BY c.cod_column;
```

```sql
-- Salud de la parametrización: tablas sin clave declarada
SELECT t.des_table
FROM   stg_s3.par_maestro_tablas_t t
LEFT   JOIN stg_s3.par_maestro_columnas_t c
       ON c.cod_table = t.cod_table AND c.chk_clave = 1
WHERE  c.cod_table IS NULL
ORDER  BY 1;
```

## Ver también

[E01_tablas_par_metadata_driven](../E%20-%20Parametrizacion/E01_tablas_par_metadata_driven.md) · [E04_par_maestro_mask_t](../E%20-%20Parametrizacion/E04_par_maestro_mask_t.md) · [D04_read_header_fn](../D%20-%20Carga%20STG/D04_read_header_fn.md) · [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md) · [R1_09_reprocesar_descartes](../R1%20-%20Descartes/R1_09_reprocesar_descartes.md)

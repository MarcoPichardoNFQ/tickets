---
titulo: "D01 — Mecánica de carga: `\COPY`, `_TMP` y `_T`"
familia: D
etapa: "Carga STG"
tipo: Referencia
tags:
  - familia/D
  - etapa/carga-stg
  - tipo/referencia
keywords: "COPY, _TMP, _T, carga, staging, run_load_plan_pc, load_files_pc"
---

# D01 — Mecánica de carga: `\COPY`, `_TMP` y `_T`

**Etapa:** Carga STG
**Tipo:** Referencia
**Palabras clave:** COPY, _TMP, _T, carga, staging, run_load_plan_pc, load_files_pc

## En una línea

El fichero entra por `\COPY` en la tabla `_TMP`, un procedimiento le pone las columnas de control,
las validaciones apartan lo malo, y lo que sobrevive queda en `_T`.

## Detalle

### La secuencia completa

```
1. load_stgtrf_script.sh    → busca el fichero, lo renombra a *_InLoad.csv
2. READ_HEADER_FN(0, tabla) → TRUNCA _TMP y devuelve la lista de columnas
3. \COPY tabla_TMP(cols) FROM fichero DELIMITERS 'sep' CSV HEADER
4. RUN_LOAD_PLAN_PC(plan, fichero, 0)
     ├── genera cod_load_trace desde SEQ_COD_LOAD_TRACE
     ├── lee la fila del plan en PAR_LOAD_PLAN_T
     ├── llama al procedimiento del plan (normalmente LOAD_FILES_PC)
     │     ├── asigna COD_SEQ_*, COD_ENT_GEO y COD_LOAD_TRACE
     │     ├── convierte '' y 'NULL' en NULL de verdad
     │     ├── hace TRIM de todas las columnas
     │     └── inserta la traza 'CARGA FICHERO' en AUD_LOAD_TRACE_T
     └── llama a VALIDATE_GEN_PC → nulos, formato, claves foráneas
5. Si fue bien: el fichero se cifra con GPG y se archiva
```

### Quién hace qué

**El `\COPY` lo lanza el shell, no la base de datos.** Es un comando de `psql`, y por eso el
fichero se lee desde el sistema de ficheros del servidor donde corre el script.

**`LOAD_FILES_PC` no carga nada.** A pesar del nombre, cuando se ejecuta el fichero ya está dentro
de `_TMP`. Lo que hace es acondicionar esas filas: numerarlas, marcarlas con el `cod_load_trace` y
normalizarlas. Ver [D06_load_files_pc](../D%20-%20Carga%20STG/D06_load_files_pc.md).

**La lista de columnas la decide la parametrización, no el fichero.** `READ_HEADER_FN` construye el
listado desde `PAR_MAESTRO_COLUMNAS_T`, excluyendo tres columnas de control. Si el fichero trae un
número distinto de columnas, el `\COPY` falla. Ver [D04_read_header_fn](../D%20-%20Carga%20STG/D04_read_header_fn.md) y [D09_error_numero_columnas](../D%20-%20Carga%20STG/D09_error_numero_columnas.md).

### Las tres columnas de control

Toda tabla de staging lleva tres columnas que **no vienen en el fichero**:

| Columna | Qué es | Quién la rellena |
|---|---|---|
| `COD_SEQ_*` | Número de secuencia de la fila | `LOAD_FILES_PC`, desde una secuencia |
| `COD_LOAD_TRACE` | Identificador de la ejecución de carga | `LOAD_FILES_PC` |
| `COD_ENT_GEO` | Entidad geográfica | `LOAD_FILES_PC`, desde el plan |

`COD_SEQ_*` es la columna que usa toda la maquinaria de descartes como «número de fila»
(`des_row_number` en la traza). Es tu manera de localizar una fila concreta.

### Normalización silenciosa

Antes de validar, `LOAD_FILES_PC` recorre todas las columnas y hace dos pasadas:

```sql
-- 1. Cadena vacía y texto 'NULL' pasan a ser NULL de verdad
UPDATE ... SET col = NULL WHERE trim(col) = '' OR UPPER(col) = 'NULL';
-- 2. Se recortan los espacios
UPDATE ... SET col = trim(col) WHERE col IS NOT NULL;
```

Esto explica por qué un campo que trae el texto `"NULL"` acaba disparando la validación de nulos:
para cuando ésta se ejecuta, ya es un NULL real. Ver [R1_04_descarte_nulo_obligatorio](../R1%20-%20Descartes/R1_04_descarte_nulo_obligatorio.md).

## Cómo verificarlo

```sql
-- Estado de las tres tablas de una interfaz
SELECT 'TMP' AS t, count(*) FROM stg_s3.<TABLA>_TMP
UNION ALL SELECT 'T',   count(*) FROM stg_s3.<TABLA>_T
UNION ALL SELECT 'ERR', count(*) FROM stg_s3.<TABLA>_ERR
UNION ALL SELECT 'DES', count(*) FROM stg_s3.<TABLA>_DES;
```

## Ver también

[D03_script_stg_trf](../D%20-%20Carga%20STG/D03_script_stg_trf.md) · [D04_read_header_fn](../D%20-%20Carga%20STG/D04_read_header_fn.md) · [D05_run_load_plan_pc](../D%20-%20Carga%20STG/D05_run_load_plan_pc.md) · [D06_load_files_pc](../D%20-%20Carga%20STG/D06_load_files_pc.md) · [R1_01_descarte_vs_error](../R1%20-%20Descartes/R1_01_descarte_vs_error.md)

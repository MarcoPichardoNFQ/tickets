---
titulo: "R2.02 — La traza `DUPLICADOS` y el riesgo del upsert a `_DES`"
familia: R2
etapa: "Validación"
tipo: Referencia
tags:
  - familia/R2
  - etapa/validacion
  - tipo/referencia
keywords: "DUPLICADOS, aud_load_valid_trace_t, ON CONFLICT, fn_merge_into_desc, pérdida de filas"
---

# R2.02 — La traza `DUPLICADOS` y el riesgo del upsert a `_DES`

**Etapa:** Validación
**Tipo:** Referencia
**Palabras clave:** DUPLICADOS, aud_load_valid_trace_t, ON CONFLICT, fn_merge_into_desc, pérdida de filas

## En una línea

`des_validate = 'DUPLICADOS'` casi nunca aparece — y el mecanismo que sí usa claves únicas, el
upsert a `_DES`, puede fallar en silencio y llevarse la fila por delante.

## Detalle

### La marca `DUPLICADOS`

La escribiría `validate_rows_key_fn` con estos campos:

| Campo | Valor |
|---|---|
| `des_validate` | `'DUPLICADOS'` |
| `des_column_name` | `'PRIMARY KEY'` (literal, no el nombre real de la columna) |
| `des_row_number` | **no se informa** |
| `cod_load_plan`, `dat_load_date` | **no se informan** |

Aunque la función llegara a ejecutarse, la traza resultante no diría **qué fila** ni **cuándo**. Y
al quedar `dat_load_date` en NULL, esos registros son invisibles para cualquier consulta filtrada
por fecha, incluidas las que usa internamente `FN_LOAD_DATA_ERR`.

En la práctica la marca no aparece, porque la función no se invoca. Ver [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md).

```sql
-- Compruébalo en tu entorno: lo esperable es cero
SELECT count(*) FROM stg_s3.aud_load_valid_trace_t WHERE des_validate = 'DUPLICADOS';
```

## ⚠ El riesgo real: el upsert a `_DES`

Donde sí hay unicidad de por medio es en el apartado de descartes de clave foránea.
`FN_MERGE_INTO_DESC` construye:

```sql
INSERT INTO stg_s3.<TABLA>_DES (columnas)
SELECT columnas FROM TMP
ON CONFLICT (<columnas con CHK_CLAVE = 1>)
DO UPDATE SET ...;
```

`ON CONFLICT (columnas)` **exige que exista un índice único o restricción sobre esas columnas**. Si
no existe, PostgreSQL responde:

```
there is no unique or exclusion constraint matching the ON CONFLICT specification
```

### ✅ Verificado en producción: 261 tablas afectadas

```sql
SELECT count(*) FROM information_schema.tables t
WHERE  t.table_schema = 'stg_s3' AND t.table_name LIKE '%\_des'
  AND  NOT EXISTS (SELECT 1 FROM pg_index i
                   WHERE i.indrelid = ('stg_s3.'||t.table_name)::regclass
                     AND i.indisunique);
```

**Resultado: 261.** En esas 261 tablas `_DES` no existe el índice único que `ON CONFLICT` necesita,
así que la instrucción no puede completarse.

### Por qué eso destruye filas

`FN_LOAD_DATA_ERR` llama al upsert y **no comprueba su resultado**:

```sql
V_EXECUTE_MERG := stg_s3.FN_MERGE_INTO_DESC(...);   -- puede haber fallado
EXECUTE 'DELETE FROM stg_s3.<TABLA>_TMP WHERE seq = n AND cod_load_trace = t';
EXECUTE 'DELETE FROM stg_s3.<TABLA>     WHERE seq = n AND cod_load_trace = t';
```

`FN_MERGE_INTO_DESC` captura su propia excepción, deja un aviso y **devuelve el texto del error en
lugar de propagarlo**. El llamador ignora ese valor y borra la fila igualmente.

Resultado: la fila desaparece de `_TMP`, desaparece de la tabla base y **no llega a `_DES`**. No
está en ningún sitio, y la única huella es la fila de `AUD_LOAD_VALID_TRACE_T` que dice que se
descartó y un mensaje de error en el log.

### Cómo confirmarlo en tu entorno

Éste es el chequeo que conviene hacer una vez, porque cambia cómo se interpreta cualquier descarte:

```sql
-- Tablas _DES sin índice único: candidatas a perder filas en el descarte
SELECT t.table_name
FROM   information_schema.tables t
WHERE  t.table_schema = 'stg_s3'
  AND  t.table_name LIKE '%\_des'
  AND  NOT EXISTS (
         SELECT 1 FROM pg_index i
         WHERE  i.indrelid = ('stg_s3.' || t.table_name)::regclass
           AND  i.indisunique)
ORDER  BY 1;
```

Y el contraste directo, para una carga concreta:

```sql
-- ¿Cuadran los descartes registrados con los que llegaron a _DES?
SELECT (SELECT count(*) FROM stg_s3.aud_load_valid_trace_t
        WHERE cod_load_trace = :trace AND des_validate = 'FOREIGN_KEY') AS registrados,
       (SELECT count(*) FROM stg_s3.<TABLA>_DES
        WHERE cod_load_trace = :trace)                                   AS en_des;
```

Si `registrados > en_des`, faltan filas. Búscalas también en `_T`: si tampoco están, se perdieron.

### El rastro del fallo

```sql
SELECT dat_load_date, cod_load_plan, des_log
FROM   stg_s3.aud_log_trace_t
WHERE  des_log ILIKE '%MERGE_INTO_DESC%'
  AND  dat_load_date >= CURRENT_DATE - 7
ORDER  BY dat_load_date DESC;
```

## Ver también

[R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md) · [R1_02_donde_cae_cada_cosa](../R1%20-%20Descartes/R1_02_donde_cae_cada_cosa.md) · [R1_06_descarte_integridad_referencial](../R1%20-%20Descartes/R1_06_descarte_integridad_referencial.md) · [R1_09_reprocesar_descartes](../R1%20-%20Descartes/R1_09_reprocesar_descartes.md)

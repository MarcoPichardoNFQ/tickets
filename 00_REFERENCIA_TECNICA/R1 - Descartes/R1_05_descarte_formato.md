---
titulo: "R1.05 — Descarte por formato"
familia: R1
etapa: "Validación"
tipo: Runbook
tags:
  - familia/R1
  - etapa/validacion
  - tipo/runbook
keywords: "FORMATO VAR, FORMATO NUM, FORMATO LONG NUM, PAR_MAESTRO_MASK_T, máscara, regex, longitud"
---

# R1.05 — Descarte por formato

**Etapa:** Validación
**Tipo:** Runbook
**Palabras clave:** FORMATO VAR, FORMATO NUM, FORMATO LONG NUM, PAR_MAESTRO_MASK_T, máscara, regex, longitud

## Síntoma

En la traza aparece `des_validate` con valor `FORMATO VAR`, `FORMATO NUM` o `FORMATO LONG NUM`.

## Qué mirar primero

```sql
SELECT des_table_name, des_column_name, des_validate, count(*) AS filas
FROM   stg_s3.aud_load_valid_trace_t
WHERE  des_validate LIKE 'FORMATO%'
  AND  dat_load_date::date = CURRENT_DATE
GROUP  BY 1,2,3
ORDER  BY filas DESC;
```

## Cómo funciona

`validate_rows_format_ent_fn()` cruza tres tablas maestras —`PAR_MAESTRO_TABLAS_T`,
`PAR_MAESTRO_COLUMNAS_T` y `PAR_MAESTRO_MASK_T`— y aplica una comprobación distinta según el
`COD_MASK` de cada columna:

| `COD_MASK` | Comprobación | `des_validate` |
|---|---|---|
| `1` | `LENGTH(CAST(columna AS VARCHAR)) > DATA_LENGTH` | `FORMATO VAR` |
| `2`, `3`, `4` | La columna **no** cumple la expresión regular `DES_REG_EXP` de la máscara | `FORMATO NUM` |
| `2`, `3`, `4` con decimales | Parte entera o decimal más larga de lo declarado | `FORMATO LONG NUM` |

La expresión regular no está en el código: vive en `PAR_MAESTRO_MASK_T.DES_REG_EXP`. Para saber
qué se le exige exactamente a una columna hay que leer esa fila.

La comprobación de longitud numérica se aplica **sólo a las filas que ya pasaron `FORMATO NUM`**
—las excluye con un `NOT IN` sobre la traza— para no reportar dos veces la misma fila.

## ⚠ Las filas con formato malo no se mueven a ninguna parte

Ésta es la diferencia grande con los nulos. `validate_gen_pc()` registra el fallo de formato en la
traza y marca el resultado, pero **no llama a `FN_LOAD_DATA_ERR` para formato**. La fila se queda
en la tabla normal.

Consecuencia práctica: si buscas en `TABLA_ERR` una fila con formato inválido no la vas a
encontrar. El único rastro está en `AUD_LOAD_VALID_TRACE_T`, y el dato malo **sigue en la tabla
buena**. Para verlo, cruza la traza con la tabla por el número de secuencia.

## Causas probables, por orden

1. **Cambio de longitud en el origen** — un código que antes tenía 10 caracteres ahora tiene 12.
2. **Separador decimal** — coma en vez de punto, o al revés. La función hace `REPLACE(..., ',', '.')` en parte de sus comprobaciones, pero no en todas.
3. **Notación científica o signo** en un campo numérico que la regex no contempla.
4. **Máscara mal parametrizada** — la regex no admite un valor que el negocio considera válido.
5. **Desplazamiento de columnas** — si falla toda una franja de columnas contiguas, el problema es de conversión, no de formato.

## Acción

1. Localiza el valor concreto que falla:

```sql
SELECT v.des_row_number, t.*
FROM   stg_s3.aud_load_valid_trace_t v
JOIN   stg_s3.<TABLA> t
       ON t.<COD_SEQ_...> = v.des_row_number
WHERE  v.des_validate LIKE 'FORMATO%'
  AND  v.cod_load_trace = :trace
LIMIT  10;
```

2. Consulta qué se le exige a esa columna:

```sql
SELECT c.des_column, c.data_type, c.data_length, c.amt_decimal,
       m.cod_mask, m.des_mask, m.des_reg_exp
FROM   stg_s3.par_maestro_columnas_t c
JOIN   stg_s3.par_maestro_mask_t  m ON m.cod_mask = c.cod_mask
JOIN   stg_s3.par_maestro_tablas_t t ON t.cod_table = c.cod_table
WHERE  t.des_table = UPPER('<TABLA>')
  AND  c.des_column = '<COLUMNA>';
```

3. Compara el valor real contra `des_reg_exp`. Si el valor es correcto de negocio, la máscara está
   mal y hay que corregir parametrización — **eso no lo hace BAU**.

## Cuándo escalar

Si el valor es válido para negocio pero la máscara lo rechaza, o si hay que cambiar
`DATA_LENGTH` / `DES_REG_EXP`. Son cambios de contrato de datos.

## Ver también

[R1_03_identificar_validacion](../R1%20-%20Descartes/R1_03_identificar_validacion.md) · [R1_02_donde_cae_cada_cosa](../R1%20-%20Descartes/R1_02_donde_cae_cada_cosa.md) · [R1_04_descarte_nulo_obligatorio](../R1%20-%20Descartes/R1_04_descarte_nulo_obligatorio.md)

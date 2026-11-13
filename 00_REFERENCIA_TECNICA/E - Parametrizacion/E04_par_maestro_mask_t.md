---
titulo: "E04 — `PAR_MAESTRO_MASK_T`: las máscaras de formato"
familia: E
etapa: "Validación"
tipo: Referencia
tags:
  - familia/E
  - etapa/validacion
  - tipo/referencia
keywords: "par_maestro_mask_t, cod_mask, des_reg_exp, expresión regular, formato, máscara"
---

# E04 — `PAR_MAESTRO_MASK_T`: las máscaras de formato

**Etapa:** Validación
**Tipo:** Referencia
**Palabras clave:** par_maestro_mask_t, cod_mask, des_reg_exp, expresión regular, formato, máscara

## En una línea

Cada columna apunta a una máscara, y la máscara contiene la expresión regular que decide si un
valor tiene formato válido.

## Estructura

| Columna | Contenido |
|---|---|
| `cod_mask` | Identificador de la máscara |
| `des_mask` | Descripción del patrón |
| `descripcion` | Texto libre |
| `des_reg_exp` | **La expresión regular que se evalúa** |

## Cómo se aplica

`VALIDATE_ROWS_FORMAT_ENT_FN` decide la comprobación según el `cod_mask` de la columna:

| `cod_mask` | Comprobación | Marca en la traza |
|---|---|---|
| `1` | Longitud: `LENGTH(CAST(col AS VARCHAR)) > data_length` | `FORMATO VAR` |
| `2`, `3`, `4` | La columna **no** cumple `des_reg_exp` | `FORMATO NUM` |
| `2`, `3`, `4` con decimales | Parte entera o decimal más larga de lo declarado | `FORMATO LONG NUM` |

La expresión regular se inserta **literalmente** en la consulta generada:

```sql
INSERT INTO stg_s3.AUD_LOAD_VALID_TRACE_T (...)
SELECT ... FROM stg_s3.<TABLA>_TMP WHERE NOT <des_reg_exp>;
```

Es decir, `des_reg_exp` no es sólo un patrón: es **un fragmento de SQL** que se evalúa como
condición booleana. Puede contener el operador de comparación y referencias a la columna. Por eso
un error de sintaxis en esa celda no produce «formato inválido» sino un fallo de la validación
entera.

### La comprobación de longitud numérica

Para columnas con decimales, la comprobación mide por separado la parte entera y la decimal:

```
parte_entera_permitida = data_length - amt_decimal
```

Y sólo se aplica a las filas que **ya pasaron** `FORMATO NUM`, excluyéndolas con un `NOT IN` sobre
la traza. Así una misma fila no se reporta dos veces por el mismo campo.

## Para qué sirve esto en soporte

Ante un descarte `FORMATO NUM` la pregunta siempre es la misma: **¿qué se le está exigiendo
exactamente a esta columna?** Esta consulta lo responde:

```sql
SELECT c.des_column, c.data_type, c.data_length, c.amt_decimal,
       m.cod_mask, m.des_mask, m.des_reg_exp
FROM   stg_s3.par_maestro_columnas_t c
JOIN   stg_s3.par_maestro_tablas_t   t ON t.cod_table = c.cod_table
JOIN   stg_s3.par_maestro_mask_t     m ON m.cod_mask  = c.cod_mask
WHERE  t.des_table  = UPPER('<TABLA>')
  AND  c.des_column = '<COLUMNA>';
```

Y después se compara contra el valor real que llegó. Si el valor es correcto de negocio pero la
máscara lo rechaza, el problema es de parametrización y **no se arregla desde soporte**.

## Cuántas máscaras hay

```sql
-- Catálogo completo de máscaras y a cuántas columnas afecta cada una
SELECT m.cod_mask, m.des_mask, m.des_reg_exp, count(c.des_column) AS columnas
FROM   stg_s3.par_maestro_mask_t m
LEFT   JOIN stg_s3.par_maestro_columnas_t c ON c.cod_mask = m.cod_mask
GROUP  BY 1,2,3
ORDER  BY columnas DESC;
```

Merece la pena mirarlo una vez: son pocas máscaras cubriendo muchas columnas, así que un cambio en
una sola fila de esta tabla afecta a decenas de interfaces a la vez.

## Ojo con las columnas sin máscara

Una columna con `cod_mask` nulo **no pasa por la validación de formato**. El cursor de la función
hace `INNER JOIN` con `PAR_MAESTRO_MASK_T`, así que las columnas sin máscara sencillamente no se
recorren. No es un fallo, pero conviene saberlo: la ausencia de descartes de formato en una columna
puede significar que no se está comprobando.

```sql
-- Columnas sin máscara asignada en una tabla
SELECT c.des_column, c.data_type
FROM   stg_s3.par_maestro_columnas_t c
JOIN   stg_s3.par_maestro_tablas_t   t ON t.cod_table = c.cod_table
WHERE  t.des_table = UPPER('<TABLA>') AND c.cod_mask IS NULL;
```

## Ver también

[E03_par_maestro_tablas_columnas](../E%20-%20Parametrizacion/E03_par_maestro_tablas_columnas.md) · [R1_05_descarte_formato](../R1%20-%20Descartes/R1_05_descarte_formato.md) · [E01_tablas_par_metadata_driven](../E%20-%20Parametrizacion/E01_tablas_par_metadata_driven.md) · [E07_validate_gen_pc](../E%20-%20Parametrizacion/E07_validate_gen_pc.md)

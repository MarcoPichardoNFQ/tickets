---
titulo: "E05 — `PAR_MAESTRO_VALID_T`: las relaciones de integridad"
familia: E
etapa: "Validación"
tipo: Referencia
tags:
  - familia/E
  - etapa/validacion
  - tipo/referencia
keywords: "par_maestro_valid_t, foreign key, integridad, des_table_fk, alias, STG_S3.TABLA A"
---

# E05 — `PAR_MAESTRO_VALID_T`: las relaciones de integridad

**Etapa:** Validación
**Tipo:** Referencia
**Palabras clave:** par_maestro_valid_t, foreign key, integridad, des_table_fk, alias, STG_S3.TABLA A

## En una línea

Declara qué columna de qué tabla debe existir en qué otra tabla — y guarda los nombres en un
formato peculiar que hay que conocer para poder consultarla.

## Estructura

| Columna | Contenido |
|---|---|
| `des_table` | Tabla origen, en formato `'STG_S3.TABLA A'` |
| `des_column` | Columna origen, a menudo con el alias delante |
| `cod_valid` | Código de la validación |
| `des_valid` | Descripción |
| `des_table_fk` | Tabla referenciada |
| `des_column_fk` | Columna referenciada |
| `dat_insert` | Fecha de alta |

## ⚠ El formato del nombre de tabla

Esto es lo primero que hay que saber, porque si no la consulta devuelve siempre cero filas.

`des_table` **no** contiene `MI_TABLA`. Contiene:

```
STG_S3.MI_TABLA A
```

Con el esquema delante y un alias `A` detrás, separado por un espacio. La función lo construye así:

```sql
WHERE DES_TABLE = 'STG_S3.' || upper(PI_DES_TABLE_NAME || ' A')
```

El alias está ahí porque los nombres se usan directamente para montar el `FROM` de la consulta de
validación. Es parametrización que contiene fragmentos de SQL, igual que las máscaras.

Para consultarla:

```sql
SELECT des_table, des_column, des_table_fk, des_column_fk
FROM   stg_s3.par_maestro_valid_t
WHERE  des_table = 'STG_S3.' || UPPER('<TABLA>') || ' A';
```

O, si no estás seguro del formato exacto:

```sql
SELECT * FROM stg_s3.par_maestro_valid_t
WHERE  des_table ILIKE '%<TABLA>%';
```

## Cómo se usa

`VALIDATE_ROWS_FOREIGN_FN` recorre las parejas tabla → tabla referenciada. Para cada una:

1. Cuenta cuántas filas tienen la columna origen no nula.
2. Cuenta cuántas de ésas casan con la tabla referenciada.
3. Si los dos conteos difieren, calcula la diferencia con `EXCEPT` y registra las filas huérfanas
   con `des_validate = 'FOREIGN_KEY'`.

Una tabla puede tener **varias relaciones declaradas**, y una relación puede abarcar **varias
columnas**: la función las va encadenando con `AND` dentro de la misma comprobación.

## Consecuencias prácticas

**Una relación declarada de más genera descartes fantasma.** Si `PAR_MAESTRO_VALID_T` declara una
relación que el negocio no exige, las filas legítimas acaban en `_DES` todos los días. Síntoma:
descartes estables, siempre del mismo tipo, que nadie echa de menos.
Ver [R1_10_descarte_correcto_sin_accion](../R1%20-%20Descartes/R1_10_descarte_correcto_sin_accion.md).

**Una relación no declarada no se comprueba.** Si una tabla no tiene filas aquí, la función sale
inmediatamente devolviendo `0` —validación correcta— sin comprobar nada. La ausencia de descartes
de integridad no prueba que los datos sean íntegros.

```sql
-- ¿Se le comprueba integridad a esta tabla?
SELECT count(*) FROM stg_s3.par_maestro_valid_t
WHERE  des_table = 'STG_S3.' || UPPER('<TABLA>') || ' A';
```

Cero significa «no se valida», no «está todo bien».

**El orden de carga importa.** La tabla referenciada tiene que estar cargada antes. Ésa es la razón
de ser de la numeración de los bloques. Ver [D07_bloques_optimizacio](../D%20-%20Carga%20STG/D07_bloques_optimizacio.md).

## Cómo verificarlo

```sql
-- Mapa de dependencias: qué tabla necesita a cuál
SELECT des_table, des_column, des_table_fk, des_column_fk
FROM   stg_s3.par_maestro_valid_t
ORDER  BY des_table, des_column;
```

```sql
-- Las tablas más referenciadas: si una de éstas falla, el daño se multiplica
SELECT des_table_fk, count(*) AS la_referencian
FROM   stg_s3.par_maestro_valid_t
WHERE  des_table_fk IS NOT NULL
GROUP  BY 1 ORDER BY 2 DESC LIMIT 20;
```

Esa segunda consulta es valiosa para priorizar: identifica los catálogos cuyo fallo provoca
descartes en cascada por todo el sistema.

## Ver también

[R1_06_descarte_integridad_referencial](../R1%20-%20Descartes/R1_06_descarte_integridad_referencial.md) · [E01_tablas_par_metadata_driven](../E%20-%20Parametrizacion/E01_tablas_par_metadata_driven.md) · [D07_bloques_optimizacio](../D%20-%20Carga%20STG/D07_bloques_optimizacio.md) · [E03_par_maestro_tablas_columnas](../E%20-%20Parametrizacion/E03_par_maestro_tablas_columnas.md)

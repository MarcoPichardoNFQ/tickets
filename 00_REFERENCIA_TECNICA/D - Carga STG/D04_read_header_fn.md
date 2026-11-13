---
titulo: "D04 — `READ_HEADER_FN`: la lista de columnas (y el truncado oculto)"
familia: D
etapa: "Carga STG"
tipo: Referencia
tags:
  - familia/D
  - etapa/carga-stg
  - tipo/referencia
keywords: "read_header_fn, columnas, TRUNCATE, COD_SEQ, COD_ENT_GEO, COD_LOAD_TRACE"
---

# D04 — `READ_HEADER_FN`: la lista de columnas (y el truncado oculto)

**Etapa:** Carga STG
**Tipo:** Referencia
**Palabras clave:** read_header_fn, columnas, TRUNCATE, COD_SEQ, COD_ENT_GEO, COD_LOAD_TRACE

## En una línea

Construye la lista de columnas para el `\COPY` a partir de la parametrización — y, pese a su
nombre, **lo primero que hace es vaciar la tabla `_TMP`**.

## Detalle

### ⚠ El efecto secundario

```sql
V_QUERY := 'TRUNCATE TABLE stg_s3.' || PI_TABLE ||'_TMP';
EXECUTE V_QUERY;
```

Es la primera instrucción del cuerpo, antes de leer nada. Una función que se llama «leer cabecera»
**borra la tabla temporal completa**.

Para el flujo normal está bien: cada carga empieza con `_TMP` limpia. Pero implica dos cosas:

1. **Nunca la llames a mano para «ver las columnas»** si hay una carga en curso o datos que te
   interesen en `_TMP`. Los perderás sin aviso.
2. Si dos cargas de la misma tabla se solapan, la segunda vacía lo que estaba haciendo la primera.

Si sólo quieres la lista de columnas sin efectos, consulta la parametrización directamente
(consulta al final de esta ficha).

### Cómo construye la lista

```sql
SELECT COD_COLUMN, DES_COLUMN FROM stg_s3.PAR_MAESTRO_COLUMNAS_T
WHERE  COD_TABLE = (SELECT COD_TABLE FROM stg_s3.PAR_MAESTRO_TABLAS_T
                    WHERE DES_TABLE = PI_TABLE)
  AND  SUBSTRING(DES_COLUMN, 1, 8) <> 'COD_SEQ_'
  AND  trim(DES_COLUMN) NOT IN ('COD_ENT_GEO', 'COD_LOAD_TRACE')
ORDER  BY 1;
```

Tres reglas:

- **El orden lo marca `COD_COLUMN`**, no el orden físico de la tabla ni el del fichero.
- **Se excluyen las tres columnas de control**: la de secuencia (`COD_SEQ_*`), `COD_ENT_GEO` y `COD_LOAD_TRACE`. Las rellena después `LOAD_FILES_PC`.
- El resultado es una cadena `COL1,COL2,COL3,...` que se inserta literalmente en el `\COPY`.

### Por qué esto importa para diagnosticar

El `\COPY` que se ejecuta es:

```sql
\COPY STG_S3.<TABLA>_TMP(COL1,COL2,...) FROM 'fichero' DELIMITERS '!' CSV HEADER
```

El número de columnas de esa lista **tiene que coincidir exactamente** con el número de campos del
fichero. La lista sale de la parametrización; el fichero sale del origen. Cuando uno de los dos
cambia sin el otro, el `\COPY` falla. Ver [D09_error_numero_columnas](../D%20-%20Carga%20STG/D09_error_numero_columnas.md).

Es decir: **la cabecera real del fichero no se usa para decidir las columnas**. Aunque el `\COPY`
lleve `CSV HEADER`, esa opción sólo sirve para *saltarse* la primera línea, no para interpretarla.
Si el origen reordena sus columnas manteniendo el mismo número, la carga no falla: **carga los
datos cambiados de sitio**. Ése es el fallo más silencioso de toda la etapa.

### Manejo de errores

Ante cualquier excepción, escribe en `AUD_LOAD_TRACE_T` con `step_load = 'LECTURA CABECERA'` y
devuelve `-1`. Ojo: devuelve un número donde el flujo normal devuelve una cadena de columnas, así
que el `\COPY` posterior recibirá `-1` como lista de columnas y fallará con un error confuso.

## Cómo verificarlo

```sql
-- La lista de columnas que se usará, SIN truncar nada
SELECT string_agg(c.des_column, ',' ORDER BY c.cod_column) AS columnas_copy,
       count(*)                                            AS n_columnas
FROM   stg_s3.par_maestro_columnas_t c
JOIN   stg_s3.par_maestro_tablas_t   t ON t.cod_table = c.cod_table
WHERE  t.des_table = UPPER('<TABLA>')
  AND  c.des_column NOT LIKE 'COD_SEQ_%'
  AND  trim(c.des_column) NOT IN ('COD_ENT_GEO','COD_LOAD_TRACE');
```

Compara `n_columnas` con los campos reales del fichero:

```bash
head -1 /ruta/al/fichero.txt | awk -F'!' '{print NF}'
```

## Ver también

[D01_mecanica_carga_copy](../D%20-%20Carga%20STG/D01_mecanica_carga_copy.md) · [D09_error_numero_columnas](../D%20-%20Carga%20STG/D09_error_numero_columnas.md) · [E03_par_maestro_tablas_columnas](../E%20-%20Parametrizacion/E03_par_maestro_tablas_columnas.md) · [D06_load_files_pc](../D%20-%20Carga%20STG/D06_load_files_pc.md)

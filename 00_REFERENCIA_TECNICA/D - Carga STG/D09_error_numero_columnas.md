---
titulo: "D09 — La carga falla por número de columnas"
familia: D
etapa: "Carga STG"
tipo: Runbook
tags:
  - familia/D
  - etapa/carga-stg
  - tipo/runbook
keywords: "extra data after last expected column, missing data for column, COPY, columnas, separador"
---

# D09 — La carga falla por número de columnas

**Etapa:** Carga STG
**Tipo:** Runbook
**Palabras clave:** extra data after last expected column, missing data for column, COPY, columnas, separador

## Síntoma

El `\COPY` falla con un mensaje del tipo:

```
ERROR: extra data after last expected column
ERROR: missing data for column "XXX"
ERROR: invalid input syntax for type numeric: "..."
```

La tabla `_TMP` queda vacía o a medias y la carga no avanza.

## Qué mirar primero

Compara lo que espera la parametrización con lo que trae el fichero.

```sql
-- Lo que espera el sistema
SELECT count(*) AS columnas_esperadas
FROM   stg_s3.par_maestro_columnas_t c
JOIN   stg_s3.par_maestro_tablas_t   t ON t.cod_table = c.cod_table
WHERE  t.des_table = UPPER('<TABLA>')
  AND  c.des_column NOT LIKE 'COD_SEQ_%'
  AND  trim(c.des_column) NOT IN ('COD_ENT_GEO','COD_LOAD_TRACE');
```

```bash
# Lo que trae el fichero (ajusta el separador)
head -1 fichero.txt | awk -F'!' '{print NF}'
awk -F'!' '{print NF}' fichero.txt | sort | uniq -c   # ¿todas las filas igual?
```

Si el `uniq -c` devuelve más de una cifra, **el problema no es el contrato: son filas concretas**
con campos de más. Eso apunta a separador dentro de un valor.

## Causas probables, por orden

**1. Un separador dentro de un dato.** La causa más frecuente. El conversor Java no entrecomilla
los valores: si un campo contiene el carácter separador (`!` o `;`), esa fila tiene un campo de
más y todas las columnas siguientes se desplazan. Ver [C11_separador_dentro_del_dato](../C%20-%20Conversion%20Java/C11_separador_dentro_del_dato.md).

**2. El origen añadió o quitó una columna.** Cambio de contrato. Todas las filas fallan por igual.

**3. Separador equivocado en la parametrización.** El lookup dice `!` y el fichero viene con `;`.
Comprueba que el separador del lookup y el de `PAR_LOAD_PLAN_T` coinciden entre sí y con el fichero.

**4. Cabecera contada como dato.** Si el `\COPY` no lleva `CSV HEADER` y el fichero sí tiene
cabecera, la primera fila se intenta insertar como datos y falla por tipo.

**5. Saltos de línea dentro de un campo.** El conversor los sustituye por espacio, pero un fichero
de otra procedencia puede traerlos.

## El fallo que NO da error

Merece un aviso aparte. Si el origen **reordena** sus columnas manteniendo el mismo número, el
`\COPY` no falla: carga los valores cambiados de sitio. La lista de columnas la fija la
parametrización, y `CSV HEADER` sólo sirve para saltarse la primera línea, no para interpretarla.
Ver [D04_read_header_fn](../D%20-%20Carga%20STG/D04_read_header_fn.md).

Síntoma indirecto: la carga va «bien» pero aparecen descartes masivos de formato o de clave foránea
en columnas que nunca fallaban. Si ves eso, compara la cabecera real del fichero con el orden
esperado:

```sql
SELECT c.cod_column, c.des_column
FROM   stg_s3.par_maestro_columnas_t c
JOIN   stg_s3.par_maestro_tablas_t   t ON t.cod_table = c.cod_table
WHERE  t.des_table = UPPER('<TABLA>')
  AND  c.des_column NOT LIKE 'COD_SEQ_%'
  AND  trim(c.des_column) NOT IN ('COD_ENT_GEO','COD_LOAD_TRACE')
ORDER  BY c.cod_column;
```

```bash
head -1 fichero.txt | tr '!' '\n' | nl
```

Las dos listas tienen que casar **posición a posición**.

## Acción

1. Determina si fallan todas las filas o sólo algunas (el `uniq -c` de arriba).
2. **Todas** → contrato o separador. Escala: es un cambio en el origen o en la parametrización.
3. **Algunas** → localiza las filas con campos de más:

```bash
awk -F'!' -v n=<esperadas> 'NF!=n {print NR": "NF" campos"}' fichero.txt | head
```

4. Si es una fila puntual con un `!` dentro de un dato, el arreglo estructural está en el origen o
   en la conversión, no en base de datos.

## Cuándo escalar

Siempre que la solución pase por cambiar `PAR_MAESTRO_COLUMNAS_T`, el separador del plan, o el
XSD/conversión. Editar el fichero a mano para desatascar una carga puntual es aceptable como medida
temporal, pero **déjalo escrito en el ticket**: si nadie corrige el origen, vuelve mañana.

## Ver también

[D04_read_header_fn](../D%20-%20Carga%20STG/D04_read_header_fn.md) · [D02_lookup_stg_formato](../D%20-%20Carga%20STG/D02_lookup_stg_formato.md) · [C11_separador_dentro_del_dato](../C%20-%20Conversion%20Java/C11_separador_dentro_del_dato.md) · [D10_tabla_t_vacia](../D%20-%20Carga%20STG/D10_tabla_t_vacia.md)

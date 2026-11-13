---
titulo: "R2.01 — Cómo se detectan los duplicados (y por qué en staging no se detectan)"
familia: R2
etapa: "Validación"
tipo: Referencia
tags:
  - familia/R2
  - etapa/validacion
  - tipo/referencia
keywords: "duplicados, validate_rows_key_fn, chk_clave, primary key, sin PK, DUPLICADOS"
---

# R2.01 — Cómo se detectan los duplicados (y por qué en staging no se detectan)

**Etapa:** Validación
**Tipo:** Referencia
**Palabras clave:** duplicados, validate_rows_key_fn, chk_clave, primary key, sin PK, DUPLICADOS

## En una línea

En `stg_s3` **nada impide ni detecta un duplicado**: no hay claves primarias en las tablas de datos,
y la función que debería comprobarlos no se invoca desde ningún sitio.

## Detalle

### Lo que la mayoría supone

Que existe una validación de clave que aparta las filas repetidas, igual que ocurre con los nulos y
las claves foráneas. La función existe: `stg_s3.validate_rows_key_fn()`. Agrupa por las columnas
con `CHK_CLAVE = 1` y registra los repetidos en `AUD_LOAD_VALID_TRACE_T` con
`des_validate = 'DUPLICADOS'`.

### Lo que realmente ocurre

**1. La función no se llama desde ninguna parte.** `VALIDATE_GEN_PC` ejecuta nulos, formato y
claves foráneas. `validate_rows_key_fn` no aparece en ningún otro procedimiento del sistema.

**2. Las tablas de staging no tienen clave primaria.** De las ~1.322 tablas de `stg_s3`, sólo tres
tienen restricción de clave primaria — `controlflag_arquivos`, `controlflag_interfaces` y
`nprinting_ondemand` — y ninguna es una tabla de datos de interfaz. La base de datos **no rechaza**
una fila repetida.

**3. Y si se llamara, no funcionaría.** La función construye la clave así:

```sql
IF V_CHK_CLAVE = 1 THEN
    V_KEY_GROUP := V_DES_TABLE || '.' || V_DES_COLUMN;
END IF;
```

`V_KEY_GROUP` se **sobrescribe** en cada vuelta, no se acumula. En una clave compuesta de tres
columnas sólo queda la última, así que agruparía por una sola columna: marcaría como duplicadas
filas que comparten esa columna pero son distintas. Además la variable nunca se reinicia entre
iteraciones, y el `INSERT` generado referencia el nombre de la tabla como si fuera una columna del
subconsulta, lo que hace fallar la sentencia. La función **no tiene manejador de excepciones**, así
que ese fallo se propagaría al llamador.

### ✅ Verificado en producción

```sql
SELECT des_validate, count(*) FROM stg_s3.aud_load_valid_trace_t GROUP BY 1 ORDER BY 2 DESC;
```

| `des_validate` | Filas |
|---|---|
| `FOREING_KEY_OLD` | 3.174.004 |
| `FOREIGN_KEY` | 1.095.443 |
| `FORMATO LONG NUM` | 784.174 |
| `NULOS` | 361.117 |
| `FORMATO NUM` | 168.143 |
| `FORMATO VAR` | 92.180 |

**`DUPLICADOS` no aparece.** En 5,7 millones de registros de validación acumulados, ni uno solo
procede de la detección de duplicados. La función nunca se ha ejecutado.

### Conclusión operativa

**Un fichero con filas repetidas se carga entero, sin aviso.** Los duplicados que ves en producción
no aparecen en staging: afloran más adelante, cuando el dato llega a una tabla que sí tiene clave —
en `trf_s3`, con sus 185 claves primarias, o en la capa de mapeos, cuyas 119 funciones deduplican
por clave natural y apartan los repetidos en `trf_s3.<TABLA>_err`. Ver [G06_catalogo_mapeos](../G%20-%20Mapeos/G06_catalogo_mapeos.md).

### Dónde sí hay control

| Capa | Control | Qué pasa con un duplicado |
|---|---|---|
| `stg_s3` | **Ninguno** | Se carga silenciosamente |
| `trf_s3` | 185 claves primarias declaradas (de ~638 tablas) | El `INSERT` falla, o el `ON CONFLICT` actualiza |
| `exp_s3` (mapeos) | Deduplicación propia y `ON CONFLICT` | Ver [R2_06_duplicados_en_mapeos](../R2%20-%20Duplicados/R2_06_duplicados_en_mapeos.md) |

Por eso el síntoma habitual no es «la carga falló por duplicado» sino «la transformación falló» o
«un importe aparece dos veces en Qlik». El origen está en staging pero **se manifiesta aguas
abajo**.

## Cómo verificarlo

```sql
-- ¿Tiene esta tabla de staging alguna restricción única? (esperable: ninguna)
SELECT conname, contype
FROM   pg_constraint
WHERE  conrelid = 'stg_s3.<TABLA>_T'::regclass;
```

```sql
-- Duplicados reales según la clave declarada en la parametrización.
-- Primero, cuál es esa clave:
SELECT string_agg(c.des_column, ', ' ORDER BY c.cod_column) AS clave
FROM   stg_s3.par_maestro_columnas_t c
JOIN   stg_s3.par_maestro_tablas_t   t ON t.cod_table = c.cod_table
WHERE  t.des_table = UPPER('<TABLA>') AND c.chk_clave = 1;

-- Y después, con esas columnas:
SELECT <col1>, <col2>, count(*) AS repeticiones
FROM   stg_s3.<TABLA>_T
GROUP  BY 1,2
HAVING count(*) > 1
ORDER  BY repeticiones DESC
LIMIT  20;
```

Ésa es, hoy por hoy, la única detección de duplicados en staging: manual.

## Ver también

[R2_02_traza_duplicados](../R2%20-%20Duplicados/R2_02_traza_duplicados.md) · [R2_03_dentro_o_entre_cargas](../R2%20-%20Duplicados/R2_03_dentro_o_entre_cargas.md) · [R2_08_consultas_duplicados](../R2%20-%20Duplicados/R2_08_consultas_duplicados.md) · [E03_par_maestro_tablas_columnas](../E%20-%20Parametrizacion/E03_par_maestro_tablas_columnas.md)

---
titulo: "R1.08 — Descartes en la capa de mapeos"
familia: R1
etapa: "Mapeos"
tipo: Referencia
tags:
  - familia/R1
  - etapa/mapeos
  - tipo/referencia
keywords: "mapeos, exp_s3, descartes, no es el mismo mecanismo, clave natural"
---

# R1.08 — Descartes en la capa de mapeos

**Etapa:** Mapeos
**Tipo:** Referencia
**Palabras clave:** mapeos, exp_s3, descartes, no es el mismo mecanismo, clave natural

## En una línea

Los mapeos **sí tienen tabla de descartes** —`trf_s3.<TABLA>_err`, en las 119 funciones— pero
aparta **duplicados por clave natural**, no filas que incumplan una validación.

## ⚠ Corrección

Una versión anterior de esta ficha decía que la capa de mapeos no tenía tablas de descarte. Es
falso: **las 119 funciones vivas escriben en `trf_s3.<TABLA>_err`**. Lo que no tienen es la
maquinaria *declarativa* de staging: no hay `PAR_MAESTRO_VALID_T`, ni `AUD_LOAD_VALID_TRACE_T`, ni
tablas `_DES`.

## El patrón real

Siempre el mismo, al final de cada función: una CTE agrupa por la clave natural y manda a `_err` lo
que aparezca más de una vez.

```sql
WITH DuplicatedRecordsCTE AS (
    ... GROUP BY <clave_natural> HAVING COUNT(*) > 1 ...
)
INSERT INTO trf_s3.<TABLA>_err (<columnas>, concatenate)
SELECT <columnas>, concatenate FROM DuplicatedRecordsCTE;
```

Es **deduplicación**, no validación de contenido: una fila va a `_err` por estar repetida en la
clave, no por tener un dato malo.

```sql
-- Qué apartó este mapeo
SELECT count(*) FROM trf_s3.<TABLA>_err;
SELECT * FROM trf_s3.<TABLA>_err ORDER BY dat_qlikupdate DESC LIMIT 20;
```

Ver [G06_catalogo_mapeos](../G%20-%20Mapeos/G06_catalogo_mapeos.md) y [R2_06_duplicados_en_mapeos](../R2%20-%20Duplicados/R2_06_duplicados_en_mapeos.md).

## Detalle

### Por qué es distinto

Las validaciones de staging trabajan sobre un fichero recién aterrizado, fila a fila, contra una
parametrización declarada en tablas `PAR_*`. Un mapeo es otra cosa: una consulta SQL que combina
varias tablas ya validadas de `trf_s3` y escribe el resultado en otra tabla de `trf_s3` (`sac_*`, `cart_*`). No hay «fichero», no
hay «número de fila del fichero», y no hay validación declarativa.

En consecuencia, una fila que no aparece en el destino de un mapeo puede haberse quedado fuera por
razones que **no son un descarte** en el sentido de staging:

- **Un `INNER JOIN` que no casa.** La fila simplemente no entra en el resultado. Muchas veces es un filtro de negocio deliberado, no un fallo.
- **Un filtro `WHERE` de negocio** que excluye estados, tipos o fechas.
- **Deduplicación por clave natural** antes de insertar.
- **`ON CONFLICT`** al insertar: la fila no se añade, actualiza a una anterior.

Ninguna de esas cuatro deja rastro en `AUD_LOAD_VALID_TRACE_T`.

### Dónde sí queda rastro

- **`exp_s3.tablas_mapeio_t`** — control de qué mapeo está activo. Si `activo_inactivo` marca
  inactivo, el mapeo no corre y el destino no se actualiza: eso no es un descarte, es un mapeo apagado.
- **`Job control errores mapeo`** — el job de Rundeck que vigila fallos de mapeo.
- **`stg_s3.aud_log_trace_t`** — traza general, donde los procedimientos dejan mensajes.

### Regla práctica para diagnosticar

Ante «faltan filas en una tabla de salida», el orden de comprobación es:

1. ¿Está el mapeo **activo**? (`tablas_mapeio_t.activo_inactivo`)
2. ¿**Corrió** hoy? (traza y job de Rundeck)
3. ¿Están las filas en el **origen**, en `trf_s3`?
4. Si están en origen y no en destino → es la lógica del mapeo: `JOIN`, `WHERE` o `ON CONFLICT`.

El paso 4 exige leer el SQL de ese mapeo concreto. No hay atajo genérico.

## Estado de esta ficha

Cobertura provisional. El detalle por mapeo —qué filtra cada uno y cuáles deduplican— entra en la
familia `G` (fase 4), junto con el catálogo de mapeos activos y su tabla destino. Esta ficha existe
para evitar el error de arranque más común: buscar descartes de mapeo en las tablas de staging.

## Cómo verificarlo

```sql
-- ¿Está activo este mapeo?
SELECT * FROM exp_s3.tablas_mapeio_t
WHERE  id_mapeo = :id;

-- ¿Hay filas en origen que no llegaron a destino?
-- (sustituye por las tablas reales del mapeo en cuestión)
SELECT count(*) FROM trf_s3.<TABLA_ORIGEN>;
SELECT count(*) FROM trf_s3.<TABLA_DESTINO>;
```

## Ver también

[R1_01_descarte_vs_error](../R1%20-%20Descartes/R1_01_descarte_vs_error.md) · [R1_02_donde_cae_cada_cosa](../R1%20-%20Descartes/R1_02_donde_cae_cada_cosa.md) · [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md)

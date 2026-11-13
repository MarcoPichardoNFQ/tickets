---
titulo: "R2.06 — Duplicados en la capa de mapeos"
familia: R2
etapa: "Mapeos"
tipo: Referencia
tags:
  - familia/R2
  - etapa/mapeos
  - tipo/referencia
keywords: "mapeos, ON CONFLICT, clave natural, exp_s3, deduplicación, upsert"
---

# R2.06 — Duplicados en la capa de mapeos

**Etapa:** Mapeos
**Tipo:** Referencia
**Palabras clave:** mapeos, ON CONFLICT, clave natural, exp_s3, deduplicación, upsert

## En una línea

Al contrario que staging, la capa de mapeos **sí** suele tener claves y `ON CONFLICT`, así que un
duplicado normalmente no se duplica: se sobrescribe — y eso puede ser peor.

## Detalle

### Dónde hay claves y dónde no

| Capa | Claves primarias | Efecto de un duplicado |
|---|---|---|
| `stg_s3` (~1.322 tablas) | 3, ninguna en tablas de datos | Se carga silenciosamente |
| `trf_s3` (~638 tablas) | 185 | El `INSERT` falla o el `ON CONFLICT` actualiza |
| `exp_s3` | Sí en las tablas de salida | `ON CONFLICT` actualiza |

### Los tres comportamientos que verás en un mapeo

**1. `ON CONFLICT ... DO UPDATE` — el upsert.** La segunda fila con la misma clave **no se añade**:
actualiza la primera. No hay duplicado, pero hay algo más sutil: **el último en llegar gana**. Si
dos filas de origen tienen la misma clave y distinto importe, el valor final depende del orden de
procesamiento, que no está garantizado. El síntoma no es «hay filas de más» sino «el importe no es
el que esperaba».

**2. `ON CONFLICT ... DO NOTHING` — el descarte silencioso.** La segunda fila se ignora sin dejar
rastro. Aquí gana el primero.

**3. Deduplicación previa en la consulta.** Muchos mapeos hacen `DISTINCT`, `GROUP BY` o usan una
función de ventana para quedarse con una fila por clave natural antes de insertar. La elección de
cuál sobrevive está en el `ORDER BY` de esa ventana.

En los tres casos, **el duplicado de origen no desaparece: se resuelve en silencio**. Por eso un
problema de duplicados en staging puede manifestarse en Qlik como un importe erróneo, no como filas
de más.

### La consecuencia práctica para diagnóstico

Cuando alguien reporta «este número está mal» y hay duplicados aguas arriba, la cadena es:

```
fichero con la fila repetida
   → staging la carga dos veces (nadie la detecta)
      → el mapeo aplica ON CONFLICT y se queda con UNA
         → Qlik muestra un valor que no es la suma ni el promedio: es "el que ganó"
```

Limpiar el duplicado en staging **no corrige el dato ya publicado**: hay que volver a ejecutar el
mapeo después de limpiar.

## Cómo verificarlo

```sql
-- ¿Qué clave tiene la tabla destino del mapeo?
SELECT conname, pg_get_constraintdef(oid) AS definicion
FROM   pg_constraint
WHERE  conrelid = 'trf_s3.<TABLA_DESTINO>'::regclass
  AND  contype IN ('p','u');
```

```sql
-- ¿Hay duplicados reales en destino? (con las columnas de la clave de arriba)
SELECT <col1>, <col2>, count(*)
FROM   trf_s3.<TABLA_DESTINO>
GROUP  BY 1,2 HAVING count(*) > 1 LIMIT 20;
```

```sql
-- Comparar volúmenes origen y destino: una diferencia grande sugiere deduplicación
SELECT (SELECT count(*) FROM trf_s3.<TABLA_ORIGEN>)   AS origen,
       (SELECT count(*) FROM trf_s3.<TABLA_DESTINO>)  AS destino;
```

Para ver exactamente qué hace un mapeo concreto —si deduplica, con qué criterio y qué gana— hay que
leer su SQL. El catálogo por `id_mapeo` está en la familia `G`.

## Estado de esta ficha

El comportamiento por mapeo individual —cuáles deduplican, con qué clave y qué variante de
`ON CONFLICT` usan— se cataloga en la familia `G` (fase 4). Esta ficha cubre el patrón general y
la consecuencia de diagnóstico, que es lo que se necesita para atender la incidencia.

## Ver también

[R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md) · [R1_08_descartes_en_mapeos](../R1%20-%20Descartes/R1_08_descartes_en_mapeos.md) · [R2_07_limpiar_sin_romper](../R2%20-%20Duplicados/R2_07_limpiar_sin_romper.md) · [R2_09_prevencion_duplicados](../R2%20-%20Duplicados/R2_09_prevencion_duplicados.md)

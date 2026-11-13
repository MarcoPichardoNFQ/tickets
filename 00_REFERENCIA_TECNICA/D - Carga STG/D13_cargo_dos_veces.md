---
titulo: "D13 — El fichero se cargó dos veces"
familia: D
etapa: "Carga STG"
tipo: Runbook
tags:
  - familia/D
  - etapa/carga-stg
  - tipo/runbook
keywords: "doble carga, duplicados, reintento, InLoad, idempotencia, recarga"
---

# D13 — El fichero se cargó dos veces

**Etapa:** Carga STG
**Tipo:** Runbook
**Palabras clave:** doble carga, duplicados, reintento, InLoad, idempotencia, recarga

## Síntoma

Una tabla tiene aproximadamente el doble de filas de lo normal, o aparecen duplicados que el
control de claves no explica.

## Qué mirar primero

```sql
-- ¿Cuántas cargas hubo hoy para este plan?
SELECT cod_load_trace, dat_load_date, des_file_loaded,
       amt_register_process, step_load, cod_status
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_plan = :plan
  AND  dat_load_date::date = CURRENT_DATE
ORDER  BY dat_load_date;
```

Más de una fila `'CARGA FICHERO'` en el mismo día para el mismo plan es la confirmación.

```sql
-- ¿Conviven varios trace en la tabla?
SELECT cod_load_trace, count(*)
FROM   stg_s3.<TABLA>_T
GROUP  BY 1 ORDER BY 1 DESC;
```

## Por qué `_TMP` normalmente lo evita, y cuándo no

Cada carga empieza con `READ_HEADER_FN`, que **trunca `_TMP`**. Eso hace que una segunda carga
sobre `_TMP` no acumule: borra y vuelve a empezar. Ver [D04_read_header_fn](../D%20-%20Carga%20STG/D04_read_header_fn.md).

La duplicación aparece cuando el dato **ya pasó de `_TMP` a `_T`** y luego se vuelve a cargar el
mismo fichero. Ahí no hay truncado que valga: son dos inserciones con dos `cod_load_trace`
distintos.

## Causas probables, por orden

**1. El fichero llegó dos veces con nombres distintos.** El origen reenvía y el patrón del lookup
casa con ambos. El script coge uno por ejecución (`head -1`), así que los procesa en pasadas
sucesivas.

```bash
. /nfq/data/cfg/env.properties
grep '|<id>|' /nfq/data/cfg/lookup_stg.txt    # ver el patrón
ls -la $raiz | grep -i "<parte_del_patrón>"   # ¿cuántos casan?
```

**2. Recarga manual sin comprobar el estado previo.** Alguien relanzó el bloque para desatascar
otra cosa y arrastró una carga que ya se había hecho.

**3. El archivado falló pero la carga fue bien.** El script decide archivar mirando la salida del
`\COPY` con una comprobación frágil. Si esa comprobación falla, el fichero **no se archiva** y se
queda en el directorio: la siguiente pasada lo vuelve a cargar. Los datos entraron dos veces aunque
el log de la primera pareciera indicar error. Ver [D08_gpg_historificacion](../D%20-%20Carga%20STG/D08_gpg_historificacion.md).

**4. Un fichero `_InLoad` restaurado a mano** cuyos datos ya habían entrado.

La causa 3 es la más traicionera porque la traza de la primera carga puede parecer fallida.

## Acción

1. **Confirma el alcance**: cuántos `cod_load_trace` distintos hay en la tabla y cuántas filas
   aporta cada uno.
2. **Comprueba si es duplicación real o convivencia legítima.** Algunas tablas acumulan cargas de
   varios días a propósito. Contrasta con la clave:

```sql
-- ¿Hay claves repetidas de verdad?  (sustituye por la PK real de la tabla)
SELECT <col_pk1>, <col_pk2>, count(*)
FROM   stg_s3.<TABLA>_T
GROUP  BY 1,2 HAVING count(*) > 1
LIMIT  20;
```

Ver [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md) para el mecanismo formal de detección.

3. **Si hay que limpiar**, borra por `cod_load_trace`, nunca por criterios de negocio:

```sql
-- Comprueba primero qué te vas a llevar
SELECT count(*) FROM stg_s3.<TABLA>_T WHERE cod_load_trace = :trace_sobrante;
-- Y sólo entonces
DELETE FROM stg_s3.<TABLA>_T WHERE cod_load_trace = :trace_sobrante;
```

`cod_load_trace` es la única forma segura de identificar «lo que entró en esa carga concreta».

4. **Retira el fichero duplicado** del directorio de trabajo para que no vuelva a entrar.
5. **Comprueba el impacto aguas abajo**: si la transformación y los mapeos ya corrieron con los
   datos duplicados, limpiar staging no basta. Ver [R2_07_limpiar_sin_romper](../R2%20-%20Duplicados/R2_07_limpiar_sin_romper.md).

## Cuándo escalar

- Si los duplicados ya llegaron a `trf_s3` o `exp_s3`: la limpieza cruza varias capas y conviene
  coordinarla.
- Si el origen está reenviando ficheros de forma sistemática: eso se corrige aguas arriba.

## Ver también

[R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md) · [R2_05_duplicados_por_relanzar](../R2%20-%20Duplicados/R2_05_duplicados_por_relanzar.md) · [R2_07_limpiar_sin_romper](../R2%20-%20Duplicados/R2_07_limpiar_sin_romper.md) · [D08_gpg_historificacion](../D%20-%20Carga%20STG/D08_gpg_historificacion.md)

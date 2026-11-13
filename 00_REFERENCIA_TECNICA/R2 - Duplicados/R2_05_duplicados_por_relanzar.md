---
titulo: "R2.05 — Duplicados provocados por relanzar un bloque"
familia: R2
etapa: "Carga STG"
tipo: Runbook
tags:
  - familia/R2
  - etapa/carga-stg
  - tipo/runbook
keywords: "relanzar, rerun, idempotencia, bloque, no idempotente, duplicar"
---

# R2.05 — Duplicados provocados por relanzar un bloque

**Etapa:** Carga STG
**Tipo:** Runbook
**Palabras clave:** relanzar, rerun, idempotencia, bloque, no idempotente, duplicar

## En una línea

Relanzar un bloque no es gratis: la carga a `_TMP` es idempotente porque se trunca, pero **la
transformación no lo es**, y ahí es donde se duplica.

## Qué es idempotente y qué no

| Etapa | ¿Relanzar duplica? | Por qué |
|---|---|---|
| `\COPY` a `_TMP` | **No** | `READ_HEADER_FN` trunca `_TMP` antes de cada carga |
| Paso de `_TMP` a `_T` | **Depende** | Si el fichero sigue en el directorio, se vuelve a cargar con otro `cod_load_trace` |
| Transformación (`trf()`) | **Depende del procedimiento** | Cada uno decide si borra antes de insertar o si acumula |
| Mapeos | **Normalmente no** | Muchos usan `ON CONFLICT` o borran antes. Ver [R2_06_duplicados_en_mapeos](../R2%20-%20Duplicados/R2_06_duplicados_en_mapeos.md) |

La zona peligrosa es la segunda fila: **si el fichero ya se archivó, relanzar no carga nada** y el
bloque simplemente pasa. Pero si el fichero sigue en el directorio de trabajo —porque el archivado
falló—, relanzar lo vuelve a cargar entero.

## Antes de relanzar: la comprobación de 30 segundos

```sql
-- ¿Esta carga ya se hizo hoy?
SELECT cod_load_trace, dat_load_date, des_file_loaded,
       amt_register_process, cod_status, des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_plan = :plan
  AND  dat_load_date::date = CURRENT_DATE
ORDER  BY dat_load_date;
```

```bash
# ¿Sigue el fichero en el directorio de trabajo?
. /nfq/data/cfg/env.properties
grep '|<id>|' /nfq/data/cfg/lookup_stg.txt | cut -d'|' -f4
ls -la $raiz | grep -i "<parte_del_patrón>"
```

**Traza de carga correcta + fichero ya archivado** → relanzar es seguro, no hará nada.
**Traza de carga correcta + fichero todavía en el directorio** → relanzar **duplicará**. Retira el
fichero antes, o acepta que tendrás que limpiar después.

## El efecto de relanzar un bloque entero

Un bloque contiene decenas de pasos. Relanzarlo para arreglar el paso 12 vuelve a ejecutar del 1 al
11 y del 13 al final. Como los errores no detienen el bucle (ver [D03_script_stg_trf](../D%20-%20Carga%20STG/D03_script_stg_trf.md)), **todos**
se ejecutan.

Consecuencias a valorar antes:

- Las cargas cuyo fichero ya se archivó no harán nada: inofensivas.
- Las cargas cuyo fichero siga en el directorio se repetirán.
- **Las transformaciones se ejecutarán todas de nuevo**, y ahí el comportamiento depende de cada
  procedimiento. Los que hacen `INSERT` sin borrado previo acumulan.

Regla práctica: **relanzar un paso concreto es preferible a relanzar el bloque**. Si Rundeck lo
permite, ejecuta sólo el paso afectado con sus argumentos.

## Cómo saber si una transformación acumula

No hay una respuesta general: hay que mirar el procedimiento. La señal rápida es si empieza
borrando:

```sql
-- Ver el cuerpo del procedimiento de transformación
SELECT prosrc
FROM   pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'trf_s3' AND p.proname = '<nombre_procedimiento>';
```

Busca al principio un `DELETE FROM` o un `TRUNCATE` sobre la tabla destino. Si lo tiene, relanzar es
seguro. Si empieza directamente con `INSERT`, acumula.

Para saber qué procedimiento corresponde a un valor del bloque:

```bash
grep '|<id>|' /nfq/data/cfg/lookup_trf.txt | cut -d'|' -f3
```

## Después de relanzar: verificar

```sql
-- ¿Cuántos trace conviven ahora en la tabla?
SELECT cod_load_trace, count(*)
FROM   stg_s3.<TABLA>_T
GROUP  BY 1 ORDER BY 1 DESC;
```

Si aparecen dos `cod_load_trace` del mismo día donde antes había uno, se duplicó.
Ver [R2_07_limpiar_sin_romper](../R2%20-%20Duplicados/R2_07_limpiar_sin_romper.md).

## Cuándo escalar

- Antes de relanzar en producción un bloque completo durante la ventana operativa.
- Si el relanzamiento ya duplicó y el dato llegó a `trf_s3` o `exp_s3`.

## Ver también

[D13_cargo_dos_veces](../D%20-%20Carga%20STG/D13_cargo_dos_veces.md) · [R2_07_limpiar_sin_romper](../R2%20-%20Duplicados/R2_07_limpiar_sin_romper.md) · [D03_script_stg_trf](../D%20-%20Carga%20STG/D03_script_stg_trf.md) · [D07_bloques_optimizacio](../D%20-%20Carga%20STG/D07_bloques_optimizacio.md) · [R2_06_duplicados_en_mapeos](../R2%20-%20Duplicados/R2_06_duplicados_en_mapeos.md)

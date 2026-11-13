---
titulo: "F14 — Faltan datos: ¿el problema está en STG o en TRF?"
familia: F
etapa: "Transformación TRF"
tipo: Runbook
tags:
  - familia/F
  - etapa/transformacion-trf
  - tipo/runbook
keywords: "dónde está el problema, staging o transformación, aislar, capa, diagnóstico"
---

# F14 — Faltan datos: ¿el problema está en STG o en TRF?

**Etapa:** Transformación TRF
**Tipo:** Runbook
**Palabras clave:** dónde está el problema, staging o transformación, aislar, capa, diagnóstico

## En una línea

Tres consultas sitúan el problema en una capa concreta, y a partir de ahí el diagnóstico ya está
escrito en otra ficha.

## Las tres consultas

```sql
-- 1. ¿Llegó y se cargó?
SELECT count(*) FROM stg_s3.<TABLA>_T;

-- 2. ¿Se apartó algo?
SELECT 'ERR' AS t, count(*) FROM stg_s3.<TABLA>_ERR
UNION ALL SELECT 'DES', count(*) FROM stg_s3.<TABLA>_DES;

-- 3. ¿Llegó al modelo de negocio?
SELECT count(*) FROM trf_s3.<TABLA_DESTINO>;
```

## La tabla de decisión

| `stg_s3._T` | `_ERR`/`_DES` | `trf_s3` | Dónde está el problema | Ficha |
|---|---|---|---|---|
| 0 | 0 | 0 | **Antes de STG**: no llegó o no se cargó | [D10_tabla_t_vacia](../D%20-%20Carga%20STG/D10_tabla_t_vacia.md) |
| 0 | >0 | 0 | **Validación**: se apartó todo | [R1_12_descarte_masivo_escalado](../R1%20-%20Descartes/R1_12_descarte_masivo_escalado.md) |
| >0 | — | 0 | **TRF**: cargó pero no transformó | [F11_trf_corrio_sin_cambios](../F%20-%20Transformacion%20TRF/F11_trf_corrio_sin_cambios.md) |
| >0 | — | menos de lo esperado | **TRF**: filtro o join del procedimiento | [F11_trf_corrio_sin_cambios](../F%20-%20Transformacion%20TRF/F11_trf_corrio_sin_cambios.md) |
| >0 | — | >0 correcto | **Después de TRF**: mapeo o Qlik | [R3_01_anatomia_fallo_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_01_anatomia_fallo_mapeo.md) |

Cinco filas que cubren prácticamente todos los casos.

## Cómo saber qué tabla de `trf_s3` corresponde

Es la pregunta que bloquea el paso 3. El índice está en [I09_indice_tabla_origen](../I%20-%20Referencia%20de%20datos/I09_indice_tabla_origen.md), y en la base:

```sql
-- Procedimientos cuyo nombre menciona la tabla
SELECT p.proname
FROM   pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'trf_s3' AND p.proname ILIKE '%<parte_del_nombre>%';
```

```bash
# O por el lookup, que enlaza id → procedimiento → tabla origen
grep -i "<TABLA>" /nfq/data/cfg/lookup_trf.txt
```

## Si el problema está en TRF, acota más

```sql
-- ¿Hubo error registrado?
SELECT dat_load_date, cod_load_plan, step_load, cod_status, des_log
FROM   stg_s3.aud_log_trace_t
WHERE  cod_status = -1 AND dat_load_date >= CURRENT_DATE
ORDER  BY dat_load_date DESC;
```

Y si no hay error pero tampoco datos, las cinco causas están en [F11_trf_corrio_sin_cambios](../F%20-%20Transformacion%20TRF/F11_trf_corrio_sin_cambios.md):
insumo vacío, descarte masivo, bloqueo por cliente, filtro del procedimiento, o una transformación
que actualiza en vez de insertar.

## Dos avisos al interpretar

**Un `trf_s3` con menos filas que `stg_s3` puede ser correcto.** Muchas transformaciones agregan,
deduplican o filtran por diseño. La comparación de conteos orienta, no prueba.

**El color del job no vale como evidencia** en ninguna de las dos capas: en STG por «PASO OMITIDO»,
en TRF por la comparación de salida con `"0"`. Ver [R5_07_alerta_vs_estado_real](../R5%20-%20Alertas%20Rundeck/R5_07_alerta_vs_estado_real.md).

## Ver también

[A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md) · [F11_trf_corrio_sin_cambios](../F%20-%20Transformacion%20TRF/F11_trf_corrio_sin_cambios.md) · [D10_tabla_t_vacia](../D%20-%20Carga%20STG/D10_tabla_t_vacia.md) · [I09_indice_tabla_origen](../I%20-%20Referencia%20de%20datos/I09_indice_tabla_origen.md) · [I11_rastrear_un_fichero_e2e](../I%20-%20Referencia%20de%20datos/I11_rastrear_un_fichero_e2e.md)

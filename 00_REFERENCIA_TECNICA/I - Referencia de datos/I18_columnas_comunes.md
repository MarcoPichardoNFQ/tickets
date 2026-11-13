---
titulo: "I18 — Las columnas que aparecen en todas partes"
familia: I
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/I
  - etapa/transversal
  - tipo/referencia
keywords: "cod_load_trace, base_id, cod_sacbbdd, dat_qlikupdate, cod_flag_mapeo, columnas de control"
---

# I18 — Las columnas que aparecen en todas partes

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** cod_load_trace, base_id, cod_sacbbdd, dat_qlikupdate, cod_flag_mapeo, columnas de control

## En una línea

Media docena de columnas se repiten por todo el sistema y son las que se usan para filtrar,
rastrear y limpiar.

## `cod_load_trace` — la unidad de rastreo

Identifica **una ejecución de carga de una tabla**. Nace en `RUN_LOAD_PLAN_PC` desde la secuencia
`stg_s3.SEQ_COD_LOAD_TRACE`.

Aparece en: `aud_load_trace_t`, `aud_load_valid_trace_t`, y como columna en las propias tablas de
staging.

**Es el único criterio seguro de borrado.** Cualquier limpieza se hace por `cod_load_trace`, nunca
por fecha ni por condición de negocio. Ver [R2_07_limpiar_sin_romper](../R2%20-%20Duplicados/R2_07_limpiar_sin_romper.md).

```sql
SELECT count(*) FROM stg_s3.<TABLA>_T WHERE cod_load_trace = :trace;
```

## `id_camda` — la unidad de lote

Agrupa todo lo que llegó en una misma tanda. Sale de
`exp_s3.controlflag_arquivos_cod_id_seq`.

```sql
SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq;
```

No confundir con `cod_load_trace`: un `id_camda` engloba muchas cargas. **No hay columna que los
relacione** — el puente es el nombre del fichero. Ver [B08_id_camda_lote](../B%20-%20Recepcion%20y%20flags/B08_id_camda_lote.md).

## `base_id` — el identificador de base

Filtra qué conjunto de datos se procesa. Aparece en 85 de las 119 funciones de mapeo y en el script
de carga de Qlik, siempre como `base_id = 0`:

```sql
... WHERE tr.base_id = 0 ...
```

**Qlik sólo publica `base_id = 0`.** Un dato con otro valor existe en la base pero no llega a los
tableros. Es una comprobación que conviene tener presente ante «el dato está y no se ve».

También interviene en `bloqueio_insercao_dados`, donde las comprobaciones sólo aplican a `base_id`
1 y 2. Ver [F07_bloqueio_insercao_dados](../F%20-%20Transformacion%20TRF/F07_bloqueio_insercao_dados.md).

## `cod_sacbbdd` — el origen del registro

El script de Qlik lo usa para filtrar al recargar desde el QVD existente:

```sql
LOAD * RESIDENT temp WHERE cod_sacbbdd <> 'MEG';
```

Es decir: **conserva del QVD todo lo que NO sea de Megara**, y luego añade lo nuevo por SQL. El
valor `'MEG'` marca los registros de este sistema.

## `dat_qlikupdate` — la marca de publicación

Fecha de actualización de cara a Qlik. Está en las tablas de salida y en las `_err` de mapeo.

```sql
SELECT max(dat_qlikupdate) FROM trf_s3.<TABLA>;
```

Es la forma más rápida de saber si una tabla se actualizó hoy, mejor que contar filas — porque
muchas transformaciones actualizan sin cambiar el conteo.

## `cod_flag_mapeo` — el filtro de los mapeos

Aparece en **las 119 funciones de mapeo**. Gobierna qué filas entran en cada ejecución.

Si un mapeo procesa cero filas teniendo datos en origen, éste es el primer sospechoso.
Ver [R3_05_mapeo_cero_filas](../R3%20-%20Errores%20de%20mapeo/R3_05_mapeo_cero_filas.md) y [G06_catalogo_mapeos](../G%20-%20Mapeos/G06_catalogo_mapeos.md).

## `ic_qlik_read` — pendiente de leer

Indicador de tres estados: `NULL` recién insertado, `'0'` pendiente de leer por Qlik, otro valor ya
procesado. Lo normalizan las funciones `actualizacao_carga_megara_*`.
Ver [F08_actualizacao_carga_megara](../F%20-%20Transformacion%20TRF/F08_actualizacao_carga_megara.md).

## `COD_SEQ_*` — el número de fila

Columna de secuencia que numera las filas dentro de una carga. La rellena `LOAD_FILES_PC` y es lo
que la traza de validación guarda como `des_row_number`.

Es la forma de localizar una fila concreta señalada por un descarte:

```sql
SELECT c.des_column FROM stg_s3.par_maestro_columnas_t c
JOIN   stg_s3.par_maestro_tablas_t t ON t.cod_table = c.cod_table
WHERE  t.des_table = UPPER('<TABLA>') AND c.des_column LIKE 'COD_SEQ_%';
```

Ver [R1_11_consultas_descartes](../R1%20-%20Descartes/R1_11_consultas_descartes.md).

## `COD_ENT_GEO` — entidad geográfica

Columna de control que rellena `LOAD_FILES_PC`. En la práctica se pasa el valor `2` codificado
directamente en `RUN_LOAD_PLAN_PC`, no desde la columna del plan de carga.
Ver [D05_run_load_plan_pc](../D%20-%20Carga%20STG/D05_run_load_plan_pc.md).

## Resumen de uso

| Necesito… | Columna |
|---|---|
| Rastrear o limpiar una carga | `cod_load_trace` |
| Identificar un lote de ficheros | `id_camda` |
| Saber si una tabla se actualizó hoy | `dat_qlikupdate` |
| Entender por qué Qlik no ve un dato | `base_id`, `cod_sacbbdd` |
| Entender por qué un mapeo no procesa | `cod_flag_mapeo` |
| Localizar la fila de un descarte | `COD_SEQ_*` |

## Ver también

[I01_convencion_nombres](../I%20-%20Referencia%20de%20datos/I01_convencion_nombres.md) · [R2_07_limpiar_sin_romper](../R2%20-%20Duplicados/R2_07_limpiar_sin_romper.md) · [B08_id_camda_lote](../B%20-%20Recepcion%20y%20flags/B08_id_camda_lote.md) · [I07_codigos_cod_dm](../I%20-%20Referencia%20de%20datos/I07_codigos_cod_dm.md) · [H09_qlik_datos_de_ayer](../H%20-%20Cierre%20y%20Qlik/H09_qlik_datos_de_ayer.md)

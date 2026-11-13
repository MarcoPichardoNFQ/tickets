---
titulo: "I02 — Inventario de `stg_s3`"
familia: I
etapa: "Carga STG"
tipo: Referencia
tags:
  - familia/I
  - etapa/carga-stg
  - tipo/referencia
keywords: "stg_s3, inventario, staging, 1322 tablas, sin claves primarias"
---

# I02 — Inventario de `stg_s3`

**Etapa:** Carga STG
**Tipo:** Referencia
**Palabras clave:** stg_s3, inventario, staging, 1322 tablas, sin claves primarias

## En una línea

~1.322 tablas de aterrizaje y control, **sin ninguna clave primaria en las tablas de datos**.

## Las cuatro familias

**Tablas de datos** — cuatro variantes por interfaz:

```
MEG_<INTERFAZ>_T_TMP    aterrizaje del \COPY, se trunca en cada carga
MEG_<INTERFAZ>_T        el dato bueno
MEG_<INTERFAZ>_T_ERR    filas con error de nulos
MEG_<INTERFAZ>_T_DES    filas descartadas por clave foránea
```

Hay **322 tablas `_DES`** y un número similar de `_ERR`.

**Parametrización — `PAR_*`** (6 tablas). Ver [E01_tablas_par_metadata_driven](../E%20-%20Parametrizacion/E01_tablas_par_metadata_driven.md).

**Auditoría — `AUD_*`** (3 tablas). Ver [E06_tablas_auditoria](../E%20-%20Parametrizacion/E06_tablas_auditoria.md).

**Control de flags** — `controlflag_arquivos`, `controlflag_interfaces`.

## ⚠ Sin claves primarias

De las ~1.322 tablas, **sólo 3 tienen restricción de clave primaria**:

```
controlflag_arquivos     (id)
controlflag_interfaces   (id)
nprinting_ondemand       (id)
```

**Ninguna es una tabla de datos.** La base no rechaza una fila repetida en staging.

Consecuencias, todas verificadas:

- **Los duplicados entran sin resistencia.** No hay clave que los pare ni validación activa que los detecte. Ver [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md)
- **261 tablas `_DES` carecen de índice único**, lo que hace fallar el `ON CONFLICT` del apartado de descartes y puede destruir filas. Ver [R2_02_traza_duplicados](../R2%20-%20Duplicados/R2_02_traza_duplicados.md)

La «clave» de cada tabla existe, pero **sólo como declaración** en
`PAR_MAESTRO_COLUMNAS_T.chk_clave`, no como restricción de base de datos.

```sql
-- Restricciones reales de una tabla (esperable: ninguna)
SELECT conname, contype FROM pg_constraint
WHERE  conrelid = 'stg_s3.<TABLA>_T'::regclass;

-- La clave declarada
SELECT string_agg(c.des_column, ', ' ORDER BY c.cod_column)
FROM   stg_s3.par_maestro_columnas_t c
JOIN   stg_s3.par_maestro_tablas_t   t ON t.cod_table = c.cod_table
WHERE  t.des_table = UPPER('<TABLA>') AND c.chk_clave = 1;
```

## Los procedimientos: 20

Carga (`load_files_pc`, `run_load_plan_pc`, `read_header_fn`), validación (`validate_gen_pc` y las
seis funciones `validate_*`), apartado (`fn_load_data_err`, `fn_merge_into_desc`,
`fn_reproceso_descart`), traza (`log_trace`) y limpieza (`cleanup_meg_t`).

**Tres no se invocan desde ningún sitio**: `validate_rows_key_fn`, `validate_variation_fn` y
`megara_reprocess`. Ver [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md) y [R1_07_descarte_variacion_volumen](../R1%20-%20Descartes/R1_07_descarte_variacion_volumen.md).

## Consultas de inventario

```sql
-- Tablas por sufijo
SELECT CASE WHEN table_name LIKE '%\_tmp' THEN 'TMP'
            WHEN table_name LIKE '%\_err' THEN 'ERR'
            WHEN table_name LIKE '%\_des' THEN 'DES'
            WHEN table_name LIKE 'par\_%'  THEN 'PAR'
            WHEN table_name LIKE 'aud\_%'  THEN 'AUD'
            ELSE 'otras' END AS tipo, count(*)
FROM   information_schema.tables WHERE table_schema = 'stg_s3'
GROUP  BY 1 ORDER BY 2 DESC;

-- Las que se vacían en el cierre
SELECT count(*) FROM information_schema.tables
WHERE  table_schema = 'stg_s3' AND table_name LIKE 'meg\_%t';
```

Ver [H02_stg_startover_cleanup](../H%20-%20Cierre%20y%20Qlik/H02_stg_startover_cleanup.md).

## Ver también

[A05_esquemas_base_de_datos](../A%20-%20Orientacion/A05_esquemas_base_de_datos.md) · [I03_inventario_trf_s3](../I%20-%20Referencia%20de%20datos/I03_inventario_trf_s3.md) · [E01_tablas_par_metadata_driven](../E%20-%20Parametrizacion/E01_tablas_par_metadata_driven.md) · [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md) · [I01_convencion_nombres](../I%20-%20Referencia%20de%20datos/I01_convencion_nombres.md)

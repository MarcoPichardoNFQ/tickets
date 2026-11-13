---
titulo: "I03 — Inventario de `trf_s3`"
familia: I
etapa: "Transformación TRF"
tipo: Referencia
tags:
  - familia/I
  - etapa/transformacion-trf
  - tipo/referencia
keywords: "trf_s3, inventario, sss_, sac_, cart_, 638 tablas, dos papeles"
---

# I03 — Inventario de `trf_s3`

**Etapa:** Transformación TRF
**Tipo:** Referencia
**Palabras clave:** trf_s3, inventario, sss_, sac_, cart_, 638 tablas, dos papeles

## En una línea

~638 tablas y 480 procedimientos, cumpliendo **dos papeles a la vez**: modelo de negocio y capa de
salida de los mapeos.

## Los dos papeles

```
trf_s3.sss_*   ← modelo de negocio        (291 tablas)
     ↓ función de mapeo trf_s3.function_meg_*()
trf_s3.sac_*   ← salida hacia SAC          (209)
trf_s3.cart_*  ← salida de cartera         (42)
```

**Origen y destino de los mapeos están en el mismo esquema.** Es la fuente de confusión más común:
`exp_s3` sólo aloja el control. Ver [A05_esquemas_base_de_datos](../A%20-%20Orientacion/A05_esquemas_base_de_datos.md).

## Familias de tabla

| Prefijo | Nº | Papel |
|---|---|---|
| `sss_` | 291 | Modelo de negocio: activos, entidades, divisas, mercados, referencial |
| `sac_` | 209 | **Salida de mapeo** hacia SAC |
| `cart_` | 42 | **Salida de mapeo**: cartera y posiciones |
| `s3_` | 16 | Control de interfaces y de errores de mapeo |
| `meg_` | 12 | Ciclo Megara |
| `master_` | 10 | Maestros |
| `delete_` | 17 | Tablas de borrado |

Más las `<TABLA>_err` de cada destino de mapeo, donde van los duplicados por clave natural.
Ver [R1_08_descartes_en_mapeos](../R1%20-%20Descartes/R1_08_descartes_en_mapeos.md).

## Claves primarias: 185

A diferencia de staging, aquí **sí hay restricciones**: 185 claves primarias sobre ~638 tablas
(~29 %).

Esto tiene una consecuencia directa para el diagnóstico: **es donde afloran los duplicados que
staging dejó pasar**. Un `INSERT` que viola la clave falla aquí, no antes.

```sql
SELECT conname, pg_get_constraintdef(oid)
FROM   pg_constraint
WHERE  conrelid = 'trf_s3.<TABLA>'::regclass AND contype IN ('p','u');
```

Ver [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md) y [F10_localizar_fallo_trf](../F%20-%20Transformacion%20TRF/F10_localizar_fallo_trf.md).

## Los 480 procedimientos

| Tipo | Nº |
|---|---|
| **Funciones de mapeo** `function_meg_*` | 152 (119 declaradas y vivas) |
| Transformación (`cs_`, `fa_`, `ec_`, `cus_`, `ch_`, `load_`…) | 328 |

Ver [F05_familias_procedimientos](../F%20-%20Transformacion%20TRF/F05_familias_procedimientos.md) y [G06_catalogo_mapeos](../G%20-%20Mapeos/G06_catalogo_mapeos.md).

## Tablas de control que viven aquí

| Tabla | Para qué |
|---|---|
| `s3_control_errores_mapeo` | Errores de mapeo |
| `s3_interface_control_t` / `_xml_t` | Publicación por cliente y NAV |
| `tmp_controlflag_interfaces` | Control de recepción con tamaño de fichero |
| `cart_estat_portfoliomaster` | Maestro de carteras, usado por el bloqueo por cliente |
| `s3_carga_megara`, `s3_fundo_extracao_carga` | Marcas `ic_qlik_read` |

Ver [I05_tablas_control_auditoria](../I%20-%20Referencia%20de%20datos/I05_tablas_control_auditoria.md).

## Consultas de inventario

```sql
-- Familias de tabla
SELECT split_part(table_name,'_',1) AS prefijo, count(*)
FROM   information_schema.tables WHERE table_schema = 'trf_s3'
GROUP  BY 1 ORDER BY 2 DESC LIMIT 15;

-- Tablas con clave primaria
SELECT count(*) FROM pg_constraint con
JOIN   pg_class c ON c.oid = con.conrelid
JOIN   pg_namespace n ON n.oid = c.relnamespace
WHERE  n.nspname = 'trf_s3' AND con.contype = 'p';

-- Procedimientos por familia
SELECT split_part(p.proname,'_',1) AS familia, count(*)
FROM   pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'trf_s3' GROUP BY 1 ORDER BY 2 DESC LIMIT 12;
```

## Ver también

[A05_esquemas_base_de_datos](../A%20-%20Orientacion/A05_esquemas_base_de_datos.md) · [I02_inventario_stg_s3](../I%20-%20Referencia%20de%20datos/I02_inventario_stg_s3.md) · [I04_inventario_exp_s3](../I%20-%20Referencia%20de%20datos/I04_inventario_exp_s3.md) · [F05_familias_procedimientos](../F%20-%20Transformacion%20TRF/F05_familias_procedimientos.md) · [G06_catalogo_mapeos](../G%20-%20Mapeos/G06_catalogo_mapeos.md)

---
titulo: "H05 — `actualizar_tablas_y_control` y su variante Flag"
familia: H
etapa: "Cierre y Qlik"
tipo: Referencia
tags:
  - familia/H
  - etapa/cierre-y-qlik
  - tipo/referencia
keywords: "actualizar_tablas_y_control, controlflag, cierre, exp_s3, llamador confirmado"
---

# H05 — `actualizar_tablas_y_control` y su variante Flag

**Etapa:** Cierre y Qlik
**Tipo:** Referencia
**Palabras clave:** actualizar_tablas_y_control, controlflag, cierre, exp_s3, llamador confirmado

## En una línea

Las dos funciones que escriben el registro de cierre — y **dos de las únicas cuatro de `exp_s3` con
llamador confirmado**.

## Las dos

| Función | La invoca | Flujo |
|---|---|---|
| `exp_s3.actualizar_tablas_y_control()` | `Procedimiento control finalizacion mapeos` | General |
| `exp_s3.actualizar_tablas_y_controlflag()` | `Procedimiento control finalizacion mapeos Flag` | Gobernado por flags |

De las 22 funciones de `exp_s3`, sólo cuatro tienen llamador identificado: éstas dos,
`incio_carga_mapeo_megara` y `fim_carga_mapeo_megara_ind`. Ver [G10_codigo_sin_llamadas](../G%20-%20Mapeos/G10_codigo_sin_llamadas.md).

## Qué alimentan

`trf_s3.s3_interface_control_t` y `s3_interface_control_xml_t`, cuya unidad es **cliente + fecha de
NAV**:

```
cod_cli, dat_hr_nav, dat_hr_proc_meg, des_user_meg, dat_hr_proc_aldrin,
cod_error, des_error, cod_process, des_status
```

La versión `_xml_t` añade `des_fnavtype` y es la que consulta el script de Qlik.

Ver [R4_04_s3_interface_control](../R4%20-%20Sets%20incompletos/R4_04_s3_interface_control.md).

## Por qué importan

Su salida —en concreto `des_status`— **decide qué clientes llegan a los tableros**. Si estas
funciones no se ejecutan, no hay registro de cierre, y el filtro del script de Qlik no encuentra
nada que publicar para ese ciclo.

```sql
-- ¿Escribieron hoy?
SELECT count(*) AS filas_hoy, min(dat_hr_proc_aldrin), max(dat_hr_proc_aldrin)
FROM   trf_s3.s3_interface_control_xml_t
WHERE  dat_hr_proc_aldrin::date = CURRENT_DATE;
```

## Cuál de las dos corre

Depende del orquestador que gobierne el ciclo:

| Orquestador | Paso de cierre |
|---|---|
| `0999 Optimizacao Blocos V6` | `Procedimiento control finalizacion mapeos` |
| `JobsArchivosFlag` | `Procedimiento control finalizacion mapeos Flag` |

Ante una incidencia, comprueba **cuál de los dos ciclos estaba en curso**: revisar el log del
equivocado lleva a concluir que el cierre no corrió.

Ver [G07_ciclo_completo_mapeos](../G%20-%20Mapeos/G07_ciclo_completo_mapeos.md) y [G04_jobs_mapeos](../G%20-%20Mapeos/G04_jobs_mapeos.md).

## Se ejecutan en paralelo con el resto del cierre

No al final. El grafo del orquestador lanza a la vez el control de errores de mapeo, el análisis de
errores, este procedimiento, la recarga de Qlik y la validación de descartes.

**La recarga de Qlik no espera a esta función.** Ver [H01_cerrar_el_lote](../H%20-%20Cierre%20y%20Qlik/H01_cerrar_el_lote.md).

## Nota de cobertura

El cuerpo de estas funciones está en el volcado de `exp_s3`, pero su lógica interna no se ha
detallado en esta base. Para consultarla:

```sql
SELECT prosrc FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'exp_s3' AND p.proname LIKE 'actualizar_tablas%';
```

Lo documentado procede de los jobs que las invocan y de la estructura real de las tablas que
alimentan.

## Ver también

[H04_procedimiento_finalizacion](../H%20-%20Cierre%20y%20Qlik/H04_procedimiento_finalizacion.md) · [R4_04_s3_interface_control](../R4%20-%20Sets%20incompletos/R4_04_s3_interface_control.md) · [H01_cerrar_el_lote](../H%20-%20Cierre%20y%20Qlik/H01_cerrar_el_lote.md) · [G10_codigo_sin_llamadas](../G%20-%20Mapeos/G10_codigo_sin_llamadas.md) · [H10_cierre_no_completado](../H%20-%20Cierre%20y%20Qlik/H10_cierre_no_completado.md)

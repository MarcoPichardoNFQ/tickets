---
titulo: "H01 — Qué significa cerrar el lote"
familia: H
etapa: "Cierre y Qlik"
tipo: Referencia
tags:
  - familia/H
  - etapa/cierre-y-qlik
  - tipo/referencia
keywords: "cierre, finalización, cinco pasos, paralelo, fin de ciclo"
---

# H01 — Qué significa cerrar el lote

**Etapa:** Cierre y Qlik
**Tipo:** Referencia
**Palabras clave:** cierre, finalización, cinco pasos, paralelo, fin de ciclo

## En una línea

Cinco comprobaciones y acciones que se lanzan **todas a la vez** cuando terminan los mapeos.

## Los cinco pasos del cierre

Según el grafo de dependencias del orquestador, al acabar los mapeos se disparan en paralelo:

| Paso | Qué hace | Ficha |
|---|---|---|
| `Job control errores mapeo` | ¿Hubo errores de mapeo en los últimos 30 min? | [G09_job_control_errores](../G%20-%20Mapeos/G09_job_control_errores.md) |
| `_00001 Análise de erros` | ⚠ Anulado con `WHERE 1=0` | [R5_08_analise_de_erros_anulado](../R5%20-%20Alertas%20Rundeck/R5_08_analise_de_erros_anulado.md) |
| `Procedimiento control finalizacion mapeos` | Registra el cierre por cliente | [H04_procedimiento_finalizacion](../H%20-%20Cierre%20y%20Qlik/H04_procedimiento_finalizacion.md) |
| `Recarga Qlik` | Lanza la tarea de recarga | [H08_recarga_qlik](../H%20-%20Cierre%20y%20Qlik/H08_recarga_qlik.md) |
| `Validacion Descartes` | Barre las tablas `_err` de mapeo | [H03_validacion_descartes](../H%20-%20Cierre%20y%20Qlik/H03_validacion_descartes.md) |

Y **después de todos ellos**, `STG StartOver`, que limpia staging. Ver [H02_stg_startover_cleanup](../H%20-%20Cierre%20y%20Qlik/H02_stg_startover_cleanup.md).

## ⚠ Que sean paralelos importa

**La recarga de Qlik no espera al procedimiento de finalización.** Puede estar recargando mientras
el control de cierre sigue ejecutándose.

Si buscas una relación de causa-efecto entre ambos —«¿se recargó porque cerró bien?»— no la hay:
son hermanos, no padre e hijo. Ver [G07_ciclo_completo_mapeos](../G%20-%20Mapeos/G07_ciclo_completo_mapeos.md).

## Qué queda registrado

| Dónde | Qué |
|---|---|
| `trf_s3.s3_interface_control_t` / `_xml_t` | Estado de publicación por cliente y NAV |
| `trf_s3.s3_control_errores_mapeo` | Errores de mapeo del ciclo |
| `stg_s3.aud_log_trace_t` | Mensajes de los procedimientos |
| Tablas `MEG_*` de staging | **Vaciadas** por la limpieza |

## Cómo comprobar que el ciclo cerró

```sql
-- ¿Se registró el cierre hoy?
SELECT cod_cli, dat_hr_nav, dat_hr_proc_aldrin, des_status, cod_error
FROM   trf_s3.s3_interface_control_xml_t
WHERE  dat_hr_proc_aldrin::date = CURRENT_DATE
ORDER  BY dat_hr_proc_aldrin DESC LIMIT 20;
```

```sql
-- ¿Se limpió staging? (no debería devolver nada)
DO $$
DECLARE r record; n bigint;
BEGIN
  FOR r IN SELECT table_name FROM information_schema.tables
           WHERE table_schema='stg_s3' AND table_name LIKE 'meg\_%t'
  LOOP
    EXECUTE format('SELECT count(*) FROM stg_s3.%I', r.table_name) INTO n;
    IF n > 0 THEN RAISE NOTICE '% -> % filas', r.table_name, n; END IF;
  END LOOP;
END $$;
```

## Los dos pasos que no sirven como evidencia

**`_00001 Análise de erros`** tiene su consulta anulada: no puede detectar nada. Su silencio no
prueba que el ciclo fuera limpio.

**`Validacion Descartes`** sólo emite mensajes de `RAISE NOTICE`. No falla, no devuelve nada que se
compruebe y no genera alerta. Es informativo.

Así que de los cinco pasos del cierre, **sólo dos producen una señal accionable**: el control de
errores de mapeo y el procedimiento de finalización. Los otros tres son informativos o inertes.

Es la razón por la que el checklist diario existe. Ver [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md).

## Ver también

[G07_ciclo_completo_mapeos](../G%20-%20Mapeos/G07_ciclo_completo_mapeos.md) · [H10_cierre_no_completado](../H%20-%20Cierre%20y%20Qlik/H10_cierre_no_completado.md) · [H02_stg_startover_cleanup](../H%20-%20Cierre%20y%20Qlik/H02_stg_startover_cleanup.md) · [H04_procedimiento_finalizacion](../H%20-%20Cierre%20y%20Qlik/H04_procedimiento_finalizacion.md) · [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md)

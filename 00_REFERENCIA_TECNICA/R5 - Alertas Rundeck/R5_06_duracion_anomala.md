---
titulo: "R5.06 — La alerta por duración anómala"
familia: R5
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/R5
  - etapa/transversal
  - tipo/referencia
keywords: "onavgduration, duración, lento, umbral, notifyAvgDurationThreshold"
---

# R5.06 — La alerta por duración anómala

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** onavgduration, duración, lento, umbral, notifyAvgDurationThreshold

## En una línea

Rundeck puede avisar cuando un job tarda más de lo habitual, pero **sólo un job de los 46 lo tiene
configurado**.

## Cómo funciona

```xml
<notification>
  <onavgduration>
    <email recipients='...' />
  </onavgduration>
</notification>
<notifyAvgDurationThreshold>...</notifyAvgDurationThreshold>
```

Rundeck calcula la duración media de las últimas ejecuciones y avisa cuando una las supera según el
umbral configurado.

**Es el único mecanismo de detección de lentitud del sistema.** No hay nada equivalente en base de
datos.

## La cobertura real

| Disparador | Jobs que lo usan |
|---|---|
| `onfailure` | 22 |
| `onstart` | 2 |
| `onsuccess` | 1 |
| **`onavgduration`** | **1** |

Un solo job vigila su duración. Los otros 45 pueden tardar cinco veces lo normal sin que nadie lo
sepa hasta que alguien lo mire.

## Por qué importa aquí más que en otros sistemas

Los procesos de este sistema tienen duraciones muy dispares y varias fuentes de lentitud
documentadas:

- **El acondicionamiento de `_TMP`**: dos `UPDATE` por columna sobre la tabla completa → [D06_load_files_pc](../D%20-%20Carga%20STG/D06_load_files_pc.md)
- **La validación de claves foráneas**: `count(*)` y `EXCEPT` por cada relación → [E05_par_maestro_valid_t](../E%20-%20Parametrizacion/E05_par_maestro_valid_t.md)
- **Los reintentos contra la API de Megara**: hasta 2,5 h por endpoint → [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md)
- **Los mapeos grandes**: `cart_pos_rf_t` tiene 796 líneas y 26 joins → [G06_catalogo_mapeos](../G%20-%20Mapeos/G06_catalogo_mapeos.md)

Un job de reintentos que lleva horas **no está colgado**: está esperando. Sin alerta de duración, la
única forma de distinguirlo es mirar.

## Cómo compensarlo

Rundeck guarda el histórico de duraciones por job. Comparar la ejecución de hoy con las de días
anteriores del mismo job es la comprobación manual equivalente.

En base de datos lo más aproximado es el reparto horario de las trazas:

```sql
SELECT cod_load_plan,
       min(dat_load_date) AS inicio,
       max(dat_load_date) AS fin,
       max(dat_load_date) - min(dat_load_date) AS duracion
FROM   stg_s3.aud_load_trace_t
WHERE  dat_load_date::date = CURRENT_DATE
GROUP  BY 1
ORDER  BY 4 DESC NULLS LAST
LIMIT  15;
```

No es la duración del job, sino la ventana entre su primera y su última traza — pero sirve para
detectar los planes que se han disparado.

## Antes de dar por lento un proceso

Comprueba si está **bloqueado** en vez de trabajando:

```sql
SELECT pid, state, now() - query_start AS duracion, wait_event_type, left(query,100)
FROM   pg_stat_activity WHERE state <> 'idle' ORDER BY query_start;
```

`wait_event_type = 'Lock'` es bloqueo, no lentitud. Ver [R3_06_mapeo_bloqueado](../R3%20-%20Errores%20de%20mapeo/R3_06_mapeo_bloqueado.md) y
[D12_carga_colgada](../D%20-%20Carga%20STG/D12_carga_colgada.md).

## Material de escalado

Extender `onavgduration` a los orquestadores principales —`Main Job Megara`, los bloques y
`Mapeos`— daría cobertura sobre un modo de fallo que hoy no tiene ninguna. Es configuración, no
código.

## Ver también

[R5_01_como_notifica_rundeck](../R5%20-%20Alertas%20Rundeck/R5_01_como_notifica_rundeck.md) · [F13_bloque_lento](../F%20-%20Transformacion%20TRF/F13_bloque_lento.md) · [D12_carga_colgada](../D%20-%20Carga%20STG/D12_carga_colgada.md) · [R5_02_jobs_sin_notificacion](../R5%20-%20Alertas%20Rundeck/R5_02_jobs_sin_notificacion.md) · [I15_volumetria_tipica](../I%20-%20Referencia%20de%20datos/I15_volumetria_tipica.md)

---
titulo: "R3.01 — Anatomía de un fallo de mapeo"
familia: R3
etapa: "Mapeos"
tipo: Runbook
tags:
  - familia/R3
  - etapa/mapeos
  - tipo/runbook
keywords: "fallo de mapeo, diagnóstico, s3_control_errores_mapeo, orden de comprobación"
---

# R3.01 — Anatomía de un fallo de mapeo

**Etapa:** Mapeos
**Tipo:** Runbook
**Palabras clave:** fallo de mapeo, diagnóstico, s3_control_errores_mapeo, orden de comprobación

## En una línea

Cinco comprobaciones en orden resuelven casi cualquier incidencia de mapeo, y la primera no es
mirar el error sino comprobar si el mapeo estaba encendido.

## El orden de comprobación

### 1. ¿Está activo?

```sql
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio,
       activo_inactivo, is_fromtis, retry_deadlock, wait_deadlock_seconds
FROM   exp_s3.tablas_mapeio_t
WHERE  nome_tabela_aldrin ILIKE '%<TABLA>%';
```

`activo_inactivo = false` → no es una incidencia técnica. Ver [R3_07_mapeo_desactivado](../R3%20-%20Errores%20de%20mapeo/R3_07_mapeo_desactivado.md).

Si el `id_mapeo` tiene **varias funciones**, comprueba el estado de todas: una tabla puede
construirse en dos fases y tener la segunda apagada.

### 2. ¿Hay error registrado?

```sql
SELECT * FROM trf_s3.s3_control_errores_mapeo
WHERE  dat_proc_exe::date = CURRENT_DATE
ORDER  BY dat_proc_exe DESC;
```

Ésta es la tabla de errores de la capa. Ver [G09_job_control_errores](../G%20-%20Mapeos/G09_job_control_errores.md).

### 3. ¿Se ejecutó el job?

En Rundeck, grupo `001 - JOBs Mapeos`, job `<id> mapeo_<tabla>`. El histórico da hora, duración y
resultado. Ver [G04_jobs_mapeos](../G%20-%20Mapeos/G04_jobs_mapeos.md).

Si el job no aparece en el histórico de hoy, el problema es de despacho, no del mapeo.
Ver [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md).

### 4. ¿Hay datos en origen?

Un mapeo sin datos de entrada produce cero filas y no falla:

```sql
SELECT count(*) FROM trf_s3.<TABLA_ORIGEN>;
SELECT count(*) FROM trf_s3.<TABLA_DESTINO>;
```

Ver [R3_05_mapeo_cero_filas](../R3%20-%20Errores%20de%20mapeo/R3_05_mapeo_cero_filas.md).

### 5. ¿Es la lógica del mapeo?

Si hay datos en origen, el mapeo corrió y no hay error, entonces las filas se quedaron fuera por un
`JOIN`, un `WHERE` o un `ON CONFLICT`. Ver [R3_10_corrio_pero_no_llego](../R3%20-%20Errores%20de%20mapeo/R3_10_corrio_pero_no_llego.md).

## Los cinco desenlaces

| Comprobación que falla | Naturaleza | Ficha |
|---|---|---|
| 1. No está activo | Decisión funcional | [R3_07_mapeo_desactivado](../R3%20-%20Errores%20de%20mapeo/R3_07_mapeo_desactivado.md) |
| 2. Hay error registrado | Fallo técnico | [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md) o [R3_06_mapeo_bloqueado](../R3%20-%20Errores%20de%20mapeo/R3_06_mapeo_bloqueado.md) |
| 3. No se ejecutó | Problema de despacho | [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md) |
| 4. Sin datos en origen | Problema aguas arriba | [R3_08_dependencia_insatisfecha](../R3%20-%20Errores%20de%20mapeo/R3_08_dependencia_insatisfecha.md) |
| 5. Todo bien y aun así falta | Lógica del mapeo | [R3_10_corrio_pero_no_llego](../R3%20-%20Errores%20de%20mapeo/R3_10_corrio_pero_no_llego.md) |

La utilidad del orden está en que **las tres primeras comprobaciones son de segundos** y descartan
la mayoría de los casos sin necesidad de leer una línea de SQL.

## Lo que distingue esta capa

**No hay tablas `_DES` ni `_ERR`.** El mecanismo de descartes de staging no existe aquí. Buscar
descartes de mapeo en `AUD_LOAD_VALID_TRACE_T` es perder el tiempo.
Ver [R1_08_descartes_en_mapeos](../R1%20-%20Descartes/R1_08_descartes_en_mapeos.md).

**No hay parametrización genérica.** Cada mapeo es SQL a medida: no hay `PAR_*` que consultar para
saber qué hace. Para la comprobación 5 hay que leer la función:

```sql
SELECT prosrc FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'exp_s3' AND p.proname = '<nome_fn_mapeio>';
```

**El paralelismo es normal.** Decenas de mapeos a la vez. Un deadlock aislado que el reintento
resuelve no es una incidencia. Ver [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md).

## Qué llevar al escalado

- `id_mapeo`, `nome_tabela_aldrin` y `nome_fn_mapeio`
- Estado de `activo_inactivo` y de `is_fromtis`
- Filas de `s3_control_errores_mapeo` del día
- Conteos de origen y destino
- Hora y duración de la ejecución en Rundeck

## Ver también

[R3_12_consultas_mapeos](../R3%20-%20Errores%20de%20mapeo/R3_12_consultas_mapeos.md) · [G01_que_es_un_mapeo](../G%20-%20Mapeos/G01_que_es_un_mapeo.md) · [G09_job_control_errores](../G%20-%20Mapeos/G09_job_control_errores.md) · [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md) · [G05_anatomia_job_mapeo](../G%20-%20Mapeos/G05_anatomia_job_mapeo.md)

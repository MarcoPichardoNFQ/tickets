---
titulo: "I13 — Cómo leer `aud_log_trace_t`"
familia: I
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/I
  - etapa/transversal
  - tipo/referencia
keywords: "aud_log_trace_t, traza, log, des_log, nivel, ADT, zona horaria"
---

# I13 — Cómo leer `aud_log_trace_t`

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** aud_log_trace_t, traza, log, des_log, nivel, ADT, zona horaria

## En una línea

La traza técnica de todos los procedimientos — con cuatro limitaciones que hay que conocer antes de
sacar conclusiones de ella.

## Estructura

```
stg_s3.aud_log_trace_t
  dat_load_date   timestamp
  cod_load_plan   integer
  step_load       integer      ← NÚMERO, no texto
  cod_status      integer      ← 0 correcto, -1 error
  des_log         varchar(4000)
  xti_wfile       integer
```

## La consulta base

```sql
SELECT dat_load_date, cod_load_plan, step_load, cod_status, des_log
FROM   stg_s3.aud_log_trace_t
WHERE  cod_load_plan = :plan AND dat_load_date >= CURRENT_DATE
ORDER  BY dat_load_date DESC
LIMIT  100;
```

Y la de errores, que es la que más se usa:

```sql
SELECT dat_load_date, cod_load_plan, step_load, des_log
FROM   stg_s3.aud_log_trace_t
WHERE  cod_status = -1 AND dat_load_date >= CURRENT_DATE
ORDER  BY dat_load_date DESC;
```

## Las cuatro limitaciones

### 1. No tiene `cod_load_trace`

Sólo `cod_load_plan`. **No se puede atar un mensaje a una ejecución concreta.** Si el mismo plan
corrió dos veces hoy, los mensajes se mezclan y hay que separarlos por hora.

Es la diferencia clave con `aud_load_trace_t`, que sí lo tiene. Ver [E06_tablas_auditoria](../E%20-%20Parametrizacion/E06_tablas_auditoria.md).

### 2. `step_load` significa otra cosa aquí

En esta tabla es un **entero**; en `aud_load_trace_t` es un **texto** descriptivo
(`'CARGA FICHERO'`). Mismo nombre, tipos distintos. No los cruces.

### 3. El nivel de log filtra mensajes

`LOG_TRACE` sólo escribe si `PAR_MAESTRO_LOG_LEVEL_T.cod_log_level <= nivel_del_mensaje`, con
`ALTO = 1`, `MEDIO = 2`, `BAJO = 3`.

**Un valor configurado alto produce menos traza.** Es contraintuitivo y hace que un log escueto
pueda ser configuración, no ausencia de actividad.

```sql
SELECT * FROM stg_s3.par_maestro_log_level_t;   -- debe tener exactamente 1 fila
```

Ver [E08_log_trace_niveles](../E%20-%20Parametrizacion/E08_log_trace_niveles.md).

### 4. Las horas conviven en dos zonas

El camino normal graba con `now() AT TIME ZONE 'ADT'` (UTC-3). El manejador de excepciones usa
`now()` a secas, que sigue la zona de la sesión.

**Los mensajes de error pueden aparecer desplazados respecto a los normales dentro de la misma
tabla.** Antes de correlacionar con Rundeck o con horas de llegada de ficheros:

```sql
SHOW timezone;
```

Ver [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md).

## Los mensajes que merece la pena buscar

| Patrón | Qué indica |
|---|---|
| `Excepción no controlada … Error: <causa>` | **Contiene el error real de PostgreSQL** al final. Léelo entero |
| `Truncado de la tabla` | Se ejecutó un `TRUNCATE` por fallo de clave foránea en flujo estricto |
| `MERGE_INTO_DESC` | Fallo al apartar descartes: posible pérdida de filas. Ver [R2_02_traza_duplicados](../R2%20-%20Duplicados/R2_02_traza_duplicados.md) |
| `VALIDATE_GEN_PC: Validacion de …` | Recorrido de las validaciones |
| `Se agotaron los intentos` | Un mapeo agotó sus reintentos por deadlock |

```sql
-- La causa real de los errores de hoy
SELECT dat_load_date, cod_load_plan, des_log
FROM   stg_s3.aud_log_trace_t
WHERE  des_log ILIKE '%Excepción no controlada%'
  AND  dat_load_date >= CURRENT_DATE - 1
ORDER  BY dat_load_date DESC;
```

## Volumen

La tabla crece con cada ejecución y no tiene purga documentada. Filtra **siempre** por fecha: sin
`WHERE dat_load_date`, una consulta recorre el histórico completo.

## Ver también

[E06_tablas_auditoria](../E%20-%20Parametrizacion/E06_tablas_auditoria.md) · [E08_log_trace_niveles](../E%20-%20Parametrizacion/E08_log_trace_niveles.md) · [F10_localizar_fallo_trf](../F%20-%20Transformacion%20TRF/F10_localizar_fallo_trf.md) · [I12_consultas_frecuentes](../I%20-%20Referencia%20de%20datos/I12_consultas_frecuentes.md) · [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md)

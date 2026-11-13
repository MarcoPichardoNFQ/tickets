---
titulo: "D10 — La tabla `_T` quedó vacía"
familia: D
etapa: "Carga STG"
tipo: Runbook
tags:
  - familia/D
  - etapa/carga-stg
  - tipo/runbook
keywords: "tabla vacía, sin datos, truncate, no cargó, cero filas"
---

# D10 — La tabla `_T` quedó vacía

**Etapa:** Carga STG
**Tipo:** Runbook
**Palabras clave:** tabla vacía, sin datos, truncate, no cargó, cero filas

## Síntoma

Una tabla `_T` que normalmente tiene datos aparece vacía o con muchas menos filas de lo habitual.

## Qué mirar primero

La respuesta está en repartir las filas entre las cuatro tablas de la interfaz:

```sql
SELECT 'TMP' AS tabla, count(*) FROM stg_s3.<TABLA>_TMP
UNION ALL SELECT 'T',   count(*) FROM stg_s3.<TABLA>_T
UNION ALL SELECT 'ERR', count(*) FROM stg_s3.<TABLA>_ERR
UNION ALL SELECT 'DES', count(*) FROM stg_s3.<TABLA>_DES;
```

| Resultado | Diagnóstico |
|---|---|
| Todo a cero | El fichero no llegó o el `\COPY` falló → punto 1 |
| `TMP` con datos, `T` vacía | La validación abortó → punto 2 |
| `DES` con datos, `T` vacía | Descarte masivo o truncado por clave foránea → punto 3 |
| `ERR` con datos, `T` con menos | Comportamiento normal: se apartaron filas → [R1_04_descarte_nulo_obligatorio](../R1%20-%20Descartes/R1_04_descarte_nulo_obligatorio.md) |

## 1. No llegó nada

```sql
SELECT cod_load_trace, dat_load_date, step_load, cod_status,
       des_file_loaded, amt_register_process, des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_plan = :plan
ORDER  BY dat_load_date DESC LIMIT 5;
```

Si no hay traza de hoy, la carga ni se intentó: el fichero no estaba. Eso es un problema de
recepción, no de carga → [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md) y familia `R4`.

Si hay traza con `cod_status = -1` y `step_load = 'CARGA FICHERO'`, el `\COPY` falló →
[D09_error_numero_columnas](../D%20-%20Carga%20STG/D09_error_numero_columnas.md).

## 2. Hay datos en `_TMP` pero no en `_T`

La validación se ejecutó y abortó. Comprueba el modo de la carga:

```sql
SELECT cod_load_plan, valid_err_des FROM stg_s3.par_load_plan_t WHERE cod_load_plan = :plan;
```

Con `valid_err_des ≠ 1` (flujo estricto), cualquier fallo de nulos o formato aborta y las filas se
quedan en `_TMP` sin pasar a `_T`. Mira qué falló:

```sql
SELECT des_validate, des_column_name, count(*)
FROM   stg_s3.aud_load_valid_trace_t
WHERE  cod_load_trace = :trace
GROUP  BY 1,2 ORDER BY 3 DESC;
```

Ver [R1_01_descarte_vs_error](../R1%20-%20Descartes/R1_01_descarte_vs_error.md).

## 3. La tabla se truncó

El caso más brusco. En flujo estricto, un fallo de clave foránea ejecuta:

```sql
truncate table stg_s3.<TABLA>
```

No quedan filas ni en `_T` ni apartadas: se vacía todo. La traza en `AUD_LOG_TRACE_T` lo dice:

```sql
SELECT dat_load_date, des_log
FROM   stg_s3.aud_log_trace_t
WHERE  des_log LIKE '%Truncado de la tabla%'
  AND  dat_load_date >= CURRENT_DATE - 1
ORDER  BY dat_load_date DESC;
```

Recuperación: hay que **recargar el fichero** una vez resuelta la causa del fallo de FK. Reprocesar
descartes no sirve, porque no hay descartes. Ver [R1_06_descarte_integridad_referencial](../R1%20-%20Descartes/R1_06_descarte_integridad_referencial.md).

## 4. Caso especial: la limpieza del cierre

`stg_s3.cleanup_meg_t()` borra el contenido de **todas** las tablas de `stg_s3` cuyo nombre
encaje con `meg_%t`. Se ejecuta en el cierre del lote. Si consultas una tabla `MEG_*` después del
cierre, está vacía **por diseño**, no por fallo.

```sql
-- ¿Tu tabla entra en el barrido de limpieza?
SELECT table_name FROM information_schema.tables
WHERE  table_schema = 'stg_s3' AND table_name LIKE 'meg\_%t'
  AND  table_name = lower('<TABLA>');
```

Si devuelve una fila, no es una incidencia: es el ciclo. Ver [H02_stg_startover_cleanup](../H%20-%20Cierre%20y%20Qlik/H02_stg_startover_cleanup.md).

## Cuándo escalar

- Si hubo truncado: hay que coordinar una recarga.
- Si el fichero no llegó y el flag sí: es un set incompleto, familia `R4`.
- Si la validación aborta por un cambio de contrato en origen.

## Ver también

[D09_error_numero_columnas](../D%20-%20Carga%20STG/D09_error_numero_columnas.md) · [R1_01_descarte_vs_error](../R1%20-%20Descartes/R1_01_descarte_vs_error.md) · [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md) · [H02_stg_startover_cleanup](../H%20-%20Cierre%20y%20Qlik/H02_stg_startover_cleanup.md) · [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md)

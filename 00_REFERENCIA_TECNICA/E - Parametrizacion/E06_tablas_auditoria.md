---
titulo: "E06 — Las tablas de auditoría: `AUD_LOAD_TRACE_T`, `AUD_LOAD_VALID_TRACE_T`, `AUD_LOG_TRACE_T`"
familia: E
etapa: "Validación"
tipo: Referencia
tags:
  - familia/E
  - etapa/validacion
  - tipo/referencia
keywords: "auditoría, aud_load_trace_t, aud_log_trace_t, aud_load_valid_trace_t, traza, step_load"
---

# E06 — Las tablas de auditoría: `AUD_LOAD_TRACE_T`, `AUD_LOAD_VALID_TRACE_T`, `AUD_LOG_TRACE_T`

**Etapa:** Validación
**Tipo:** Referencia
**Palabras clave:** auditoría, aud_load_trace_t, aud_log_trace_t, aud_load_valid_trace_t, traza, step_load

## En una línea

Tres tablas con nombres parecidos y propósitos distintos: una por **carga**, otra por **fila
rechazada** y otra por **mensaje de log**.

## Las tres, y cuándo usar cada una

### `AUD_LOAD_TRACE_T` — una fila por carga

La tabla de cabecera. Responde «¿qué pasó con esta carga?».

| Columna | Contenido |
|---|---|
| `cod_load_trace` | Identificador de la ejecución. **La llave de todo el rastreo** |
| `cod_load_plan` | Plan de carga |
| `dat_load_date` | Momento |
| `step_load` | **Texto** con la etapa: `CARGA FICHERO`, `Validacion Nulos`, `LECTURA CABECERA`… |
| `des_file_loaded` | Fichero procesado |
| `des_file_loaded_destiny` | Destino |
| `cod_status` | `0` correcto, `-1` error |
| `amt_register_process` | **Filas cargadas.** El conteo bueno para control de volumen |
| `amt_register_notprocess` | Filas no procesadas |
| `des_process_executed` | Narración del recorrido, con tramos separados por `\|` |

`des_process_executed` es la columna más útil de las tres tablas. Se va concatenando a medida que
avanza la validación:

```
Fichero cargado correctamente en la tabla TMP|Errores en validación de nulos se inserta en tabla err
```

Léela como un relato: te dice hasta dónde llegó el proceso y qué apartó por el camino.

### `AUD_LOAD_VALID_TRACE_T` — una fila por dato rechazado

El detalle del diagnóstico. Responde «¿qué falló exactamente y en qué fila?».

| Columna | Contenido |
|---|---|
| `cod_load_trace` | Carga afectada |
| `cod_load_plan` | Plan |
| `dat_load_date` | Momento |
| `des_table_name` | Tabla, normalmente con sufijo `_TMP` |
| `des_column_name` | **Columna que falló** |
| `des_validate` | **Regla incumplida** |
| `des_row_number` | Número de secuencia de la fila (`COD_SEQ_*`) |

Detalle completo de los valores de `des_validate` en [R1_03_identificar_validacion](../R1%20-%20Descartes/R1_03_identificar_validacion.md).

### `AUD_LOG_TRACE_T` — una fila por mensaje

La traza técnica que escriben los procedimientos vía `LOG_TRACE()`.

| Columna | Contenido |
|---|---|
| `dat_load_date` | Momento |
| `cod_load_plan` | Plan |
| `step_load` | **Número** de etapa (1, 2, 3…) |
| `cod_status` | `0` correcto, `-1` error |
| `des_log` | Mensaje |
| `xti_wfile` | Indicador auxiliar |

## Cuatro trampas al leerlas

**1. `step_load` significa cosas distintas.** En `AUD_LOAD_TRACE_T` es un **texto** descriptivo
(`'CARGA FICHERO'`). En `AUD_LOG_TRACE_T` es un **entero**. Mismo nombre, tipos y semánticas
distintos. No los cruces.

**2. `AUD_LOG_TRACE_T` no tiene `cod_load_trace`.** Sólo `cod_load_plan`. No puedes atar un mensaje
de log a una ejecución concreta: si el mismo plan corrió dos veces hoy, los mensajes se mezclan y
hay que separarlos por hora.

**3. Las horas conviven en dos zonas.** `LOG_TRACE()` graba con `now() AT TIME ZONE 'ADT'`, pero su
ruta de excepción usa `now()` a secas, que sigue la zona de la sesión. En la misma tabla puede
haber marcas con desfase. Comprueba `SHOW timezone;` antes de correlacionar con otros sistemas.
Ver [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md).

**4. No todos los mensajes llegan.** `LOG_TRACE()` filtra por nivel:
`PAR_MAESTRO_LOG_LEVEL_T.cod_log_level <= nivel_del_mensaje`. Con el nivel configurado alto, los
mensajes de detalle no se escriben. Un log escueto puede ser configuración, no ausencia de
actividad. Ver [E08_log_trace_niveles](../E%20-%20Parametrizacion/E08_log_trace_niveles.md).

## Consultas de arranque

```sql
-- Cabecera: qué pasó hoy
SELECT cod_load_trace, cod_load_plan, dat_load_date, step_load, cod_status,
       amt_register_process, des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  dat_load_date::date = CURRENT_DATE
ORDER  BY dat_load_date DESC;

-- Detalle: qué se rechazó en una carga
SELECT des_table_name, des_column_name, des_validate, des_row_number
FROM   stg_s3.aud_load_valid_trace_t
WHERE  cod_load_trace = :trace
ORDER  BY des_row_number;

-- Log técnico de un plan
SELECT dat_load_date, step_load, cod_status, des_log
FROM   stg_s3.aud_log_trace_t
WHERE  cod_load_plan = :plan AND dat_load_date >= CURRENT_DATE
ORDER  BY dat_load_date DESC LIMIT 100;
```

## Ver también

[R1_11_consultas_descartes](../R1%20-%20Descartes/R1_11_consultas_descartes.md) · [E08_log_trace_niveles](../E%20-%20Parametrizacion/E08_log_trace_niveles.md) · [D05_run_load_plan_pc](../D%20-%20Carga%20STG/D05_run_load_plan_pc.md) · [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md)

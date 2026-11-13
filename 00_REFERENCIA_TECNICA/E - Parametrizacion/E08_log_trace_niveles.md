---
titulo: "E08 — `LOG_TRACE()` y los niveles de log"
familia: E
etapa: "Validación"
tipo: Referencia
tags:
  - familia/E
  - etapa/validacion
  - tipo/referencia
keywords: "log_trace, nivel de log, par_maestro_log_level_t, ALTO, MEDIO, BAJO, ADT, verbosidad"
---

# E08 — `LOG_TRACE()` y los niveles de log

**Etapa:** Validación
**Tipo:** Referencia
**Palabras clave:** log_trace, nivel de log, par_maestro_log_level_t, ALTO, MEDIO, BAJO, ADT, verbosidad

## En una línea

Todos los procedimientos escriben su traza con la misma función, y un único valor de configuración
decide cuánto de eso llega realmente a la tabla.

## Firma

```sql
stg_s3.log_trace(
    pi_log_level    numeric,   -- 1 ALTO, 2 MEDIO, 3 BAJO
    pi_cod_load_plan numeric,
    pi_step_load    numeric,
    pi_cod_status   numeric,   -- 0 correcto, -1 error
    pi_des_process  varchar    -- el mensaje
) RETURNS numeric
```

Escribe en `stg_s3.AUD_LOG_TRACE_T`.

## ⚠ El filtro es contraintuitivo

```sql
SELECT COD_LOG_LEVEL INTO v_log_level FROM stg_s3.PAR_MAESTRO_LOG_LEVEL_T;
IF v_log_level <= PI_LOG_LEVEL THEN
    -- se escribe el mensaje
END IF;
```

Las constantes son `ALTO = 1`, `MEDIO = 2`, `BAJO = 3`. Es decir, **«ALTO» es el número más bajo**.
Y como la condición es `configurado <= nivel_del_mensaje`:

| `cod_log_level` configurado | Qué se escribe |
|---|---|
| `1` | Todo: los mensajes de nivel 1, 2 y 3 |
| `2` | Sólo los de nivel 2 y 3 |
| `3` | Sólo los de nivel 3 |

Así que **subir el número configurado reduce la traza**. Si alguien «sube el nivel de log» pensando
en ver más detalle, consigue lo contrario.

```sql
SELECT * FROM stg_s3.par_maestro_log_level_t;
```

Consecuencia para diagnóstico: **un log escueto puede ser configuración, no ausencia de
actividad**. Antes de concluir que un procedimiento no se ejecutó, comprueba el nivel.

## La consulta de configuración no filtra

```sql
SELECT COD_LOG_LEVEL INTO v_log_level FROM stg_s3.PAR_MAESTRO_LOG_LEVEL_T;
```

Sin `WHERE` y sin `ORDER BY`. Si la tabla llegara a tener más de una fila, PostgreSQL toma una
cualquiera y el nivel efectivo se vuelve impredecible entre ejecuciones. Debe haber exactamente una:

```sql
SELECT count(*) FROM stg_s3.par_maestro_log_level_t;   -- tiene que ser 1
```

## La zona horaria

El camino normal graba así:

```sql
VALUES (now() AT TIME ZONE 'ADT', ...)
```

`ADT` es UTC-3. Pero el manejador de excepciones de la propia función graba con `now()` a secas,
que depende de la zona de la sesión de base de datos. Si esa zona no es UTC-3, **los mensajes de
error aparecen desplazados respecto a los normales dentro de la misma tabla**.

```sql
SHOW timezone;
```

Antes de correlacionar horas de `AUD_LOG_TRACE_T` con logs de Rundeck o con horas de llegada de
ficheros, confirma este punto. Es una fuente habitual de diagnósticos equivocados.

## Si la propia traza falla

La función tiene manejador de excepciones: ante error inserta directamente en `AUD_LOG_TRACE_T` un
mensaje con `cod_status = -1` y el texto de error de PostgreSQL. Nunca propaga el fallo hacia
arriba: **un problema de log jamás detiene una carga**, lo cual es lo correcto, pero implica que
puede haber fallos de traza pasando inadvertidos.

## Cómo verificarlo

```sql
-- Nivel configurado y volumen de traza reciente
SELECT (SELECT cod_log_level FROM stg_s3.par_maestro_log_level_t LIMIT 1) AS nivel_configurado,
       count(*)                                                            AS mensajes_hoy
FROM   stg_s3.aud_log_trace_t
WHERE  dat_load_date::date = CURRENT_DATE;
```

```sql
-- Errores registrados hoy
SELECT dat_load_date, cod_load_plan, step_load, des_log
FROM   stg_s3.aud_log_trace_t
WHERE  cod_status = -1 AND dat_load_date >= CURRENT_DATE
ORDER  BY dat_load_date DESC;
```

## Ver también

[E06_tablas_auditoria](../E%20-%20Parametrizacion/E06_tablas_auditoria.md) · [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md) · [A03_glosario](../A%20-%20Orientacion/A03_glosario.md) · [E07_validate_gen_pc](../E%20-%20Parametrizacion/E07_validate_gen_pc.md)

---
titulo: "F11 — La transformación corrió pero la tabla no cambió"
familia: F
etapa: "Transformación TRF"
tipo: Runbook
tags:
  - familia/F
  - etapa/transformacion-trf
  - tipo/runbook
keywords: "sin cambios, no actualizó, insumo vacío, bloqueo por cliente, filtro"
---

# F11 — La transformación corrió pero la tabla no cambió

**Etapa:** Transformación TRF
**Tipo:** Runbook
**Palabras clave:** sin cambios, no actualizó, insumo vacío, bloqueo por cliente, filtro

## Síntoma

El paso de transformación se ejecutó, no hay error en la traza, y la tabla de `trf_s3` sigue igual
que antes.

## Las cinco causas, en orden de frecuencia

### 1. El insumo estaba vacío

Lo más común. La transformación hizo su trabajo: no había nada que transformar.

```sql
SELECT count(*) FROM stg_s3.<TABLA_ORIGEN>_T;

SELECT cod_load_trace, dat_load_date, amt_register_process, cod_status, des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_plan = :plan_de_carga
ORDER  BY dat_load_date DESC LIMIT 3;
```

Sin traza de hoy → el fichero no llegó. Con traza y `amt_register_process = 0` → llegó vacío.
Ver [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md) y [C10_conversion_sin_filas](../C%20-%20Conversion%20Java/C10_conversion_sin_filas.md).

### 2. Todo se descartó en la validación

El fichero llegó y las filas se apartaron antes de llegar a `_T`:

```sql
SELECT des_validate, des_column_name, count(*)
FROM   stg_s3.aud_load_valid_trace_t
WHERE  cod_load_trace = :trace
GROUP  BY 1,2 ORDER BY 3 DESC;
```

Ver [R1_12_descarte_masivo_escalado](../R1%20-%20Descartes/R1_12_descarte_masivo_escalado.md).

### 3. Bloqueo por cliente

`bloqueio_insercao_dados` puede impedir la inserción de clientes concretos según el origen de su
maestro de cartera. Síntoma característico: **faltan los datos de unos clientes y no de otros**.

```sql
SELECT cod_cli, cd_origem, fl_master
FROM   trf_s3.cart_estat_portfoliomaster
WHERE  cod_cli = '<CLIENTE>';
```

Ver [F07_bloqueio_insercao_dados](../F%20-%20Transformacion%20TRF/F07_bloqueio_insercao_dados.md).

### 4. Un filtro del procedimiento excluyó todo

La transformación tiene su propia lógica: fechas, estados, `base_id`. Si el filtro no casa con los
datos de hoy, el resultado es cero filas sin error.

```sql
SELECT prosrc FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'trf_s3' AND p.proname = '<procedimiento>';
```

Busca los `WHERE` y los `INNER JOIN`. Un `INNER` que no casa elimina filas; un filtro de fecha las
excluye en bloque.

### 5. La transformación actualiza en vez de insertar

Algunos procedimientos hacen `UPDATE` de filas existentes en lugar de añadir. El conteo de la tabla
no cambia **aunque el proceso haya funcionado**. Comprueba el contenido, no el número de filas:

```sql
SELECT max(<columna_de_fecha>) FROM trf_s3.<TABLA>;
```

Si la fecha máxima es de hoy, la transformación sí trabajó.

## Lo que NO sirve como prueba

**El color del job.** El indicador de error de esta etapa compara la salida de `psql` con `"0"`, y
el resultado depende de la firma del procedimiento, no de si transformó bien. Un procedimiento sin
parámetro de salida emite `CALL` y se marca como error habiendo funcionado.
Ver [F03_funcion_trf](../F%20-%20Transformacion%20TRF/F03_funcion_trf.md).

**La ausencia de mensajes en la traza.** `LOG_TRACE` filtra por nivel; con el nivel configurado
alto, los mensajes de detalle no se escriben. Ver [E08_log_trace_niveles](../E%20-%20Parametrizacion/E08_log_trace_niveles.md).

```sql
SELECT * FROM stg_s3.par_maestro_log_level_t;
```

## El orden de comprobación

```
1. ¿Hay datos en stg_s3.<TABLA>_T?      → no: causas 1 o 2
2. ¿Cambió la fecha máxima del destino? → sí: causa 5, funcionó
3. ¿Faltan sólo algunos clientes?       → sí: causa 3
4. Si no, leer el procedimiento         → causa 4
```

Dos consultas resuelven los dos primeros pasos, que cubren la mayoría de los casos.

## Cuándo escalar

- Si el insumo falta: es una incidencia de recepción o de carga, no de transformación.
- Si el bloqueo por cliente parece mal configurado: es funcional.
- Si el filtro del procedimiento excluye algo que el negocio espera: hace falta quien conozca la regla.

## Ver también

[F10_localizar_fallo_trf](../F%20-%20Transformacion%20TRF/F10_localizar_fallo_trf.md) · [F07_bloqueio_insercao_dados](../F%20-%20Transformacion%20TRF/F07_bloqueio_insercao_dados.md) · [F14_faltan_datos_stg_o_trf](../F%20-%20Transformacion%20TRF/F14_faltan_datos_stg_o_trf.md) · [R1_12_descarte_masivo_escalado](../R1%20-%20Descartes/R1_12_descarte_masivo_escalado.md) · [F03_funcion_trf](../F%20-%20Transformacion%20TRF/F03_funcion_trf.md)

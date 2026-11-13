---
titulo: "R1.10 — Cuándo un descarte es correcto y no hay nada que hacer"
familia: R1
etapa: "Validación"
tipo: Runbook
tags:
  - familia/R1
  - etapa/validacion
  - tipo/runbook
keywords: "falso positivo, no es incidencia, descarte legítimo, cerrar ticket, ruido"
---

# R1.10 — Cuándo un descarte es correcto y no hay nada que hacer

**Etapa:** Validación
**Tipo:** Runbook
**Palabras clave:** falso positivo, no es incidencia, descarte legítimo, cerrar ticket, ruido

## En una línea

No todo descarte es un fallo: varios son comportamiento previsto del sistema y cerrar el ticket es
la respuesta correcta.

## Los casos legítimos

### 1. Descarte de clave foránea que se resuelve solo

Es el más frecuente. La fila apunta a un catálogo que todavía no se había cargado cuando llegó.
En el siguiente ciclo, con el catálogo ya presente, el reproceso la recupera.

**Cómo confirmarlo:** el mismo valor que faltaba existe ahora en la tabla referenciada, y el
descarte no se repite en la carga siguiente.
**Acción:** ninguna, o un reproceso si hay prisa por el dato. Ver [R1_09_reprocesar_descartes](../R1%20-%20Descartes/R1_09_reprocesar_descartes.md).

### 2. Filtro de negocio permanente

Una fila que un `INNER JOIN` o un `WHERE` deja fuera **a propósito**, en la capa de mapeos. No es
un descarte a reintentar: es la definición del proceso. Reprocesarla no la va a meter nunca.

**Cómo confirmarlo:** el mismo tipo de fila queda fuera todos los días, con el mismo volumen
relativo, sin que nadie se queje del dato.
**Acción:** ninguna. Ver [R1_08_descartes_en_mapeos](../R1%20-%20Descartes/R1_08_descartes_en_mapeos.md).

### 3. Mapeo desactivado a propósito

`exp_s3.tablas_mapeio_t.activo_inactivo` marca el mapeo como inactivo. La tabla destino no se
actualiza porque **no debe** actualizarse.

**Cómo confirmarlo:** consulta la fila de control del mapeo.
**Acción:** ninguna. Si alguien espera ese dato, la conversación es con negocio, no con soporte.

### 4. Mensaje de traza alarmante que no corresponde a nada

`validate_rows_null_fn` escribe siempre `'Error de Validacion de Nulos. Tabla Truncada'` cuando
encuentra nulos, incluso en el flujo tolerante donde no se trunca nada y la carga sigue. Leer ese
mensaje y abrir una incidencia de pérdida de datos es un falso positivo clásico.

**Cómo confirmarlo:** cuenta las filas de la tabla. Si tiene datos, no se truncó.
**Acción:** ninguna. Ver [R1_04_descarte_nulo_obligatorio](../R1%20-%20Descartes/R1_04_descarte_nulo_obligatorio.md).

### 5. Silencio del control de errores

`_00001_Análise_de_erros` tiene su consulta anulada con `WHERE 1=0`. Que no avise **no prueba que
no haya errores**. El caso inverso al anterior: aquí el peligro es dar por bueno un silencio.

**Acción:** no uses ese job como evidencia de nada. Comprueba los descartes directamente.

### 6. Descartes históricos que ya no existen

Los registros de clave foránea del ciclo anterior se renombran a `FOREING_KEY_OLD`. Si cuentas
`AUD_LOAD_VALID_TRACE_T` sin filtrar por fecha, estás sumando ciclos viejos y el número asusta sin
motivo. Filtra siempre por `dat_load_date` o por `cod_load_trace`.

## Antes de cerrar un ticket como «sin acción»

Comprueba estas tres cosas y déjalas escritas en el ticket:

1. **El volumen es el habitual** para esa interfaz — compara con los días anteriores.
2. **La causa está identificada** y encaja con uno de los casos de arriba.
3. **No se repite creciendo.** Un descarte legítimo es estable; uno que crece día a día es una incidencia disfrazada.

Si las tres se cumplen, cerrar es lo correcto y documentarlo evita que el siguiente turno vuelva a
investigar lo mismo.

## Cómo verificarlo

```sql
-- ¿Este descarte es estable o está creciendo?
SELECT dat_load_date::date AS dia, des_validate, count(*) AS filas
FROM   stg_s3.aud_load_valid_trace_t
WHERE  des_table_name = UPPER('<TABLA>_TMP')
  AND  dat_load_date >= CURRENT_DATE - 14
GROUP  BY 1,2
ORDER  BY 1 DESC, 3 DESC;
```

Una serie plana es normalidad. Una serie que sube es incidencia.

## Ver también

[R1_03_identificar_validacion](../R1%20-%20Descartes/R1_03_identificar_validacion.md) · [R1_12_descarte_masivo_escalado](../R1%20-%20Descartes/R1_12_descarte_masivo_escalado.md) · [R1_08_descartes_en_mapeos](../R1%20-%20Descartes/R1_08_descartes_en_mapeos.md) · [R1_07_descarte_variacion_volumen](../R1%20-%20Descartes/R1_07_descarte_variacion_volumen.md)

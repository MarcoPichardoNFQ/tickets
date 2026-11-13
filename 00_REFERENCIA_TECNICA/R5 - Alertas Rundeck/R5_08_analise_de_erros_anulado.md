---
titulo: "R5.08 — ⚠ `_00001 Análise de erros` está anulado"
familia: R5
etapa: "Cierre y Qlik"
tipo: Runbook
tags:
  - familia/R5
  - etapa/cierre-y-qlik
  - tipo/runbook
keywords: "Análise de erros, WHERE 1=0, anulado, silencio, falso negativo, trampa"
---

# R5.08 — ⚠ `_00001 Análise de erros` está anulado

**Etapa:** Cierre y Qlik
**Tipo:** Runbook
**Palabras clave:** Análise de erros, WHERE 1=0, anulado, silencio, falso negativo, trampa

## En una línea

El job de análisis de errores tiene su consulta **anulada con `WHERE 1=0`**: no puede devolver
resultados nunca, y su silencio no prueba absolutamente nada.

## Qué hace en realidad

El job existe, está programado, se ejecuta y termina correctamente. Pero su consulta lleva una
condición que **nunca se cumple**, así que el resultado es siempre vacío y la conclusión siempre
«no hay errores».

Cuando encuentra algo —que no puede— imprimiría:

```
Error: Se encontró información errónea en los últimos 15 minutos.
Favor verificar detalle en la siguiente URL
https://qlik.s3caceis.com.br/sense/app/cec10006-.../sheet/4a6a2053-.../state/analysis?qlikTicket=...
```

Ese mensaje no se ha emitido nunca desde que la condición está así.

## Por qué es peligroso

Es el peor tipo de fallo de monitorización: **uno que parece funcionar**.

- El job aparece en verde en Rundeck.
- Está en el flujo de cierre, ocupando el sitio de un control real.
- Tiene notificación configurada, así que da la impresión de estar vigilado.
- Y no comprueba nada.

Alguien que revise el estado del sistema y vea este job en verde concluirá que no hay errores. **Es
un falso negativo permanente.**

## Qué NO hacer

**No lo uses como evidencia.** Ni para cerrar un ticket, ni para afirmar que un ciclo fue limpio, ni
para descartar una hipótesis. Su salida no contiene información.

Si alguien argumenta «el análisis de errores no ha dado nada», la respuesta correcta es que ese
control lleva anulado desde hace tiempo y hay que comprobar por otra vía.

## Qué usar en su lugar

Los controles que sí funcionan:

```sql
-- Errores de carga
SELECT cod_load_trace, cod_load_plan, dat_load_date, step_load, des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  cod_status = -1 AND dat_load_date::date = CURRENT_DATE
ORDER  BY dat_load_date DESC;

-- Errores técnicos registrados
SELECT dat_load_date, cod_load_plan, des_log
FROM   stg_s3.aud_log_trace_t
WHERE  cod_status = -1 AND dat_load_date >= CURRENT_DATE
ORDER  BY dat_load_date DESC;

-- Descartes y errores de validación
SELECT des_table_name, des_validate, count(*)
FROM   stg_s3.aud_load_valid_trace_t
WHERE  dat_load_date::date = CURRENT_DATE
GROUP  BY 1,2 ORDER BY 3 DESC;

-- Errores de mapeo
SELECT * FROM trf_s3.s3_control_errores_mapeo
WHERE  dat_proc_exe::date = CURRENT_DATE
ORDER  BY dat_proc_exe DESC;
```

Esas cuatro consultas cubren lo que este job pretendía cubrir. Están recogidas en el checklist
diario. Ver [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md).

## Cómo confirmarlo en tu entorno

Abre el job en Rundeck y busca la condición en su consulta:

```bash
grep -i -A5 "where" "_00001_Análise_de_erros.xml" | grep -i "1=0"
```

Si en algún momento se corrige, esta ficha deja de aplicar — pero **compruébalo antes de confiar en
el job**, no al revés.

## Por qué está así

No consta. Puede haberse anulado temporalmente para silenciar falsos positivos y no haberse
restaurado nunca. Es la hipótesis más probable y también la más común en este tipo de sistemas: un
silenciado temporal que se vuelve permanente porque nadie recuerda que está.

## Material de escalado

Éste es un hallazgo que merece llegar a quien pueda decidir: **hay un control de errores en el flujo
de cierre que no comprueba nada**. O se restaura, o se retira para que no genere una falsa sensación
de cobertura. Dejarlo como está es la peor de las tres opciones.

## Ver también

[J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md) · [R5_02_jobs_sin_notificacion](../R5%20-%20Alertas%20Rundeck/R5_02_jobs_sin_notificacion.md) · [R5_07_alerta_vs_estado_real](../R5%20-%20Alertas%20Rundeck/R5_07_alerta_vs_estado_real.md) · [R1_07_descarte_variacion_volumen](../R1%20-%20Descartes/R1_07_descarte_variacion_volumen.md)

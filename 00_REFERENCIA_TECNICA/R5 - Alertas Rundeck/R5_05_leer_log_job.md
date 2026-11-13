---
titulo: "R5.05 — Leer el log de un job fallido"
familia: R5
etapa: "Transversal"
tipo: Runbook
tags:
  - familia/R5
  - etapa/transversal
  - tipo/runbook
keywords: "log de Rundeck, ejecución, paso a paso, qué buscar, triaje"
---

# R5.05 — Leer el log de un job fallido

**Etapa:** Transversal
**Tipo:** Runbook
**Palabras clave:** log de Rundeck, ejecución, paso a paso, qué buscar, triaje

## En una línea

Cuatro cosas que mirar en el detalle de una ejecución, y qué patrones buscar en la salida.

## Los cuatro datos del detalle de ejecución

| Dato | Para qué sirve |
|---|---|
| **Qué paso falló** | Sitúa la etapa. El nombre del paso suele decir la tabla |
| **Hora de inicio y fin** | Compara con ejecuciones anteriores del mismo job |
| **Estado de los demás pasos** | Ver más abajo: **los errores no detienen el bloque** |
| **La salida del paso** | La causa real |

## ⚠ Un fallo no detiene el bloque

Los `exit` del script de carga están comentados. Un paso que falla marca error pero **el bloque
sigue ejecutando todo lo demás**.

Consecuencias al leer el log:

- **Puede haber varios fallos**, no sólo el primero. Revisa la lista completa
- **Que un job acabe en rojo no dice dónde se paró**, porque no se paró
- Los pasos posteriores al fallo **sí se ejecutaron**

Ver [D03_script_stg_trf](../D%20-%20Carga%20STG/D03_script_stg_trf.md).

## Y varios pasos corren en paralelo

El orquestador tiene un grafo de dependencias declarado: algunos pasos se lanzan a la vez. Horas
solapadas entre pasos son normales, no señal de nada. Ver [G07_ciclo_completo_mapeos](../G%20-%20Mapeos/G07_ciclo_completo_mapeos.md).

## Qué buscar en la salida

| Patrón | Significa | Ficha |
|---|---|---|
| `PASO OMITIDO` | Interfaz sin fichero. **La causa de ruido nº1** | [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md) |
| `ERROR CRÍTICO: Carga incompleta` | Faltan prefijos oficiales | [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md) |
| `ArchivoAyudaRundeckMegara NO contiene 1` | El ciclo está **apagado** | [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md) |
| `Falló con código NNN. Reintentando en 5 minutos` | La API de Megara no responde. Hasta 2,5 h por endpoint | [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md) |
| `NO es válido. Razón:` | Fallo de XSD, con línea y elemento | [C09_xml_no_valida](../C%20-%20Conversion%20Java/C09_xml_no_valida.md) |
| `[Ljava.lang.StackTraceElement;@...` | Error del conversor, **ilegible** | [C12_conversion_fallo_log](../C%20-%20Conversion%20Java/C12_conversion_fallo_log.md) |
| `Eliminando los archivos generados` | La conversión abortó y borró su salida | [C06_ficheros_de_salida](../C%20-%20Conversion%20Java/C06_ficheros_de_salida.md) |
| `Archivo vacío, termina proceso` | XML sin nodos. **Sale con éxito** | [C10_conversion_sin_filas](../C%20-%20Conversion%20Java/C10_conversion_sin_filas.md) |
| `El atributo "X" no existe` | Herencia mal declarada | [C07_herencias_claves](../C%20-%20Conversion%20Java/C07_herencias_claves.md) |
| `extra data after last expected column` | Separador dentro de un dato | [C11_separador_dentro_del_dato](../C%20-%20Conversion%20Java/C11_separador_dentro_del_dato.md) |
| `Tabla % Contiene por lo menos 1 regitro descartado` | Duplicados de mapeo | [H03_validacion_descartes](../H%20-%20Cierre%20y%20Qlik/H03_validacion_descartes.md) |
| `Ejecutando: SELECT trf_s3.function_meg_…` | Traza del despacho de mapeos | [G08_fim_carga_mapeo](../G%20-%20Mapeos/G08_fim_carga_mapeo.md) |
| `Deadlock detectado. Intento N` | Reintento en curso. **No es fallo aún** | [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md) |
| `Se agotaron los intentos` | El mapeo **sí falló** | [R3_02_leer_error_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_02_leer_error_mapeo.md) |

## Correlacionar con la base de datos

El log de Rundeck dice qué pasó en el shell; la base dice qué pasó con el dato. Los dos hacen falta.

```sql
SELECT cod_load_trace, cod_load_plan, dat_load_date, step_load, cod_status,
       amt_register_process, des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  dat_load_date::date = CURRENT_DATE
ORDER  BY dat_load_date DESC;
```

**Las horas son comparables:** el job se programa en `GMT-3:00` y `LOG_TRACE` graba en `ADT`, que es
el mismo desfase. La excepción es la ruta de error de `LOG_TRACE`, que usa `now()` a secas.
Ver [G07_ciclo_completo_mapeos](../G%20-%20Mapeos/G07_ciclo_completo_mapeos.md) y [E08_log_trace_niveles](../E%20-%20Parametrizacion/E08_log_trace_niveles.md).

## Cuando el log no basta

Tres casos documentados en que la salida no contiene la causa:

- **El conversor Java** imprime la traza de pila como dirección de memoria → [C12_conversion_fallo_log](../C%20-%20Conversion%20Java/C12_conversion_fallo_log.md)
- **El nivel de log** puede estar suprimiendo mensajes → [E08_log_trace_niveles](../E%20-%20Parametrizacion/E08_log_trace_niveles.md)
- **22 jobs no notifican nada**: si el fallo fue en uno de ellos, no hay correo que leer → [R5_02_jobs_sin_notificacion](../R5%20-%20Alertas%20Rundeck/R5_02_jobs_sin_notificacion.md)

En los tres, la vía es la base de datos.

## Ver también

[R5_04_alertas_con_y_sin_log](../R5%20-%20Alertas%20Rundeck/R5_04_alertas_con_y_sin_log.md) · [R5_09_catalogo_alertas](../R5%20-%20Alertas%20Rundeck/R5_09_catalogo_alertas.md) · [R5_07_alerta_vs_estado_real](../R5%20-%20Alertas%20Rundeck/R5_07_alerta_vs_estado_real.md) · [I12_consultas_frecuentes](../I%20-%20Referencia%20de%20datos/I12_consultas_frecuentes.md)

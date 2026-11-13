---
titulo: "J10 — Trampas conocidas: parece un fallo y no lo es"
familia: J
etapa: "Transversal"
tipo: Runbook
tags:
  - familia/J
  - etapa/transversal
  - tipo/runbook
keywords: "trampas, falsos positivos, ruido, no es incidencia, cerrar ticket, gotchas"
---

# J10 — Trampas conocidas: parece un fallo y no lo es

**Etapa:** Transversal
**Tipo:** Runbook
**Palabras clave:** trampas, falsos positivos, ruido, no es incidencia, cerrar ticket, gotchas

## En una línea

La lista de cosas que parecen incidencias y no lo son — y de cosas que parecen correctas y no lo
están. Leerla ahorra la mitad de las investigaciones.

## Parece un fallo, no lo es

| Lo que ves | Realidad | Ficha |
|---|---|---|
| Traza dice **«Tabla Truncada»** tras un fallo de nulos | El texto es fijo. **No se trunca nada** en flujo tolerante | [R1_04_descarte_nulo_obligatorio](../R1%20-%20Descartes/R1_04_descarte_nulo_obligatorio.md) |
| **«PASO OMITIDO»** y el bloque en rojo | Una interfaz que hoy no tocaba. Marca error general | [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md) |
| **CSV de salida de 0 bytes** | Deliberados: nodos del XSD ausentes en el XML | [C06_ficheros_de_salida](../C%20-%20Conversion%20Java/C06_ficheros_de_salida.md) |
| Tabla **`MEG_*` vacía** tras el cierre | La limpieza las vacía todas por diseño | [H02_stg_startover_cleanup](../H%20-%20Cierre%20y%20Qlik/H02_stg_startover_cleanup.md) |
| **Deadlock `40P01`** registrado | Esperable con el paralelismo. Comprueba si el reintento lo resolvió | [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md) |
| Descartes de **clave foránea** en una interfaz | Suele ser orden, no calidad: el catálogo llegó después | [R1_06_descarte_integridad_referencial](../R1%20-%20Descartes/R1_06_descarte_integridad_referencial.md) |
| Texto con **`¡`** donde debía haber `!` | Sustitución deliberada antes de convertir | [C05_sed_separador](../C%20-%20Conversion%20Java/C05_sed_separador.md) |
| **XML vacío** archivado con éxito | Un día sin movimientos. El job sale en verde | [C10_conversion_sin_filas](../C%20-%20Conversion%20Java/C10_conversion_sin_filas.md) |
| Job de mapeo **verde sin actualizar** la tabla | Mapeo desactivado en `tablas_mapeio_t` | [R3_07_mapeo_desactivado](../R3%20-%20Errores%20de%20mapeo/R3_07_mapeo_desactivado.md) |
| Miles de ejecuciones del mismo job | El vigilante corre cada 3 segundos. Es normal | [B04_job_validacion_constante](../B%20-%20Recepcion%20y%20flags/B04_job_validacion_constante.md) |
| Nada corre **entre las 06:00 y las 07:00** | El orquestador `0999` excluye la hora 6 | [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md) |
| Alerta **`URGENTE no se recibieron...`** sin ficheros ausentes | Cuatro de sus seis comprobaciones no son sobre ausencia | [R4_03_validacion_cantidades](../R4%20-%20Sets%20incompletos/R4_03_validacion_cantidades.md) |

## Parece correcto, no lo está

Éstas son las peligrosas: el sistema dice que todo va bien y no es cierto.

| Lo que ves | Realidad | Ficha |
|---|---|---|
| **`Análise de erros`** en verde | Su consulta está anulada con `WHERE 1=0`. No comprueba nada | [R5_08_analise_de_erros_anulado](../R5%20-%20Alertas%20Rundeck/R5_08_analise_de_erros_anulado.md) |
| Paso **«Recarga Qlik»** en verde | Hace `exit 0` sin comprobar el resultado. Y **un fallo de Qlik durante la recarga no genera alerta** | [H12_recarga_qlik_fallo](../H%20-%20Cierre%20y%20Qlik/H12_recarga_qlik_fallo.md) |
| **Ninguna alerta** en toda la jornada | 22 de 46 jobs no notifican nada | [R5_02_jobs_sin_notificacion](../R5%20-%20Alertas%20Rundeck/R5_02_jobs_sin_notificacion.md) |
| **Sin descartes de duplicados** | Nada los detecta: ni claves en staging ni validación activa | [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md) |
| **Sin alarmas de volumen** | La validación de variación no se ejecuta, y compara mal | [R1_07_descarte_variacion_volumen](../R1%20-%20Descartes/R1_07_descarte_variacion_volumen.md) |
| Tabla de salida **con datos** | Puede estar a medias si el mapeo tiene una segunda función apagada | [R3_07_mapeo_desactivado](../R3%20-%20Errores%20de%20mapeo/R3_07_mapeo_desactivado.md) |
| Un mapeo activo que **nunca falla** | Puede ser huérfano: no está en la lista del orquestador | [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md) |
| Carga **sin errores de columnas** | Si el origen reordenó columnas, cargó los datos desplazados | [D04_read_header_fn](../D%20-%20Carga%20STG/D04_read_header_fn.md) |

## Trampas al consultar

| Trampa | Qué pasa |
|---|---|
| Buscar `FOREIGN_KEY_OLD` | Está escrito **`FOREING_KEY_OLD`**. No encontrarás nada |
| Buscar en `PAR_MAESTRO_VALID_T` por nombre de tabla | Se guarda como **`'STG_S3.TABLA A'`**, con esquema y alias |
| Correlacionar horas entre tablas | `LOG_TRACE` usa `AT TIME ZONE 'ADT'`; su ruta de error usa `now()` |
| Ordenar por `data_recebemento` | Es **texto**, no fecha: ordena alfabéticamente |
| Usar `last_value` en una investigación larga | Cambia si llega otro flag. Fíjalo al principio |
| Contar `AUD_LOAD_VALID_TRACE_T` sin filtrar fecha | Suma ciclos históricos y el número asusta sin motivo |
| Subir el nivel de log para ver más | El filtro es al revés: número más alto = menos mensajes |
| Buscar `inicio_carga_mapeo` | El procedimiento se llama **`incio_carga_mapeo`**, sin la primera n |
| Comparar `nome_fn_mapeio` con `pg_proc.proname` | La tabla los guarda en **mayúsculas mezcladas**; `pg_proc` en minúsculas. Sin `lower()` en ambos lados, no casa ninguno |

## Antes de abrir una incidencia

1. ¿Está en alguna de estas tablas?
2. ¿El volumen es el habitual comparado con días anteriores?
3. ¿Se repite o es puntual?

Si es una trampa conocida, **ciérralo citando la ficha**. Eso evita que el siguiente turno repita
la investigación entera, que es el coste real de estos falsos positivos.

## Ver también

[R5_07_alerta_vs_estado_real](../R5%20-%20Alertas%20Rundeck/R5_07_alerta_vs_estado_real.md) · [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md) · [R1_10_descarte_correcto_sin_accion](../R1%20-%20Descartes/R1_10_descarte_correcto_sin_accion.md) · [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md)

---
titulo: "R5.07 — Llega alerta pero el job está verde, y al revés"
familia: R5
etapa: "Transversal"
tipo: Runbook
tags:
  - familia/R5
  - etapa/transversal
  - tipo/runbook
keywords: "falso positivo, falso negativo, verde pero mal, alerta sin causa, discrepancia"
---

# R5.07 — Llega alerta pero el job está verde, y al revés

**Etapa:** Transversal
**Tipo:** Runbook
**Palabras clave:** falso positivo, falso negativo, verde pero mal, alerta sin causa, discrepancia

## En una línea

El estado de un job y el estado real del dato **no son lo mismo**, y en este sistema se separan por
causas conocidas.

## Verde pero mal — los falsos negativos

Un job puede terminar correctamente sin haber hecho su trabajo. Las causas documentadas:

| Situación | Por qué sale verde |
|---|---|
| **Mapeo desactivado** | El procedimiento comprueba `activo_inactivo` y no hace nada. Ver [R3_07_mapeo_desactivado](../R3%20-%20Errores%20de%20mapeo/R3_07_mapeo_desactivado.md) |
| **`Análise de erros`** | Su consulta está anulada con `WHERE 1=0`. Ver [R5_08_analise_de_erros_anulado](../R5%20-%20Alertas%20Rundeck/R5_08_analise_de_erros_anulado.md) |
| **Recarga de Qlik** | El paso hace `echo` y `exit 0` pase lo que pase. Ver [H08_recarga_qlik](../H%20-%20Cierre%20y%20Qlik/H08_recarga_qlik.md) |
| **XML vacío** | La conversión archiva y sale con 0 sin generar planos. Ver [C10_conversion_sin_filas](../C%20-%20Conversion%20Java/C10_conversion_sin_filas.md) |
| **Mapeo huérfano** | No está en la lista del orquestador: nadie lo llama, nadie falla. Ver [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md) |
| **Job sin notificación** | Falló, pero no avisa. Ver [R5_02_jobs_sin_notificacion](../R5%20-%20Alertas%20Rundeck/R5_02_jobs_sin_notificacion.md) |

Son seis mecanismos distintos con el mismo efecto: **el verde no prueba nada**.

## Rojo pero bien — los falsos positivos

Y al revés: un job en rojo que no corresponde a ninguna incidencia real.

| Situación | Por qué sale rojo |
|---|---|
| **«PASO OMITIDO»** | Una interfaz que hoy no tocaba marca error general. La causa de ruido nº1. Ver [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md) |
| **`URGENTE no se recibieron...`** | La comparación contra el lote fijo `29817` marca como problema interfaces nuevas. Ver [R4_03_validacion_cantidades](../R4%20-%20Sets%20incompletos/R4_03_validacion_cantidades.md) |
| **`ERROR EN MAPEO`** | Un deadlock que el reintento resolvió deja registro igualmente. Ver [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md) |
| **`Tabla Truncada`** | El mensaje se escribe siempre que hay nulos, aunque no se trunque nada. Ver [R1_04_descarte_nulo_obligatorio](../R1%20-%20Descartes/R1_04_descarte_nulo_obligatorio.md) |

## La regla operativa

**Verifica siempre contra el dato, nunca contra el color.**

```sql
-- ¿Cargó lo de hoy?
SELECT cod_load_plan, count(*), sum(amt_register_process) AS filas
FROM   stg_s3.aud_load_trace_t
WHERE  dat_load_date::date = CURRENT_DATE AND step_load = 'CARGA FICHERO'
GROUP  BY 1 ORDER BY 1;

-- ¿Hay errores reales?
SELECT count(*) FROM stg_s3.aud_load_trace_t
WHERE  cod_status = -1 AND dat_load_date::date = CURRENT_DATE;

-- ¿Se poblaron las tablas de salida?
SELECT count(*) FROM trf_s3.<TABLA_DESTINO>;
```

Esas tres preguntas dicen más sobre el estado del sistema que la bandeja de entrada completa.

## Cuando la discrepancia es real

Si tras verificar sigue sin cuadrar —el job dice una cosa y el dato otra, y ninguna de las causas
conocidas lo explica— entonces sí hay algo nuevo. En ese caso, para escalar hacen falta:

- ID de ejecución del job en Rundeck y su log completo
- `cod_load_trace` afectados
- Conteos reales de las tablas implicadas
- Qué causa conocida descartaste y por qué

Ese último punto es el que convierte un ticket vago en uno accionable.

## Ver también

[R5_09_catalogo_alertas](../R5%20-%20Alertas%20Rundeck/R5_09_catalogo_alertas.md) · [R5_02_jobs_sin_notificacion](../R5%20-%20Alertas%20Rundeck/R5_02_jobs_sin_notificacion.md) · [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md) · [R5_08_analise_de_erros_anulado](../R5%20-%20Alertas%20Rundeck/R5_08_analise_de_erros_anulado.md) · [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md)

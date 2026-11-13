---
titulo: "A06 — Árbol de decisión: mi incidencia, ¿de qué etapa es?"
familia: A
etapa: "Transversal"
tipo: Runbook
tags:
  - familia/A
  - etapa/transversal
  - tipo/runbook
keywords: "diagnóstico, triaje, por dónde empiezo, incidencia, decisión"
---

# A06 — Árbol de decisión: mi incidencia, ¿de qué etapa es?

**Etapa:** Transversal
**Tipo:** Runbook
**Palabras clave:** diagnóstico, triaje, por dónde empiezo, incidencia, decisión

## En una línea

Empieza por el síntoma que ve el usuario y baja: cada respuesta te lleva a una etapa concreta y a
la ficha que la cubre.

## Detalle

### Punto de partida: ¿qué se ve mal?

**«Falta un dato en Qlik» / «Qlik muestra datos de ayer»**

1. ¿El dato existe en `exp_s3`? Si **sí** → el problema es de recarga de Qlik → familia `H`.
2. Si **no**, ¿existe en `trf_s3`? Si **sí** → el mapeo no corrió o falló → familia `R3`.
3. Si **no**, ¿existe en `stg_s3.TABLA_T`? Si **sí** → la transformación no corrió → familia `F`.
4. Si **no**, ¿está en `TABLA_ERR` o `TABLA_DES`? Si **sí** → fue descartado → familia `R1`.
5. Si **no** está en ningún sitio → el fichero no llegó o no se cargó → familias `R4` y `D`.

Esa escalera de cinco preguntas resuelve la mayoría de los casos. Las consultas concretas para
recorrerla están en [R1_11_consultas_descartes](../R1%20-%20Descartes/R1_11_consultas_descartes.md).

**«Llegó una alerta de Rundeck»** → familia `R5`. Empieza por identificar el job y si la alerta
es `onfailure` o `onstart`.

**«Hay filas de más» / «un importe está duplicado»** → familia `R2`.

**«El proceso no ha arrancado hoy»**

1. ¿Llegó el flag? → `R4`
2. ¿Llegaron todos los XML del lote? → `R4`
3. ¿Es día hábil y toca ejecutar? → ficha de calendario `I18`
4. ¿Está el job programado y habilitado en Rundeck? → `R5`

**«Un proceso lleva horas colgado»** → mira primero bloqueos y deadlocks: `R3.03` si es un mapeo,
familia `F` si es una transformación.

### Regla de oro

**Ve siempre desde el final hacia el principio.** Es más rápido comprobar si el dato está en la
tabla final y retroceder, que seguir el flujo desde el fichero. Cinco consultas te sitúan la
incidencia en una etapa; a partir de ahí la ficha de esa etapa te da la causa.

### Antes de escalar, ten esto

- `cod_load_trace` de la carga afectada
- Nombre de la tabla y de la interfaz
- Fecha y hora del lote
- Qué dice `des_process_executed` en `aud_load_trace_t`
- Si hay filas en `_ERR` o `_DES` y con qué `des_validate`

## Cómo verificarlo

Consulta de situación general, primer vistazo ante cualquier incidencia:

```sql
SELECT cod_load_trace, cod_load_plan, dat_load_date,
       step_load, cod_status,
       amt_register_process, amt_register_notprocess,
       des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  dat_load_date::date = CURRENT_DATE
ORDER  BY dat_load_date DESC;
```

`cod_status = -1` marca lo que se detuvo. `des_process_executed` cuenta el recorrido en texto.

## Ver también

[A02_flujo_e2e_seis_pasos](../A%20-%20Orientacion/A02_flujo_e2e_seis_pasos.md) · [R1_11_consultas_descartes](../R1%20-%20Descartes/R1_11_consultas_descartes.md) · [R1_03_identificar_validacion](../R1%20-%20Descartes/R1_03_identificar_validacion.md) · [A05_esquemas_base_de_datos](../A%20-%20Orientacion/A05_esquemas_base_de_datos.md)

---
titulo: "A01 — Qué es Aldrin y qué hace"
familia: A
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/A
  - etapa/transversal
  - tipo/referencia
keywords: "Aldrin, Megara, ETL, visión general, S3 CACEIS, custodia, Brasil"
---

# A01 — Qué es Aldrin y qué hace

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** Aldrin, Megara, ETL, visión general, S3 CACEIS, custodia, Brasil

## En una línea

Aldrin es el ETL que recibe cada día los ficheros XML de **Megara** (el sistema de custodia),
los convierte,
los valida, los carga en PostgreSQL, los transforma al modelo de negocio y los publica en Qlik.

## Detalle

El dato entra como **XML** desde Megara, el sistema origen (MegaCommon / innotech), depositado en un
directorio del servidor junto con un **archivo flag** que anuncia que el lote está completo.
A partir de ahí todo lo orquesta **Rundeck**.

El recorrido tiene seis etapas:

1. **Recepción** — se detecta el flag y se registran los archivos esperados.
2. **Conversión** — un programa Java valida cada XML contra su XSD y lo convierte a texto plano.
3. **Carga a staging** — los planos entran en PostgreSQL, esquema `stg_s3`, por `\COPY`.
4. **Validación** — nulos, formato e integridad referencial; lo que no pasa se aparta sin parar el proceso.
5. **Transformación** — los datos sanos pasan al modelo de negocio, esquema `trf_s3`.
6. **Mapeos y salida** — se consolidan las vistas de negocio en `exp_s3` y se recargan las tareas de Qlik.

Tres rasgos definen el sistema y explican casi todo lo que verás en incidencias:

**Es metadata-driven.** Qué se carga, con qué separador, qué columnas son obligatorias, qué
formato debe tener cada campo y qué claves foráneas se comprueban no está en el código: está en
las tablas `PAR_*` de `stg_s3`. Cambiar el comportamiento de una carga es cambiar filas de una
tabla, no tocar un script.

**No para ante una fila mala.** Una fila que falla una validación se aparta a una tabla espejo
(`_ERR` o `_DES`) y el proceso continúa con el resto. Esto es deliberado. Ver [R1_01_descarte_vs_error](../R1%20-%20Descartes/R1_01_descarte_vs_error.md).

**Se ejecuta en ciclos cortos, no una vez al día.** Los orquestadores raíz se disparan cada 10
minutos y comprueban si hay trabajo pendiente. Ver [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md).

## Cómo verificarlo

Estado del último lote:

```sql
SELECT cod_load_trace, cod_load_plan, dat_load_date, step_load,
       cod_status, des_process_executed
FROM   stg_s3.aud_load_trace_t
ORDER  BY dat_load_date DESC
LIMIT  20;
```

## Ver también

[Inicio](../Inicio.md) · [A02_flujo_e2e_seis_pasos](../A%20-%20Orientacion/A02_flujo_e2e_seis_pasos.md) · [A03_glosario](../A%20-%20Orientacion/A03_glosario.md) · [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md)

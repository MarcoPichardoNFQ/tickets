---
titulo: "R1.09 — Reprocesar descartes con `fn_reproceso_descart`"
familia: R1
etapa: "Validación"
tipo: Runbook
tags:
  - familia/R1
  - etapa/validacion
  - tipo/runbook
keywords: "fn_reproceso_descart, reproceso, reintento, _DES, truncate, recuperar descartes"
---

# R1.09 — Reprocesar descartes con `fn_reproceso_descart`

**Etapa:** Validación
**Tipo:** Runbook
**Palabras clave:** fn_reproceso_descart, reproceso, reintento, _DES, truncate, recuperar descartes

## Síntoma

Hay filas en `TABLA_DES` que se descartaron por clave foránea, el catálogo que faltaba ya está
cargado, y queremos que esas filas entren.

## Qué hace la función

`stg_s3.fn_reproceso_descart(tabla, cod_load_trace, cod_load_plan)` hace exactamente dos cosas:

```sql
-- 1. Reinserta en _TMP las filas de _DES cuya clave NO esté ya en _TMP
INSERT INTO stg_s3.<TABLA>_TMP (columnas...)
SELECT columnas... FROM stg_s3.<TABLA>_DES
WHERE  clave_concatenada IN (
         SELECT clave_concatenada FROM stg_s3.<TABLA>_DES
         EXCEPT
         SELECT clave_concatenada FROM stg_s3.<TABLA>_TMP);

-- 2. Vacía la tabla de descartes
TRUNCATE TABLE stg_s3.<TABLA>_DES;
```

La clave se construye concatenando las columnas marcadas con `CHK_CLAVE = 1` en
`PAR_MAESTRO_COLUMNAS_T`. El `EXCEPT` evita reinsertar lo que ya está en `_TMP`.

## ⚠ Tres cosas que hay que saber antes de lanzarlo

**1. El `TRUNCATE` es incondicional.** Se ejecuta siempre, se hayan reinsertado filas o no. Las
filas de `_DES` que **no** se reinsertaron —porque su clave ya existía en `_TMP`— también
desaparecen. No hay copia. Si necesitas conservar constancia de lo descartado, sácala antes:

```sql
CREATE TABLE tmp_backup_des AS SELECT * FROM stg_s3.<TABLA>_DES;
```

**2. Si falla, no te vas a enterar de por qué.** El manejador de excepciones intenta registrar el
error así:

```sql
INSERT INTO stg_s3.load_trace_t (...) VALUES (...);
```

`stg_s3.load_trace_t` **no existe** en el DDL — la tabla de trazas se llama `aud_load_trace_t`.
El manejador falla al ejecutarse y el error que ves es «relation does not exist», que sustituye al
error original. El fallo real queda oculto. Confírmalo en tu entorno con:

```sql
SELECT to_regclass('stg_s3.load_trace_t');   -- NULL = no existe
```

**3. Reinsertar en `_TMP` no es cargar.** La función deja las filas en la tabla temporal. Para que
lleguen a `_T` tiene que volver a pasar el ciclo de validación. Si la causa del descarte sigue ahí,
volverán a descartarse.

## Acción, paso a paso

1. **Confirma que la causa está resuelta.** Si era falta de catálogo, comprueba que el catálogo ya
   tiene el valor:

```sql
SELECT count(*) FROM stg_s3.<TABLA_REFERENCIADA>
WHERE  <columna_fk> = '<valor_que_faltaba>';
```

2. **Respalda `_DES`** si te importa el histórico (ver arriba).
3. **Cuenta lo que hay antes**, para poder comparar:

```sql
SELECT count(*) AS en_des FROM stg_s3.<TABLA>_DES;
SELECT count(*) AS en_tmp FROM stg_s3.<TABLA>_TMP;
```

4. **Lanza el reproceso** con el `cod_load_trace` y `cod_load_plan` de la carga original.
5. **Verifica**: `_DES` debe estar vacía y `_TMP` debe haber crecido.
6. **Vuelve a lanzar la carga** para que las filas atraviesen la validación y lleguen a `_T`.

## Causas probables de que el reproceso no arregle nada

1. **El catálogo sigue sin el valor.** Las filas vuelven a `_DES` en el siguiente ciclo.
2. **La clave ya estaba en `_TMP`.** El `EXCEPT` las excluye y el `TRUNCATE` las borra: parece que se procesaron y en realidad se perdieron.
3. **La causa no era orden sino dato malo.** Reprocesar no arregla un valor que no existe en ningún sitio.

## Cuándo escalar

Si el reproceso deja `_DES` vacía pero las filas no aparecen en `_T`, o si necesitas recuperar
descartes ya truncados. Lo segundo, sin respaldo previo, no tiene vuelta atrás desde base de datos.

## Ver también

[R1_06_descarte_integridad_referencial](../R1%20-%20Descartes/R1_06_descarte_integridad_referencial.md) · [R1_02_donde_cae_cada_cosa](../R1%20-%20Descartes/R1_02_donde_cae_cada_cosa.md) · [R1_10_descarte_correcto_sin_accion](../R1%20-%20Descartes/R1_10_descarte_correcto_sin_accion.md) · [R1_11_consultas_descartes](../R1%20-%20Descartes/R1_11_consultas_descartes.md)

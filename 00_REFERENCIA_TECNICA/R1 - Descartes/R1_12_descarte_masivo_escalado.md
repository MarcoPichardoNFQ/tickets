---
titulo: "R1.12 — Descarte masivo de una interfaz completa"
familia: R1
etapa: "Validación"
tipo: Runbook
tags:
  - familia/R1
  - etapa/validacion
  - tipo/runbook
keywords: "descarte masivo, interfaz completa, escalado, truncate, contrato de datos, incidencia grave"
---

# R1.12 — Descarte masivo de una interfaz completa

**Etapa:** Validación
**Tipo:** Runbook
**Palabras clave:** descarte masivo, interfaz completa, escalado, truncate, contrato de datos, incidencia grave

## Síntoma

Una interfaz que normalmente descarta unas pocas filas descarta hoy la mayoría, o la tabla `_T`
aparece vacía después de una carga que terminó.

## Qué mirar primero, en este orden

**1. ¿Es un descarte o un truncado?**

```sql
SELECT count(*) FROM stg_s3.<TABLA>_T;    -- ¿hay algo?
SELECT count(*) FROM stg_s3.<TABLA>_DES;  -- ¿está apartado?
```

Tabla vacía **y** `_DES` vacía → no es descarte, es truncado. Vete al punto 2.
Tabla vacía **y** `_DES` llena → descarte masivo. Punto 3.

**2. Si fue truncado: comprueba el modo de la carga**

```sql
SELECT cod_load_plan, valid_err_des FROM stg_s3.par_load_plan_t
WHERE  cod_load_plan = :plan;
```

Si `valid_err_des ≠ 1`, la carga es estricta y **un solo fallo de clave foránea ejecuta
`TRUNCATE` sobre la tabla completa**. No hay filas apartadas que recuperar: hay que **recargar el
fichero** una vez resuelta la causa. Ver [R1_01_descarte_vs_error](../R1%20-%20Descartes/R1_01_descarte_vs_error.md) y [R1_06_descarte_integridad_referencial](../R1%20-%20Descartes/R1_06_descarte_integridad_referencial.md).

**3. Si fue descarte masivo: mira la forma del fallo**

```sql
SELECT des_validate, des_column_name, count(*) AS filas
FROM   stg_s3.aud_load_valid_trace_t
WHERE  des_table_name = UPPER('<TABLA>_TMP')
  AND  dat_load_date::date = CURRENT_DATE
GROUP  BY 1,2
ORDER  BY filas DESC;
```

La **forma** del fallo dice la causa:

| Patrón | Causa casi segura |
|---|---|
| Una sola columna, muchas filas | Cambio de contrato en origen: esa columna cambió de formato, longitud o dejó de venir |
| Varias columnas **contiguas**, muchas filas | Desplazamiento de columnas en la conversión — un `!` dentro de un valor. Familia `C` |
| Todas las filas, `FOREIGN_KEY` | El catálogo referenciado no se cargó. Problema de orden o de set incompleto |
| Todas las filas, `NULOS` | El fichero llegó con estructura distinta, o la conversión produjo columnas vacías |

## Causas probables, por orden

1. **Cambio no anunciado en el fichero de origen.** Es la causa número uno de un descarte masivo repentino en una interfaz estable.
2. **Falta el catálogo del que depende.** Si la tabla referenciada no cargó, todas las filas quedan huérfanas a la vez.
3. **Conversión defectuosa** — separador dentro de un dato, encoding, XSD desactualizado.
4. **Parametrización tocada recientemente.** Si alguien cambió `PAR_MAESTRO_*` ayer, empieza por ahí.

## Acción

1. **No reproceses a ciegas.** Un reproceso sobre una causa no resuelta vacía `_DES` sin recuperar
   nada. Ver la advertencia del `TRUNCATE` en [R1_09_reprocesar_descartes](../R1%20-%20Descartes/R1_09_reprocesar_descartes.md).
2. **Respalda `_DES` antes de tocar nada**, si hay volumen relevante:

```sql
CREATE TABLE tmp_backup_<tabla>_des AS SELECT * FROM stg_s3.<TABLA>_DES;
```

3. **Compara contra el histórico** para dimensionar. Consulta de tendencia en [R1_11_consultas_descartes](../R1%20-%20Descartes/R1_11_consultas_descartes.md).
4. **Recupera un ejemplo concreto** de fila mala y mira el valor real frente a lo que se le exige.
5. **Determina si el dato o la regla es lo que cambió.** De eso depende a quién escalas.

## Cuándo escalar — y a quién

Escala **siempre** en estos casos, sin intentar arreglarlo desde base de datos:

| Situación | A quién |
|---|---|
| El fichero de origen cambió de estructura o contenido | Equipo funcional / proveedor del dato |
| Hay que modificar `PAR_MAESTRO_COLUMNAS_T`, `_MASK_T` o `_VALID_T` | Responsable del contrato de datos |
| El truncado ya ocurrió y hay que recargar | Equipo de operación, con la recarga coordinada |
| El XSD ya no corresponde al XML recibido | Equipo que gestiona la interfaz |

## Qué llevar al escalado

Sin estos cinco datos el ticket rebota:

- `cod_load_trace` y `cod_load_plan`
- Nombre de la tabla y de la interfaz
- Reparto por `des_validate` y `des_column_name` (la consulta del punto 3)
- Comparación con los 7 días anteriores
- Un ejemplo de fila concreta con el valor que falla y la regla que incumple

## Ver también

[R1_01_descarte_vs_error](../R1%20-%20Descartes/R1_01_descarte_vs_error.md) · [R1_09_reprocesar_descartes](../R1%20-%20Descartes/R1_09_reprocesar_descartes.md) · [R1_11_consultas_descartes](../R1%20-%20Descartes/R1_11_consultas_descartes.md) · [R1_10_descarte_correcto_sin_accion](../R1%20-%20Descartes/R1_10_descarte_correcto_sin_accion.md) · [R1_06_descarte_integridad_referencial](../R1%20-%20Descartes/R1_06_descarte_integridad_referencial.md)

---
titulo: "R1.03 — Identificar qué validación descartó la fila"
familia: R1
etapa: "Validación"
tipo: Runbook
tags:
  - familia/R1
  - etapa/validacion
  - tipo/runbook
keywords: "diagnóstico, des_validate, qué falló, validate_gen_pc, orden de validaciones"
---

# R1.03 — Identificar qué validación descartó la fila

**Etapa:** Validación
**Tipo:** Runbook
**Palabras clave:** diagnóstico, des_validate, qué falló, validate_gen_pc, orden de validaciones

## Síntoma

Hay filas apartadas y hay que averiguar por qué antes de decidir nada.

## Qué mirar primero

```sql
SELECT des_table_name, des_column_name, des_validate,
       des_row_number, dat_load_date
FROM   stg_s3.aud_load_valid_trace_t
WHERE  cod_load_trace = :trace
ORDER  BY des_row_number;
```

Tres columnas te dan el diagnóstico completo: **qué columna** (`des_column_name`), **qué regla**
(`des_validate`) y **qué fila del fichero** (`des_row_number`).

## Cómo interpretar `des_validate`

| Valor | Significado | Ficha |
|---|---|---|
| `NULOS` | Columna obligatoria vacía | [R1_04_descarte_nulo_obligatorio](../R1%20-%20Descartes/R1_04_descarte_nulo_obligatorio.md) |
| `FORMATO VAR` | Texto más largo que la longitud declarada | [R1_05_descarte_formato](../R1%20-%20Descartes/R1_05_descarte_formato.md) |
| `FORMATO NUM` | No cumple la expresión regular de la máscara | [R1_05_descarte_formato](../R1%20-%20Descartes/R1_05_descarte_formato.md) |
| `FORMATO LONG NUM` | Demasiados dígitos en la parte entera o decimal | [R1_05_descarte_formato](../R1%20-%20Descartes/R1_05_descarte_formato.md) |
| `FOREIGN_KEY` | El valor no existe en la tabla referenciada | [R1_06_descarte_integridad_referencial](../R1%20-%20Descartes/R1_06_descarte_integridad_referencial.md) |
| `FOREING_KEY_OLD` | Descarte de FK de un **ciclo anterior**, renombrado (sí, mal escrito) | [R1_02_donde_cae_cada_cosa](../R1%20-%20Descartes/R1_02_donde_cae_cada_cosa.md) |
| `DUPLICADOS` | Clave primaria repetida | [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md) |

## Qué validaciones corren realmente

Esto importa y contradice lo que suele suponerse. Dentro de `validate_gen_pc()` se ejecutan
**sólo tres**, en este orden:

```
1. VALIDATE_ROWS_NULL_FN        → nulos
2. VALIDATE_ROWS_FORMAT_ENT_FN  → formato (tres sub-comprobaciones)
3. VALIDATE_ROWS_FOREIGN_FN     → claves foráneas
```

`VALIDATE_ROWS_KEY_FN` (duplicados) y `VALIDATE_VARIATION_FN` (variación de volumen)
**no se invocan desde `validate_gen_pc`**. Existen y funcionan, pero se llaman desde otro sitio.
Si esperabas que una carga detectara duplicados automáticamente en esta etapa, no lo hace.
Ver [R1_07_descarte_variacion_volumen](../R1%20-%20Descartes/R1_07_descarte_variacion_volumen.md) y [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md).

## Causas probables, por orden

1. **El dato de origen cambió** — el proveedor empezó a mandar un campo vacío, más largo o con otro formato. Es la causa más frecuente.
2. **Falta el dato maestro referenciado** — la fila es correcta pero el catálogo al que apunta no se ha cargado todavía. Muy típico en `FOREIGN_KEY`: es un problema de **orden**, no de calidad.
3. **La parametrización está desalineada** — `PAR_MAESTRO_COLUMNAS_T` declara una longitud o una máscara que ya no corresponde al dato real.
4. **El fichero se convirtió mal** — un separador `!` dentro de un valor desplaza las columnas y todo falla a la vez. Señal: fallos masivos en columnas contiguas.

## Acción

- Si fallan **pocas filas** y son de negocio → traza al proveedor del dato.
- Si fallan **muchas filas de la misma columna** → sospecha de parametrización o de conversión, no del dato.
- Si fallan **columnas contiguas en muchas filas** → casi seguro es desplazamiento de columnas en la conversión.
- Si es `FOREIGN_KEY` y el catálogo llega después → candidato a reproceso, ver [R1_09_reprocesar_descartes](../R1%20-%20Descartes/R1_09_reprocesar_descartes.md).

## Cuándo escalar

Cuando el porcentaje de filas apartadas supere lo habitual para esa interfaz, o cuando falle una
columna que nunca fallaba: eso apunta a un cambio de contrato de datos y hay que avisar al equipo
que lo gestiona, no arreglarlo en base de datos. Ver [R1_12_descarte_masivo_escalado](../R1%20-%20Descartes/R1_12_descarte_masivo_escalado.md).

## Ver también

[R1_02_donde_cae_cada_cosa](../R1%20-%20Descartes/R1_02_donde_cae_cada_cosa.md) · [R1_01_descarte_vs_error](../R1%20-%20Descartes/R1_01_descarte_vs_error.md) · [R1_11_consultas_descartes](../R1%20-%20Descartes/R1_11_consultas_descartes.md)

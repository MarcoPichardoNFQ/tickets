---
titulo: "R1.04 — Descarte por nulo obligatorio"
familia: R1
etapa: "Validación"
tipo: Runbook
tags:
  - familia/R1
  - etapa/validacion
  - tipo/runbook
keywords: "NULOS, CHK_NULL, validate_rows_null_fn, obligatorio, vacío, tabla truncada"
---

# R1.04 — Descarte por nulo obligatorio

**Etapa:** Validación
**Tipo:** Runbook
**Palabras clave:** NULOS, CHK_NULL, validate_rows_null_fn, obligatorio, vacío, tabla truncada

## Síntoma

Filas en `TABLA_ERR`, y en la traza `des_validate = 'NULOS'`.

## Qué mirar primero

```sql
SELECT des_table_name, des_column_name, count(*) AS filas
FROM   stg_s3.aud_load_valid_trace_t
WHERE  des_validate = 'NULOS'
  AND  dat_load_date::date = CURRENT_DATE
GROUP  BY 1,2
ORDER  BY filas DESC;
```

## Cómo funciona

`validate_rows_null_fn()` recorre las columnas de la tabla que tienen `CHK_NULL = 1` en
`stg_s3.PAR_MAESTRO_COLUMNAS_T` y marca como nula toda fila donde la columna cumpla:

```sql
columna IS NULL  OR  columna = ''  OR  UPPER(columna) = 'NULL'
```

**Las tres condiciones cuentan.** Un campo que contenga el texto literal `null`, `NULL` o `Null`
se considera vacío, igual que la cadena vacía. Esto sorprende a menudo: el fichero «trae dato»
pero el dato es la palabra «NULL».

Si encuentra alguna, las registra en `AUD_LOAD_VALID_TRACE_T` con `des_validate = 'NULOS'` y
devuelve `1`. Después `validate_gen_pc()` decide qué hacer según `VALID_ERR_DES`:

- **Tolerante (`= 1`)**: `FN_LOAD_DATA_ERR` copia las filas a `TABLA_ERR`, las borra de la base, y **la carga continúa**.
- **Estricto (`≠ 1`)**: devuelve `-1` y la carga se detiene.

## ⚠ El mensaje de traza miente

Cuando hay nulos, la función escribe en `AUD_LOAD_TRACE_T`:

```
DES_PROCESS_EXECUTED = 'Error de Validacion de Nulos. Tabla Truncada'
```

**No se trunca ninguna tabla.** El texto está fijo en el código y se escribe siempre, incluso en
el flujo tolerante donde la carga sigue adelante sin problema. Si lees ese mensaje y concluyes que
perdiste la tabla, te estás asustando de más: comprueba el conteo real antes de actuar.

El truncado sí existe, pero es otra cosa: sólo ocurre en flujo estricto y sólo por fallo de clave
foránea. Ver [R1_01_descarte_vs_error](../R1%20-%20Descartes/R1_01_descarte_vs_error.md).

## Causas probables, por orden

1. **El origen dejó de informar un campo.** Cambio en el sistema emisor. Lo más común.
2. **El campo llega con el texto «NULL»** en vez de vacío. Distinto síntoma, misma causa raíz.
3. **La columna se declaró obligatoria y no lo es.** `CHK_NULL = 1` puesto de más en la parametrización.
4. **Desplazamiento de columnas en la conversión** — si un `!` viaja dentro de un valor, las columnas se corren y varias aparecen vacías a la vez.

## Acción

1. Mira cuántas columnas distintas fallan. **Una sola columna** → problema de dato. **Varias contiguas** → problema de conversión, ve a la familia `C`.
2. Recupera una fila concreta para verla:

```sql
SELECT * FROM stg_s3.<TABLA>_ERR
WHERE  cod_load_trace = :trace
LIMIT  10;
```

3. Si el campo es legítimamente opcional, la corrección es de parametrización: `CHK_NULL` en
   `PAR_MAESTRO_COLUMNAS_T`. **Eso no lo cambia BAU por su cuenta** — es un cambio de contrato de datos.

## Cuándo escalar

Siempre que la solución pase por tocar `PAR_MAESTRO_COLUMNAS_T`, o cuando falle una columna que
nunca había fallado: es un cambio en el origen y tiene que saberlo el equipo funcional.

## Ver también

[R1_03_identificar_validacion](../R1%20-%20Descartes/R1_03_identificar_validacion.md) · [R1_02_donde_cae_cada_cosa](../R1%20-%20Descartes/R1_02_donde_cae_cada_cosa.md) · [R1_01_descarte_vs_error](../R1%20-%20Descartes/R1_01_descarte_vs_error.md) · [R1_05_descarte_formato](../R1%20-%20Descartes/R1_05_descarte_formato.md)

---
titulo: "E01 — Las tablas `PAR_*`: el corazón metadata-driven"
familia: E
etapa: "Validación"
tipo: Referencia
tags:
  - familia/E
  - etapa/validacion
  - tipo/referencia
keywords: "PAR_, metadata-driven, parametrización, sin hardcodear, tablas maestras"
---

# E01 — Las tablas `PAR_*`: el corazón metadata-driven

**Etapa:** Validación
**Tipo:** Referencia
**Palabras clave:** PAR_, metadata-driven, parametrización, sin hardcodear, tablas maestras

## En una línea

El comportamiento del sistema no está en el código: está en seis tablas de `stg_s3` que empiezan
por `PAR_`. Cambiar una carga es cambiar filas, no scripts.

## Detalle

### El principio de diseño

La directiva del sistema es explícita: **está prohibido programar lógica de negocio en los scripts
bash**. Toda integración nueva se hace insertando registros en las tablas `PAR_*` y añadiendo
líneas a los ficheros `lookup_*.txt`.

Consecuencia práctica para soporte: cuando algo se comporta de forma inesperada, la explicación
casi nunca está en el código —que es genérico— sino en la fila de parametrización de esa interfaz.
**Empieza siempre por mirar la parametrización, no el procedimiento.**

### Las seis tablas

| Tabla | Gobierna |
|---|---|
| `PAR_LOAD_PLAN_T` | Cómo se carga cada fichero: origen, destino, separador, tolerancia a errores |
| `PAR_MAESTRO_TABLAS_T` | Catálogo de tablas participantes y su esquema |
| `PAR_MAESTRO_COLUMNAS_T` | Cada columna: tipo, longitud, decimales, máscara, si es clave, si es obligatoria |
| `PAR_MAESTRO_MASK_T` | Las máscaras de formato y sus expresiones regulares |
| `PAR_MAESTRO_VALID_T` | Las relaciones de integridad entre tablas |
| `PAR_MAESTRO_LOG_LEVEL_T` | El nivel de detalle de la traza |

### Cómo se encadenan

```
PAR_LOAD_PLAN_T ──cod_table──> PAR_MAESTRO_TABLAS_T
                                       │ cod_table
                                       ▼
                              PAR_MAESTRO_COLUMNAS_T ──cod_mask──> PAR_MAESTRO_MASK_T
                                       │
                                       │ (por nombre de tabla, con formato propio)
                                       ▼
                              PAR_MAESTRO_VALID_T
```

`cod_table` es la llave que une casi todo. `PAR_MAESTRO_VALID_T` es la excepción: se enlaza por
**nombre de tabla en un formato peculiar** —`'STG_S3.TABLA A'`— y no por código.
Ver [E05_par_maestro_valid_t](../E%20-%20Parametrizacion/E05_par_maestro_valid_t.md).

### Qué controla cada decisión del sistema

| Pregunta | Dónde está la respuesta |
|---|---|
| ¿Qué columnas se cargan y en qué orden? | `PAR_MAESTRO_COLUMNAS_T.cod_column` |
| ¿Qué campo es obligatorio? | `PAR_MAESTRO_COLUMNAS_T.chk_null` |
| ¿Qué campo es clave? | `PAR_MAESTRO_COLUMNAS_T.chk_clave` |
| ¿Qué formato debe tener? | `cod_mask` → `PAR_MAESTRO_MASK_T.des_reg_exp` |
| ¿Contra qué se valida su integridad? | `PAR_MAESTRO_VALID_T` |
| ¿Una fila mala aparta o aborta? | `PAR_LOAD_PLAN_T.valid_err_des` |
| ¿Cuánta traza se escribe? | `PAR_MAESTRO_LOG_LEVEL_T.cod_log_level` |

### Una consulta que resume una interfaz entera

Es la más útil de esta familia: te da todo el contrato de una tabla de un vistazo.

```sql
SELECT c.cod_column,
       c.des_column,
       c.data_type,
       c.data_length,
       c.amt_decimal,
       c.chk_null   AS obligatoria,
       c.chk_clave  AS es_clave,
       m.cod_mask,
       m.des_reg_exp
FROM   stg_s3.par_maestro_columnas_t c
JOIN   stg_s3.par_maestro_tablas_t   t ON t.cod_table = c.cod_table
LEFT   JOIN stg_s3.par_maestro_mask_t m ON m.cod_mask = c.cod_mask
WHERE  t.des_table = UPPER('<TABLA>')
ORDER  BY c.cod_column;
```

### Aviso

Modificar una tabla `PAR_*` cambia el comportamiento de la carga a partir de la siguiente
ejecución, sin necesidad de desplegar nada. Eso las hace cómodas y peligrosas a partes iguales:
**no son cambios de soporte**, son cambios de contrato de datos, y necesitan el mismo control que
un despliegue.

## Ver también

[E02_par_load_plan_t](../E%20-%20Parametrizacion/E02_par_load_plan_t.md) · [E03_par_maestro_tablas_columnas](../E%20-%20Parametrizacion/E03_par_maestro_tablas_columnas.md) · [E04_par_maestro_mask_t](../E%20-%20Parametrizacion/E04_par_maestro_mask_t.md) · [E05_par_maestro_valid_t](../E%20-%20Parametrizacion/E05_par_maestro_valid_t.md) · [A05_esquemas_base_de_datos](../A%20-%20Orientacion/A05_esquemas_base_de_datos.md)

---
titulo: "R1.01 — Qué es un descarte y en qué se diferencia de un error"
familia: R1
etapa: "Validación"
tipo: Referencia
tags:
  - familia/R1
  - etapa/validacion
  - tipo/referencia
keywords: "descarte, error, _DES, _ERR, VALID_ERR_DES, tolerante, estricto"
---

# R1.01 — Qué es un descarte y en qué se diferencia de un error

**Etapa:** Validación
**Tipo:** Referencia
**Palabras clave:** descarte, error, _DES, _ERR, VALID_ERR_DES, tolerante, estricto

## En una línea

Un descarte es una fila apartada que deja seguir al resto; un error detiene la carga. Cuál de las
dos ocurre depende de `VALID_ERR_DES` — y **hoy, en producción, todas las cargas están en el modo
tolerante**.

## ✅ Verificado en producción

```sql
SELECT p.cod_load_plan, t.des_table, p.valid_err_des
FROM   stg_s3.par_load_plan_t p
LEFT   JOIN stg_s3.par_maestro_tablas_t t ON t.cod_table = p.cod_table
WHERE  p.valid_err_des IS DISTINCT FROM 1;
```

**Devuelve cero filas.** Ninguna carga está en flujo estricto. El comportamiento real del sistema
es siempre: apartar la fila mala y continuar.

Lo que sigue describe el flujo estricto porque **está en el código y basta cambiar una columna para
activarlo** — y porque explica por qué existen ciertas ramas en los procedimientos. Pero como
diagnóstico de una incidencia de hoy, **empieza asumiendo el flujo tolerante**.

## Detalle

### El interruptor que lo decide todo

`stg_s3.PAR_LOAD_PLAN_T` tiene una columna `VALID_ERR_DES` (valor por defecto `1`). El
procedimiento `validate_gen_pc()` la lee al empezar y a partir de ahí sigue **dos caminos
completamente distintos**:

| | `VALID_ERR_DES = 1` (tolerante) | `VALID_ERR_DES ≠ 1` (estricto) |
|---|---|---|
| Fallo de **nulos** | Filas malas → `_ERR`. La carga **continúa**. | Aborta. `PO_VALID_RESULT = -1`. |
| Fallo de **formato** | Se registra. La carga **continúa**. | Aborta. `PO_VALID_RESULT = -1`. |
| Fallo de **clave foránea** | Filas malas → `_DES`. La carga **continúa**. | **`TRUNCATE` de la tabla entera** y aborta. |

Esto es lo primero que hay que mirar ante cualquier incidencia de descartes. La misma fila mala,
en el mismo fichero, produce «se apartaron 12 filas» o «se perdió el fichero completo» según el
valor de esa columna.

### El caso que más daño hace

En flujo estricto, un fallo de integridad referencial ejecuta:

```sql
truncate table stg_s3.<TABLA>
```

No es un descarte de las filas malas: **vacía la tabla de destino completa**. Si te encuentras una
tabla `_T` inesperadamente a cero después de una carga, comprueba el `VALID_ERR_DES` de su plan.

### Vocabulario, entonces

- **Descarte** — fila apartada a `_DES` por integridad referencial. El fichero se carga igual.
- **Error** — fila apartada a `_ERR` por nulos. En flujo tolerante el fichero también se carga.
- **Aborto** — el flujo estricto se detiene y devuelve `-1`. Aquí no hay filas apartadas: no entra nada.

La distinción `_ERR` / `_DES` es **por tipo de validación**, no por gravedad.
Ver [R1_02_donde_cae_cada_cosa](../R1%20-%20Descartes/R1_02_donde_cae_cada_cosa.md).

### Por qué el sistema es tolerante por defecto

`VALID_ERR_DES` tiene `DEFAULT 1`. La intención de diseño es que una fila mala no bloquee el
lote diario: se aparta, se deja traza y el negocio recibe el resto. Un fichero que se pierde
entero por una fila mala es peor que un fichero al que le faltan tres filas registradas.

## Cómo verificarlo

```sql
-- ¿Esta carga es tolerante o estricta?
SELECT cod_load_plan, des_procedure_run, valid_err_des,
       CASE WHEN valid_err_des = 1 THEN 'TOLERANTE: aparta filas'
            ELSE 'ESTRICTO: aborta, y FK trunca la tabla' END AS comportamiento
FROM   stg_s3.par_load_plan_t
ORDER  BY valid_err_des, cod_load_plan;
```

## Ver también

[R1_02_donde_cae_cada_cosa](../R1%20-%20Descartes/R1_02_donde_cae_cada_cosa.md) · [R1_03_identificar_validacion](../R1%20-%20Descartes/R1_03_identificar_validacion.md) · [R1_10_descarte_correcto_sin_accion](../R1%20-%20Descartes/R1_10_descarte_correcto_sin_accion.md) · [R1_12_descarte_masivo_escalado](../R1%20-%20Descartes/R1_12_descarte_masivo_escalado.md)

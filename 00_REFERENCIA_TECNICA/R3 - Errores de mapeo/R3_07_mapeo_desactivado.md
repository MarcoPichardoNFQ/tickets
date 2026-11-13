---
titulo: "R3.07 — El mapeo está desactivado a propósito"
familia: R3
etapa: "Mapeos"
tipo: Runbook
tags:
  - familia/R3
  - etapa/mapeos
  - tipo/runbook
keywords: "activo_inactivo false, desactivado, no es incidencia, cerrar ticket, decisión funcional"
---

# R3.07 — El mapeo está desactivado a propósito

**Etapa:** Mapeos
**Tipo:** Runbook
**Palabras clave:** activo_inactivo false, desactivado, no es incidencia, cerrar ticket, decisión funcional

## Síntoma

Una tabla de salida no se actualiza. El job de Rundeck sale en verde. No hay errores.

## La comprobación

```sql
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio, activo_inactivo, is_fromtis
FROM   exp_s3.tablas_mapeio_t
WHERE  nome_tabela_aldrin ILIKE '%<TABLA>%';
```

`activo_inactivo = false` → **el mapeo está apagado deliberadamente.** No es un fallo técnico.

## Por qué el job sale en verde

El job invoca el procedimiento; el procedimiento consulta la tabla de control y, si el mapeo está
inactivo, no hace nada y termina correctamente. Desde Rundeck es indistinguible de una ejecución que
sí trabajó.

Es la razón por la que **un job verde no prueba que la tabla se haya actualizado**, y por la que
esta comprobación va la primera en el diagnóstico. Ver [R3_01_anatomia_fallo_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_01_anatomia_fallo_mapeo.md).

## El caso parcial, más difícil de ver

La clave primaria de la tabla de control es `(nome_tabela_aldrin, nome_fn_mapeio)`: **un mismo
`id_mapeo` puede tener varias funciones, cada una con su propio interruptor**.

```sql
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio, activo_inactivo
FROM   exp_s3.tablas_mapeio_t
WHERE  id_mapeo = :id
ORDER  BY nome_fn_mapeio;
```

Si una tabla se construye en dos fases y la segunda está desactivada, **el destino queda a medias**:
con datos, pero incompletos. Ese caso no se detecta comprobando si la tabla está vacía, y es de los
que más cuesta diagnosticar.

## Qué hacer

**No lo reactives.** `activo_inactivo` no es un parámetro técnico: refleja una decisión de negocio.
Alguien lo apagó por una razón, y reactivarlo puede repoblar una tabla que se quería congelada.

La respuesta correcta al ticket es informativa:

> El mapeo `<id> <nombre>` está desactivado en `exp_s3.tablas_mapeio_t`. La tabla no se actualiza
> por diseño, no por un fallo. Reactivarlo requiere validación funcional.

Y después, escalar la pregunta a quien pueda responderla: **¿debería seguir apagado?**

## Cómo saber desde cuándo

La tabla de control no guarda fecha de modificación. La forma indirecta de estimarlo es mirar la
última actualización del destino:

```sql
-- Si la tabla destino tiene columna de fecha
SELECT max(<col_fecha>) FROM trf_s3.<TABLA_DESTINO>;
```

Esa fecha es una buena aproximación de cuándo dejó de correr, y suele ser el dato que más interesa a
quien reporta la incidencia.

## Ten la lista preparada

Merece la pena revisar de vez en cuando qué hay apagado, porque es la respuesta anticipada a varios
tickets:

```sql
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio
FROM   exp_s3.tablas_mapeio_t
WHERE  NOT activo_inactivo
ORDER  BY id_mapeo;
```

Y los mapeos parcialmente activos, que son los que dan diagnósticos confusos:

```sql
SELECT id_mapeo,
       count(*)                                  AS funciones,
       count(*) FILTER (WHERE activo_inactivo)   AS activas
FROM   exp_s3.tablas_mapeio_t
GROUP  BY 1
HAVING count(*) FILTER (WHERE activo_inactivo) BETWEEN 1 AND count(*) - 1
ORDER  BY 1;
```

## Ver también

[G02_tablas_mapeio_activo](../G%20-%20Mapeos/G02_tablas_mapeio_activo.md) · [R3_01_anatomia_fallo_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_01_anatomia_fallo_mapeo.md) · [R1_10_descarte_correcto_sin_accion](../R1%20-%20Descartes/R1_10_descarte_correcto_sin_accion.md) · [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md)

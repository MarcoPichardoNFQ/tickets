---
titulo: "G02 — `tablas_mapeio_t.activo_inactivo`: el interruptor real"
familia: G
etapa: "Mapeos"
tipo: Referencia
tags:
  - familia/G
  - etapa/mapeos
  - tipo/referencia
keywords: "activo_inactivo, desactivado, no corre, interruptor, is_fromtis, retry_deadlock"
---

# G02 — `tablas_mapeio_t.activo_inactivo`: el interruptor real

**Etapa:** Mapeos
**Tipo:** Referencia
**Palabras clave:** activo_inactivo, desactivado, no corre, interruptor, is_fromtis, retry_deadlock

## En una línea

Un mapeo puede estar apagado en base de datos aunque su job exista y se ejecute en Rundeck — y ésa
es la primera comprobación ante «esta tabla no se actualiza».

## La columna

```sql
activo_inactivo bool DEFAULT true NOT NULL
```

`true` = el mapeo se ejecuta. `false` = no se ejecuta, aunque todo lo demás esté en su sitio.

**El job de Rundeck puede correr y salir en verde con el mapeo desactivado.** El job invoca el
procedimiento, y éste comprueba la tabla de control antes de hacer nada. Desde fuera parece que se
ejecutó.

Por eso, ante «la tabla de salida X no se actualiza», el orden correcto es:

```sql
-- 1. ¿Está activo?
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio, activo_inactivo, is_fromtis
FROM   exp_s3.tablas_mapeio_t
WHERE  nome_tabela_aldrin ILIKE '%<TABLA>%';
```

Si `activo_inactivo` es `false`, **no es una incidencia técnica**: alguien lo apagó a propósito.
La conversación es con negocio, no con soporte. Ver [R1_10_descarte_correcto_sin_accion](../R1%20-%20Descartes/R1_10_descarte_correcto_sin_accion.md).

## Las otras columnas de control

### `retry_deadlock` y `wait_deadlock_seconds`

Configuran el reintento ante bloqueo mutuo, **por mapeo**:

```sql
SELECT id_mapeo, nome_fn_mapeio, retry_deadlock, wait_deadlock_seconds
FROM   exp_s3.tablas_mapeio_t
WHERE  activo_inactivo
ORDER  BY retry_deadlock DESC NULLS LAST;
```

Un mapeo con `retry_deadlock` nulo o a cero **no reintenta**: al primer bloqueo, falla. Los que
tocan tablas muy disputadas suelen tener valores altos. Ver [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md).

### `is_fromtis`

Marca de origen, de un solo carácter. Interviene en la selección de qué mapeos se despachan, junto
con `activo_inactivo` — de hecho hay un índice sobre las tres columnas a la vez:

```sql
idx_tablas_mapeio_t_id_mapeo_activo_isfromtis ON (id_mapeo, activo_inactivo, is_fromtis)
```

Que exista ese índice indica que la consulta de despacho filtra por las tres. **Un mapeo puede
quedar fuera del despacho por su valor de `is_fromtis` aunque esté activo.** Si un mapeo está
activo y aun así no corre nunca, mira esta columna:

```sql
SELECT is_fromtis, count(*), count(*) FILTER (WHERE activo_inactivo) AS activos
FROM   exp_s3.tablas_mapeio_t
GROUP  BY 1;
```

Compara el valor del mapeo problemático con el de los mapeos que sí se ejecutan a diario.

## Varias funciones por mapeo

La clave primaria es `(nome_tabela_aldrin, nome_fn_mapeio)`, no `id_mapeo`. Un mismo `id_mapeo`
puede tener **varias funciones**, y cada una tiene su propio `activo_inactivo`.

```sql
-- Mapeos con más de una función
SELECT id_mapeo, count(*) AS funciones,
       count(*) FILTER (WHERE activo_inactivo) AS activas
FROM   exp_s3.tablas_mapeio_t
GROUP  BY 1
HAVING count(*) > 1
ORDER  BY 2 DESC;
```

Una tabla de salida que se construye en dos fases y tiene la segunda desactivada queda **a medias**:
con datos, pero incompletos. Es de los diagnósticos más difíciles, porque la tabla no está vacía.

## Antes de cambiar nada

`activo_inactivo` es una columna que cambia el comportamiento del sistema en la siguiente ejecución,
sin desplegar nada. **Activar o desactivar un mapeo no es una acción de soporte**: es una decisión
funcional. Si hay que hacerlo, que quede en el ticket quién lo pidió y por qué.

## Cómo verificarlo

```sql
-- Foto del control de mapeos
SELECT activo_inactivo, is_fromtis, count(*)
FROM   exp_s3.tablas_mapeio_t
GROUP  BY 1,2 ORDER BY 1,2;

-- Los desactivados, por si alguien pregunta por ellos
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio
FROM   exp_s3.tablas_mapeio_t
WHERE  NOT activo_inactivo
ORDER  BY id_mapeo;
```

Esa última lista conviene tenerla revisada: es la respuesta preparada a «¿por qué no tengo datos
de X?».

## Ver también

[G01_que_es_un_mapeo](../G%20-%20Mapeos/G01_que_es_un_mapeo.md) · [R3_07_mapeo_desactivado](../R3%20-%20Errores%20de%20mapeo/R3_07_mapeo_desactivado.md) · [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md) · [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md)

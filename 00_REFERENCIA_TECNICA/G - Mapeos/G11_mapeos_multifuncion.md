---
titulo: "G11 — Mapeos multi-función: fases sobre la misma tabla"
familia: G
etapa: "Mapeos"
tipo: Referencia
tags:
  - familia/G
  - etapa/mapeos
  - tipo/referencia
keywords: "multi-función, fases, control_carga, contador, tabla a medias, orden"
---

# G11 — Mapeos multi-función: fases sobre la misma tabla

**Etapa:** Mapeos
**Tipo:** Referencia
**Palabras clave:** multi-función, fases, control_carga, contador, tabla a medias, orden

## En una línea

122 funciones para 74 tablas destino: **muchos mapeos se construyen en varias fases**, y una fase
apagada deja la tabla a medias sin que nada lo señale.

## Los números

| | |
|---|---|
| `id_mapeo` distintos | 74 |
| Tablas destino distintas | 74 — **relación 1:1** |
| Funciones declaradas | 122 |
| Media de funciones por mapeo | 1,65 |

Los casos extremos se ven en los nombres: `function_meg_cart_caixa_cpr_t` tiene 15 variantes
numeradas (`t2`, `t3`, `t4`, `t8`…`t18`), y `sac_stat_bas_cad_if_t` otras 15.

```sql
-- Mapeos con más de una función
SELECT id_mapeo, nome_tabela_aldrin,
       count(*)                                AS funciones,
       count(*) FILTER (WHERE activo_inactivo) AS activas
FROM   exp_s3.tablas_mapeio_t
GROUP  BY 1,2 HAVING count(*) > 1
ORDER  BY 3 DESC;
```

## Cómo se ejecutan

El despacho abre un cursor sobre **todas** las funciones activas de ese `id_mapeo` y las recorre en
bucle:

```sql
OPEN C_MAPEIO_CUR FOR
SELECT nome_tabela_aldrin, nome_fn_mapeio, retry_deadlock, wait_deadlock_seconds
FROM   exp_s3.tablas_mapeio_t
WHERE  is_fromtis = 'N' AND activo_inactivo = TRUE AND id_mapeo = v_id_mapeo;
```

**El orden lo decide PostgreSQL**, no hay `ORDER BY`. Si las fases dependen unas de otras, el orden
no está garantizado por la consulta.

## El contador es lo que las ata

`control_mapeio_t.control_carga` se inicializa con **el número de funciones de esa tabla** y baja
una por cada función completada:

```sql
UPDATE exp_s3.control_mapeio_t
SET    control_carga = control_carga - 1, data_fim_upload = NOW()
WHERE  tabela_carga = v_nome_tabela_aldrin AND control_carga <> 0 AND id = v_id;
```

Cuando llega a `0`, la tabla se considera terminada y **las llamadas posteriores se saltan**.

Ver [G08_fim_carga_mapeo](../G%20-%20Mapeos/G08_fim_carga_mapeo.md).

## ⚠ El caso que cuesta diagnosticar: la tabla a medias

Cada función tiene **su propio `activo_inactivo`**. Si un mapeo tiene tres fases y una está apagada:

- La tabla **sí tiene datos** — las otras dos fases corrieron
- **No hay error** en ninguna parte
- El job sale en verde
- Y el contenido está incompleto

Comprobar si la tabla está vacía no sirve: no lo está. La comprobación correcta es el estado de
**todas** las funciones:

```sql
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio, activo_inactivo, retry_deadlock
FROM   exp_s3.tablas_mapeio_t
WHERE  lower(nome_tabela_aldrin) = lower('<TABLA>')
ORDER  BY nome_fn_mapeio;
```

Y la lista de todos los que están parcialmente activos, que conviene tener revisada:

```sql
SELECT id_mapeo, nome_tabela_aldrin,
       count(*)                                AS funciones,
       count(*) FILTER (WHERE activo_inactivo) AS activas
FROM   exp_s3.tablas_mapeio_t
GROUP  BY 1,2
HAVING count(*) FILTER (WHERE activo_inactivo) BETWEEN 1 AND count(*) - 1
ORDER  BY 1;
```

## El segundo caso silencioso: `retry_deadlock` NULL

Se combina mal con lo anterior. Una fase con `retry_deadlock` NULL **no se ejecuta** —el bucle
`WHILE 0 < NULL` no entra nunca— **y aun así decrementa el contador** como si hubiera terminado.

Resultado: la tabla queda incompleta, el contador dice que está completa, y no hay error.

```sql
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio
FROM   exp_s3.tablas_mapeio_t
WHERE  activo_inactivo AND is_fromtis = 'N' AND retry_deadlock IS NULL
ORDER  BY id_mapeo;
```

Todo lo que devuelva esa consulta son fases que no se ejecutan. Ver [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md).

## Al relanzar un mapeo multi-función

Relanzar el job ejecuta **todas** sus funciones activas, no una sola. Y si el contador ya está a
cero, ninguna. Ver [R3_11_relanzar_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_11_relanzar_mapeo.md).

## Ver también

[G08_fim_carga_mapeo](../G%20-%20Mapeos/G08_fim_carga_mapeo.md) · [G02_tablas_mapeio_activo](../G%20-%20Mapeos/G02_tablas_mapeio_activo.md) · [R3_07_mapeo_desactivado](../R3%20-%20Errores%20de%20mapeo/R3_07_mapeo_desactivado.md) · [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md) · [G06_catalogo_mapeos](../G%20-%20Mapeos/G06_catalogo_mapeos.md)

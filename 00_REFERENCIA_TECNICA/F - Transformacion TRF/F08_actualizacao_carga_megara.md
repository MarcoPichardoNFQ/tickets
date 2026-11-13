---
titulo: "F08 — `actualizacao_carga_megara` y las marcas `ic_qlik_read`"
familia: F
etapa: "Transformación TRF"
tipo: Referencia
tags:
  - familia/F
  - etapa/transformacion-trf
  - tipo/referencia
keywords: "ic_qlik_read, s3_carga_megara, marca de lectura, actualizacao, primera, segunda"
---

# F08 — `actualizacao_carga_megara` y las marcas `ic_qlik_read`

**Etapa:** Transformación TRF
**Tipo:** Referencia
**Palabras clave:** ic_qlik_read, s3_carga_megara, marca de lectura, actualizacao, primera, segunda

## En una línea

Dos funciones de una línea que marcan filas como «pendientes de leer por Qlik» poniendo a `'0'` lo
que estaba en NULL.

## Qué hacen

```sql
CREATE FUNCTION trf_s3.actualizacao_carga_megara_primera() RETURNS void
LANGUAGE sql AS $$
    UPDATE trf_s3.s3_carga_megara
    SET    ic_qlik_read = '0'
    WHERE  ic_qlik_read IS NULL
$$;
```

La variante `_segunda` hace lo mismo sobre su propia tabla. Y en `exp_s3` existe un par gemelo,
`actualizacao_icqlikread_extracao_carga_primera` / `_segunda`, que actúa sobre
`trf_s3.s3_fundo_extracao_carga`.

Cuatro funciones, la misma operación: **normalizar NULL a `'0'` en una columna de marca**.

## El significado de `ic_qlik_read`

Es un indicador de tres estados:

| Valor | Significado |
|---|---|
| `NULL` | Recién insertado, sin marcar |
| `'0'` | **Pendiente de leer por Qlik** |
| Otro valor | Ya procesado |

Las funciones convierten el primer estado en el segundo. Es decir: **hacen visible para Qlik lo que
acaba de entrar**.

Sin esa normalización, las filas nuevas quedarían en un estado indeterminado que las consultas
posteriores podrían no recoger.

## Cuándo importa en un diagnóstico

Ante «el dato está en la tabla pero Qlik no lo coge», además de las comprobaciones habituales,
mira si quedaron filas sin marcar:

```sql
SELECT ic_qlik_read, count(*)
FROM   trf_s3.s3_carga_megara
GROUP  BY 1 ORDER BY 2 DESC;
```

Un número alto de `NULL` significa que la normalización no se ejecutó en ese ciclo.

Lo mismo para la tabla de extracción:

```sql
SELECT ic_qlik_read, count(*)
FROM   trf_s3.s3_fundo_extracao_carga
GROUP  BY 1;
```

## ⚠ Las dos de `exp_s3` no tienen llamador localizado

`actualizacao_icqlikread_extracao_carga_primera` y `_segunda` no aparecen invocadas desde ningún
job, script ni procedimiento del material disponible. Están entre las 18 funciones de `exp_s3` sin
llamador confirmado. Ver [G10_codigo_sin_llamadas](../G%20-%20Mapeos/G10_codigo_sin_llamadas.md).

Antes de asumir que `s3_fundo_extracao_carga` se está normalizando, comprueba si las filas en NULL
se acumulan con el tiempo:

```sql
SELECT ic_qlik_read, count(*), min(dat_carga), max(dat_carga)
FROM   trf_s3.s3_fundo_extracao_carga
GROUP  BY 1;
```

Si los `NULL` incluyen fechas antiguas, nadie las está normalizando.

## Ver también

[G10_codigo_sin_llamadas](../G%20-%20Mapeos/G10_codigo_sin_llamadas.md) · [F01_que_hace_la_capa_trf](../F%20-%20Transformacion%20TRF/F01_que_hace_la_capa_trf.md) · [H09_qlik_datos_de_ayer](../H%20-%20Cierre%20y%20Qlik/H09_qlik_datos_de_ayer.md) · [I18_columnas_comunes](../I%20-%20Referencia%20de%20datos/I18_columnas_comunes.md)

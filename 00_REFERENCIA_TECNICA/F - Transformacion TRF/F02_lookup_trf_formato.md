---
titulo: "F02 — `lookup_trf.txt`: formato y cómo leerlo"
familia: F
etapa: "Transformación TRF"
tipo: Referencia
tags:
  - familia/F
  - etapa/transformacion-trf
  - tipo/referencia
keywords: "lookup_trf, formato, procedimiento, parámetros, id"
---

# F02 — `lookup_trf.txt`: formato y cómo leerlo

**Etapa:** Transformación TRF
**Tipo:** Referencia
**Palabras clave:** lookup_trf, formato, procedimiento, parámetros, id

## En una línea

Cada línea asocia un identificador con **el procedimiento y sus parámetros, escritos tal cual se
van a ejecutar**.

## Formato

```
|id|esquema.procedimiento(parámetros)|[tabla_origen]
```

```
|1|trf_s3.load_carteira_receitas(0,60)|
|2|trf_s3.load_carteira_rebates(0,60)|
|4|trf_s3.load_fund_carteira_bulle(0)|
|5|trf_s3.load_mt_caixa(0)|SAC_CAIXA_MT_T
|6|trf_s3.load_cpr_caixa(0)|SAC_CAIXA_CPR_T
```

| Campo | Contenido |
|---|---|
| 2 | **id** — el valor que aparece en los `scriptargs` de los pasos de bloque |
| 3 | **Procedimiento con parámetros**, literal. Es lo que se mete en el `call` |
| 4 | Tabla de origen. Informativo, no siempre presente |

El fichero tiene **582 líneas**.

## Cómo lo usa el script

```bash
procedimiento=`grep '|'$valor'|' $lookup_trf | cut -d '|' -f 3 | tr -d '\n'`
sql="call "$procedimiento" ;"
V_OUT=$($DB_CONN -c "$sql")
```

El campo 3 se inserta **literalmente** en el `call`. No hay validación: si la línea está mal escrita,
el error aparece como sintaxis SQL, no como problema de configuración.

## Los parámetros van escritos en el lookup

`trf_s3.load_carteira_receitas(0,60)` se ejecuta exactamente así. El primer parámetro suele ser un
código de proceso y el segundo, cuando existe, un valor de negocio.

Consecuencia: **para cambiar un parámetro de una transformación se edita este fichero**, no el
procedimiento. Y como el `grep` busca `|<id>|`, un id que aparezca como subcadena en otro sitio
delimitado por barras devuelve varias líneas que se concatenan. Comprobación:

```bash
grep -c '|5|' /nfq/data/cfg/lookup_trf.txt   # debería ser 1
```

## Búsquedas útiles

```bash
# Qué procedimiento ejecuta un paso
grep '|<id>|' /nfq/data/cfg/lookup_trf.txt | cut -d'|' -f3

# Qué paso alimenta una tabla
grep -i "<TABLA>" /nfq/data/cfg/lookup_trf.txt

# Todas las transformaciones de una familia
grep -i "trf_s3.load_" /nfq/data/cfg/lookup_trf.txt
grep -i "trf_s3.cs_"   /nfq/data/cfg/lookup_trf.txt
```

## La relación con los bloques

Cada paso de un bloque pasa **un par de valores**: el primero es el id de `lookup_stg.txt` y el
segundo el de `lookup_trf.txt`.

```
<scriptargs>159,124</scriptargs>
   159 → carga    (lookup_stg,  posición impar)
   124 → transforma (lookup_trf, posición par)
```

Ver [F03_funcion_trf](../F%20-%20Transformacion%20TRF/F03_funcion_trf.md) y [D07_bloques_optimizacio](../D%20-%20Carga%20STG/D07_bloques_optimizacio.md).

## Ver también

[F01_que_hace_la_capa_trf](../F%20-%20Transformacion%20TRF/F01_que_hace_la_capa_trf.md) · [F03_funcion_trf](../F%20-%20Transformacion%20TRF/F03_funcion_trf.md) · [D02_lookup_stg_formato](../D%20-%20Carga%20STG/D02_lookup_stg_formato.md) · [F05_familias_procedimientos](../F%20-%20Transformacion%20TRF/F05_familias_procedimientos.md)

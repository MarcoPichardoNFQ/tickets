---
titulo: "F03 — La función `trf()` y el truco de los índices pares"
familia: F
etapa: "Transformación TRF"
tipo: Referencia
tags:
  - familia/F
  - etapa/transformacion-trf
  - tipo/referencia
keywords: "trf, índices pares, posición, lista de argumentos, desalineación"
---

# F03 — La función `trf()` y el truco de los índices pares

**Etapa:** Transformación TRF
**Tipo:** Referencia
**Palabras clave:** trf, índices pares, posición, lista de argumentos, desalineación

## En una línea

La transformación se ejecuta cuando el valor ocupa una **posición par** en la lista de argumentos —
no por lo que valga el número.

## La función

```bash
trf(){
    lookup_trf="/nfq/data/cfg/lookup_trf.txt"
    local valor=$1
    procedimiento=`grep '|'$valor'|' $lookup_trf | cut -d '|' -f 3 | tr -d '\n'`
    sql="call "$procedimiento" ;"
    V_OUT=$($DB_CONN -c "$sql")
    if [ "$V_OUT" != "0" ]; then
        flag_error_gral=1
        echo "error en " $procedimiento
    fi
}
```

Cuatro líneas útiles: busca, construye el `call`, ejecuta, y compara la salida con `"0"`.

## La regla de posición

```bash
for i in "${!array[@]}"; do
    indice=$((i + 1))
    if ((indice % 2 != 0)); then  stg "$valor" & wait   # IMPAR → carga
    else                          trf "$valor"          # PAR   → transformación
    fi
done
```

**Lo que decide es la posición, no el número.** El mismo valor `17` es una carga en primera posición
y una transformación en segunda. Por eso las listas repiten cada valor: `17,17` significa «carga la
17, transforma la 17».

## ⚠ El riesgo: la desalineación

Si alguien añade o quita un elemento de la lista de un bloque, **todo lo que va detrás cambia de
significado**. Un valor que era carga pasa a ser transformación y viceversa.

Síntomas de una lista desalineada:

- Un `call` a un procedimiento que no existe — porque el id venía de `lookup_stg`
- Una carga que busca un fichero con nombre absurdo — porque el id venía de `lookup_trf`
- Errores de sintaxis SQL sin explicación aparente

Comprobación: **la lista tiene que tener un número par de elementos.**

```bash
echo "159,124,160,125,161,126" | tr ',' '\n' | wc -l   # par = bien
```

En Rundeck, los `scriptargs` de cada paso de bloque son pares `<stg>,<trf>`. Ver [D07_bloques_optimizacio](../D%20-%20Carga%20STG/D07_bloques_optimizacio.md).

## La detección de errores

```bash
if [ "$V_OUT" != "0" ]; then flag_error_gral=1; fi
```

La conexión está definida con `-t -A`, así que la salida viene sin formato. Pero para que la
comparación dé «correcto», el procedimiento tiene que devolver literalmente `0`:

- Con parámetro de salida que valga `0` → la comparación acierta
- Sin parámetro de salida → `psql` emite la etiqueta `CALL`, que **no es `"0"`** → se marca error

**El indicador depende de la firma del procedimiento, no de si la transformación fue bien.**
Juzga por los datos y las trazas. Ver [F01_que_hace_la_capa_trf](../F%20-%20Transformacion%20TRF/F01_que_hace_la_capa_trf.md) y [R5_07_alerta_vs_estado_real](../R5%20-%20Alertas%20Rundeck/R5_07_alerta_vs_estado_real.md).

## Los errores no detienen el bucle

Los `exit` del script están comentados. Un fallo sólo marca `flag_error_gral=1` y **el bloque sigue
con el resto de la lista**. Que acabe en rojo no dice dónde se paró: no se paró.
Ver [D03_script_stg_trf](../D%20-%20Carga%20STG/D03_script_stg_trf.md).

## Ver también

[F02_lookup_trf_formato](../F%20-%20Transformacion%20TRF/F02_lookup_trf_formato.md) · [D03_script_stg_trf](../D%20-%20Carga%20STG/D03_script_stg_trf.md) · [D07_bloques_optimizacio](../D%20-%20Carga%20STG/D07_bloques_optimizacio.md) · [F10_localizar_fallo_trf](../F%20-%20Transformacion%20TRF/F10_localizar_fallo_trf.md)

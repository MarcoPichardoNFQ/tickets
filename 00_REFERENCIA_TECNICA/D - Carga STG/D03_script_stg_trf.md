---
titulo: "D03 — `load_stgtrf_script.sh`: `stg()`, `trf()` y el truco de los índices"
familia: D
etapa: "Carga STG"
tipo: Referencia
tags:
  - familia/D
  - etapa/carga-stg
  - tipo/referencia
keywords: "load_stgtrf_script, stg, trf, impares, pares, DB_CONN, script de carga"
---

# D03 — `load_stgtrf_script.sh`: `stg()`, `trf()` y el truco de los índices

**Etapa:** Carga STG
**Tipo:** Referencia
**Palabras clave:** load_stgtrf_script, stg, trf, impares, pares, DB_CONN, script de carga

## En una línea

Un único script hace carga y transformación: recibe una lista de números y decide por **posición**
—impar o par— si ese número es una carga a staging o un procedimiento de transformación.

## Detalle

### El truco de los índices

El script recibe un único argumento: una lista separada por comas.

```bash
./load_stgtrf_script.sh "17,17,18,18,19,19"
```

Y recorre la lista aplicando esta regla:

```bash
for i in "${!array[@]}"; do
    indice=$((i + 1))
    if ((indice % 2 != 0)); then
        stg "$valor" &     # posición IMPAR → carga a staging
        wait
    else
        trf "$valor"       # posición PAR   → transformación
    fi
done
```

**Lo que decide no es el número, es su posición en la lista.** El mismo valor `17` es una carga si
va en primera posición y una transformación si va en segunda. Por eso las listas reales repiten
cada valor: `17,17` significa «carga la 17, luego transforma la 17».

Consecuencia para diagnóstico: si alguien edita la lista de un bloque y añade o quita un elemento,
**todo lo que va detrás cambia de significado**. Una lista con un número impar de elementos
desalinea el resto.

### `stg(valor)` — qué hace

1. Busca la línea `|valor|` en `lookup_stg.txt` y extrae tabla, patrón, ruta, separador y opciones.
2. Comprueba si la tabla `_des` tiene descartes pendientes.
3. Busca el fichero: `ls -ltr $raiz$fichero`, excluyendo los que ya llevan `_InLoad`, y coge el primero.
4. Si **no hay fichero y no hay descartes** → «PASO OMITIDO». Ver [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md).
5. Renombra el fichero a `<nombre>_InLoad.csv`.
6. Llama a `READ_HEADER_FN` para obtener la lista de columnas.
7. Ejecuta el `\COPY` y a continuación `RUN_LOAD_PLAN_PC`.
8. Si todo fue bien: cifra con GPG, archiva y borra el original. Ver [D08_gpg_historificacion](../D%20-%20Carga%20STG/D08_gpg_historificacion.md).

### `trf(valor)` — qué hace

1. Busca la línea `|valor|` en `lookup_trf.txt` y extrae el campo 3: el procedimiento con sus parámetros.
2. Ejecuta `call <procedimiento>;`.
3. Si la salida **no es exactamente `0`**, marca error.

Formato de `lookup_trf.txt`:

```
|1|trf_s3.load_carteira_receitas(0,60)|
|5|trf_s3.load_mt_caixa(0)|SAC_CAIXA_MT_T
```

### Tres comportamientos que conviene conocer

**Los errores no detienen el bucle.** Todas las llamadas a `exit` dentro de las funciones están
comentadas en el código. Un fallo sólo pone `flag_error_gral=1` y el bucle **sigue con el resto de
la lista**. El script devuelve error al final, pero para entonces ya ejecutó todo. Que un bloque
termine en rojo no significa que se parara en el primer fallo.

**El `&` seguido de `wait` no paraleliza nada.** `stg "$valor" & wait` lanza en segundo plano y
espera inmediatamente. Es equivalente a llamarla directamente.

**El nombre temporal siempre acaba en `.csv`.** El script construye
`nom_process="${select}_InLoad.csv"` con la extensión fija, aunque el fichero original sea `.txt`.
No suele dar problema, pero si buscas un fichero en curso por su extensión original no lo vas a
encontrar.

### Dependencias del script

```bash
. /nfq/data/cfg/env.properties       # rutas
. /nfq/data/cfg/db_config_gral.env   # define $DB_CONN, la conexión a la base
```

Si `db_config_gral.env` no existe, el script aborta de entrada con
`Error: Archivo de configuración no encontrado.`

## Cómo verificarlo

```bash
# Qué lista recibe cada bloque: míralo en la definición del job en Rundeck
# Y comprueba que la lista tiene un número PAR de elementos
echo "17,17,18,18" | tr ',' '\n' | wc -l
```

## Ver también

[D02_lookup_stg_formato](../D%20-%20Carga%20STG/D02_lookup_stg_formato.md) · [D01_mecanica_carga_copy](../D%20-%20Carga%20STG/D01_mecanica_carga_copy.md) · [D07_bloques_optimizacio](../D%20-%20Carga%20STG/D07_bloques_optimizacio.md) · [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md) · [F03_funcion_trf](../F%20-%20Transformacion%20TRF/F03_funcion_trf.md)

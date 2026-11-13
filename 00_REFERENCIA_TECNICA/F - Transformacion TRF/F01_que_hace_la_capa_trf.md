---
titulo: "F01 — Qué hace la capa TRF y hacia dónde escribe"
familia: F
etapa: "Transformación TRF"
tipo: Referencia
tags:
  - familia/F
  - etapa/transformacion-trf
  - tipo/referencia
keywords: "TRF, transformación, trf_s3, procedimientos, lookup_trf, familias"
---

# F01 — Qué hace la capa TRF y hacia dónde escribe

**Etapa:** Transformación TRF
**Tipo:** Referencia
**Palabras clave:** TRF, transformación, trf_s3, procedimientos, lookup_trf, familias

## En una línea

Toma el dato validado de `stg_s3` y lo consolida en el modelo de negocio de `trf_s3` mediante 480
procedimientos, uno o varios por tabla destino.

## Cómo se invoca

El mismo script que carga staging ejecuta las transformaciones, según la **posición par** del valor
en la lista de argumentos:

```bash
procedimiento=`grep '|'$valor'|' $lookup_trf | cut -d '|' -f 3`
sql="call "$procedimiento" ;"
V_OUT=$($DB_CONN -c "$sql")
```

Ver [D03_script_stg_trf](../D%20-%20Carga%20STG/D03_script_stg_trf.md).

## `lookup_trf.txt`

```
|id|procedimiento(parámetros)|[tabla_origen]
```

```
|1|trf_s3.load_carteira_receitas(0,60)|
|5|trf_s3.load_mt_caixa(0)|SAC_CAIXA_MT_T
```

| Campo | Contenido |
|---|---|
| 2 | id — se referencia desde los pasos de los bloques |
| 3 | **Procedimiento con sus parámetros, tal cual se llama** |
| 4 | Tabla de origen (opcional, informativo) |

Los parámetros están escritos en el propio lookup. El `0` inicial suele ser un código de proceso.

```bash
grep '|<id>|' /nfq/data/cfg/lookup_trf.txt        # qué procedimiento corre este paso
grep -i "<TABLA>" /nfq/data/cfg/lookup_trf.txt    # qué paso alimenta esta tabla
```

## Las familias de procedimientos

Son 480 en `trf_s3`, y el prefijo indica el dominio de origen:

| Prefijo | Ejemplos | Dominio |
|---|---|---|
| `cs_` | `cs_alt_cod_bond_pc`, `cs_assets_price_transf_pc` | Activos y sus atributos |
| `ch_` | `ch_cashbal_transf_pc`, `ch_cashmovm_transf_pc` | Efectivo y movimientos |
| `load_` | `load_carteira_receitas`, `load_mt_caixa` | Cargas de dominio (BULLE, SAC, FIDC) |

Los sufijos también son sistemáticos: `_pc` procedimiento, `_transf_pc` transformación.

Y las tablas destino, dentro de `trf_s3`, se agrupan por prefijo: `sss_` (291 tablas, referencial),
`sac_` (209, salida a SAC), `cart_` (42, cartera). Ver [A05_esquemas_base_de_datos](../A%20-%20Orientacion/A05_esquemas_base_de_datos.md).

## La traza

Todo procedimiento de transformación llama a `stg_s3.LOG_TRACE()`, que escribe en
`stg_s3.AUD_LOG_TRACE_T`. **Ésa es la única traza de esta etapa**: no hay equivalente a
`AUD_LOAD_TRACE_T`, que es específica de la carga.

```sql
SELECT dat_load_date, cod_load_plan, step_load, cod_status, des_log
FROM   stg_s3.aud_log_trace_t
WHERE  cod_load_plan = :plan AND dat_load_date >= CURRENT_DATE
ORDER  BY dat_load_date DESC LIMIT 50;
```

Limitación importante: `AUD_LOG_TRACE_T` **no tiene `cod_load_trace`**, sólo `cod_load_plan`. No se
puede atar un mensaje a una ejecución concreta; si el mismo plan corrió dos veces, hay que separar
por hora. Ver [E06_tablas_auditoria](../E%20-%20Parametrizacion/E06_tablas_auditoria.md).

Y recuerda que el nivel de log configurado puede estar filtrando mensajes. Ver [E08_log_trace_niveles](../E%20-%20Parametrizacion/E08_log_trace_niveles.md).

## ⚠ Cómo detecta errores el script

```bash
if [ "$V_OUT" != "0" ]; then
    flag_error_gral=1
    echo "error en " $procedimiento
fi
```

Compara la salida de `psql` con la cadena `"0"`. La conexión está definida como

```bash
export DB_CONN='psql -t -A -h ... -p 5432 -d postgres -U ...'
```

así que la salida viene sin cabeceras ni formato, y la comparación **puede** funcionar. Pero sólo
si el procedimiento devuelve literalmente `0`: los que tienen parámetro de salida devuelven su
valor, y los que no lo tienen hacen que `psql` emita la etiqueta de comando `CALL`, que **no es
`"0"`** y marcaría error.

Consecuencia práctica: el indicador de error de esta etapa **depende de la firma de cada
procedimiento**, no de si la transformación fue bien.

**Juzga la transformación por los datos y las trazas, no por el color del job.**
Ver [R5_07_alerta_vs_estado_real](../R5%20-%20Alertas%20Rundeck/R5_07_alerta_vs_estado_real.md).

## Ver también

[D03_script_stg_trf](../D%20-%20Carga%20STG/D03_script_stg_trf.md) · [D07_bloques_optimizacio](../D%20-%20Carga%20STG/D07_bloques_optimizacio.md) · [E06_tablas_auditoria](../E%20-%20Parametrizacion/E06_tablas_auditoria.md) · [A05_esquemas_base_de_datos](../A%20-%20Orientacion/A05_esquemas_base_de_datos.md) · [E08_log_trace_niveles](../E%20-%20Parametrizacion/E08_log_trace_niveles.md)

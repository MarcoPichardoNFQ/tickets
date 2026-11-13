---
titulo: "K02 — Las interfaces BULLE"
familia: K
etapa: "Carga STG"
tipo: Referencia
tags:
  - familia/K
  - etapa/carga-stg
  - tipo/referencia
keywords: "BULLE, BUL_, receita, rebate, democota, fundo, punto y coma"
---

# K02 — Las interfaces BULLE

**Etapa:** Carga STG
**Tipo:** Referencia
**Palabras clave:** BULLE, BUL_, receita, rebate, democota, fundo, punto y coma

## En una línea

Cuatro interfaces, separador `;`, y **sin la protección que sí tienen las del flujo XML**.

## El inventario

| Tabla | Patrón de fichero | Separador |
|---|---|---|
| `BUL_RECEITA_T` | `S3_FIN_RECEITA*.csv` | `;` |
| `BUL_REBATE_T` | `S3_FIN_REBATE*.csv` | `;` |
| `BUL_DEMOCOTA_T` | `S3_DEM_DEMOCO*.csv` | `;` |
| `BUL_FUNDO_T` | `S3_SGC_FUNDOS*.csv` | `;` |

Histórico en `DIR_PROCESSED/DIR_BULLE/`. Ficheros de control `BULLE_markedFiles.ctrl` y
`BULLE_processedFiles.ctrl`.

```bash
grep -i "DIR_BULLE" /nfq/data/cfg/lookup_stg.txt
```

## Las transformaciones

```
|1|trf_s3.load_carteira_receitas(0,60)|
|2|trf_s3.load_carteira_rebates(0,60)|
|3|trf_s3.load_carteira_democotas(0,60)|
|4|trf_s3.load_fund_carteira_bulle(0)|
```

Los tres primeros llevan un segundo parámetro `60`; el cuarto sólo uno. Ver [F09_load_bulle_sac_fidc](../F%20-%20Transformacion%20TRF/F09_load_bulle_sac_fidc.md).

## ⚠ El separador `;` no está protegido

El flujo XML sustituye los `!` por `¡` antes de convertir, así que el separador nunca aparece dentro
de un dato:

```bash
sed -i 's/!/¡/g' "$fileToOpen"
```

**No existe nada equivalente para el punto y coma.** Un `;` dentro de una descripción rompe la línea
y desplaza las columnas.

**Es la causa número uno de errores de columnas en estas cuatro interfaces.** Y como los ficheros
vienen ya generados —no pasan por el conversor—, no hay ningún punto donde interceptarlo.

Diagnóstico:

```bash
awk -F';' '{print NF}' <FICHERO>.csv | sort | uniq -c
awk -F';' -v n=<esperados> 'NF!=n {print NR": "NF" campos -> "$0}' <FICHERO>.csv | head -5
```

Ver [C11_separador_dentro_del_dato](../C%20-%20Conversion%20Java/C11_separador_dentro_del_dato.md) y [D09_error_numero_columnas](../D%20-%20Carga%20STG/D09_error_numero_columnas.md).

## No hay control de recepción

`controlflag_interfaces` no sabe nada de BULLE: **no se puede preguntar «¿llegó todo lo de BULLE
hoy?»** con el mecanismo habitual. La única señal es la traza de carga:

```sql
SELECT cod_load_plan, cod_load_trace, dat_load_date, des_file_loaded,
       amt_register_process, cod_status
FROM   stg_s3.aud_load_trace_t
WHERE  des_file_loaded ILIKE '%BUL%' OR des_file_loaded ILIKE '%S3_FIN%'
    OR des_file_loaded ILIKE '%S3_DEM%' OR des_file_loaded ILIKE '%S3_SGC%'
ORDER  BY dat_load_date DESC LIMIT 20;
```

Y la comparación con su propia historia:

```sql
SELECT cod_load_plan, dat_load_date::date AS dia,
       count(*), sum(amt_register_process) AS filas
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_plan IN (1,2,3,4) AND dat_load_date > CURRENT_DATE - 30
GROUP  BY 1,2 ORDER BY 2 DESC, 1;
```

## Qué aplica y qué no

| Familia | ¿Aplica a BULLE? |
|---|---|
| `B` — flags | **No** |
| `C` — conversión Java | **No** |
| `D` — carga STG | Sí |
| `E`, `R1` — validaciones y descartes | Sí |
| `R2` — duplicados | Sí |
| `F` — transformación, vía `load_*` | Sí |

## Ver también

[K01_bulle_sac_fidc](../K%20-%20BULLE%20SAC%20FIDC/K01_bulle_sac_fidc.md) · [F09_load_bulle_sac_fidc](../F%20-%20Transformacion%20TRF/F09_load_bulle_sac_fidc.md) · [C11_separador_dentro_del_dato](../C%20-%20Conversion%20Java/C11_separador_dentro_del_dato.md) · [K05_runbook_bulle_sac](../K%20-%20BULLE%20SAC%20FIDC/K05_runbook_bulle_sac.md) · [D02_lookup_stg_formato](../D%20-%20Carga%20STG/D02_lookup_stg_formato.md)

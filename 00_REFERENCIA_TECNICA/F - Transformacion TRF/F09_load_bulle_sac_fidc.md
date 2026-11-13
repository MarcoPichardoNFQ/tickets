---
titulo: "F09 — Los procedimientos `load_*`: BULLE, SAC y FIDC"
familia: F
etapa: "Transformación TRF"
tipo: Referencia
tags:
  - familia/F
  - etapa/transformacion-trf
  - tipo/referencia
keywords: "load_, BULLE, SAC, FIDC, dominios periféricos, carteira, caixa"
---

# F09 — Los procedimientos `load_*`: BULLE, SAC y FIDC

**Etapa:** Transformación TRF
**Tipo:** Referencia
**Palabras clave:** load_, BULLE, SAC, FIDC, dominios periféricos, carteira, caixa

## En una línea

La familia `load_*` transforma los dominios que **no vienen del flujo de XML y flags**: entran como
ficheros planos ya generados.

## Cómo se reconocen

En `lookup_trf.txt`, por el prefijo del procedimiento:

```
|1|trf_s3.load_carteira_receitas(0,60)|
|2|trf_s3.load_carteira_rebates(0,60)|
|3|trf_s3.load_carteira_democotas(0,60)|
|4|trf_s3.load_fund_carteira_bulle(0)|
|5|trf_s3.load_mt_caixa(0)|SAC_CAIXA_MT_T
|6|trf_s3.load_cpr_caixa(0)|SAC_CAIXA_CPR_T
```

Y en `lookup_stg.txt`, por el prefijo de tabla y el directorio de histórico:

| Dominio | Prefijo de tabla | Directorio | Separador |
|---|---|---|---|
| BULLE | `BUL_` | `DIR_PROCESSED/DIR_BULLE/` | `;` |
| SAC | `SAC_` | `DIR_PROCESSED/DIR_SAC/` | `!` |

```bash
grep -c "DIR_BULLE" /nfq/data/cfg/lookup_stg.txt
grep -c "DIR_SAC"   /nfq/data/cfg/lookup_stg.txt
grep -i "load_"     /nfq/data/cfg/lookup_trf.txt
```

## En qué se diferencian del flujo principal

| | Flujo `MEGA*` | `load_*` |
|---|---|---|
| Entrada | XML declarados por un flag | Ficheros planos ya generados |
| Conversión Java | Sí | **No** |
| Control por flag | `controlflag_interfaces` | **Ninguno** |
| Validaciones de staging | Sí | Sí |
| Transformación | `cs_`, `ch_`, `fa_` | `load_*` |

**No pasan por conversión ni por control de flags.** Las familias `B` y `C` de esta base no les
aplican; el resto sí.

## La consecuencia operativa

**No hay forma de preguntar «¿llegó todo lo de BULLE hoy?»** con el mecanismo habitual:
`controlflag_interfaces` no sabe nada de estos dominios.

La única señal es la traza de carga:

```sql
SELECT cod_load_plan, cod_load_trace, dat_load_date, des_file_loaded,
       amt_register_process, cod_status, des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  des_file_loaded ILIKE '%BUL%' OR des_file_loaded ILIKE '%SAC%'
ORDER  BY dat_load_date DESC LIMIT 20;
```

Y la comparación con su propia historia, para saber si hoy falta algo:

```sql
SELECT cod_load_plan, dat_load_date::date AS dia, count(*), sum(amt_register_process) AS filas
FROM   stg_s3.aud_load_trace_t
WHERE  des_file_loaded ILIKE '%BUL%'
  AND  dat_load_date > CURRENT_DATE - 15
GROUP  BY 1,2 ORDER BY 2 DESC, 1;
```

## ⚠ El separador `;` de BULLE no está protegido

El flujo XML sustituye los `!` por `¡` antes de convertir, así que el separador nunca aparece dentro
de un dato. **Las cargas BULLE usan `;` y no tienen ninguna sustitución equivalente**: un punto y
coma dentro de una descripción rompe la línea y desplaza las columnas.

Es la causa número uno de errores de columnas en estas interfaces.
Ver [C11_separador_dentro_del_dato](../C%20-%20Conversion%20Java/C11_separador_dentro_del_dato.md) y [D09_error_numero_columnas](../D%20-%20Carga%20STG/D09_error_numero_columnas.md).

## Los ficheros de control `.ctrl`

Los campos 8 y 9 de `lookup_stg.txt` referencian ficheros de control propios por familia:
`BULLE_markedFiles.ctrl` / `BULLE_processedFiles.ctrl`, `SACCAIXA_*`, `SACPOS_*`. Son un mecanismo
de seguimiento específico de estos dominios.

## Ver también

[K01_bulle_sac_fidc](../K%20-%20BULLE%20SAC%20FIDC/K01_bulle_sac_fidc.md) · [F05_familias_procedimientos](../F%20-%20Transformacion%20TRF/F05_familias_procedimientos.md) · [C11_separador_dentro_del_dato](../C%20-%20Conversion%20Java/C11_separador_dentro_del_dato.md) · [D02_lookup_stg_formato](../D%20-%20Carga%20STG/D02_lookup_stg_formato.md)

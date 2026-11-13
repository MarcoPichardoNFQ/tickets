---
titulo: "K03 — Las interfaces SAC"
familia: K
etapa: "Carga STG"
tipo: Referencia
tags:
  - familia/K
  - etapa/carga-stg
  - tipo/referencia
keywords: "SAC, SAC_, 226 interfaces, posiciones, movimientos, caixa"
---

# K03 — Las interfaces SAC

**Etapa:** Carga STG
**Tipo:** Referencia
**Palabras clave:** SAC, SAC_, 226 interfaces, posiciones, movimientos, caixa

## En una línea

**226 interfaces** — con diferencia el dominio periférico más grande, mucho mayor que BULLE.

## El volumen

```bash
grep -c "DIR_SAC" /nfq/data/cfg/lookup_stg.txt      # 226
grep -c "DIR_BULLE" /nfq/data/cfg/lookup_stg.txt    # 4
```

Separador `!`, histórico en `DIR_PROCESSED/DIR_SAC/`.

## Los dominios

Por el patrón del nombre de fichero se agrupan así:

| Familia | Ejemplos de tabla | Fichero |
|---|---|---|
| **Caixa** | `SAC_CAIXA_MT_T`, `SAC_CAIXA_CPR_T` | `_MT_CAIXA.txt`, `_SAC_CL_CPR.txt` |
| **Posiciones** | `SAC_POS_RV_T`, `SAC_POS_RF_T`, `SAC_POS_FU_T`, `SAC_POS_FI_T`, `SAC_POS_SW2_T`, `SAC_POS_RV_EM_T`, `SAC_POS_RV_TERMO_T` | `_SAC_<tipo>_POS.txt` |
| **Patrimonio** | `SAC_PL_CL_PATRSINT_T` | `_SAC_CL_PATRSINT.txt` |
| **Rentabilidad** | `SAC_STAT_CL_RENTAB_T` | `_SAC_CL_RENTAB.txt` |
| **Clientes** | `SAC_STAT_CLI_BAS_T` | `_CLI_BAS.txt` |

El sufijo indica el tipo de activo: `RV` renta variable, `RF` renta fija, `FU` futuros, `FI` fondos,
`SW` swaps, `TERMO` a plazo, `EM` empréstimos.

```bash
grep -i "DIR_SAC" /nfq/data/cfg/lookup_stg.txt | awk -F'|' '{printf "%-28s %s\n",$3,$4}'
```

## Las familias de control `.ctrl`

Los campos 8 y 9 del lookup referencian ficheros de control agrupados por dominio:

```
SACCAIXA_markedFiles.ctrl      SACCAIXA170_markedFiles.ctrl
SACMOV_markedFiles.ctrl        SACMOV170_markedFiles.ctrl
SACMEM_markedFiles.ctrl        SACMEM170_markedFiles.ctrl
SACPOS_markedFiles.ctrl        …
```

**El sufijo `170` marca una variante** que convive con la principal — probablemente otra entidad o
una versión distinta del mismo dominio. Conviene confirmarlo antes de tratarlas como equivalentes.

```bash
awk -F'|' 'NF>8{print $8}' /nfq/data/cfg/lookup_stg.txt | sort -u
```

## SAC está a los dos lados del flujo

Es lo que más despista de este dominio:

| Prefijo | Esquema | Papel |
|---|---|---|
| `SAC_*` | `stg_s3` | **Entrada**: ficheros planos que llegan |
| `sac_*` | `trf_s3` | **Salida**: 209 tablas producidas por los mapeos |

Son cosas distintas con nombres parecidos. Ante «la tabla SAC no tiene datos», la primera pregunta
es **de qué lado**. Ver [A05_esquemas_base_de_datos](../A%20-%20Orientacion/A05_esquemas_base_de_datos.md) y [I01_convencion_nombres](../I%20-%20Referencia%20de%20datos/I01_convencion_nombres.md).

## Sin control de recepción

Como BULLE, `controlflag_interfaces` no cubre estas interfaces. La única señal es la traza:

```sql
SELECT cod_load_plan, cod_load_trace, dat_load_date, des_file_loaded,
       amt_register_process, cod_status
FROM   stg_s3.aud_load_trace_t
WHERE  des_file_loaded ILIKE '%_SAC_%' OR des_file_loaded ILIKE '%_CLI_%'
    OR des_file_loaded ILIKE '%_MT_CAIXA%'
ORDER  BY dat_load_date DESC LIMIT 30;
```

## El separador `!` sí está en riesgo aquí

Los ficheros SAC usan `!` como separador, igual que la salida del conversor. Pero **estos ficheros
no pasan por el conversor**, así que **no reciben la sustitución `sed 's/!/¡/g'`**.

Un `!` dentro de un dato en un fichero SAC rompe la línea igual que un `;` en uno de BULLE.
Ver [C11_separador_dentro_del_dato](../C%20-%20Conversion%20Java/C11_separador_dentro_del_dato.md).

## Ver también

[K01_bulle_sac_fidc](../K%20-%20BULLE%20SAC%20FIDC/K01_bulle_sac_fidc.md) · [K02_interfaces_bulle](../K%20-%20BULLE%20SAC%20FIDC/K02_interfaces_bulle.md) · [F09_load_bulle_sac_fidc](../F%20-%20Transformacion%20TRF/F09_load_bulle_sac_fidc.md) · [K05_runbook_bulle_sac](../K%20-%20BULLE%20SAC%20FIDC/K05_runbook_bulle_sac.md) · [I01_convencion_nombres](../I%20-%20Referencia%20de%20datos/I01_convencion_nombres.md)

---
titulo: "K06 — Los ficheros `.ctrl` de control"
familia: K
etapa: "Carga STG"
tipo: Referencia
tags:
  - familia/K
  - etapa/carga-stg
  - tipo/referencia
keywords: "ctrl, markedFiles, processedFiles, control propio, familias"
---

# K06 — Los ficheros `.ctrl` de control

**Etapa:** Carga STG
**Tipo:** Referencia
**Palabras clave:** ctrl, markedFiles, processedFiles, control propio, familias

## En una línea

Los dominios periféricos tienen su propio mecanismo de control por ficheros `.ctrl`, distinto del
control por flags del flujo principal.

## Dónde se declaran

Campos 8 y 9 de cada línea de `lookup_stg.txt`:

```
|1|BUL_RECEITA_T|S3_FIN_RECEITA*.csv|DIR_PROCESSED/DIR_BULLE/|;|CSV HEADER|BULLE_markedFiles.ctrl|BULLE_processedFiles.ctrl|
                                                                          └── campo 8 ────────┘ └── campo 9 ──────────┘
```

Dos ficheros por familia:

| Fichero | Propósito aparente |
|---|---|
| `<FAMILIA>_markedFiles.ctrl` | Ficheros marcados |
| `<FAMILIA>_processedFiles.ctrl` | Ficheros ya procesados |

## Las familias

```bash
awk -F'|' 'NF>8{print $8}' /nfq/data/cfg/lookup_stg.txt | sort -u
```

```
BULLE_markedFiles.ctrl
FIDC_markedFiles.ctrl
KYC_markedFiles.ctrl
SACCAIXA_markedFiles.ctrl      SACCAIXA170_markedFiles.ctrl
SACMEM_markedFiles.ctrl        SACMEM170_markedFiles.ctrl
SACMOV_markedFiles.ctrl        SACMOV170_markedFiles.ctrl
…
```

Confirman los cuatro dominios periféricos —BULLE, SAC, FIDC, KYC— y revelan la subdivisión de SAC
por tipo: **CAIXA** (efectivo), **MOV** (movimientos), **MEM** (memoria), **POS** (posiciones).

## El sufijo `170`

Varias familias tienen una variante `170` que convive con la principal: `SACCAIXA` y `SACCAIXA170`,
`SACMOV` y `SACMOV170`, `SACMEM` y `SACMEM170`.

**Su significado no está determinado** con el material disponible. Podría ser otra entidad, otra
versión del formato o un entorno distinto. Antes de tratarlas como equivalentes, compruébalo:

```bash
grep "170" /nfq/data/cfg/lookup_stg.txt | awk -F'|' '{printf "%-28s %s\n",$3,$4}' | head
```

Comparar los patrones de fichero de una y otra suele aclararlo.

## ⚠ Nota de cobertura

**No he podido determinar qué proceso escribe o lee estos ficheros.** El script de carga
(`load_stgtrf_script.sh`) extrae los campos 2 al 7 del lookup y **no usa los campos 8 y 9**:

```bash
cod_tab=`echo $cadena | cut -d '|' -f 2`
nom_tab=`echo $cadena | cut -d '|' -f 3`
fichero=`echo $cadena | cut -d '|' -f 4`
ruta_hist=`echo $cadena | cut -d '|' -f 5`
sep=`echo $cadena | cut -d '|' -f 6`
cabe=`echo $cadena | cut -d '|' -f 7`
```

Así que **el consumidor de estos ficheros no está en el material disponible**, igual que ocurre con
`lookup_qlik.txt`. Dado el historial de este sistema —donde ya han aparecido varias piezas
declaradas y no usadas—, **no des por hecho que este control esté operativo**.

Comprobación directa:

```bash
. /nfq/data/cfg/env.properties
find / -name "*_markedFiles.ctrl" 2>/dev/null | head
find / -name "*_processedFiles.ctrl" -newermt "-7 days" 2>/dev/null | head
```

Si no existen, o no se han modificado en días, el mecanismo no está en uso.

## Ver también

[K01_bulle_sac_fidc](../K%20-%20BULLE%20SAC%20FIDC/K01_bulle_sac_fidc.md) · [K03_interfaces_sac](../K%20-%20BULLE%20SAC%20FIDC/K03_interfaces_sac.md) · [D02_lookup_stg_formato](../D%20-%20Carga%20STG/D02_lookup_stg_formato.md) · [G10_codigo_sin_llamadas](../G%20-%20Mapeos/G10_codigo_sin_llamadas.md) · [H15_catalogo_tareas_qlik](../H%20-%20Cierre%20y%20Qlik/H15_catalogo_tareas_qlik.md)

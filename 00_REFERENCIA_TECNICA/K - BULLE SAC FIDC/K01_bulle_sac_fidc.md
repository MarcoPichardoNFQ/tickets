---
titulo: "K01 — BULLE, SAC y FIDC: qué son y cómo encajan"
familia: K
etapa: "Transformación TRF"
tipo: Referencia
tags:
  - familia/K
  - etapa/transformacion-trf
  - tipo/referencia
keywords: "BULLE, SAC, FIDC, load_, no migrado, dominios periféricos"
---

# K01 — BULLE, SAC y FIDC: qué son y cómo encajan

**Etapa:** Transformación TRF
**Tipo:** Referencia
**Palabras clave:** BULLE, SAC, FIDC, load_, no migrado, dominios periféricos

## En una línea

Tres dominios que entran por la misma maquinaria de carga pero **no vienen del flujo de XML y
flags**: llegan como CSV o TXT ya planos, con su propio separador y su propio ciclo.

## Cómo se distinguen del flujo principal

| | Flujo principal (MEGA*) | BULLE / SAC / FIDC |
|---|---|---|
| Origen | XML declarados por un flag | Ficheros planos ya generados |
| Conversión Java | Sí | **No** |
| Separador | `!` | `;` (BULLE), `!` (SAC) |
| Disparador | Llegada del flag | El propio ciclo de carga |
| Directorio de histórico | `DIR_PROCESSED/DIR_MEGARA/` | `DIR_PROCESSED/DIR_BULLE/`, `DIR_PROCESSED/DIR_SAC/` |

**No pasan por la etapa de conversión.** Entran directamente en la carga a staging, así que las
familias `B` (flags) y `C` (conversión) **no aplican** a ellos. Todo lo demás —validaciones,
descartes, transformación— sí.

## Cómo se ven en la parametrización

En `lookup_stg.txt` se reconocen por el prefijo de tabla y el directorio de histórico:

```
|1|BUL_RECEITA_T|S3_FIN_RECEITA*.csv|DIR_PROCESSED/DIR_BULLE/|;|CSV HEADER|...
|2|BUL_REBATE_T|S3_FIN_REBATE*.csv|DIR_PROCESSED/DIR_BULLE/|;|CSV HEADER|...
|5|SAC_CAIXA_MT_T|_MT_CAIXA.txt|DIR_PROCESSED/DIR_SAC/|!|CSV HEADER|...
|7|SAC_POS_RV_T|_SAC_RV_POS.txt|DIR_PROCESSED/DIR_SAC/|!|CSV HEADER|...
```

Prefijos de tabla: **`BUL_`** para BULLE, **`SAC_`** para SAC.

Y en `lookup_trf.txt`, los procedimientos con prefijo `load_`:

```
|1|trf_s3.load_carteira_receitas(0,60)|
|4|trf_s3.load_fund_carteira_bulle(0)|
|5|trf_s3.load_mt_caixa(0)|SAC_CAIXA_MT_T
```

```bash
# Inventario rápido
grep -c "DIR_BULLE" /nfq/data/cfg/lookup_stg.txt
grep -c "DIR_SAC"   /nfq/data/cfg/lookup_stg.txt
grep -i "bulle\|fidc" /nfq/data/cfg/lookup_trf.txt
```

## Diferencias operativas que importan

**El separador es `;` en BULLE.** Y a diferencia de las cargas con `!`, **no hay ninguna
sustitución previa que lo proteja**: un punto y coma dentro de un dato rompe la línea. Es la causa
número uno de errores de columnas en estas interfaces. Ver [C11_separador_dentro_del_dato](../C%20-%20Conversion%20Java/C11_separador_dentro_del_dato.md).

**No hay control de recepción por flag.** `controlflag_interfaces` no sabe nada de ellos: no se
puede preguntar «¿llegó todo lo de BULLE hoy?» de la forma habitual. La única señal es la traza de
carga:

```sql
SELECT cod_load_plan, cod_load_trace, dat_load_date, des_file_loaded,
       amt_register_process, cod_status
FROM   stg_s3.aud_load_trace_t
WHERE  des_file_loaded ILIKE '%BUL%' OR des_file_loaded ILIKE '%SAC%'
ORDER  BY dat_load_date DESC LIMIT 20;
```

**Los ficheros de control `.ctrl`.** Los campos 8 y 9 de `lookup_stg.txt` referencian
`*_markedFiles.ctrl` y `*_processedFiles.ctrl` por familia: `BULLE_*`, `SACCAIXA_*`, `SACPOS_*`.
Son un mecanismo de control propio de estas familias.

## Qué aplica y qué no

| Familia de fichas | ¿Aplica a BULLE/SAC/FIDC? |
|---|---|
| `B` — flags | **No** |
| `C` — conversión Java | **No** |
| `D` — carga STG | **Sí**, íntegramente |
| `E` / `R1` — validaciones y descartes | **Sí** |
| `R2` — duplicados | **Sí** |
| `F` — transformación | Sí, vía los procedimientos `load_*` |
| `G` / `R3` — mapeos | Depende del caso |

## Estado de esta ficha

Cobertura de orientación. El detalle por interfaz —qué tablas alimenta cada una, sus consumidores y
sus particularidades— exige recorrer sus procedimientos `load_*` uno a uno. Lo que hay aquí es
suficiente para **situar una incidencia** y saber qué fichas del resto de la base aplican, que es lo
que se necesita al recibir el ticket.

## Ver también

[D02_lookup_stg_formato](../D%20-%20Carga%20STG/D02_lookup_stg_formato.md) · [C11_separador_dentro_del_dato](../C%20-%20Conversion%20Java/C11_separador_dentro_del_dato.md) · [F01_que_hace_la_capa_trf](../F%20-%20Transformacion%20TRF/F01_que_hace_la_capa_trf.md) · [D01_mecanica_carga_copy](../D%20-%20Carga%20STG/D01_mecanica_carga_copy.md) · [K04_fidc_kyc_alertas](../K%20-%20BULLE%20SAC%20FIDC/K04_fidc_kyc_alertas.md) · [K06_ficheros_ctrl](../K%20-%20BULLE%20SAC%20FIDC/K06_ficheros_ctrl.md)

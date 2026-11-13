---
titulo: "F05 — Las familias de procedimientos de `trf_s3`"
familia: F
etapa: "Transformación TRF"
tipo: Referencia
tags:
  - familia/F
  - etapa/transformacion-trf
  - tipo/referencia
keywords: "cs_, ch_, fa_, ec_, cus_, load_, prefijos, familias, _pc"
---

# F05 — Las familias de procedimientos de `trf_s3`

**Etapa:** Transformación TRF
**Tipo:** Referencia
**Palabras clave:** cs_, ch_, fa_, ec_, cus_, load_, prefijos, familias, _pc

## En una línea

480 procedimientos en `trf_s3`, y el prefijo del nombre dice de qué dominio viene el dato.

## El reparto

De los 480, **152 son funciones de mapeo** (`function_meg_*`, ver [G06_catalogo_mapeos](../G%20-%20Mapeos/G06_catalogo_mapeos.md)). Los
**328 restantes** son la transformación propiamente dicha:

| Prefijo | Nº | Dominio |
|---|---|---|
| `cs_` | 219 | **Custodia y activos.** El grueso: bonos, acciones, opciones, futuros, precios, emisores |
| `fa_` | 33 | **Fund accounting.** Valor liquidativo, rentabilidad, comisiones |
| `ec_` | 26 | Entidades y cuentas |
| `cus_` | 10 | Custodios |
| `ch_` | 7 | **Cash.** Efectivo, movimientos, transferencias |
| `s3_` | 4 | Control de interfaces |
| `data_`, `traducir_`, `formatear_`, `reports_`, `fn_`, `delete_` | 2 c/u | Utilidades |
| `load_` | resto | **Cargas de dominio**: BULLE, SAC, FIDC. Ver [F09_load_bulle_sac_fidc](../F%20-%20Transformacion%20TRF/F09_load_bulle_sac_fidc.md) |

## Los sufijos

| Sufijo | Nº | Qué indica |
|---|---|---|
| `_pc` | 292 | Procedimiento (*procedure*). Es el sufijo dominante |
| `_t` | 113 | Devuelve o alimenta una tabla |
| `_t1`, `_t2`, `_t3` | 14 | Variantes o fases sucesivas del mismo proceso |

Combinaciones típicas: `cs_alt_cod_bond_pc`, `ch_cashbal_transf_pc`, `cs_assets_price_transf_pc`.
El infijo `_transf_` marca las que hacen transformación propiamente dicha.

## Para qué sirve esto en soporte

**Localizar el procedimiento de una tabla.** El nombre suele contener el de la tabla destino:

```bash
ls /ruta/procedures/ | grep -i "<parte_del_nombre_de_tabla>"
```

O directamente en la base:

```sql
SELECT p.proname
FROM   pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'trf_s3' AND p.proname ILIKE '%<tabla>%'
ORDER  BY 1;
```

**Situar el dominio de una incidencia.** Un fallo en un `cs_` afecta a activos y custodia; en un
`ch_`, a efectivo; en un `fa_`, a valoración y rentabilidad. Sirve para saber a quién afecta antes
de entender la causa.

**Estimar el alcance.** Los `cs_` son 219 de 328: dos tercios de la transformación giran en torno a
activos y custodia. Un problema en un catálogo de activos tiene mucho más radio que uno de efectivo.

## Leer un procedimiento

```sql
SELECT prosrc FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'trf_s3' AND p.proname = '<nombre>';
```

Y el índice completo procedimiento → tabla destino → origen está en [I09_indice_tabla_origen](../I%20-%20Referencia%20de%20datos/I09_indice_tabla_origen.md).

## Ver también

[F01_que_hace_la_capa_trf](../F%20-%20Transformacion%20TRF/F01_que_hace_la_capa_trf.md) · [I09_indice_tabla_origen](../I%20-%20Referencia%20de%20datos/I09_indice_tabla_origen.md) · [G06_catalogo_mapeos](../G%20-%20Mapeos/G06_catalogo_mapeos.md) · [F09_load_bulle_sac_fidc](../F%20-%20Transformacion%20TRF/F09_load_bulle_sac_fidc.md) · [A05_esquemas_base_de_datos](../A%20-%20Orientacion/A05_esquemas_base_de_datos.md)

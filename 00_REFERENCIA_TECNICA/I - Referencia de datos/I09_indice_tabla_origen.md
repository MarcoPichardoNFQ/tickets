---
titulo: "I09 — Índice: tabla destino → qué la llena"
familia: I
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/I
  - etapa/transversal
  - tipo/referencia
keywords: "índice, qué llena esta tabla, procedimiento, origen, grafo, trazabilidad inversa"
---

# I09 — Índice: tabla destino → qué la llena

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** índice, qué llena esta tabla, procedimiento, origen, grafo, trazabilidad inversa

## En una línea

La pregunta número uno ante un dato que falta —«¿quién debería haber escrito esto?»— y las tres
consultas que la responden según la capa.

## Capa 1 — ¿Qué llena una tabla de `stg_s3`?

Un fichero, a través de un plan de carga. La cadena es
`fichero → lookup_stg → PAR_LOAD_PLAN_T → tabla`.

```sql
SELECT p.cod_load_plan, t.des_table, p.des_procedure_run,
       p.des_source_dir, p.des_separator, p.valid_err_des
FROM   stg_s3.par_load_plan_t p
JOIN   stg_s3.par_maestro_tablas_t t ON t.cod_table = p.cod_table
WHERE  t.des_table = UPPER('<TABLA>');
```

Y el patrón de fichero que la alimenta:

```bash
grep -i "|<TABLA>|" /nfq/data/cfg/lookup_stg.txt
```

## Capa 2 — ¿Qué llena una tabla de `trf_s3`?

Un procedimiento de transformación. El catálogo de Fase 0 lo tiene mapeado:

```
7_planeacion_proyecto/catalogo_fase0/grafo_transformacion.csv
name, tablas_destino, dependencias_intra_lote, datos_ya_residentes, oleada
```

300 filas con esta forma:

```
ch_cashtrantype_transf_pc, trf_s3.sss_cashtrantype_t, , stg_s3.meg_cashtrantype_t, 0
cs_addl_deriv_price_pc,    trf_s3.sss_addl_deriv_price_t, , stg_s3.meg_addl_deriv_price_t, 0
```

Se lee de derecha a izquierda: `stg_s3.meg_cashtrantype_t` → `ch_cashtrantype_transf_pc` →
`trf_s3.sss_cashtrantype_t`.

```bash
# Qué procedimiento escribe esta tabla
grep -i "<TABLA>" grafo_transformacion.csv
```

En la base, sin el CSV:

```sql
SELECT p.proname
FROM   pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'trf_s3' AND p.proname ILIKE '%<parte_del_nombre>%'
ORDER  BY 1;
```

O por el lookup, que es más directo:

```bash
grep -i "<TABLA>" /nfq/data/cfg/lookup_trf.txt
```

## Capa 3 — ¿Qué llena una tabla de salida (`sac_*`, `cart_*`)?

Una función de mapeo. La tabla de control lo declara:

```sql
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio,
       activo_inactivo, is_fromtis, retry_deadlock
FROM   exp_s3.tablas_mapeio_t
WHERE  lower(nome_tabela_aldrin) = lower('<TABLA>')
ORDER  BY nome_fn_mapeio;
```

El `lower()` es obligatorio. Y ojo: **un mismo destino puede tener varias funciones** — 122
funciones para 74 tablas. Si falta parte del dato, comprueba el estado de todas.
Ver [G06_catalogo_mapeos](../G%20-%20Mapeos/G06_catalogo_mapeos.md).

## Capa 4 — ¿Qué llega a Qlik?

```sql
SELECT count(*) FROM exp_s3.relaciontablacolumnas
WHERE  lower(tabla) = lower('<TABLA>');
```

Cero columnas = esa tabla no se publica por esa vía. Y el UUID de su tarea de recarga:

```bash
grep -i "<TABLA>" /nfq/data/cfg/lookup_qlik.txt
```

## La cadena completa, de un vistazo

```
fichero          → lookup_stg  → stg_s3.<TABLA>_T
stg_s3.<TABLA>_T → lookup_trf  → trf_s3.sss_*        (grafo_transformacion.csv)
trf_s3.sss_*     → tablas_mapeio_t → trf_s3.sac_*/cart_*
trf_s3.sac_*     → relaciontablacolumnas → Qlik
```

Cuatro saltos, cada uno con su tabla de control. **No hay identificador único que recorra los
cuatro**: el puente es el nombre de la tabla o del fichero. Ver [I11_rastrear_un_fichero_e2e](../I%20-%20Referencia%20de%20datos/I11_rastrear_un_fichero_e2e.md).

## El sentido inverso

Si lo que tienes es el dato mal y quieres llegar al origen, ve al revés por la misma escalera.
Ver [I10_rastrear_hacia_atras](../I%20-%20Referencia%20de%20datos/I10_rastrear_hacia_atras.md).

## Ver también

[I11_rastrear_un_fichero_e2e](../I%20-%20Referencia%20de%20datos/I11_rastrear_un_fichero_e2e.md) · [I10_rastrear_hacia_atras](../I%20-%20Referencia%20de%20datos/I10_rastrear_hacia_atras.md) · [F06_dependencias_oleadas](../F%20-%20Transformacion%20TRF/F06_dependencias_oleadas.md) · [G06_catalogo_mapeos](../G%20-%20Mapeos/G06_catalogo_mapeos.md) · [F14_faltan_datos_stg_o_trf](../F%20-%20Transformacion%20TRF/F14_faltan_datos_stg_o_trf.md)

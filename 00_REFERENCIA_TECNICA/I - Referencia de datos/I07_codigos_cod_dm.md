---
titulo: "I07 — Los códigos `COD_DM*`: dimensiones resueltas por lookup"
familia: I
etapa: "Transformación TRF"
tipo: Referencia
tags:
  - familia/I
  - etapa/transformacion-trf
  - tipo/referencia
keywords: "cod_dm, dimensión, lookup, clave sustituta, COD_DMASSE, COD_DMCURR"
---

# I07 — Los códigos `COD_DM*`: dimensiones resueltas por lookup

**Etapa:** Transformación TRF
**Tipo:** Referencia
**Palabras clave:** cod_dm, dimensión, lookup, clave sustituta, COD_DMASSE, COD_DMCURR

## En una línea

Columnas que sustituyen una clave de negocio por un identificador interno, resuelto contra una tabla
de dimensión — y cuando no resuelve, **la fila se pierde**.

## Qué son

`COD_DM` + abreviatura del dominio. Hay decenas:

| Columna | Dimensión |
|---|---|
| `COD_DMASSE` | Activo |
| `COD_DMCURR` | Divisa |
| `COD_DMMRKT` | Mercado |
| `COD_DMBROK` | Bróker |
| `COD_DMCOUNT` | País |
| `COD_DMCUST` | Custodio |
| `COD_DMACCT` | Cuenta |
| `COD_DMASFM` | Familia de activo |
| `COD_DMCHMOVM` | Movimiento de efectivo |
| `COD_DMCHTNTYE` | Tipo de transacción de efectivo |

```sql
-- Todas las que existen en una tabla
SELECT column_name FROM information_schema.columns
WHERE  table_schema = 'trf_s3' AND table_name = lower('<TABLA>')
  AND  column_name ILIKE 'cod_dm%'
ORDER  BY ordinal_position;
```

## Cómo se resuelven

En la transformación, mediante un `JOIN` contra la tabla de dimensión correspondiente:

```sql
... TRF.COD_DMASSE = C.COD_DMASSE AND TRF.COD_IDAC = STG.COD_IDAC ...
```

La clave natural que viene en el fichero —un ISIN, un código de divisa, un identificador de
mercado— se traduce al `COD_DM*` interno.

## ⚠ Lo que importa: un lookup que no resuelve descarta la fila

Si el valor de negocio no existe en la dimensión, el `JOIN` no casa y **la fila no llega al
destino**. No se registra como error de validación: sencillamente no aparece.

Es la causa de un síntoma muy concreto: **la carga fue bien, no hay descartes, y aun así faltan
filas en `trf_s3`.**

Y el motivo casi siempre es de **orden, no de calidad**: el catálogo de dimensión se carga en un
bloque anterior, y si ese bloque falló o llegó tarde, las filas que lo referencian se caen en
silencio. Ver [F06_dependencias_oleadas](../F%20-%20Transformacion%20TRF/F06_dependencias_oleadas.md) y [R4_11_efecto_domino](../R4%20-%20Sets%20incompletos/R4_11_efecto_domino.md).

## Cómo diagnosticarlo

### 1. ¿Está poblada la dimensión?

```sql
SELECT count(*) FROM trf_s3.sss_asset_t;      -- para COD_DMASSE
SELECT count(*) FROM trf_s3.sss_currency_t;   -- para COD_DMCURR
SELECT count(*) FROM trf_s3.sss_market_t;     -- para COD_DMMRKT
```

Una dimensión vacía o incompleta explica una pérdida masiva aguas abajo.

### 2. ¿Existe el valor concreto?

```sql
SELECT * FROM trf_s3.sss_asset_t WHERE <clave_natural> = '<valor>';
```

Cero filas = ese activo no está dado de alta, y todas las filas que lo referencien se pierden.

### 3. ¿Cuántas filas se cayeron?

Compara conteos entre origen y destino. La diferencia sin descartes registrados apunta a lookups
que no resuelven:

```sql
SELECT (SELECT count(*) FROM stg_s3.<TABLA>_T)  AS en_staging,
       (SELECT count(*) FROM trf_s3.<TABLA>)    AS en_negocio;
```

## Los que pueden ser nulos y los que no

No todos los `COD_DM*` son obligatorios. Algunos proceden de campos opcionales del fichero y su
ausencia es legítima; otros forman parte de la clave y su ausencia elimina la fila.

La distinción está en cada procedimiento de transformación, no en una tabla de configuración: hay
que leer el `JOIN` para saber si es `INNER` —elimina— o `LEFT` —deja nulo—.

```sql
SELECT prosrc FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'trf_s3' AND p.proname = '<procedimiento>';
```

Ver [R3_10_corrio_pero_no_llego](../R3%20-%20Errores%20de%20mapeo/R3_10_corrio_pero_no_llego.md) para la misma distinción aplicada a los mapeos.

## Material de referencia

El repositorio incluye documentación de apoyo en
`4_base_de_datos/Informaciones cod_dm/`: tipos de entidad existentes, jerarquías con claves
naturales visibles, y conteos de nulos por dimensión. Útil cuando hay que entender qué representa
una dimensión concreta.

## Ver también

[F06_dependencias_oleadas](../F%20-%20Transformacion%20TRF/F06_dependencias_oleadas.md) · [R4_11_efecto_domino](../R4%20-%20Sets%20incompletos/R4_11_efecto_domino.md) · [I01_convencion_nombres](../I%20-%20Referencia%20de%20datos/I01_convencion_nombres.md) · [F11_trf_corrio_sin_cambios](../F%20-%20Transformacion%20TRF/F11_trf_corrio_sin_cambios.md) · [I18_columnas_comunes](../I%20-%20Referencia%20de%20datos/I18_columnas_comunes.md)

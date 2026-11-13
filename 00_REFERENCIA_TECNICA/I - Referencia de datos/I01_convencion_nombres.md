---
titulo: "I01 — Convención de nombres y sufijos"
familia: I
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/I
  - etapa/transversal
  - tipo/referencia
keywords: "nomenclatura, sufijos, prefijos, _T, _TMP, _DES, _ERR, MEG_, convención"
---

# I01 — Convención de nombres y sufijos

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** nomenclatura, sufijos, prefijos, _T, _TMP, _DES, _ERR, MEG_, convención

## En una línea

El nombre de una tabla dice en qué capa está, qué contiene y en qué estado — si se sabe leer.

## Sufijos de tabla

| Sufijo | Contenido | Esquema |
|---|---|---|
| `_TMP` | Aterrizaje del `\COPY`. Se **trunca** al empezar cada carga | `stg_s3` |
| `_T` | Tabla definitiva. El dato bueno | `stg_s3`, `trf_s3` |
| `_ERR` | Filas con error de nulos. Copiadas y borradas de la base | `stg_s3` |
| `_DES` | Filas descartadas por clave foránea. Upsert por PK | `stg_s3` |
| `_err` | **Duplicados por clave natural apartados por un mapeo** | `trf_s3` |
| `_temp` | Tablas de uso no confirmado | `exp_s3` |

Ojo con la distinción de las dos últimas frente a las de staging: `stg_s3.<TABLA>_ERR` guarda fallos
de validación; `trf_s3.<TABLA>_err` guarda duplicados de mapeo. Mismo sufijo, mecanismos distintos.
Ver [R1_02_donde_cae_cada_cosa](../R1%20-%20Descartes/R1_02_donde_cae_cada_cosa.md) y [R1_08_descartes_en_mapeos](../R1%20-%20Descartes/R1_08_descartes_en_mapeos.md).

## Prefijos de tabla

| Prefijo | Esquema | Dominio |
|---|---|---|
| `MEG_` | `stg_s3` | Datos del ciclo Megara. **Se vacían en el cierre** |
| `BUL_` | `stg_s3` | BULLE |
| `SAC_` | `stg_s3` / `trf_s3` | SAC. En staging es entrada; en `trf_s3`, salida de mapeo |
| `sss_` | `trf_s3` | Modelo de negocio: referencial, activos, entidades (291 tablas) |
| `cart_` | `trf_s3` | Cartera y posiciones. Salida de mapeo (42) |
| `s3_` | `trf_s3` | Control de interfaces (16) |
| `PAR_` | `stg_s3` | Parametrización |
| `AUD_` | `stg_s3` | Auditoría |
| `api_` | `exp_s3` | Capa de API |

## Prefijos de procedimiento

| Prefijo | Nº | Dominio |
|---|---|---|
| `cs_` | 219 | Custodia y activos |
| `fa_` | 33 | Fund accounting |
| `ec_` | 26 | Entidades y cuentas |
| `cus_` | 10 | Custodios |
| `ch_` | 7 | Cash |
| `load_` | — | BULLE, SAC, FIDC |
| `function_meg_` | 152 | **Funciones de mapeo** |

Sufijos: `_pc` procedimiento (292 casos), `_transf_` transformación, `_fn` función.
Ver [F05_familias_procedimientos](../F%20-%20Transformacion%20TRF/F05_familias_procedimientos.md).

## Prefijos de columna

| Prefijo | Significa |
|---|---|
| `COD_` | Código o identificador |
| `DES_` | Descripción, texto |
| `DAT_` | Fecha |
| `AMT_` | Importe o cantidad |
| `CHK_` | Indicador booleano de comprobación (`CHK_NULL`, `CHK_CLAVE`) |
| `XTI_` | Indicador auxiliar |
| `COD_DM` | **Código de dimensión resuelto por lookup.** Ver [I07_codigos_cod_dm](../I%20-%20Referencia%20de%20datos/I07_codigos_cod_dm.md) |

## ⚠ Las mayúsculas no son fiables

El sistema mezcla mayúsculas y minúsculas en el mismo identificador según dónde se guarde:

- `tablas_mapeio_t.nome_fn_mapeio` → `function_MEG_CART_CAIXA_CPR_T18`
- `pg_proc.proname` → `function_meg_cart_caixa_cpr_t18`
- `relaciontablacolumnas.tabla` → minúsculas
- `par_maestro_tablas_t.des_table` → mayúsculas

**Cualquier cruce entre tablas de control necesita `lower()` en los dos lados.** Sin eso salen
falsos negativos que parecen referencias rotas. Ver [J10_trampas_conocidas](../J%20-%20Operacion/J10_trampas_conocidas.md).

## Cómo leer un nombre completo

```
stg_s3.MEG_TAX_PAYER_CAT_T_DES
│      │   │                │
│      │   │                └── descartada por clave foránea
│      │   └─────────────────── interfaz TaxPayerCategory
│      └─────────────────────── ciclo Megara, se vacía en el cierre
└────────────────────────────── staging
```

## Ver también

[A03_glosario](../A%20-%20Orientacion/A03_glosario.md) · [A05_esquemas_base_de_datos](../A%20-%20Orientacion/A05_esquemas_base_de_datos.md) · [I07_codigos_cod_dm](../I%20-%20Referencia%20de%20datos/I07_codigos_cod_dm.md) · [I18_columnas_comunes](../I%20-%20Referencia%20de%20datos/I18_columnas_comunes.md) · [F05_familias_procedimientos](../F%20-%20Transformacion%20TRF/F05_familias_procedimientos.md) · [I08_secuencias](../I%20-%20Referencia%20de%20datos/I08_secuencias.md)

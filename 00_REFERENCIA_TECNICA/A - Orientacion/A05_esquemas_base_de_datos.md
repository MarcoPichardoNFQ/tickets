---
titulo: "A05 — Mapa de esquemas de base de datos"
familia: A
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/A
  - etapa/transversal
  - tipo/referencia
keywords: "esquemas, stg_s3, trf_s3, exp_s3, prefijos, sss, sac, cart, PostgreSQL"
---

# A05 — Mapa de esquemas de base de datos

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** esquemas, stg_s3, trf_s3, exp_s3, prefijos, sss, sac, cart, PostgreSQL

## En una línea

Sólo hay tres esquemas — `stg_s3`, `trf_s3` y `exp_s3` — y el dato los recorre en ese orden.

## Detalle

### `stg_s3` — staging (~1.322 tablas)

Aterrizaje del dato crudo y toda la maquinaria de control. Contiene cuatro familias:

- **Tablas de datos**: `_TMP` (aterrizaje), `_T` (definitiva), `_ERR` y `_DES` (apartados).
- **Tablas maestras `PAR_*`**: la parametrización que gobierna el sistema.
  `PAR_LOAD_PLAN_T`, `PAR_MAESTRO_TABLAS_T`, `PAR_MAESTRO_COLUMNAS_T`,
  `PAR_MAESTRO_MASK_T`, `PAR_MAESTRO_VALID_T`, `PAR_MAESTRO_LOG_LEVEL_T`.
- **Tablas de auditoría `AUD_*`**: `AUD_LOAD_TRACE_T`, `AUD_LOAD_VALID_TRACE_T`, `AUD_LOG_TRACE_T`.
- **Control de flags**: `controlflag_arquivos`, `controlflag_interfaces`.

Aloja 20 procedimientos: carga, validación, apartado de descartes y limpieza.

### `trf_s3` — modelo de negocio (~638 tablas)

El dato ya transformado. **Los prefijos de tabla no son esquemas**, son familias de nombre:

| Prefijo | Nº de tablas | Dominio |
|---|---|---|
| `sss_` | 291 | Referencial y estático: activos, entidades, divisas, mercados |
| `sac_` | 209 | Salida hacia el sistema SAC |
| `cart_` | 42 | Cartera y posiciones |
| `s3_` | 16 | Control de interfaces |
| `meg_` | 12 | Ciclo Megara |
| `master_` | 10 | Maestros |

Aloja 480 procedimientos de transformación, con prefijos que indican origen: `cs_`, `ch_`, `load_`.

> El documento de arquitectura heredado habla de "esquemas core `trf_s3`, `sss`, `cs`, `fa`".
> Es impreciso: `sss` y `cs` son prefijos de tabla y de procedimiento dentro de `trf_s3`.
> No busques un esquema `sss`, no existe.

### `exp_s3` — control, área temporal y un dominio de salida propio (195 tablas)

Tres cosas distintas conviven aquí, y confundirlas lleva a diagnósticos equivocados:

**1. Control del ciclo de mapeos**

- `tablas_mapeio_t` — qué mapeo está activo, con sus reintentos
- `control_mapeio_t` — el contador `control_carga` por tabla y lote. Ver [G08_fim_carga_mapeo](../G%20-%20Mapeos/G08_fim_carga_mapeo.md)
- `relaciontablacolumnas` — qué columnas expone Qlik de cada tabla (103 tablas, 1.722 columnas)
- `tabla_control` — auditoría de recargas de Qlik
- Las secuencias `cod_seq_control_mapeio` y `controlflag_arquivos_cod_id_seq`
- Los procedimientos de inicio y fin de ciclo

**2. 112 tablas `*_temp` — de uso no confirmado**

`sac_*_temp` (98) y `cart_*_temp` (14). Por el nombre parecen el área de trabajo de los mapeos,
**pero no lo son**: de las 152 funciones de mapeo, sólo **una** menciona `_temp` y sólo 16 mencionan
`exp_s3` siquiera. Las funciones leen y escriben dentro de `trf_s3`.

Quién las usa está sin determinar. Trátalas como código de uso no confirmado, no como parte del
flujo de mapeos. Ver [G10_codigo_sin_llamadas](../G%20-%20Mapeos/G10_codigo_sin_llamadas.md).

**3. Un dominio de salida propio**

`api_*` (28), `alertas*`, `acumulado_de_gestion`, `fluxo*`, `novos*`… Éstas sí son tablas de salida,
pero de **otro consumidor**: alimentan las tareas `LOAD_QVD_*` del catálogo de Qlik (FIDC, KYC,
alertas), no los mapeos SAC y cartera.

### ⚠ Dónde NO están las tablas de destino de los mapeos

Las tablas finales de los mapeos —`sac_pl_cl_patrrf_t`, `cart_pos_rf_t`…— viven en **`trf_s3`**.

En `exp_s3` sólo existe su versión `_temp`. Buscar `exp_s3.sac_pl_cl_patrrf_t` devuelve «relation
does not exist»; lo que hay es `exp_s3.sac_pl_cl_patrrf_temp`, que es otra cosa.

```
trf_s3.sss_*            modelo de negocio
   ↓  función trf_s3.<nome_fn_mapeio>()
exp_s3.<tabla>_temp     área de trabajo
   ↓
trf_s3.sac_* / cart_*   destino final  ← Qlik lee de aquí
```

### Dónde está cada cosa dentro de `trf_s3`

`trf_s3` cumple **dos papeles a la vez**, y por eso tiene tantas tablas:

| Prefijo | Papel |
|---|---|
| `sss_` (291) | Modelo de negocio: referencial, activos, entidades |
| `sac_` (209) | **Salida de mapeos** hacia SAC |
| `cart_` (42) | **Salida de mapeos** de cartera y posiciones |
| `s3_` (16) | Control de interfaces |

Un mapeo lee de las `sss_*` y escribe en una `sac_*` o `cart_*`. **Origen y destino están en el
mismo esquema.**

### Recorrido completo de una fila

```
fichero plano
   ↓  \COPY
stg_s3.TABLA_TMP        ← aterrizaje
   ↓  validaciones
stg_s3.TABLA_T          ← dato bueno
stg_s3.TABLA_ERR        ← falló nulos o formato
stg_s3.TABLA_DES        ← falló integridad referencial
   ↓  transformación
trf_s3.sss_*            ← modelo de negocio
   ↓  mapeo  (función en exp_s3, destino en trf_s3)
trf_s3.sac_* / cart_*   ← tabla de salida
   ↓  Qlik lee por SQL directo y genera sus QVD
Qlik
```

Qlik **no lee de una capa intermedia**: su script de carga se conecta a la base y hace
`SELECT ... FROM trf_s3.<tabla>` directamente. Ver [H09_qlik_datos_de_ayer](../H%20-%20Cierre%20y%20Qlik/H09_qlik_datos_de_ayer.md).

## Cómo verificarlo

```sql
-- Tablas por esquema
SELECT table_schema, count(*)
FROM   information_schema.tables
WHERE  table_schema IN ('stg_s3','trf_s3','exp_s3')
GROUP  BY table_schema;

-- Familias de tabla dentro de trf_s3
SELECT split_part(table_name,'_',1) AS prefijo, count(*)
FROM   information_schema.tables
WHERE  table_schema = 'trf_s3'
GROUP  BY 1 ORDER BY 2 DESC;
```

## Ver también

[A03_glosario](../A%20-%20Orientacion/A03_glosario.md) · [A02_flujo_e2e_seis_pasos](../A%20-%20Orientacion/A02_flujo_e2e_seis_pasos.md) · [R1_02_donde_cae_cada_cosa](../R1%20-%20Descartes/R1_02_donde_cae_cada_cosa.md)

---
titulo: "I04 — Inventario de `exp_s3`"
familia: I
etapa: "Mapeos"
tipo: Referencia
tags:
  - familia/I
  - etapa/mapeos
  - tipo/referencia
keywords: "exp_s3, inventario, 195 tablas, control, api_, temp, FIDC"
---

# I04 — Inventario de `exp_s3`

**Etapa:** Mapeos
**Tipo:** Referencia
**Palabras clave:** exp_s3, inventario, 195 tablas, control, api_, temp, FIDC

## En una línea

195 tablas y 22 funciones, en **tres poblaciones distintas** que conviene no mezclar.

## Grupo 1 — Control del ciclo (6 tablas)

| Tabla | Para qué |
|---|---|
| `tablas_mapeio_t` | Qué mapeo corre: `activo_inactivo`, `is_fromtis`, `retry_deadlock` |
| `control_mapeio_t` | El contador `control_carga` por tabla y lote |
| `relaciontablacolumnas` | Qué columnas expone Qlik — 103 tablas, 1.722 columnas |
| `tabla_control` | Auditoría de recargas de Qlik (uso no confirmado) |

Más las secuencias `cod_seq_control_mapeio` y `controlflag_arquivos_cod_id_seq`.

Ver [G02_tablas_mapeio_activo](../G%20-%20Mapeos/G02_tablas_mapeio_activo.md) y [G08_fim_carga_mapeo](../G%20-%20Mapeos/G08_fim_carga_mapeo.md).

## Grupo 2 — 112 tablas `*_temp`

`sac_*_temp` (98) y `cart_*_temp` (14).

**Su uso no está confirmado.** Por el nombre parecen el área de trabajo de los mapeos, pero de las
152 funciones de mapeo **sólo una menciona `_temp`** y apenas 16 mencionan `exp_s3`: las funciones
leen y escriben dentro de `trf_s3`.

No las trates como parte del flujo de mapeos sin comprobarlo. Ver [G10_codigo_sin_llamadas](../G%20-%20Mapeos/G10_codigo_sin_llamadas.md).

## Grupo 3 — Dominio de salida propio (~77 tablas)

Éstas **sí** son tablas de salida, pero de otro consumidor:

| Familia | Nº | Contenido |
|---|---|---|
| `api_*` | 28 | Capa de API: consultas de administrador, cliente, gestor, script |
| `alertas*` | 4 | Alertas por escenario, listas internacionales, parecer |
| `fluxo*` | 6 | Flujo de caja proyectado |
| Otras | — | `acumulado_de_gestion`, `novos*`, `gestor*`, `relatorios*`, `vista*` |

Alimentan las tareas **`LOAD_QVD_*`** del catálogo de Qlik: `LOAD_QVD_ACUMULADODEGESTION`,
`LOAD_QVD_ALERTASPORCENARIO`, `LOAD_QVD_FLUXOCAIXA`, `KYC`, `FIDC`… Ver [H07_lookup_qlik](../H%20-%20Cierre%20y%20Qlik/H07_lookup_qlik.md).

Es un flujo **paralelo** al de los mapeos SAC y cartera, con sus propias tablas y su propio
consumidor.

## Las 22 funciones

| Estado | Cuántas | Cuáles |
|---|---|---|
| **Con llamador confirmado** | 4 | `incio_carga_mapeo_megara`, `fim_carga_mapeo_megara_ind`, `actualizar_tablas_y_control`, `actualizar_tablas_y_controlflag` |
| Sin llamador localizado | 18 | API de auditoría de Qlik (`inicio`, `fin`, `principio`, `completar`…), `fluxo_caixa_projectado*`, variantes de cierre |

Ver [G10_codigo_sin_llamadas](../G%20-%20Mapeos/G10_codigo_sin_llamadas.md).

## ⚠ Lo que NO está en `exp_s3`

**Las tablas finales de los mapeos.** Están en `trf_s3`. Aquí sólo existe su versión `_temp`.

```
exp_s3.sac_pl_cl_patrrf_temp    ← existe
exp_s3.sac_pl_cl_patrrf_t       ← NO existe
trf_s3.sac_pl_cl_patrrf_t       ← aquí está la buena
```

**Las funciones de mapeo.** Están en `trf_s3` como `function_meg_*`. Aquí sólo está el control que
dice cuáles ejecutar.

Es el error de modelo mental más fácil de cometer con este esquema.

## Consultas de inventario

```sql
SELECT split_part(table_name,'_',1) AS prefijo, count(*)
FROM   information_schema.tables WHERE table_schema = 'exp_s3'
GROUP  BY 1 ORDER BY 2 DESC LIMIT 15;

SELECT count(*) FILTER (WHERE table_name LIKE '%\_temp') AS temporales,
       count(*)                                          AS total
FROM   information_schema.tables WHERE table_schema = 'exp_s3';
```

## Ver también

[A05_esquemas_base_de_datos](../A%20-%20Orientacion/A05_esquemas_base_de_datos.md) · [I03_inventario_trf_s3](../I%20-%20Referencia%20de%20datos/I03_inventario_trf_s3.md) · [G10_codigo_sin_llamadas](../G%20-%20Mapeos/G10_codigo_sin_llamadas.md) · [G02_tablas_mapeio_activo](../G%20-%20Mapeos/G02_tablas_mapeio_activo.md) · [H07_lookup_qlik](../H%20-%20Cierre%20y%20Qlik/H07_lookup_qlik.md)

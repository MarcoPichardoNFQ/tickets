---
titulo: "K04 — FIDC, KYC y el dominio de alertas"
familia: K
etapa: "Mapeos"
tipo: Referencia
tags:
  - familia/K
  - etapa/mapeos
  - tipo/referencia
keywords: "FIDC, KYC, alertas, acumulado_de_gestion, api_, exp_s3, LOAD_QVD"
---

# K04 — FIDC, KYC y el dominio de alertas

**Etapa:** Mapeos
**Tipo:** Referencia
**Palabras clave:** FIDC, KYC, alertas, acumulado_de_gestion, api_, exp_s3, LOAD_QVD

## En una línea

Un flujo **paralelo** al de los mapeos SAC y cartera: sus tablas viven en `exp_s3` y alimentan
tareas de Qlik distintas.

## Dónde vive

En `exp_s3`, en el grupo de tablas que **no** son control ni `_temp` — unas 77:

| Familia | Nº | Contenido |
|---|---|---|
| `api_*` | 28 | Consultas de administrador, cliente, gestor, script, papel, moeda… |
| `alertas*` | 4 | `alertas_por_cenario`, `alertas_por_listas_internacional`, `alertas_por_parecer` |
| `fluxo*` | 6 | Flujo de caja proyectado |
| Otras | — | `acumulado_de_gestion`, `novos*`, `gestor*`, `relatorios*`, `vista*` |

Ver [I04_inventario_exp_s3](../I%20-%20Referencia%20de%20datos/I04_inventario_exp_s3.md).

## Cómo se conecta con Qlik

Los nombres de estas tablas **coinciden con las tareas globales del catálogo de Qlik**:

| Tabla en `exp_s3` | Tarea de Qlik |
|---|---|
| `acumulado_de_gestion` | `LOAD_QVD_ACUMULADODEGESTION` / `LOAD_UPDATE_ACUMULADODEGESTION` |
| `alertas_por_cenario` | `LOAD_QVD_ALERTASPORCENARIO` |
| `alertas_por_listas_internacional` | `LOAD_QVD_ALERTASPORLISTASINTERNACIONAL` |
| `alertas_por_parecer` | `LOAD_QVD_ALERTASPORPARECER` |
| `fluxo*` | `LOAD_QVD_FLUXOCAIXA` |
| — | `KYC`, `FIDC`, `SANTANDER CACEIS DATAHUB` |

Y las funciones `exp_s3.fluxo_caixa_projectado*` refuerzan la conexión: cuatro variantes cuyo nombre
coincide con `LOAD_QVD_FLUXOCAIXA`. Ver [H15_catalogo_tareas_qlik](../H%20-%20Cierre%20y%20Qlik/H15_catalogo_tareas_qlik.md) y [G10_codigo_sin_llamadas](../G%20-%20Mapeos/G10_codigo_sin_llamadas.md).

## Los ficheros de control

En `lookup_stg.txt` aparecen familias `.ctrl` propias:

```
FIDC_markedFiles.ctrl
KYC_markedFiles.ctrl
```

Confirman que FIDC y KYC tienen su propio flujo de entrada, con el mismo mecanismo de control que
BULLE y SAC.

```bash
awk -F'|' 'NF>8{print $8}' /nfq/data/cfg/lookup_stg.txt | sort -u | grep -iE "fidc|kyc"
```

## Un flujo paralelo, no una etapa

Lo que hay que retener:

```
XML + flags → conversión → stg_s3 → trf_s3 → mapeos → trf_s3.sac_*/cart_* → Qlik (INCREMENTAL_*)
ficheros    →              stg_s3 → …     →          exp_s3.api_*/alertas* → Qlik (LOAD_QVD_*)
```

**Dos caminos con destinos distintos y consumidores distintos.** Las fichas de mapeos —familia `G`—
describen el primero. Este dominio sigue el segundo.

## Estado de la documentación

Cobertura de orientación. **No he documentado el detalle interno de este flujo**: qué procedimiento
alimenta cada tabla `api_*`, ni la lógica de las alertas, ni el cálculo del flujo de caja.

Dos razones. Su código está mayoritariamente entre las **18 funciones de `exp_s3` sin llamador
localizado**, lo que impide afirmar qué está activo. Y su consumidor son tareas de Qlik distintas
de las que documenta la familia `H`.

Antes de dar por operativa cualquier pieza de este dominio, comprueba quién la llama.
Ver [G10_codigo_sin_llamadas](../G%20-%20Mapeos/G10_codigo_sin_llamadas.md).

## Comprobaciones útiles

```sql
-- ¿Tienen datos recientes estas tablas?
SELECT count(*) FROM exp_s3.acumulado_de_gestion;
SELECT count(*) FROM exp_s3.alertas_por_cenario;

-- ¿Se está usando la auditoría de recargas?
SELECT count(*), max(fin) FROM exp_s3.tabla_control;
```

Una `tabla_control` sin filas recientes indica que la instrumentación de este flujo ya no se usa.

## Ver también

[K01_bulle_sac_fidc](../K%20-%20BULLE%20SAC%20FIDC/K01_bulle_sac_fidc.md) · [I04_inventario_exp_s3](../I%20-%20Referencia%20de%20datos/I04_inventario_exp_s3.md) · [G10_codigo_sin_llamadas](../G%20-%20Mapeos/G10_codigo_sin_llamadas.md) · [H15_catalogo_tareas_qlik](../H%20-%20Cierre%20y%20Qlik/H15_catalogo_tareas_qlik.md)

---
titulo: "G04 — Los jobs `Mapeos` y `MapeosFlag`"
familia: G
etapa: "Mapeos"
tipo: Referencia
tags:
  - familia/G
  - etapa/mapeos
  - tipo/referencia
keywords: "Mapeos, MapeosFlag, jobref, paralelo, 001 - JOBs Mapeos, despacho"
---

# G04 — Los jobs `Mapeos` y `MapeosFlag`

**Etapa:** Mapeos
**Tipo:** Referencia
**Palabras clave:** Mapeos, MapeosFlag, jobref, paralelo, 001 - JOBs Mapeos, despacho

## En una línea

Dos jobs orquestadores que invocan, uno por uno pero en paralelo, los jobs individuales de cada
mapeo.

## Cómo están construidos

`Mapeos.xml` es una lista de referencias a otros jobs:

```xml
<command>
  <description>mapeo_cart_pos_rf_t</description>
  <jobref group='001 - JOBs Mapeos' name='14 mapeo_cart_pos_rf_t'>
    <useName>true</useName>
  </jobref>
</command>
```

Un bloque así por cada mapeo. Todos los jobs individuales viven en el grupo
**`001 - JOBs Mapeos`** y se llaman `<id> mapeo_<tabla_destino>`.

Consecuencia práctica: **para encontrar el job de un mapeo, busca por su número** en ese grupo de
Rundeck. Es la forma más rápida de llegar al log de una ejecución concreta.

## `Mapeos` vs `MapeosFlag`

Dos orquestadores con la misma estructura y distinto disparador. `MapeosFlag` pertenece al flujo
gobernado por los archivos flag; `Mapeos` al flujo general.

Ante una incidencia importa saber **cuál de los dos** debía ejecutar el mapeo afectado, porque
revisar el log del orquestador equivocado lleva a concluir que el mapeo nunca se lanzó.

## El paralelismo y su consecuencia

Los mapeos se ejecutan **simultáneamente**, decenas a la vez. Esto es intencionado —acorta mucho el
ciclo— y tiene dos efectos que hay que asumir:

**Los bloqueos mutuos son esperables.** Varios mapeos tocando las mismas tablas de `trf_s3` a la vez
producen deadlocks con regularidad. Por eso el reintento está parametrizado por mapeo en la tabla de
control. Un deadlock aislado que se resuelve con reintento **no es una incidencia**.
Ver [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md).

**El orden de finalización no es determinista.** Dos ejecuciones del mismo día pueden terminar en
orden distinto. No saques conclusiones de que un mapeo acabara antes o después que otro.

## Los mapeos que despacha

El listado de descripciones del job es el catálogo práctico de mapeos:

```
35 mapeo_sac_pl_cl_patrrf_t      14 mapeo_cart_pos_rf_t
16 mapeo_cart_caixa_mt_t          2 mapeo_sac_stat_cli_addr_t
 3 mapeo_cart_estat_administracao_t   4 mapeo_cart_estat_gestor_t
 ...
```

Los prefijos de la tabla destino agrupan por dominio:

| Prefijo | Dominio |
|---|---|
| `sac_` | Salida hacia el sistema SAC |
| `cart_` | Cartera y posiciones |

## ⚠ La lista del job y la tabla de control pueden no coincidir

Ésta es la comprobación más valiosa de esta ficha. El job de Rundeck contiene una lista **estática**
de referencias; la tabla `exp_s3.tablas_mapeio_t` contiene el catálogo **real** de mapeos activos.
Nada garantiza que estén sincronizados.

Un mapeo activo en la tabla pero ausente de la lista del job **no se ejecuta nunca**, y no deja
rastro de error: sencillamente nadie lo llama.

```sql
-- Catálogo real de activos, para contrastar con las descripciones del job
SELECT id_mapeo, nome_tabela_aldrin
FROM   exp_s3.tablas_mapeio_t
WHERE  activo_inactivo
ORDER  BY id_mapeo;
```

Compara ese resultado con la lista de pasos de `Mapeos` y `MapeosFlag` en Rundeck. Si el conteo no
cuadra, hay mapeos huérfanos en un sentido o en otro. Es una revisión que merece hacerse una vez y
documentar el resultado.

## Cómo verificarlo

En Rundeck: grupo `001 - JOBs Mapeos`, buscar por número. El histórico de ejecuciones de cada job
individual da la hora, la duración y el resultado de ese mapeo concreto.

## Ver también

[G01_que_es_un_mapeo](../G%20-%20Mapeos/G01_que_es_un_mapeo.md) · [G02_tablas_mapeio_activo](../G%20-%20Mapeos/G02_tablas_mapeio_activo.md) · [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md) · [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md) · [G03_control_inicio_carga_mapeo](../G%20-%20Mapeos/G03_control_inicio_carga_mapeo.md) · [G05_anatomia_job_mapeo](../G%20-%20Mapeos/G05_anatomia_job_mapeo.md)

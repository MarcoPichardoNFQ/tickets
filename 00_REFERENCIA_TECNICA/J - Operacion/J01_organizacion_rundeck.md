---
titulo: "J01 — Cómo está organizado Rundeck"
familia: J
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/J
  - etapa/transversal
  - tipo/referencia
keywords: "Rundeck, grupos, jobs, organización, dónde busco, jobref"
---

# J01 — Cómo está organizado Rundeck

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** Rundeck, grupos, jobs, organización, dónde busco, jobref

## En una línea

45 jobs en cuatro grupos, de los que **sólo 5 tienen horario propio**: el resto se ejecuta porque
otro los llama.

## Los grupos

| Grupo | Contenido |
|---|---|
| `00 - JOBs MEGARA Base` | Control del ciclo: `Control Inicio Carga Mapeo`, `STG StartOver`, `Procedimiento control finalizacion mapeos`, `_00001 Análise de erros` |
| `001 - JOBs Mapeos` | Un job por mapeo: `<id> mapeo_<tabla>`, más `Job control errores mapeo` |
| `999 - Bloques Optimizados` | Los 14 bloques `OptimizacioBloque*TRFySTG`, `Javas Bloque Estaticos/Dinamico`, `Mapeos` |
| `ArchivosFlag` | Flujo de flags: `CargaInformacion`, `JobsArchivosFlag`, `Validacion Cantidades Recibidas` |

## Lo que está programado

| Job | Cadencia |
|---|---|
| `0999 Carga Megara` | **Cada 3 segundos** — el vigilante de flags |
| `Main Job Megara` | Cada 10 min, minuto :04 |
| `CargaInformacion` | Cada 10 min, minuto :04 |
| `JobsArchivosFlag` | Cada 10 min, minuto :04 |
| `0999 Optimizacao Blocos V6` | Cada 10 min, minuto :04 — **excepto la hora 6** |

**Los otros 40 no tienen `<schedule>`.** Que aparezcan «sin programar» es normal: los invoca su
padre mediante `<jobref>`. Ver [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md).

## Cómo se encadenan

```xml
<jobref group='001 - JOBs Mapeos' name='14 mapeo_cart_pos_rf_t'>
  <useName>true</useName>
</jobref>
```

Un job padre contiene una lista de referencias. Consecuencia importante: **la lista es estática**,
mientras que el catálogo real de mapeos está en base de datos. Si no coinciden, hay mapeos que nunca
se llaman. Ver [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md).

## Cómo encontrar un job

| Busco… | Dónde |
|---|---|
| El job de un mapeo | Grupo `001 - JOBs Mapeos`, por su `id_mapeo` |
| El job de un bloque | Grupo `999 - Bloques Optimizados` |
| Dónde se carga una tabla | Por la **descripción del paso**: `0030 - LOAD STG MEG_TAX_PAYER_CAT_T,0040 - LOAD TRF TAX PAYER` |
| El flujo de flags | Grupo `ArchivosFlag` |

La descripción de cada paso de bloque dice en texto plano qué tabla carga y qué transforma. Es la
forma más rápida de localizar una interfaz. Ver [D07_bloques_optimizacio](../D%20-%20Carga%20STG/D07_bloques_optimizacio.md).

## El orden dentro de un job no es lineal

Los orquestadores llevan un grafo de dependencias declarado (`WorkflowStrategy` con reglas
`run-after`). Varios pasos corren en paralelo. Ver [G07_ciclo_completo_mapeos](../G%20-%20Mapeos/G07_ciclo_completo_mapeos.md).

## Zona horaria

Los jobs se programan en `GMT-3:00`, que coincide con el `AT TIME ZONE 'ADT'` de la traza de base de
datos. **Las horas son comparables** entre Rundeck y `aud_log_trace_t`, salvo en la ruta de
excepción. Ver [E08_log_trace_niveles](../E%20-%20Parametrizacion/E08_log_trace_niveles.md).

## ⚠ Duplicados en los exports

Hay ficheros con el mismo nombre y sufijos de duda:
`Job_control_errores_mapeo (verificar si es el mismo).xml`,
`Procedimiento_control_finalizacion_mapeos (1).xml`.

**Puede haber jobs duplicados en producción**, lo que explicaría alertas repetidas del mismo evento.
Merece comprobarse en la consola. Ver [G09_job_control_errores](../G%20-%20Mapeos/G09_job_control_errores.md).

## Ver también

[J02_orquestadores_raiz](../J%20-%20Operacion/J02_orquestadores_raiz.md) · [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md) · [G07_ciclo_completo_mapeos](../G%20-%20Mapeos/G07_ciclo_completo_mapeos.md) · [D07_bloques_optimizacio](../D%20-%20Carga%20STG/D07_bloques_optimizacio.md) · [R5_05_leer_log_job](../R5%20-%20Alertas%20Rundeck/R5_05_leer_log_job.md)

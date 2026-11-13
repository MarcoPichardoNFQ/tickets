---
titulo: "G07 — El ciclo completo, y por qué no es una secuencia lineal"
familia: G
etapa: "Mapeos"
tipo: Referencia
tags:
  - familia/G
  - etapa/mapeos
  - tipo/referencia
keywords: "WorkflowStrategy, run-after, paralelo, orden, dependencias, DAG, GMT-3"
---

# G07 — El ciclo completo, y por qué no es una secuencia lineal

**Etapa:** Mapeos
**Tipo:** Referencia
**Palabras clave:** WorkflowStrategy, run-after, paralelo, orden, dependencias, DAG, GMT-3

## En una línea

El orquestador no ejecuta sus pasos en fila: tiene un **grafo de dependencias declarado**, y varios
tramos corren en paralelo.

## El grafo

`0999 Optimizacao Blocos V6` define su orden con reglas explícitas:

```
[1]                 run-at-start
[22]                run-after:1
[2]                 run-after:22
[3]                 run-after:2
[4]                 run-after:3
[5]                 run-after:3          ← 4 y 5 en paralelo
[6]                 run-after:4
[7,8]               run-after:6          ← paralelo
[9,10,11]           run-after:7,8        ← paralelo
[12,13]             run-after:9,10,11    ← paralelo
[14,16]             run-after:12,13      ← paralelo
[15]                run-after:14
[17]                run-after:5,15,16    ← Mapeos espera a tres ramas
[18,19,20,23,24]    run-after:17         ← el cierre, TODO en paralelo
[21]                run-after:18,19,20,23,24
```

## Lo que hay que retener

**Los bloques no van uno detrás de otro.** Varios se ejecutan simultáneamente cuando sus
dependencias lo permiten. Por eso el tiempo total del ciclo es menor que la suma de los bloques, y
por eso los deadlocks entre mapeos son esperables. Ver [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md).

**Los mapeos (paso 17) esperan a tres ramas a la vez.** No arrancan hasta que terminan los bloques
estáticos y las dos últimas ramas de bloques. Si una sola de esas ramas se atasca, los mapeos no
empiezan — y el síntoma es «ningún mapeo corrió». Ver [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md).

**El cierre corre todo en paralelo.** Control de errores de mapeo, análisis de errores,
procedimiento de finalización, recarga de Qlik y validación de descartes **se lanzan a la vez**
cuando terminan los mapeos.

Esto último tiene una consecuencia concreta: **la recarga de Qlik no espera al procedimiento de
finalización**. Puede estar recargando mientras el control de cierre sigue ejecutándose. Si buscas
una relación de causa-efecto entre ambos, no la hay: son hermanos, no padre e hijo.

## La zona horaria del job

```xml
<timeZone>GMT-3:00</timeZone>
```

El job se programa en **GMT-3**, que coincide con el `AT TIME ZONE 'ADT'` que usa `LOG_TRACE` para
grabar. Así que las horas de Rundeck y las de la traza normal **sí son comparables**.

La excepción sigue siendo la ruta de error de `LOG_TRACE`, que usa `now()` a secas y depende de la
zona de la sesión de base de datos. Ver [E08_log_trace_niveles](../E%20-%20Parametrizacion/E08_log_trace_niveles.md) y [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md).

## Cómo leerlo al diagnosticar

En Rundeck, el detalle de ejecución muestra cada paso con su hora de inicio y fin. Con el grafo
delante se puede distinguir:

| Observación | Interpretación |
|---|---|
| Dos pasos con horas solapadas | Normal: están en la misma rama paralela |
| Un paso que empieza mucho después de terminar el anterior | Espera a otra rama que aún no acabó |
| Los mapeos no arrancan | Alguna de las tres ramas previas sigue en curso o falló |
| Todo el cierre a la misma hora | Normal: se lanzan juntos |

## El otro orquestador

`JobsArchivosFlag` tiene una estructura más corta —`CargaInformacion` y luego el cierre— pero el
mismo patrón: los pasos de cierre en paralelo. Ver [G04_jobs_mapeos](../G%20-%20Mapeos/G04_jobs_mapeos.md).

## Ver también

[D07_bloques_optimizacio](../D%20-%20Carga%20STG/D07_bloques_optimizacio.md) · [F06_dependencias_oleadas](../F%20-%20Transformacion%20TRF/F06_dependencias_oleadas.md) · [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md) · [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md) · [H01_cerrar_el_lote](../H%20-%20Cierre%20y%20Qlik/H01_cerrar_el_lote.md)

---
titulo: "I14 — Calendario: qué corre y con qué periodicidad"
familia: I
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/I
  - etapa/transversal
  - tipo/referencia
keywords: "calendario, periodicidad, diario, semanal, mensual, intradía, frecuencia"
---

# I14 — Calendario: qué corre y con qué periodicidad

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** calendario, periodicidad, diario, semanal, mensual, intradía, frecuencia

## En una línea

El sistema no tiene un ciclo diario: tiene **un bucle continuo** con cuatro periodicidades de flag
superpuestas.

## Las cuatro periodicidades

| Periodicidad | Flags | Cuándo esperarlos |
|---|---|---|
| **Intradía** | `MEGAACCOUNTING_IntraDay`, `MEGACUSTODY_IntraDay`, `MEGARAFA_IntraDay` | Varias veces al día |
| **Fin de día** | `MEGAACCOUNTING_EndOfDay`, `MEGACUSTODY_EndOfDay` | Cada día hábil |
| **Fin de semana** | `MEGAACCOUNTING_EndOfWeek`, `MEGACUSTODY_EndOfWeek` | Semanal |
| **Fin de mes** | `MEGAACCOUNTING_EndOfMonth`, `MEGARAFA_EndOfMonth` | Mensual |

Ver [B02_los_nueve_flags](../B%20-%20Recepcion%20y%20flags/B02_los_nueve_flags.md).

## El ritmo de la orquestación

| Job | Cadencia |
|---|---|
| `0999 Carga Megara` (vigilante de flags) | **Cada 3 segundos** |
| `Main Job Megara` | Cada 10 min, minuto :04 |
| `CargaInformacion` | Cada 10 min, minuto :04 |
| `JobsArchivosFlag` | Cada 10 min, minuto :04 |
| `0999 Optimizacao Blocos V6` | Cada 10 min, minuto :04 — **excepto la hora 6** |

Los otros 40 jobs no tienen horario: los invoca su padre. Ver [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md).

## El bucle

```
Rundeck pide ficheros a la API de Megara
   ↓
Megara genera el lote y lo deposita
   ↓
El vigilante detecta los flags (3 s)
   ↓
Cuando el set está completo, arranca la carga
   ↓
Bloques → mapeos → cierre → recarga de Qlik
   ↓
vuelta a empezar
```

No hay ventana nocturna: el ciclo se repite mientras haya trabajo.
Ver [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md).

## Cómo saber qué es normal para cada interfaz

La periodicidad teórica orienta, pero **lo que manda es el histórico real**:

```sql
-- Con qué frecuencia ha llegado este flag en 45 días
SELECT nome_base, data_recebemento::date AS dia, count(*)
FROM   stg_s3.controlflag_arquivos
WHERE  data > CURRENT_DATE - 45
GROUP  BY 1,2 ORDER BY 1, 2 DESC;
```

```sql
-- Y para una carga concreta
SELECT dat_load_date::date AS dia, count(*), sum(amt_register_process) AS filas
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_plan = :plan AND dat_load_date > CURRENT_DATE - 45
GROUP  BY 1 ORDER BY 1 DESC;
```

**Es la consulta que evita la mitad de los falsos positivos.** Un «PASO OMITIDO» en una interfaz que
sólo llega los viernes no es una incidencia de martes a jueves. Ver [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md).

## La frecuencia real varía enormemente

Medido sobre 30 días y 76 planes con actividad: desde **1 carga al mes hasta 145 al día**. No hay
una cadencia común; cada interfaz tiene la suya.

Los dos planes más frecuentes, `511` y `512`, se ejecutan 4.363 veces en 30 días — unas 145 diarias,
que coincide con el ciclo de 10 minutos durante todo el día. Ver [I15_volumetria_tipica](../I%20-%20Referencia%20de%20datos/I15_volumetria_tipica.md).

## La hora 6

`0999 Optimizacao Blocos V6` tiene su lista de horas como `0,1,2,3,4,5,7,8,…,23`. **Entre las 06:00
y las 06:59 no se dispara.** Si una incidencia aparece siempre a esa hora, no es casualidad.

## Ver también

[A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md) · [B02_los_nueve_flags](../B%20-%20Recepcion%20y%20flags/B02_los_nueve_flags.md) · [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md) · [I16_dias_habiles](../I%20-%20Referencia%20de%20datos/I16_dias_habiles.md) · [I15_volumetria_tipica](../I%20-%20Referencia%20de%20datos/I15_volumetria_tipica.md)

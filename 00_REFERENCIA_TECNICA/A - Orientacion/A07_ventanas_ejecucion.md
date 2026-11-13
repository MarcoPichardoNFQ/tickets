---
titulo: "A07 — Ventanas de ejecución: qué corre y cuándo"
familia: A
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/A
  - etapa/transversal
  - tipo/referencia
keywords: "horarios, schedule, cron, cada 10 minutos, ventanas, programación, Rundeck"
---

# A07 — Ventanas de ejecución: qué corre y cuándo

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** horarios, schedule, cron, cada 10 minutos, ventanas, programación, Rundeck

## En una línea

El sistema no corre una vez al día: cuatro orquestadores se despiertan **cada 10 minutos** y
comprueban si hay trabajo; el resto de jobs no tienen horario propio y se invocan en cadena.

## Detalle

### Lo que está programado

De los 46 jobs exportados, **sólo 5 tienen `<schedule>` propio**. Los demás se ejecutan porque
otro job los llama.

| Job | Cadencia |
|---|---|
| `Main Job Megara` | Cada 10 min, en el minuto :04 — todas las horas, todos los días |
| `CargaInformacion` | Cada 10 min, en el minuto :04 |
| `JobsArchivosFlag` | Cada 10 min, en el minuto :04 |
| `0999 -. Optimizacao Blocos Rundeck V6` | Cada 10 min, en el minuto :04 — **excepto la hora 6** |
| `0999 Carga Megara 2026-04-24` | **Cada 3 segundos**, todo el día |

«Minuto :04» significa `minute='4/10'`: se dispara en :04, :14, :24, :34, :44 y :54.

### Dos cosas que sorprenden y son intencionadas

**La hora 6 está excluida** en `0999 -. Optimizacao Blocos Rundeck V6`. Su lista de horas es
`0,1,2,3,4,5,7,8,...,23`. Entre las 06:00 y las 06:59 ese orquestador no se dispara. Si una
incidencia aparece siempre a esa hora, no es casualidad.

**Hay un job cada 3 segundos.** `0999 Carga Megara 2026-04-24` usa `seconds='0/3'` con hora y
minuto comodín: se ejecuta 20 veces por minuto. Es el vigilante de presencia de archivos flag.
Un fallo en ese job genera ruido enorme muy rápido.

### Lo que no tiene horario

Los 41 jobs restantes —los bloques `OptimizacioBloque*TRFySTG`, los `Flag_MEGA*`, `Mapeos`,
`MapeosFlag`, `STG StartOver`, las validaciones de cierre— **se invocan desde otro job**. Que un
job no tenga schedule no significa que esté parado; significa que depende de que su padre lo llame.

Consecuencia para diagnóstico: si un bloque no se ejecutó, la pregunta no es «¿está programado?»
sino «¿quién debía llamarlo y por qué no lo hizo?».

### Ritmo real del sistema

El diseño es de **sondeo continuo**, no de ventana nocturna. Los orquestadores comprueban cada 10
minutos si hay flag nuevo o trabajo pendiente y actúan. Por eso un fichero que llega a las 15:20
empieza a procesarse hacia las 15:24, no al día siguiente.

### Zona horaria de las trazas

`LOG_TRACE()` graba con `now() AT TIME ZONE 'ADT'` (UTC-3). La ruta de excepción, en cambio, usa
`now()` a secas, que depende de la zona horaria de la sesión de base de datos. Si ambas no
coinciden verás saltos de horas entre mensajes normales y mensajes de error en la misma tabla.

```sql
SHOW timezone;   -- compara con UTC-3 antes de correlacionar horas
```

## Cómo verificarlo

En Rundeck, filtra por jobs con schedule habilitado. En el export XML es el bloque:

```xml
<schedule>
  <time hour='...' minute='4/10' seconds='0' />
</schedule>
<scheduleEnabled>true</scheduleEnabled>
```

## Ver también

[A02_flujo_e2e_seis_pasos](../A%20-%20Orientacion/A02_flujo_e2e_seis_pasos.md) · [A04_rutas_y_directorios](../A%20-%20Orientacion/A04_rutas_y_directorios.md) · [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md)

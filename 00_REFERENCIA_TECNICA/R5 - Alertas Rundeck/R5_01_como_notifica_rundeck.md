---
titulo: "R5.01 — Cómo notifica Rundeck"
familia: R5
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/R5
  - etapa/transversal
  - tipo/referencia
keywords: "notificación, onfailure, onstart, onsuccess, onavgduration, email, attachLog"
---

# R5.01 — Cómo notifica Rundeck

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** notificación, onfailure, onstart, onsuccess, onavgduration, email, attachLog

## En una línea

Rundeck avisa sólo por correo, y sólo desde los jobs que tienen notificación configurada — que no
son todos.

## Los cuatro disparadores

| Disparador | Cuándo salta | Cuántos jobs lo usan |
|---|---|---|
| `onfailure` | El job termina con error | **22** |
| `onstart` | El job empieza | 2 |
| `onsuccess` | El job termina bien | 1 |
| `onavgduration` | El job tarda más de lo habitual | 1 |

Ejemplo real, del job de validación de cantidades:

```xml
<notification>
  <onfailure>
    <email recipients='...' subject='URGENTE no se recibieron todas las interfaces' />
  </onfailure>
</notification>
```

## Lo que hay que saber para interpretar una alerta

**El asunto lo define el job, no el error.** El texto `URGENTE no se recibieron todas las interfaces`
está escrito en la definición del job y se manda **siempre** que ese job falle, sea cual sea la
causa real. Un job puede fallar por un problema de conexión y mandar un asunto que habla de
interfaces. **No diagnostiques por el asunto.**

**Sólo hay correo.** No hay integración con sistemas de tickets, ni chat, ni telefonía. Si nadie
lee el buzón, la alerta se pierde.

**Algunos adjuntan el log y otros no.** El atributo `attachLog='true' attachLogInFile='true'`
aparece en cuatro configuraciones. Las alertas sin log obligan a entrar en Rundeck para ver qué
pasó. Ver [R5_04_alertas_con_y_sin_log](../R5%20-%20Alertas%20Rundeck/R5_04_alertas_con_y_sin_log.md).

**`onavgduration` sólo está en un job.** La detección de ejecuciones anormalmente lentas cubre un
único caso de los 46.

## La cobertura real

De los 46 jobs exportados, **24 tienen notificación y 22 no tienen ninguna**.

Eso significa que **casi la mitad de los jobs del sistema fallan en silencio**. Ver [R5_02_jobs_sin_notificacion](../R5%20-%20Alertas%20Rundeck/R5_02_jobs_sin_notificacion.md).

## Cómo comprobarlo

En Rundeck, cada job muestra su configuración de notificaciones en la pestaña correspondiente. Sobre
los exports XML:

```bash
cd <directorio de exports>
grep -l "<notification>" *.xml | wc -l     # jobs con notificación
ls *.xml | wc -l                           # total
grep -h -A2 "<notification>" *.xml | grep -oE "<(onfailure|onstart|onsuccess|onavgduration)>" | sort | uniq -c
```

## Ver también

[R5_02_jobs_sin_notificacion](../R5%20-%20Alertas%20Rundeck/R5_02_jobs_sin_notificacion.md) · [R5_03_listas_distribucion](../R5%20-%20Alertas%20Rundeck/R5_03_listas_distribucion.md) · [R5_04_alertas_con_y_sin_log](../R5%20-%20Alertas%20Rundeck/R5_04_alertas_con_y_sin_log.md) · [R5_09_catalogo_alertas](../R5%20-%20Alertas%20Rundeck/R5_09_catalogo_alertas.md)

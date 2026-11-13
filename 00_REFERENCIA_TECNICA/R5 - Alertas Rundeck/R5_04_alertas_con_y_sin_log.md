---
titulo: "R5.04 — Alertas con log adjunto y sin él"
familia: R5
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/R5
  - etapa/transversal
  - tipo/referencia
keywords: "attachLog, adjunto, correo, log en el correo, diagnóstico rápido"
---

# R5.04 — Alertas con log adjunto y sin él

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** attachLog, adjunto, correo, log en el correo, diagnóstico rápido

## En una línea

Cuatro configuraciones de notificación adjuntan el log al correo; el resto obliga a entrar en
Rundeck para saber qué pasó.

## La diferencia

```xml
<!-- Con log adjunto -->
<email attachLog='true' attachLogInFile='true' recipients='...' />

<!-- Sin log -->
<email recipients='...' />
```

| Atributo | Efecto |
|---|---|
| `attachLog='true'` | Incluye la salida en el cuerpo del correo |
| `attachLogInFile='true'` | La adjunta además como fichero |

Sólo **cuatro** configuraciones de las que existen llevan ambos atributos. Las demás mandan un
correo con asunto y poco más.

## Qué implica en la práctica

**Con log adjunto** puedes hacer el primer triaje desde el correo: ver el mensaje de error, en qué
paso ocurrió, y decidir si es ruido conocido. Eso ahorra la mitad del tiempo de respuesta.

**Sin log** el correo sólo dice «este job falló». Hay que:

1. Entrar en Rundeck
2. Localizar la ejecución por fecha y hora
3. Abrir el detalle paso a paso

## El asunto no es diagnóstico

Con log o sin él, **el asunto está escrito en la definición del job y se manda siempre igual**, sea
cual sea la causa. `URGENTE no se recibieron todas las interfaces` se envía también cuando el fallo
fue de conexión.

**No diagnostiques por el asunto.** Ver [R5_09_catalogo_alertas](../R5%20-%20Alertas%20Rundeck/R5_09_catalogo_alertas.md).

## Qué buscar en un log adjunto

| Patrón | Significa |
|---|---|
| `PASO OMITIDO` | Interfaz sin fichero. Suele ser ruido → [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md) |
| `ERROR CRÍTICO: Carga incompleta` | Faltan prefijos de la lista oficial → [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md) |
| `ArchivoAyudaRundeckMegara NO contiene 1` | **El ciclo está apagado** → [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md) |
| `[Ljava.lang.StackTraceElement;@...` | Error del conversor, ilegible → [C12_conversion_fallo_log](../C%20-%20Conversion%20Java/C12_conversion_fallo_log.md) |
| `NO es válido. Razón:` | Fallo de validación XSD → [C09_xml_no_valida](../C%20-%20Conversion%20Java/C09_xml_no_valida.md) |
| `Eliminando los archivos generados` | La conversión abortó y borró su salida → [C06_ficheros_de_salida](../C%20-%20Conversion%20Java/C06_ficheros_de_salida.md) |
| `Tabla % Contiene por lo menos 1 regitro descartado` | Duplicados de mapeo → [H03_validacion_descartes](../H%20-%20Cierre%20y%20Qlik/H03_validacion_descartes.md) |

Esa tabla convierte un log adjunto en un diagnóstico de treinta segundos.

## Material de escalado

Añadir `attachLog='true'` a las notificaciones que no lo tienen es un cambio de configuración
barato con retorno inmediato en tiempo de respuesta. Junto con los **22 jobs que no notifican
nada**, es la mejora más rentable de la monitorización actual. Ver [R5_02_jobs_sin_notificacion](../R5%20-%20Alertas%20Rundeck/R5_02_jobs_sin_notificacion.md).

## Ver también

[R5_01_como_notifica_rundeck](../R5%20-%20Alertas%20Rundeck/R5_01_como_notifica_rundeck.md) · [R5_05_leer_log_job](../R5%20-%20Alertas%20Rundeck/R5_05_leer_log_job.md) · [R5_09_catalogo_alertas](../R5%20-%20Alertas%20Rundeck/R5_09_catalogo_alertas.md) · [R5_02_jobs_sin_notificacion](../R5%20-%20Alertas%20Rundeck/R5_02_jobs_sin_notificacion.md)

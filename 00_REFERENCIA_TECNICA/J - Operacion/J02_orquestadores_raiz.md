---
titulo: "J02 — Los orquestadores raíz"
familia: J
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/J
  - etapa/transversal
  - tipo/referencia
keywords: "Main Job Megara, CargaInformacion, JobsArchivosFlag, 0999, raíz, quién llama"
---

# J02 — Los orquestadores raíz

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** Main Job Megara, CargaInformacion, JobsArchivosFlag, 0999, raíz, quién llama

## En una línea

Cinco jobs programados sostienen todo el sistema; los otros 40 dependen de ellos.

## Los cinco

### `0999 Carga Megara 2026-04-24` — el vigilante

**Cada 3 segundos**, todo el día. Su primer paso es `Validacion constante presencia archivos flag`.

Es el más crítico del sistema: **si deja de correr, nada se detecta y nada avanza**. Y un fallo
persistente genera miles de alertas por hora, así que ante una avalancha de correos del mismo job,
es éste. Ver [B04_job_validacion_constante](../B%20-%20Recepcion%20y%20flags/B04_job_validacion_constante.md).

### `0999 -. Optimizacao Blocos Rundeck V6` — el ciclo completo

Cada 10 min en el minuto :04, **excepto la hora 6**. Es el orquestador principal: arranque de
mapeos, conversiones Java, los 14 bloques, mapeos y los cinco pasos de cierre.

Lleva un grafo de dependencias declarado, con tramos en paralelo. Ver [G07_ciclo_completo_mapeos](../G%20-%20Mapeos/G07_ciclo_completo_mapeos.md).

### `JobsArchivosFlag` — el ciclo por flags

Cada 10 min en el minuto :04. Estructura más corta: `CargaInformacion`, control de errores, análisis,
finalización **variante Flag**, recarga de Qlik y validación de descartes.

### `Main Job Megara` y `CargaInformacion`

Cada 10 min en el minuto :04. Orquestadores del flujo general de carga.

## Los dos ciclos que conviven

| | `0999 Optimizacao Blocos V6` | `JobsArchivosFlag` |
|---|---|---|
| Cierre | `Procedimiento control finalizacion mapeos` | …`mapeos Flag` |
| Mapeos | `Mapeos` | vía `CargaInformacion` |
| Función de cierre | `actualizar_tablas_y_control()` | `actualizar_tablas_y_controlflag()` |

**Ante una incidencia, comprueba cuál de los dos estaba en curso.** Revisar el log del equivocado
lleva a concluir que algo no corrió cuando sí lo hizo. Ver [H05_actualizar_tablas_y_control](../H%20-%20Cierre%20y%20Qlik/H05_actualizar_tablas_y_control.md).

## Cómo saber si el sistema está vivo

```
1. ¿El vigilante se está ejecutando?     ← lo más importante
2. ¿Hay ejecuciones recientes de los orquestadores de 10 min?
3. ¿Está el ciclo encendido?
```

Para el punto 3:

```bash
cat /nfq/data/cfg/ArchivoAyudaRundeckMegara.txt
```

Cualquier cosa que no sea `1` detiene la petición de ficheros a Megara **y el job sale en verde**.
Ver [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md).

Y en base de datos, la señal de que el ciclo avanza:

```sql
SELECT max(dat_load_date) AS ultima_carga FROM stg_s3.aud_load_trace_t;
SELECT max(data) AS ultimo_flag FROM stg_s3.controlflag_arquivos;
```

## Ninguno de los cinco es inocuo al relanzar

Relanzar un orquestador raíz ejecuta **todo su árbol**: decenas de cargas, transformaciones y
mapeos. Para recuperar una pieza concreta, relanza su job individual.
Ver [J03_relanzar_seguro](../J%20-%20Operacion/J03_relanzar_seguro.md).

## Ver también

[J01_organizacion_rundeck](../J%20-%20Operacion/J01_organizacion_rundeck.md) · [B04_job_validacion_constante](../B%20-%20Recepcion%20y%20flags/B04_job_validacion_constante.md) · [G07_ciclo_completo_mapeos](../G%20-%20Mapeos/G07_ciclo_completo_mapeos.md) · [J03_relanzar_seguro](../J%20-%20Operacion/J03_relanzar_seguro.md) · [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md)

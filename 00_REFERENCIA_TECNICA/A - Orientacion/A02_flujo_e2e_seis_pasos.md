---
titulo: "A02 — El flujo de punta a punta: los 6 pasos"
familia: A
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/A
  - etapa/transversal
  - tipo/referencia
keywords: "flujo, end to end, etapas, pipeline, recorrido del dato"
---

# A02 — El flujo de punta a punta: los 6 pasos

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** flujo, end to end, etapas, pipeline, recorrido del dato

## En una línea

XML + flag → conversión Java a texto plano → `\COPY` a `stg_s3` → validación y apartado de
descartes → transformación a `trf_s3` → mapeos a `trf_s3` → recarga de Qlik.

## Detalle

### Paso 1 — Recepción y detección de flags

Llegan los XML de negocio y un archivo **flag** que declara el lote. Rundeck vigila el directorio
de forma constante. Los flags conocidos son 9, listados en `/nfq/data/cfg/lookupflags.txt`.

- Jobs: `Validacion constante presencia archivos flag`, `Manejo Flag`, `LlamadaTablaControlArquivosFlag`, y un job por flag (`Flag_MEGAACCOUNTING_*`, `Flag_MEGACUSTODY_*`)
- Scripts: `load_filesflag_script.sh`, `load_filesflag_option_script.sh`
- Tablas: `stg_s3.controlflag_arquivos`, `stg_s3.controlflag_interfaces`

### Paso 2 — Conversión XML (capa Java)

Cada XML se valida contra su XSD y se convierte a texto plano separado por `!`.
Un XML genera **varios** ficheros de salida, uno por tipo de nodo.

- Script: `load_java_script.sh` (ejecuta `xmllint`, `xmlConversor.jar` y cifra el original con `gpg`)
- Lookup: `/nfq/data/cfg/lookup_java.txt`
- Jobs: agrupados en `Javas Bloque Estaticos` y `Javas Bloque Dinamico`, con ~132 micro-jobs de conversión

### Paso 3 — Carga a staging

Los planos entran por `\COPY` a una tabla temporal `_TMP` y de ahí a la tabla `_T`.

- Script: `load_stgtrf_script.sh`, función `stg()`
- Lookup: `/nfq/data/cfg/lookup_stg.txt`
- Tablas maestras: `PAR_LOAD_PLAN_T`, `PAR_MAESTRO_TABLAS_T`, `PAR_MAESTRO_COLUMNAS_T`
- Funciones: `read_header_fn()`, `run_load_plan_pc()`

### Paso 3.1 — Validación y apartado de descartes

Antes de dar por buena la carga se validan nulos, formato e integridad referencial.
Lo que falla se aparta a `_ERR` o `_DES` según el caso. Ver [R1_02_donde_cae_cada_cosa](../R1%20-%20Descartes/R1_02_donde_cae_cada_cosa.md).

- Función orquestadora: `stg_s3.validate_gen_pc()`
- Tablas maestras: `PAR_MAESTRO_MASK_T` (formatos), `PAR_MAESTRO_VALID_T` (claves foráneas)

### Paso 4 — Transformación

Los datos sanos se consolidan en el modelo de negocio, dentro del esquema `trf_s3`.

- Script: `load_stgtrf_script.sh`, función `trf()`
- Lookup: `/nfq/data/cfg/lookup_trf.txt`
- Jobs: los mismos `OptimizacioBloque*TRFySTG` del paso 3
- Traza: todo procedimiento llama a `stg_s3.LOG_TRACE()`

### Paso 5 — Mapeos

Se construyen las tablas consolidadas de salida —`trf_s3.sac_*` y `trf_s3.cart_*`— en paralelo masivo. `exp_s3` sólo aloja el control y las funciones.

- Jobs orquestadores: `Mapeos` y `MapeosFlag`
- Control: `exp_s3.tablas_mapeio_t` (columna `activo_inactivo`)
- Mecánica crítica: captura de `SQLSTATE '40P01'` (deadlock) con reintento por `pg_sleep()`

### Paso 6 — Cierre y Qlik

Se comprueba que el lote está completo, se limpia staging y se recargan las tareas de Qlik.

- Jobs: `STG StartOver`, `Validacion Cantidades Recibidas`, `Job control errores mapeo`, `Procedimiento control finalizacion mapeos`
- Limpieza: `stg_s3.cleanup_meg_t()`
- Qlik: 265 tareas catalogadas en `/nfq/data/cfg/lookup_qlik.txt`, cada una con su UUID

## Cómo verificarlo

Para saber en qué paso está una carga concreta, `des_process_executed` de `aud_load_trace_t`
acumula el recorrido separado por `|`:

```sql
SELECT cod_load_trace, des_file_loaded, step_load, des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  dat_load_date::date = CURRENT_DATE
ORDER  BY dat_load_date DESC;
```

## Ver también

[A01_que_es_aldrin](../A%20-%20Orientacion/A01_que_es_aldrin.md) · [A04_rutas_y_directorios](../A%20-%20Orientacion/A04_rutas_y_directorios.md) · [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md) · [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md)

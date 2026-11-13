---
titulo: "A03 — Glosario de términos y sufijos"
familia: A
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/A
  - etapa/transversal
  - tipo/referencia
keywords: "glosario, siglas, sufijos, _T, _DES, _ERR, _TMP, STG, TRF, EXP, flag, bloque, mapeo"
---

# A03 — Glosario de términos y sufijos

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** glosario, siglas, sufijos, _T, _DES, _ERR, _TMP, STG, TRF, EXP, flag, bloque, mapeo

## En una línea

Diccionario mínimo para leer cualquier nombre de tabla, job o script del sistema.

## Detalle

### Los dos nombres que no hay que confundir

| Término | Qué es |
|---|---|
| **Aldrin** | El sistema documentado en este vault: el ETL que recibe, convierte, valida, carga, transforma y publica. Todo lo que corre en Rundeck + PostgreSQL + Qlik es Aldrin. |
| **Megara** | El sistema **origen** (custodia, S3 CACEIS): genera los XML del lote (MegaCommon/innotech) y expone las APIs `MegaAccounting`/`MegaCustody` a las que Rundeck pide los ficheros. Aldrin consume lo que Megara produce. |

### Esquemas

| Término | Qué es |
|---|---|
| `stg_s3` | **Staging.** Donde aterriza el dato crudo desde los ficheros planos. ~1.322 tablas. |
| `trf_s3` | **Transformación.** El modelo de negocio ya consolidado. ~638 tablas. |
| `exp_s3` | **Control de mapeos.** Aloja las funciones `mapeo_*` y sus tablas de control. **No contiene tablas de salida.** |

Ojo: `sss`, `sac`, `cart`, `cs`, `fa` **no son esquemas**, son prefijos de nombre de tabla dentro
de `trf_s3`. Ver [A05_esquemas_base_de_datos](../A%20-%20Orientacion/A05_esquemas_base_de_datos.md).

### Sufijos de tabla

| Sufijo | Qué contiene |
|---|---|
| `_TMP` | Tabla temporal de aterrizaje. El `\COPY` escribe aquí primero. |
| `_T` | Tabla definitiva. El dato bueno acaba aquí. |
| `_ERR` | Filas con **error**: se copian aquí y se borran de la tabla base. |
| `_DES` | Filas **descartadas** por integridad referencial. Upsert por clave primaria. |
| `MEG_` | Prefijo de tablas del ciclo Megara, candidatas a limpieza en el cierre. |

La diferencia entre `_ERR` y `_DES` no es de gravedad sino de **qué validación falló**:
ver [R1_02_donde_cae_cada_cosa](../R1%20-%20Descartes/R1_02_donde_cae_cada_cosa.md).

### Conceptos de proceso

| Término | Qué significa |
|---|---|
| **Flag** | Archivo de control que anuncia que un lote de XML está completo y puede procesarse. Hay 9. |
| **Interfaz** | Cada tipo de fichero de negocio (`AccountCategory`, `Bond`, `CGCPosition`…). ~129 interfaces `MEGA*`. |
| **Bloque** | Agrupación de cargas que se ejecutan juntas y en orden. Los jobs `OptimizacioBloque*TRFySTG`. Hay 14. |
| **Mapeo** | Proceso que construye una tabla de salida en `trf_s3` (`sac_*`, `cart_*`) a partir del modelo de negocio. Se identifican por `id_mapeo`. |
| **Load plan** | Fila de `PAR_LOAD_PLAN_T` que define cómo se carga un fichero: origen, destino, separador, nº de columnas, tolerancia. |
| **Load trace** | Identificador de una ejecución de carga concreta (`cod_load_trace`). Es la unidad de rastreo. |
| **Descarte** | Fila apartada por no cumplir una validación. No para el proceso. |

### Códigos de estado

| `cod_status` | Significado |
|---|---|
| `0` | Correcto |
| `1` | Validación fallida, filas apartadas, el proceso continúa |
| `-1` | Error: el proceso se detiene o la tabla se trunca |

### Niveles de log

`LOG_TRACE()` recibe un nivel: **1 = ALTO** (más detalle), **2 = MEDIO**, **3 = BAJO**.
El filtro es `PAR_MAESTRO_LOG_LEVEL_T.cod_log_level <= nivel_del_mensaje`, así que un valor
configurado **alto** produce **menos** mensajes. Contraintuitivo, pero es así.

## Cómo verificarlo

```sql
-- Nivel de log configurado actualmente
SELECT * FROM stg_s3.par_maestro_log_level_t;
```

## Ver también

[A05_esquemas_base_de_datos](../A%20-%20Orientacion/A05_esquemas_base_de_datos.md) · [R1_02_donde_cae_cada_cosa](../R1%20-%20Descartes/R1_02_donde_cae_cada_cosa.md) · [A01_que_es_aldrin](../A%20-%20Orientacion/A01_que_es_aldrin.md)

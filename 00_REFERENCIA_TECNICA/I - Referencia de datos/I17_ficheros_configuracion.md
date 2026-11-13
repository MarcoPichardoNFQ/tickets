---
titulo: "I17 — Índice de ficheros de configuración"
familia: I
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/I
  - etapa/transversal
  - tipo/referencia
keywords: "configuración, ficheros, cfg, lookups, credenciales, dónde está"
---

# I17 — Índice de ficheros de configuración

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** configuración, ficheros, cfg, lookups, credenciales, dónde está

## En una línea

Todo lo que gobierna el sistema fuera de la base de datos está en `/nfq/data/cfg/`.

## `/nfq/data/cfg/`

| Fichero | Gobierna | Ficha |
|---|---|---|
| `env.properties` | Rutas, directorios, clave de cifrado | [A04_rutas_y_directorios](../A%20-%20Orientacion/A04_rutas_y_directorios.md) |
| `db_config_gral.env` | 🔒 `DB_CONN` — la conexión a la base | — |
| `credentials.properties` | 🔒 Credenciales de base de datos | — |
| `reload_task.credentials` | 🔒 `QLIK_HOST`, `QLIK_USER`, `QLIK_XRFKEY` | [H08_recarga_qlik](../H%20-%20Cierre%20y%20Qlik/H08_recarga_qlik.md) |
| `lookupflags.txt` | Los 9 flags y su directorio | [B02_los_nueve_flags](../B%20-%20Recepcion%20y%20flags/B02_los_nueve_flags.md) |
| `lookup_java.txt` | Conversión XML (vía manual) | [C03_lookup_java_formato](../C%20-%20Conversion%20Java/C03_lookup_java_formato.md) |
| `lookup_java_flag.txt` | Conversión XML (vía flag) | [C03_lookup_java_formato](../C%20-%20Conversion%20Java/C03_lookup_java_formato.md) |
| `lookup_stg.txt` | Carga a staging — 573 líneas | [D02_lookup_stg_formato](../D%20-%20Carga%20STG/D02_lookup_stg_formato.md) |
| `lookup_trf.txt` | Transformación — 582 líneas | [F02_lookup_trf_formato](../F%20-%20Transformacion%20TRF/F02_lookup_trf_formato.md) |
| `lookup_qlik.txt` | Catálogo de tareas Qlik — **no lo lee nadie** | [H07_lookup_qlik](../H%20-%20Cierre%20y%20Qlik/H07_lookup_qlik.md) |
| **`ArchivoAyudaRundeckMegara.txt`** | **Interruptor general del ciclo** | [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md) |
| `client.pem` / `client_key.pem` | Certificados de cliente para Qlik | [H08_recarga_qlik](../H%20-%20Cierre%20y%20Qlik/H08_recarga_qlik.md) |

## Scripts en `/nfq/data/cfg/`

| Script | Qué hace |
|---|---|
| `load_filesflag_script.sh` | Procesa el flag y registra las interfaces |
| `load_filesflag_option_script.sh` | Variante |
| `load_java_script.sh` | Conversión XML, vía manual |
| `load_java2_optiflag_script.sh` | Conversión XML, vía flag |
| `load_stgtrf_script.sh` | Carga a staging y transformación |
| `LLamada Rundeck Flags Obligatorios.sh` | Pide ficheros a la API de Megara |

## `/nfq/XMLconversor/`

| Elemento | Qué es |
|---|---|
| `xmlConversor.jar` | El conversor |
| `config.properties` | `output=/DIR_SSS_LOCAL/`, `separator=!`, `encoding=UTF-8` |
| `xsd/` | Los esquemas, uno por interfaz |

**`config.properties` se lee con ruta relativa**: el conversor debe lanzarse desde este directorio.
Ver [C01_que_hace_xmlconversor](../C%20-%20Conversion%20Java/C01_que_hace_xmlconversor.md).

## Los tres ficheros que más incidencias explican

**`ArchivoAyudaRundeckMegara.txt`.** Si no contiene `1`, el sistema deja de pedir ficheros a Megara
y **el job sale en verde**. Primera comprobación ante «hace horas que no llega nada».

```bash
cat /nfq/data/cfg/ArchivoAyudaRundeckMegara.txt
```

**`lookup_stg.txt`.** El patrón de fichero de cada carga. Un patrón que ya no casa con el nombre que
manda el origen produce «PASO OMITIDO» todos los días.

**`env.properties`.** Todas las rutas. Si algo se busca donde no es, empieza aquí.

## Dónde NO está la configuración

Buena parte del comportamiento **no está en ficheros sino en tablas**:

| Comportamiento | Dónde |
|---|---|
| Qué columnas se cargan y su orden | `PAR_MAESTRO_COLUMNAS_T` |
| Qué campos son obligatorios o clave | `PAR_MAESTRO_COLUMNAS_T` |
| Formatos válidos | `PAR_MAESTRO_MASK_T` |
| Integridad referencial | `PAR_MAESTRO_VALID_T` |
| Tolerancia ante fallo | `PAR_LOAD_PLAN_T.valid_err_des` |
| Qué mapeo corre | `exp_s3.tablas_mapeio_t` |
| Qué columnas ve Qlik | `exp_s3.relaciontablacolumnas` |

Ver [E01_tablas_par_metadata_driven](../E%20-%20Parametrizacion/E01_tablas_par_metadata_driven.md) y [I05_tablas_control_auditoria](../I%20-%20Referencia%20de%20datos/I05_tablas_control_auditoria.md).

Y dos casos codificados **dentro del código**, que no se pueden cambiar sin tocarlo:

- La lista de ~130 prefijos obligatorios, en el script de shell. Ver [I06_catalogo_interfaces_mega](../I%20-%20Referencia%20de%20datos/I06_catalogo_interfaces_mega.md)
- El lote de referencia `29817` de la validación de cantidades. Ver [R4_03_validacion_cantidades](../R4%20-%20Sets%20incompletos/R4_03_validacion_cantidades.md)

## Ver también

[A04_rutas_y_directorios](../A%20-%20Orientacion/A04_rutas_y_directorios.md) · [E01_tablas_par_metadata_driven](../E%20-%20Parametrizacion/E01_tablas_par_metadata_driven.md) · [I05_tablas_control_auditoria](../I%20-%20Referencia%20de%20datos/I05_tablas_control_auditoria.md) · [J04_que_no_tocar](../J%20-%20Operacion/J04_que_no_tocar.md)

---
titulo: "A04 — Mapa de rutas y directorios de producción"
familia: A
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/A
  - etapa/transversal
  - tipo/referencia
keywords: "rutas, directorios, env.properties, DIR_FLAG, DIR_PROCESSED, DIR_UNMATCHED, bucket, cfg"
---

# A04 — Mapa de rutas y directorios de producción

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** rutas, directorios, env.properties, DIR_FLAG, DIR_PROCESSED, DIR_UNMATCHED, bucket, cfg

## En una línea

Todo el sistema lee sus rutas de `/nfq/data/cfg/env.properties`; los ficheros viajan de un
directorio de llegada a `OK`, y de ahí a `PROCESSED` o a `UNMATCHED`.

## Detalle

### El fichero de configuración raíz

`/nfq/data/cfg/env.properties` — todos los scripts hacen `. $env` sobre él. Contenido:

| Variable | Valor | Para qué |
|---|---|---|
| `bucket` | `/mnt/nfqbucket/DIR_SSS/` | Almacenamiento montado |
| `fileshare` | `/prddatahub/` | Raíz del recurso compartido |
| `raiz` | `/DIR_SSS_LOCAL/` | Raíz local |
| `temp` | `/prddatahub/DIR_SSS/OK/` | Ficheros listos para procesar |
| `destino` | `/prddatahub/DIR_UNMATCHED/` | Ficheros que no casan con nada esperado |
| `processed` | `/prddatahub/DIR_PROCESSED/` | Ficheros ya procesados |
| `bandera` | `/prddatahub/DIR_FLAG/` | Archivos flag |
| `cfg` | `/nfq/data/cfg/` | Configuración y lookups |
| `key_cript` | `bk_stored` | Clave de cifrado GPG del XML original |
| `qlik_client` | `/opt/qliktasks/cert/` | Certificados de cliente para la API de Qlik |

### Directorio de origen de los XML

Los flags y los XML de negocio llegan a:

```
/prdmegara/PRD/Devices/MegaCommon/innotech/
```

Esta ruta está en `lookupflags.txt`, una vez por cada uno de los 9 flags.

### Ficheros de configuración en `/nfq/data/cfg/`

| Fichero | Qué gobierna |
|---|---|
| `env.properties` | Rutas y variables de entorno |
| `lookupflags.txt` | Los 9 flags y su directorio |
| `lookup_java.txt` | Conversión XML → plano |
| `lookup_stg.txt` | Carga a staging |
| `lookup_trf.txt` | Transformación |
| `lookup_qlik.txt` | Tareas de recarga de Qlik |
| `credentials.properties` | Credenciales de base de datos |
| `reload_task.credentials` | Credenciales y host de la API de Qlik |
| `db_config_gral.env` | Configuración de conexión usada por los pasos de validación |
| `client.pem` / `client_key.pem` | Certificado de cliente para Qlik |
| `config.properties` | Salida, separador y encoding del conversor Java |

### Ciclo de vida de un fichero

```
/prdmegara/PRD/Devices/MegaCommon/innotech/   ← llegada del XML y del flag
                  ↓
/prddatahub/DIR_FLAG/                         ← el flag detectado
                  ↓
/prddatahub/DIR_SSS/OK/                       ← listo para procesar
                  ↓
        ┌─────────┴─────────┐
/prddatahub/DIR_PROCESSED/   /prddatahub/DIR_UNMATCHED/
   procesado correctamente      no casa con lo esperado
```

Un fichero en `DIR_UNMATCHED` es la señal de que llegó algo que el sistema no sabe encaminar:
nombre inesperado, interfaz no catalogada o fuera del lote declarado por el flag.

## Cómo verificarlo

```bash
. /nfq/data/cfg/env.properties
ls -la $bandera        # flags pendientes
ls -la $temp           # ficheros en cola
ls -la $destino        # unmatched: esto no debería acumularse
ls -lat $processed | head -20
```

## Ojo

`3_scripts_motores/config.properties` en el repositorio contiene una ruta de pruebas local,
no la de producción. La ruta buena es la de `env.properties`.

## Ver también

[A02_flujo_e2e_seis_pasos](../A%20-%20Orientacion/A02_flujo_e2e_seis_pasos.md) · [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md) · [A01_que_es_aldrin](../A%20-%20Orientacion/A01_que_es_aldrin.md)

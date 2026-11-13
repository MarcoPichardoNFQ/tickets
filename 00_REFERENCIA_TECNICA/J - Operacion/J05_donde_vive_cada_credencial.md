---
titulo: "J05 — Dónde vive cada credencial"
familia: J
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/J
  - etapa/transversal
  - tipo/referencia
keywords: "credenciales, usuarios, certificados, dónde está, permisos, acceso"
---

# J05 — Dónde vive cada credencial

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** credenciales, usuarios, certificados, dónde está, permisos, acceso

## En una línea

Qué credencial existe, para qué sirve y dónde se guarda — **sin valores**.

## El inventario

| Credencial | Fichero | Variables | Para qué |
|---|---|---|---|
| Base de datos (general) | `/nfq/data/cfg/db_config_gral.env` | `PGPASSWORD`, `DB_CONN` | Todas las cargas y transformaciones |
| Base de datos (por partes) | `/nfq/data/cfg/credentials.properties` | `POSTGRES_HOST`, `_PORT`, `_DATABASE`, `_USERNAME`, `_PASSWORD` | Jobs que construyen la conexión a mano |
| Qlik | `/nfq/data/cfg/reload_task.credentials` | `QLIK_HOST`, `QLIK_USER`, `QLIK_XRFKEY` | Lanzar la recarga |
| Certificados de Qlik | `/nfq/data/cfg/client.pem` y `client_key.pem` | — | Autenticación de cliente |
| Cifrado de ficheros | `env.properties` → `key_cript` | Destinatario GPG `bk_stored` | Archivar los originales |
| **API de Megara** | **Escrita en el propio script** | `CREDENTIALS` en `LLamada Rundeck Flags Obligatorios.sh` | Pedir el siguiente lote |

## Los destinos

| Servicio | Host y puerto |
|---|---|
| PostgreSQL | `psqlprddatahub03.postgres.database.cloud.corp:5432`, base `postgres` |
| Megara Accounting | `megaapps.s3caceis.com.br:9447` |
| Megara Custody | `megaapps.s3caceis.com.br:9445` |
| Qlik (API QRS) | `qlik.s3caceis.com.br:4242` |
| Qlik (tableros) | `qlik.s3caceis.com.br` |

## Usuarios de servicio

| Usuario | Dónde |
|---|---|
| `svc.db.rdkprd@…` | Conexión a PostgreSQL |
| `userrdkmeg@ALL` | API de Megara |
| Usuario de servicio de Qlik | `QLIK_USER` |

## Tres observaciones de seguridad

**Las credenciales de la API de Megara están en el código del script**, no en un fichero de
credenciales. Cualquiera con acceso de lectura al script las ve.
Ver [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md).

**La llamada a Qlik desactiva la verificación TLS** (`--insecure`): la autenticación de cliente
funciona, pero no se valida la identidad del servidor. Ver [H16_credenciales_qlik](../H%20-%20Cierre%20y%20Qlik/H16_credenciales_qlik.md).

**Hay dos ficheros de credenciales de base de datos** con formatos distintos: `db_config_gral.env`
define una cadena `DB_CONN` completa, y `credentials.properties` las variables por separado. Cada
script usa uno u otro. Si cambia la contraseña, **hay que actualizar los dos**.

## Comprobaciones que sí puede hacer soporte

```bash
# ¿Existen y son legibles?
ls -la /nfq/data/cfg/*.pem /nfq/data/cfg/*.env /nfq/data/cfg/credentials.properties

# ¿Cuándo caduca el certificado de Qlik?
openssl x509 -in /nfq/data/cfg/client.pem -noout -dates
```

Esa última merece hacerse de forma preventiva: **un certificado caducado detiene la recarga de Qlik
sin más aviso que el fallo de la tarea**, y el paso de Rundeck sale en verde igualmente.
Ver [H12_recarga_qlik_fallo](../H%20-%20Cierre%20y%20Qlik/H12_recarga_qlik_fallo.md).

```bash
# ¿La conexión lleva salida sin formato? Determina si dos comprobaciones del sistema funcionan
grep -i "DB_CONN" /nfq/data/cfg/db_config_gral.env
```

Ver [R4_03_validacion_cantidades](../R4%20-%20Sets%20incompletos/R4_03_validacion_cantidades.md) y [F01_que_hace_la_capa_trf](../F%20-%20Transformacion%20TRF/F01_que_hace_la_capa_trf.md).

## Lo que NO hay que hacer

**No copiar valores de credenciales a tickets, correos ni documentos.** Los nombres de variable y
los hosts bastan para diagnosticar.

**No editar estos ficheros.** Un cambio mal hecho detiene todas las cargas a la vez, y el fallo
aparece como error de conexión en decenas de jobs simultáneamente.

## Ver también

[I17_ficheros_configuracion](../I%20-%20Referencia%20de%20datos/I17_ficheros_configuracion.md) · [H16_credenciales_qlik](../H%20-%20Cierre%20y%20Qlik/H16_credenciales_qlik.md) · [J06_servidores_accesos](../J%20-%20Operacion/J06_servidores_accesos.md) · [J04_que_no_tocar](../J%20-%20Operacion/J04_que_no_tocar.md)

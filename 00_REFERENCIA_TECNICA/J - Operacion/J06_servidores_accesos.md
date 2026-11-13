---
titulo: "J06 — Servidores, rutas y accesos que necesita BAU"
familia: J
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/J
  - etapa/transversal
  - tipo/referencia
keywords: "accesos, servidores, permisos, qué necesito, incorporación, entorno"
---

# J06 — Servidores, rutas y accesos que necesita BAU

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** accesos, servidores, permisos, qué necesito, incorporación, entorno

## En una línea

Lo que hay que tener para poder diagnosticar sin depender de nadie.

## Los cinco accesos

| Acceso | Para qué | Sin él no puedes… |
|---|---|---|
| **PostgreSQL, lectura** | Todas las consultas de esta base | Prácticamente nada |
| **Rundeck, consola** | Logs, histórico, relanzar jobs | Ver por qué falló un job |
| **Servidor de aplicación** (shell) | Directorios, ficheros, lookups | Comprobar si un fichero llegó |
| **Qlik, consola** | Historial de tareas, relanzar recargas | Cerrar una incidencia de tableros |
| **Buzón de alertas** | Recibir las notificaciones | Enterarte de nada |

Los tres primeros cubren la mayoría de las incidencias. El cuarto es imprescindible para la
familia `H`; el quinto determina de qué te enteras. Ver [R5_03_listas_distribucion](../R5%20-%20Alertas%20Rundeck/R5_03_listas_distribucion.md).

## Los destinos

| Servicio | Host y puerto |
|---|---|
| PostgreSQL | `psqlprddatahub03.postgres.database.cloud.corp:5432`, base `postgres` |
| Megara Accounting | `megaapps.s3caceis.com.br:9447` |
| Megara Custody | `megaapps.s3caceis.com.br:9445` |
| Qlik (API QRS) | `qlik.s3caceis.com.br:4242` |
| Qlik (tableros) | `qlik.s3caceis.com.br` |

## Las rutas del servidor

| Ruta | Qué hay |
|---|---|
| `/nfq/data/cfg/` | Toda la configuración y los scripts |
| `/nfq/XMLconversor/` | El conversor, su `config.properties` y los XSD |
| `/prdmegara/PRD/Devices/MegaCommon/innotech/` | Llegada de XML y flags |
| `…/innotech/Flags/` | Flags ya procesados |
| `…/innotech/Manual/` | Entrada de la vía manual de conversión |
| `/DIR_SSS_LOCAL/` | Salida del conversor = entrada de la carga |
| `/prddatahub/DIR_SSS/OK/` | Ficheros listos |
| `/prddatahub/DIR_UNMATCHED/` | Sin encaminar |
| `/prddatahub/DIR_PROCESSED/` | Archivados y cifrados |
| `/prddatahub/DIR_FLAG/` | Flags |

Ver [A04_rutas_y_directorios](../A%20-%20Orientacion/A04_rutas_y_directorios.md).

## Comprobación de acceso, en cinco órdenes

```bash
. /nfq/data/cfg/env.properties
ls -la /nfq/data/cfg/ | head                        # ¿lees la configuración?
ls -la $raiz | head                                 # ¿ves los ficheros en curso?
ls -la $processed/DIR_MEGARA/ | head                # ¿ves el histórico?
```

```sql
SELECT count(*) FROM stg_s3.aud_load_trace_t WHERE dat_load_date >= CURRENT_DATE;
SELECT count(*) FROM exp_s3.tablas_mapeio_t;
```

Si las cinco funcionan, tienes lo necesario para el 90 % de las incidencias.

## Lo que hace falta para descifrar el histórico

Los ficheros archivados están cifrados con GPG para el destinatario `bk_stored`. Para leerlos hace
falta **la clave privada correspondiente**:

```bash
gpg --decrypt FICHERO.xml.gpg | head -50
```

Sin ella, se puede ver que el fichero existe y cuándo se archivó, pero no su contenido. Es una
petición de acceso que conviene resolver antes de necesitarla con urgencia.
Ver [C08_cifrado_xml_original](../C%20-%20Conversion%20Java/C08_cifrado_xml_original.md).

## Lo que no se puede consultar desde ningún sitio de aquí

| Qué | Dónde está |
|---|---|
| Permisos de usuario en Qlik | `VistaFondos.qvd` — sólo desde Qlik |
| Contenido de los QVD | Sólo desde Qlik |
| Duración histórica de un job | Sólo en Rundeck |

Ver [H14_section_access](../H%20-%20Cierre%20y%20Qlik/H14_section_access.md) y [R5_06_duracion_anomala](../R5%20-%20Alertas%20Rundeck/R5_06_duracion_anomala.md).

## Para quien se incorpora

1. Pedir los cinco accesos y **verificarlos con las cinco órdenes de arriba**
2. Comprobar en qué listas de distribución estás. Ver [R5_03_listas_distribucion](../R5%20-%20Alertas%20Rundeck/R5_03_listas_distribucion.md)
3. Leer [A01_que_es_aldrin](../A%20-%20Orientacion/A01_que_es_aldrin.md), [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md) y [J10_trampas_conocidas](../J%20-%20Operacion/J10_trampas_conocidas.md)
4. Ejecutar [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md) un par de días para tener línea base

## Ver también

[A04_rutas_y_directorios](../A%20-%20Orientacion/A04_rutas_y_directorios.md) · [J05_donde_vive_cada_credencial](../J%20-%20Operacion/J05_donde_vive_cada_credencial.md) · [R5_03_listas_distribucion](../R5%20-%20Alertas%20Rundeck/R5_03_listas_distribucion.md) · [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md)

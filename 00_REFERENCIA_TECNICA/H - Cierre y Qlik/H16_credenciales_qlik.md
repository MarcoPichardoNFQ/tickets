---
titulo: "H16 — Credenciales y certificados de Qlik"
familia: H
etapa: "Cierre y Qlik"
tipo: Referencia
tags:
  - familia/H
  - etapa/cierre-y-qlik
  - tipo/referencia
keywords: "certificados, pem, QRS, xrfkey, 4242, credenciales, TLS"
---

# H16 — Credenciales y certificados de Qlik

**Etapa:** Cierre y Qlik
**Tipo:** Referencia
**Palabras clave:** certificados, pem, QRS, xrfkey, 4242, credenciales, TLS

## En una línea

La conexión con Qlik usa **certificados de cliente** y una clave anti-falsificación, todo declarado
en `/nfq/data/cfg/`.

## Los elementos

| Elemento | Dónde | Qué es |
|---|---|---|
| `QLIK_HOST` | `reload_task.credentials` | `https://qlik.s3caceis.com.br:4242/qrs/task/` |
| `QLIK_USER` | `reload_task.credentials` | Usuario de servicio |
| `QLIK_XRFKEY` | `reload_task.credentials` | Clave anti-CSRF exigida por la API |
| `client.pem` | `/nfq/data/cfg/` | Certificado de cliente |
| `client_key.pem` | `/nfq/data/cfg/` | Clave privada del certificado |
| `qlik_client` | `env.properties` | `/opt/qliktasks/cert/` — **variable que nadie usa** |

## El puerto 4242 es la API de repositorio

`:4242/qrs/` es el **Qlik Repository Service**, la API de administración. La URL completa que se
construye es:

```
https://qlik.s3caceis.com.br:4242/qrs/task/<uuid>/start?xrfkey=<clave>
```

Y la llamada exige tres cabeceras:

```bash
--header "Content-type:application/json"
--header "X-Qlik-Xrfkey: $QLIK_XRFKEY"
--header "X-Qlik-User: UserDirectory=CLOUD;UserId=$QLIK_USER"
```

La `xrfkey` va **duplicada**: en la URL y en la cabecera. Es un requisito de la API de Qlik; si no
coinciden, rechaza la petición.

## ⚠ Dos observaciones de seguridad

**La conexión desactiva la verificación TLS:**

```bash
curl -s --key client_key.pem --cert client.pem --insecure ...
```

`--insecure` significa que **no se valida el certificado del servidor**. La autenticación de cliente
sí funciona, pero la identidad del extremo no se comprueba. No impide que opere; es información para
quien gestione la seguridad del entorno.

**Y en el otro extremo del ciclo**, la llamada a la API de Megara lleva las credenciales escritas
en claro dentro del script:

```bash
CREDENTIALS="userrdkmeg@ALL:..."
```

No en un fichero de credenciales, sino en el código del propio script.
Ver [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md).

## Las dos variables que no se usan

`reload_task.credentials` define también:

```
TLIMIT="85200"
T_SLEEP=30
```

**El paso «Recarga Qlik» no las utiliza.** Sugieren un mecanismo de sondeo con límite de tiempo
—85.200 segundos son unas 23,7 horas— que no está en el script disponible.

Junto con `qlik_client`, que tampoco lee nadie, son restos de una implementación anterior.
Ver [H15_catalogo_tareas_qlik](../H%20-%20Cierre%20y%20Qlik/H15_catalogo_tareas_qlik.md).

## Qué comprobar si la recarga falla por autenticación

```bash
. /nfq/data/cfg/env.properties

# ¿Existen los certificados y son legibles?
ls -la /nfq/data/cfg/client.pem /nfq/data/cfg/client_key.pem

# ¿Cuándo caducan?
openssl x509 -in /nfq/data/cfg/client.pem -noout -dates
```

**Un certificado caducado detiene la recarga sin más aviso que el fallo de la tarea en Qlik** — y el
paso de Rundeck sale en verde igualmente, porque no comprueba el resultado.
Ver [H12_recarga_qlik_fallo](../H%20-%20Cierre%20y%20Qlik/H12_recarga_qlik_fallo.md).

Esa comprobación de fecha merece hacerse de forma preventiva: es de las pocas incidencias de esta
familia que se puede anticipar.

## Ver también

[H08_recarga_qlik](../H%20-%20Cierre%20y%20Qlik/H08_recarga_qlik.md) · [H12_recarga_qlik_fallo](../H%20-%20Cierre%20y%20Qlik/H12_recarga_qlik_fallo.md) · [I17_ficheros_configuracion](../I%20-%20Referencia%20de%20datos/I17_ficheros_configuracion.md) · [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md)

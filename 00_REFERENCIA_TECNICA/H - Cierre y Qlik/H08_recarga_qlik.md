---
titulo: "H08 — La recarga de Qlik y el paso que no envía nada"
familia: H
etapa: "Cierre y Qlik"
tipo: Referencia
tags:
  - familia/H
  - etapa/cierre-y-qlik
  - tipo/referencia
keywords: "recarga Qlik, RecargadesdeRundeck, curl, --X POST, certificados pem, xrfkey"
---

# H08 — La recarga de Qlik y el paso que no envía nada

**Etapa:** Cierre y Qlik
**Tipo:** Referencia
**Palabras clave:** recarga Qlik, RecargadesdeRundeck, curl, --X POST, certificados pem, xrfkey

## En una línea

Hay dos vías de recarga: la incremental por tabla —que es la que funciona— y un paso global
`RecargadesdeRundeck` cuyo `curl` **no puede enviar la petición**.

## Dónde está el paso global

No es un job propio, sino un **paso** dentro de dos jobs:

- `0999 -. Optimizacao Blocos Rundeck V6`, paso «Recarga Qlik»
- `JobsArchivosFlag`, paso «Recarga Qlik»

Por eso no aparece como job independiente al buscarlo en Rundeck.

## Qué hace el paso

```bash
cfg="/nfq/data/cfg/"
env="/nfq/data/cfg/env.properties"
task="/nfq/data/cfg/reload_task.credentials"
. $env
. $task

nom_task="RecargadesdeRundeck"
id_task="a75bd6d3-d26b-41ec-8c88-1c29b1ff9202"

url=$QLIK_HOST$id_task/start?xrfkey=$QLIK_XRFKEY

curl -s \
    --key $cfg"client_key.pem" \
    --cert $cfg"client.pem" \
    --insecure \
    --X POST \
    --header "Content-type:application/json" \
    --header "X-Qlik-Xrfkey: $QLIK_XRFKEY" \
    --header "X-Qlik-User: UserDirectory=CLOUD;UserId=$QLIK_USER" \
    -d "" \
    $url

echo "Task $nom_task lanzada"
exit 0
```

| Elemento | Valor |
|---|---|
| Tarea | `RecargadesdeRundeck` |
| UUID | `a75bd6d3-d26b-41ec-8c88-1c29b1ff9202` |
| Certificados | `/nfq/data/cfg/client.pem` y `client_key.pem` |
| Credenciales y host | `/nfq/data/cfg/reload_task.credentials` (`QLIK_HOST`, `QLIK_XRFKEY`, `QLIK_USER`) |

## ⚠ El `curl` no puede enviar la petición

```
--X POST
```

**`--X` no es una opción válida de curl.** La forma larga es `--request`; la corta, `-X`. Ante una
opción larga desconocida, curl responde:

```
curl: option --X: is unknown
```

y **termina con código 2 sin enviar nada**. Comprobado ejecutándolo.

El typo está **igual en las dos copias** del paso.

## Y el paso siempre reporta éxito

Tres factores se suman:

1. `curl -s` — modo silencioso, no imprime el error.
2. En la copia de `0999`, la llamada va en segundo plano con `&`.
3. Ambas copias terminan con `echo "Task lanzada"; exit 0` **sin comprobar el resultado**.

Resultado: **el paso sale en verde se envíe la petición o no.**

## Es el único disparador de Qlik en toda la orquestación

Conviene subrayarlo porque cambia el peso del hallazgo: **este paso es el final del proceso y no hay
ningún otro punto donde Rundeck toque Qlik.**

```
0999 Optimizacao Blocos V6:  ... → Mapeos → Job control errores → Análise de erros
                             → Procedimiento control finalizacion mapeos
                             → STG StartOver → Recarga Qlik → Validacion Descartes

JobsArchivosFlag:            CargaInformacion → Job control errores → Análise de erros
                             → Procedimiento control finalizacion mapeos Flag
                             → Recarga Qlik → Validacion Descartes
```

Y las 265 tareas de `lookup_qlik.txt` **no las dispara nada del flujo**: ese fichero se menciona una
sola vez en todo el sistema, en la definición de su propia variable en `env.properties`, que nadie
lee. Lo mismo ocurre con `qlik_client`. Ver [H07_lookup_qlik](../H%20-%20Cierre%20y%20Qlik/H07_lookup_qlik.md).

Así que si en producción el `curl` está tal como aparece aquí, **Rundeck no está lanzando ninguna
recarga de Qlik**, y los tableros se actualizan por otra vía ajena a esta orquestación.

## ✅ Resuelto: en producción funciona

Verificado contra el entorno real: **la tarea `RecargadesdeRundeck` se ejecuta de forma continua,
varias veces al día**, siguiendo el ciclo de los orquestadores.

Conclusión: **el script de producción tiene la opción bien escrita (`-X POST`) y el export del
repositorio está desactualizado.** No hay ningún defecto activo aquí.

Lo que sí conviene retener de todo esto:

- **El export de Rundeck puede no reflejar producción.** Ante una discrepancia entre lo que dice un
  export y lo que hace el sistema, manda el sistema.
- **El paso sigue sin comprobar el resultado.** Aunque el `curl` esté bien, el `exit 0` posterior es
  incondicional: el paso reporta éxito sin mirar si Qlik aceptó la petición. Ver [H12_recarga_qlik_fallo](../H%20-%20Cierre%20y%20Qlik/H12_recarga_qlik_fallo.md).

## Cómo confirmarlo

Sólo se puede hacer desde la consola de Qlik: historial de ejecuciones de la tarea
`RecargadesdeRundeck` (`a75bd6d3-d26b-41ec-8c88-1c29b1ff9202`).

- Si **no tiene ejecuciones** o las que tiene no coinciden con el fin de los mapeos → confirmado.
- Si se ejecuta puntualmente tras cada ciclo → el script de producción difiere del exportado, y
  entonces el export está obsoleto.

## Otro detalle: `--insecure`

La llamada desactiva la verificación del certificado del servidor. No impide que funcione, pero
significa que la conexión con Qlik no valida la identidad del extremo, aun usando certificados de
cliente. Es información para quien gestione la seguridad del entorno, no una incidencia operativa.

## Ver también

[H07_lookup_qlik](../H%20-%20Cierre%20y%20Qlik/H07_lookup_qlik.md) · [H09_qlik_datos_de_ayer](../H%20-%20Cierre%20y%20Qlik/H09_qlik_datos_de_ayer.md) · [H12_recarga_qlik_fallo](../H%20-%20Cierre%20y%20Qlik/H12_recarga_qlik_fallo.md) · [R5_07_alerta_vs_estado_real](../R5%20-%20Alertas%20Rundeck/R5_07_alerta_vs_estado_real.md)

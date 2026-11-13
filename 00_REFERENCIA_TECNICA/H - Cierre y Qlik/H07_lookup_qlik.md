---
titulo: "H07 — `lookup_qlik.txt`: las 265 tareas de recarga"
familia: H
etapa: "Cierre y Qlik"
tipo: Referencia
tags:
  - familia/H
  - etapa/cierre-y-qlik
  - tipo/referencia
keywords: "lookup_qlik, tareas Qlik, UUID, QVD, incremental, flag Qlik_"
---

# H07 — `lookup_qlik.txt`: las 265 tareas de recarga

**Etapa:** Cierre y Qlik
**Tipo:** Referencia
**Palabras clave:** lookup_qlik, tareas Qlik, UUID, QVD, incremental, flag Qlik_

## En una línea

265 tareas de Qlik catalogadas, en dos familias: recargas globales y recargas incrementales por
tabla, cada una disparada por su propio archivo flag.

## Formato

```
|id|NOMBRE_DE_LA_TAREA|UUID|[fichero_flag]|
```

### Familia 1 — recargas globales (entradas 1 a 40)

Sin cuarto campo:

```
|1|LOAD_QVD_ACUMULADODEGESTION|69c48258-a258-4036-9363-274ec961ed37|
|13|LOAD_QVD_P&L|58cf2546-6d7d-4f5b-8283-b9d173a71206|
|19|LOAD_UPDATE_ACUMULADODEGESTION|5f439010-639a-42cc-b12a-204bb104557b|
|38|KYC|24f86b61-4d6d-41cf-acdb-ba471de2dd67|
|39|FIDC|fd384406-f84a-4e56-8925-ff746a200c40|
|40|SANTANDER CACEIS DATAHUB|fa96a867-5185-4538-9b99-cb8d0427df0e|
```

Tres grupos dentro de esta familia:

- **`LOAD_QVD_*`** (1-18) — carga de los ficheros QVD
- **`LOAD_UPDATE_*`** (19-37) — actualización, con los mismos nombres de negocio
- **Nominales** (38-40) — `KYC`, `FIDC`, `SANTANDER CACEIS DATAHUB`

Los nombres de negocio se repiten entre `LOAD_QVD_` y `LOAD_UPDATE_`: son dos fases sobre el mismo
dominio.

### Familia 2 — incrementales por tabla (entradas 101 en adelante)

Con cuarto campo, que es un **archivo flag**:

```
|101|INCREMENTAL_LOAD_QVD_SAC_QLIK_BA_BLOQUEIO_V|5dd3a21c-...|Qlik_SAC_BA_BLOQUEIO_T.flag
|111|INCREMENTAL_LOAD_QVD_SAC_QLIK_CART_POS_RF_V|2643b641-...|Qlik_CART_POS_RF_T.flag
```

El patrón es sistemático:

| Elemento | Patrón |
|---|---|
| Nombre de tarea | `INCREMENTAL_LOAD_QVD_SAC_QLIK_<TABLA>_V` |
| Fichero flag | `Qlik_<TABLA>_T.flag` |

**Cada tabla de salida tiene su propia tarea de recarga y su propio flag.** Es la relación
uno-a-uno que permite recargar una tabla sin tocar las demás.

Los identificadores saltan de 40 a 101: el hueco es deliberado, separa las dos familias.

## Para qué sirve esto en soporte

**Es el índice tabla → tarea de Qlik.** Ante «esta tabla no se ve actualizada en Qlik», aquí está
el nombre y el UUID de la tarea concreta que hay que revisar o relanzar:

```bash
grep -i "<TABLA>" /nfq/data/cfg/lookup_qlik.txt
```

Devuelve el nombre de la tarea, su UUID y el flag que la dispara. Con eso ya se puede buscar en la
consola de Qlik.

## ⚠ Este fichero no lo lee nadie

Éste es el hallazgo más desconcertante de la familia. `lookup_qlik.txt` aparece **una sola vez** en
todo el sistema:

```
env.properties:12   lookup_qlik=$cfg"lookup_qlik.txt"
```

Es la definición de una variable **que ningún script utiliza**. Lo mismo ocurre con
`qlik_client="/opt/qliktasks/cert/"` en la línea 14: definida y nunca leída.

Y en Rundeck, el único punto donde se toca Qlik es el paso «Recarga Qlik» al final del proceso, que
lanza **una sola tarea global** con su UUID codificado en el propio script —`RecargadesdeRundeck`,
`a75bd6d3-d26b-41ec-8c88-1c29b1ff9202`— sin consultar este catálogo para nada.
Ver [H08_recarga_qlik](../H%20-%20Cierre%20y%20Qlik/H08_recarga_qlik.md).

**Conclusión: las 265 tareas de este fichero no las dispara la orquestación.** El cuarto campo con
el nombre del flag `Qlik_<TABLA>_T.flag` sugiere un mecanismo basado en ficheros, pero nada en el
material disponible los genera ni los consume.

Tres explicaciones posibles, sin datos para elegir entre ellas:

1. El fichero es **documentación viva de las tareas de Qlik** —un catálogo de referencia— y quien
   las dispara es el propio planificador de Qlik.
2. Existe un consumidor **fuera de este servidor** o fuera del material que tengo.
3. Es un **resto de una implementación anterior** basada en flags que se sustituyó por la recarga
   global, y nadie retiró ni el fichero ni las variables.

La tercera es la más probable, y hay dos indicios que la respaldan:

- **Las dos variables están muertas a la vez** (`lookup_qlik` y `qlik_client`), lo que encaja con
  una retirada incompleta.
- **No existe ni una sola referencia a los ficheros `Qlik_*.flag`** en ningún job ni script: nada
  los genera y nada los consume. El cuarto campo del lookup apunta a un mecanismo que no está.
- Un análisis previo del sistema ya había catalogado este fichero como **no utilizado**, con las
  265 entradas contabilizadas.

**Para BAU esto significa: no busques el proceso que lee este fichero, no existe.** Si una tabla no
se recarga, el camino es el paso «Recarga Qlik» del final del proceso y la consola de Qlik, no este
catálogo.

**Lo que sí sirve, sea cual sea la respuesta:** el fichero es un **índice fiable de tabla → tarea de
Qlik con su UUID**, y eso es exactamente lo que hace falta para localizar una tarea en la consola de
Qlik ante una incidencia.

## Verificaciones útiles

```bash
# Total de tareas catalogadas
grep -c "^|" /nfq/data/cfg/lookup_qlik.txt

# Sólo las incrementales (las que tienen flag)
awk -F'|' 'NF>4 && $5!=""' /nfq/data/cfg/lookup_qlik.txt | wc -l

# La tarea de una tabla concreta
grep -i "CART_POS_RF" /nfq/data/cfg/lookup_qlik.txt

# ¿Qué flags de Qlik hay pendientes ahora mismo?
. /nfq/data/cfg/env.properties
ls -la $bandera | grep -i "^Qlik_"
```

Esa última orden es la más útil en caliente: flags de Qlik acumulados significa que las recargas no
se están consumiendo.

## Ver también

[H08_recarga_qlik](../H%20-%20Cierre%20y%20Qlik/H08_recarga_qlik.md) · [H09_qlik_datos_de_ayer](../H%20-%20Cierre%20y%20Qlik/H09_qlik_datos_de_ayer.md) · [R4_04_s3_interface_control](../R4%20-%20Sets%20incompletos/R4_04_s3_interface_control.md) · [A04_rutas_y_directorios](../A%20-%20Orientacion/A04_rutas_y_directorios.md)

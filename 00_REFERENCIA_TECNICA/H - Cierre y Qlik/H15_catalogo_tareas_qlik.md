---
titulo: "H15 — Catálogo de tareas de Qlik y sus UUID"
familia: H
etapa: "Cierre y Qlik"
tipo: Referencia
tags:
  - familia/H
  - etapa/cierre-y-qlik
  - tipo/referencia
keywords: "UUID, tareas Qlik, catálogo, LOAD_QVD, INCREMENTAL, buscar tarea"
---

# H15 — Catálogo de tareas de Qlik y sus UUID

**Etapa:** Cierre y Qlik
**Tipo:** Referencia
**Palabras clave:** UUID, tareas Qlik, catálogo, LOAD_QVD, INCREMENTAL, buscar tarea

## En una línea

265 tareas catalogadas con su UUID en `lookup_qlik.txt`: **el fichero no lo lee ningún proceso**,
pero sigue siendo el índice para localizar una tarea en la consola de Qlik.

## Las dos familias

### Globales — entradas 1 a 40

Sin cuarto campo:

```
|1|LOAD_QVD_ACUMULADODEGESTION|69c48258-a258-4036-9363-274ec961ed37|
|13|LOAD_QVD_P&L|58cf2546-6d7d-4f5b-8283-b9d173a71206|
|19|LOAD_UPDATE_ACUMULADODEGESTION|5f439010-639a-42cc-b12a-204bb104557b|
|38|KYC|24f86b61-4d6d-41cf-acdb-ba471de2dd67|
|39|FIDC|fd384406-f84a-4e56-8925-ff746a200c40|
|40|SANTANDER CACEIS DATAHUB|fa96a867-5185-4538-9b99-cb8d0427df0e|
```

Tres grupos: `LOAD_QVD_*` (1-18), `LOAD_UPDATE_*` (19-37) con los mismos nombres de negocio, y tres
nominales.

**Sus nombres coinciden con las tablas del dominio propio de `exp_s3`**: `acumulado_de_gestion`,
`alertas_por_cenario`, `fluxo*`… Ver [I04_inventario_exp_s3](../I%20-%20Referencia%20de%20datos/I04_inventario_exp_s3.md).

### Incrementales por tabla — entradas 101 en adelante

Con cuarto campo, un fichero flag:

```
|101|INCREMENTAL_LOAD_QVD_SAC_QLIK_BA_BLOQUEIO_V|5dd3a21c-...|Qlik_SAC_BA_BLOQUEIO_T.flag
|111|INCREMENTAL_LOAD_QVD_SAC_QLIK_CART_POS_RF_V|2643b641-...|Qlik_CART_POS_RF_T.flag
```

Patrón sistemático:

| Elemento | Forma |
|---|---|
| Tarea | `INCREMENTAL_LOAD_QVD_SAC_QLIK_<TABLA>_V` |
| Flag | `Qlik_<TABLA>_T.flag` |

**Una tarea por tabla de salida.** Los identificadores saltan de 40 a 101 para separar las familias.

## Para qué sirve, dado que nadie lo lee

Es el **índice tabla → tarea de Qlik con su UUID**, y eso es exactamente lo que hace falta para
localizar una tarea en la consola cuando alguien reporta que una tabla no se ve actualizada:

```bash
grep -i "<TABLA>" /nfq/data/cfg/lookup_qlik.txt
```

Devuelve nombre de tarea, UUID y el flag asociado. Con el UUID se busca directamente en Qlik.

## ⚠ El fichero está huérfano

`lookup_qlik.txt` aparece **una sola vez** en todo el sistema: en la definición de su variable en
`env.properties:12`, que ningún script utiliza. Lo mismo con `qlik_client` en la línea 14.

Y no existe ninguna referencia a los ficheros `Qlik_*.flag` en ningún job ni script: nada los genera
y nada los consume.

Un análisis previo del sistema ya lo tenía catalogado como **no utilizado**, con las 265 entradas
contabilizadas.

**Conclusión: no busques el proceso que lee este fichero.** La recarga real la dispara el paso
«Recarga Qlik» del cierre, con un único UUID escrito en el propio script. Ver [H08_recarga_qlik](../H%20-%20Cierre%20y%20Qlik/H08_recarga_qlik.md).

## La tarea que sí se usa

```
RecargadesdeRundeck
a75bd6d3-d26b-41ec-8c88-1c29b1ff9202
```

Codificada en el paso de Rundeck. Se ejecuta de forma continua, varias veces al día.

## Consultas útiles

```bash
# Total y reparto
grep -c "^|" /nfq/data/cfg/lookup_qlik.txt
awk -F'|' 'NF>4 && $5!=""' /nfq/data/cfg/lookup_qlik.txt | wc -l   # las incrementales

# La tarea de una tabla
grep -i "CART_POS_RF" /nfq/data/cfg/lookup_qlik.txt

# ¿Hay flags de Qlik acumulados?
. /nfq/data/cfg/env.properties
ls -la $bandera | grep -i "^Qlik_"
```

## Ver también

[H07_lookup_qlik](../H%20-%20Cierre%20y%20Qlik/H07_lookup_qlik.md) · [H08_recarga_qlik](../H%20-%20Cierre%20y%20Qlik/H08_recarga_qlik.md) · [H12_recarga_qlik_fallo](../H%20-%20Cierre%20y%20Qlik/H12_recarga_qlik_fallo.md) · [I04_inventario_exp_s3](../I%20-%20Referencia%20de%20datos/I04_inventario_exp_s3.md)

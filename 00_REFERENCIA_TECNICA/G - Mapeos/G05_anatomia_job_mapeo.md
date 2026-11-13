---
titulo: "G05 — Anatomía de un job de mapeo"
familia: G
etapa: "Mapeos"
tipo: Referencia
tags:
  - familia/G
  - etapa/mapeos
  - tipo/referencia
keywords: "job de mapeo, 001 - JOBs Mapeos, jobref, id_mapeo, relanzar"
---

# G05 — Anatomía de un job de mapeo

**Etapa:** Mapeos
**Tipo:** Referencia
**Palabras clave:** job de mapeo, 001 - JOBs Mapeos, jobref, id_mapeo, relanzar

## En una línea

Un job por mapeo, todos en el mismo grupo, todos con la misma estructura: llaman al despacho
pasándole su `id_mapeo`.

## Cómo se llaman

Grupo **`001 - JOBs Mapeos`**, nombre `<id> mapeo_<tabla_destino>`:

```
14 mapeo_cart_pos_rf_t
35 mapeo_sac_pl_cl_patrrf_t
111 mapeo_cart_estat_clibas_t
```

**El número del nombre es el `id_mapeo`.** Es la forma más rápida de llegar al log de un mapeo
concreto: buscar por ese número en ese grupo.

## Cómo los invoca el orquestador

`Mapeos` y `MapeosFlag` son listas de referencias:

```xml
<command>
  <description>mapeo_cart_pos_rf_t</description>
  <jobref group='001 - JOBs Mapeos' name='14 mapeo_cart_pos_rf_t'>
    <useName>true</useName>
  </jobref>
</command>
```

Un bloque así por mapeo. Ver [G04_jobs_mapeos](../G%20-%20Mapeos/G04_jobs_mapeos.md).

## Qué hace cada job

Invoca el procedimiento de despacho con su identificador:

```sql
CALL exp_s3.fim_carga_mapeo_megara_ind(:po_outcode, <id_mapeo>);
```

Y el despacho hace el resto: recorre las funciones activas de ese `id_mapeo`, comprueba el
contador, ejecuta con reintentos y decrementa. Ver [G08_fim_carga_mapeo](../G%20-%20Mapeos/G08_fim_carga_mapeo.md).

**El job no contiene lógica de negocio.** Toda la inteligencia está en la base de datos. Por eso
los jobs son intercambiables y sólo se diferencian en el número que pasan.

## Lo que esto implica para relanzar

**Relanzar el job individual es la forma correcta** de recuperar un mapeo: hace exactamente lo mismo
que haría el orquestador para ese mapeo, sin arrastrar los demás.

Pero hay una condición que el job no comprueba: **si el contador `control_carga` de esa tabla ya
llegó a `0` en el lote actual, no se ejecuta nada** y el job sale en verde sin trabajar.

```sql
SELECT tabela_carga, control_carga, data_ini_upload, data_fim_upload
FROM   exp_s3.control_mapeio_t
WHERE  id = (SELECT last_value FROM exp_s3.cod_seq_control_mapeio)
  AND  lower(tabela_carga) = lower('<TABLA>');
```

`control_carga = 0` → relanzar no hará nada. Ver [R3_11_relanzar_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_11_relanzar_mapeo.md).

## Localizar el job de una tabla

```sql
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio, activo_inactivo
FROM   exp_s3.tablas_mapeio_t
WHERE  lower(nome_tabela_aldrin) = lower('<TABLA>');
```

El `id_mapeo` que devuelva es el número del job en Rundeck.

## ⚠ Un job que existe no garantiza que se ejecute

La lista de `Mapeos` es **estática**; el catálogo real está en `tablas_mapeio_t`. Un mapeo activo
en la tabla pero ausente de la lista del orquestador **no se ejecuta nunca y no genera error**:
nadie lo llama.

Contrasta la lista de pasos del orquestador en Rundeck con:

```sql
SELECT DISTINCT id_mapeo, nome_tabela_aldrin
FROM   exp_s3.tablas_mapeio_t
WHERE  activo_inactivo AND is_fromtis = 'N'
ORDER  BY id_mapeo;
```

Ver [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md).

## Ver también

[G04_jobs_mapeos](../G%20-%20Mapeos/G04_jobs_mapeos.md) · [G08_fim_carga_mapeo](../G%20-%20Mapeos/G08_fim_carga_mapeo.md) · [R3_11_relanzar_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_11_relanzar_mapeo.md) · [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md) · [G06_catalogo_mapeos](../G%20-%20Mapeos/G06_catalogo_mapeos.md)

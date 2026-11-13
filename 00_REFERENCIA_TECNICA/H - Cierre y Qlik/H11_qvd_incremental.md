---
titulo: "H11 — Los QVD y el patrón incremental"
familia: H
etapa: "Cierre y Qlik"
tipo: Referencia
tags:
  - familia/H
  - etapa/cierre-y-qlik
  - tipo/referencia
keywords: "QVD, incremental, cod_sacbbdd, MEG, histórico, acumulado"
---

# H11 — Los QVD y el patrón incremental

**Etapa:** Cierre y Qlik
**Tipo:** Referencia
**Palabras clave:** QVD, incremental, cod_sacbbdd, MEG, histórico, acumulado

## En una línea

Cada tabla se publica en un fichero QVD que **acumula histórico**: en cada recarga se conserva lo
que no es de Megara y se refresca sólo lo que sí lo es.

## El patrón

```qlik
temp:
LOAD <columnas>, cod_mload_trace, cod_sacbbdd
FROM [lib://QVD (...)/<nombre>.qvd](qvd);          ← 1. lee el QVD anterior

<tabla>:
LOAD * RESIDENT temp WHERE cod_sacbbdd <> 'MEG';  ← 2. conserva lo NO Megara
DROP TABLE temp;

SQL SELECT <columnas> FROM trf_s3.<tabla> ...;    ← 3. añade lo fresco de Megara

STORE <tabla> INTO [lib://QVD (...)/<nombre>.qvd](qvd);   ← 4. reescribe el QVD
```

## `cod_sacbbdd` es la bisagra

| Valor | Origen | En cada recarga |
|---|---|---|
| `'MEG'` | Este sistema | **Se descarta del QVD y se recarga desde la base** |
| Otro | Otra procedencia | **Se conserva del QVD** |

Es decir: **el QVD guarda datos de más de un sistema**, y sólo la parte de Megara se refresca. Lo
demás vive únicamente en el QVD.

Ver [I18_columnas_comunes](../I%20-%20Referencia%20de%20datos/I18_columnas_comunes.md).

## Las tres consecuencias operativas

### El QVD es un acumulado, no una foto

Contiene más historia de la que hay en `trf_s3` en ese momento. Comparar conteos entre la tabla y lo
que se ve en Qlik **no tiene por qué cuadrar**, y no es señal de nada.

### Si la recarga falla, el QVD anterior sigue sirviendo datos

Los tableros no se quedan vacíos: siguen mostrando lo del QVD previo. **Por eso un fallo de recarga
se manifiesta como «datos de ayer» y no como «no hay datos»** — y por eso pasa inadvertido.
Ver [H12_recarga_qlik_fallo](../H%20-%20Cierre%20y%20Qlik/H12_recarga_qlik_fallo.md).

### Los datos que no son de Megara sólo existen en el QVD

Si un QVD se corrompe o se pierde, la parte `cod_sacbbdd <> 'MEG'` **no se puede reconstruir desde
esta base**: no está en `trf_s3`. Es un punto de dependencia que conviene conocer antes de tocar
ficheros QVD.

## Dónde viven

```
lib://QVD (cloud_datahubadmin02)/<nombre>.qvd
```

Con nombres del tipo `sac_qlik_pl_cl_patrrf_v`, `sac_qlik_cart_pos_rf_v`. La correspondencia
tabla → QVD está en la lista `INLINE` del propio script. Ver [H06_script_carga_qlik](../H%20-%20Cierre%20y%20Qlik/H06_script_carga_qlik.md).

## Cómo verificar qué debería estar publicado

Desde la base sólo se ve la parte de Megara — que es la que se recarga:

```sql
SELECT count(*) FROM trf_s3.<TABLA> WHERE base_id = 0;
SELECT max(dat_qlikupdate) FROM trf_s3.<TABLA>;
```

El contenido real del QVD sólo se comprueba desde Qlik.

## Ver también

[H06_script_carga_qlik](../H%20-%20Cierre%20y%20Qlik/H06_script_carga_qlik.md) · [H12_recarga_qlik_fallo](../H%20-%20Cierre%20y%20Qlik/H12_recarga_qlik_fallo.md) · [H13_fechas_de_corte](../H%20-%20Cierre%20y%20Qlik/H13_fechas_de_corte.md) · [I18_columnas_comunes](../I%20-%20Referencia%20de%20datos/I18_columnas_comunes.md) · [H09_qlik_datos_de_ayer](../H%20-%20Cierre%20y%20Qlik/H09_qlik_datos_de_ayer.md)

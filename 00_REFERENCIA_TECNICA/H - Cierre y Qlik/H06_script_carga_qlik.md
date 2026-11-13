---
titulo: "H06 — El script de carga de Qlik: cómo funciona"
familia: H
etapa: "Cierre y Qlik"
tipo: Referencia
tags:
  - familia/H
  - etapa/cierre-y-qlik
  - tipo/referencia
keywords: "script de carga, app de Qlik, LIB CONNECT, SQL SELECT, QVD, relaciontablacolumnas"
---

# H06 — El script de carga de Qlik: cómo funciona

**Etapa:** Cierre y Qlik
**Tipo:** Referencia
**Palabras clave:** script de carga, app de Qlik, LIB CONNECT, SQL SELECT, QVD, relaciontablacolumnas

## En una línea

Qlik **no recibe datos: los va a buscar**. Su script se conecta a PostgreSQL y hace `SELECT` directo
contra `trf_s3`.

## La estructura

```qlik
LIB CONNECT TO 'Aldrin PRD (cloud_datahubadmin02)';

tablas:
LOAD * INLINE [
Tabla,Data,NombreQvd
sac_pl_cl_patrrf_t,dat_pos,sac_qlik_pl_cl_patrrf_v
cart_pos_rf_t,dat_hist,sac_qlik_cart_pos_rf_v
...
];

FOR NTabla = 1 to NoOfRows('tablas')
    LET NameTable  = PEEK('Tabla',NTabla-1,'tablas');
    LET VName_qvd  = PEEK('NombreQvd',NTabla-1,'tablas');
    LET FieldData  = PEEK('Data',NTabla-1,'tablas');
    ...
NEXT NTabla
```

Una lista **codificada dentro del script** con tres columnas por tabla: nombre, campo de fecha y
nombre del QVD.

## Los cuatro pasos por tabla

### 1. Averigua qué columnas cargar

```sql
SQL SELECT STRING_AGG(distinct(columna), ',') AS columnas_concatenadas
    FROM exp_s3.relaciontablacolumnas
    WHERE tabla = '$(NameTable)';
LET valores = PEEK('columnas_concatenadas');
```

**Aquí es donde entra `relaciontablacolumnas`.** Si no hay columnas declaradas para esa tabla, la
variable queda vacía y el `LOAD` posterior se genera inválido. Ver [H07_lookup_qlik](../H%20-%20Cierre%20y%20Qlik/H07_lookup_qlik.md).

### 2. Carga el QVD anterior, filtrando

```qlik
temp:
LOAD $(valores), cod_mload_trace, cod_sacbbdd
FROM [lib://QVD (cloud_datahubadmin02)/$(VName_qvd).qvd](qvd);

$(NameTable):
LOAD * RESIDENT temp WHERE cod_sacbbdd <> 'MEG' AND $(FieldData) >= '2025-08-01';
DROP TABLE temp;
```

**Conserva del QVD todo lo que NO sea de Megara.** Lo de Megara se va a recargar fresco desde la
base. Ver [H11_qvd_incremental](../H%20-%20Cierre%20y%20Qlik/H11_qvd_incremental.md).

### 3. Añade lo nuevo por SQL

```sql
SQL SELECT $(valores), cod_mload_trace, cod_sacbbdd
    FROM trf_s3.$(NameTable) AS tr
    JOIN (SELECT cod_cli AS cod_cli_i, max(dat_hr_nav) AS dat_hr_nav
          FROM trf_s3.s3_interface_control_xml_t
          WHERE des_status IN ('Publish','WaitingFMValidation')
          GROUP BY cod_cli) AS interfaz
      ON tr.cod_cli = interfaz.cod_cli_i
    WHERE date($(FieldData)) <= date(interfaz.dat_hr_nav)
      AND tr.base_id = 0
      AND date($(FieldData)) >= '2024-12-31';
```

**Tres filtros determinan qué se publica:**

| Filtro | Efecto |
|---|---|
| `des_status IN ('Publish','WaitingFMValidation')` | Sólo clientes en esos dos estados |
| `date(<campo>) <= date(dat_hr_nav)` | Sólo datos hasta la fecha de NAV del cliente |
| `tr.base_id = 0` | Sólo la base 0 |

Ver [R4_04_s3_interface_control](../R4%20-%20Sets%20incompletos/R4_04_s3_interface_control.md) y [I18_columnas_comunes](../I%20-%20Referencia%20de%20datos/I18_columnas_comunes.md).

### 4. Guarda el QVD y libera

```qlik
STORE $(NameTable) INTO [lib://QVD (cloud_datahubadmin02)/$(VName_qvd).qvd](qvd);
DROP TABLE $(NameTable);
```

## Las tres secciones del script

El script tiene **tres bloques** con listas de tablas y cortes de fecha distintos:

| Sección | Tablas | Corte | Particularidad |
|---|---|---|---|
| 1 | 16 | `>= '2025-08-01'` | Cruza contra el control de interfaces |
| 2 | 2 | `>= '2025-08-01'` | **Sin** cruce contra el control |
| 3 | 21 | `>= '2025-03-01'` | Cruce con `DISTINCT` y más columnas |

Las secciones 1 y 3 **se solapan mucho** en las tablas que recorren. Parece evolución del script más
que diseño: una versión nueva convive con la anterior.

En total el script recorre **23 tablas distintas**, mientras que `relaciontablacolumnas` declara
**103**. Las otras 80 no las carga esta app.

## Qué comprobar cuando falla

```sql
-- ¿Tiene columnas declaradas la tabla?
SELECT count(*) FROM exp_s3.relaciontablacolumnas
WHERE  lower(tabla) = lower('<TABLA>');

-- ¿Coinciden con las columnas reales?
SELECT (SELECT count(*) FROM exp_s3.relaciontablacolumnas r
        WHERE lower(r.tabla) = lower('<TABLA>'))                             AS declaradas,
       (SELECT count(*) FROM information_schema.columns c
        WHERE c.table_schema='trf_s3' AND c.table_name = lower('<TABLA>'))   AS reales;
```

Un desajuste entre ambas rompe el `SELECT` generado. Ver [H12_recarga_qlik_fallo](../H%20-%20Cierre%20y%20Qlik/H12_recarga_qlik_fallo.md).

## Ver también

[H11_qvd_incremental](../H%20-%20Cierre%20y%20Qlik/H11_qvd_incremental.md) · [H13_fechas_de_corte](../H%20-%20Cierre%20y%20Qlik/H13_fechas_de_corte.md) · [H07_lookup_qlik](../H%20-%20Cierre%20y%20Qlik/H07_lookup_qlik.md) · [H12_recarga_qlik_fallo](../H%20-%20Cierre%20y%20Qlik/H12_recarga_qlik_fallo.md) · [R4_04_s3_interface_control](../R4%20-%20Sets%20incompletos/R4_04_s3_interface_control.md)

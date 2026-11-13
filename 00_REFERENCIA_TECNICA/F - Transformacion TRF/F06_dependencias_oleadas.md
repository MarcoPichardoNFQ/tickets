---
titulo: "F06 — Dependencias y oleadas: por qué el orden importa"
familia: F
etapa: "Transformación TRF"
tipo: Referencia
tags:
  - familia/F
  - etapa/transformacion-trf
  - tipo/referencia
keywords: "dependencias, oleada, orden, bloques, catálogos, cascada"
---

# F06 — Dependencias y oleadas: por qué el orden importa

**Etapa:** Transformación TRF
**Tipo:** Referencia
**Palabras clave:** dependencias, oleada, orden, bloques, catálogos, cascada

## En una línea

Los bloques están numerados por **dependencia de datos**, no por tamaño: los primeros cargan los
catálogos que los últimos necesitan para resolver sus claves foráneas.

## El concepto de oleada

El catálogo de transformaciones asigna a cada procedimiento una **oleada** (`oleada`), que expresa
en qué momento del ciclo puede ejecutarse:

```
name, tablas_destino, dependencias_intra_lote, datos_ya_residentes, oleada
ch_cashtrantype_transf_pc, trf_s3.sss_cashtrantype_t, , stg_s3.meg_cashtrantype_t, 0
cs_addl_deriv_price_pc,    trf_s3.sss_addl_deriv_price_t, , stg_s3.meg_addl_deriv_price_t, 0
```

| Columna | Qué dice |
|---|---|
| `tablas_destino` | Qué tabla escribe |
| `dependencias_intra_lote` | Qué **otras transformaciones del mismo lote** necesita antes |
| `datos_ya_residentes` | Qué tablas de staging lee |
| `oleada` | Su turno. **Oleada 0 = sin dependencias**, puede ir primero |

Una transformación con `dependencias_intra_lote` vacía y oleada 0 sólo necesita su tabla de
staging. Las de oleada superior esperan a que otras terminen.

## Cómo se traduce en los bloques

| Bloques | Contenido | Papel |
|---|---|---|
| 1, 2, 2.5 | Catálogos: categorías fiscales, entidades, divisas, mercados, calendarios | **Todo lo demás depende de ellos** |
| 3 | Activos: acciones, bonos, opciones, futuros, fondos | Dependen de 1-2.5 |
| 4.x, 5.x | Posiciones, precios, eventos corporativos | Dependen de 3 |
| 6.x, 7.x | Movimientos, valoración, rentabilidad, comisiones | Dependen de casi todo |

## La consecuencia para diagnosticar

**Un fallo en un bloque bajo se manifiesta como descartes masivos en los bloques altos.**

Si el bloque 1 no carga el catálogo de divisas, todas las tablas de los bloques 5, 6 y 7 que
referencian divisa descartan filas por clave foránea — y el síntoma aparece muy lejos de la causa.

Regla práctica: **ante descartes de `FOREIGN_KEY` en un bloque alto, comprueba primero si los
bloques anteriores corrieron bien.**

```sql
-- Recorrido del ciclo de hoy, en orden cronológico
SELECT cod_load_plan, cod_load_trace, dat_load_date, step_load,
       cod_status, amt_register_process
FROM   stg_s3.aud_load_trace_t
WHERE  dat_load_date::date = CURRENT_DATE
ORDER  BY dat_load_date;
```

Un hueco o un `cod_status = -1` en las primeras entradas explica lo que pase después.
Ver [R4_11_efecto_domino](../R4%20-%20Sets%20incompletos/R4_11_efecto_domino.md).

## Qué catálogos hacen más daño si fallan

Los más referenciados por integridad declarada:

```sql
SELECT des_table_fk, count(*) AS la_referencian
FROM   stg_s3.par_maestro_valid_t
WHERE  des_table_fk IS NOT NULL
GROUP  BY 1 ORDER BY 2 DESC LIMIT 15;
```

Merece tener esa lista revisada: son las tablas cuyo fallo se multiplica por todo el sistema.
Ver [E05_par_maestro_valid_t](../E%20-%20Parametrizacion/E05_par_maestro_valid_t.md).

## Al relanzar

**El orden importa igual que en la ejecución normal.** Relanzar una transformación de bloque alto
sin haber resuelto la de bloque bajo repite el mismo resultado.

La secuencia correcta ante un dominó es de abajo arriba: catálogo → transformaciones dependientes →
mapeos → recarga de Qlik. Ver [R4_11_efecto_domino](../R4%20-%20Sets%20incompletos/R4_11_efecto_domino.md).

## Ver también

[D07_bloques_optimizacio](../D%20-%20Carga%20STG/D07_bloques_optimizacio.md) · [R4_11_efecto_domino](../R4%20-%20Sets%20incompletos/R4_11_efecto_domino.md) · [E05_par_maestro_valid_t](../E%20-%20Parametrizacion/E05_par_maestro_valid_t.md) · [I09_indice_tabla_origen](../I%20-%20Referencia%20de%20datos/I09_indice_tabla_origen.md) · [F14_faltan_datos_stg_o_trf](../F%20-%20Transformacion%20TRF/F14_faltan_datos_stg_o_trf.md)

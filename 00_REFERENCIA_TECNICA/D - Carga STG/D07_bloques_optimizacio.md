---
titulo: "D07 — Los bloques `OptimizacioBloque*TRFySTG`"
familia: D
etapa: "Carga STG"
tipo: Referencia
tags:
  - familia/D
  - etapa/carga-stg
  - tipo/referencia
keywords: "bloques, OptimizacioBloque, orden, dependencias, scriptargs, paso a paso"
---

# D07 — Los bloques `OptimizacioBloque*TRFySTG`

**Etapa:** Carga STG
**Tipo:** Referencia
**Palabras clave:** bloques, OptimizacioBloque, orden, dependencias, scriptargs, paso a paso

## En una línea

Catorce jobs de Rundeck agrupan todas las cargas y transformaciones; dentro de cada uno, cada paso
carga una tabla y ejecuta acto seguido su transformación.

## Detalle

### Los bloques

| Bloque | Contenido predominante |
|---|---|
| 1 | Catálogos básicos: categorías fiscales, naturalezas de cuenta, clasificaciones CVM, país, divisa, mercado |
| 2 | Entidades: emisores, garantes, custodios, brókers, contrapartes, administradores, auditores |
| 2.5 | Referencias y calendarios: tasas, entradas de cuenta, calendarios, sectores |
| 3 | Activos: acciones, bonos, opciones, futuros, fondos, forwards, swaps, clientes y sus cuentas |
| 4.1 | Cuentas nostro y precios de activo |
| 4.2 | Eventos corporativos, posiciones elegibles, pagos, curvas de tipos |
| 5.1 | Rentabilidad indexada, bancos, posiciones CGC, precios de valoración |
| 5.2 | FRC, SCC, SCS, criterios de precio, benchmarks, flujos de caja |
| 5.3 | Reglas de comisión |
| 6.1 | Movimientos y transferencias de efectivo, bloqueos, órdenes |
| 6.2 | Ejecuciones netas de mercado |
| 7.1 | Valor liquidativo, pasivos, participaciones |
| 7.2 | — |
| 7.3 | Rentabilidad, performance, comisiones, transacciones |

Además existen `Optimizacion1,2,2.5TrfyStg` (agrupa los tres primeros) y
`0999 -. Optimizacao Blocos Rundeck V6` como orquestador general.

### Anatomía de un paso

Cada paso del job ejecuta el mismo script con un par de valores:

```
<description>0030 - LOAD STG MEG_TAX_PAYER_CAT_T,0040 - LOAD TRF TAX PAYER</description>
<scriptargs>159,124</scriptargs>
```

`159` es el id de `lookup_stg.txt` — va en posición impar, así que es una **carga**.
`124` es el id de `lookup_trf.txt` — posición par, así que es una **transformación**.

La descripción del paso te dice en texto plano qué tabla se carga y qué se transforma. Es la forma
más rápida de localizar en qué bloque vive una interfaz: busca el nombre de la tabla en las
descripciones de los jobs.

### Por qué el orden importa

Los bloques están numerados por **dependencia**, no por tamaño. El bloque 1 carga catálogos que el
bloque 3 necesita para resolver sus claves foráneas. Si el bloque 1 falla o se salta, el bloque 3
descarta filas masivamente por integridad referencial y el diagnóstico apunta al sitio equivocado.

Regla práctica: **ante descartes de clave foránea en un bloque alto, comprueba primero si los
bloques anteriores corrieron bien.** Ver [R1_06_descarte_integridad_referencial](../R1%20-%20Descartes/R1_06_descarte_integridad_referencial.md).

### Un fallo no detiene el bloque

El script de carga lleva sus `exit` comentados: un paso que falla marca el error pero el bloque
continúa con los pasos siguientes. El job acaba en rojo, pero **todos sus pasos se ejecutaron**.
No supongas que lo que va detrás del primer fallo se quedó sin correr. Ver [D03_script_stg_trf](../D%20-%20Carga%20STG/D03_script_stg_trf.md).

## Cómo verificarlo

En Rundeck, abre el job del bloque y revisa el resultado paso a paso: cada paso indica su
descripción y su resultado individual. En base de datos:

```sql
-- Qué cargó cada plan hoy, ordenado por hora: reconstruye el recorrido del bloque
SELECT cod_load_plan, cod_load_trace, dat_load_date,
       step_load, cod_status, amt_register_process
FROM   stg_s3.aud_load_trace_t
WHERE  dat_load_date::date = CURRENT_DATE
ORDER  BY dat_load_date;
```

## Ver también

[D03_script_stg_trf](../D%20-%20Carga%20STG/D03_script_stg_trf.md) · [D02_lookup_stg_formato](../D%20-%20Carga%20STG/D02_lookup_stg_formato.md) · [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md) · [R1_06_descarte_integridad_referencial](../R1%20-%20Descartes/R1_06_descarte_integridad_referencial.md)

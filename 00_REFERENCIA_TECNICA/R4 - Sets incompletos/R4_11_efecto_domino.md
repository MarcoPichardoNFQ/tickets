---
titulo: "R4.11 — Efecto dominó: qué se para cuando falta un fichero"
familia: R4
etapa: "Transversal"
tipo: Runbook
tags:
  - familia/R4
  - etapa/transversal
  - tipo/runbook
keywords: "efecto dominó, cascada, dependencias, propagación, catálogo, bloques"
---

# R4.11 — Efecto dominó: qué se para cuando falta un fichero

**Etapa:** Transversal
**Tipo:** Runbook
**Palabras clave:** efecto dominó, cascada, dependencias, propagación, catálogo, bloques

## En una línea

Un fichero que falta no se queda quieto: se propaga como descartes de clave foránea, mapeos vacíos
y un cierre que no se completa.

## La cadena de propagación

```
Falta el fichero de un CATÁLOGO
   ↓
No se carga su tabla en stg_s3
   ↓
Las tablas que lo referencian descartan filas por FOREIGN_KEY  → _DES
   ↓  (o, en flujo estricto, se TRUNCAN por completo)
La transformación produce menos filas de lo normal en trf_s3
   ↓
Los mapeos que leen esas tablas devuelven menos filas o ninguna
   ↓
El conteo de interfaces no cuadra y el cierre no se completa
   ↓
Qlik muestra datos incompletos o de ayer
```

Cada eslabón genera sus propios síntomas y sus propias alertas. **Lo peligroso es tratar cada
síntoma como una incidencia independiente**: se acaban abriendo cinco tickets para una sola causa.

## Cómo reconocer que estás ante un dominó

Tres señales, y con dos basta:

1. **Descartes de clave foránea en varias tablas a la vez**, todos apuntando a la misma tabla referenciada.
2. **Los descartes empiezan todos a la misma hora**.
3. **Las tablas afectadas están en bloques posteriores** al de la tabla que falta.

```sql
-- Descartes de FK de hoy, agrupados: si una sola causa afecta a muchas tablas, se ve aquí
SELECT des_table_name, des_column_name, count(*) AS filas, min(dat_load_date) AS desde
FROM   stg_s3.aud_load_valid_trace_t
WHERE  des_validate = 'FOREIGN_KEY'
  AND  dat_load_date::date = CURRENT_DATE
GROUP  BY 1,2
ORDER  BY filas DESC;
```

Muchas tablas distintas con descartes que empiezan a la misma hora = una causa común aguas arriba.

## Cómo encontrar la causa raíz

### 1. Identifica la tabla referenciada común

```sql
-- Para cada tabla con descartes de FK, a quién referencia esa columna
SELECT v.des_table, v.des_column, v.des_table_fk
FROM   stg_s3.par_maestro_valid_t v
WHERE  v.des_table ILIKE '%<TABLA_CON_DESCARTES>%';
```

Si varias tablas afectadas apuntan al mismo `des_table_fk`, ése es el catálogo culpable.

### 2. Comprueba si ese catálogo se cargó

```sql
SELECT count(*) FROM stg_s3.<CATALOGO>_T;

SELECT cod_load_trace, dat_load_date, cod_status, amt_register_process, des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  des_file_loaded ILIKE '%<CATALOGO>%'
ORDER  BY dat_load_date DESC LIMIT 5;
```

Sin traza de hoy = no se cargó. Y entonces la pregunta es si llegó el fichero:

```sql
SELECT nome_interface_base, recebido, track_status
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
  AND  nome_interface_base ILIKE '%<INTERFAZ>%';
```

### 3. Mide el alcance antes de actuar

```sql
SELECT des_table_fk, count(*) AS tablas_dependientes
FROM   stg_s3.par_maestro_valid_t
WHERE  des_table_fk ILIKE '%<CATALOGO>%'
GROUP  BY 1;
```

## El orden de recuperación

Cuando el fichero por fin llega, la recuperación va **en el mismo orden del dominó**, de arriba
abajo. Saltarse un paso deja el siguiente sin efecto:

1. **Cargar el catálogo** que faltaba.
2. **Reprocesar los descartes** de las tablas afectadas — `fn_reproceso_descart`, y volver a lanzar
   su carga para que atraviesen la validación. Ver [R1_09_reprocesar_descartes](../R1%20-%20Descartes/R1_09_reprocesar_descartes.md).
3. **Reejecutar las transformaciones** de esas tablas.
4. **Reejecutar los mapeos** que las consumen.
5. **Forzar la recarga de Qlik** de las tablas afectadas.

Si te quedas en el paso 2, el dato está en `stg_s3` pero no llega al usuario, y el ticket vuelve.

## El caso peor: flujo estricto

Si alguna de las tablas afectadas tiene `valid_err_des ≠ 1`, no hay descartes que reprocesar:
**la tabla se truncó entera**. Hay que recargar su fichero, no reprocesar.

```sql
SELECT p.cod_load_plan, t.des_table, p.valid_err_des
FROM   stg_s3.par_load_plan_t p
LEFT   JOIN stg_s3.par_maestro_tablas_t t ON t.cod_table = p.cod_table
WHERE  p.valid_err_des IS DISTINCT FROM 1;
```

Ten esa lista a mano: son las interfaces donde un dominó no deja descartes sino agujeros.
Ver [R1_01_descarte_vs_error](../R1%20-%20Descartes/R1_01_descarte_vs_error.md).

## Cuándo escalar

- En cuanto confirmes que es un dominó y no incidencias independientes: cambia la prioridad y el interlocutor.
- Si hay truncados de por medio: la recuperación exige recargas coordinadas.

## Ver también

[R4_09_esperar_forzar_escalar](../R4%20-%20Sets%20incompletos/R4_09_esperar_forzar_escalar.md) · [R1_06_descarte_integridad_referencial](../R1%20-%20Descartes/R1_06_descarte_integridad_referencial.md) · [R1_09_reprocesar_descartes](../R1%20-%20Descartes/R1_09_reprocesar_descartes.md) · [D07_bloques_optimizacio](../D%20-%20Carga%20STG/D07_bloques_optimizacio.md) · [R4_04_s3_interface_control](../R4%20-%20Sets%20incompletos/R4_04_s3_interface_control.md)

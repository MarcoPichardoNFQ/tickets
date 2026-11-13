---
titulo: "R3.08 — Dependencia insatisfecha: falta el insumo"
familia: R3
etapa: "Mapeos"
tipo: Runbook
tags:
  - familia/R3
  - etapa/mapeos
  - tipo/runbook
keywords: "insumo, dependencia, tabla de origen vacía, cascada, aguas arriba"
---

# R3.08 — Dependencia insatisfecha: falta el insumo

**Etapa:** Mapeos
**Tipo:** Runbook
**Palabras clave:** insumo, dependencia, tabla de origen vacía, cascada, aguas arriba

## Síntoma

El mapeo se ejecutó sin error y produjo cero filas o muchas menos de lo normal. El problema no está
en el mapeo: **está en lo que debía leer**.

## La comprobación

```sql
SELECT (SELECT count(*) FROM trf_s3.<TABLA_ORIGEN>)   AS origen,
       (SELECT count(*) FROM trf_s3.<TABLA_DESTINO>)  AS destino;
```

Origen a cero → el mapeo hizo su trabajo, no había nada. Sigue hacia atrás.

## Hacia atrás, paso a paso

### 1. ¿Se transformó?

```sql
SELECT dat_load_date, cod_load_plan, step_load, cod_status, des_log
FROM   stg_s3.aud_log_trace_t
WHERE  cod_status = -1 AND dat_load_date >= CURRENT_DATE
ORDER  BY dat_load_date DESC;
```

Ver [F10_localizar_fallo_trf](../F%20-%20Transformacion%20TRF/F10_localizar_fallo_trf.md).

### 2. ¿Se cargó?

```sql
SELECT cod_load_trace, dat_load_date, des_file_loaded,
       amt_register_process, cod_status, des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  des_file_loaded ILIKE '%<INTERFAZ>%'
ORDER  BY dat_load_date DESC LIMIT 5;
```

### 3. ¿Llegó el fichero?

```sql
SELECT nome_interface_base, recebido, track_status, data_recebemento
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
  AND  nome_interface_base ILIKE '%<INTERFAZ>%';
```

Ver [R4_05_flag_sin_xml](../R4%20-%20Sets%20incompletos/R4_05_flag_sin_xml.md).

## Qué tabla es el origen

Es la pregunta que bloquea el diagnóstico. Hay que leer la función:

```sql
SELECT prosrc FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'trf_s3' AND lower(p.proname) = lower('<nome_fn_mapeio>');
```

Busca los `FROM trf_s3.` y los `JOIN`. Y el catálogo del grafo de transformación da el sentido
inverso —qué procedimiento llena cada tabla—. Ver [I09_indice_tabla_origen](../I%20-%20Referencia%20de%20datos/I09_indice_tabla_origen.md).

## El caso frecuente: falta un catálogo, no el origen principal

**La tabla principal tiene datos y aun así el mapeo produce poco.** Entonces lo que falta es alguna
de las tablas con las que cruza.

Un `INNER JOIN` contra un catálogo vacío **elimina todas las filas**. Un `LEFT JOIN` sólo deja
nulos. Comprueba cada cruce:

```sql
SELECT count(*) FROM trf_s3.<TABLA_CRUZADA>;
```

Ver [R3_10_corrio_pero_no_llego](../R3%20-%20Errores%20de%20mapeo/R3_10_corrio_pero_no_llego.md) y [I07_codigos_cod_dm](../I%20-%20Referencia%20de%20datos/I07_codigos_cod_dm.md).

## Es casi siempre efecto dominó

Si varios mapeos producen poco a la vez, no son incidencias independientes: es una causa común
aguas arriba, normalmente un catálogo que no cargó.

```sql
-- Descartes de clave foránea de hoy, agrupados
SELECT des_table_name, des_column_name, count(*) AS filas, min(dat_load_date) AS desde
FROM   stg_s3.aud_load_valid_trace_t
WHERE  des_validate = 'FOREIGN_KEY' AND dat_load_date::date = CURRENT_DATE
GROUP  BY 1,2 ORDER BY filas DESC;
```

Muchas tablas distintas empezando a la misma hora = una sola causa. Ver [R4_11_efecto_domino](../R4%20-%20Sets%20incompletos/R4_11_efecto_domino.md).

## El orden de recuperación

Cuando el insumo llega, hay que ir **de arriba abajo**, sin saltarse pasos:

1. Cargar el catálogo o interfaz que faltaba
2. Reprocesar descartes si los hubo → [R1_09_reprocesar_descartes](../R1%20-%20Descartes/R1_09_reprocesar_descartes.md)
3. Reejecutar la transformación
4. Reejecutar el mapeo → [R3_11_relanzar_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_11_relanzar_mapeo.md)
5. Forzar la recarga de Qlik → [H12_recarga_qlik_fallo](../H%20-%20Cierre%20y%20Qlik/H12_recarga_qlik_fallo.md)

Quedarse en el paso 3 deja el dato en `trf_s3` sin llegar al usuario, y el ticket vuelve.

## Cuándo escalar

Siempre que el insumo falte de verdad: soporte no puede generarlo. Lo que sí aporta es el
diagnóstico —qué falta, desde cuándo, y cuántos mapeos dependen de ello—. Ver [J07_escalado](../J%20-%20Operacion/J07_escalado.md).

## Ver también

[R3_05_mapeo_cero_filas](../R3%20-%20Errores%20de%20mapeo/R3_05_mapeo_cero_filas.md) · [R4_11_efecto_domino](../R4%20-%20Sets%20incompletos/R4_11_efecto_domino.md) · [F14_faltan_datos_stg_o_trf](../F%20-%20Transformacion%20TRF/F14_faltan_datos_stg_o_trf.md) · [I09_indice_tabla_origen](../I%20-%20Referencia%20de%20datos/I09_indice_tabla_origen.md) · [R3_10_corrio_pero_no_llego](../R3%20-%20Errores%20de%20mapeo/R3_10_corrio_pero_no_llego.md)

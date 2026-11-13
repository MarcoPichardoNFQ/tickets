---
titulo: "R4.10 — Consultas: qué falta ahora mismo"
familia: R4
etapa: "Recepción de flags"
tipo: Runbook
tags:
  - familia/R4
  - etapa/recepcion-de-flags
  - tipo/runbook
keywords: "consultas, qué falta, set incompleto, copiar y pegar, comparar lotes"
---

# R4.10 — Consultas: qué falta ahora mismo

**Etapa:** Recepción de flags
**Tipo:** Runbook
**Palabras clave:** consultas, qué falta, set incompleto, copiar y pegar, comparar lotes

## En una línea

Las consultas para saber en 30 segundos qué falta, desde cuándo y si es normal.

## 1. Fija el lote

`last_value` se mueve si llega otro flag mientras investigas. Anótalo y úsalo literal.

```sql
SELECT last_value AS camda_actual FROM exp_s3.controlflag_arquivos_cod_id_seq;
```

## 2. Qué falta en el lote actual

```sql
SELECT nome_flag_geral,
       nome_interface_base,
       nome_interface_completo,
       track_status,
       begin_time, end_time
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = :camda
  AND  NOT recebido
ORDER  BY nome_interface_base;
```

## 3. Resumen de completitud

```sql
SELECT nome_flag_geral,
       count(*)                                                       AS declaradas,
       count(*) FILTER (WHERE recebido)                               AS presentes,
       count(*) FILTER (WHERE NOT recebido)                           AS faltan,
       count(*) FILTER (WHERE recebido AND NOT track_status)          AS con_aviso_origen,
       count(*) FILTER (WHERE recebido IS NULL OR track_status IS NULL) AS indeterminadas
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = :camda
GROUP  BY 1;
```

## 4. ¿Qué había antes y ahora no?

La comprobación que detecta el caso difícil: interfaces que el flag **ya ni declara**.

```sql
SELECT nome_flag_geral, nome_interface_base
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = :camda_anterior
EXCEPT
SELECT nome_flag_geral, nome_interface_base
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = :camda
ORDER  BY 1,2;
```

Y al revés, para ver interfaces nuevas:

```sql
SELECT nome_flag_geral, nome_interface_base
FROM   stg_s3.controlflag_interfaces WHERE id_camda = :camda
EXCEPT
SELECT nome_flag_geral, nome_interface_base
FROM   stg_s3.controlflag_interfaces WHERE id_camda = :camda_anterior;
```

## 5. ¿Es habitual que falte esta interfaz?

```sql
SELECT id_camda,
       recebido,
       track_status,
       data_recebemento
FROM   stg_s3.controlflag_interfaces
WHERE  nome_interface_base = '<INTERFAZ>'
ORDER  BY id_camda DESC
LIMIT  30;
```

Columna `recebido` con muchos `false` = patrón conocido. Todo `true` y hoy `false` = incidencia nueva.

## 6. Tamaños: detectar ficheros truncados

Presentes pero sospechosamente pequeños:

```sql
SELECT nome_interface_base,
       tamanho_interfaz::bigint AS bytes,
       data_recebemento
FROM   trf_s3.tmp_controlflag_interfaces
WHERE  id_camda = :camda
ORDER  BY tamanho_interfaz::bigint NULLS FIRST
LIMIT  20;
```

Frente a su propia historia:

```sql
SELECT id_camda, tamanho_interfaz::bigint AS bytes
FROM   trf_s3.tmp_controlflag_interfaces
WHERE  nome_interface_base = '<INTERFAZ>'
ORDER  BY id_camda DESC LIMIT 15;
```

## 7. Historial de llegada de flags

```sql
SELECT nome_base,
       max(data_recebemento) AS ultima_llegada,
       max(id_camda)         AS ultimo_lote,
       count(*)              AS llegadas_30d
FROM   stg_s3.controlflag_arquivos
WHERE  data > CURRENT_DATE - 30
GROUP  BY 1
ORDER  BY 2 DESC NULLS LAST;
```

Sirve para dos cosas: saber si un flag lleva sin llegar más de lo normal, y aprender la
periodicidad real de cada uno.

## 8. Salud del control

Lotes anormalmente grandes, señal de que dos llegadas se mezclaron:

```sql
SELECT id_camda, count(*) AS interfaces, min(nome_flag_geral) AS flag
FROM   stg_s3.controlflag_interfaces
GROUP  BY 1 ORDER BY 1 DESC LIMIT 15;
```

Ver [B08_id_camda_lote](../B%20-%20Recepcion%20y%20flags/B08_id_camda_lote.md).

## 9. Del control a la carga

`controlflag_interfaces` dice si el fichero llegó; **no** dice si se cargó. Para eso:

```sql
SELECT cod_load_trace, cod_load_plan, dat_load_date,
       des_file_loaded, amt_register_process, cod_status
FROM   stg_s3.aud_load_trace_t
WHERE  des_file_loaded ILIKE '%<INTERFAZ>%'
ORDER  BY dat_load_date DESC LIMIT 10;
```

No hay columna que enlace `id_camda` con `cod_load_trace`: el puente es el nombre del fichero.

## Ver también

[R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md) · [R4_05_flag_sin_xml](../R4%20-%20Sets%20incompletos/R4_05_flag_sin_xml.md) · [B08_id_camda_lote](../B%20-%20Recepcion%20y%20flags/B08_id_camda_lote.md) · [R1_11_consultas_descartes](../R1%20-%20Descartes/R1_11_consultas_descartes.md)

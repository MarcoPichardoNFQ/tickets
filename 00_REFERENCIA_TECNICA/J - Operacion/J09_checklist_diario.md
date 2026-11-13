---
titulo: "J09 — Checklist de verificación diaria"
familia: J
etapa: "Transversal"
tipo: Runbook
tags:
  - familia/J
  - etapa/transversal
  - tipo/runbook
keywords: "checklist, verificación diaria, rutina, comprobación, salud del sistema"
---

# J09 — Checklist de verificación diaria

**Etapa:** Transversal
**Tipo:** Runbook
**Palabras clave:** checklist, verificación diaria, rutina, comprobación, salud del sistema

## En una línea

Como 22 de los 46 jobs no avisan si fallan, la verificación activa no es opcional: es lo único que
detecta los fallos silenciosos.

## Por qué existe este checklist

El sistema tiene seis mecanismos documentados por los que un fallo puede pasar inadvertido:

- 22 jobs sin ninguna notificación
- `_00001 Análise de erros` anulado con `WHERE 1=0`
- La recarga global de Qlik que reporta éxito sin enviar nada
- Los mapeos desactivados que salen en verde
- La validación de variación de volumen que no se ejecuta
- Los mapeos huérfanos que nadie llama

**Una bandeja de entrada vacía no significa que el ciclo fuera bien.**

## Las siete comprobaciones

### 1. ¿Llegaron los flags esperados?

```sql
SELECT nome_base, max(data_recebemento) AS ultima, max(id_camda) AS lote
FROM   stg_s3.controlflag_arquivos
WHERE  data > CURRENT_DATE - 7
GROUP  BY 1 ORDER BY 2 DESC NULLS LAST;
```

Contrasta con la periodicidad de cada flag. Ver [B02_los_nueve_flags](../B%20-%20Recepcion%20y%20flags/B02_los_nueve_flags.md).

### 2. ¿Está completo el set del último lote?

```sql
SELECT nome_flag_geral,
       count(*)                             AS declaradas,
       count(*) FILTER (WHERE recebido)     AS presentes,
       count(*) FILTER (WHERE NOT recebido) AS faltan
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
GROUP  BY 1;
```

### 3. ¿Hubo errores de carga?

```sql
SELECT cod_load_trace, cod_load_plan, dat_load_date, step_load, des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  cod_status = -1 AND dat_load_date::date = CURRENT_DATE
ORDER  BY dat_load_date DESC;
```

### 4. ¿Cuántos descartes y de qué tipo?

```sql
SELECT des_table_name, des_validate, count(*) AS filas
FROM   stg_s3.aud_load_valid_trace_t
WHERE  dat_load_date::date = CURRENT_DATE
GROUP  BY 1,2 ORDER BY filas DESC LIMIT 20;
```

Lo que importa no es el número absoluto sino **si cambió respecto a días anteriores**.
Ver [R1_10_descarte_correcto_sin_accion](../R1%20-%20Descartes/R1_10_descarte_correcto_sin_accion.md).

### 5. ¿Hubo errores de mapeo?

```sql
SELECT * FROM trf_s3.s3_control_errores_mapeo
WHERE  dat_proc_exe::date = CURRENT_DATE
ORDER  BY dat_proc_exe DESC;
```

Filtrado por día, no por los 30 minutos que mira el job de control. Ver [G09_job_control_errores](../G%20-%20Mapeos/G09_job_control_errores.md).

### 6. ¿Quedaron ficheros atascados?

```bash
. /nfq/data/cfg/env.properties
find $raiz -name "*_InLoad*" -mmin +60 -ls      # cargas abortadas
find $destino -type f -mtime -1 | wc -l         # unmatched del día: debería ser 0
ls -la $bandera | grep -i "^Qlik_"              # recargas de Qlik sin consumir
```

### 7. ¿Está vivo el vigilante?

En Rundeck, el job `0999 Carga Megara` debería mostrar ejecuciones continuas, cada 3 segundos. Una
interrupción en esa serie marca la hora exacta en que el sistema se paró.

**Es la comprobación más importante de las siete** y la que no tiene alerta.
Ver [B04_job_validacion_constante](../B%20-%20Recepcion%20y%20flags/B04_job_validacion_constante.md).

## Versión rápida: una sola consulta

Para el vistazo de la mañana:

```sql
SELECT 'errores de carga'  AS que, count(*) AS n
FROM   stg_s3.aud_load_trace_t
WHERE  cod_status = -1 AND dat_load_date::date = CURRENT_DATE
UNION ALL
SELECT 'errores tecnicos', count(*)
FROM   stg_s3.aud_log_trace_t
WHERE  cod_status = -1 AND dat_load_date >= CURRENT_DATE
UNION ALL
SELECT 'descartes hoy', count(*)
FROM   stg_s3.aud_load_valid_trace_t
WHERE  dat_load_date::date = CURRENT_DATE
UNION ALL
SELECT 'errores de mapeo', count(*)
FROM   trf_s3.s3_control_errores_mapeo
WHERE  dat_proc_exe::date = CURRENT_DATE
UNION ALL
SELECT 'interfaces que faltan', count(*)
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
  AND  NOT recebido;
```

Cinco números. Compáralos con los de ayer: **lo que importa es la variación, no el valor**.

## Qué anotar

Lleva registro de los cinco números cada día. Sin línea base, no hay forma de distinguir «300
descartes» normal de «300 descartes» anómalo, y esa distinción es la mitad del trabajo.

## Ver también

[R5_02_jobs_sin_notificacion](../R5%20-%20Alertas%20Rundeck/R5_02_jobs_sin_notificacion.md) · [R5_07_alerta_vs_estado_real](../R5%20-%20Alertas%20Rundeck/R5_07_alerta_vs_estado_real.md) · [R5_08_analise_de_erros_anulado](../R5%20-%20Alertas%20Rundeck/R5_08_analise_de_erros_anulado.md) · [R1_11_consultas_descartes](../R1%20-%20Descartes/R1_11_consultas_descartes.md) · [R4_10_consultas_que_falta](../R4%20-%20Sets%20incompletos/R4_10_consultas_que_falta.md)

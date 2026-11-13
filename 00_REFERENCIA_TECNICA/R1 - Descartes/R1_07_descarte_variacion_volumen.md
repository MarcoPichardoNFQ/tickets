---
titulo: "R1.07 — Validación de variación de volumen"
familia: R1
etapa: "Validación"
tipo: Referencia
tags:
  - familia/R1
  - etapa/validacion
  - tipo/referencia
keywords: "validate_variation_fn, des_variation, volumen, amt_register_process, variación anómala"
---

# R1.07 — Validación de variación de volumen

**Etapa:** Validación
**Tipo:** Referencia
**Palabras clave:** validate_variation_fn, des_variation, volumen, amt_register_process, variación anómala

## En una línea

Existe una validación que compara el volumen de una carga con el de la anterior, pero **no se
invoca desde el flujo normal de validación y, tal como está escrita, no compara lo que parece**.

## Detalle

### Qué pretende hacer

`stg_s3.validate_variation_fn(tabla, cod_load_trace, cod_load_plan, des_variation)` recibe un
porcentaje de tolerancia —`des_variation`, columna de `PAR_LOAD_PLAN_T`— y comprueba que el número
de registros de la carga actual esté dentro de ese margen respecto de la carga anterior:

```
máximo = anterior + (anterior * variación/100)
mínimo = anterior - (anterior * variación/100)
```

Devuelve `0` si el volumen está dentro del margen y `-1` si se sale.

### Dos motivos por los que no te va a avisar de nada

**1. No se llama desde `validate_gen_pc()`.** El orquestador de validaciones recibe el parámetro
`pi_des_variation` y declara variables para ello, pero en su cuerpo sólo ejecuta nulos, formato y
claves foráneas. La validación de variación no forma parte de la cadena.

**2. La comparación no filtra por tabla.** Las dos consultas que obtienen «la carga actual» y «la
carga anterior» son de esta forma:

```sql
SELECT amt_register_process FROM stg_s3.aud_load_trace_t
WHERE  dat_load_date IN (
         SELECT MAX(dat_load_date) FROM stg_s3.aud_load_trace_t
         WHERE cod_load_trace IN (SELECT MAX(cod_load_trace) - 1
                                  FROM stg_s3.aud_load_trace_t))
AND    amt_register_process IS NOT NULL;
```

No hay ninguna condición sobre `cod_load_plan` ni sobre la tabla. `MAX(cod_load_trace)` y
`MAX(cod_load_trace) - 1` son **las dos últimas cargas del sistema entero**, sean de la interfaz
que sean. Comparar el volumen de `Bond` con el de `AccountCategory` no significa nada.

### Qué implica para BAU

- **No confíes en esta validación para detectar un fichero truncado o inflado.** No está en la cadena y, si se invocara, compararía peras con manzanas.
- Si necesitas control de volumen, hazlo a mano contra el histórico de la misma interfaz. La consulta está más abajo.
- Un volumen anómalo pasará silenciosamente a `_T` y llegará hasta Qlik.

Éste es el tipo de cosa que conviene tener presente: la existencia de una función con un nombre
tranquilizador no prueba que haya control real. Ver también `_00001_Análise_de_erros`, que está
anulado con `WHERE 1=0` y ficha `R5.08`.

## Cómo verificarlo

Control de volumen manual, por interfaz, comparando contra su propia historia:

```sql
SELECT cod_load_plan,
       dat_load_date::date       AS dia,
       des_file_loaded,
       amt_register_process      AS filas
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_plan = :plan
  AND  amt_register_process IS NOT NULL
ORDER  BY dat_load_date DESC
LIMIT  30;
```

Y para detectar saltos bruscos en el último día frente a la media de los 10 anteriores:

```sql
WITH h AS (
  SELECT cod_load_plan, dat_load_date, amt_register_process,
         ROW_NUMBER() OVER (PARTITION BY cod_load_plan ORDER BY dat_load_date DESC) AS rn
  FROM   stg_s3.aud_load_trace_t
  WHERE  amt_register_process IS NOT NULL
)
SELECT cod_load_plan,
       MAX(CASE WHEN rn = 1 THEN amt_register_process END)      AS ultima,
       ROUND(AVG(CASE WHEN rn BETWEEN 2 AND 11
                      THEN amt_register_process END))           AS media_10_previas
FROM   h
WHERE  rn <= 11
GROUP  BY cod_load_plan
ORDER  BY 1;
```

## Ver también

[R1_03_identificar_validacion](../R1%20-%20Descartes/R1_03_identificar_validacion.md) · [R1_12_descarte_masivo_escalado](../R1%20-%20Descartes/R1_12_descarte_masivo_escalado.md) · [R1_11_consultas_descartes](../R1%20-%20Descartes/R1_11_consultas_descartes.md)

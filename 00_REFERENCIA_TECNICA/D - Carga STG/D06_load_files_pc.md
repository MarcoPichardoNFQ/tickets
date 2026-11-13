---
titulo: "D06 — `LOAD_FILES_PC`: acondicionamiento de `_TMP`"
familia: D
etapa: "Carga STG"
tipo: Referencia
tags:
  - familia/D
  - etapa/carga-stg
  - tipo/referencia
keywords: "load_files_pc, COD_SEQ, COD_LOAD_TRACE, trim, normalización, código de salida"
---

# D06 — `LOAD_FILES_PC`: acondicionamiento de `_TMP`

**Etapa:** Carga STG
**Tipo:** Referencia
**Palabras clave:** load_files_pc, COD_SEQ, COD_LOAD_TRACE, trim, normalización, código de salida

## En una línea

A pesar del nombre no carga ningún fichero: numera las filas que ya están en `_TMP`, las marca con
el `cod_load_trace` y normaliza los valores antes de validarlos.

## Detalle

### Qué hace de verdad

Cuando se ejecuta, el `\COPY` ya metió los datos en `_TMP`. Este procedimiento:

**1. Rellena las tres columnas de control**

```sql
UPDATE stg_s3.<TABLA>_TMP
SET    <COD_SEQ_*>   = nextval('stg_s3.<secuencia>'),
       COD_ENT_GEO    = <entidad>,
       COD_LOAD_TRACE = <trace>
WHERE  <COD_SEQ_*> IS NULL AND COD_ENT_GEO IS NULL AND COD_LOAD_TRACE IS NULL;
```

Fíjate en el `WHERE`: sólo toca filas donde **las tres** están vacías. Filas que ya vengan con
alguna de ellas informada quedan sin numerar y sin `cod_load_trace`, y desaparecen del radar de las
validaciones y de las consultas por trace.

**2. Normaliza los vacíos**

```sql
UPDATE ... SET col = NULL WHERE trim(col) = '' OR UPPER(col) = 'NULL';
```

Una pasada por cada columna. Convierte la cadena vacía y el texto literal `NULL` en NULL real.

**3. Recorta espacios**

```sql
UPDATE ... SET col = trim(col) WHERE col IS NOT NULL;
```

Otra pasada por columna. En tablas anchas esto son decenas de `UPDATE` sobre la tabla completa: es
una de las razones por las que una carga grande tarda más de lo que parecería.

**4. Deja traza**

```sql
INSERT INTO stg_s3.AUD_LOAD_TRACE_T
VALUES (trace, proceso, NOW(), 'CARGA FICHERO', fichero, NULL, 0, <filas>, 0, ...);
```

`amt_register_process` recibe el número de filas afectadas por el paso 1. **Ése es el conteo real
de filas cargadas** y la cifra que debes usar para controlar volumen.

### ⚠ Dos rarezas del código

**El mensaje de éxito acaba en NULL.** La traza se inserta con
`'Fichero Cargado Correctamente: ' || V_SQLERR`, y en el camino de éxito `V_SQLERR` está vacío. En
PostgreSQL, concatenar texto con NULL da **NULL**. Así que `des_process_executed` queda en NULL, no
con el texto. Normalmente no se nota porque `VALIDATE_GEN_PC` lo sobrescribe después con el
recorrido real; pero si la validación no llega a ejecutarse, la fila se queda con la descripción
vacía. Una traza sin descripción no significa que no pasara nada.

**El código de salida está invertido.** El procedimiento contiene un bloque que compara un contador
de columnas que nunca se rellena, y termina asignando `po_outcode := -1` cuando **sí** hubo filas y
`0` cuando **no** las hubo. Como el llamador no puede leer ese valor de vuelta (ver
[D05_run_load_plan_pc](../D%20-%20Carga%20STG/D05_run_load_plan_pc.md)), en la práctica da igual — pero explica por qué el código de retorno de
esta etapa no sirve para diagnosticar nada.

**Conclusión operativa: juzga la carga por los datos y las trazas, no por códigos de retorno.**

## Cómo verificarlo

```sql
-- Filas cargadas según la traza, frente a las que hay realmente
SELECT amt_register_process AS segun_traza
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_trace = :trace AND step_load = 'CARGA FICHERO';

SELECT count(*) AS realmente_en_tmp
FROM   stg_s3.<TABLA>_TMP
WHERE  cod_load_trace = :trace;
```

```sql
-- ¿Hay filas huérfanas sin trace? No deberían existir
SELECT count(*) FROM stg_s3.<TABLA>_TMP WHERE cod_load_trace IS NULL;
```

## Ver también

[D05_run_load_plan_pc](../D%20-%20Carga%20STG/D05_run_load_plan_pc.md) · [D01_mecanica_carga_copy](../D%20-%20Carga%20STG/D01_mecanica_carga_copy.md) · [E06_tablas_auditoria](../E%20-%20Parametrizacion/E06_tablas_auditoria.md) · [R1_04_descarte_nulo_obligatorio](../R1%20-%20Descartes/R1_04_descarte_nulo_obligatorio.md)

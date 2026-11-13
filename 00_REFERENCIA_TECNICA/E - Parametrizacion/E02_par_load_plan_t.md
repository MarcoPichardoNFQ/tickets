---
titulo: "E02 — `PAR_LOAD_PLAN_T` campo por campo"
familia: E
etapa: "Validación"
tipo: Referencia
tags:
  - familia/E
  - etapa/validacion
  - tipo/referencia
keywords: "par_load_plan_t, valid_err_des, des_variation, plan de carga, cod_load_plan"
---

# E02 — `PAR_LOAD_PLAN_T` campo por campo

**Etapa:** Validación
**Tipo:** Referencia
**Palabras clave:** par_load_plan_t, valid_err_des, des_variation, plan de carga, cod_load_plan

## En una línea

Una fila por cada carga parametrizada; define de dónde viene el fichero, cómo se lee, a dónde va y
—lo más importante— qué pasa cuando algo falla.

## Estructura

| Columna | Tipo | Qué hace |
|---|---|---|
| `cod_load_plan` | integer | Identificador del plan. Coincide con el id de `lookup_stg.txt` |
| `des_procedure_run` | varchar(255) | Procedimiento que ejecuta la carga. Normalmente `LOAD_FILES_PC` |
| `cod_table` | smallint | Enlaza con `PAR_MAESTRO_TABLAS_T` |
| `des_source_dir` | varchar(80) | Directorio de origen |
| `des_destiny_dir` | varchar(80) | Directorio de destino |
| `des_separator` | varchar(4) | Separador de campos |
| `amt_linestart` | integer | Línea de inicio |
| `amt_num_columns` | integer | Número de columnas esperado |
| `des_sequence_table` | varchar(50) | Secuencia que numera las filas (`COD_SEQ_*`) |
| `amt_lines_delete` | integer | Líneas a descartar del fichero |
| `des_column_delete` | varchar(50) | Columna usada para el borrado |
| `des_variation` | integer | Porcentaje de variación de volumen tolerado |
| `cod_ent_geo` | integer | Entidad geográfica |
| `valid_err_des` | integer, **default 1** | **Tolerante (1) o estricto (≠1) ante fallos** |

## Las dos columnas que hay que mirar siempre

### `valid_err_des` — la más importante del sistema

Con valor `1` las filas malas se apartan y la carga sigue. Con cualquier otro valor la carga aborta,
y un fallo de clave foránea ejecuta `TRUNCATE` sobre la tabla completa.

Es la primera consulta ante cualquier incidencia de descartes:

```sql
SELECT cod_load_plan, des_procedure_run, valid_err_des,
       CASE WHEN valid_err_des = 1
            THEN 'TOLERANTE: aparta filas y continúa'
            ELSE 'ESTRICTO: aborta; fallo de FK TRUNCA la tabla' END AS comportamiento
FROM   stg_s3.par_load_plan_t
ORDER  BY valid_err_des, cod_load_plan;
```

Detalle completo en [R1_01_descarte_vs_error](../R1%20-%20Descartes/R1_01_descarte_vs_error.md).

### `des_variation` — declarada pero sin efecto real

Es el porcentaje de tolerancia que usaría `VALIDATE_VARIATION_FN`. Se lee del plan y se pasa a
`VALIDATE_GEN_PC`, pero esa validación **no se ejecuta** dentro del flujo, y tal como está escrita
compara volúmenes de interfaces distintas. Que una interfaz tenga aquí un `10` no significa que
alguien vigile su volumen. Ver [R1_07_descarte_variacion_volumen](../R1%20-%20Descartes/R1_07_descarte_variacion_volumen.md).

## Otras trampas

**`amt_num_columns` no valida nada en la práctica.** Se pasa a `LOAD_FILES_PC` y allí se compara
contra un contador que nunca se rellena, en un bloque cuyo resultado no llega al llamador. La
comprobación real del número de columnas la hace el propio `\COPY` de PostgreSQL al fallar.
Ver [D06_load_files_pc](../D%20-%20Carga%20STG/D06_load_files_pc.md) y [D09_error_numero_columnas](../D%20-%20Carga%20STG/D09_error_numero_columnas.md).

**El separador vive en dos sitios.** Está en `des_separator` y también en el campo 6 de
`lookup_stg.txt`. **El que se usa en el `\COPY` es el del lookup**, porque lo lee el script de
shell. Si ambos difieren, manda el lookup y la tabla te está mintiendo:

```sql
SELECT cod_load_plan, des_separator FROM stg_s3.par_load_plan_t WHERE cod_load_plan = :id;
```
```bash
grep '|<id>|' /nfq/data/cfg/lookup_stg.txt | cut -d'|' -f6
```

**`cod_ent_geo` se lee pero no se usa** en la llamada de `RUN_LOAD_PLAN_PC`, que pasa el valor `2`
codificado directamente. Ver [D05_run_load_plan_pc](../D%20-%20Carga%20STG/D05_run_load_plan_pc.md).

## Cómo verificarlo

```sql
-- Ficha completa de un plan
SELECT * FROM stg_s3.par_load_plan_t WHERE cod_load_plan = :id;

-- Qué planes son estrictos: los de mayor riesgo de truncado
SELECT p.cod_load_plan, t.des_table, p.valid_err_des
FROM   stg_s3.par_load_plan_t   p
LEFT   JOIN stg_s3.par_maestro_tablas_t t ON t.cod_table = p.cod_table
WHERE  p.valid_err_des IS DISTINCT FROM 1
ORDER  BY 2;
```

Esa segunda consulta merece guardarse: la lista de interfaces que pueden perder la tabla entera por
una sola fila huérfana.

## Ver también

[E01_tablas_par_metadata_driven](../E%20-%20Parametrizacion/E01_tablas_par_metadata_driven.md) · [R1_01_descarte_vs_error](../R1%20-%20Descartes/R1_01_descarte_vs_error.md) · [D05_run_load_plan_pc](../D%20-%20Carga%20STG/D05_run_load_plan_pc.md) · [D02_lookup_stg_formato](../D%20-%20Carga%20STG/D02_lookup_stg_formato.md) · [R1_07_descarte_variacion_volumen](../R1%20-%20Descartes/R1_07_descarte_variacion_volumen.md)

---
titulo: "I08 — Las secuencias del sistema"
familia: I
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/I
  - etapa/transversal
  - tipo/referencia
keywords: "secuencias, last_value, nextval, cod_load_trace, id_camda, contador"
---

# I08 — Las secuencias del sistema

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** secuencias, last_value, nextval, cod_load_trace, id_camda, contador

## En una línea

Tres secuencias generan los identificadores que hacen posible el rastreo, y `last_value` es la
expresión que aparece por todo el sistema para decir «lo de ahora mismo».

## Las tres

| Secuencia | Genera | Quién la avanza |
|---|---|---|
| `stg_s3.SEQ_COD_LOAD_TRACE` | `cod_load_trace` — una ejecución de carga | `RUN_LOAD_PLAN_PC` |
| `exp_s3.controlflag_arquivos_cod_id_seq` | `id_camda` — un lote de ficheros | El paso que abre el lote |
| `exp_s3.cod_seq_control_mapeio` | El identificador del lote de mapeos | `incio_carga_mapeo_megara` |

Y una por tabla para numerar filas: `des_sequence_table` del plan de carga alimenta la columna
`COD_SEQ_*`. Ver [D06_load_files_pc](../D%20-%20Carga%20STG/D06_load_files_pc.md).

## `last_value`: el patrón que verás por todas partes

```sql
SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq;
```

Esa expresión aparece literalmente en el script de flags, en la validación de cantidades y en
prácticamente cualquier consulta de control. Significa **«el lote actual»**.

Igual con los mapeos:

```sql
SELECT last_value FROM exp_s3.cod_seq_control_mapeio;
```

## ⚠ Tres cautelas con `last_value`

**Se mueve mientras investigas.** Si llega otro flag, `last_value` cambia y tus consultas pasan a
mirar otro lote. En una investigación larga, **fija el número al principio** y úsalo literal.

```sql
SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq;   -- p. ej. 30112
SELECT * FROM stg_s3.controlflag_interfaces WHERE id_camda = 30112;
```

**Un lote no es un día.** Cada llegada de flag abre lote. En un día con flags intradía, de fin de
día y de fin de semana hay **varios `id_camda` distintos**.

**En una réplica, `last_value` puede no estar sincronizado** con la sesión que consultas. Si los
números no cuadran con lo que ves en las tablas, comprueba contra qué instancia estás trabajando.

## Los tres identificadores no se relacionan entre sí

| Identificador | Ámbito | Se enlaza con… |
|---|---|---|
| `id_camda` | Un lote de ficheros recibidos | *nada, por columna* |
| `cod_load_trace` | Una carga de una tabla | *nada, por columna* |
| `id` de `control_mapeio_t` | Un lote de mapeos | *nada, por columna* |

**No hay ninguna columna que los una.** El puente entre capas es el nombre del fichero o el de la
tabla. Es la limitación de fondo de la trazabilidad del sistema.
Ver [I11_rastrear_un_fichero_e2e](../I%20-%20Referencia%20de%20datos/I11_rastrear_un_fichero_e2e.md).

## Consultas útiles

```sql
-- Estado de las tres
SELECT 'load_trace' AS seq, last_value FROM stg_s3.seq_cod_load_trace
UNION ALL SELECT 'id_camda',  last_value FROM exp_s3.controlflag_arquivos_cod_id_seq
UNION ALL SELECT 'mapeo',     last_value FROM exp_s3.cod_seq_control_mapeio;
```

```sql
-- Todas las secuencias del sistema
SELECT sequence_schema, sequence_name
FROM   information_schema.sequences
WHERE  sequence_schema IN ('stg_s3','trf_s3','exp_s3')
ORDER  BY 1,2;
```

## Ver también

[B08_id_camda_lote](../B%20-%20Recepcion%20y%20flags/B08_id_camda_lote.md) · [D05_run_load_plan_pc](../D%20-%20Carga%20STG/D05_run_load_plan_pc.md) · [G08_fim_carga_mapeo](../G%20-%20Mapeos/G08_fim_carga_mapeo.md) · [I18_columnas_comunes](../I%20-%20Referencia%20de%20datos/I18_columnas_comunes.md) · [I11_rastrear_un_fichero_e2e](../I%20-%20Referencia%20de%20datos/I11_rastrear_un_fichero_e2e.md)

---
titulo: "B08 — `id_camda`: el identificador de lote"
familia: B
etapa: "Recepción de flags"
tipo: Referencia
tags:
  - familia/B
  - etapa/recepcion-de-flags
  - tipo/referencia
keywords: "id_camda, camada, lote, secuencia, last_value, controlflag_arquivos_cod_id_seq"
---

# B08 — `id_camda`: el identificador de lote

**Etapa:** Recepción de flags
**Tipo:** Referencia
**Palabras clave:** id_camda, camada, lote, secuencia, last_value, controlflag_arquivos_cod_id_seq

## En una línea

`id_camda` agrupa todo lo que llegó en una misma tanda, y **todas las consultas de control usan
`last_value` de su secuencia para referirse al lote actual**.

## De dónde sale

```sql
SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq;
```

Esa expresión aparece literalmente en el script de flags, en la validación de cantidades recibidas y
en prácticamente cualquier consulta de control. Es la forma canónica de decir «el lote de ahora
mismo».

## Cómo usarlo

```sql
-- El lote actual
SELECT * FROM stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq);

-- El lote anterior, para comparar
SELECT * FROM stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value - 1 FROM exp_s3.controlflag_arquivos_cod_id_seq);
```

Comparar el lote actual con el anterior es el diagnóstico más rápido ante «hoy falta algo»:

```sql
SELECT nome_interface_base,
       count(*) FILTER (WHERE id_camda = (SELECT last_value     FROM exp_s3.controlflag_arquivos_cod_id_seq)) AS hoy,
       count(*) FILTER (WHERE id_camda = (SELECT last_value - 1 FROM exp_s3.controlflag_arquivos_cod_id_seq)) AS anterior
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda IN ((SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq),
                    (SELECT last_value - 1 FROM exp_s3.controlflag_arquivos_cod_id_seq))
GROUP  BY 1
HAVING count(*) FILTER (WHERE id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)) = 0
ORDER  BY 1;
```

Devuelve las interfaces que estaban en el lote anterior y **no** en el actual.

## ⚠ Tres trampas de `last_value`

**1. `last_value` es global y se mueve.** Si llega un flag nuevo mientras diagnosticas, `last_value`
cambia y tus consultas pasan a mirar otro lote. En una investigación larga, **fija el número al
principio** y úsalo literal:

```sql
SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq;   -- p. ej. 30112
-- y a partir de ahí:
SELECT * FROM stg_s3.controlflag_interfaces WHERE id_camda = 30112;
```

**2. Un lote no es un día.** Cada llegada de flag abre lote. En un día con flags intradía, de fin de
día y de fin de semana hay **varios `id_camda` distintos**. «El lote actual» es el último flag, no
la jornada.

**3. Si el paso que abre el lote falla, todo se escribe en el lote anterior.** El script de flags no
crea la fila de `controlflag_arquivos`: la actualiza. Si esa fila no existe porque
`LlamadaTablaControlArquivosFlag` falló, el `UPDATE` no afecta a nada, el script sigue, y las
interfaces se registran con el `id_camda` viejo. Síntoma: un lote con muchas más interfaces
declaradas de lo normal, mezclando dos llegadas.

```sql
-- Detecta lotes anormalmente grandes
SELECT id_camda, count(*) AS interfaces, min(nome_flag_geral) AS flag
FROM   stg_s3.controlflag_interfaces
GROUP  BY 1
ORDER  BY 1 DESC
LIMIT  15;
```

Un salto brusco en el conteo respecto a los lotes vecinos delata este problema.

## Relación con `cod_load_trace`

No se confundan: son dos identificadores de cosas distintas.

| Identificador | Ámbito | Nace en |
|---|---|---|
| `id_camda` | Un lote de ficheros recibidos | La secuencia de flags |
| `cod_load_trace` | Una ejecución de carga de **una** tabla | `RUN_LOAD_PLAN_PC` |

Un `id_camda` engloba muchos `cod_load_trace`. No hay columna que los relacione directamente: el
puente es el nombre del fichero.

## Ver también

[B07_tablas_controlflag](../B%20-%20Recepcion%20y%20flags/B07_tablas_controlflag.md) · [B05_job_manejo_flag](../B%20-%20Recepcion%20y%20flags/B05_job_manejo_flag.md) · [R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md) · [R4_10_consultas_que_falta](../R4%20-%20Sets%20incompletos/R4_10_consultas_que_falta.md) · [D05_run_load_plan_pc](../D%20-%20Carga%20STG/D05_run_load_plan_pc.md)

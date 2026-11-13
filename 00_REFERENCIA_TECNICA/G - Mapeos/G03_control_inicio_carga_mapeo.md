---
titulo: "G03 — `Control Inicio Carga Mapeo`"
familia: G
etapa: "Mapeos"
tipo: Referencia
tags:
  - familia/G
  - etapa/mapeos
  - tipo/referencia
keywords: "Control Inicio Carga Mapeo, incio_carga_mapeo_megara, arranque, puerta de entrada"
---

# G03 — `Control Inicio Carga Mapeo`

**Etapa:** Mapeos
**Tipo:** Referencia
**Palabras clave:** Control Inicio Carga Mapeo, incio_carga_mapeo_megara, arranque, puerta de entrada

## En una línea

Es la puerta de entrada al ciclo de mapeos: llama a `exp_s3.incio_carga_mapeo_megara`, que decide si
hay trabajo pendiente.

## El job

```sql
call exp_s3.incio_carga_mapeo_megara
```

Nótese la ortografía: **`incio`**, sin la primera «n». Está así en el nombre real del
procedimiento. Si lo buscas escrito correctamente no lo encuentras:

```sql
SELECT n.nspname, p.proname
FROM   pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  p.proname ILIKE '%carga_mapeo%';
```

## Qué hace

Marca el inicio del ciclo de mapeos y determina qué hay pendiente de procesar. Es la contraparte de
`fim_carga_mapeo_megara_ind`, que lo cierra. Ver [G08_fim_carga_mapeo](../G%20-%20Mapeos/G08_fim_carga_mapeo.md).

> **Nota de cobertura.** El cuerpo de este procedimiento no está en el material disponible: el
> volcado de `exp_s3` en el repositorio contiene únicamente la tabla de control. Lo anterior procede
> del job de Rundeck y del documento de arquitectura. Para ver qué hace realmente:
>
> ```sql
> SELECT prosrc FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
> WHERE  n.nspname = 'exp_s3' AND p.proname ILIKE '%incio_carga_mapeo%';
> ```

## Su sitio en la secuencia

```
Control Inicio Carga Mapeo          ← abre el ciclo
   ↓
Mapeos  /  MapeosFlag               ← despachan los mapeos en paralelo
   ↓
Job control errores mapeo           ← comprueba si hubo fallos
   ↓
Procedimiento control finalizacion mapeos   ← cierra
```

Si este primer paso falla, **no arranca ningún mapeo** y el síntoma aparece mucho más adelante: las
tablas de salida sin actualizar y Qlik con datos de ayer. El diagnóstico se va por el camino
equivocado si no se mira aquí primero.

## Qué comprobar cuando ningún mapeo ha corrido

No uno: **ninguno**. Ése es el patrón que apunta a este paso.

1. En Rundeck, si el job se ejecutó y con qué resultado.
2. Si el procedimiento existe y es invocable:

```sql
SELECT proname, pronargs
FROM   pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'exp_s3' AND p.proname ILIKE '%carga_mapeo%';
```

3. Si hay bloqueos que impidan al procedimiento avanzar:

```sql
SELECT pid, state, now() - query_start AS duracion, left(query,100)
FROM   pg_stat_activity
WHERE  query ILIKE '%carga_mapeo%' AND state <> 'idle';
```

4. Si el ciclo anterior se cerró. Un ciclo que no cerró puede impedir que el siguiente abra.
   Ver [R4_04_s3_interface_control](../R4%20-%20Sets%20incompletos/R4_04_s3_interface_control.md) y [H10_cierre_no_completado](../H%20-%20Cierre%20y%20Qlik/H10_cierre_no_completado.md).

## Ver también

[G04_jobs_mapeos](../G%20-%20Mapeos/G04_jobs_mapeos.md) · [G08_fim_carga_mapeo](../G%20-%20Mapeos/G08_fim_carga_mapeo.md) · [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md) · [G09_job_control_errores](../G%20-%20Mapeos/G09_job_control_errores.md)

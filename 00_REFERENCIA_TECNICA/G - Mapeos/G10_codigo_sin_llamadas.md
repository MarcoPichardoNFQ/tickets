---
titulo: "G10 — Código sin llamadas localizadas"
familia: G
etapa: "Mapeos"
tipo: Referencia
tags:
  - familia/G
  - etapa/mapeos
  - tipo/referencia
keywords: "código muerto, sin llamadas, tabla_control, auditoría Qlik, no asumir, huérfanas"
---

# G10 — Código sin llamadas localizadas

**Etapa:** Mapeos
**Tipo:** Referencia
**Palabras clave:** código muerto, sin llamadas, tabla_control, auditoría Qlik, no asumir, huérfanas

## En una línea

De las 22 funciones de `exp_s3` sólo **4 tienen llamador identificado**, y de las 152 funciones de
mapeo en `trf_s3` hay **33 que la tabla de control no declara**.

## Las funciones de mapeo huérfanas — 33 de 152

| | |
|---|---|
| Ficheros `trf_s3.function_meg_*` | 152 |
| Declaradas en `exp_s3.tablas_mapeio_t` | 122 |
| **Sin declarar: no las llama nadie** | **33** |
| Declaradas pero ausentes del volcado del repositorio | 3 |

Los nombres delatan su naturaleza: sufijos `_temporal`, `_intermedia`, `_cgc`, `_cc`, más series
numeradas (`rvcad_lote_2` … `_6`, `cadsubscricao_t1`, `t2`) y alguna suelta como `delete_fi`.
Trabajo intermedio y versiones antiguas que quedaron en la base.

**Ninguna se ejecuta**: el despacho sólo recorre lo que está en `tablas_mapeio_t`.
Ver [G08_fim_carga_mapeo](../G%20-%20Mapeos/G08_fim_carga_mapeo.md).

### ⚠ Cómo comprobarlo sin equivocarse

`nome_fn_mapeio` guarda los nombres en **mayúsculas mezcladas** (`function_MEG_CART_CAIXA_CPR_T18`),
mientras que `pg_proc.proname` los tiene en minúsculas. Una comparación directa **no casa ninguno** y
produce una lista falsa de referencias rotas.

```sql
-- Funciones de mapeo que existen en la base pero nadie declara
SELECT p.proname
FROM   pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'trf_s3' AND p.proname LIKE 'function\_meg\_%'
  AND  NOT EXISTS (SELECT 1 FROM exp_s3.tablas_mapeio_t t
                   WHERE lower(t.nome_fn_mapeio) = lower(p.proname))
ORDER  BY 1;

-- Y la inversa: declaradas cuya función no existe (éstas sí fallarían siempre)
SELECT t.id_mapeo, t.nome_tabela_aldrin, t.nome_fn_mapeio
FROM   exp_s3.tablas_mapeio_t t
WHERE  t.activo_inactivo
  AND  NOT EXISTS (SELECT 1 FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
                   WHERE n.nspname = 'trf_s3'
                     AND lower(p.proname) = lower(t.nome_fn_mapeio));
```

El `lower()` en ambos lados no es opcional. Ver [J10_trampas_conocidas](../J%20-%20Operacion/J10_trampas_conocidas.md).

El despacho real tolera la inconsistencia por accidente: construye
`SELECT trf_s3.<nombre>()` **sin comillas**, y PostgreSQL pliega el identificador a minúsculas al
ejecutarlo. Funciona, pero cualquier diagnóstico que compare nombres a mano tiene que replicarlo.

## Las funciones de `exp_s3`

## Las que sí están vivas

| Función | La llama |
|---|---|
| `incio_carga_mapeo_megara` | Job `Control Inicio Carga Mapeo` |
| `fim_carga_mapeo_megara_ind` | Los jobs individuales de mapeo |
| `actualizar_tablas_y_control` | Job `Procedimiento control finalizacion mapeos` |
| `actualizar_tablas_y_controlflag` | Variante Flag del anterior |

## Las que no tienen llamador localizado

**No están confirmadas como muertas.** Significa que no las llama nada de lo que puedo ver: los 46
jobs de Rundeck exportados, los scripts de `/nfq/data/cfg/`, los 501 procedimientos de `stg_s3` y
`trf_s3`, ni la app de Qlik disponible.

### Grupo A — parecen una API de auditoría para Qlik

```
inicio(name_app, name_table_main, name_table_delete, name_qvd, app_id, app_url,
       max_qlik_update, time_start, time_finish, time_total, m_load_trace,
       completed, load_type, no_of_records)
fin(app_id, max_qlik_update, time_start, time_finish, time_total,
    m_load_trace, completed, no_of_records)
principio(nom_table, nom_qvd, id_qvd, url, max_qlik_update, inicio)
completar / completarr  (dos sobrecargas cada una)
borrar / borrarr
insert_temp()
handle_error(p_sqlstate, p_sqlerrm, p_function_name)
```

Escriben en `exp_s3.tabla_control`. Los parámetros —nombre de app, URL de app, nombre de QVD,
tiempos de inicio y fin, número de registros— **sólo tienen sentido llamados desde un script de
carga de Qlik**.

La app de Qlik disponible (`Recarga desde Qlik`) sólo usa `exp_s3.relaciontablacolumnas` y **no las
invoca**. Así que o las llama otra app de Qlik que no tenemos, o son el resto de una instrumentación
retirada.

### Grupo B — flujo de caja proyectado

```
fluxo_caixa_projectado
fluxo_caixa_projectado_170
fluxo_caixa_projectado_borrar
fluxo_caixa_projectado_borrar_parcial
```

El nombre coincide con la tarea `LOAD_QVD_FLUXOCAIXA` del catálogo `lookup_qlik.txt`, lo que apunta
otra vez a una app de Qlik como llamador.

### Grupo C — variantes del cierre de mapeos

```
fim_carga_mapeo_megara
fim_carga_mapeo_megara_indflag
```

Hermanas de la que sí está viva. La segunda parece la variante para el flujo Flag.

### Grupo D — actualización de marcas de Qlik

```
actualizacao_icqlikread_extracao_carga_primera
actualizacao_icqlikread_extracao_carga_segunda
```

Ambas hacen un `UPDATE trf_s3.s3_fundo_extracao_carga SET ic_qlik_read = '0' WHERE ic_qlik_read IS NULL`.

### Grupo E — nombres duplicados

`borrar` / `borrarr`, `completar` / `completarr`. La duplicación con una letra de más es el patrón
clásico de «copié la función para probar algo y me quedé con las dos». Sospechosas, pero sin
confirmar.

## Qué hacer con esto en soporte

**No documentes su funcionamiento como si estuvieran activas.** Si una incidencia parece apuntar a
una de ellas, la primera pregunta es si algo la llama de verdad.

**Comprobación en tu entorno**, que es la que zanja el asunto:

```sql
-- ¿Se ha ejecutado alguna vez? Requiere pg_stat_statements
SELECT calls, total_exec_time, query
FROM   pg_stat_statements
WHERE  query ILIKE '%exp_s3.fluxo_caixa_projectado%'
    OR query ILIKE '%exp_s3.inicio(%'
    OR query ILIKE '%exp_s3.principio(%';
```

```sql
-- ¿Tiene datos recientes la tabla que alimentan?
SELECT count(*), max(fin) FROM exp_s3.tabla_control;
```

Una `tabla_control` sin filas recientes es un indicio fuerte de que esa API ya no se usa.

Y en Qlik: revisar si alguna otra app llama a estas funciones en su script de carga.

## Por qué importa

Este sistema ya ha acumulado varias piezas que existen, parecen operativas y no hacen nada:
la validación de duplicados, la de variación de volumen, `megara_reprocess`, el catálogo
`lookup_qlik.txt` y el job de análisis de errores. Ver [J10_trampas_conocidas](../J%20-%20Operacion/J10_trampas_conocidas.md).

La regla que se deduce: **en este sistema, que una función exista no prueba que se ejecute.**
Antes de basar un diagnóstico en ella, comprueba quién la llama.

## Ver también

[G08_fim_carga_mapeo](../G%20-%20Mapeos/G08_fim_carga_mapeo.md) · [J10_trampas_conocidas](../J%20-%20Operacion/J10_trampas_conocidas.md) · [R5_08_analise_de_erros_anulado](../R5%20-%20Alertas%20Rundeck/R5_08_analise_de_erros_anulado.md) · [R1_07_descarte_variacion_volumen](../R1%20-%20Descartes/R1_07_descarte_variacion_volumen.md) · [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md)

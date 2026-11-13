---
titulo: "G08 — El despacho real: `incio_carga_mapeo_megara` y `fim_carga_mapeo_megara_ind`"
familia: G
etapa: "Mapeos"
tipo: Referencia
tags:
  - familia/G
  - etapa/mapeos
  - tipo/referencia
keywords: "despacho, control_mapeio_t, control_carga, is_fromtis, cod_seq_control_mapeio, contador"
---

# G08 — El despacho real: `incio_carga_mapeo_megara` y `fim_carga_mapeo_megara_ind`

**Etapa:** Mapeos
**Tipo:** Referencia
**Palabras clave:** despacho, control_mapeio_t, control_carga, is_fromtis, cod_seq_control_mapeio, contador

## En una línea

El ciclo abre un lote en `exp_s3.control_mapeio_t` con un contador por tabla, y cada mapeo que
termina bien lo decrementa; ese contador es lo que decide si un mapeo se ejecuta o se salta.

## Paso 1 — `incio_carga_mapeo_megara` abre el lote

```sql
V_OUT_SEQ_CONTROL := NEXTVAL('exp_s3.cod_seq_control_mapeio');

INSERT INTO exp_s3.control_mapeio_t (tabela_carga, data_ini_upload, control_carga)
(SELECT DISTINCT ON (nome_tabela_aldrin) nome_tabela_aldrin, now(), count(nome_tabela_aldrin)
 FROM   exp_s3.tablas_mapeio_t
 WHERE  is_fromtis = 'N'
 GROUP  BY nome_tabela_aldrin);

UPDATE exp_s3.control_mapeio_t SET id = V_OUT_SEQ_CONTROL WHERE id IS NULL;
```

Una fila por **tabla de destino**, con `control_carga` = **cuántas funciones tiene esa tabla**. Es
un contador descendente.

Fíjate en el filtro: **`is_fromtis = 'N'` y nada más**. No filtra por `activo_inactivo`, así que
`control_mapeio_t` incluye también filas de mapeos desactivados. Es inofensivo, pero explica que el
conteo de filas no coincida con el de mapeos activos.

## Paso 2 — `fim_carga_mapeo_megara_ind(po_outcode, id_mapeo)` ejecuta

```sql
SELECT last_value INTO v_id FROM exp_s3.cod_seq_control_mapeio;

OPEN C_MAPEIO_CUR FOR
SELECT nome_tabela_aldrin, nome_fn_mapeio, retry_deadlock, wait_deadlock_seconds
FROM   exp_s3.tablas_mapeio_t
WHERE  is_fromtis = 'N' AND activo_inactivo = TRUE AND id_mapeo = v_id_mapeo;
```

Aquí sí se exigen **las dos condiciones**: `is_fromtis = 'N'` **y** `activo_inactivo = TRUE`.

Y por cada función, antes de ejecutarla, consulta el contador:

```sql
SELECT control_carga INTO v_count_mapeo
FROM   exp_s3.control_mapeio_t
WHERE  tabela_carga = v_nome_tabela_aldrin AND id = v_id;

IF v_count_mapeo > 0 THEN ... END IF;
```

## Las funciones de mapeo viven en `trf_s3`

```sql
v_mapeo := 'SELECT trf_s3.' || v_nome_fn_mapeio || '();';
EXECUTE v_mapeo;
```

**No están en `exp_s3`.** `exp_s3` sólo aloja el control. Para leer la lógica de un mapeo concreto:

```sql
SELECT prosrc FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'trf_s3' AND p.proname = '<nome_fn_mapeio>';
```

## Los tres desenlaces de una ejecución

| SQLSTATE | Rama | Qué hace |
|---|---|---|
| `40P01` | Deadlock | Registra el intento, `pg_sleep(wait_deadlock_seconds)` y **reintenta** |
| `21000` | Etiquetado «Duplicate error» | Registra y **sale sin reintentar** |
| Cualquier otro | No controlado | Registra y **sale sin reintentar** |

Los tres escriben en `trf_s3.s3_control_errores_mapeo (des_func, des_sqlerrm, cod_sqlstate)`.

**Ojo con la etiqueta de `21000`.** El comentario del código dice «Duplicate error», pero `21000`
es `cardinality_violation` — «más de una fila devuelta por una subconsulta usada como expresión».
No es una clave duplicada, que sería `23505`. Si ves ese código, el problema es una subconsulta del
mapeo que devuelve más filas de las que espera, no un duplicado de datos.

## El cierre de cada función

```sql
IF v_attempt >= v_retries THEN
    -- registra 'Se agotaron los intentos por deadlock'
ELSE
    UPDATE exp_s3.control_mapeio_t
    SET    control_carga = control_carga - 1, data_fim_upload = NOW()
    WHERE  tabela_carga = v_nome_tabela_aldrin AND control_carga <> 0 AND id = v_id;
END IF;
```

El contador baja uno por cada función completada. Cuando llega a `0`, la tabla está terminada.

## Dos consecuencias operativas importantes

### Relanzar un mapeo ya completado no hace nada

La condición de entrada es `IF v_count_mapeo > 0`. Si el contador de esa tabla ya llegó a `0` en
este lote, **la función no se ejecuta** y el job sale en verde sin trabajar.

```sql
SELECT tabela_carga, control_carga, data_ini_upload, data_fim_upload
FROM   exp_s3.control_mapeio_t
WHERE  id = (SELECT last_value FROM exp_s3.cod_seq_control_mapeio)
ORDER  BY control_carga DESC;
```

`control_carga = 0` significa completada. Para reejecutarla de verdad hay que abrir lote nuevo, no
relanzar el job. Ver [R3_11_relanzar_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_11_relanzar_mapeo.md).

### Si el arranque no corrió, todos los mapeos se saltan en silencio

Si `incio_carga_mapeo_megara` no se ejecutó, no hay fila en `control_mapeio_t` para el `id` actual.
Entonces `v_count_mapeo` queda NULL, `IF NULL > 0` no es cierto, y **cada mapeo se salta sin
ejecutarse y sin registrar error**.

Síntoma: ninguna tabla de salida se actualiza, ningún job falla, la tabla de errores vacía. Es el
escenario de [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md) en su versión más silenciosa.

```sql
-- ¿Se abrió lote hoy?
SELECT id, count(*) AS tablas, min(data_ini_upload) AS abierto
FROM   exp_s3.control_mapeio_t
GROUP  BY id ORDER BY id DESC LIMIT 5;
```

## Las variantes que existen

| Función | Estado |
|---|---|
| `incio_carga_mapeo_megara` | **Viva** — la llama `Control Inicio Carga Mapeo` |
| `fim_carga_mapeo_megara_ind` | **Viva** — es la que despacha, por `id_mapeo` |
| `fim_carga_mapeo_megara` | Sin llamadas localizadas |
| `fim_carga_mapeo_megara_indflag` | Sin llamadas localizadas — probablemente la variante Flag |

Las dos últimas no aparecen invocadas desde ningún job, script ni procedimiento del material
disponible. Antes de asumir que están en uso, compruébalo. Ver [G10_codigo_sin_llamadas](../G%20-%20Mapeos/G10_codigo_sin_llamadas.md).

## Ver también

[G03_control_inicio_carga_mapeo](../G%20-%20Mapeos/G03_control_inicio_carga_mapeo.md) · [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md) · [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md) · [R3_11_relanzar_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_11_relanzar_mapeo.md) · [G09_job_control_errores](../G%20-%20Mapeos/G09_job_control_errores.md) · [G02_tablas_mapeio_activo](../G%20-%20Mapeos/G02_tablas_mapeio_activo.md)

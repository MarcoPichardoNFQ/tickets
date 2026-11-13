---
titulo: "R3.03 — Deadlock `40P01` y el reintento"
familia: R3
etapa: "Mapeos"
tipo: Runbook
tags:
  - familia/R3
  - etapa/mapeos
  - tipo/runbook
keywords: "deadlock, 40P01, pg_sleep, retry_deadlock, bloqueo mutuo, reintento, paralelo"
---

# R3.03 — Deadlock `40P01` y el reintento

**Etapa:** Mapeos
**Tipo:** Runbook
**Palabras clave:** deadlock, 40P01, pg_sleep, retry_deadlock, bloqueo mutuo, reintento, paralelo

## En una línea

Los bloqueos mutuos entre mapeos son **esperables** por el paralelismo, y el sistema los reintenta
solo; sólo importan cuando el reintento se agota.

## Qué es

`40P01` es el código SQLSTATE de PostgreSQL para `deadlock_detected`: dos transacciones se esperan
mutuamente y el motor mata a una para desbloquear.

Los mapeos corren decenas a la vez sobre las mismas tablas de `trf_s3`. Que se pisen es una
consecuencia del diseño, no una anomalía.

## El reintento

El procedimiento captura la excepción, espera con `pg_sleep()` y vuelve a intentarlo. Y —esto es lo
importante— **los parámetros son por mapeo**, en la tabla de control:

```sql
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio,
       retry_deadlock         AS reintentos,
       wait_deadlock_seconds  AS espera_seg
FROM   exp_s3.tablas_mapeio_t
WHERE  activo_inactivo
ORDER  BY retry_deadlock DESC NULLS LAST;
```

| Valor | Comportamiento |
|---|---|
| `retry_deadlock` alto | Mapeo sobre tablas muy disputadas: aguanta varios choques |
| `retry_deadlock = 1` | Un solo intento; al primer bloqueo, falla |
| **`retry_deadlock` NULL** | **⚠ El mapeo NO SE EJECUTA NUNCA — y se marca como completado** |

## ⚠ El caso `retry_deadlock` NULL

El despacho hace esto:

```sql
v_retries INT := 1;
FETCH C_MAPEIO_CUR INTO v_nome_tabela_aldrin, v_nome_fn_mapeio, v_retries, v_wait_deadlock;
WHILE v_attempt < v_retries LOOP
    EXECUTE 'SELECT trf_s3.' || v_nome_fn_mapeio || '();';
    ...
END LOOP;

IF v_attempt >= v_retries THEN
    -- registra "Se agotaron los intentos"
ELSE
    UPDATE exp_s3.control_mapeio_t SET control_carga = control_carga - 1, data_fim_upload = NOW() ...
END IF;
```

Si `retry_deadlock` es NULL, `v_retries` pasa a NULL y ocurren **dos cosas encadenadas**:

1. `WHILE 0 < NULL` evalúa a NULL, que no es cierto → **el bucle no se ejecuta ni una vez**. La
   función de mapeo nunca se invoca.
2. `IF 0 >= NULL` también evalúa a NULL, que no es cierto → se va por el `ELSE` → **decrementa
   `control_carga` y sella `data_fim_upload` como si hubiera terminado con éxito**.

Resultado: la tabla de destino no se actualiza, no se registra ningún error, y el control queda
marcado como completado. **Silencioso en las tres vías.**

Ésta es la primera comprobación ante «este mapeo no actualiza nada y no da error»:

```sql
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio, retry_deadlock, wait_deadlock_seconds
FROM   exp_s3.tablas_mapeio_t
WHERE  activo_inactivo AND is_fromtis = 'N' AND retry_deadlock IS NULL
ORDER  BY id_mapeo;
```

Todo lo que devuelva esa consulta son mapeos que **no se están ejecutando**.

## Cuándo es incidencia y cuándo no

| Situación | ¿Incidencia? |
|---|---|
| Deadlock registrado, el mapeo terminó bien tras reintentar | **No.** Funcionamiento normal |
| Deadlock y el mapeo falló tras agotar reintentos | **Sí** |
| Deadlocks masivos en muchos mapeos a la vez | **Sí**, y apunta a un solape estructural |
| Deadlock en un mapeo sin reintentos configurados | Configuración, no fallo |

La primera fila explica por qué la tabla de errores puede tener registros sin que nada esté mal.
**La presencia de un `40P01` no prueba un fallo**: hay que comprobar si el mapeo acabó.

## Diagnóstico

```sql
-- Errores de mapeo de hoy
SELECT * FROM trf_s3.s3_control_errores_mapeo
WHERE  dat_proc_exe::date = CURRENT_DATE
ORDER  BY dat_proc_exe DESC;
```

```sql
-- ¿Se pobló la tabla destino a pesar del deadlock?
SELECT count(*) FROM trf_s3.<TABLA_DESTINO>;
```

Datos actualizados = el reintento funcionó, cierra el ticket.

### En caliente, mientras ocurre

```sql
SELECT bloqueada.pid  AS pid_bloqueado,
       bloqueante.pid AS pid_bloqueante,
       now() - bloqueada.query_start AS esperando,
       left(bloqueada.query, 80)  AS consulta_bloqueada,
       left(bloqueante.query, 80) AS consulta_bloqueante
FROM   pg_stat_activity bloqueada
JOIN   LATERAL unnest(pg_blocking_pids(bloqueada.pid)) AS b(pid) ON true
JOIN   pg_stat_activity bloqueante ON bloqueante.pid = b.pid
ORDER  BY esperando DESC;
```

### Deadlocks acumulados en el motor

```sql
SELECT datname, deadlocks FROM pg_stat_database WHERE datname = current_database();
```

Un crecimiento brusco de ese contador confirma que hay un problema de concurrencia y no un fallo
puntual.

## Acción

1. **Comprueba si el mapeo acabó** a pesar del deadlock. Si acabó, no hay nada que hacer.
2. Si falló, **relanza sólo ese mapeo** desde su job individual. Con menos concurrencia suele
   pasar a la primera. Ver [R3_11_relanzar_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_11_relanzar_mapeo.md).
3. Si falla repetidamente, mira su configuración de reintentos.
4. Si hay deadlocks masivos, el problema es de solape: demasiados mapeos tocando lo mismo a la vez.
   Eso no se arregla relanzando.

## Lo que no hay que hacer

**No matar sesiones a la primera.** PostgreSQL ya resuelve el deadlock por su cuenta matando a una
de las dos: intervenir sólo añade ruido.

**No relanzar el orquestador completo** para recuperar un mapeo. Reejecuta decenas de mapeos y
aumenta la concurrencia justo cuando el problema es la concurrencia.

## Cuándo escalar

- Deadlocks masivos y recurrentes: es un problema de diseño de la concurrencia.
- Un mapeo que falla por deadlock todos los días: hay que ajustar sus reintentos o su orden de
  ejecución, y eso es un cambio de configuración con impacto.

## Ver también

[R3_06_mapeo_bloqueado](../R3%20-%20Errores%20de%20mapeo/R3_06_mapeo_bloqueado.md) · [G02_tablas_mapeio_activo](../G%20-%20Mapeos/G02_tablas_mapeio_activo.md) · [R3_11_relanzar_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_11_relanzar_mapeo.md) · [G09_job_control_errores](../G%20-%20Mapeos/G09_job_control_errores.md) · [D12_carga_colgada](../D%20-%20Carga%20STG/D12_carga_colgada.md)

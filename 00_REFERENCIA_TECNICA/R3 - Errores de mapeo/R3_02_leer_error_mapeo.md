---
titulo: "R3.02 — Leer el error registrado de un mapeo"
familia: R3
etapa: "Mapeos"
tipo: Runbook
tags:
  - familia/R3
  - etapa/mapeos
  - tipo/runbook
keywords: "s3_control_errores_mapeo, des_sqlerrm, cod_sqlstate, interpretar error"
---

# R3.02 — Leer el error registrado de un mapeo

**Etapa:** Mapeos
**Tipo:** Runbook
**Palabras clave:** s3_control_errores_mapeo, des_sqlerrm, cod_sqlstate, interpretar error

## Síntoma

Hay filas en `trf_s3.s3_control_errores_mapeo` y hay que entender qué dicen.

## La consulta

```sql
SELECT e.dat_proc_exe, e.cod_sqlstate, e.des_func, e.des_sqlerrm,
       t.id_mapeo, t.nome_tabela_aldrin
FROM   trf_s3.s3_control_errores_mapeo e
LEFT   JOIN exp_s3.tablas_mapeio_t t ON lower(t.nome_fn_mapeio) = lower(e.des_func)
WHERE  e.dat_proc_exe::date = CURRENT_DATE
ORDER  BY e.dat_proc_exe DESC;
```

El `lower()` en el `JOIN` es obligatorio: la tabla de control guarda los nombres en mayúsculas
mezcladas. Ver [J10_trampas_conocidas](../J%20-%20Operacion/J10_trampas_conocidas.md).

## Interpretar `cod_sqlstate`

| Código | Qué es de verdad | ¿Reintentó? |
|---|---|---|
| `40P01` | `deadlock_detected` | **Sí**, con `pg_sleep` |
| `21000` | `cardinality_violation` — una subconsulta devolvió más de una fila | No |
| `23505` | Violación de clave única | No |
| `22P02` | Formato de dato inválido | No |
| `42P01` | La tabla o función no existe | No |
| Otros | Error no controlado | No |

**⚠ `21000` está mal etiquetado en el código como «Duplicate error».** No es una clave duplicada
—eso sería `23505`—: es una subconsulta del mapeo que devuelve más filas de las que espera. Buscar
un duplicado de datos ante ese código lleva por el camino equivocado.

## Interpretar `des_sqlerrm`

| Mensaje | Significa |
|---|---|
| `Se agotaron los intentos por deadlock` | El reintento llegó a su límite. **El mapeo no completó** |
| Texto que empieza por un número | Es el número de intento: `2 deadlock detected...` |
| Mensaje de PostgreSQL | La causa real, tal cual |

Un registro de `40P01` **no prueba un fallo**: puede ser un intento que después salió bien. Lo que
confirma el fallo es el mensaje «Se agotaron los intentos».

## La comprobación decisiva: ¿acabó o no?

```sql
-- ¿Se pobló la tabla destino?
SELECT count(*), max(dat_qlikupdate) FROM trf_s3.<TABLA_DESTINO>;

-- ¿El contador bajó?
SELECT tabela_carga, control_carga, data_ini_upload, data_fim_upload
FROM   exp_s3.control_mapeio_t
WHERE  id = (SELECT last_value FROM exp_s3.cod_seq_control_mapeio)
  AND  lower(tabela_carga) = lower('<TABLA>');
```

`control_carga = 0` y `data_fim_upload` informada = la tabla terminó, aunque hubiera errores por el
camino. Ver [G08_fim_carga_mapeo](../G%20-%20Mapeos/G08_fim_carga_mapeo.md).

## Lo que la tabla NO te dice

**No tiene `id_mapeo`.** El enlace es por `des_func`, con `lower()`.

**No registra los saltos silenciosos.** Un mapeo con `retry_deadlock` NULL no se ejecuta y **no deja
ninguna fila aquí**. Ver [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md).

**No registra que un mapeo no fuera llamado.** Un mapeo huérfano —ausente de la lista del
orquestador— tampoco aparece. Ver [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md).

Es decir: **la ausencia de error no prueba que el mapeo corriera**.

## El job que la vigila

`Job control errores mapeo` consulta esta tabla filtrando por los **últimos 30 minutos**. Un error
de hace 40 minutos no dispara alerta. Para saber si hubo errores hoy, filtra por día, no confíes en
el job. Ver [G09_job_control_errores](../G%20-%20Mapeos/G09_job_control_errores.md).

## Ver también

[G09_job_control_errores](../G%20-%20Mapeos/G09_job_control_errores.md) · [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md) · [R3_01_anatomia_fallo_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_01_anatomia_fallo_mapeo.md) · [G08_fim_carga_mapeo](../G%20-%20Mapeos/G08_fim_carga_mapeo.md) · [R3_12_consultas_mapeos](../R3%20-%20Errores%20de%20mapeo/R3_12_consultas_mapeos.md)

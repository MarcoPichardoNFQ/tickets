---
titulo: "R3.09 — El contador `control_carga` no llegó a cero"
familia: R3
etapa: "Mapeos"
tipo: Runbook
tags:
  - familia/R3
  - etapa/mapeos
  - tipo/runbook
keywords: "control_carga, contador, a medias, control_mapeio_t, data_fim_upload"
---

# R3.09 — El contador `control_carga` no llegó a cero

**Etapa:** Mapeos
**Tipo:** Runbook
**Palabras clave:** control_carga, contador, a medias, control_mapeio_t, data_fim_upload

## Síntoma

El ciclo terminó, pero el contador de una tabla sigue por encima de cero: **alguna de sus funciones
no completó**.

## La consulta

```sql
SELECT tabela_carga, control_carga, data_ini_upload, data_fim_upload
FROM   exp_s3.control_mapeio_t
WHERE  id = (SELECT last_value FROM exp_s3.cod_seq_control_mapeio)
ORDER  BY control_carga DESC;
```

| `control_carga` | Significa |
|---|---|
| `0` | Todas las funciones de esa tabla completaron |
| `> 0` | **Quedan tantas funciones sin completar** |
| Sin fila | El lote no se abrió para esa tabla |

## Cómo funciona el contador

`incio_carga_mapeo_megara` lo inicializa con **el número de funciones de esa tabla**, y cada
función que termina bien lo decrementa:

```sql
UPDATE exp_s3.control_mapeio_t
SET    control_carga = control_carga - 1, data_fim_upload = NOW()
WHERE  tabela_carga = ... AND control_carga <> 0 AND id = v_id;
```

Ver [G08_fim_carga_mapeo](../G%20-%20Mapeos/G08_fim_carga_mapeo.md) y [G11_mapeos_multifuncion](../G%20-%20Mapeos/G11_mapeos_multifuncion.md).

## Las cuatro causas

### 1. Una función falló y agotó sus reintentos

```sql
SELECT dat_proc_exe, des_func, cod_sqlstate, des_sqlerrm
FROM   trf_s3.s3_control_errores_mapeo
WHERE  dat_proc_exe::date = CURRENT_DATE
  AND  des_sqlerrm ILIKE '%agotaron%';
```

Ver [R3_02_leer_error_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_02_leer_error_mapeo.md).

### 2. Una función quedó bloqueada y nunca terminó

No deja error registrado. Ver [R3_06_mapeo_bloqueado](../R3%20-%20Errores%20de%20mapeo/R3_06_mapeo_bloqueado.md).

### 3. El ciclo se interrumpió

Rundeck se detuvo, o alguien canceló el job, a mitad del recorrido.

### 4. Una función está desactivada

Si `incio` contó las funciones **sin filtrar por `activo_inactivo`** pero el despacho **sí filtra**,
las funciones apagadas se cuentan al inicializar y nunca se decrementan.

```sql
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio, activo_inactivo
FROM   exp_s3.tablas_mapeio_t
WHERE  lower(nome_tabela_aldrin) = lower('<TABLA>')
ORDER  BY nome_fn_mapeio;
```

Si hay funciones con `activo_inactivo = false`, **el contador nunca podrá llegar a cero** para esa
tabla — y eso es estructural, no una incidencia del día. Ver [G11_mapeos_multifuncion](../G%20-%20Mapeos/G11_mapeos_multifuncion.md).

Comprueba si es recurrente antes de investigar:

```sql
SELECT id, tabela_carga, control_carga
FROM   exp_s3.control_mapeio_t
WHERE  lower(tabela_carga) = lower('<TABLA>')
ORDER  BY id DESC LIMIT 10;
```

El mismo valor residual en todos los lotes = causa 4, estructural. Un valor distinto de lo habitual
sólo hoy = causas 1, 2 o 3.

## ⚠ Y el caso inverso: contador a cero sin haber trabajado

Más peligroso, porque parece correcto. Una función con `retry_deadlock` NULL **no se ejecuta y aun
así decrementa el contador**: el bucle `WHILE 0 < NULL` no entra, y el `IF 0 >= NULL` tampoco es
cierto, así que se va por la rama de éxito.

```sql
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio
FROM   exp_s3.tablas_mapeio_t
WHERE  activo_inactivo AND is_fromtis = 'N' AND retry_deadlock IS NULL;
```

**Un contador a cero no prueba que la tabla se poblara.** Contrasta siempre con el dato:

```sql
SELECT count(*), max(dat_qlikupdate) FROM trf_s3.<TABLA>;
```

Ver [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md).

## Acción

1. Identifica la causa con la tabla de arriba.
2. Si fue fallo o bloqueo, resuélvelo y **relanza el job individual**.
3. Ten en cuenta que **si el contador ya llegó a cero, relanzar no hace nada**. En ese caso hay que
   abrir lote nuevo, no relanzar. Ver [R3_11_relanzar_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_11_relanzar_mapeo.md).
4. Verifica el dato, no el contador.

## Cuándo escalar

- Si el residuo es estructural (funciones desactivadas): es una decisión funcional, no un fallo.
- Si hay que abrir lote nuevo fuera del ciclo normal.

## Ver también

[G08_fim_carga_mapeo](../G%20-%20Mapeos/G08_fim_carga_mapeo.md) · [G11_mapeos_multifuncion](../G%20-%20Mapeos/G11_mapeos_multifuncion.md) · [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md) · [R3_11_relanzar_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_11_relanzar_mapeo.md) · [R3_02_leer_error_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_02_leer_error_mapeo.md)

---
titulo: "G01 — Qué es un mapeo y a dónde escribe"
familia: G
etapa: "Mapeos"
tipo: Referencia
tags:
  - familia/G
  - etapa/mapeos
  - tipo/referencia
keywords: "mapeo, exp_s3, id_mapeo, tabla aldrin, salida, consolidación"
---

# G01 — Qué es un mapeo y a dónde escribe

**Etapa:** Mapeos
**Tipo:** Referencia
**Palabras clave:** mapeo, exp_s3, id_mapeo, tabla aldrin, salida, consolidación

## En una línea

Un mapeo es una función de base de datos que lee el modelo de negocio de `trf_s3` y escribe una
tabla de salida consolidada, lista para que la consuma Qlik.

## Detalle

### El sitio que ocupa en la cadena

```
trf_s3 (modelo de negocio)
   ↓  mapeo: una función SQL por tabla de salida
trf_s3 → tabla de salida del mapeo (sac_*, cart_*)
   ↓  recarga
Qlik
```

Es la última transformación antes de que el dato salga del sistema. A diferencia de las etapas
anteriores —que son genéricas y parametrizadas— **cada mapeo es una consulta escrita a medida** para
su tabla destino.

### Cómo se identifican

Cada mapeo tiene un `id_mapeo` numérico y un nombre de función. Los jobs de Rundeck los nombran
combinando ambos:

```
14 mapeo_cart_pos_rf_t
35 mapeo_sac_pl_cl_patrrf_t
111 mapeo_cart_estat_clibas_t
```

Los identificadores **no son correlativos**: hay huecos, porque algunos mapeos se retiraron con el
tiempo. Un id que no existe no es un error.

### La tabla de control

Todo lo que gobierna los mapeos está en `exp_s3.tablas_mapeio_t`:

| Columna | Contenido |
|---|---|
| `nome_tabela_aldrin` | Tabla de salida |
| `nome_fn_mapeio` | Función que la construye |
| `is_fromtis` | Marca de origen |
| `id_mapeo` | Identificador numérico |
| **`activo_inactivo`** | **`true` = el mapeo corre; `false` = no** |
| `retry_deadlock` | Nº de reintentos ante bloqueo mutuo |
| `wait_deadlock_seconds` | Segundos de espera entre reintentos |

Clave primaria: `(nome_tabela_aldrin, nome_fn_mapeio)`.

Que la clave sea compuesta tiene una consecuencia importante: **un mismo `id_mapeo` puede tener
varias funciones**. Una tabla de salida se construye a veces en varias fases, cada una con su
función. Al diagnosticar «el mapeo 38 falló», conviene mirar cuántas funciones tiene:

```sql
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio, activo_inactivo
FROM   exp_s3.tablas_mapeio_t
WHERE  id_mapeo = :id
ORDER  BY nome_fn_mapeio;
```

### Lo que distingue a esta capa

**No hay parametrización genérica.** No existen `PAR_*` para los mapeos: la lógica está en el SQL de
cada función.

**No hay tablas `_DES` ni `_ERR`.** El mecanismo de descartes de staging no aplica aquí.
Ver [R1_08_descartes_en_mapeos](../R1%20-%20Descartes/R1_08_descartes_en_mapeos.md).

**Se ejecutan en paralelo masivo.** Decenas de mapeos a la vez, lo que hace de los bloqueos mutuos
un fenómeno esperado y no una anomalía. Por eso existen las dos columnas de reintento.
Ver [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md).

**El control de errores es una tabla propia**: `trf_s3.s3_control_errores_mapeo`.
Ver [G09_job_control_errores](../G%20-%20Mapeos/G09_job_control_errores.md).

## Cómo verificarlo

```sql
-- Catálogo de mapeos activos
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio,
       retry_deadlock, wait_deadlock_seconds
FROM   exp_s3.tablas_mapeio_t
WHERE  activo_inactivo
ORDER  BY id_mapeo;

-- Cuántos activos e inactivos
SELECT activo_inactivo, count(*) FROM exp_s3.tablas_mapeio_t GROUP BY 1;
```

## Ver también

[G02_tablas_mapeio_activo](../G%20-%20Mapeos/G02_tablas_mapeio_activo.md) · [G04_jobs_mapeos](../G%20-%20Mapeos/G04_jobs_mapeos.md) · [R3_01_anatomia_fallo_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_01_anatomia_fallo_mapeo.md) · [R1_08_descartes_en_mapeos](../R1%20-%20Descartes/R1_08_descartes_en_mapeos.md)

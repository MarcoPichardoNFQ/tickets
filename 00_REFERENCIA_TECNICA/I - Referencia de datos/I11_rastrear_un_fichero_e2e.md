---
titulo: "I11 — Rastrear un fichero desde la llegada hasta Qlik"
familia: I
etapa: "Transversal"
tipo: Runbook
tags:
  - familia/I
  - etapa/transversal
  - tipo/runbook
keywords: "rastreo, seguimiento, extremo a extremo, dónde está mi dato, trazabilidad"
---

# I11 — Rastrear un fichero desde la llegada hasta Qlik

**Etapa:** Transversal
**Tipo:** Runbook
**Palabras clave:** rastreo, seguimiento, extremo a extremo, dónde está mi dato, trazabilidad

## En una línea

Siete comprobaciones siguen a un fichero por todo el sistema; la que falle marca la etapa donde se
quedó.

## El problema de la trazabilidad

**No hay un identificador único que recorra todo el sistema.** Cada etapa usa el suyo:

| Etapa | Identificador | Puente con la anterior |
|---|---|---|
| Recepción | `id_camda` | — |
| Conversión | nombre del fichero | El `filename` del flag |
| Carga | `cod_load_trace` | El nombre del fichero |
| Transformación | `cod_load_plan` | El plan de carga |
| Mapeo | `id_mapeo` | La tabla de origen |
| Qlik | UUID de tarea | El nombre de la tabla |

El puente entre etapas es casi siempre **el nombre del fichero o el de la tabla**. Por eso el
rastreo se hace por nombre, no por identificador.

## Las siete comprobaciones

### 1. ¿Lo declaró el flag?

```sql
SELECT id_camda, nome_flag_geral, nome_interface_base, nome_interface_completo,
       recebido, track_status, data_recebemento
FROM   stg_s3.controlflag_interfaces
WHERE  nome_interface_base ILIKE '%<INTERFAZ>%'
ORDER  BY id_camda DESC LIMIT 5;
```

No aparece → el origen no lo declaró. `recebido = false` → declarado pero ausente.
Ver [R4_05_flag_sin_xml](../R4%20-%20Sets%20incompletos/R4_05_flag_sin_xml.md).

### 2. ¿Llegó físicamente?

```bash
. /nfq/data/cfg/env.properties
ls -la /prdmegara/PRD/Devices/MegaCommon/innotech/ | grep -i "<INTERFAZ>"
```

### 3. ¿Se convirtió?

El XML original archivado y cifrado es la prueba:

```bash
ls -la $processed/DIR_MEGARA/ | grep -i "<INTERFAZ>"
```

Presente → convirtió (o venía vacío). Ausente y el XML sigue en llegada → la conversión falló.
Ver [C10_conversion_sin_filas](../C%20-%20Conversion%20Java/C10_conversion_sin_filas.md).

### 4. ¿Se generaron los planos?

```bash
ls -la $raiz | grep "<timestamp_del_xml>"
```

Todas las salidas de un XML comparten su timestamp. Ficheros de 0 bytes son normales.
Ver [C06_ficheros_de_salida](../C%20-%20Conversion%20Java/C06_ficheros_de_salida.md).

### 5. ¿Se cargó?

```sql
SELECT cod_load_trace, cod_load_plan, dat_load_date, des_file_loaded,
       amt_register_process, cod_status, des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  des_file_loaded ILIKE '%<INTERFAZ>%'
ORDER  BY dat_load_date DESC LIMIT 5;
```

**Anota el `cod_load_trace`**: es el identificador con el que se sigue el rastro dentro de la base.

```sql
-- Reparto entre buenas, erróneas y descartadas
SELECT 'T' AS t, count(*) FROM stg_s3.<TABLA>_T   WHERE cod_load_trace = :trace
UNION ALL SELECT 'ERR', count(*) FROM stg_s3.<TABLA>_ERR WHERE cod_load_trace = :trace
UNION ALL SELECT 'DES', count(*) FROM stg_s3.<TABLA>_DES WHERE cod_load_trace = :trace;
```

### 6. ¿Se transformó?

```sql
SELECT count(*) FROM trf_s3.<TABLA_DESTINO>;

SELECT dat_load_date, step_load, cod_status, des_log
FROM   stg_s3.aud_log_trace_t
WHERE  cod_load_plan = :plan AND dat_load_date >= CURRENT_DATE
ORDER  BY dat_load_date DESC LIMIT 30;
```

### 7. ¿Se mapeó y se recargó?

```sql
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio, activo_inactivo
FROM   exp_s3.tablas_mapeio_t
WHERE  nome_tabela_aldrin ILIKE '%<TABLA>%';

SELECT count(*) FROM trf_s3.<TABLA_SALIDA>;
```

```bash
grep -i "<TABLA>" /nfq/data/cfg/lookup_qlik.txt    # tarea y UUID de recarga
```

## Tabla de resultados

| Última comprobación que pasó | Se quedó en | Ficha |
|---|---|---|
| Ninguna | El origen no lo mandó | [R4_05_flag_sin_xml](../R4%20-%20Sets%20incompletos/R4_05_flag_sin_xml.md) |
| 1 | Declarado pero no llegó | [R4_05_flag_sin_xml](../R4%20-%20Sets%20incompletos/R4_05_flag_sin_xml.md) |
| 2 | No se convirtió | [C12_conversion_fallo_log](../C%20-%20Conversion%20Java/C12_conversion_fallo_log.md) |
| 3 | Convirtió pero sin salida: XML vacío | [C10_conversion_sin_filas](../C%20-%20Conversion%20Java/C10_conversion_sin_filas.md) |
| 4 | No se cargó | [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md) / [D09_error_numero_columnas](../D%20-%20Carga%20STG/D09_error_numero_columnas.md) |
| 5 | Cargó pero no transformó | Familia `F` |
| 6 | Transformó pero no mapeó | [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md) |
| 7 | Todo bien: es cosa de Qlik | [H09_qlik_datos_de_ayer](../H%20-%20Cierre%20y%20Qlik/H09_qlik_datos_de_ayer.md) |

## El atajo

En la práctica, **empieza por el final**. Comprobar si el dato está en `exp_s3` y retroceder es más
rápido que seguir el camino desde el fichero: la mayoría de las veces el dato sí llegó y el problema
está en el último tramo. Ver [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md).

## Ver también

[A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md) · [A02_flujo_e2e_seis_pasos](../A%20-%20Orientacion/A02_flujo_e2e_seis_pasos.md) · [B03_ciclo_de_vida_del_fichero](../B%20-%20Recepcion%20y%20flags/B03_ciclo_de_vida_del_fichero.md) · [R1_11_consultas_descartes](../R1%20-%20Descartes/R1_11_consultas_descartes.md) · [R4_10_consultas_que_falta](../R4%20-%20Sets%20incompletos/R4_10_consultas_que_falta.md)

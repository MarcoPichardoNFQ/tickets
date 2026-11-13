---
titulo: "I05 — Índice de tablas de control y auditoría"
familia: I
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/I
  - etapa/transversal
  - tipo/referencia
keywords: "índice, tablas de control, auditoría, dónde miro, mapa"
---

# I05 — Índice de tablas de control y auditoría

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** índice, tablas de control, auditoría, dónde miro, mapa

## En una línea

Todas las tablas donde el sistema deja rastro, ordenadas por la pregunta que responden.

## Por pregunta

| Necesito saber… | Tabla | Ficha |
|---|---|---|
| ¿Llegó el flag? | `stg_s3.controlflag_arquivos` | [B07_tablas_controlflag](../B%20-%20Recepcion%20y%20flags/B07_tablas_controlflag.md) |
| ¿Llegó cada fichero declarado? | `stg_s3.controlflag_interfaces` | [R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md) |
| ¿Cuánto pesaba cada fichero? | `trf_s3.tmp_controlflag_interfaces` | [B07_tablas_controlflag](../B%20-%20Recepcion%20y%20flags/B07_tablas_controlflag.md) |
| ¿Qué pasó con esta carga? | `stg_s3.aud_load_trace_t` | [E06_tablas_auditoria](../E%20-%20Parametrizacion/E06_tablas_auditoria.md) |
| ¿Qué fila se descartó y por qué? | `stg_s3.aud_load_valid_trace_t` | [R1_02_donde_cae_cada_cosa](../R1%20-%20Descartes/R1_02_donde_cae_cada_cosa.md) |
| ¿Qué mensajes dejó el proceso? | `stg_s3.aud_log_trace_t` | [I13_leer_aud_log_trace](../I%20-%20Referencia%20de%20datos/I13_leer_aud_log_trace.md) |
| ¿Qué mapeo está activo? | `exp_s3.tablas_mapeio_t` | [G02_tablas_mapeio_activo](../G%20-%20Mapeos/G02_tablas_mapeio_activo.md) |
| ¿Se abrió el lote de mapeos? | `exp_s3.control_mapeio_t` | [G08_fim_carga_mapeo](../G%20-%20Mapeos/G08_fim_carga_mapeo.md) |
| ¿Falló algún mapeo? | `trf_s3.s3_control_errores_mapeo` | [G09_job_control_errores](../G%20-%20Mapeos/G09_job_control_errores.md) |
| ¿Se publica este cliente en Qlik? | `trf_s3.s3_interface_control_xml_t` | [R4_04_s3_interface_control](../R4%20-%20Sets%20incompletos/R4_04_s3_interface_control.md) |
| ¿Qué columnas expone Qlik? | `exp_s3.relaciontablacolumnas` | [H07_lookup_qlik](../H%20-%20Cierre%20y%20Qlik/H07_lookup_qlik.md) |
| ¿Está bloqueado este cliente? | `trf_s3.cart_estat_portfoliomaster` | [F07_bloqueio_insercao_dados](../F%20-%20Transformacion%20TRF/F07_bloqueio_insercao_dados.md) |

## Por capa

**Recepción**

```
stg_s3.controlflag_arquivos       una fila por flag recibido
stg_s3.controlflag_interfaces     una fila por interfaz declarada  ← recebido / track_status
trf_s3.tmp_controlflag_interfaces igual + tamanho_interfaz
```

**Carga y validación**

```
stg_s3.aud_load_trace_t           una fila por carga     ← des_process_executed
stg_s3.aud_load_valid_trace_t     una fila por rechazo   ← des_validate
stg_s3.aud_log_trace_t            una fila por mensaje
stg_s3.<TABLA>_ERR / _DES         las filas apartadas
```

**Parametrización**

```
stg_s3.PAR_LOAD_PLAN_T            cómo se carga cada fichero  ← valid_err_des
stg_s3.PAR_MAESTRO_TABLAS_T       catálogo de tablas
stg_s3.PAR_MAESTRO_COLUMNAS_T     contrato por columna        ← chk_null, chk_clave
stg_s3.PAR_MAESTRO_MASK_T         máscaras de formato
stg_s3.PAR_MAESTRO_VALID_T        relaciones de integridad
stg_s3.PAR_MAESTRO_LOG_LEVEL_T    verbosidad de la traza
```

Ver [E01_tablas_par_metadata_driven](../E%20-%20Parametrizacion/E01_tablas_par_metadata_driven.md).

**Mapeos**

```
exp_s3.tablas_mapeio_t            control por mapeo   ← activo_inactivo, is_fromtis, retry_deadlock
exp_s3.control_mapeio_t           contador por lote   ← control_carga
trf_s3.s3_control_errores_mapeo   errores             ← des_func, cod_sqlstate, des_sqlerrm
trf_s3.<TABLA>_err                duplicados apartados
```

**Cierre y publicación**

```
trf_s3.s3_interface_control_t     control por cliente y NAV
trf_s3.s3_interface_control_xml_t igual + des_fnavtype   ← lo que consulta Qlik
exp_s3.relaciontablacolumnas      columnas expuestas
exp_s3.tabla_control              auditoría de recargas (uso no confirmado)
```

## Las que NO existen aunque lo parezca

| Nombre | Realidad |
|---|---|
| `stg_s3.load_trace_t` | **No existe.** El manejador de `fn_reproceso_descart` escribe ahí y falla |
| Tabla de duplicados | No hay: `validate_rows_key_fn` nunca se ejecuta |
| Registro de duración por bloque | No está en base de datos, sólo en el histórico de Rundeck |

Ver [R1_09_reprocesar_descartes](../R1%20-%20Descartes/R1_09_reprocesar_descartes.md) y [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md).

## Ver también

[E06_tablas_auditoria](../E%20-%20Parametrizacion/E06_tablas_auditoria.md) · [I12_consultas_frecuentes](../I%20-%20Referencia%20de%20datos/I12_consultas_frecuentes.md) · [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md) · [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md)

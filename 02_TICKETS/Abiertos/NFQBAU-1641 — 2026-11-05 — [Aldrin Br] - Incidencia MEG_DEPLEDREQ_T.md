---
id: NFQBAU-1641
fecha_apertura: 2026-11-05
fecha_limite: 2026-11-06
fecha_resolucion: 2026-11-06
estado: Resuelto
prioridad: Baja
responsable: Antonio Montoro
origen: email
referencia_origen: "[Aldrin Br] - Incidencia MEG_DEPLEDREQ_T (2026-11-05)"
categoria:
  - Rundeck
entorno:
  - Producción
sintoma: Se ha encontrado un error en una llamada de proceso a nivel STG relacionado con la tabla MEG_DEPLEDREQ_T durante una ejecución de Rundeck.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-06 22:44
actualizado_por: Marco Pichardo
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marco P., Senior Consultant de NFQ, informa de un error en una ejecución de Rundeck. El problema se detectó el 2026-11-04 al revisar el histórico de ejecuciones y está relacionado con la tabla MEG_DEPLEDREQ_T. Adjunta un link de Rundeck.

Detalles: ID Ejecución: 11328333; Link Ejecución: https://rundeck.s3caceis.com.br:4443/project/Aldrin-Megara/execution/show/11328333; Fecha Log: 2026-11-04 16:24:31; Contexto: 2 @node\=Rundeck Server PRD - azu-0051-rdkspo/2/1@node\=Rundeck Server PRD - azu-0051-rdkspo/12@node\=Rundeck Server PRD - azu-0051-rdkspo/19; Ruta Jerárquica: ROOT -> 00 - JOBs MEGARA Base/Main Job Megara; Recurso / Job: Script / Comando Interno; Tablas afectadas: STG_S3.MEG_DEPLEDREQ_T; Funciones mencionadas: LOAD_FILES_PC, VALIDATE_GEN_PC, fn_count_reg_tables, validate_rows_foreign_fn, FN_MERGE_INTO_DESCARTES, FN_LOAD_DATA_ERR, log_trace, trf_s3.cs_DEPLEDREQ_transf_pc; Mensajes de error: DYB V_VALID_ERR_DES error formarto 1=DES 1; FN_MERGE_INTO_DESC v_sqlerr there is no unique or exclusion constraint matching the ON CONFLICT specification; FN_LOAD_DATA_ERR v_sqlerr function log_trace(integer, character varying, integer, integer, unknown) does not exist; /tmp/136900-11328333-Rundeck_Server_PRD_-_azu-0051-rdkspo-load_stgtrf_script.sh: line 77: /prddatahub/DIR_FLAG/: Is a directory

## Histórico de interacciones

- 2026-11-05 00:27 — Correo automático — Marco P., Senior Consultant de NFQ, informa de un error en una ejecución de Rundeck. El problema se detectó el 2026-11-04 al revisar el histórico de ejecuciones y está relacionado con la tabla MEG_DEPLEDREQ_T. Adjunta un link de Rundeck.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

### Cómo se comprobó

### Con quién se habló

### Servicios, jobs o tablas tocados

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-11-05 00:27 — nuevo → Abierto — Correo automático
- 2026-11-06 12:14 — nuevo → Abierto — Matheus Fransoni
- 2026-11-06 12:32 — Abierto → Resuelto — Matheus Fransoni

---
id: NFQBAU-1690
fecha_apertura: 2026-11-11
fecha_limite: 2026-11-12
fecha_resolucion:            # obligatoria al pasar a Resuelto
estado: Abierto              # ver 05_GENERAL/listas.json
prioridad: Media
responsable:                 # Nombre Apellido, igual que el fichero en 04_PERSONAS
origen: email
referencia_origen: "[ALDRIN BR] - Demora Carga Atual PRD - PATR RF (2026-11-11)"
categoria: [BBDD]
entorno: [Producción]
sintoma: "Demora en la ejecución de la función trf_s3.function_meg_sac_pl_cl_patrrf_t() durante la carga."
solucion_corta:              # una línea: qué lo arregló
codigo_relacionado:
  - repo:
    modulo:
    version:                 # tag de PRD cuando se despliegue
tickets_proveedor: []        # notas de 03_PROVEEDORES
decision_relacionada:
referencias_tecnicas: []     # fichas de 00_REFERENCIA_TECNICA que ayudaron
actualizado: 2026-11-11 16:41
actualizado_por: Correo automático
tags: [ticket, bau]
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Gustavo B., desarrollador del cliente, solicita la modificación de la función trf_s3.function_meg_sac_pl_cl_patrrf_t() para corregir un problema de rendimiento en producción. Pide desplegar primero la versión actualizada en el entorno de UAT para realizar las pruebas necesarias. Adjunta un fichero y capturas.

Detalles: Función afectada: trf_s3.function_meg_sac_pl_cl_patrrf_t(); Tablas involucradas: MAX_VALPORCS, trf_s3.sss_refrate_price_t, TEM_meg_sac_pl_cl_patrrf_t, POSI, cdi; Problema técnico: el LEFT JOIN con la tabla sss_refrate_price_t evalúa trf_s3.data_calc por cada línea sin usar índices ni hash join; Solución propuesta: creación de tabla temporal cdi indexada para buscar la tasa CDI una sola vez por fecha; Archivo adjunto: UPDATE function_meg_sac_pl_cl_patrrf_t_20261111.sql
Adjuntos del correo: image.png, UPDATE function_meg_sac_pl_cl_patrrf_t_20261111.sql

## Histórico de interacciones

- 2026-11-11 16:41 — Correo automático — Gustavo B., desarrollador del cliente, solicita la modificación de la función trf_s3.function_meg_sac_pl_cl_patrrf_t() para corregir un problema de rendimiento en producción. Pide desplegar primero la versión actualizada en el entorno de UAT para realizar las pruebas necesarias. Adjunta un fichero y capturas.

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
- 2026-11-11 16:41 — nuevo → Abierto — Correo automático

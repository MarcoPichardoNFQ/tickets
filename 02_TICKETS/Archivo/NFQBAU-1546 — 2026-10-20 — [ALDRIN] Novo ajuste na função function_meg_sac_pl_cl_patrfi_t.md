---
id: NFQBAU-1546
fecha_apertura: 2026-10-20
fecha_limite: 2026-10-20
fecha_resolucion: 2026-11-04
estado: Resuelto
prioridad: Alta
responsable: Deborah Bertoldo
origen: email
referencia_origen: "[ALDRIN] Novo ajuste na função function_meg_sac_pl_cl_patrfi_t (2026-10-20)"
categoria:
  - BBDD
entorno:
  - Producción
sintoma: La función function_meg_sac_pl_cl_patrfi_t está calculando incorrectamente la diferencia de segundos dentro del mismo procesamiento al usar la fecha y hora de actualización en lugar del número de procesamiento.
solucion_corta: "Se ajustó la lógica de la función para usar cod_valprocs en lugar de dat_update para identificar el procesamiento."
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-08 08:30
actualizado_por: Correo automático
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Thiago A., de Sancac, solicita a Marco J. P., Deborah B. y Matheus D. que ajusten una función de base de datos. El problema se debe a una diferencia de segundos en el procesamiento que afecta a la lógica de selección de datos en producción. Adjunta una captura.

Detalles: Función a ajustar: function_meg_sac_pl_cl_patrfi_t (); El ajuste implica cambiar la lógica de unión para usar 'cod_valprocs' en lugar de 'dat_update' para identificar el procesamiento; Se propone una subconsulta con 'row_number() over(partition by E.DES_OWNER, E.DAT_VALUAT order by E.DAT_UPDATE desc) as rn' para seleccionar el registro más reciente por DES_OWNER y DAT_VALUAT y luego usar cod_valprocs; Adjunta capturas.
Adjuntos del correo: image001.png

## Histórico de interacciones

- 2026-10-20 15:42 — Correo automático — Thiago A., de Sancac, solicita a Marco J. P., Deborah B. y Matheus D. que ajusten una función de base de datos. El problema se debe a una diferencia de segundos en el procesamiento que afecta a la lógica de selección de datos en producción. Adjunta una captura.
- 2026-11-08 08:30 — Correo automático — Resolución redactada automáticamente a partir del histórico; revisar.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Se modificó la lógica de unión de la función. Se implementó una subconsulta utilizando row_number para seleccionar el registro más reciente por DES_OWNER y DAT_VALUAT.

### Cómo se comprobó

No consta en el histórico.

### Con quién se habló

Thiago A., Sancac; Marco J. P., soporte; Deborah B., soporte; Matheus D., soporte.

### Servicios, jobs o tablas tocados

function_meg_sac_pl_cl_patrfi_t, cod_valprocs, dat_update, DES_OWNER, DAT_VALUAT

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-10-20 15:42 — (vacío) → Abierto — Correo automático
- 2026-10-21 01:29 — Abierto → Revisión cliente — Marco Pichardo
- 2026-11-04 15:34 — Revisión cliente → Resuelto — Matheus Fransoni

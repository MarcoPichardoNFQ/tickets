---
id: NFQBAU-1667
fecha_apertura: 2026-11-08
fecha_limite: 2026-11-09
fecha_resolucion: 2026-11-09
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: "[ALDRIN] - Houve errors no mapeamento de PRD (2026-11-08)"
categoria:
  - Rundeck
entorno:
  - Producción
sintoma: El job 'Job control errores mapeo' de Rundeck falló en producción, indicando errores en el mapeo.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-09 17:26
actualizado_por: Matheus Fransoni
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Continúa el hilo del [NFQBAU-1620](../Abiertos/NFQBAU-1620%20—%202026-11-03%20—%20[ALDRIN]%20-%20Houve%20errors%20no%20mapeamento%20de%20PRD.md), cerrado el 2026-11-05: no se reabre, se crea este. El sistema ha generado una alerta automática informando que un job de control de errores de mapeo ha fallado en producción.

Detalles: Execution ID: #11519837; URL de ejecución: https://rundeck.s3caceis.com.br:4443/project/Aldrin-Megara/execution/show/11519837; Job referenciado: '001 - JOBs Mapeos/Job control errores mapeo'; Usuario: t000055; Inicio: 2026-11-08 12:35:54.02; Nodos fallidos: 1 de 1; Pasos del job: /Validacion constante presencia archivos flag (Aldrin-Megara); 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara)

## Histórico de interacciones

- 2026-11-08 12:41 — Correo automático — Continúa el hilo del [NFQBAU-1620](../Abiertos/NFQBAU-1620%20—%202026-11-03%20—%20[ALDRIN]%20-%20Houve%20errors%20no%20mapeamento%20de%20PRD.md), cerrado el 2026-11-05: no se reabre, se crea este. El sistema ha generado una alerta automática informando que un job de control de errores de mapeo ha fallado en producción.
- 2026-11-08 12:46 — Correo automático — Correo nuevo en el hilo: El sistema de alertas de Rundeck informa de un error en la ejecución de un job de mapeo en producción. El problema ocurrió el 8 de noviembre de 2026. Detalles: Execution ID: #11520156; Job: '001 - JOBs Mapeos/Job control errores mapeo'; Usuario: t000055; Inicio: 2026-11-08 12:42:03.019; Pasos: '/Validacion constante presencia archivos flag (Aldrin-Megara)'; '00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara)'; 1 de 1 nodo falló.
- 2026-11-08 12:46 — Correo automático — Correo nuevo en el hilo: Una alerta automática de Rundeck informa de un error en la ejecución de un job de mapeo en producción. Detalles: Execution ID: 11519998; Job: '001 - JOBs Mapeos/Job control errores mapeo'; Usuario: t000055; Inicio: 2026-11-08 12:38:45.02; 1 nodo falló; Proyecto: Aldrin-Megara.
- 2026-11-08 12:51 — Correo automático — Correo nuevo en el hilo: El sistema Rundeck ha enviado una alerta automática informando de errores en la ejecución de un job de mapeo en producción. Detalles: Execution ID: #11520304; Job: "001 - JOBs Mapeos/Job control errores mapeo"; Usuario: t000055; Inicio: 2026-11-08 12:44:54.014; Proyecto: Aldrin-Megara; Pasos: /Validacion constante presencia archivos flag (Aldrin-Megara), 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara); Nodos: 1 de 1 fallido.
- 2026-11-08 12:51 — Correo automático — Correo nuevo en el hilo: Un sistema automático de Rundeck ha notificado un error en la ejecución de un job de mapeo en producción, que ha fallado hace 2 minutos y 16 segundos. Detalles: Execution ID: #11520445; Referenced Job: '001 - JOBs Mapeos/Job control errores mapeo'; User: t000055; Started: 2026-11-08 12:47:42.023; Steps: '/Validacion constante presencia archivos flag (Aldrin-Megara)'; '00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara)'; Nodes: 1 failed of 1; Link: https://rundeck.s3caceis.com.br:4443/project/Aldrin-Megara/execution/show/11520445
- 2026-11-08 12:56 — Correo automático — Correo nuevo en el hilo: El sistema Rundeck ha enviado una alerta automática informando que la ejecución del job de control de errores de mapeo ha fallado en producción. El job fue iniciado por t000055. Detalles: Execution ID: 11520608; Job '001 - JOBs Mapeos/Job control errores mapeo' falló; Iniciado por t000055; Hora de inicio: 2026-11-08 12:50:24.023; Un nodo falló (1 de 1); El job incluye los pasos 'Validacion constante presencia archivos flag' y '00 - JOBs MEGARA Base/Main Job Megara'.
- 2026-11-08 12:57 — Correo automático — Correo nuevo en el hilo: El sistema de alertas de Rundeck informa de errores en el mapeo de producción. La ejecución del job #11520747 ha fallado. Detalles: La ejecución #11520747 del job '001 - JOBs Mapeos/Job control errores mapeo' en el proyecto Aldrin-Megara ha fallado; el usuario t000055 inició la ejecución el 2026-11-08 12:53:15.015; un nodo ha fallado; los pasos involucrados son 'Validacion constante presencia archivos flag' y '00 - JOBs MEGARA Base/Main Job Megara'.
- 2026-11-08 13:06 — Correo automático — Correo nuevo en el hilo: El sistema de alertas de Rundeck informa de un error en la ejecución de un job de mapeo en producción. Detalles: Execution ID: #11520908; Referenced Job: "001 - JOBs Mapeos/Job control errores mapeo"; User: t000055; Started: 2026-11-08 12:56:06.03; Project: Aldrin-Megara; 1 de 1 nodo falló.
- 2026-11-08 13:06 — Correo automático — Correo nuevo en el hilo: El sistema de alertas de Rundeck informa que la ejecución del job 'Job control errores mapeo' en el proyecto Aldrin-Megara ha fallado, con errores en el mapeo en producción. El incidente ocurrió el 8 de noviembre de 2026. Detalles: Execution ID: #11521041; Job principal: '001 - JOBs Mapeos/Job control errores mapeo'; Proyecto: Aldrin-Megara; Usuario que inició la ejecución: t000055; Inicio de ejecución: 2026-11-08 12:58:51.015; Pasos involucrados: '/Validacion constante presencia archivos flag (Aldrin-Megara)'; '00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara)'; Nodos fallidos: 1 de 1.
- 2026-11-08 13:06 — Correo automático — Correo nuevo en el hilo: Una alerta automática de Rundeck informa de un error en la ejecución de un job de mapeo en producción. El problema ocurrió hoy, 2026-11-08. Detalles: ID de ejecución: #11521206; URL de ejecución: https://rundeck.s3caceis.com.br:4443/project/Aldrin-Megara/execution/show/11521206; Usuario: t000055; Inicio: 2026-11-08 13:01:57.018; Job referenciado: '001 - JOBs Mapeos/Job control errores mapeo'; Nodos fallidos: 1 de 1; Pasos mencionados: '/Validacion constante presencia archivos flag (Aldrin-Megara)'; '00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara)'
- 2026-11-08 13:07 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema alertando sobre un error en la ejecución del proceso de mapeos en el entorno de producción.
Se registra un nodo fallido en la ejecución del flujo de trabajo el 2026-11-08. Detalles: Ejecución: #11520908; Proyecto: Aldrin-Megara; Usuario de ejecución: t000055; Job referenciado: 001 - JOBs Mapeos/Job control errores mapeo; Pasos del flujo: /Validacion constante presencia archivos flag (Aldrin-Megara), 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara); Resultado: 1 failed (1 of 1 100% Complete)
- 2026-11-08 13:11 — Correo automático — Correo nuevo en el hilo: El sistema Rundeck ha enviado una alerta automática informando de un error en la ejecución de un job de mapeo en producción, ocurrido el 8 de noviembre de 2026. Detalles: Execution ID: #11521358; Job: "001 - JOBs Mapeos/Job control errores mapeo"; Usuario: t000055; Inicio: 2026-11-08 13:05:18.014; 1 nodo fallido de 1; Pasos: /Validacion constante presencia archivos flag (Aldrin-Megara), 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara); Proyecto: Aldrin-Megara
- 2026-11-08 13:11 — Correo automático — Correo nuevo en el hilo: El sistema Rundeck ha notificado un error en la ejecución del job de control de mapeos en producción. El problema se ha detectado hoy. Detalles: Execution ID: #11521509; Job: '001 - JOBs Mapeos/Job control errores mapeo'; Ejecutado por: t000055; Iniciado: 2026-11-08 13:07:54.019; Proyecto: Aldrin-Megara; Un nodo ha fallado; Pasos involucrados: 'Validacion constante presencia archivos flag' y '00 - JOBs MEGARA Base/Main Job Megara'.
- 2026-11-08 13:56 — Correo automático — Correo nuevo en el hilo: Una alerta automática de Rundeck informa que la ejecución del job "Job control errores mapeo" ha fallado en producción. El usuario t000055 inició la ejecución. Detalles: Execution ID: #11523648; URL: https://rundeck.s3caceis.com.br:4443/project/Aldrin-Megara/execution/show/11523648; Usuario: t000055; Inicio: 2026-11-08 13:50:30.023; Job referenciado: "001 - JOBs Mapeos/Job control errores mapeo"; Pasos: 1. /Validacion constante presencia archivos flag (Aldrin-Megara); 2. 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara); Nodos fallidos: 1 de 1.
- 2026-11-08 14:01 — Correo automático — Correo nuevo en el hilo: El sistema Rundeck ha enviado una alerta automática informando de un error en la ejecución de un job de mapeo en producción. Detalles: Execution ID: #11523788; Job: "001 - JOBs Mapeos/Job control errores mapeo"; Usuario: t000055; Inicio: 2026-11-08 13:53:57.022; Duración: 2m21s; Proyecto: Aldrin-Megara; Nodos: 1 de 1 fallido; Pasos: /Validacion constante presencia archivos flag (Aldrin-Megara); 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara)
- 2026-11-08 14:01 — Correo automático — Correo nuevo en el hilo: El sistema de alertas de Rundeck informa de un error en la ejecución de un job de mapeo en producción. El correo es una notificación automática. Detalles: Execution ID: #11523949; Job: "001 - JOBs Mapeos/Job control errores mapeo"; Proyecto: Aldrin-Megara; Usuario: t000055; Inicio: 2026-11-08 13:56:45.021; Nodos fallidos: 1 de 1; Pasos involucrados: /Validacion constante presencia archivos flag (Aldrin-Megara); 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara)
- 2026-11-08 14:06 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema Rundeck que avisa de que se ha producido un error en el mapeo de producción en la ejecución #11524088 iniciada por el usuario t000055. Detalles: Execution ID: 11524088; Proyecto: Aldrin-Megara; Job: 001 - JOBs Mapeos/Job control errores mapeo; Usuario: t000055; Fecha de inicio: 2026-11-08 13:59:45.02; Pasos involucrados: Validacion constante presencia archivos flag (Aldrin-Megara), 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara); 1 nodo fallido de 1 total.
- 2026-11-08 14:06 — Correo automático — Correo nuevo en el hilo: Una alerta automática de Rundeck informa de errores en el mapeo de PRD. La ejecución del job #11524269, iniciada por t000055, ha fallado. Detalles: Execution ID: #11524269; Job: '001 - JOBs Mapeos/Job control errores mapeo'; Usuario: t000055; Inicio: 2026-11-08 14:03:15.02; Pasos involucrados: '/Validacion constante presencia archivos flag (Aldrin-Megara)'; '00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara)'; Falló 1 de 1 nodo.
- 2026-11-08 14:11 — Correo automático — Correo nuevo en el hilo: Notificación automática enviada por el sistema Rundeck informando sobre el fallo en la ejecución del job de control de errores de mapeo el 2026-11-08. Detalles: ID de ejecución: #11524401; Proyecto: Aldrin-Megara; Job: 001 - JOBs Mapeos/Job control errores mapeo; Usuario: t000055; Fecha de inicio: 2026-11-08 14:05:57.019; Pasos: Validacion constante presencia archivos flag (Aldrin-Megara), 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara); Estado: 1 nodo fallido
- 2026-11-08 14:21 — Correo automático — Correo nuevo en el hilo: El sistema ha enviado una alerta automática informando de un error en la ejecución de un job de mapeo en producción. Detalles: Execution ID: #11524559; Job: '001 - JOBs Mapeos/Job control errores mapeo'; Proyecto: Aldrin-Megara; Usuario que inició: t000055; Inicio: 2026-11-08 14:08:45.021; 1 de 1 nodo falló; Pasos mencionados: '/Validacion constante presencia archivos flag (Aldrin-Megara)'; '00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara)'
- 2026-11-08 14:21 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema Rundeck informando sobre el fallo en la ejecución del job de control de errores de mapeo en el entorno de producción. Detalles: Execution ID: 11524699; Proyecto: Aldrin-Megara; Job: 001 - JOBs Mapeos/Job control errores mapeo; Usuario ejecutor: t000055; Fecha y hora: 2026-11-08 14:11:54.021; Pasos afectados: Validacion constante presencia archivos flag, 00 - JOBs MEGARA Base/Main Job Megara; 1 nodo fallido.
- 2026-11-08 14:22 — Correo automático — Correo nuevo en el hilo: El sistema de alertas de Rundeck notifica un error en la ejecución número 11525017 del job de mapeo. Detalles: Execution ID: 11525017; Job: 001 - JOBs Mapeos/Job control errores mapeo; Proyecto: Aldrin-Megara; Usuario: t000055; Fecha y hora: 2026-11-08 14:18:06.019; Pasos involucrados: Validacion constante presencia archivos flag, 00 - JOBs MEGARA Base/Main Job Megara.
- 2026-11-08 14:22 — Correo automático — Correo nuevo en el hilo: Se ha recibido una alerta automática del sistema notificando un error de mapeo en el entorno de producción.
El job finalizó con un nodo fallido en el proyecto Aldrin-Megara el 2026-11-08. Detalles: ID de ejecución: #11524699; Proyecto: Aldrin-Megara; Job referenciado: 001 - JOBs Mapeos/Job control errores mapeo; Usuario ejecutor: t000055; Inicio: 2026-11-08 14:11:54.021; Pasos: 1. /Validacion constante presencia archivos flag (Aldrin-Megara), 2. 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara); Resultado: 1 nodo fallido (100% completado)
- 2026-11-08 14:27 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema alertando de errores en el mapeo de producción. Se informa de que el job de control de errores de mapeo presentó un fallo en un nodo tras su ejecución el 2026-11-08. Detalles: ID de ejecución: 11525169; Proyecto: Aldrin-Megara; Job: 001 - JOBs Mapeos/Job control errores mapeo; Usuario de ejecución: t000055; Inicio de ejecución: 2026-11-08 14:20:51.025; Pasos involucrados: /Validacion constante presencia archivos flag, 00 - JOBs MEGARA Base/Main Job Megara; Estado de nodos: 1 failed (100% completado con fallo)
- 2026-11-08 14:31 — Correo automático — Correo nuevo en el hilo: El sistema de alertas de Rundeck informa de un error en la ejecución del job 'Job control errores mapeo' en el proyecto Aldrin-Megara. La ejecución, iniciada por t000055, falló el 8 de noviembre de 2026. Detalles: Execution ID: 11525478; Job: '001 - JOBs Mapeos/Job control errores mapeo'; Usuario que inició la ejecución: t000055; Hora de inicio: 2026-11-08 14:27:09.019; Un nodo falló (1 de 1); El job incluye los pasos 'Validacion constante presencia archivos flag (Aldrin-Megara)' y '00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara)'.
- 2026-11-08 14:31 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema que informa sobre errores en el mapeo de producción. El sistema Rundeck reporta el fallo de una ejecución generada el 08/11/2026. Detalles: Proyecto: Aldrin-Megara; Ejecución: #11525324; Job: 001 - JOBs Mapeos/Job control errores mapeo; Usuario: t000055; Fecha y hora de inicio: 2026-11-08 14:24:21.021; Pasos: 1. /Validacion constante presencia archivos flag, 2. 00 - JOBs MEGARA Base/Main Job Megara; Resultado: 1 failed
- 2026-11-08 14:36 — Correo automático — Correo nuevo en el hilo: El sistema automático de Rundeck notifica un error en la ejecución número 11525625 del job '001 - JOBs Mapeos/Job control errores mapeo' en el proyecto Aldrin-Megara. Detalles: Execution: #11525625; Job: 001 - JOBs Mapeos/Job control errores mapeo; Proyecto: Aldrin-Megara; Usuario: t000055; Fecha inicio: 2026-11-08 14:30:00.076; Pasos afectados: Validacion constante presencia archivos flag, 00 - JOBs MEGARA Base/Main Job Megara; 1 nodo fallido.
- 2026-11-08 14:36 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema informando de que ha fallado la ejecución número 11525782 del job de control de errores de mapeo en el proyecto Aldrin-Megara. Detalles: Job: 001 - JOBs Mapeos/Job control errores mapeo; Execution ID: 11525782; Usuario: t000055; Fecha y hora: 2026-11-08 14:33:12.023; Paso fallido: Validacion constante presencia archivos flag (Aldrin-Megara)
- 2026-11-08 14:41 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema informando sobre un error en la ejecución del job de mapeo en el entorno de producción. Detalles: Execution #11525930; Proyecto: Aldrin-Megara; Job: 001 - JOBs Mapeos/Job control errores mapeo; Usuario: t000055; Fecha y hora: 2026-11-08 14:36:12.022; Paso fallido: 00 - JOBs MEGARA Base/Main Job Megara; URL: https://rundeck.s3caceis.com.br:4443/project/Aldrin-Megara/execution/show/11525930

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
- 2026-11-08 12:41 — nuevo → Abierto — Correo automático
- 2026-11-09 17:26 — Abierto → Resuelto — Matheus Fransoni

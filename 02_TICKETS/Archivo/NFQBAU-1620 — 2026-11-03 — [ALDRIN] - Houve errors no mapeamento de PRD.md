---
id: NFQBAU-1620
fecha_apertura: 2026-11-03
fecha_limite: 2026-11-04
fecha_resolucion: 2026-11-05
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: "[ALDRIN] - Houve errors no mapeamento de PRD (2026-11-03)"
categoria:
  - Rundeck
entorno:
  - Producción
sintoma: La ejecución del job de Rundeck 'Job control errores mapeo' en el proyecto Aldrin-Megara ha fallado en producción.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-06 22:43
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

Una alerta automática de Rundeck informa que una ejecución de un job de mapeo en producción ha fallado el 2026-11-03.

Detalles: Execution ID: #11279255; Job: '001 - JOBs Mapeos/Job control errores mapeo'; Usuario: t000055; Inicio: 2026-11-03 17:27:36.019; Pasos: /Validacion constante presencia archivos flag (Aldrin-Megara), 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara); Nodos fallidos: 1 de 1; Proyecto: Aldrin-Megara

## Histórico de interacciones

- 2026-11-03 17:36 — Correo automático — Una alerta automática de Rundeck informa que una ejecución de un job de mapeo en producción ha fallado el 2026-11-03.
- 2026-11-03 17:41 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema informando de un error en la ejecución del job de Rundeck. Detalles: Execution #11279459; Proyecto: Aldrin-Megara; Job: '001 - JOBs Mapeos/Job control errores mapeo'; Usuario: t000055; Fecha inicio: 2026-11-03 17:34:15.021; Paso fallido: Validacion constante presencia archivos flag (Aldrin-Megara) y 00 - JOBs MEGARA Base/Main Job Megara; 1 node failed.
- 2026-11-03 17:46 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema informando de un error en la ejecución del job de Rundeck en el entorno de producción. Detalles: Execution #11279654; Job: 001 - JOBs Mapeos/Job control errores mapeo; Proyecto: Aldrin-Megara; Usuario: t000055; Fecha de inicio: 2026-11-03 17:40:09.025; Paso fallido: Validacion constante presencia archivos flag (Aldrin-Megara); 1 nodo fallido de 1.
- 2026-11-03 17:51 — Correo automático — Correo nuevo en el hilo: Se ha recibido una alerta automatizada del sistema indicando un error en la ejecución del mapeo en el proyecto Aldrin-Megara. Detalles: Execution: #11279836; Proyecto: Aldrin-Megara; Usuario: t000055; Fecha inicio: 2026-11-03 17:45:54.013; Job: 001 - JOBs Mapeos/Job control errores mapeo; Paso fallido: Validacion constante presencia archivos flag / Main Job Megara; Nodos fallidos: 1
- 2026-11-03 17:56 — Correo automático — Correo nuevo en el hilo: El sistema automatizado de alertas notifica que se ha producido un error en la ejecución del job de mapeo en el proyecto Aldrin-Megara. Detalles: Job ID: #11280019; Proyecto: Aldrin-Megara; Job referenciado: 001 - JOBs Mapeos/Job control errores mapeo; Usuario: t000055; Fecha de inicio: 2026-11-03 17:50:57.023; Paso fallido: 1. /Validacion constante presencia archivos flag (Aldrin-Megara)
- 2026-11-03 18:01 — Correo automático — Correo nuevo en el hilo: El sistema notificó de forma automática el 2026-11-03 la existencia de errores en el mapeo del entorno de producción.
La alerta se generó tras la ejecución del proceso de control de errores en la plataforma Rundeck, el cual finalizó con nodos fallidos. Detalles: ID de ejecución: #11280208; Job referenciado: '001 - JOBs Mapeos/Job control errores mapeo'; Proyecto: Aldrin-Megara; Usuario: t000055; Fecha de inicio: 2026-11-03 17:56:15.021; Pasos del flujo: 1. /Validacion constante presencia archivos flag, 2. 00 - JOBs MEGARA Base/Main Job Megara; Resultado: 1 nodo fallido
- 2026-11-03 18:06 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema indicando que se ha producido un error en el job de mapeo. Detalles: Execution #11280380; Proyecto: Aldrin-Megara; Job: 001 - JOBs Mapeos/Job control errores mapeo; Paso fallido: Validacion constante presencia archivos flag (Aldrin-Megara) y 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara); Fecha de inicio: 2026-11-03 18:00:33.019
- 2026-11-03 18:21 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema Rundeck informando sobre un error en la ejecución del job de mapeo en el proyecto Aldrin-Megara. Detalles: Job ID: #11280757; Proyecto: Aldrin-Megara; Job referenciado: 001 - JOBs Mapeos/Job control errores mapeo; Usuario: t000055; Fecha de inicio: 2026-11-03 18:12:42.018; Pasos afectados: Validacion constante presencia archivos flag, 00 - JOBs MEGARA Base/Main Job Megara; 1 nodo fallido.
- 2026-11-03 18:26 — Correo automático — Correo nuevo en el hilo: El sistema automático de alertas notifica un error en la ejecución del job de mapeo de producción. Detalles: Execution ID: #11280934; Proyecto: Aldrin-Megara; Job con errores: '001 - JOBs Mapeos/Job control errores mapeo'; Usuario de ejecución: t000055; Fecha y hora de inicio: 2026-11-03 18:17:42.021; Paso fallido: Validacion constante presencia archivos flag (Aldrin-Megara).
- 2026-11-03 18:31 — Correo automático — Correo nuevo en el hilo: El sistema de alertas de Rundeck notifica un error en la ejecución del job #11281144 en el entorno de producción, lanzado por el usuario t000055 el 2026-11-03 a las 18:24. Detalles: Execution #11281144; Proyecto: Aldrin-Megara; Usuario: t000055; Fecha inicio: 2026-11-03 18:24:18.028; Job referenciado: 001 - JOBs Mapeos/Job control errores mapeo; Pasos: 1. /Validacion constante presencia archivos flag (Aldrin-Megara), 2. 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara); 1 nodo fallido.
- 2026-11-03 18:36 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema Rundeck que avisa de que se ha producido un error en la ejecución del mapeo en PRD. Detalles: Execution #11281318; Proyecto: Aldrin-Megara; Job: 001 - JOBs Mapeos/Job control errores mapeo; Usuario: t000055; Fecha inicio: 2026-11-03 18:29:27.016; Paso fallido: 00 - JOBs MEGARA Base/Main Job Megara
- 2026-11-03 18:41 — Correo automático — Correo nuevo en el hilo: El sistema automático de alertas notifica un fallo en la ejecución #11281492 del job de Rundeck asociado al proyecto Aldrin-Megara. Detalles: Job ID: 11281492; Proyecto: Aldrin-Megara; Job afectado: 001 - JOBs Mapeos/Job control errores mapeo; Paso fallido: 00 - JOBs MEGARA Base/Main Job Megara; Fecha de inicio: 2026-11-03 18:33:42.018
- 2026-11-03 18:46 — Correo automático — Correo nuevo en el hilo: Se ha recibido una notificación automática de alerta del sistema indicando que ha fallado la ejecución de un job de mapeo en el entorno de producción. Detalles: Job: 001 - JOBs Mapeos/Job control errores mapeo; Ejecución ID: #11281672; Proyecto: Aldrin-Megara; Usuario de ejecución: t000055; Fecha y hora de inicio: 2026-11-03 18:38:00.026; Paso fallido: Validacion constante presencia archivos flag; URL: https://rundeck.s3caceis.com.br:4443/project/Aldrin-Megara/execution/show/11281672
- 2026-11-03 18:51 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema de alertas indicando que ha fallado la ejecución del job. Detalles: Job ID: 11281834; Proyecto: Aldrin-Megara; Job referenciado: 001 - JOBs Mapeos/Job control errores mapeo; Paso fallido: Validacion constante presencia archivos flag / 00 - JOBs MEGARA Base/Main Job Megara; Fecha de inicio: 2026-11-03 18:42:39.022
- 2026-11-03 18:56 — Correo automático — Correo nuevo en el hilo: Una alerta automática de Rundeck informa que la ejecución del job 'Job control errores mapeo' ha fallado en producción. Detalles: Execution ID: #11282010; Referenced Job: "001 - JOBs Mapeos/Job control errores mapeo"; User: t000055; Started: 2026-11-03 18:47:06.02; Steps: /Validacion constante presencia archivos flag (Aldrin-Megara); 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara); Nodes: 1 failed of 1; Project: Aldrin-Megara
- 2026-11-03 19:01 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema informando de que el job de mapeo en producción ha dado errores. Se trata de un aviso automatizado generado por Rundeck. Detalles: Execution ID: 11282193; Proyecto: Aldrin-Megara; Usuario: t000055; Job referenciado: 001 - JOBs Mapeos/Job control errores mapeo; Paso fallido: 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara); Fecha de inicio: 2026-11-03 18:52:15.015
- 2026-11-03 19:06 — Correo automático — Correo nuevo en el hilo: El sistema de alertas de Rundeck informa que la ejecución #11282364 del job 'Job control errores mapeo' ha fallado. El problema ocurrió el 3 de noviembre de 2026. Detalles: Ejecución de Rundeck #11282364; Job '001 - JOBs Mapeos/Job control errores mapeo'; Proyecto Aldrin-Megara; Usuario: t000055; Iniciado: 2026-11-03 18:56:57.016; Un nodo falló (1 de 1); Pasos del job: 'Validacion constante presencia archivos flag (Aldrin-Megara)' y '00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara)'
- 2026-11-03 19:11 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema indicando que el job #11282722 ha fallado en el entorno de producción. Detalles: Job ID: #11282722; Proyecto: Aldrin-Megara; Usuario de ejecución: t000055; Fecha de inicio: 2026-11-03 19:06:45.021; Job referenciado: 001 - JOBs Mapeos/Job control errores mapeo; Paso fallido: Validacion constante presencia archivos flag (Aldrin-Megara) y 00 - JOBs MEGARA Base/Main Job Megara; 1 nodo fallido de 1.
- 2026-11-03 19:16 — Correo automático — Correo nuevo en el hilo: Una notificación automática de Rundeck informa de un error en el mapeo de PRD. Detalles: Execution ID: #11282894; Job: '001 - JOBs Mapeos/Job control errores mapeo'; Usuario: t000055; Inicio: 2026-11-03 19:11:00.024; Pasos: /Validacion constante presencia archivos flag (Aldrin-Megara), 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara); Nodos fallidos: 1 de 1; Proyecto: Aldrin-Megara
- 2026-11-03 19:21 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema Rundeck informando sobre el fallo en la ejecución del job de mapeo en producción el 2026-11-03. Detalles: Execution: #11283059; Proyecto: Aldrin-Megara; Job referenciado: 001 - JOBs Mapeos/Job control errores mapeo; Usuario: t000055; Fecha/Hora inicio: 2026-11-03 19:14:36.022; Paso fallido: Validacion constante presencia archivos flag (Aldrin-Megara); 1 nodo fallido de 1.
- 2026-11-03 19:26 — Correo automático — Correo nuevo en el hilo: El sistema de alertas de Rundeck informa de un error en la ejecución del job 'Job control errores mapeo' en el proyecto Aldrin-Megara. Detalles: Execution ID: #11283217; Job: '001 - JOBs Mapeos/Job control errores mapeo'; Proyecto: Aldrin-Megara; Usuario: t000055; Inicio: 2026-11-03 19:18:36.021; Nodos: 1 de 1 fallido; Pasos: '/Validacion constante presencia archivos flag (Aldrin-Megara)'; '00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara)'; Mensaje de error: 'Houve errors no mapeamento de PRD'
- 2026-11-03 19:31 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema indicando que se ha producido un error en el job de Rundeck de mapeo en producción desde el 2026-11-03. Detalles: Execution #11283412; Proyecto: Aldrin-Megara; Usuario de ejecución: t000055; Fecha de inicio: 2026-11-03 19:24:51.019; Job referenciado: 001 - JOBs Mapeos/Job control errores mapeo; Paso fallido: Validacion constante presencia archivos flag (Aldrin-Megara) y 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara); 1 nodo fallido de 1.
- 2026-11-03 19:36 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema indicando que se han producido errores en el mapeo de producción en el job de Rundeck #11283601 del proyecto Aldrin-Megara. Detalles: Execution ID: 11283601; Proyecto: Aldrin-Megara; Usuario: t000055; Fecha de inicio: 2026-11-03 19:30:00.441; Job: 001 - JOBs Mapeos/Job control errores mapeo; Pasos afectados: Validacion constante presencia archivos flag (Aldrin-Megara) y 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara); 1 nodo fallido.
- 2026-11-03 19:41 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema indicando que ha fallado la ejecución #11283770 del job de mapeo en el entorno de producción. Detalles: Execution: #11283770; Proyecto: Aldrin-Megara; Job: 001 - JOBs Mapeos/Job control errores mapeo; Usuario: t000055; Fecha inicio: 2026-11-03 19:34:24.016; Paso fallido: 1 /Validacion constante presencia archivos flag (Aldrin-Megara); Nodes: 1 failed (1 of 1 100% Complete)
- 2026-11-03 19:46 — Correo automático — Correo nuevo en el hilo: Notificación automática de Rundeck informando sobre el fallo en la ejecución #11283966 del job de mapeo en el proyecto Aldrin-Megara. Detalles: Execution #11283966; Project: Aldrin-Megara; User: t000055; Job: 001 - JOBs Mapeos/Job control errores mapeo; Failed step: 00 - JOBs MEGARA Base/Main Job Megara; Fecha de inicio: 2026-11-03 19:40:30.021
- 2026-11-03 19:56 — Correo automático — Correo nuevo en el hilo: El sistema automático de alertas notifica un fallo en la ejecución #11284294 del job de Rundeck '001 - JOBs Mapeos/Job control errores mapeo'. Detalles: Execution: 11284294; Proyecto: Aldrin-Megara; Job: 001 - JOBs Mapeos/Job control errores mapeo; Usuario: t000055; Fecha de inicio: 2026-11-03 19:48:33.02; Pasos afectados: Validacion constante presencia archivos flag (Aldrin-Megara), 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara); Nodes: 1 failed.
- 2026-11-03 20:11 — Correo automático — Correo nuevo en el hilo: Se notifica un error automático de Rundeck en la ejecución del job de mapeo del proyecto Aldrin-Megara en el entorno de producción. Detalles: Execution ID: 11284508; Proyecto: Aldrin-Megara; Job: 001 - JOBs Mapeos/Job control errores mapeo; Usuario: t000055; Fecha inicio: 2026-11-03 19:55:36.029; Pasos: /Validacion constante presencia archivos flag (Aldrin-Megara), 00 - JOBs MEGARA Base/Main Job Megara (Aldrin-Megara); 1 nodo fallido de 1.
- 2026-11-03 20:16 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema de Rundeck que informa sobre un error en la ejecución del mapeo en producción. Detalles: Execution ID: 11284820; Proyecto: Aldrin-Megara; Job: 001 - JOBs Mapeos/Job control errores mapeo; Usuario: t000055; Fecha de inicio: 2026-11-03 20:09:45.021; Paso fallido: Validacion constante presencia archivos flag (Aldrin-Megara)
- 2026-11-03 20:26 — Correo automático — Correo nuevo en el hilo: Notificación automática del sistema indicando que ha fallado la ejecución del job en producción. Detalles: Execution ID: 11284820; Job: 001 - JOBs Mapeos/Job control errores mapeo; Proyecto: Aldrin-Megara; Usuario: t000055; Fecha inicio: 2026-11-03 20:09:45.021; Paso fallido: Validacion constante presencia archivos flag (Aldrin-Megara)

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
- 2026-11-03 17:36 — nuevo → Abierto — Correo automático
- 2026-11-04 16:02 — Abierto → Resuelto — Matheus Fransoni
- 2026-11-05 12:24 — Abierto → Resuelto — Marco Pichardo

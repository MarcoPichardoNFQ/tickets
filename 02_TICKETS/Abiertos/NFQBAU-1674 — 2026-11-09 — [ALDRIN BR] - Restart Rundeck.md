---
id: NFQBAU-1674
fecha_apertura: 2026-11-09
fecha_limite: 2026-11-12
fecha_resolucion:
estado: En curso
prioridad: Baja
responsable:
origen: email
referencia_origen: "[ALDRIN BR] - Restart Rundeck (2026-11-09)"
categoria:
  - Rundeck
entorno: []
sintoma: Falta de notificación sobre las reinicializaciones de la herramienta Rundeck.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-09 20:16
actualizado_por: Marco Pichardo
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marco P., de NFQ/SANCAC, solicita que se les notifique cada vez que se realice una reinicialización de la herramienta Rundeck. Esta petición se debe a requisitos de gobernanza de datos para que puedan realizar validaciones de consistencia e integridad.

Detalles: Herramienta: Rundeck; Acción: Reinicialización; Requisito: Notificación para validaciones de consistencia e integridad de datos.

## Histórico de interacciones

- 2026-11-09 17:51 — Correo automático — Marco P., de NFQ/SANCAC, solicita que se les notifique cada vez que se realice una reinicialización de la herramienta Rundeck. Esta petición se debe a requisitos de gobernanza de datos para que puedan realizar validaciones de consistencia e integridad.
- 2026-11-09 19:51 — Correo automático — Correo nuevo en el hilo: Marco P., consultor senior de NFQ, pregunta si pueden proceder con la configuración indicada en producción para realizar un reinicio de Rundeck todos los días a las 5h BRT. Detalles: Configuración de restart en Rundeck todos los días a las 5h BRT en el entorno p0.

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
- 2026-11-09 17:51 — nuevo → Abierto — Correo automático
- 2026-11-09 20:16 — Abierto → En curso — Marco Pichardo

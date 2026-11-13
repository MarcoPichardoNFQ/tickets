---
id: NFQBAU-1549
fecha_apertura: 2026-10-20
fecha_limite: 2026-10-20
fecha_resolucion: 2026-10-21
estado: Resuelto
prioridad: Alta
responsable: Marco Pichardo
origen: email
referencia_origen: "[Aldrin BR] Problema Carga (2026-10-20)"
categoria:
  - Rundeck
entorno:
  - Producción
sintoma: Las cargas en Rundeck no se ejecutan debido a que las llamadas vía API a Megara devuelven error 401.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-21 01:29
actualizado_por: Marco Pichardo
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marco P., consultor senior de NFQ, solicita abrir ticket tras detectarse a las 13:30 (hora de México) que las cargas de Rundeck están detenidas.
La investigación apunta a que Megara rechaza las solicitudes de la API por un posible cambio de contraseña, arrojando error 401 no solventado tras un reinicio.
El equipo intenta contactar con Eunice M. y con Herson para revisar los accesos a Megara y desbloquear el proceso.

Detalles: Hora de detección: 13:30 hrs (hora de México); Herramientas/Sistemas afectados: Rundeck, Megara; Error HTTP: 401 (no autorizado / posible cambio de contraseña de la API); Acciones previas: Megara fue reiniciado por el equipo de NTT sin resolver el problema

## Histórico de interacciones

- 2026-10-20 18:33 — Correo automático — Marco P., consultor senior de NFQ, solicita abrir ticket tras detectarse a las 13:30 (hora de México) que las cargas de Rundeck están detenidas.
La investigación apunta a que Megara rechaza las solicitudes de la API por un posible cambio de contraseña, arrojando error 401 no solventado tras un reinicio.
El equipo intenta contactar con Eunice M. y con Herson para revisar los accesos a Megara y desbloquear el proceso.

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
- 2026-10-20 18:33 — (vacío) → Abierto — Correo automático
- 2026-10-21 01:29 — Abierto → Resuelto — Marco Pichardo

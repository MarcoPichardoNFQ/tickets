---
id: NFQBAU-1608
fecha_apertura: 2026-10-30
fecha_limite: 2026-10-30
fecha_resolucion: 2026-11-03
estado: Resuelto
prioridad: Alta
responsable: Matheus Fransoni
origen: email
referencia_origen: Entrar na sala WR P1 (2026-10-30)
categoria: [Sala]
entorno: []
sintoma: Solicitud de asistencia a una sala de crisis (War Room P1) sin especificar el sistema o fallo concreto.
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

Marcos M., del área de tecnología, solicita a Matheus D. que se incorpore a la sala WR P1. No se proporciona contexto sobre el fallo ocurrido ni desde cuándo se presenta.

Detalles: Sala convocada: WR P1
Adjuntos del correo: image001.png, image002.png, image003.png

## Histórico de interacciones

- 2026-10-30 16:58 — Correo automático — Marcos M., del área de tecnología, solicita a Matheus D. que se incorpore a la sala WR P1. No se proporciona contexto sobre el fallo ocurrido ni desde cuándo se presenta.
- 2026-10-30 17:15 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador de NFQ, responde confirmando que está acudiendo a la sala de reunión indicada. No solicita ninguna acción adicional. Adjuntos del correo: image001.png, image002.png, image003.png

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
- 2026-10-30 16:58 — nuevo → Abierto — Correo automático
- 2026-10-30 17:01 — nuevo → Abierto — Matheus Fransoni
- 2026-11-03 09:59 — Abierto → Resuelto — Matheus Fransoni

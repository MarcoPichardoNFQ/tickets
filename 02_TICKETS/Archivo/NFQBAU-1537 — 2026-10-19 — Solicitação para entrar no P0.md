---
id: NFQBAU-1537
fecha_apertura: 2026-10-19
fecha_limite: 2026-10-19
fecha_resolucion: 2026-10-21
estado: Resuelto
prioridad: Alta
responsable: Deborah Bertoldo
origen: email
referencia_origen: Solicitação para entrar no P0 (2026-10-19)
categoria: [Sala]
entorno: []
sintoma: Solicitud para incorporarse a la llamada de atención de incidencia P0.
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
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Thiago A. solicita a Deborah B. que se una a la sesión de P0.
Adjunta un fichero.

Detalles: Solicitud de ingreso a P0
Adjuntos del correo: image001.png

## Histórico de interacciones

- 2026-10-19 15:31 — Correo automático — Thiago A. solicita a Deborah B. que se una a la sesión de P0.
Adjunta un fichero.
- 2026-10-19 15:32 — Correo automático — Correo nuevo en el hilo: Thiago A. solicita a Deborah B. que entre en la fase P0. Adjunta una captura. Detalles: Se solicita entrar en la fase P0. · Adjuntos del correo: image001.png
- 2026-10-19 15:32 — Correo automático — Correo nuevo en el hilo: Marco P., Senior Consultant, solicita que se añada a 'sancac' a los destinatarios principales. El correo original de Thiago A. preguntaba si Deborah B. podía entrar en P0. Adjunta capturas. Detalles: Añadir 'sancac' a los destinatarios principales. · Adjuntos del correo: image001.png
- 2026-10-19 15:33 — Correo automático — Correo nuevo en el hilo: Marco P., Senior Consultant de NFQ, solicita añadir al grupo 'sancac' a los destinatarios principales de un correo. Adjunta una captura. Detalles: Se solicita añadir 'sancac' a los destinatarios principales; Adjunta una captura de pantalla que no aporta información relevante para la solicitud. · Adjuntos del correo: image001.png
- 2026-10-20 10:32 — Correo automático — Correo nuevo en el hilo: Deborah Y., Developer de NFQ, solicita acceso a P0 para corregir un error de carga identificado a las 10:13 en la interface CA. Detalles: Error de carga a las 10:13 en la interface CA; Se solicita acceso a P0 para corregir el error.

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
- 2026-10-19 15:31 — nuevo → Abierto — Correo automático
- 2026-10-21 01:29 — Abierto → Resuelto — Marco Pichardo

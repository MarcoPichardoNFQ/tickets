---
id: NFQBAU-1645
fecha_apertura: 2026-11-05
fecha_limite: 2026-11-05
fecha_resolucion: 2026-11-05
estado: Resuelto
prioridad: Alta
responsable: Juan Antonio Gascón
origen: email
referencia_origen: Solicitação para entrar no P0 (2026-11-05)
categoria: [Sala]
entorno: []
sintoma: Solicitud de acceso o ingreso a la sala/reunión de incidencia P0.
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

Continúa el hilo del [NFQBAU-1537](../Archivo/NFQBAU-1537%20—%202026-10-19%20—%20Solicitação%20para%20entrar%20no%20P0.md), cerrado el 2026-10-21: no se reabre, se crea este. Thiago A. solicita a Deborah B. y Matheus F. del equipo de soporte el acceso para unirse a la llamada de P0.
No se detalla la causa raíz del incidente en el mensaje.
Adjunta capturas.

Detalles: Mensaje literal: 'Pode entrar em P0, por favor?'; Archivo adjunto image001.png con la imagen de la firma corporativa.
Adjuntos del correo: image001.png

## Histórico de interacciones

- 2026-11-05 15:26 — Correo automático — Continúa el hilo del [NFQBAU-1537](../Archivo/NFQBAU-1537%20—%202026-10-19%20—%20Solicitação%20para%20entrar%20no%20P0.md), cerrado el 2026-10-21: no se reabre, se crea este. Thiago A. solicita a Deborah B. y Matheus F. del equipo de soporte el acceso para unirse a la llamada de P0.
No se detalla la causa raíz del incidente en el mensaje.
Adjunta capturas.

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
- 2026-11-05 15:26 — nuevo → Abierto — Correo automático
- 2026-11-05 17:43 — Abierto → Resuelto — Marco Pichardo
- 2026-11-06 12:14 — nuevo → Resuelto — Matheus Fransoni

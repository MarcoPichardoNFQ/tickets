---
id: NFQBAU-1598
fecha_apertura: 2026-10-29
fecha_limite: 2026-10-29
fecha_resolucion: 2026-11-03
estado: Resuelto
prioridad: Alta
responsable: Deborah Bertoldo
origen: email
referencia_origen: Pode entrar em WR P1 (2026-10-29)
categoria: [Sala]
entorno: []
sintoma: Convocatoria a una War Room P1 para tratar un despliegue.
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

Ado G., del área de Tecnología, solicita conectarse a una War Room P1. Indica que el motivo de la reunión es tratar un despliegue.

Detalles: WR P1; tema: deploy
Adjuntos del correo: image.png, image.png, image.png

## Histórico de interacciones

- 2026-10-29 13:16 — Correo automático — Ado G., del área de Tecnología, solicita conectarse a una War Room P1. Indica que el motivo de la reunión es tratar un despliegue.
- 2026-10-29 13:16 — Correo automático — Correo nuevo en el hilo: Ado G., del área de tecnología, consulta sobre la posibilidad de realizar un despliegue (deploy) en WR P1.
No especifica detalles adicionales en el texto del mensaje.
Adjunta capturas. Detalles: Consulta sobre despliegue (deploy) y la ventana/versión WR P1 · Adjuntos del correo: image.png, image.png, image.png
- 2026-10-29 13:17 — Correo automático — Correo nuevo en el hilo: Matheus D., Developer III, indica que se está uniendo a la sala de crisis/deploy (WR P1). Se trata de una respuesta breve a una conversación previa sin aportar peticiones técnicas adicionales. Adjunta capturas. Detalles: Mención a WR P1 y deploy · Adjuntos del correo: image.png, image.png, image.png

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
- 2026-10-29 13:16 — nuevo → Abierto — Correo automático
- 2026-11-03 17:59 — Abierto → Resuelto — Matheus Fransoni

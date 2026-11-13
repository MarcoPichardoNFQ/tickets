---
id: NFQBAU-1540
fecha_apertura: 2026-10-19
fecha_limite: 2026-10-19
fecha_resolucion: 2026-10-21
estado: Resuelto
prioridad: Alta
responsable: Deborah Bertoldo
origen: email
referencia_origen: Boa tarde! Poderiam entrar em P0 (2026-10-19)
categoria: [Sala]
entorno: []
sintoma: Convocatoria para ingresar a la sala de crisis o puente de incidencia crítica (P0) sin detallar el componente afectado.
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

Marcela C., del área de Tecnología, solicita al equipo de soporte que se una a la sala de atención de una incidencia prioritaria (P0).
No se proporciona información sobre el fallo específico ni el sistema afectado.

Detalles: Solicitud de ingreso a puente/sala P0
Adjuntos del correo: image001.png, image002.png

## Histórico de interacciones

- 2026-10-19 17:37 — Correo automático — Marcela C., del área de Tecnología, solicita al equipo de soporte que se una a la sala de atención de una incidencia prioritaria (P0).
No se proporciona información sobre el fallo específico ni el sistema afectado.
- 2026-10-19 17:37 — Correo automático — Correo nuevo en el hilo: Marco P., Senior Consultant, acusa recibo de la petición de Marcela C., Tecnología, para activar un procedimiento P0. Marco P. adjunta capturas. Detalles: Adjunta capturas de pantalla (image001.png, image002.png). · Adjuntos del correo: image001.png, image002.png
- 2026-10-19 17:46 — Correo automático — Correo nuevo en el hilo: Marcela Y. de Sancac, Tecnología, solicita que se vuelva a P0. Adjunta capturas. Detalles: Se solicita volver a P0; adjunta dos capturas de pantalla (image001.png, image002.png) que no se describen en el cuerpo del correo. · Adjuntos del correo: image001.png, image002.png
- 2026-10-19 17:46 — Correo automático — Correo nuevo en el hilo: Marcela C., tecnología, solicita al equipo de soporte volver a entrar en la sala de incidencia P0. Marco P., consultor de NFQ, confirma que se suma a la petición. Adjunta capturas. Detalles: Solicitud de acceso y seguimiento en tiempo real a sesión de incidencia crítica P0. · Adjuntos del correo: image001.png, image002.png

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
- 2026-10-19 17:37 — nuevo → Abierto — Correo automático
- 2026-10-21 01:29 — Abierto → Resuelto — Marco Pichardo

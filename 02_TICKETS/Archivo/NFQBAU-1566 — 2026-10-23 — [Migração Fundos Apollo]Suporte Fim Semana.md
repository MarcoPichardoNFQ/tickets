---
id: NFQBAU-1566
fecha_apertura: 2026-10-23
fecha_limite: 2026-10-24
fecha_resolucion: 2026-10-26
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: "[Migração Fundos Apollo]Suporte Fim Semana (2026-10-23)"
categoria:
  - Otros
entorno: []
sintoma: No se describe un problema en un sistema específico, sino una solicitud de disponibilidad de soporte.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-26 17:26
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

Fernando A., de Tecnología, solicita disponibilidad del equipo de soporte para el fin de semana, sábado y domingo, para la migración de Fondos Apollo. Adjunta capturas.

Detalles: Solicita soporte el sábado de 13h a 23h; Si las actividades no concluyen el sábado, se necesitará el mismo período para el domingo de 13h a 23h.
Adjuntos del correo: image001.png, image002.png, image003.png

## Histórico de interacciones

- 2026-10-23 16:06 — Correo automático — Fernando A., de Tecnología, solicita disponibilidad del equipo de soporte para el fin de semana, sábado y domingo, para la migración de Fondos Apollo. Adjunta capturas.
- 2026-10-23 16:36 — Correo automático — Correo nuevo en el hilo: Marco P., de NFQ, confirma la cobertura de soporte solicitada por Fernando M. para el proceso de migración durante el fin de semana. Define la asignación de Deborah B. para el sábado y Enrique T. para el domingo. Adjunta capturas. Detalles: Proyecto: Migração Fundos Apollo; Horarios solicitados: de 13:00 a 23:00; Sábado 24/10: Deborah B.; Domingo 25/10: Enrique T. · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-10-23 16:36 — Correo automático — Correo nuevo en el hilo: Marco P., consultor sénior de NFQ, confirma la cobertura de soporte requerida para el fin de semana de migración de fondos Apollo. Informa que Deborah B., de NFQ, estará de guardia el sábado 24/10 y Enrique T., de NFQ, el domingo 25/10. Detalles: Migração Fundos Apollo; Cobertura definida para el sábado 24/10/2026 y domingo 25/10/2026 · Adjuntos del correo: image001.png, image002.png, image003.png

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
- 2026-10-23 16:06 — (vacío) → Abierto — Correo automático
- 2026-10-26 17:26 — Abierto → Resuelto — Marco Pichardo

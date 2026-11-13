---
id: NFQBAU-1523
fecha_apertura: 2026-10-16
fecha_limite: 2026-10-17
fecha_resolucion: 2026-10-21
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: "[Aldrin Br] Melhoria no sistema de tickets NFQ (2026-10-16)"
categoria: []
entorno: []
sintoma: Se solicita la implementación de un envío periódico de informes de tickets de proyecto.
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
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Correo automático'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Ricardo C., responsable del Proyecto Apollo, solicita que, aprovechando las mejoras en el sistema de tickets, se implemente el envío periódico (por ejemplo, semanal) de un informe con todos los tickets de proyecto (pendientes, concluidos y en curso). Esto es una continuación del correo de Marco P. sobre la mejora del sistema de tickets.

## Histórico de interacciones

- 2026-10-16 10:20 — Correo automático — Ricardo C., responsable del Proyecto Apollo, solicita que, aprovechando las mejoras en el sistema de tickets, se implemente el envío periódico (por ejemplo, semanal) de un informe con todos los tickets de proyecto (pendientes, concluidos y en curso). Esto es una continuación del correo de Marco P. sobre la mejora del sistema de tickets.
- 2026-10-16 19:57 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, confirma a Ricardo C., responsable del Proyecto Apollo, el envío semanal del informe de tickets los lunes.
El informe abarcará diversos estados de solicitud y métricas de AWT para revisiones e implantaciones. Detalles: Envío semanal del informe de tickets programado para los lunes; estados contemplados: Aberto, Em andamento, Revisão S3, Pendente de implantação em UAT, Testes S3 UAT, Pendente de implantação em PRD; inclusión de métricas de AWT referentes a revisiones e implantaciones en UAT y PRD · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-10-20 15:47 — Correo automático — Correo nuevo en el hilo: Ricardo C., del Proyecto Apollo, pregunta si el informe semanal de tickets, que Marco P., consultor senior, confirmó que se enviaría los lunes, ha comenzado a enviarse esta semana, ya que no lo ha recibido. Adjunta capturas. Detalles: El informe semanal de tickets debe incluir el estado de las solicitudes: Abierto; En andamento; Revisión S3; Pendiente de implantación en UAT; Testes S3 UAT; Pendiente de implantación en PRD. También debe incluir métricas AWT de revisiones e implantaciones en UAT y PRD. Adjunta capturas de pantalla. · Adjuntos del correo: image001.png, image002.png, image003.png

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
- 2026-10-16 10:20 — (vacío) → Abierto — Correo automático
- 2026-10-17 11:51 — Abierto → En curso — Ricardo Reyes
- 2026-10-21 01:29 — En curso → Resuelto — Marco Pichardo

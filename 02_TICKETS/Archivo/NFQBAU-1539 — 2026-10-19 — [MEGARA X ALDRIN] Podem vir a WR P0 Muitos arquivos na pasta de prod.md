---
id: NFQBAU-1539
fecha_apertura: 2026-10-19
fecha_limite: 2026-10-19
fecha_resolucion: 2026-10-21
estado: Resuelto
prioridad: Alta
responsable: Deborah Bertoldo
origen: email
referencia_origen: "[MEGARA X ALDRIN] Podem vir a WR P0? Muitos arquivos na pasta de prod (2026-10-19)"
categoria: [Sala]
entorno:
  - Producción
sintoma: Acumulación anómala de archivos en la carpeta de producción de la integración MEGARA y ALDRIN.
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

Ado S., del área de Tecnología, convoca al equipo a una sala de crisis WR P0 ante la presencia de demasiados archivos pendientes en la carpeta de producción. Adjunta capturas.

Detalles: Sistemas involucrados: MEGARA y ALDRIN; Incidencia clasificada como P0 con solicitud de ingreso a War Room; Exceso de archivos acumulados en el directorio de producción
Adjuntos del correo: image.png, image.png, image.png

## Histórico de interacciones

- 2026-10-19 16:48 — Correo automático — Ado S., del área de Tecnología, convoca al equipo a una sala de crisis WR P0 ante la presencia de demasiados archivos pendientes en la carpeta de producción. Adjunta capturas.
- 2026-10-19 16:48 — Correo automático — Correo nuevo en el hilo: Marco P., Senior Consultant, solicita registrar una petición para que Ado S., Tecnología, pueda ir a P0. El correo original de Ado S. ya había solicitado ir a P0. Adjunta capturas. Detalles: Se solicita registrar la visita de Ado S. a WR P0; El asunto del correo menciona 'Muitos arquivos na pasta de prod'. · Adjuntos del correo: image.png, image.png, image.png

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
- 2026-10-19 16:48 — (vacío) → Abierto — Correo automático
- 2026-10-21 01:29 — Abierto → Resuelto — Marco Pichardo

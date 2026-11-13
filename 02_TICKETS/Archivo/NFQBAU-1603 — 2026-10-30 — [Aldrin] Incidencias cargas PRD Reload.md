---
id: NFQBAU-1603
fecha_apertura: 2026-10-30
fecha_limite: 2026-10-31
fecha_resolucion: 2026-11-03
estado: Resuelto
prioridad: Media
responsable: Manuel Hervas
origen: email
referencia_origen: "[Aldrin] Incidencias cargas PRD Reload (2026-10-30)"
categoria:
  - Rundeck
entorno:
  - Producción
sintoma: Encolamiento de archivos en los procesos de carga.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-03 09:59
actualizado_por: Matheus Fransoni
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Continúa el hilo del [NFQBAU-1542](../Archivo/NFQBAU-1542%20—%202026-10-20%20—%20[Aldrin]%20Incidencias%20cargas%20PRD%20Reload.md), cerrado el 2026-10-21: no se reabre, se crea este. Manuel H., Developer I de NFQ, solicita realizar una recarga a partir de las 4:45 (horario de Brasil). La solicitud se debe a que se ha producido un encolamiento de archivos en las cargas. Adjunta capturas.

Detalles: Recarga solicitada a partir de las 4:45 (horario de Brasil); Causa: enfileiramento de arquivos nas cargas; Sistema Aldrin en PRD
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png

## Histórico de interacciones

- 2026-10-30 06:30 — Correo automático — Continúa el hilo del [NFQBAU-1542](../Archivo/NFQBAU-1542%20—%202026-10-20%20—%20[Aldrin]%20Incidencias%20cargas%20PRD%20Reload.md), cerrado el 2026-10-21: no se reabre, se crea este. Manuel H., Developer I de NFQ, solicita realizar una recarga a partir de las 4:45 (horario de Brasil). La solicitud se debe a que se ha producido un encolamiento de archivos en las cargas. Adjunta capturas.
- 2026-10-30 08:28 — Correo automático — Correo nuevo en el hilo: Renato L., de PR Serviços, comunica que ha ejecutado la recarga a partir de las 04:30 tras la incidencia de encolamiento de archivos. Solicita al equipo de soporte que valide si el proceso se encuentra correcto. Adjunta capturas. Detalles: Recarga ejecutada a partir de las 04:30; seguimiento de encolamiento previo de archivos en las cargas · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-11-02 04:46 — Correo automático — Correo nuevo en el hilo: Ismael B., desarrollador de NFQ, solicita ejecutar una recarga a partir de las 22:00 (horario de Brasilia) del día 31 de octubre.
Explica que Rundeck perdió una ejecución previa, otra quedó incompleta y se están detectando errores de mapeo.
Adjunta capturas. Detalles: Recarga solicitada a partir de las 22:00 (horario de Brasilia) del 31/10/2026; fallo de ejecución perdida en Rundeck; ejecución posterior incompleta; fallos de mapeo recientes · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-11-02 04:51 — Correo automático — Correo nuevo en el hilo: Ismael B., desarrollador de NFQ, solicita realizar una recarga a partir de las 22:00 (horario de Brasilia) del día 31 de octubre. Explica que se perdió una ejecución en Rundeck, otra quedó incompleta y se están produciendo fallos de mapeo. Adjunta capturas. Detalles: Recarga requerida a partir de las 22:00 (horario de Brasilia) del día 31/10/2026; Ejecución perdida en Rundeck; Ejecución posterior incompleta; Fallos de mapeo recientes en las cargas · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png

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
- 2026-10-30 06:30 — nuevo → Abierto — Correo automático
- 2026-11-03 09:59 — Abierto → Resuelto — Matheus Fransoni

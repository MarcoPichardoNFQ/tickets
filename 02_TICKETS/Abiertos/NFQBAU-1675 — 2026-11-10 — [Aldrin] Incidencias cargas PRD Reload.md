---
id: NFQBAU-1675
fecha_apertura: 2026-11-10
fecha_limite: 2026-11-11
fecha_resolucion: 2026-11-10
estado: Resuelto
prioridad: Media
responsable: Antonio Montoro
origen: email
referencia_origen: "[Aldrin] Incidencias cargas PRD Reload (2026-11-10)"
categoria:
  - Rundeck
entorno:
  - Producción
sintoma: El sistema Rundeck perdió una ejecución y una recarga posterior quedó incompleta.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-10 17:54
actualizado_por: Matheus Fransoni
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Continúa el hilo del [NFQBAU-1603](../Abiertos/NFQBAU-1603%20—%202026-10-30%20—%20[Aldrin]%20Incidencias%20cargas%20PRD%20Reload.md), cerrado el 2026-11-03: no se reabre, se crea este. Antonio M., consultor de datos, solicita realizar una recarga a partir de las 22:00 (horario de Brasilia) con datos del día 09. Explica que Rundeck perdió una ejecución y que posteriormente otra quedó incompleta. Adjunta capturas.

Detalles: Plataforma: Rundeck; Recarga solicitada desde las 22:00 (horario de Brasilia) del día 09-11-2026; Errores: ejecución perdida y ejecución posterior incompleta
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png

## Histórico de interacciones

- 2026-11-10 05:28 — Correo automático — Continúa el hilo del [NFQBAU-1603](../Abiertos/NFQBAU-1603%20—%202026-10-30%20—%20[Aldrin]%20Incidencias%20cargas%20PRD%20Reload.md), cerrado el 2026-11-03: no se reabre, se crea este. Antonio M., consultor de datos, solicita realizar una recarga a partir de las 22:00 (horario de Brasilia) con datos del día 09. Explica que Rundeck perdió una ejecución y que posteriormente otra quedó incompleta. Adjunta capturas.

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
- 2026-11-10 05:28 — nuevo → Abierto — Correo automático
- 2026-11-10 17:54 — Abierto → Resuelto — Matheus Fransoni

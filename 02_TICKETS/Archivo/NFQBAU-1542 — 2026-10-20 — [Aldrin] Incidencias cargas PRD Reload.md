---
id: NFQBAU-1542
fecha_apertura: 2026-10-20
fecha_limite: 2026-10-20
fecha_resolucion: 2026-10-21
estado: Resuelto
prioridad: Alta
responsable: Marco Pichardo
origen: email
referencia_origen: "[Aldrin] Incidencias cargas PRD Reload (2026-10-20)"
categoria:
  - Rundeck
entorno:
  - Producción
sintoma: Un job de carga está detenido debido a la falta del archivo MEGAACCOUNTING_IntraDay.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-26 14:23
actualizado_por: Ricardo Reyes
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Continúa el hilo del [NFQBAU-1521](../Abiertos/NFQBAU-1521%20—%202026-10-16%20—%20[Aldrin]%20Incidencias%20cargas%20PRD%20Reload.md), cerrado el 2026-10-16: no se reabre, se crea este. Juan Antonio G., consultor de NFQ, consulta por un job que se encuentra parado desde las 6:07 (horario de Brasil) por la falta del archivo MEGAACCOUNTING_IntraDay. Pide verificar por qué no ha llegado el fichero o si hay alguna tarea de mantenimiento en curso. Adjunta capturas.

Detalles: Job detenido desde las 06:07 am (horario de Brasil); Archivo faltante: MEGAACCOUNTING_IntraDay
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png

## Histórico de interacciones

- 2026-10-20 06:37 — Correo automático — Continúa el hilo del [NFQBAU-1521](../Abiertos/NFQBAU-1521%20—%202026-10-16%20—%20[Aldrin]%20Incidencias%20cargas%20PRD%20Reload.md), cerrado el 2026-10-16: no se reabre, se crea este. Juan Antonio G., consultor de NFQ, consulta por un job que se encuentra parado desde las 6:07 (horario de Brasil) por la falta del archivo MEGAACCOUNTING_IntraDay. Pide verificar por qué no ha llegado el fichero o si hay alguna tarea de mantenimiento en curso. Adjunta capturas.
- 2026-10-20 06:43 — Correo automático — Correo nuevo en el hilo: Juan Antonio G., consultor de NFQ, informa que el job ya se encuentra corriendo con normalidad.
No realiza ninguna nueva petición al estar la situación regularizada.
Adjunta capturas. Detalles: Job ejecutándose correctamente · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png

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
- 2026-10-20 06:37 — (vacío) → Abierto — Correo automático
- 2026-10-21 01:29 — Abierto → Resuelto — Marco Pichardo

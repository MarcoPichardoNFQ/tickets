---
id: NFQBAU-1536
fecha_apertura: 2026-10-19
fecha_limite: 2026-10-19
fecha_resolucion: 2026-10-21
estado: Resuelto
prioridad: Alta
responsable: Deborah Bertoldo
origen: email
referencia_origen: Entrar em P0 (2026-10-19)
categoria: [Sala]
entorno:
  - Producción
sintoma: Se solicita acceso o configuración de un entorno identificado como P0.
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

Continúa el hilo del [NFQBAU-1512](../Abiertos/NFQBAU-1512%20—%202026-10-05%20—%20Entrar%20em%20P0.md), cerrado el 2026-10-08: no se reabre, se crea este. Marcela C., de Tecnología, solicita al equipo de soporte entrar en P0. Adjunta capturas.

Detalles: Se solicita acceso o configuración del entorno P0; adjunta capturas de pantalla.
Adjuntos del correo: image001.png, image002.png

## Histórico de interacciones

- 2026-10-19 13:26 — Correo automático — Continúa el hilo del [NFQBAU-1512](../Abiertos/NFQBAU-1512%20—%202026-10-05%20—%20Entrar%20em%20P0.md), cerrado el 2026-10-08: no se reabre, se crea este. Marcela C., de Tecnología, solicita al equipo de soporte entrar en P0. Adjunta capturas.
- 2026-10-19 13:42 — Correo automático — Correo nuevo en el hilo: Deborah B., desarrolladora de NFQ, reporta un problema con la carga de datos de un informe XML referentes al 16/10.
Indica que los datos existen en la base aldrin pero tardan ~10 minutos en reflejarse en el portal, además de bloqueos identificados en S3.
Adjunta capturas. Detalles: Informe: relatório XML; Código: 4763; Fecha de los datos afectados: 16/10; Base de datos: aldrin; Latencia: ~10 min para cargar en el portal tras la carga; Bloqueos identificados en S3; adjunta capturas · Adjuntos del correo: image001.png, image002.png

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
- 2026-10-19 13:27 — nuevo → Abierto — Correo automático
- 2026-10-21 01:29 — Abierto → Resuelto — Marco Pichardo

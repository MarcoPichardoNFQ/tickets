---
id: NFQBAU-1611
fecha_apertura: 2026-10-31
fecha_limite: 2026-10-31
fecha_resolucion: 2026-11-03
estado: Resuelto
prioridad: Alta
responsable: Deborah Bertoldo
origen: email
referencia_origen: "[Implantação] Plantão NFQ (2026-10-31)"
categoria:
  - APIs
entorno: []
sintoma: El proceso de consumo de clientInstruction dejó de ejecutarse correctamente en el mapeo, afectando al flujo esperado.
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

Mykhael A. solicita al equipo de soporte el análisis y tratamiento de una incidencia surgida tras la implantación del 31/10/2026. Reporta que el proceso de consumo de clientInstruction falló en el mapeo y pide gestionar el caso con prioridad P0 por su impacto operacional. Adjunta capturas.

Detalles: Proceso afectado: consumo de clientInstruction; Error: falló la ejecución en el mapeo tras la implantación; Fecha de implantación: 31/10/2026; Prioridad solicitada: P0
Adjuntos del correo: image.png

## Histórico de interacciones

- 2026-10-31 11:22 — Correo automático — Mykhael A. solicita al equipo de soporte el análisis y tratamiento de una incidencia surgida tras la implantación del 31/10/2026. Reporta que el proceso de consumo de clientInstruction falló en el mapeo y pide gestionar el caso con prioridad P0 por su impacto operacional. Adjunta capturas.

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
- 2026-10-31 11:22 — nuevo → Abierto — Correo automático
- 2026-11-03 09:59 — Abierto → Resuelto — Matheus Fransoni

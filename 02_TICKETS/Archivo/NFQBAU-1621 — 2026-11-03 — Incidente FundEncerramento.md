---
id: NFQBAU-1621
fecha_apertura: 2026-11-03
fecha_limite: 2026-11-03
fecha_resolucion: 2026-11-09
estado: Resuelto
prioridad: Alta
responsable: Matheus Fransoni
origen: email
referencia_origen: Incidente FundEncerramento (2026-11-03)
categoria:
  - APIs
entorno:
  - Producción
sintoma: El servicio web de FundEncerramento en el entorno de producción presenta un incidente en WR.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-09 10:04
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

Lucas C., tecnología de PR Serviços, informa que se encuentran en WR en relación con el servicio de FundEncerramento y solicita unirse a una llamada para resolverlo.

Detalles: URL del servicio afectado: http://dh-fundencerramento.prd.aks.internal/fund/findAll?page_size=100000&page_number=0; Adjunta capturas (image.png).
Adjuntos del correo: image.png

## Histórico de interacciones

- 2026-11-03 18:16 — Correo automático — Lucas C., tecnología de PR Serviços, informa que se encuentran en WR en relación con el servicio de FundEncerramento y solicita unirse a una llamada para resolverlo.

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
- 2026-11-03 18:16 — nuevo → Abierto — Correo automático
- 2026-11-04 16:02 — Abierto → Resuelto — Matheus Fransoni
- 2026-11-05 17:43 — Abierto → En curso — Marco Pichardo
- 2026-11-06 12:14 — Resuelto → En curso — Matheus Fransoni
- 2026-11-09 10:04 — En curso → Resuelto — Matheus Fransoni

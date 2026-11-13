---
id: NFQBAU-1601
fecha_apertura: 2026-10-29
fecha_limite: 2026-10-29
fecha_resolucion: 2026-11-03
estado: Resuelto
prioridad: Alta
responsable: Deborah Bertoldo
origen: email
referencia_origen: "[ALDRIN BR] - Cargas Interfaces (2026-10-29)"
categoria:
  - Rundeck
entorno: []
sintoma: Posible fallo en la ejecución de la carga de la interfaz de Unit.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-03 10:05
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

Gustavo B. solicita soporte técnico para identificar un fallo en la carga de interfaces, concretamente en la carga de Unit.
Indica que se encuentran a la espera en la WR P0.
Adjunta un fichero.

Detalles: Interfaz afectada: Carga de Unit; Ubicación/Nivel indicado: WR P0
Adjuntos del correo: image.png

## Histórico de interacciones

- 2026-10-29 17:31 — Correo automático — Gustavo B. solicita soporte técnico para identificar un fallo en la carga de interfaces, concretamente en la carga de Unit.
Indica que se encuentran a la espera en la WR P0.
Adjunta un fichero.

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
- 2026-10-29 17:31 — nuevo → Abierto — Correo automático
- 2026-11-03 10:05 — Abierto → Resuelto — Matheus Fransoni

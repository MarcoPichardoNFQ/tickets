---
id: NFQBAU-1642
fecha_apertura: 2026-11-05
fecha_limite: 2026-11-06
fecha_resolucion: 2026-11-05
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: "[ALDRIN BR] Nuevos Excedidos - Incidências cargas PRD (2026-11-05)"
categoria:
  - Rundeck
entorno:
  - Producción
sintoma: Archivos de interfaz exceden su tamaño medio histórico en producción.
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
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Continúa el hilo del [NFQBAU-1575](../Archivo/NFQBAU-1575%20—%202026-10-27%20—%20[ALDRIN%20BR]%20Nuevos%20Excedidos%20-%20Incidências%20cargas%20PRD.md), cerrado el 2026-10-27: no se reabre, se crea este. Sancac B., soporte, informa que varios archivos de interfaz han excedido su tamaño medio histórico. El problema se manifiesta desde al menos el 23 de octubre de 2026, con picos de tamaño muy por encima del límite.

Detalles: Interfaces afectadas y total de veces excedido: DetailedCashFlow (359), SecurityPrice (162), PayableReceivable (130), CGCPosition (46), CashAccountingEntry (27), DetailedPriceCriterion (15), NetAssetValue (4), ValorizedPosition (4), FeesDetails (3), ClientInstruction (2); Ejemplos de archivos excedidos: DetailedPriceCriterion_1793819410456.xml (22817127 / 20971520, 8.80% excedido el 2026-11-04); DetailedCashFlow_1793818298562.xml (35403843 / 20971520, 68.82% excedido el 2026-11-04); PayableReceivable_1793693400502.xml (87628013 / 20971520, 317.84% excedido el 2026-11-03); CGCPosition_1793693436416.xml (41982809 / 20971520, 100.19% excedido el 2026-11-03); El problema se observa desde al menos el 23 de octubre de 2026.
Adjuntos del correo: 

## Histórico de interacciones

- 2026-11-05 04:52 — Correo automático — Continúa el hilo del [NFQBAU-1575](../Archivo/NFQBAU-1575%20—%202026-10-27%20—%20[ALDRIN%20BR]%20Nuevos%20Excedidos%20-%20Incidências%20cargas%20PRD.md), cerrado el 2026-10-27: no se reabre, se crea este. Sancac B., soporte, informa que varios archivos de interfaz han excedido su tamaño medio histórico. El problema se manifiesta desde al menos el 23 de octubre de 2026, con picos de tamaño muy por encima del límite.

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
- 2026-11-05 04:52 — nuevo → Abierto — Correo automático
- 2026-11-05 12:24 — Abierto → Resuelto — Marco Pichardo
- 2026-11-06 12:14 — nuevo → Resuelto — Matheus Fransoni

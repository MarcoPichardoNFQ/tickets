---
id: NFQBAU-1648
fecha_apertura: 2026-11-06
fecha_limite: 2026-11-07
fecha_resolucion: 2026-11-06
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: "[ALDRIN BR] Nuevos Excedidos - Incidências cargas PRD (2026-11-06)"
categoria:
  - Rundeck
entorno:
  - Producción
sintoma: Múltiples cargas de archivos de interfaz XML superan el tamaño promedio histórico en producción.
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

Continúa el hilo del [NFQBAU-1642](../Abiertos/NFQBAU-1642%20—%202026-11-05%20—%20[ALDRIN%20BR]%20Nuevos%20Excedidos%20-%20Incidências%20cargas%20PRD.md), cerrado el 2026-11-05: no se reabre, se crea este. Sancac S., soporte de NFQ, reporta que varios archivos de interfaz han superado su límite histórico de tamaño medio.
La incidencia se registra de forma continuada en diversas cargas desde el 16 de octubre de 2026.
Se detalla el desglose de los archivos e interfaces afectados para su seguimiento.

Detalles: Interfaces afectadas y veces excedidas: DetailedCashFlow (361), SecurityPrice (163), PayableReceivable (130), CGCPosition (46), CashAccountingEntry (27), DetailedPriceCriterion (16), NetAssetValue (4), ValorizedPosition (4), FeesDetails (3), ClientInstruction (2); Límite de tamaño base: 20.971.520 bytes; Ejemplos de ficheros excedidos: DetailedPriceCriterion_1793906664800.xml (23.98 MB, 14.38% excedido), DetailedCashFlow_1793905367861.xml (35.44 MB, 69.01% excedido), PayableReceivable_1793693400502.xml (87.62 MB, 317.84% excedido); Rango de fechas afectadas: del 2026-10-16 al 2026-11-05
Adjuntos del correo: 

## Histórico de interacciones

- 2026-11-06 04:46 — Correo automático — Continúa el hilo del [NFQBAU-1642](../Abiertos/NFQBAU-1642%20—%202026-11-05%20—%20[ALDRIN%20BR]%20Nuevos%20Excedidos%20-%20Incidências%20cargas%20PRD.md), cerrado el 2026-11-05: no se reabre, se crea este. Sancac S., soporte de NFQ, reporta que varios archivos de interfaz han superado su límite histórico de tamaño medio.
La incidencia se registra de forma continuada en diversas cargas desde el 16 de octubre de 2026.
Se detalla el desglose de los archivos e interfaces afectados para su seguimiento.

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
- 2026-11-06 04:46 — nuevo → Abierto — Correo automático
- 2026-11-06 12:14 — nuevo → Abierto — Matheus Fransoni
- 2026-11-06 12:32 — Abierto → Resuelto — Matheus Fransoni

---
id: NFQBAU-1575
fecha_apertura: 2026-10-27
fecha_limite: 2026-10-28
fecha_resolucion: 2026-10-27
estado: Resuelto
prioridad: Media
responsable: Juan Antonio Gascón
origen: email
referencia_origen: "[ALDRIN BR] Nuevos Excedidos - Incidências cargas PRD (2026-10-27)"
categoria:
  - Rundeck
entorno:
  - Producción
sintoma: Diversos archivos XML de interfaces de carga superan el límite de tamaño medio histórico configurado.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-06 15:31
actualizado_por: Ricardo Reyes
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Continúa el hilo del [NFQBAU-1530](../Abiertos/NFQBAU-1530%20—%202026-10-19%20—%20[ALDRIN%20BR]%20Nuevos%20Excedidos%20-%20Incidências%20cargas%20PRD.md), cerrado el 2026-10-26: no se reabre, se crea este. El equipo de soporte de Sancac B. informa de que múltiples archivos de interfaz han superado el tamaño medio histórico en las cargas de producción. Detallan los casos detectados entre el 7 y el 26 de octubre de 2026 agrupados por interfaz base y solicitan seguimiento.

Detalles: Límite establecido: 20971520 bytes; Interfaces afectadas: DetailedCashFlow (333 veces), SecurityPrice (157), PayableReceivable (118), CGCPosition (37), CashAccountingEntry (25), DetailedPriceCriterion (8), FeesDetails (3), ClientInstruction (2), NetAssetValue (2), ValorizedPosition (2); Fechas afectadas: del 2026-10-07 al 2026-10-26; Ejemplos de archivos: DetailedCashFlow_1793045914540.xml (35003576 bytes, +66.91%), PayableReceivable_1792991269088.xml (71280298 bytes, +239.89%), CGCPosition_1792991269421.xml (38125990 bytes, +81.80%), DetailedCashFlow_1792820808227.xml (70298755 bytes, +235.21%)
Adjuntos del correo: 

## Histórico de interacciones

- 2026-10-27 04:45 — Correo automático — Continúa el hilo del [NFQBAU-1530](../Abiertos/NFQBAU-1530%20—%202026-10-19%20—%20[ALDRIN%20BR]%20Nuevos%20Excedidos%20-%20Incidências%20cargas%20PRD.md), cerrado el 2026-10-26: no se reabre, se crea este. El equipo de soporte de Sancac B. informa de que múltiples archivos de interfaz han superado el tamaño medio histórico en las cargas de producción. Detallan los casos detectados entre el 7 y el 26 de octubre de 2026 agrupados por interfaz base y solicitan seguimiento.
- 2026-10-27 08:15 — Correo automático — Correo nuevo en el hilo: El equipo de soporte de Sancac B. reporta incidencias en las cargas de producción debido a archivos de interfaz que exceden el tamaño promedio histórico. Envía un desglose acumulado de archivos y métricas de exceso registradas durante el mes de octubre de 2026. Detalles: Interfaces afectadas y veces excedidas: DetailedCashFlow (333), SecurityPrice (157), PayableReceivable (120), CGCPosition (39), CashAccountingEntry (25), DetailedPriceCriterion (8), FeesDetails (3), ClientInstruction (2), NetAssetValue (2), ValorizedPosition (2); Límite de tamaño: 20971520 bytes; Archivos con mayor porcentaje de exceso: PayableReceivable_1793077574974.xml (74122702 bytes, +253.44%), DetailedCashFlow_1792820808227.xml (70298755 bytes, +235.21%), PayableReceivable_1792469256192.xml (69344182 bytes, +230.66%); Rango de fechas de eventos registrados: 2026-10-08 a 2026-10-27 · Adjuntos del correo: 

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
- 2026-10-27 04:45 — (vacío) → Abierto — Correo automático
- 2026-10-27 08:12 — Abierto → Revisión cliente — Ricardo Reyes
- 2026-10-27 16:26 — Revisión cliente → Resuelto — Matheus Fransoni

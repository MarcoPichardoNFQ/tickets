---
id: NFQBAU-1530
fecha_apertura: 2026-10-19
fecha_limite: 2026-10-20
fecha_resolucion: 2026-10-26
estado: Resuelto
prioridad: Media
responsable: Ismael Barranco
origen: email
referencia_origen: "[ALDRIN BR] Nuevos Excedidos - Incidências cargas PRD (2026-10-19)"
categoria:
  - Rundeck
entorno:
  - Producción
sintoma: Diversos archivos de interfaz superan el tamaño medio histórico permitido durante las cargas.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-26 17:25
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

Sancac, del equipo de soporte de Brasil, reporta que múltiples archivos de interfaz han excedido el tamaño medio histórico en las cargas de producción. Facilita el resumen de interfaces y el detalle de archivos afectados entre finales de septiembre y octubre de 2026 para su control.

Detalles: Límite de tamaño configurado: 20971520 bytes; Interfaces afectadas y número de excesos: DetailedCashFlow (307), SecurityPrice (152), PayableReceivable (109), CGCPosition (30), CashAccountingEntry (25), DetailedPriceCriterion (4), FeesDetails (3), ClientInstruction (2), NetAssetValue (2), ValorizedPosition (2); Rango de fechas de ficheros afectados: 2026-09-29 a 2026-10-19; Principales archivos excedidos: PayableReceivable_1792382905839.xml (64910793 bytes, +209.52%), PayableReceivable_1791950861539.xml (64014460 bytes, +205.24%), DetailedCashFlow_1791497260232.xml (58424216 bytes, +178.59%), DetailedPriceCriterion_1791708539781.xml (57023614 bytes, +171.91%)
Adjuntos del correo: 

## Histórico de interacciones

- 2026-10-19 08:26 — Correo automático — Sancac, del equipo de soporte de Brasil, reporta que múltiples archivos de interfaz han excedido el tamaño medio histórico en las cargas de producción. Facilita el resumen de interfaces y el detalle de archivos afectados entre finales de septiembre y octubre de 2026 para su control.
- 2026-10-20 08:26 — Correo automático — Correo nuevo en el hilo: El equipo de soporte de Sancac B. reporta incidencias en las cargas de producción debido a archivos de interfaz que sobrepasan el tamaño límite histórico.
Se facilita un resumen y desglose detallado de los archivos excedidos registrados entre finales de septiembre y el 20 de octubre de 2026. Detalles: Interfaces afectadas y total excedido: DetailedCashFlow (311), SecurityPrice (152), PayableReceivable (110), CGCPosition (31), CashAccountingEntry (25), DetailedPriceCriterion (5), FeesDetails (3), ClientInstruction (2), NetAssetValue (2), ValorizedPosition (2); Límite de tamaño: 20971520 bytes (20 MB); Rango de fechas afectadas: del 2026-09-30 al 2026-10-20; Ficheros con mayores excesos: PayableReceivable_1792469256192.xml (69344182 bytes, +230.66%), PayableReceivable_1792382905839.xml (64910793 bytes, +209.52%), PayableReceivable_1791950861539.xml (64014460 bytes, +205.24%), DetailedCashFlow_1791497260232.xml (58424216 bytes, +178.59%), DetailedPriceCriterion_1791708539781.xml (57023614 bytes, +171.91%) · Adjuntos del correo: 
- 2026-10-23 04:42 — Correo automático — Correo nuevo en el hilo: El equipo de soporte de Sancac Brasil reporta que diversos archivos de interfaz han superado el tamaño medio histórico permitido en las cargas de producción entre el 2 y el 22 de octubre.
Envían un desglose detallado con las interfaces afectadas, la cantidad de excesos y el porcentaje de superación del umbral para su seguimiento. Detalles: Límite de tamaño: 20971520 bytes (20 MB); Periodo reportado: del 2026-10-02 al 2026-10-22; Interfaces afectadas y total de excesos: DetailedCashFlow (321), SecurityPrice (156), PayableReceivable (113), CGCPosition (33), CashAccountingEntry (25), DetailedPriceCriterion (5), FeesDetails (3), ClientInstruction (2), NetAssetValue (2), ValorizedPosition (2); Archivos XML afectados: DetailedCashFlow, SecurityPrice, CGCPosition, PayableReceivable, DetailedPriceCriterion, CashAccountingEntry y FeesDetails, registrando sobrepasos de tamaño de hasta un 230.66% · Adjuntos del correo: 
- 2026-10-26 08:16 — Correo automático — Correo nuevo en el hilo: Notificación informativa que reporta archivos de diversas interfaces que han superado el límite de tamaño histórico establecido. Se desglosa el volumen y porcentaje de exceso registrado entre el 6 y el 26 de octubre de 2026, sin solicitar ninguna acción específica. Detalles: Interfaces afectadas y totales excedidos: DetailedCashFlow (329), SecurityPrice (156), PayableReceivable (118), CGCPosition (37), CashAccountingEntry (25), DetailedPriceCriterion (8), FeesDetails (3), ClientInstruction (2), NetAssetValue (2), ValorizedPosition (2); Límite de tamaño: 20971520 bytes (20 MB); Rango de fechas de los archivos reportados: 2026-10-06 al 2026-10-26 · Adjuntos del correo: 
- 2026-10-26 08:18 — Correo automático — Correo nuevo en el hilo: Notificación automática de alerta que informa sobre archivos de interfaz que han sobrepasado el límite de tamaño histórico establecido. El reporte detalla incidencias registradas entre el 7 y el 26 de octubre de 2026 sin solicitar ninguna acción específica. Detalles: Límite configurado: 20971520 bytes (20 MB); Interfaces base afectadas y conteo de excesos: DetailedCashFlow (329), SecurityPrice (156), PayableReceivable (118), CGCPosition (37), CashAccountingEntry (25), DetailedPriceCriterion (8), FeesDetails (3), ClientInstruction (2), NetAssetValue (2), ValorizedPosition (2); Archivos destacados con mayor exceso: PayableReceivable_1792991269088.xml (71280298 bytes, +239.89%), DetailedCashFlow_1792820808227.xml (70298755 bytes, +235.21%), CGCPosition_1792991269421.xml (38125990 bytes, +81.80%) · Adjuntos del correo: 

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
- 2026-10-19 08:26 — (vacío) → Abierto — Correo automático
- 2026-10-19 08:32 — Abierto → Revisión cliente — Ismael Barranco
- 2026-10-26 17:25 — Revisión cliente → Resuelto — Marco Pichardo

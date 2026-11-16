---
id: NFQBAU-1649
fecha_apertura: 2026-11-06
fecha_limite: 2026-11-07
fecha_resolucion: 2026-11-09
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: "Updates to OTCSwap extraction : SC-10631 (2026-11-06)"
categoria:
  - APIs
entorno:
  - UAT
sintoma: Se requiere realizar pruebas tras actualizar la configuración y los esquemas de campos en la extracción de OTCSwap.
solucion_corta: "Se actualizó la configuración y los esquemas de campos en la extracción de OTCSwap en el entorno PRE."
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-10 09:59
actualizado_por: Correo automático
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Continúa el hilo del [NFQBAU-1614](../Abiertos/NFQBAU-1614%20—%202026-11-03%20—%20Updates%20to%20OTCSwap%20extraction%20%20SC-10631.md), cerrado el 2026-11-06: no se reabre, se crea este. Oussema A., experto técnico de Vermeg, informa a Marcos M., del equipo de tecnología, que la configuración en el entorno PRE ha sido actualizada y se puede proceder con las pruebas.
La solicitud viene de incluir nuevos campos requeridos en la extracción de OTCSwap.
Adjunta capturas.

Detalles: Identificador: SC-10631; Entorno: PRE (PRE-PROD); Componente: Extracción OTCSwap (ficheros XSD y XML); Nuevos campos agregados: underlyingTradableAsset_code, haircutAdjustment; Las capturas muestran el archivo OTCSwap.xsd editado con los atributos opcionales underlyingTradableAsset_code (string) y haircutAdjustment (float) agregados en IndexLeg y EquityLeg
Adjuntos del correo: image014.gif, image001.png, image002.png, image004.png, image005.png, image006.png, image007.png, image016.png, image017.png, image811266.gif, image193489.png

## Histórico de interacciones

- 2026-11-06 13:44 — Correo automático — Continúa el hilo del [NFQBAU-1614](../Abiertos/NFQBAU-1614%20—%202026-11-03%20—%20Updates%20to%20OTCSwap%20extraction%20%20SC-10631.md), cerrado el 2026-11-06: no se reabre, se crea este. Oussema A., experto técnico de Vermeg, informa a Marcos M., del equipo de tecnología, que la configuración en el entorno PRE ha sido actualizada y se puede proceder con las pruebas.
La solicitud viene de incluir nuevos campos requeridos en la extracción de OTCSwap.
Adjunta capturas.
- 2026-11-10 09:57 — Correo automático — Resolución redactada automáticamente a partir del histórico; revisar.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Se incluyeron nuevos campos requeridos en la extracción de OTCSwap. Se agregaron los atributos opcionales underlyingTradableAsset_code y haircutAdjustment en IndexLeg y EquityLeg en el archivo OTCSwap.xsd. Se actualizó la configuración en el entorno PRE.

### Cómo se comprobó

No consta en el histórico.

### Con quién se habló

Oussema A., experto técnico de Vermeg; Marcos M., equipo de tecnología

### Servicios, jobs o tablas tocados

Extracción OTCSwap, ficheros XSD y XML, IndexLeg, EquityLeg

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-11-06 13:44 — nuevo → Abierto — Correo automático
- 2026-11-06 19:52 — Abierto → Pruebas cliente UAT — Marco Pichardo
- 2026-11-09 16:18 — Pruebas cliente UAT → Resuelto — Matheus Fransoni

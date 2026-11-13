---
id: NFQBAU-1614
fecha_apertura: 2026-11-03
fecha_limite: 2026-11-04
fecha_resolucion: 2026-11-06
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: "Updates to OTCSwap extraction : SC-10631 (2026-11-03)"
categoria:
  - APIs
entorno: []
sintoma: Actualización de la extracción de OTCSwap pendiente de aplicar en la actividad detenida.
solucion_corta: "Se recibieron los ficheros actualizados de Vermeg para reanudar la extracción de OTCSwap."
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-06 22:43
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

Marcos M., tecnología, avanza que se han recibido los ficheros actualizados de Vermeg para la extracción de OTCSwap y pide continuar con la actividad que estaba en espera desde el proveedor.

Detalles: Campos solicitados en XSD y XML: underlyingTradableAsset_code, haircutAdjustment; Fichero adjunto: VERMEG_ALDRIN_XSD_XML_OTCSwap_03112026.zip; SC-10631
Adjuntos del correo: image003.png, image579833.gif, image909458.png, image001.png, image002.png, image004.png, VERMEG_ALDRIN_XSD_XML_OTCSwap_03112026.zip

## Histórico de interacciones

- 2026-11-03 12:08 — Correo automático — Marcos M., tecnología, avanza que se han recibido los ficheros actualizados de Vermeg para la extracción de OTCSwap y pide continuar con la actividad que estaba en espera desde el proveedor.
- 2026-11-03 15:31 — Correo automático — Correo nuevo en el hilo: Matheus F., desarrollador de nfq, informa que retoman la actividad de extracción de OTCSwap (SC-10631). Marcos M., de tecnología, solicitó dar continuidad a la tarea que estaba pausada a la espera de los archivos XSD y XML actualizados. Adjunta capturas. Detalles: Identificador: SC-10631; Extracción: OTCSwap; Archivos involucrados: OTCSwap.xsd y XML; Nuevos campos integrados: underlyingTradableAsset_code (tipo string) y haircutAdjustment (tipo float); Las capturas muestran la definición del esquema OTCSwap.xsd con las modificaciones agregadas en las estructuras IndexLeg y EquityLeg. · Adjuntos del correo: image003.png, image579833.gif, image909458.png, image001.png, image002.png, image004.png
- 2026-11-06 11:58 — Correo automático — Correo nuevo en el hilo: Marcos M., Tecnología, solicita a Oussema A., Technical Expert de Vermeg, que se incluyan los nuevos campos 'underlyingTradableAsset_code' y 'haircutAdjustment' en la extracción OTCSwap para el entorno PRE-PROD. NFQ ya ha actualizado su entorno para estos campos. Oussema A. había adjuntado previamente el XSD y XML con los campos actualizados. La actividad estaba en espera de esta actualización. Adjunta capturas. Detalles: Nombres de campos: 'underlyingTradableAsset_code', 'haircutAdjustment'; Nombre de la extracción: 'OTCSwap'; Entorno: PRE-PROD; Se adjuntan XSD y XML con los campos actualizados; La captura de pantalla muestra el archivo OTCSwap.xsd con las líneas 18-19, 34-35 y 50-51 resaltadas, que corresponden a la adición de los atributos 'underlyingTradableAsset_code' y 'haircutAdjustment'. · Adjuntos del correo: image001.png, image002.png, image004.png, image005.png, image006.gif, image007.png
- 2026-11-06 21:06 — Correo automático — Resolución redactada automáticamente a partir del histórico; revisar.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Se recibieron los ficheros actualizados de Vermeg para la extracción de OTCSwap. NFQ retomó la actividad y actualizó su entorno para integrar los nuevos campos. Finalmente, se solicitó a Vermeg incluir los campos en PRE-PROD.

### Cómo se comprobó

No consta en el histórico.

### Con quién se habló

Marcos M., tecnología; Matheus F., desarrollador de nfq; Oussema A., Technical Expert de Vermeg

### Servicios, jobs o tablas tocados

Extracción de OTCSwap, OTCSwap.xsd, XML, IndexLeg, EquityLeg

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-11-03 12:08 — nuevo → Abierto — Correo automático
- 2026-11-06 04:58 — Abierto → En curso — Marco Pichardo
- 2026-11-06 05:27 — En curso → Revisión cliente — Marco Pichardo
- 2026-11-06 12:14 — Abierto → Revisión cliente — Matheus Fransoni
- 2026-11-06 12:38 — Revisión cliente → Resuelto — Matheus Fransoni

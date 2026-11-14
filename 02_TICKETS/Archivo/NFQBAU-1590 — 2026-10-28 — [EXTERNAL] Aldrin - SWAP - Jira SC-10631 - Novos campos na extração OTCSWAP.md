---
id: NFQBAU-1590
fecha_apertura: 2026-10-28
fecha_limite: 2026-10-29
fecha_resolucion: 2026-11-06
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: '[EXTERNAL] Aldrin - SWAP - Jira SC-10631 - Novos campos na extração "OTCSWAP" (2026-10-28)'
categoria:
  - APIs
entorno: []
sintoma: La extracción "OTCSWAP" no incluye los campos "basis" e "interestRate" necesarios para el producto Swap.
solucion_corta: "Se solicitó poner la demanda On Hold a la espera de un nuevo XSD."
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

Ricardo C., Proyecto Apollo, informa que Vermeg ha entregado el nuevo XSD con los campos "basis" e "interestRate" solicitados por Marcos M., Tecnología. Se pide a Fernando A., S3CACEIS, que priorice esta actividad en su plan de proyecto. Adjunta un fichero y capturas.

Detalles: Jira ID: SC-10631; Extracción afectada: OTCSWAP; Campos solicitados: "basis", "interestRate"; Adjunta un fichero ZIP con el XSD y XML actualizados para OTCSWAP; Captura 1 muestra el XSD "OTCSwap.xsd" con la definición de los atributos "basis" (string) e "interestRate" (float) resaltados; Captura 2 muestra la pantalla "Edit: OTC Swap Leg" donde se visualizan los campos "Basis" e "Interest Rate".
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image018.png, image019.png, image020.png, image021.png, image037260.gif, image728544.png, image005.png, image006.png, image007.png, VERMEG_ALDRIN_XSD_XML_OTCSwap_28102026.zip

## Histórico de interacciones

- 2026-10-28 15:01 — Correo automático — Ricardo C., Proyecto Apollo, informa que Vermeg ha entregado el nuevo XSD con los campos "basis" e "interestRate" solicitados por Marcos M., Tecnología. Se pide a Fernando A., S3CACEIS, que priorice esta actividad en su plan de proyecto. Adjunta un fichero y capturas.
- 2026-10-28 17:47 — Correo automático — Correo nuevo en el hilo: Ricardo C., del Proyecto Apollo, solicita poner la demanda "On Hold" porque se han solicitado dos campos adicionales para la extracción "OTCSWAP" y están a la espera de un nuevo XSD que los contemple. Adjunta capturas. Detalles: La extracción afectada es "OTCSWAP"; El Jira asociado es SC-10631; Se solicitan dos campos adicionales para el XSD de la extracción; Anteriormente, Vermeg había proporcionado un XSD con los campos "basis" e "interestRate"; Las capturas muestran el archivo "OTCSwap.xsd" con los campos "basis" e "interestRate" resaltados. · Adjuntos del correo: image005.png, image006.png, image007.png, image008.png, image009.gif, image010.png, image011.png, image012.png, image013.png, image014.png, image015.png, image016.png, image017.png
- 2026-11-06 21:06 — Correo automático — Resolución redactada automáticamente a partir del histórico; revisar.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Ricardo C. informó que Vermeg entregó el nuevo XSD con los campos 'basis' e 'interestRate' solicitados por Marcos M., Se pidió a Fernando A. que priorizara la actividad en su plan de proyecto., Posteriormente, Ricardo C. solicitó poner la demanda 'On Hold' porque se pidieron dos campos adicionales y se espera un nuevo XSD.

### Cómo se comprobó

No consta en el histórico.

### Con quién se habló

Ricardo C., Proyecto Apollo; Marcos M., Tecnología; Fernando A., S3CACEIS

### Servicios, jobs o tablas tocados

OTCSWAP

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-10-28 15:01 — nuevo → Abierto — Correo automático
- 2026-11-04 15:46 — Abierto → En curso — Matheus Fransoni
- 2026-11-06 05:27 — En curso → Revisión cliente — Marco Pichardo
- 2026-11-06 12:14 — En curso → Revisión cliente — Matheus Fransoni
- 2026-11-06 12:38 — Revisión cliente → Resuelto — Matheus Fransoni

---
id: NFQBAU-1576
fecha_apertura: 2026-10-27
fecha_limite: 2026-10-30
fecha_resolucion:
estado: Pruebas cliente UAT
prioridad: Baja
responsable: Marco Pichardo
origen: email
referencia_origen: New Aldrin Extraction + ValorizedPosition update - JIra SC-10594 (2026-10-27)
categoria:
  - APIs
entorno: [UAT]
sintoma: Se requiere la implementación y adecuación de las extracciones SettledPrice, HtmPrice y ValorizedPosition.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-04 15:40
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

Ricardo C., responsable del Proyecto Apollo, solicita priorizar junto a los PMOs la incorporación de nuevas extracciones y ajustes de tributación para los proyectos SAM y carteras tributadas según el Jira SC-10594. Adjunta capturas y ficheros.

Detalles: Jira SC-10594; Extracción SettledPrice: nuevo mapeo utilizando el campo Market Yield y clave primaria pk; Extracción HtmPrice: clave primaria pk; Extracción ValorizedPosition: inclusión de información de tributación con los campos totalValueBeforeTax y taxAmount; La captura de pantalla muestra el archivo ValorizedPosition.xsd agregando los atributos taxAmount y totalValueBeforeTax
Adjuntos del correo: image003.png, image422157.gif, image403434.png, image001.png, image002.png, image004.png, VERMEG_ALDRIN_XSD_XML_HtmPrice_23102026.zip, VERMEG_ALDRIN_XSD_XML_SettledPrice_23102026.zip, VERMEG_ALDRIN_XSD_XML_ValorizedPosition_23102026.zip

## Histórico de interacciones

- 2026-10-27 10:15 — Correo automático — Ricardo C., responsable del Proyecto Apollo, solicita priorizar junto a los PMOs la incorporación de nuevas extracciones y ajustes de tributación para los proyectos SAM y carteras tributadas según el Jira SC-10594. Adjunta capturas y ficheros.
- 2026-10-30 14:11 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador de nfq, envía el código modificado para la extracción Valorized Position según lo acordado. Solicita a Marcos M. la revisión y validación del desarrollo para verificar que cumple con los requerimientos. Adjunta un fichero. Detalles: Jira SC-10594; Entrega de modificaciones en el código de la extracción Valorized Position; Ficheros adjuntos: function.sql, ValorizedPosition.xsd, stg.sql, query_valorizedposition.sql y trf.sql; La captura de pantalla muestra en ValorizedPosition.xsd la adición de los atributos opcionales 'taxAmount' y 'totalValueBeforeTax' de tipo float · Adjuntos del correo: image003.png, image422157.gif, image403434.png, image001.png, image002.png, image004.png, function.sql, ValorizedPosition.xsd, stg.sql, query_valorizedposition.sql, trf.sql
- 2026-10-30 14:17 — Correo automático — Correo nuevo en el hilo: Marcos M. confirma la validación en UAT. Matheus D. había solicitado validar el código adjunto para la alteración en Valorized Position. Ricardo C., del Proyecto Apollo, había detallado las modificaciones solicitadas en el Jira SC-10594: una nueva extracción SettledPrice, la extracción HtmPrice y la adecuación de Valorized Position para la lectura de información de tributación. Oussema A. había adjuntado los XML y XSD para las nuevas extracciones y la actualización de Valorized Position con dos nuevos campos. Adjunta capturas. Detalles: Jira SC-10594; Nueva extracción SettledPrice: usar campo "Market Yield" en lugar de "Yield To Maturity"; Extracción HtmPrice; Extracción Valorized Position: adecuación para lectura de información de tributación; La extracción Valorized Position se actualiza con los campos "totalValueBeforeTax" y "taxAmount" (tipo xs:float); La captura de pantalla muestra el XSD de ValorizedPosition con los nuevos atributos "taxAmount" y "totalValueBeforeTax". · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.gif, image006.png
- 2026-10-30 16:42 — Correo automático — Correo nuevo en el hilo: Matheus D., Developer III de NFQ, solicita al equipo de soporte compilar el código adjunto en el entorno UAT. La modificación es para la extracción de Aldrin, permitiendo la lectura de información de tributación. Se adjuntan capturas y varios ficheros con el código y el plan de rollback. Detalles: Host: psqlcerdatahub01.postgres.database.cloud.corp; Descripción de la cambio: Adecuación de la extracción para lectura de las informaciones de tributación; Servicios afectados: Database; Plan de rollback: Ejecución del archivo ROLLBACK.sql adjunto; Impacto al negocio: Inserción de informaciones en Aldrin; Ficheros adjuntos: ValorizedPosition.xsd, query_valorizedposition.sql, ROLLBACK.sql; Capturas de pantalla muestran el fichero ValorizedPosition.xsd con la adición de los atributos taxAmount y totalValueBeforeTax. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.gif, image006.png, image.png, ValorizedPosition.xsd, query_valorizedposition.sql, ROLLBACK.sql
- 2026-11-03 13:18 — Correo automático — Correo nuevo en el hilo: Marcos M. de PR Serviços reenvía una solicitud de Matheus D. de NFQ para compilar código adjunto en UAT. El cambio es una adaptación de la extracción de datos para incluir información de tributación en Aldrin. Se adjuntan capturas y un fichero. Detalles: Host de la base de datos: psqlcerdatahub01.postgres.database.cloud.corp; Descripción del cambio: Adecuación de la extracción para lectura de información de tributación; Servicios afectados: Database; Plan de rollback: Ejecución del archivo ROLLBACK adjunto; No habrá indisponibilidad; Impacto al negocio: Inserción de información en Aldrin; La captura de pantalla muestra un archivo ValorizedPosition.xsd con la adición de dos atributos: taxAmount y totalValueBeforeTax, ambos de tipo xs:float y opcionales; Kleverson B. indica que Marcos M., Ado G., Ricardo C. o David pueden aprobar ejecuciones en UAT; El archivo a compilar es query_valorizedposition.sql. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.gif, image007.png
- 2026-11-03 16:02 — Correo automático — Correo nuevo en el hilo: Marcos M., tecnología de PR Serviços, solicita un retorno sobre la ejecución de una petición de NFQ. Matheus D. F., desarrollador de NFQ, había pedido compilar código adjunto en UAT para adecuar la extracción de Aldrin y la tabla ValorizedPosition para incluir información de tributación. Deborah Y. B., desarrolladora de NFQ, aclaró que el archivo query_valorizedposition.sql contiene todas las queries necesarias. Marcos M. también preguntó sobre un archivo trf para la inclusión de nuevas columnas en la tabla position. Adjunta capturas. Detalles: Se solicita compilar código adjunto en UAT; Host: psqlcerdatahub01.postgres.database.cloud.corp; Descripción del cambio: Adecuación de la extracción para lectura de información de tributación; Servicios afectados: Database; Impacto al negocio: Inserción de información en Aldrin; Plan de rollback: Ejecución del archivo ROLLBACK adjunto; El archivo query_valorizedposition.sql contiene todas las queries necesarias; Se menciona un archivo trf para la inclusión de dos nuevas columnas en la tabla position; Las capturas muestran que el proceso de aprobación para UAT ha cambiado y que Marcos M., Ado G., Ricardo C. o David pueden aprobar; Una captura de ValorizedPosition.xsd muestra la adición de dos atributos: taxAmount (tipo float, opcional) y totalValueBeforeTax (tipo float, opcional). · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.gif, image007.png

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
- 2026-10-27 10:15 — nuevo → Abierto — Correo automático
- 2026-11-04 15:40 — Abierto → Pruebas cliente UAT — Matheus Fransoni

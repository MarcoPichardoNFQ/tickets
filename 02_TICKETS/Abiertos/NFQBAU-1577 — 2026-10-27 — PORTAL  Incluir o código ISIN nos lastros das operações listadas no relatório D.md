---
id: NFQBAU-1577
fecha_apertura: 2026-10-27
fecha_limite: 2026-10-28
fecha_resolucion:
estado: Revisión cliente
prioridad: Baja
responsable: Deborah Bertoldo
origen: email
referencia_origen: PORTAL | Incluir o código ISIN nos lastros das operações listadas no relatório Detalhado de Estoque de Renda Fixa (2026-10-27)
categoria:
  - Qlik
entorno:
  - UAT
sintoma: El informe 'Detalhado de Estoque de Renda Fixa' no incluye el código ISIN en sus operaciones y presenta un error al intentar generarse.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-13 00:42
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

Jefferson N., de PR Serviços, solicita asistencia técnica para añadir el código ISIN en el informe de Renda Fixa y solucionar su generación. La petición proviene de un seguimiento iniciado en mayo de 2026 que quedó pendiente en el entorno de pruebas. Adjunta capturas.

Detalles: Informe afectado: Detalhado de Estoque de Renda Fixa [GFFQ]; Requerimiento: inclusión del código ISIN en los lastres de las operaciones; Mensaje de error literal mostrado: 'Falha ao gerar relatório. Tente novamente mais tarde. Detalhado de Estoque de Renda Fixa [GFFQ]'; Descripción de capturas: la pantalla del portal S3 Caceis muestra la sección de informes del activo con un banner de error emergente en rojo al intentar generar el informe para carteras como CUST4157 y ASSET DODO.
Adjuntos del correo: image001.png, image002.jpg, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png

## Histórico de interacciones

- 2026-10-27 11:32 — Correo automático — Jefferson N., de PR Serviços, solicita asistencia técnica para añadir el código ISIN en el informe de Renda Fixa y solucionar su generación. La petición proviene de un seguimiento iniciado en mayo de 2026 que quedó pendiente en el entorno de pruebas. Adjunta capturas.
- 2026-10-27 16:06 — Correo automático — Correo nuevo en el hilo: Deborah B., desarrolladora de NFQ, remite al equipo de soporte el seguimiento sobre la inclusión del código ISIN en el informe Detalhado de Estoque de Renda Fixa. Informa que la solicitud se gestionará mediante el ticket NFQBAU1577. Adjunta capturas. Detalles: Informe afectado: Detalhado de Estoque de Renda Fixa; Referencia de ticket: NFQBAU1577; Error en pantalla: 'Falha ao gerar relatório. Tente novamente mais tarde. Detalhado de Estoque de Renda Fixa [GFFQ]'; Cambio requerido: incluir código ISIN en los lastros de las operaciones; Las capturas muestran errores al intentar generar el informe para carteras/fondos como ASSET DODO y CUST4157, así como una vista previa del informe con la columna ISIN requerida · Adjuntos del correo: image001.png, image002.jpg, image003.png, image004.png, image005.png, image006.png, image007.png, image010.png, image008.png, image009.png
- 2026-10-27 16:11 — Correo automático — Correo nuevo en el hilo: Jefferson A., del cliente, pregunta por la previsión de entrega para la inclusión del código ISIN en el informe "Detalhado de Estoque de Renda Fixa". Deborah Y., developer de NFQ, había confirmado previamente la apertura del ticket NFQBAU1577 para esta solicitud. El informe había presentado errores al generarse en UAT y no mostraba el campo ISIN. Adjunta capturas. Detalles: Nombre del informe: "Detalhado de Estoque de Renda Fixa"; Campo solicitado: código ISIN; Mensaje de error previo: "Falha ao gerar relatório. Tente novamente mais tarde. Detalhado de Estoque de Renda Fixa (GFFQ)"; Entorno afectado: UAT; Ticket asociado: NFQBAU1577; Capturas de pantalla muestran la interfaz de generación de informes del portal S3 Caceis Investor Services, con el informe "Detalhado de Estoque de Renda Fixa" seleccionado y el mensaje de error al intentar generarlo para fechas como 26/05/2026, 16/04/2026 y 27/04/2026, y grupos de carteras CUST4157 y Private. · Adjuntos del correo: ~WRD0000.jpg, image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png
- 2026-10-27 17:26 — Correo automático — Correo nuevo en el hilo: Matheus D., Developer III de NFQ, informa a Jefferson A. de PR Serviços que han generado los informes en Producción y UAT sin problemas de formato o datos. Pregunta en qué posición debe insertarse el código ISIN en el informe "Detalhado de Estoque de Renda Fixa" y adjunta capturas y dos ficheros PDF. También indica que se necesita la aprobación de Kleverson B. de S3 Caceis para la modificación. Detalles: Nombre del informe: Detalhado de Estoque de Renda Fixa; Campo a incluir: código ISIN; Se solicita la posición exacta para la inserción del campo ISIN; Matheus D. confirma que no se observaron problemas de formato o quiebre de datos al generar los informes en Producción y UAT; Se adjuntan 11 capturas de pantalla y 2 ficheros PDF (uno de UAT y otro de PRD del informe); Se requiere la aprobación de Kleverson B. para la modificación del contenido del informe; Se adjunta una imagen con el orden actual de los campos del informe. · Adjuntos del correo: ~WRD0000.jpg, image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image.png, Detalhado de Estoque de Renda Fixa UAT20261027140250.pdf, Detalhado de Estoque de Renda Fixa PRD20261027165251.pdf
- 2026-10-27 18:06 — Correo automático — Correo nuevo en el hilo: Matheus D., Developer III, informa que los informes en Producción y UAT no presentan errores de datos ni formato. Pregunta a Jefferson A., de PR Serviços, en qué posición debe insertarse el campo 'código ISIN' y solicita la aprobación de Kleverson B. para la modificación. Jefferson A. responde adjuntando el modelo en formato XLS y PDF. Adjunta capturas. Detalles: Informe afectado: 'Detalhado de Estoque de Renda Fixa'; Campo a incluir: 'código ISIN'; Matheus D. adjunta la orden actual de los campos del informe; Jefferson A. adjunta el modelo en XLS y PDF mostrando la posición deseada para el campo ISIN. · Adjuntos del correo: ~WRD0002.jpg, image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png
- 2026-10-28 14:18 — Correo automático — Correo nuevo en el hilo: Matheus F., desarrollador de NFQ, consulta a Jefferson N., de PR Serviços, si se debe mantener el campo 'Tipo' en la versión PDF del informe Detalhado de Estoque de Renda Fixa tras la inclusión del código ISIN.
La modificación está en proceso a la espera del visto bueno de Kleverson B., de S3 Caceis. Adjunta capturas. Detalles: Informe afectado: Detalhado de Estoque de Renda Fixa; Código de ticket de trabajo: NFQBAU1577; Campo a incluir: ISIN; Campo en consulta: 'Tipo' (presente en PDF); Las capturas muestran las vistas del informe en Excel y PDF con campos como Operação, Tipo, Emitente, Condição, ISIN, Emissão, Vencimento · Adjuntos del correo: ~WRD0000.jpg, image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png, image.png
- 2026-10-28 14:26 — Correo automático — Correo nuevo en el hilo: Jefferson N., de PR Serviços, informa a Matheus D., de NFQ, que el campo ISIN ya está presente en el informe 'Detalhado de Estoque de Renda Fixa' y no debe ser modificado. Matheus D. había consultado previamente sobre la presencia de un campo 'Tipo' adicional en la versión PDF del informe y la inclusión del código ISIN. Adjunta capturas. Detalles: Informe afectado: 'Detalhado de Estoque de Renda Fixa'; Campo 'ISIN' ya existe en el informe; Matheus D. consultó sobre la presencia de un campo 'Tipo' adicional en la versión PDF del informe; Se adjuntan capturas del informe en formato XLS y PDF mostrando la columna 'ISIN' y 'Tipo'. · Adjuntos del correo: ~WRD0001.jpg, image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png, image011.png
- 2026-11-12 21:06 — Correo automático — Correo nuevo en el hilo: Marco P., consultor senior de NFQ, reporta la imposibilidad de acceder a NPrinting PRD tanto por URL como desde las aplicaciones de Qlik.
Solicita al equipo de soporte que revise la herramienta para verificar si hay algún problema.
Adjunta capturas. Detalles: Servicio afectado: NPrinting PRD; Métodos de acceso fallidos: URL directa y conexión a través de aplicaciones Qlik; Las capturas de pantalla muestran modelos del informe 'Detalhado de Estoque de Renda Fixa' con el campo ISIN destacado. · Adjuntos del correo: image003.png, image001.png, image007.png, image004.jpg, image006.png, image005.png, image002.png, image008.png
- 2026-11-12 21:08 — Correo automático — Correo nuevo en el hilo: Marco P., consultor sénior en NFQ, reporta que no pueden acceder a NPrinting en producción desde hoy, solicitando verificar si el entorno funciona correctamente. Detalles: Herramienta afectada: NPrinting PRD; Fallo: No es posible realizar login ni mediante URL directa ni por conexión desde aplicaciones Qlik; Adjunta capturas · Adjuntos del correo: image003.png, image001.png, image007.png, image004.jpg, image006.png, image005.png, image002.png, image008.png
- 2026-11-12 23:18 — Correo automático — Correo nuevo en el hilo: Marco P., consultor senior de NFQ, comunica que ya se realizaron los ajustes necesarios para incluir el código ISIN en el informe. Pide que se valide el nuevo formato planteado. Adjunta capturas. Detalles: Informe: Detalhado de Estoque de Renda Fixa; Modificación: inclusión del campo/columna ISIN; Las capturas adjuntas muestran el diseño del informe en formato PDF y hoja de cálculo Excel con la columna ISIN resaltada en amarillo · Adjuntos del correo: image003.png, image001.png, image007.png, image004.jpg, image006.png, image005.png, image002.png, image008.png

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
- 2026-10-27 11:32 — nuevo → Abierto — Correo automático
- 2026-10-27 16:21 — Abierto → En curso — Matheus Fransoni
- 2026-11-05 12:24 — En curso → Abierto — Marco Pichardo
- 2026-11-06 12:14 — En curso → Abierto — Matheus Fransoni
- 2026-11-12 20:42 — Abierto → En curso — Marco Pichardo
- 2026-11-13 00:42 — En curso → Revisión cliente — Marco Pichardo

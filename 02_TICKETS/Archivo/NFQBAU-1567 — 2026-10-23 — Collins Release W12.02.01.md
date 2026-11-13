---
id: NFQBAU-1567
fecha_apertura: 2026-10-23
fecha_limite: 2026-10-24
fecha_resolucion: 2026-10-26
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: Collins Release W12.02.01 (2026-10-23)
categoria:
  - Otros
entorno:
  - Producción
sintoma: Ningún fallo reportado; se solicita la subida de un paquete de release a producción como dependencia para el producto SWAP.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-26 17:26
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

Ado S., tecnología, solicita que se suba a producción el paquete de release correspondiente ya que es una dependencia necesaria para el funcionamiento del producto SWAP en la integración MEGARA X ALDRIN.

Detalles: Paquete de release: Collins Release W12.02.01; Integración afectada: MEGARA X ALDRIN; Producto dependiente: SWAP; adjunta capturas
Adjuntos del correo: image.png, image706531.gif, image066259.png, image001.png, image002.png, image003.png, image.png, image.png, image.png

## Histórico de interacciones

- 2026-10-23 16:14 — Correo automático — Ado S., tecnología, solicita que se suba a producción el paquete de release correspondiente ya que es una dependencia necesaria para el funcionamiento del producto SWAP en la integración MEGARA X ALDRIN.
- 2026-10-23 16:21 — Correo automático — Correo nuevo en el hilo: Ado S. informa que se ha abierto un ticket para la solicitud de despliegue del paquete Collins Release W12.02.01 a producción. Esta acción es crítica para el producto SWAP y la integración MEGARA X ALDRIN. Ado S. y Oussema A. han alineado esta necesidad. Adjunta capturas. Detalles: Paquete: Collins Release W12.02.01; Dependencia para el funcionamiento del producto SWAP en la integración MEGARA X ALDRIN; El paquete se encuentra en Microsoft Azure Storage; Adjunta capturas de pantalla del Azure Storage mostrando los archivos 'Installation Guide ReleaseCollinsW 12.02.01.docx' y 'ReleaseCollinsW 12.02.01.docx' en la ruta 'megara-files/PRE/ReleaseCollinsWRelease12.02.01'. · Adjuntos del correo: image.png, image706531.gif, image066259.png, image001.png, image002.png, image003.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png
- 2026-10-23 16:36 — Correo automático — Correo nuevo en el hilo: Pedro C., soporte de TI de NTT DATA, solicita la aprobación de Kleverson B. o Mauricio L. para ejecutar el despliegue de la versión Collins W12.02.01. Informa que el despliegue consiste en un script y requerirá la parada de todos los módulos del entorno de producción. Adjunta capturas. Detalles: Release: Collins Release W12.02.01; Acción: Ejecución de script de despliegue; Impacto: Parada de todos los módulos de Megara PRD; Ruta Azure Storage: megara-files/PRE/ReleaseCollinsWRelease12.02.01; Ficheros de la release: carpetas 01DBScript, Installation Guide ReleaseCollinsW 12.02.01.docx y ReleaseCollinsW 12.02.01.docx · Adjuntos del correo: image.png, image706531.gif, image066259.png, image001.png, image002.png, image003.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png
- 2026-10-23 16:37 — Correo automático — Correo nuevo en el hilo: Pedro G., analista de soporte de IT, solicita la aprobación de Kleverson B. y Mauricio L. para el despliegue de un script en producción. Ado S., de Tecnología, había solicitado previamente el despliegue de un paquete, indicando que es una dependencia para el funcionamiento del producto SWAP en la integración MEGARA X ALDRIN. Adjunta capturas. Detalles: Despliegue de la versión Collins Release W12.02.01; Se trata de un script que requiere parar todos los módulos del sistema Megara PRD; Es una dependencia para que el producto SWAP funcione en la integración MEGARA X ALDRIN; Adjunta capturas de pantalla que muestran un Azure Storage con los archivos 'Installation Guide ReleaseCollinsW 12.02.01.docx', 'ReleaseCollinsW 12.02.01.docx' y una carpeta '01DBScript'. · Adjuntos del correo: image.png, image706531.gif, image066259.png, image001.png, image002.png, image003.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png
- 2026-10-23 16:41 — Correo automático — Correo nuevo en el hilo: Ado S., tecnología, solicita a Oussema A., de Vermeg, que reenvíe el paquete de la release Collins W12.02.01 a NTT porque ya no está disponible en el almacenamiento. Pedro G., analista de soporte de NTT, evaluará el impacto y definirá la ventana de despliegue. El despliegue es un script que requiere parar todos los módulos de Megara PRD y es una dependencia para que el producto SWAP funcione en la integración MEGARA X ALDRIN. Adjunta capturas. Detalles: Nombre de la release: Collins Release W12.02.01; El paquete no está disponible en STORAGE; El despliegue es un script; Requiere parar todos los módulos del sistema Megara PRD; Es una dependencia para que el producto SWAP funcione en la integración MEGARA X ALDRIN; El paquete original estaba en Microsoft Azure Storage bajo la ruta megara-files > PRE > ReleaseCollinsWRelease12.02.01; Las capturas de pantalla muestran el contenido del Azure Storage con los archivos "Installation Guide ReleaseCollinsW 12.02.01.docx" y "ReleaseCollinsW 12.02.01.docx", y un registro de eliminación de un archivo de la versión 9.11.00. · Adjuntos del correo: image.png, image706531.gif, image066259.png, image001.png, image002.png, image003.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png

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
- 2026-10-23 16:14 — nuevo → Abierto — Correo automático
- 2026-10-26 17:26 — Abierto → Resuelto — Marco Pichardo

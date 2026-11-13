---
id: NFQBAU-1568
fecha_apertura: 2026-10-23
fecha_limite: 2026-10-23
fecha_resolucion: 2026-10-26
estado: Resuelto
prioridad: Alta
responsable: Marco Pichardo
origen: email
referencia_origen: "[EXTERNAL] RE: Collins Release W12.02.01 (2026-10-23)"
categoria:
  - BBDD
entorno:
  - Producción
sintoma: Se requiere la ejecución de un script de la release Collins W12.02.01 en el entorno de Producción, lo que implica la parada de los módulos de Megara PRD.
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

Oussema A., Technical Expert de Vermeg, adjunta el script `AldrinDBProcedures19052026.sql` para la release Collins W12.02.01, que debe ser ejecutado. Este script es una dependencia para que el producto SWAP funcione en la integración MEGARA X ALDRIN. Pedro G., IT Support Analyst de NTT Data, había indicado previamente que el despliegue requiere parar los módulos de Megara PRD y solicitaba aprobación. Ado S., de Tecnología de PR Serviços, había solicitado a Oussema A. reenviar el paquete porque NTT no lo tenía disponible. Adjunta un fichero SQL y varias capturas.

Detalles: Nombre de la release: Collins Release W12.02.01; Nombre del script a ejecutar: AldrinDBProcedures19052026.sql; Entorno afectado: Megara PRD; El despliegue del script requiere parar todos los módulos de Megara PRD; Es una dependencia para que el producto SWAP funcione en la integración MEGARA X ALDRIN; Adjunta capturas de pantalla: una muestra un ticket S3C-22891 "MEGARA PRD - Collins Release W12.02.01" con un adjunto `RE_Collins Release W12.02.01.zip`; otra captura muestra el explorador de Azure con la ruta `megara-files/PRE/ReleaseCollinsW12.02.01/` donde se listan `01DB Script` y `Installation Guide ReleaseCollinsW12.02.01.docx` con fecha de modificación 19/05/2026.
Adjuntos del correo: image011.png, image023.gif, image002.png, image003.png, image026.png, image027.png, image028.png, image029.png, image030.png, image031.png, image032.png, image033.png, image034.png, image035.png, image036.png, image037.png, image038.png, image473536.gif, image594164.png, AldrinDBProcedures19052026.sql

## Histórico de interacciones

- 2026-10-23 16:46 — Correo automático — Oussema A., Technical Expert de Vermeg, adjunta el script `AldrinDBProcedures19052026.sql` para la release Collins W12.02.01, que debe ser ejecutado. Este script es una dependencia para que el producto SWAP funcione en la integración MEGARA X ALDRIN. Pedro G., IT Support Analyst de NTT Data, había indicado previamente que el despliegue requiere parar los módulos de Megara PRD y solicitaba aprobación. Ado S., de Tecnología de PR Serviços, había solicitado a Oussema A. reenviar el paquete porque NTT no lo tenía disponible. Adjunta un fichero SQL y varias capturas.
- 2026-10-23 16:56 — Correo automático — Correo nuevo en el hilo: Pedro Henrique G., analista de soporte en NTT Data, consulta si hay acuerdo para ejecutar un script de release sin realizar una parada del entorno. Pedro confirma que el script no es grande y solicita la validación del impacto. Detalles: Release W12.02.01; Script para ejecutar sin parada del entorno; Módulos afectados: Megara PRD; adjunta capturas e imágenes. · Adjuntos del correo: image011.png, image023.gif, image002.png, image003.png, image026.png, image027.png, image028.png, image029.png, image030.png, image031.png, image032.png, image033.png, image034.png, image035.png, image036.png, image037.png, image038.png, image473536.gif, image594164.png, image.png
- 2026-10-23 17:01 — Correo automático — Correo nuevo en el hilo: Kleverson B., tecnología de soporte, pregunta si es necesario detener los módulos de Megara para ejecutar el script recibido. Pedro G., analista de soporte en NTT Data, confirma que se puede realizar sin detener el entorno. Detalles: Release W12.02.01; Script de despliegue para Megara PRD; adjunta capturas y un fichero ZIP; consulta si se requiere parada de módulos. · Adjuntos del correo: image001.png, image004.png, image005.png, image006.png, image007.gif, image008.png, image009.png, image010.png, image012.png, image013.png, image014.png, image015.png, image016.png, image017.png, image018.png, image019.png, image020.png, image021.png, image022.png, image023.png, image024.png, image025.png
- 2026-10-23 17:06 — Correo automático — Correo nuevo en el hilo: Oussema A., experto técnico en Vermeg, responde que no es necesario detener los módulos de Megara para ejecutar el script de despliegue. Detalles: Script asociado a la release Collins W12.02.01; módulos de Megara PRD; adjunta capturas · Adjuntos del correo: image001.png, image004.png, image005.png, image006.png, image007.gif, image008.png, image009.png, image010.png, image012.png, image013.png, image014.png, image015.png, image016.png, image017.png, image018.png, image019.png, image020.png, image021.png, image022.png, image023.png, image024.png, image025.png, image088505.gif, image729484.png
- 2026-10-23 17:11 — Correo automático — Correo nuevo en el hilo: Pedro G., analista de soporte de NTT Data, informa que el despliegue de la versión W12.02.01 de Collins y la ejecución del script han finalizado con éxito. Se refiere al ticket S3C-22891. Detalles: Ticket S3C-22891; Despliegue de Collins Release W12.02.01; Script ejecutado con éxito; No fue necesario detener los módulos de Megara. · Adjuntos del correo: image001.png, image004.png, image005.png, image006.png, image007.gif, image008.png, image009.png, image010.png, image012.png, image013.png, image014.png, image015.png, image016.png, image017.png, image018.png, image019.png, image020.png, image021.png, image022.png, image023.png, image024.png, image025.png, image088505.gif, image729484.png, image.png
- 2026-10-23 17:26 — Correo automático — Correo nuevo en el hilo: Oussema A., experto técnico de Vermeg, confirma que la funcionalidad AdditionalDerivativePrice ya está activa en Producción. Esto sigue a la ejecución exitosa de un script por parte de Pedro G. C., analista de soporte de NTT Data, como parte del despliegue de la versión Collins Release W12.02.01, asociado al ticket S3C-22891. Se adjuntan capturas. Detalles: Despliegue de la versión Collins Release W12.02.01; Script ejecutado con éxito; Ticket S3C-22891; Funcionalidad activada: AdditionalDerivativePrice; No fue necesario detener los módulos de Megara para la ejecución del script; La captura de pantalla muestra el ticket S3C-22891 en Jira con el título "MEGARA PRD - Collins Release W12.02.01"; Otra captura muestra archivos en Azure Storage en la ruta "megara-files/PRE > ReleaseCollinsW12.02.01", incluyendo un "01DB Script" y una "Installation Guide ReleaseCollinsW12.02.01.docx". · Adjuntos del correo: image003.gif, image034.png, image001.png, image004.png, image005.png, image006.png, image008.png, image009.png, image010.png, image012.png, image013.png, image014.png, image015.png, image016.png, image017.png, image018.png, image019.png, image020.png, image021.png, image022.png, image023.png, image024.png, image025.png, image046.png, image451219.gif, image250195.png
- 2026-10-23 17:26 — Correo automático — Correo nuevo en el hilo: Oussema A., technical expert de Vermeg, confirma que ya está hecho en respuesta a la petición de Ricardo C., del proyecto Apollo, para realizar una configuración. Adjuntos del correo: image813239.gif, image889887.png

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
- 2026-10-23 16:46 — (vacío) → Abierto — Correo automático
- 2026-10-26 17:26 — Abierto → Resuelto — Marco Pichardo

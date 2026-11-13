---
id: NFQBAU-1617
fecha_apertura: 2026-11-03
fecha_limite: 2026-11-04
fecha_resolucion:
estado: Revisión cliente
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: "[EXTERNAL] Jiras Packages in the PRE-PROD Environment - 30/10/2026 (2026-11-03)"
categoria:
  - Otros
entorno:
  - UAT
sintoma: Solicitud de validación sobre el estado de los Jiras y paquetes de implementación tras la implantación del fin de semana, con dudas específicas sobre el Jira SC-9009.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-06 13:13
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

Fernando A. Martins Junior, del equipo de soporte, solicita a Marcelo F. do Prado Santos, de PR Serviços, que valide si los comentarios sobre los paquetes de Jiras para la implementación del fin de semana han cambiado. Tiene dudas sobre el Jira SC-9009. Adjunta capturas.

Detalles: Jira SC-9009: "Create field in FIDIC operation – RISK", pendiente de validación y no forma parte de los paquetes a implementar; Jira SC-9513: "Aldrin - Data Hub Extraction for INR portfolios (on Hold)", pendiente de validación y no forma parte de los paquetes a implementar; Jira SC-10118: "CDA - Legal Report - Contractual client", pendiente de validación y no forma parte de los paquetes a implementar; Jira SC-10475: "Aldrin reload - Max last two business dates", pendiente de validación y no forma parte de los paquetes a implementar; Jira SC-10594: "Create a new extraction - Settled Price", pendiente de validación y no forma parte de los paquetes a implementar; Jira SC-10631: "Aldrin - OTC SWAP - additional fields", pendiente de validación y no forma parte de los paquetes a implementar; Jira SC-10653: "[ALDRIN] Massively improve CGCPosition performance for data reload", validado y sube en la implementación; Jira SC-10665: "ALDRIN : NavBankBalnce : fix currency_code", validado y sube en la implementación; Paquetes a implementar: Collins Release W15.00.00; Collins Release W15.00.01; Collins Release W15.00.02; Collins Release W15.01.00; Collins Release W15.01.01; Collins Release W15.01.02; Collins Release W15.01.03; Collins Release W15.01.04; Las capturas muestran una tabla con el estado de varios Jiras ('JIRAS WAITING', 'JIRAS - EM VALIDAÇÃO', 'JIRAS - IMPEDITIVOS') asignados a diferentes usuarios como Ado G., Augusto M., Cintia V., Fabiana A., Guilherme V., Francinete S., Jose N., Juliana V., Matheus T., Soraia A. y Wellington F.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.gif, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png, image011.png, image012.png, image013.png, image014.png, image015.png, image016.png, image017.png, image018.png, image019.png, image020.png

## Histórico de interacciones

- 2026-11-03 13:18 — Correo automático — Fernando A. Martins Junior, del equipo de soporte, solicita a Marcelo F. do Prado Santos, de PR Serviços, que valide si los comentarios sobre los paquetes de Jiras para la implementación del fin de semana han cambiado. Tiene dudas sobre el Jira SC-9009. Adjunta capturas.
- 2026-11-03 13:51 — Correo automático — Correo nuevo en el hilo: Diogo H., del Proyecto Apollo, informa a Fernando M. que el campo 'With Risk' sí consta en Producción. Esto es en respuesta a una consulta previa de Fernando M. sobre si hubo cambios en los comentarios durante la implementación del fin de semana, específicamente para el Jira SC-9009. Adjunta capturas. Detalles: Jira ID: SC-9009; Campo consultado: 'With Risk'; Pantalla: 'Client Instructions' -> 'Monitor'; La captura de pantalla muestra la interfaz de la aplicación 'megaapps.s3caceis.com.br:9445/MegaCustody/WebApp.jsp' con la sección 'Client Instructions' abierta y la subsección 'Monitor' seleccionada. Se resalta la columna 'With Risk' con valores 'No' en todas las filas visibles. · Adjuntos del correo: image021.jpg, image022.png, image023.png, image024.png, image025.gif, image026.png, image027.png, image028.png, image029.png, image030.png, image031.png, image032.png, image033.png, image034.png, image035.png, image036.png, image037.png, image038.png, image039.png, image040.png, image041.png

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
- 2026-11-03 13:18 — nuevo → Abierto — Correo automático
- 2026-11-04 16:02 — Abierto → Resuelto — Matheus Fransoni
- 2026-11-05 17:43 — Abierto → Revisión cliente — Marco Pichardo
- 2026-11-06 12:14 — Resuelto → Revisión cliente — Matheus Fransoni

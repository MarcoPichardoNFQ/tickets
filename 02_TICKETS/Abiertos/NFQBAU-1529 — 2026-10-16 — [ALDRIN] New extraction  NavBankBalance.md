---
id: NFQBAU-1529
fecha_apertura: 2026-10-16
fecha_limite: 2026-10-17
fecha_resolucion:
estado: Pruebas cliente UAT
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: "[ALDRIN] New extraction : NavBankBalance (2026-10-16)"
categoria:
  - Rundeck
entorno:
  - UAT
sintoma: Solicitud de autorización para actualizar el archivo de flags lookup_java_flag.txt de la extracción NavBankBalance.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-21 01:38
actualizado_por: Marco Pichardo
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Correo automático'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marco P., consultor de NFQ, solicita autorización a Fernando M., de S3 Caceis, para actualizar el archivo lookup_java_flag.txt en el entorno UAT. La solicitud se realiza en el marco de la nueva extracción NavBankBalance. Adjunta un fichero y capturas.

Detalles: Extracción: NavBankBalance; Archivo: lookup_java_flag.txt; Ruta: /nfq/data/cfg/; Entorno: UAT
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image.png, image016.png, image011.gif, image018.png, image014.jpg, image008.png, image013.jpg, image007.png, image009.png, image015.png, image012.png, image010.png, image017.png, lookup_java_flag.txt

## Histórico de interacciones

- 2026-10-16 22:46 — Correo automático — Marco P., consultor de NFQ, solicita autorización a Fernando M., de S3 Caceis, para actualizar el archivo lookup_java_flag.txt en el entorno UAT. La solicitud se realiza en el marco de la nueva extracción NavBankBalance. Adjunta un fichero y capturas.
- 2026-10-16 23:51 — Correo automático — Correo nuevo en el hilo: Fernando M., de S3 Caceis, responde manifestando su acuerdo con la solicitud previa del equipo técnico. Con ello autoriza a modificar la configuración necesaria para la extracción NavBankBalance en el entorno de pruebas. Detalles: Autorización para actualizar el archivo lookup_java_flag.txt en la ruta /nfq/data/cfg/ para el entorno UAT; Extracción: NavBankBalance · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image.png, image016.png, image011.gif, image018.png, image014.jpg, image008.png, image013.jpg, image007.png, image009.png, image015.png, image012.png, image010.png, image017.png
- 2026-10-17 02:21 — Correo automático — Correo nuevo en el hilo: Thiago S., analista de soporte de NTT DATA, informa de que el fichero ha sido actualizado según lo solicitado bajo el ticket S3C-22797. Adjunta capturas del servidor confirmando la modificación del archivo. Detalles: Ticket asociado: S3C-22797; Fichero actualizado: lookup_java_flag.txt en la ruta /nfq/data/cfg/; Servidor: AZU-0050-APPSPO; La captura de terminal muestra la lista de ficheros con la copia de seguridad lookup_java_flag.txt.17102026 y el fichero lookup_java_flag.txt modificado con fecha 17 de octubre · Adjuntos del correo: image001.png, image002.gif, image003.png, image004.png, image005.png, image006.png, image019.png, image020.png, image021.png, image022.png, image023.png, image024.png, image025.png, image026.gif, image027.png, image028.jpg, image029.jpg, image030.png, image031.png, image032.png, image033.png

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
- 2026-10-16 22:46 — (vacío) → Abierto — Correo automático
- 2026-10-17 11:51 — Abierto → En curso — Ricardo Reyes
- 2026-10-21 01:38 — En curso → Pruebas cliente UAT — Marco Pichardo

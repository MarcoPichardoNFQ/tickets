---
id: NFQBAU-1595
fecha_apertura: 2026-10-28
fecha_limite: 2026-10-31
fecha_resolucion: 2026-10-29
estado: Resuelto
prioridad: Baja
responsable: Matheus Fransoni
origen: email
referencia_origen: "[ALDRIN] Novo Ajuste na função cs_cli_cash_account_transf_pc (2026-10-28)"
categoria:
  - BBDD
entorno:
  - UAT
sintoma: Se requiere actualizar la función cs_cli_cash_account_transf_pc para que inserte el campo dat_qlikupdate en cada nuevo registro.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-29 17:34
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

Deborah B., desarrolladora de NFQ, envía una modificación en una función para registrar el campo dat_qlikupdate con cada nuevo registro. Consulta a Marcos M. si es posible proceder con la solicitud de actualización en el entorno de UAT; adjunta un fichero.

Detalles: Función: cs_cli_cash_account_transf_pc; Campo a insertar: dat_qlikupdate; Archivo adjunto: UPDATE cs_cli_cash_account_transf_pc.sql
Adjuntos del correo: UPDATE cs_cli_cash_account_transf_pc.sql

## Histórico de interacciones

- 2026-10-28 20:29 — Correo automático — Deborah B., desarrolladora de NFQ, envía una modificación en una función para registrar el campo dat_qlikupdate con cada nuevo registro. Consulta a Marcos M. si es posible proceder con la solicitud de actualización en el entorno de UAT; adjunta un fichero.
- 2026-10-29 11:36 — Correo automático — Correo nuevo en el hilo: Marcos M., del área de Tecnología, da su conformidad para avanzar con la actualización en el entorno de UAT. Señala además que ya había otorgado su aprobación el día anterior. Detalles: Función cs_cli_cash_account_transf_pc; Aprobación otorgada para actualización en UAT · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-10-29 12:03 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador de NFQ, solicita al equipo de soporte ayuda para compilar el código de una función en UAT.
El cambio cuenta con la aprobación de Marcos M., del área de tecnología, para añadir el campo dat_qlikupdate a cada nuevo registro.
Adjunta capturas y ficheros para la aplicación y el rollback. Detalles: Función afectada: cs_cli_cash_account_transf_pc; Host: psqlcerdatahub01.postgres.database.cloud.corp; Objetivo: Inserción del campo dat_qlikupdate a cada nuevo registro; Ficheros adjuntos: UPDATE cs_cli_cash_account_transf_pc.sql, ROLLBACK cs_cli_cash_account_transf_pc.sql; Fecha/Hora inicio prevista: 2026-10-29 12:00; La captura adjunta muestra la confirmación del flujo de aprobación requerido para UAT · Adjuntos del correo: image001.png, image002.png, image003.png, image.png, UPDATE cs_cli_cash_account_transf_pc.sql, ROLLBACK cs_cli_cash_account_transf_pc.sql
- 2026-10-29 16:21 — Correo automático — Correo nuevo en el hilo: Gilcemar G., de NTT Data, informa que el ticket S3C-22979 ha sido ejecutado con éxito en el ambiente UAT. Adjunta capturas. Detalles: Ticket S3C-22979; Se modificó la función cs_cli_cash_account_transf_pc para insertar el campo dat_qlikupdate a cada nuevo registro; Host: psqlcerdatahub01.postgres.database.cloud.corp; La captura de pantalla muestra la ejecución de un DROP y CREATE OR REPLACE PROCEDURE para la función trf_s3_cs_cli_cash_account_transf_pc; Otra captura muestra el mensaje 'Query returned successfully in 608 msec.' y 'Query complete 00:00:00.608'. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png
- 2026-10-29 16:22 — Correo automático — Correo nuevo en el hilo: Marcos M., tecnología, informa que las pruebas del ajuste en la función cs_cli_cash_account_transf_pc han finalizado con éxito en UAT. Solicita gestionar la aprobación y actualización correspondiente en Producción. Adjunta capturas. Detalles: Función: trf_s3.cs_cli_cash_account_transf_pc; Tabla: trf_s3.sss_cli_csh_acc_t; Campo insertado: dat_qlikupdate; Host: psqlcerdatahub01.postgres.database.cloud.corp; Ticket Jira: S3C-22979; Las capturas muestran la consulta SQL comprobando la actualización del campo dat_qlikupdate, la recreación del procedimiento compilado con éxito en pgAdmin y un correo aclaratorio sobre aprobaciones. · Adjuntos del correo: image006.png, image007.png, image008.png, image009.png, image010.png, image011.png
- 2026-10-29 17:01 — Correo automático — Correo nuevo en el hilo: Matheus F., desarrollador de NFQ, solicita aprobación para ejecutar un script de actualización en la base de datos de producción. La modificación agrega el campo dat_qlikupdate en la función cs_cli_cash_account_transf_pc del sistema ALDRIN y ya fue validada en UAT por Marcos M., del equipo de tecnología. Adjunta capturas y ficheros. Detalles: Host PRD: psqlprddatahub03.postgres.database.cloud.corp; Sistema: ALDRIN; Ticket ID: NFQBAU1593; Función afectada: trf_s3.cs_cli_cash_account_transf_pc; Objetivo: insertar el campo dat_qlikupdate a cada nuevo registro; Archivos: UPDATE cs_cli_cash_account_transf_pc.sql y ROLLBACK cs_cli_cash_account_transf_pc.sql; Capturas: muestran la creación exitosa del procedimiento almacenado en PostgreSQL y la verificación en la tabla trf_s3.sss_cli_csh_acc_t con el campo dat_qlikupdate informado (2026-10-29 16:10:21.227) · Adjuntos del correo: image006.png, image007.png, image008.png, image009.png, image010.png, image011.png, image.png, UPDATE cs_cli_cash_account_transf_pc.sql, ROLLBACK cs_cli_cash_account_transf_pc.sql
- 2026-10-29 17:02 — Correo automático — Correo nuevo en el hilo: Matheus D. F., desarrollador, solicita la aprobación y ejecución de un código SQL en la base de datos de Producción para modificar la función cs_cli_cash_account_transf_pc. Esta modificación, solicitada por Marcos A. M. de S3, busca insertar el campo dat_qlikupdate en cada nuevo registro. Kleverson B., de Tecnología, ha dado su aprobación para proceder. El cambio ya fue probado con éxito en UAT. Adjunta capturas. Detalles: Función afectada: cs_cli_cash_account_transf_pc; Objetivo: Insertar el campo dat_qlikupdate en cada nuevo registro; Sistema: ALDRIN; Host de Producción: psqlprddatahub03.postgres.database.cloud.corp; Host de UAT: psqlcerdatahub01.postgres.database.cloud.corp; Ticket ID: NFQBAU1593, S3C-22979; Impacto: Clientes y otros sistemas (ALDRIN es repositorio central de datos); Plan de rollback: Ejecución de código que compila la versión anterior (archivo ROLLBACK); No habrá indisponibilidad; Captura image004.png muestra una consulta 'select a.dat_qlikupdate from trf_s3.sss_cli_cash_acc_t a left join trf' con el campo dat_qlikupdate y un valor '2026-10-29 16:10:21.223'; Captura image007.png muestra la ejecución de 'CREATE OR REPLACE PROCEDURE trf_s3.cs_cli_cash_account_transf_pc'; Se adjuntan dos archivos: uno para la actualización (UPDATE) y otro para el rollback (ROLLBACK). · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png

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
- 2026-10-28 20:29 — nuevo → Abierto — Correo automático
- 2026-10-29 17:34 — Abierto → Resuelto — Matheus Fransoni

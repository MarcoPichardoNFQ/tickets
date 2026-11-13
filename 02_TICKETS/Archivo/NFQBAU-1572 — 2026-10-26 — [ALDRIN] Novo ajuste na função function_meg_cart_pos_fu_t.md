---
id: NFQBAU-1572
fecha_apertura: 2026-10-26
fecha_limite: 2026-10-27
fecha_resolucion: 2026-10-29
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: "[ALDRIN] Novo ajuste na função function_meg_cart_pos_fu_t (2026-10-26)"
categoria:
  - BBDD
entorno:
  - UAT
sintoma: La función function_meg_cart_pos_fu_t utiliza una fecha incorrecta para la cotización de precios.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-06 15:31
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

Continúa el hilo del [NFQBAU-1518](../Abiertos/NFQBAU-1518%20—%202026-10-15%20—%20[ALDRIN]%20Novo%20ajuste%20na%20função%20function_meg_cart_pos_fu_t.md), cerrado el 2026-10-26: no se reabre, se crea este. Marco P., Senior Consultant de NFQ Advisory, solicita validar si el código enviado atiende la petición. Thiago A., de PR Serviços, había solicitado previamente un ajuste en la función function_meg_cart_pos_fu_t para corregir la fecha de cotización de precios. Adjunta capturas y dos ficheros SQL.

Detalles: Adjunta capturas de pantalla (sin descripción); Adjunta ficheros SQL 'AJUSTE_function_meg_cart_pos_fu_t.sql' y 'BKP_function_meg_cart_pos_fu_t.sql'; La modificación solicitada en la función function_meg_cart_pos_fu_t es para cambiar la condición de join de `pri.dat_price = val.dat_valuat` a `pri.dat_price = val.dat_assepr`; También se añaden los campos `cod_valprocs` y `dat_assepr` a la cláusula SELECT y GROUP BY de la subconsulta que selecciona de `trf_s3.sss_position_t`.
Adjuntos del correo: image001.png, AJUSTE_function_meg_cart_pos_fu_t.sql, BKP_function_meg_cart_pos_fu_t.sql

## Histórico de interacciones

- 2026-10-26 14:56 — Correo automático — Continúa el hilo del [NFQBAU-1518](../Abiertos/NFQBAU-1518%20—%202026-10-15%20—%20[ALDRIN]%20Novo%20ajuste%20na%20função%20function_meg_cart_pos_fu_t.md), cerrado el 2026-10-26: no se reabre, se crea este. Marco P., Senior Consultant de NFQ Advisory, solicita validar si el código enviado atiende la petición. Thiago A., de PR Serviços, había solicitado previamente un ajuste en la función function_meg_cart_pos_fu_t para corregir la fecha de cotización de precios. Adjunta capturas y dos ficheros SQL.
- 2026-10-26 15:26 — Correo automático — Correo nuevo en el hilo: Thiago A., desarrollo, solicita a Marco P., consultor senior, que verifique la función function_meg_cart_pos_fu_t porque el group by aún está incompleto. Marco P. había enviado previamente una propuesta de código para su validación. Adjunta capturas. Detalles: La función afectada es function_meg_cart_pos_fu_t; El group by debe incluir los campos DAT_VALUAT, DES_OWNER, cod_dmasse, des_counter, cod_valprocs, dat_assepr; Adjunta capturas que muestran el código con el group by incompleto. · Adjuntos del correo: image001.png, image002.png
- 2026-10-26 15:33 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, solicita a Thiago A., de PR Serviços, que valide si el código adjunto resuelve la solicitud de ajuste en la función function_meg_cart_pos_fu_t. Previamente, Thiago A. había solicitado este ajuste para corregir la fecha de cotización de precios y completar la cláusula GROUP BY. Adjunta capturas y un fichero. Detalles: La función a ajustar es function_meg_cart_pos_fu_t(). Se requiere añadir cod_valprocs y dat_assepr al GROUP BY de la subconsulta val en trf_s3.sss_position_t. La condición de JOIN con trf_s3.sss_prices_t debe cambiar de pri.dat_price = val.dat_valuat a pri.dat_price = val.dat_assepr. Se adjuntan capturas de pantalla y un fichero AJUSTE_function_meg_cart_pos_fu_t.sql con el código. · Adjuntos del correo: image001.png, image002.png, AJUSTE_function_meg_cart_pos_fu_t.sql
- 2026-10-26 18:25 — Correo automático — Correo nuevo en el hilo: Thiago A., desarrollador de PR Servicios, confirma que el ajuste realizado cumple con lo requerido. Solicita a Marco P., consultor senior, que suba los cambios al entorno de UAT. Adjunta capturas. Detalles: Función: function_meg_cart_pos_fu_t; Tablas afectadas: trf_s3.sss_position_t, trf_s3.sss_prices_t; Despliegue solicitado a UAT tras validar el ajuste en el agrupamiento y cruce de datos por dat_assepr · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-10-27 10:30 — Correo automático — Correo nuevo en el hilo: Matheus D., ingeniero de software de NFQ, solicita compilar en UAT un script de actualización para la función function_meg_cart_pos_fu_t con el fin de corregir la fecha de cotización de precios. Indica las personas autorizadas para aprobar el cambio según instrucciones de Kleverson B. Adjunta capturas y ficheros. Detalles: Host: psqlcerdatahub01.postgres.database.cloud.corp; Función afectada: function_meg_cart_pos_fu_t; Tablas involucradas: trf_s3.sss_position_t, trf_s3.sss_prices_t; Ficheros adjuntos: UPDATE function_meg_cart_pos_fu_t.sql y ROLLBACK function_meg_cart_pos_fu_t.sql; Fecha y hora prevista de ejecución: 2026-10-27 10:25; La captura image.png muestra un correo sobre la política de aprobaciones para UAT · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image.png, UPDATE function_meg_cart_pos_fu_t.sql, ROLLBACK function_meg_cart_pos_fu_t.sql
- 2026-10-27 11:37 — Correo automático — Correo nuevo en el hilo: Matheus D. F., software engineer JR, solicita ayuda para compilar un código adjunto en el entorno UAT. El cambio busca corregir la fecha de cotización de precios. Reinaldo R. A. de NTT DATA confirma el entorno UAT y adjunta capturas. El hilo de correo comenzó el 26 de octubre de 2026. Detalles: Nombre de la función: function_meg_cart_pos_fu_t; Host de la base de datos: psqlcerdatahub01.postgres.database.cloud.corp; Descripción del cambio: Data correta para cotação de preço; Servicios afectados: Database; Plan de rollback: Execução do arquivo ROLLBACK em anexo; No habrá indisponibilidad; Impacto al negocio: Inserção de informações no Aldrin; La captura de pantalla muestra la ejecución de un CREATE OR REPLACE FUNCTION para trf_s3.function_meg_cart_pos_fu_t en psqlcerdatahub01.postgres.database.cloud.corp, con el mensaje "Query returned successfully in 384 msec."; Kleverson B. indicó que Marcos A. M., Ado G. S. o Ricardo C. pueden aprobar ejecuciones en UAT; Adjunta capturas. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image.png, image.png, image.png
- 2026-10-28 17:37 — Correo automático — Correo nuevo en el hilo: Thiago A., desarrollador de PR Serviços, comunica que el ajuste en la función ha sido validado con éxito en el entorno de UAT. Solicita al equipo que procedan a subir el cambio al entorno de producción. Adjunta capturas. Detalles: Función: trf_s3.function_meg_cart_pos_fu_t; Sistema: ALDRIN; Servidor host: psqlcerdatahub01.postgres.database.cloud.corp; Ticket previo UAT: S3C-22944; La captura muestra una comparativa de consultas en cliente SQL entre sss_position_t y cart_pos_fu_t con registros para cod_cli CUST4604 y CUST4666 con fecha 2026-09-30; Se observa también ejecución exitosa de CREATE OR REPLACE FUNCTION trf_s3.function_meg_cart_pos_fu_t() en pgAdmin · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png
- 2026-10-28 20:16 — Correo automático — Correo nuevo en el hilo: Deborah Yohana B., desarrolladora de NFQ, solicita la aprobación de Kleverson B., Mauricio L. y Fernando M., responsables del cliente, para ejecutar un script SQL en el entorno de producción. El objetivo es ajustar la función function_meg_cart_pos_fu_t para corregir la fecha de cotización de precio en el sistema ALDRIN. Adjunta capturas y ficheros. Detalles: Ticket ID: NFQBAU1572; Función afectada: function_meg_cart_pos_fu_t(); Host PRD: psqlprddatahub03.postgres.database.cloud.corp; Archivo de actualización: UPDATE function_meg_cart_pos_fu_t.sql; Archivo de rollback: ROLLBACK function_meg_cart_pos_fu_t.sql; Las capturas adjuntas muestran diferencias en los resultados de consulta SQL entre la vista y la función, además de la compilación exitosa de CREATE OR REPLACE FUNCTION trf_s3.function_meg_cart_pos_fu_t() en la base de datos. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, ROLLBACK function_meg_cart_pos_fu_t.sql, UPDATE function_meg_cart_pos_fu_t.sql
- 2026-10-29 08:41 — Correo automático — Correo nuevo en el hilo: Kleverson B., del área de Tecnología de S3 Caceis, da su aprobación para ejecutar el cambio en el entorno productivo.
El cambio responde a una solicitud previa para corregir la función en la base de datos tras haberse validado con éxito en UAT. Detalles: Host: psqlprddatahub03.postgres.database.cloud.corp; Sistema: ALDRIN; Función afectada: trf_s3.function_meg_cart_pos_fu_t(); Ticket ID: NFQBAU1572 / S3C-22944; Motivo del ajuste: corrección de la fecha de cotización de precio; Tablas relacionadas en capturas: sss_position_t, cart_pos_fu_t; Script con prefijo UPDATE para aplicar cambio y ROLLBACK para reversión · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png, image011.png
- 2026-10-29 08:42 — Correo automático — Correo nuevo en el hilo: Kleverson B., de Tecnología en S3 Caceis, responde dando su aprobación ("De acordo") a la solicitud de pase a producción. La petición previa requería el visto bueno para compilar el ajuste de la función en la base de datos de PRD. Detalles: Host: psqlprddatahub03.postgres.database.cloud.corp; Función afectada: trf_s3.function_meg_cart_pos_fu_t(); Sistema: ALDRIN; Ticket ID asociado: NFQBAU1572; Ticket previo en UAT: S3C-22944; Motivo del cambio: corrección de la fecha de cotización de precio; Tiempo estimado de rollback: 30 minutos · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png, image011.png

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
- 2026-10-26 14:56 — (vacío) → Abierto — Correo automático
- 2026-10-26 17:26 — Abierto → Revisión cliente — Marco Pichardo
- 2026-10-27 10:23 — Revisión cliente → Pendiente despliegue UAT — Matheus Fransoni
- 2026-10-27 11:52 — Pendiente despliegue UAT → Pruebas cliente UAT — Matheus Fransoni
- 2026-10-29 10:19 — Pruebas cliente UAT → Resuelto — Matheus Fransoni

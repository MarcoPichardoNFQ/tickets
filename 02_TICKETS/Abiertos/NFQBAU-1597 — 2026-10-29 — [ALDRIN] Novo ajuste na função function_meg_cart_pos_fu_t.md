---
id: NFQBAU-1597
fecha_apertura: 2026-10-29
fecha_limite: 2026-10-30
fecha_resolucion:
estado: Pruebas cliente UAT
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: "[ALDRIN] Novo ajuste na função function_meg_cart_pos_fu_t (2026-10-29)"
categoria:
  - BBDD
entorno: [Producción, UAT]
  - Producción
sintoma: La función function_meg_cart_pos_fu_t del sistema ALDRIN requiere un ajuste para corregir la fecha de cotización de precios.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-07 13:41
actualizado_por: Correo automático
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Continúa el hilo del [NFQBAU-1572](../Abiertos/NFQBAU-1572%20—%202026-10-26%20—%20[ALDRIN]%20Novo%20ajuste%20na%20função%20function_meg_cart_pos_fu_t.md), cerrado el 2026-10-29: no se reabre, se crea este. Reinaldo R. Alves, de NTT DATA, envía un correo muy breve con el ticket S3C-22971 y menciona el entorno de Producción. Esto da continuidad a la petición de Deborah Y. B., de NFQ, para ejecutar un código SQL que ajusta la función function_meg_cart_pos_fu_t para corregir la fecha de cotización de precios, solicitado por Thiago A. Adjunta capturas.

Detalles: Sistema: ALDRIN; Host: psqlprddatahub03.postgres.database.cloud.corp; Función afectada: function_meg_cart_pos_fu_t; Objetivo: Corrección de la fecha de cotización de precio; Ticket ID: S3C-22971 (mencionado en el último correo), NFQBAU1572 (mencionado en el correo de Deborah); Impacto en cliente: Sí; Impacto en otros sistemas: Sí, ALDRIN es un repositorio central de datos; Tiempo de indisponibilidad: N/A; Tiempo de rollback: 30 minutos; Responsable test funcional: Thiago A.; Responsable test técnico: Thiago A. / Marco P.; Adjunta capturas de pantalla que muestran la comparación de datos antes y después del ajuste de la función, y la sentencia SQL para la creación o reemplazo de la función trf_s3.function_meg_cart_pos_fu_t.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png, image011.png, image.png, image.png

## Histórico de interacciones

- 2026-10-29 13:03 — Correo automático — Continúa el hilo del [NFQBAU-1572](../Abiertos/NFQBAU-1572%20—%202026-10-26%20—%20[ALDRIN]%20Novo%20ajuste%20na%20função%20function_meg_cart_pos_fu_t.md), cerrado el 2026-10-29: no se reabre, se crea este. Reinaldo R. Alves, de NTT DATA, envía un correo muy breve con el ticket S3C-22971 y menciona el entorno de Producción. Esto da continuidad a la petición de Deborah Y. B., de NFQ, para ejecutar un código SQL que ajusta la función function_meg_cart_pos_fu_t para corregir la fecha de cotización de precios, solicitado por Thiago A. Adjunta capturas.
- 2026-10-29 20:02 — Correo automático — Correo nuevo en el hilo: Reinaldo A., de NTT DATA, informa de la ejecución del cambio en el entorno de producción bajo el ticket S3C-22988.
No realiza ninguna petición nueva ni reporta problemas, únicamente adjunta capturas como evidencia del despliegue. Detalles: Ticket S3C-22988; Entorno PRD; Función trf_s3.function_meg_cart_pos_fu_t; Captura adjunta con la evidencia de ejecución del script en base de datos · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png, image011.png, image.png, image.png
- 2026-10-30 13:15 — Correo automático — Correo nuevo en el hilo: Thiago A. solicita realizar un ajuste en la función function_meg_cart_pos_fu_t para contemplar correctamente las opciones de futuros en moneda extranjera. Para ello, proporciona los fragmentos de código SQL con las modificaciones a aplicar. Detalles: Función: function_meg_cart_pos_fu_t(); Tabla: trf_s3.sss_position_t; Cambio en el cálculo del campo AMT_PRICE_MERC (antes AMT_PREC_MERC) para aplicar val.amt_bookto cuando COD_DMASFM = 6 y cod_seccla = 'OPTION ON FUTURE'; Inclusión del campo amt_bookto en el SELECT y GROUP BY sobre la tabla trf_s3.sss_position_t · Adjuntos del correo: image001.png
- 2026-10-30 13:26 — Correo automático — Correo nuevo en el hilo: Matheus D. de NFQ Advisory adjunta un fichero con código SQL y pide validar si el ajuste en la función function_meg_cart_pos_fu_t atiende la solicitud de corrección de futuros en moneda extranjera. Adjunta un fichero. Detalles: Se solicita validar el ajuste en la función function_meg_cart_pos_fu_t para corregir la opción de futuros en moneda extranjera.; El ajuste implica cambios en dos secciones del código SQL.; Sección 1: La expresión de cálculo de AMT_PREC_MERC se modifica para incluir un CASE WHEN basado en b.COD_DMASFM = 6 y b.cod_seccla = 'OPTION ON FUTURE', asignando val.amt_bookto en ese caso, o la expresión original en otro caso, renombrando la columna a AMT_PRICE_MERC.; Sección 2: En la subconsulta de trf_s3.sss_position_t, se añade amt_bookto a las cláusulas SELECT y GROUP BY.; Adjunta un fichero UPDATE function_meg_cart_pos_fu_t_20261030.sql con el código de la función. · Adjuntos del correo: image001.png, UPDATE function_meg_cart_pos_fu_t_20261030.sql
- 2026-10-30 13:26 — Correo automático — Correo nuevo en el hilo: Thiago A., de PR Serviços, solicita que se suba a UAT un ajuste en la función function_meg_cart_pos_fu_t que ha sido validado. Este ajuste es para la opción de futuros en moneda extranjera. Matheus D., desarrollador de NFQ, había pedido previamente la validación del código. Adjunta capturas. Detalles: La función a ajustar es function_meg_cart_pos_fu_t. El ajuste es para la opción de futuros en moneda extranjera. Se detallan cambios en dos secciones de código: 1) Se añade un CASE para b.COD_DMASFM = 6 and b.cod_seccla = 'OPTION ON FUTURE' en el cálculo de AMT_PRICE_MERC; 2) Se añade amt_bookto al SELECT y GROUP BY de la tabla trf_s3.sss_position_t donde COD_TYPEAS es 'Future' u 'Option'. Adjunta capturas de pantalla, aunque no se describe su contenido. · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-10-30 13:33 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador de NFQ, solicita ayuda para compilar un código ajustado en UAT referente a la opción de futuros en moneda extranjera. El cambio está programado para el 30/10/2026 a las 13:30 y cuenta con plan de rollback. Adjunta capturas y ficheros. Detalles: Función afectada: function_meg_cart_pos_fu_t; Servidor BBDD: psqlcerdatahub01.postgres.database.cloud.corp; Ficheros adjuntos: UPDATE function_meg_cart_pos_fu_t_20261030.sql y ROLLBACK function_meg_cart_pos_fu_t_20261030.sql; Horario previsto: 2026-10-30 13:30; La captura muestra un correo aclarando el proceso de aprobación de cambios para UAT · Adjuntos del correo: image001.png, image002.png, image003.png, image.png, ROLLBACK function_meg_cart_pos_fu_t_20261030.sql, UPDATE function_meg_cart_pos_fu_t_20261030.sql
- 2026-10-30 16:41 — Correo automático — Correo nuevo en el hilo: Guilherme S. informa de la ejecución exitosa del ticket S3C-23003 en UAT. Este ticket se originó por una petición de Matheus D., desarrollador de NFQ, para compilar código de la función function_meg_cart_pos_fu_t en UAT, con la aprobación de Marcos M., Ado G. y Ricardo C. Thiago A. de PR Serviços había validado previamente el código. Adjunta capturas. Detalles: Ticket ID: S3C-23003; Función afectada: function_meg_cart_pos_fu_t; Host: psqlcerdatahub01.postgres.database.cloud.corp; Descripción de la cambio: Alteración para ajustar opción de futuros en moneda extranjera; Servicios afectados: Database; Plan de rollback: Ejecución del archivo ROLLBACK adjunto; No hay indisponibilidad; Impacto al negocio: Inserción de información en Aldrin; Captura 1: Muestra la ejecución de un script SQL para DROP FUNCTION y CREATE OR REPLACE FUNCTION trf_s3.function_meg_cart_pos_fu_t() en psqlcerdatahub01, con 0 filas actualizadas y 0.505s de tiempo de ejecución; Captura 2: Muestra un correo de Kleverson B. indicando que Marcos M., Ado G., Ricardo C. o David pueden aprobar para UAT; El correo original de Thiago A. detalla los cambios en el código SQL de la función, específicamente en las cláusulas case when y la selección de amt_bookto. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png
- 2026-11-05 16:53 — Correo automático — Correo nuevo en el hilo: Thiago A., del equipo de desarrollo, solicita la aprobación y despliegue en Producción de un ajuste en la función function_meg_cart_pos_fu_t del sistema ALDRIN, tras haber sido validado en UAT. Reinaldo A., de NTT Data, confirma la solicitud para el ticket S3C-22988 y adjunta capturas de los resultados. Detalles: Función afectada: trf_s3.function_meg_cart_pos_fu_t; Host: psqlprddatahub03.postgres.database.cloud.corp; Ticket ID: NFQBAU1572; Las capturas muestran comparativas de datos en la tabla trf_s3.cart_pos_fu_t filtradas por cod_cli 'CUST4945' y la ejecución exitosa de la creación de la función; adjunta capturas. · Adjuntos del correo: image012.png, image013.png, image014.png, image015.png, image016.png, image017.png, image018.png, image019.png, image020.png, image021.png, image022.png, image023.png, image024.png, image025.png
- 2026-11-05 17:56 — Correo automático — Correo nuevo en el hilo: Marco P., consultor senior en NFQ, pide registrar actividad sobre la validación y el despliegue del ajuste en la función tras haber sido probado en UAT y aprobado para producción.
El cambio corrige la fecha de cotización de precio. Detalles: Función afectada: trf_s3.function_meg_cart_pos_fu_t(); Tabla afectada: trf_s3.cart_pos_fu_t; Host: psqlprddatahub03.postgres.database.cloud.corp; Ticket ID: NFQBAU1572; Motivo del cambio: corrección de la fecha de cotización de precio; Las capturas muestran consultas SQL ejecutadas sobre la tabla trf_s3.cart_pos_fu_t filtrando por cod_cli = 'CUST4945' y el código fuente de creación de la función en PostgreSQL. · Adjuntos del correo: image012.png, image013.png, image014.png, image015.png, image016.png, image017.png, image018.png, image019.png, image020.png, image021.png, image022.png, image023.png, image024.png, image025.png
- 2026-11-06 13:57 — Correo automático — Correo nuevo en el hilo: Thiago A. solicita un ajuste en la función 'function_meg_cart_pos_fu_t'. El cambio implica modificar la cláusula GROUP BY y la agregación de 'amt_bookto' dentro de una subconsulta. Adjunta capturas. Detalles: Función a ajustar: 'function_meg_cart_pos_fu_t()'; Tabla afectada: 'trf_s3.sss_position_t'; Cambio en la subconsulta: antes 'amt_bookto' no estaba en el GROUP BY y se seleccionaba directamente, ahora se agrega con SUM(amt_bookto) y se elimina del GROUP BY; La captura de pantalla es la firma del remitente. · Adjuntos del correo: image001.png
- 2026-11-06 14:17 — Correo automático — Correo nuevo en el hilo: Marco P., consultor sénior, solicita abrir un ticket para registrar la actividad y atender la solicitud de ajuste en una función enviada previamente por Thiago A., del proyecto o servicio. Detalles: Función afectada: function_meg_cart_pos_fu_t (); Tabla implicada: trf_s3.sss_position_t; Modificación solicitada: añadir SUM(amt_bookto) amt_bookto en el select y eliminar amt_bookto del group by. · Adjuntos del correo: image001.png
- 2026-11-06 15:06 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador, confirma que la solicitud de modificación de la función será atendida en el ticket NFQBAU1651, tras la petición inicial de Thiago A., desarrollador. Detalles: Función afectada: function_meg_cart_pos_fu_t; Tabla: trf_s3.sss_position_t; Modificación solicitada: añadir SUM(amt_bookto) amt_bookto en el select y eliminar amt_bookto del group by. · Adjuntos del correo: image001.png
- 2026-11-06 15:11 — Correo automático — Correo nuevo en el hilo: Matheus D., developer de NFQ, pregunta a Thiago A., de PR Serviços, si el código enviado en el fichero adjunto atiende su solicitud previa de modificación en la función, gestionada bajo el ticket NFQBAU1651. Detalles: Función afectada: function_meg_cart_pos_fu_t (); Adjunta capturas; Adjunta un fichero: UPDATE function_meg_cart_pos_fu_t_20261106.sql; Modificación en consulta SQL sobre trf_s3.sss_position_t añadiendo sum(amt_bookto) y modificando el group by. · Adjuntos del correo: image001.png, UPDATE function_meg_cart_pos_fu_t_20261106.sql
- 2026-11-06 15:41 — Correo automático — Correo nuevo en el hilo: Thiago A., proveedor, solicita que se suba el cambio realizado a UAT. Adjunta capturas. Detalles: Función: function_meg_cart_pos_fu_t (); Tabla afectada: trf_s3.sss_position_t; Modificación en el group by y en la función sum sobre el campo amt_bookto; adjunta capturas. · Adjuntos del correo: image001.png, image002.png
- 2026-11-06 16:21 — Correo automático — Correo nuevo en el hilo: Matheus D., developer en NFQ, solicita compilar en UAT el código adjunto para ajustar la función de base de datos function_meg_cart_pos_fu_t, contando con la aprobación previa de Thiago A. Detalles: Host: psqlcerdatahub01.postgres.database.cloud.corp; Función afectada: function_meg_cart_pos_fu_t; Fecha y hora prevista: 2026-11-06 16:15; adjunta capturas y ficheros UPDATE function_meg_cart_pos_fu_t_20261106.sql y ROLLBACK function_meg_cart_pos_fu_t_20261106.sql · Adjuntos del correo: image001.png, image002.png, image.png, UPDATE function_meg_cart_pos_fu_t_20261106.sql, ROLLBACK function_meg_cart_pos_fu_t_20261106.sql
- 2026-11-06 17:16 — Correo automático — Correo nuevo en el hilo: Thiago A., desarrollador de proveedor, comunica que se ha validado correctamente en UAT y solicita proceder con la aprobación y actualización en PRD.
Adjunta capturas. Detalles: Host: psqlcerdatahub01.postgres.database.cloud.corp; Función afectada: trf_s3.function_meg_cart_pos_fu_t(); Capturas muestran la ejecución exitosa de la función en la consola de PostgreSQL y consultas de validación en la tabla trf_s3.cart_pos_fu_t con el cliente CUST4945. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png
- 2026-11-06 18:16 — Correo automático — Correo nuevo en el hilo: Matheus F., desarrollador de NFQ, solicita la aprobación para ejecutar un script de ajuste en la función de base de datos function_meg_cart_pos_fu_t en el entorno de producción tras ser validado en UAT.
El cambio fue solicitado por Thiago A., responsable de pruebas técnicas en S3, para el sistema ALDRIN.
Adjunta capturas y un fichero. Detalles: Ticket ID: NFQBAU1651 (S3C-23110); Host PRD: psqlprddatahub03.postgres.database.cloud.corp; Sistema: ALDRIN; Función PostgreSQL: trf_s3.function_meg_cart_pos_fu_t(); Ficheros SQL: UPDATE function_meg_cart_pos_fu_t_20261106.sql y ROLLBACK function_meg_cart_pos_fu_t_20261106.sql; Tiempo de rollback estimado: 30 minutos; Capturas de pantalla: Muestran resultados de consulta SQL sobre la tabla trf_s3.cart_pos_fu_t para el cliente CUST4945 y la compilación exitosa de la función en pgAdmin (Query returned successfully in 310 msec) · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image.png, image.png, ROLLBACK function_meg_cart_pos_fu_t_20261106.sql, UPDATE function_meg_cart_pos_fu_t_20261106.sql
- 2026-11-06 19:06 — Correo automático — Correo nuevo en el hilo: Kleverson B., soporte técnico, confirma y aprueba la ejecución del código SQL para el ajuste en la función solicitada tras la validación previa en UAT. Detalles: Sistema: ALDRIN; Host: psqlprddatahub03.postgres.database.cloud.corp; Función: trf_s3.function_meg_cart_pos_fu_t; Ticket ID: NFQBAU1651; S3C-23110; adjunta capturas mostrando consultas SQL y resultados en PostgreSQL. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image.png, image.png
- 2026-11-06 19:31 — Correo automático — Correo nuevo en el hilo: Reinaldo R., miembro del equipo técnico, adjunta capturas para solicitar que se compile el código proporcionado en UAT, contando ya con la aprobación de los responsables correspondientes. Detalles: Ticket: S3C-23110; Host: psqlcerdatahub01.postgres.database.cloud.corp; Función afectada: trf_s3.function_meg_cart_pos_fu_t(); Fecha y hora prevista: 2026-11-06 16:15; adjunta capturas de pantalla que muestran un correo antiguo de aprobación y la consola ejecutando exitosamente la creación de la función con el mensaje 'Query returned successfully in 310 msec.' · Adjuntos del correo: image001.png, image002.png, image.png, image.png, image.png
- 2026-11-07 13:41 — Correo automático — Correo nuevo en el hilo: Luiz C., técnico de operaciones de NTT DATA, informa que se ha ejecutado en producción el ajuste solicitado para la función SQL function_meg_cart_pos_fu_t (ticket S3C-23130). Previamente, Matheus F., desarrollador de NFQ, había solicitado la aprobación del despliegue tras la validación en UAT. Adjunta capturas. Detalles: Función afectada: function_meg_cart_pos_fu_t; Host: psqlprddatahub03.postgres.database.cloud.corp; Tickets: S3C-23130, NFQBAU1651; Sistema: ALDRIN; Ejecución de script SQL UPDATE en base de datos de Producción. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png, image011.png

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
- 2026-10-29 13:03 — nuevo → Abierto — Correo automático
- 2026-10-30 15:42 — Abierto → Pruebas cliente UAT — Matheus Fransoni

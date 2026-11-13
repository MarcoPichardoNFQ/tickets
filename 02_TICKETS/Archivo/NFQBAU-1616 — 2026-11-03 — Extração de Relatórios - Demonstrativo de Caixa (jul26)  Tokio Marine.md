---
id: NFQBAU-1616
fecha_apertura: 2026-11-03
fecha_limite: 2026-11-04
fecha_resolucion: 2026-11-05
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: Extração de Relatórios - Demonstrativo de Caixa (jul/26) | Tokio Marine (2026-11-03)
categoria:
  - Qlik
entorno:
  - Producción
sintoma: El informe de Demonstrativo de Caixa no presenta datos desde julio de 2026 para el cliente CUST2337.
solucion_corta:
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

Marcela C., del equipo de tecnología de PR Serviços, solicita revisar el problema con el cliente CUST2337 cuyo informe de caixa no muestra datos desde julio de 2026. Anteriormente, Caio D., de Tokio Marine, informó que al extraer el informe solo obtenía los saldos finales del día y solicitó el reporte en Excel y PDF. Adjunta capturas.

Detalles: Código de cliente afectado: CUST2337 (Tokio Marine); Informe afectado: Demonstrativo de Caixa; Período de datos sin información: desde 2026-07-01 hasta 2026-07-31; Captura de pantalla: muestra DBeaver en PostgreSQL (entornos Aldrin - PR) consultando las tablas SACCUSTODIA.MT_CAIXA y trf_s3.cart_caixa_mt_t para el cliente CUST2337 y la función trf_s3.reports_verificar_fundo_publish_demonstrativo_caixa
Adjuntos del correo: image001.png, image006.png, image007.png, image008.png, image009.png, image010.png, image002.png, image003.png

## Histórico de interacciones

- 2026-11-03 12:51 — Correo automático — Marcela C., del equipo de tecnología de PR Serviços, solicita revisar el problema con el cliente CUST2337 cuyo informe de caixa no muestra datos desde julio de 2026. Anteriormente, Caio D., de Tokio Marine, informó que al extraer el informe solo obtenía los saldos finales del día y solicitó el reporte en Excel y PDF. Adjunta capturas.
- 2026-11-03 15:56 — Correo automático — Correo nuevo en el hilo: Caio D., de Tokio Marine, solicita ayuda para extraer el informe "Demonstrativo de Caixa" para julio de 2026, ya que el portal solo devuelve saldos finales. Marcela Y. C., de Tecnología, hace seguimiento a la petición y menciona el CUST2337. Guilherme F. M. O. indica que la cantidad de lanzamientos es la misma en SAC y ALDRIN. Adjunta capturas. Detalles: El informe afectado es "Demonstrativo de Caixa" para el periodo de julio de 2026; El portal devuelve un archivo con solo los saldos finales del día; Se solicita en formato .xlsx y .pdf; Se menciona el código CUST2337; Guilherme F. M. O. indica que la cantidad de lanzamientos es la misma en SAC y ALDRIN; Las capturas muestran consultas SQL en una base de datos PostgreSQL, posiblemente del sistema ALDRIN (entorno PRD), relacionadas con el CUST2337 y el periodo 20260701. Las consultas parecen buscar datos de caja y saldos. · Adjuntos del correo: image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png
- 2026-11-04 10:27 — Correo automático — Correo nuevo en el hilo: Marcela C., tecnología de Sancac, solicita verificar por qué el informe "Demonstrativo de Caixa" para el cliente CUST2337 sigue sin datos. Caio D., de Tokio Marine, había reportado que el informe solo mostraba saldos finales del día para julio de 2026. Guilherme O. había indicado que la cantidad de registros en SAC y ALDRIN era la misma. Adjunta capturas. Detalles: El informe afectado es "Demonstrativo de Caixa" para el cliente CUST2337; El problema se manifiesta desde julio de 2026; El portal devuelve un archivo con solo los saldos finales del día; Se solicita la extracción en .xlsx y .pdf; Guilherme O. menciona que la cantidad de lanzamientos en SAC y ALDRIN es la misma; Las capturas de pantalla muestran consultas SQL a las tablas "SANCAC"."CUST2337" y "CUST_CAIXA_REF_1_1" para el periodo 2026-07-01 a 2026-07-31; Ambas consultas devuelven 143 filas con datos para ese periodo, lo que sugiere que los datos existen en la BBDD pero no se reflejan correctamente en el informe. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png
- 2026-11-04 10:28 — Correo automático — Correo nuevo en el hilo: Marcela Y. C., tecnología de Sancac, pregunta si se ha verificado el problema, ya que los informes siguen sin datos. Originalmente, Caio A. D., de Tokio Marine, solicitó ayuda para extraer el informe "Demonstrativo de Caixa" para julio de 2026 en formato .xlsx y .pdf, ya que el portal solo devuelve los saldos finales. Guilherme F. O. mencionó que la cantidad de registros en SAC y ALDRIN es la misma. El correo adjunta capturas. Detalles: El informe afectado es "Demonstrativo de Caixa" para el cliente CUST2337; El periodo afectado es julio de 2026 (del 2026-07-01 al 2026-07-31); El portal solo devuelve los saldos finales del día; Se solicita la extracción en .xlsx y .pdf; La captura de pantalla muestra consultas SQL a la tabla CUST2337 en la base de datos SANCAC para el rango de fechas 20260701 a 20260731, y los resultados de la consulta; También se menciona que la cantidad de lanzamientos en SAC y ALDRIN es la misma. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png
- 2026-11-04 11:11 — Correo automático — Correo nuevo en el hilo: Caio D., de Tokio Marine, solicita ayuda para extraer el informe "Demonstrativo de Caixa" para julio de 2026, ya que el portal solo devuelve los saldos finales. Marcela C., de Tecnología, ha hecho seguimiento indicando que los informes siguen sin datos. Adjunta capturas. Detalles: Informe afectado: 'Demonstrativo de Caixa'; Periodo afectado: julio/2026; El portal devuelve un archivo con solo los saldos finales del día; Formato solicitado: .xlsx y .pdf; Se menciona el código de cliente CUST2337; Adjunta capturas de pantalla de una herramienta de base de datos mostrando consultas SQL para el cliente CUST2337 y el periodo 2026-07-01 a 2026-07-31 en la tabla 'SANCAC.CAIXA', y también resultados de tablas como 'cart_caixa_ref_1' con 143 filas para el mismo cliente y periodo. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png
- 2026-11-04 17:08 — Correo automático — Correo nuevo en el hilo: Marcela C., tecnología, solicita una actualización sobre la falta de datos en el informe Demonstrativo de Caixa para Tokio Marine desde julio de 2026. El equipo de soporte está verificando el caso. Se adjuntan capturas. Detalles: Cliente: CUST2337 (Tokio Marine); Informe afectado: Demonstrativo de Caixa; Periodo afectado: datos desde julio de 2026 (2026-07-01 a 2026-07-31); Captura de DBeaver muestra consultas SQL sobre la base PostgreSQL 'Aldrin - PR' en las tablas SACCUSTODIA.MT_CAIXA y trf_s3.cart_caixa_mt_t filtrando por CODCLI = 'CUST2337', devolviendo 143 registros; Función observada en DBeaver: reports_verificar_fundo_publish_demonstrativo_caixa · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png
- 2026-11-04 18:06 — Correo automático — Correo nuevo en el hilo: Marcela C., de Tecnología, solicita verificar el informe "Demonstrativo de Caixa" para el cliente CUST2337, ya que no presenta datos desde julio de 2026. Marco P., consultor senior, está analizando el problema. Adjunta capturas. Detalles: El informe afectado es "Demonstrativo de Caixa" para el cliente CUST2337; Los datos no se muestran desde julio de 2026; Las capturas de pantalla muestran consultas SQL a la tabla "SANCAC"."CAIXA_DEMONSTRATIVO" en el entorno `aldrin-prd-postgres.database.cloud.corp:5432`; Las consultas para el cliente CUST2337 y el periodo julio de 2026 devuelven 143 registros, lo que indica que los datos existen en la base de datos. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png
- 2026-11-04 18:08 — Correo automático — Correo nuevo en el hilo: Marco P., consultor senior, informa que está analizando el problema y responderá pronto. Marcela C., tecnología, ha estado solicitando actualizaciones sobre el informe "Demonstrativo de Caixa" que no muestra datos desde julio de 2026. Matheus D., developer III, había indicado previamente que estaban verificando. Guilherme O. había mencionado que la cantidad de registros en SAC y ALDRIN era la misma. Adjunta capturas. Detalles: El informe afectado es "Demonstrativo de Caixa" (CUST2337); No presenta datos desde julio de 2026; Las capturas muestran consultas SQL a las tablas `sancac.cust2337_demonstrativo_caixa` y `aldrin.pr_carga_sancac.cust_cart_caixa_ct_1`; Se observa un navegador de base de datos con esquemas `sancac` y `aldrin`; Las consultas SQL muestran que existen 143 registros para CUST2337 con fechas a partir de 2026-07-01 en ambas tablas. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png
- 2026-11-04 20:01 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, informa a Marcela C., de Tecnología, que las validaciones realizadas confirman que los datos para el informe están presentes. Solicita evidencias de la extracción del informe para poder analizar el problema. El problema es que el informe 'Demonstrativo de Caixa' no muestra datos desde julio de 2026. Adjunta capturas. Detalles: Cliente afectado: CUST2337; Informe afectado: 'Demonstrativo de Caixa'; Periodo afectado: Desde julio de 2026; Estado actual: Los datos para el informe están presentes en la base de datos, según validaciones; Acción solicitada: Marcela C. debe proporcionar evidencias de la extracción del informe; Las capturas de pantalla muestran un navegador de base de datos PostgreSQL con consultas SQL; Una consulta busca datos para CUST2337 entre 2026-07-01 y 2026-11-01 en la tabla 'Sancac'.'cust_cai_cli'; Otra consulta busca datos para CUST2337 entre 2026-09-01 y 2026-09-30 en la tabla 'cod_cli_cart_caixa_at_1'; Los resultados de ambas consultas muestran registros para el cliente CUST2337 en los periodos consultados. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png

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
- 2026-11-03 12:51 — nuevo → Abierto — Correo automático
- 2026-11-03 13:50 — Abierto → En curso — Matheus Fransoni
- 2026-11-05 12:24 — En curso → Resuelto — Marco Pichardo
- 2026-11-06 12:14 — En curso → Resuelto — Matheus Fransoni

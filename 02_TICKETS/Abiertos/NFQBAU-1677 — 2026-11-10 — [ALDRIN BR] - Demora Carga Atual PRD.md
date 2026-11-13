---
id: NFQBAU-1677
fecha_apertura: 2026-11-10
fecha_limite: 2026-11-10
fecha_resolucion:
estado: En curso
prioridad: Alta
responsable:
origen: email
referencia_origen: "[ALDRIN BR] - Demora Carga Atual PRD (2026-11-10)"
categoria:
  - Rundeck
entorno:
  - Producción
sintoma: La carga actual en producción presenta una demora atípica de 30 minutos.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-12 13:56
actualizado_por: Correo automático
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Matheus D., desarrollador de NFQ, informa que la carga actual está tomando un tiempo atípico de 30 minutos y están investigando el motivo.
Solicita realizar un análisis conjunto con el equipo de S3 para solucionar el problema lo antes posible.

Detalles: Tiempo atípico de ejecución de la carga: 30 minutos

## Histórico de interacciones

- 2026-11-10 12:11 — Correo automático — Matheus D., desarrollador de NFQ, informa que la carga actual está tomando un tiempo atípico de 30 minutos y están investigando el motivo.
Solicita realizar un análisis conjunto con el equipo de S3 para solucionar el problema lo antes posible.
- 2026-11-10 12:17 — Correo automático — Correo nuevo en el hilo: Matheus D., Developer III de NFQ, informa que la carga que presentaba una demora atípica ya ha sido concluida. Acompañará las próximas cargas para asegurar el buen funcionamiento del proceso. Detalles: La carga se demoró 30 minutos; La carga ha sido concluida.
- 2026-11-10 12:21 — Correo automático — Correo nuevo en el hilo: Thiago A., de PR Serviços, indica a Matheus D., de NFQ, que en caso de identificar problemas con las cargas, debe contactar directamente la sala P0, ya que son un punto muy sensible que afecta a los clientes. Esto surge a raíz de una carga que tardó 30 minutos más de lo habitual y que ya ha sido completada. Adjunta una captura. Detalles: La carga actual tardó 30 minutos más de lo habitual; la carga ya ha sido concluida. · Adjuntos del correo: image001.png
- 2026-11-10 12:31 — Correo automático — Correo nuevo en el hilo: Matheus D., Developer III de NFQ, informa que la carga que estaba con demora ya ha concluido. Thiago A., de Sancac, le aconseja usar la sala P0 para problemas futuros debido a la sensibilidad de las cargas para los clientes. Adjunta capturas. Detalles: La carga actual tuvo un tiempo atípico de 30 minutos; la carga fue concluida; se adjunta una captura de pantalla. · Adjuntos del correo: image001.png
- 2026-11-10 12:36 — Correo automático — Correo nuevo en el hilo: Mauricio Roberto L., tecnología de S3 Caceis, avisa que las cargas están más lentas y pide que se revise si alguna implementación reciente afecta al rendimiento. Adjunta capturas. Detalles: adjunta capturas; cargas más lentas esta semana en producción · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-11-10 15:47 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, informa que la lentitud en la carga se debe a modificaciones recientes en los mapeos. Sugiere aplicar las optimizaciones de rendimiento una vez finalizadas las alteraciones y cuando el objeto esté estabilizado. Adjunta capturas. Detalles: Mapeos afectados: cart_pos_rf_t; Causa: aumento del tiempo de ejecución derivado de modificaciones recientes en el objeto; Plan: ejecutar la optimización de performance una vez concluida la etapa de cambios y estabilizado el objeto. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-11-11 12:12 — Correo automático — APROBACIÓN PRD — Correo nuevo en el hilo: Fernando M., cliente de S3 Caceis, aprueba avanzar con la optimización de rendimiento en producción debido a los impactos observados.
Indica que administrarán las nuevas subidas y ajustes técnicos durante el día junto con el equipo de soporte.
Adjunta capturas. Detalles: Mapeo y objeto afectado: cart_pos_rf_t; Atraso considerable en tiempo de ejecución tras cambios recientes; Cargas en producción con tiempo atípico de 30 minutos; Se planifica optimización y administración de subidas durante el día. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-11-11 12:36 — Correo automático — Correo nuevo en el hilo: Matheus D. F., Developer III de NFQ, adjunta una función modificada para su validación, con el objetivo de optimizar y reducir la demora en la carga de datos. Esto sigue a la aprobación de Fernando A. M. J., de S3 Caceis, para proceder con la optimización debido a problemas de rendimiento en producción, que Mauricio R. L., de Tecnología de S3 Caceis, había reportado como cargas más lentas desde esta semana. Adjunta capturas y un fichero. Detalles: La función 'function_meg_cart_pos_rf_t' ha sido modificada para optimización; el fichero adjunto es 'UPDATE function_meg_cart_pos_rf_t_20261111.sql'; el problema afecta a los mapeos, especialmente 'cart_pos_rf_t'; el retraso se observa desde las recientes modificaciones del objeto; adjunta 4 capturas de pantalla. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, UPDATE function_meg_cart_pos_rf_t_20261111.sql
- 2026-11-11 12:37 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador de NFQ, remite para validación una función con modificaciones orientadas a optimizar el rendimiento y mitigar la lentitud de la carga. Adjunta un fichero. Detalles: Función o script: UPDATE function_meg_cart_pos_rf_t_20261111.sql; Mapeo afectado: cart_pos_rf_t · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, UPDATE function_meg_cart_pos_rf_t_20261111.sql
- 2026-11-11 13:16 — Correo automático — Correo nuevo en el hilo: Gustavo B., desarrollo del proveedor, propone ajustes de rendimiento en código SQL para optimizar las cargas en producción. Explica la creación de una tabla temporal indexada para el valor de CDI y la modificación de un JOIN. Adjunta capturas. Detalles: Optimización SQL propuesta: incluir 'drop table if exists cdi' en bucle; añadir la columna dat_ref_cdi en el SELECT de MAX_VALPORCS usando la función trf_s3.data_calc(dat_valuat, -1) para 'Opening NAV'; crear la tabla temporal 'cdi' a partir de trf_s3.sss_refrate_price_t donde cod_reratepr = 'CDI', añadiendo índice y analyze; sustituir el LEFT JOIN de trf_s3.sss_refrate_price_t por 'left join cdi refrate on refrate.dat_prdate = MAX_VALPORCS.dat_ref_cdi'. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image.png
- 2026-11-11 16:28 — Correo automático — Correo nuevo en el hilo: Gustavo B., de PR Serviços, envía una nueva versión del script SQL de la función trf_s3.function_meg_cart_pos_rf_t() con optimizaciones de rendimiento y corrección de joins.
Solicita subir la función corregida al entorno de UAT para ejecutar las pruebas correspondientes antes de pasar el cambio a producción.
Adjunta capturas y un fichero. Detalles: Función afectada: trf_s3.function_meg_cart_pos_rf_t(); Tablas involucradas: TEM_meg_cart_pos_rf_t, trf_s3.sss_refrate_price_t, MAX_VALPORCS, cart_pos_rf_t_err; Cambios realizados: creación de la tabla temporal indexada cdi para obtener la tasa CDI una sola vez por fecha, adición de la columna dat_ref_cdi en MAX_VALPORCS, ajuste del JOIN final y agregado de drop table if exists cdi al inicio del loop; Archivo adjunto: UPDATE function_meg_cart_pos_rf_t_20261111_v2.sql · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image.png, UPDATE function_meg_cart_pos_rf_t_20261111_v2.sql
- 2026-11-11 16:38 — Correo automático — Correo nuevo en el hilo: Marco P., consultor senior de NFQ, consulta a Maurício L. si la propuesta recibida invalida las mejoras de rendimiento en las que están trabajando sobre la función. Aclara que sus cambios no se limitan a joins e índices, sino que incluyen un tratamiento general de clientes. Adjunta capturas. Detalles: Duda sobre la función trf_s3.function_meg_cart_pos_rf_t(); se menciona que los cambios requeridos contemplan inclusión de tratamiento general de clientes además de optimización de joins e índices · Adjuntos del correo: image001.png, image.png, image002.png, image004.png, image003.png
- 2026-11-11 16:56 — Correo automático — Correo nuevo en el hilo: Thiago A., de PR Serviços, aclara a Marco P., consultor de NFQ, que su sugerencia de mejora de rendimiento para la función trf_s3.function_meg_cart_pos_rf_t() es adicional y no reemplaza otros cambios. Previamente, Gustavo B., de PR Serviços, solicitó implementar estas modificaciones en UAT para pruebas, buscando optimizar la carga y corregir la duplicidad de lotes. Adjunta un fichero con la función completa y capturas. Detalles: La función afectada es trf_s3.function_meg_cart_pos_rf_t(). El problema se debe a un LEFT JOIN en el select final que alimenta TEM_meg_cart_pos_rf_t, donde la condición dat_prdate compara con un CASE que llama a trf_s3.data_calc(POSI.DAT_VALUAT, -1). Esto impide el uso de índices y hash join, ejecutando data_calc por cada comparación y duplicando lotes si sss_refrate_price_t tiene más de una línea CDI para la misma fecha, enviándolos a cart_pos_rf_t_err. Las modificaciones propuestas son: 1) Añadir execute 'drop table if exists cdi'; al inicio del loop de clientes. 2) Incluir case when des_process = 'Opening NAV' then trf_s3.data_calc(dat_valuat, -1) else dat_valuat end as dat_ref_cdi en la create temp table MAX_VALPORCS. 3) Crear una nueva tabla temporal cdi con select dat_prdate, max(amt_rate) as amt_rate from trf_s3.sss_refrate_price_t where cod_reratepr = 'CDI' and dat_prdate in (select dat_ref_cdi from MAX_VALPORCS) group by dat_prdate; create index ix_cdi on cdi (dat_prdate); analyze cdi;. 4) Sustituir el LEFT JOIN del CDI en el select final por left join cdi refrate on refrate.dat_prdate = MAX_VALPORCS.dat_ref_cdi. Se espera reducción del tiempo del select final y que los lotes con más de una tasa CDI se graben correctamente en cart_pos_rf_t. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png
- 2026-11-12 11:38 — Correo automático — Correo nuevo en el hilo: Mauricio L., tecnología de S3 Caceis, informa que continúan sufriendo lentitud en las cargas desde el fin de semana. Pide actualizaciones sobre lo que se está haciendo y exige solucionar el rendimiento hoy mismo. Adjunta capturas. Detalles: Sistema ALDRIN BR; Cargas de PRD con tiempo atípico y lentitud desde el fin de semana previo al 2026-11-12; El cliente exige solución en el día; Adjunta imágenes (image001.png, image002.png, image003.png, image004.png) · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-11-12 11:52 — Correo automático — Correo nuevo en el hilo: Matheus F., desarrollador de NFQ, informa a Mauricio L., del área de tecnología del cliente, que la lentitud de la carga proviene de un impacto de rendimiento en la función cart_pos_rf_t. Solicita su visto bueno para continuar con las pruebas de la solución optimizada en UAT. Adjunta capturas. Detalles: Función afectada: cart_pos_rf_t; Causa: alteración reciente en la función que afectó la performance de las cargas; Solución propuesta: propuesta de optimización enviada anteriormente pendiente de pruebas en UAT · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-11-12 12:52 — Correo automático — Correo nuevo en el hilo: Mauricio L., de Tecnología, informa que Gustavo ha sugerido mejoras a la propuesta de optimización enviada ayer y aún no han recibido respuesta. Solicita al equipo de soporte que se unan a una reunión P0 hoy a las 14:30h (BRT) porque necesitan desplegar la solución hoy mismo. Adjunta capturas. Detalles: La lentitud en las cargas de datos persiste desde el fin de semana. La causa es un impacto en la performance de la función cart_pos_rf_t que sufrió una alteración reciente. Se envió una sugerencia de optimización. Gustavo ha propuesto mejoras a la sugerencia. Se requiere una reunión P0 hoy a las 14:30h (BRT) para desplegar la solución hoy. Adjunta 4 capturas de pantalla que muestran el problema o la propuesta. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-11-12 13:56 — Correo automático — Correo nuevo en el hilo: Marco P., Senior Consultant de NFQ, responde a Mauricio L., tecnología del cliente, confirmando que las mejoras planteadas por Gustavo coinciden con la propuesta enviada previamente. Indica que se conectarán a la reunión señalada para alinearse. Adjunta capturas. Detalles: Problema de rendimiento en la función cart_pos_rf_t tras modificación reciente; propuesta de optimización planteada para normalizar la carga y realizar pruebas en UAT · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png

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
- 2026-11-10 12:11 — nuevo → Abierto — Correo automático
- 2026-11-10 17:54 — Abierto → En curso — Matheus Fransoni

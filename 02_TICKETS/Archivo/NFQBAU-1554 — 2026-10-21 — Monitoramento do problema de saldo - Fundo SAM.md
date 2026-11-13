---
id: NFQBAU-1554
fecha_apertura: 2026-10-21
fecha_limite: 2026-10-22
fecha_resolucion: 2026-11-04
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: Monitoramento do problema de saldo - Fundo SAM (2026-10-21)
categoria:
  - Qlik
entorno: []
sintoma: El saldo del día no se muestra de forma intermitente en el informe Demonstrativo de Caixa para el fondo SAM.
solucion_corta: "Se implementó una optimización de rendimiento en el informe para reducir el tiempo de carga y reflejar datos actualizados."
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-08 08:30
actualizado_por: Correo automático
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Ricardo C., de Proyecto Apollo, informa que no lograron reproducir el error puesto que el saldo del día de hoy se mostró con normalidad en el informe. Solicita a Marco P., de NFQ, que el equipo de soporte de la mañana genere el reporte hacia las 8:00 para monitorizarlo y capturar el fallo en tiempo real si vuelve a ocurrir. Adjunta capturas y un fichero.

Detalles: Fondo afectado: SAM (código CUST2152); Pasos indicados: generar el informe Demonstrativo de Caixa alrededor de las 8:00 seleccionando periodo con fecha final igual a la fecha actual para comprobar que aparezca el saldo; Antecedente técnico: en incidencias similares se ajustó el horario del job de Megara que genera la línea de NAV en Supervision Dashboard; Las capturas muestran consultas a la tabla trf_s3.cart_caixa_saldo_t con campos dat_qlikupdate, cod_cli, cod_ord, dat_liq, des_typ, des_hist ('Saldo dia Anterior') y amt_val, así como registros de carga en Aldrin con fecha de llegada 2026-10-14 04:03:00.144 para el saldo de 2026-10-13
Adjuntos del correo: image003.png, image004.png, image005.png, image010.png, image011.png, image012.png, image013.png, image014.png, image015.png, Demonstrativo de Caixa.xlsx

## Histórico de interacciones

- 2026-10-21 10:06 — Correo automático — Ricardo C., de Proyecto Apollo, informa que no lograron reproducir el error puesto que el saldo del día de hoy se mostró con normalidad en el informe. Solicita a Marco P., de NFQ, que el equipo de soporte de la mañana genere el reporte hacia las 8:00 para monitorizarlo y capturar el fallo en tiempo real si vuelve a ocurrir. Adjunta capturas y un fichero.
- 2026-10-21 11:56 — Correo automático — Correo nuevo en el hilo: Christian P., de Tecnología de S3 Caceis, indica que Marco P., de NFQ, ya cuenta con una solución implementada para la incidencia de saldo del fondo SAM. Solicita el envío del paquete de cambios para proceder con su validación. Detalles: Informe: Demonstrativo de Caixa (Demonstrativo de Caixa Portal); Fondo: SAM (código CUST2152); Tablas: trf_s3.cart_caixa_saldo_t, cart_caixa_mt_t; Job de Megara encargado de la línea de NAV en Supervision Dashboard; Base de datos/sistema Aldrin; Se solicita paquete de despliegue con la solución implementada · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png
- 2026-10-22 15:11 — Correo automático — Correo nuevo en el hilo: Ricardo C. del Proyecto Apollo pregunta si la solución implementada para Performance también resuelve el problema de saldo para el fondo SAM. Adjunta capturas. Detalles: Fondo afectado: SAM, CUST2152; Problema: Saldo del día no aparece o es incorrecto en el informe; Ejemplo: Saldo del 13/10 estuvo disponible en Aldrin el 14/10 a las 04:00 BRT, pero el usuario consultó el 14/10 a las 09:33 y el saldo estaba incorrecto; Tablas de BBDD mencionadas: cart_caixa_saldo_t, cart_caixa_mt_t; Job relacionado: Job de Megara que genera la línea NAV del día en la Supervision Dashboard; Pasos para reproducir (sugeridos): Generar el informe alrededor de las 8h; usar el fondo CUST2152 seleccionando un período con fecha final igual a la fecha de generación (ej. hasta 21/10). El saldo de ese día debe aparecer en el informe; Capturas muestran: Una tabla con DATA, MOMENTO EM QUE CHEGOU A ALDRIN, SALDO, destacando que el saldo del 13/10 llegó a Aldrin el 14/10 a las 04:03:00.144; Fragmentos de correo que indican que el cliente consultó el informe el 14/10 a las 09:33 y el saldo estaba incorrecto, a pesar de que la actualización en Aldrin fue a las 04:03; Tablas s3.cart_caixa_mt_t y s3.cart_caixa_saldo_t con datos para CUST2152, mostrando dat_qlikupdate y dat_liq para el 13/10 y 14/10. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png
- 2026-10-22 15:21 — Correo automático — Correo nuevo en el hilo: Christian S., tecnología, pide a Marco P., NFQ, que evalúe y responda a Ricardo C., Proyecto Apollo, sobre el problema de saldo del "Fundo SAM". Ricardo C. tiene dudas si la solución de Performance resuelve el problema. El problema original, escalado por el cliente, es que el saldo del 13/10 no se mostraba correctamente en el informe el 14/10, a pesar de la actualización en Aldrin. Ricardo C. no pudo reproducir el error el 21/10, pero sugiere monitorear el informe por la mañana. Adjunta capturas. Detalles: Fondo afectado: "Fundo SAM", código "CUST2152"; Informes/pantallas afectados: "Demonstrativo de Caixa Portal", "Supervision Dashboard"; Tablas mencionadas: cart_caixa_saldo_t, cart_caixa_mt_t; Fechas/periodos afectados: Saldo del 2026-10-13 no disponible correctamente el 2026-10-14 a las 09:33; Proceso/Job: "job do Megara responsável por gerar a linha de NAV do dia"; Comportamiento: El saldo de cierre del 2026-10-13 estuvo disponible en Aldrin el 2026-10-14 a las 04:03:00.144 (BRT). El cliente consultó el informe el 2026-10-14 a las 09:33 y el saldo era incorrecto; Pasos para reproducir/monitorear: Generar el informe alrededor de las 8h, usando el fondo CUST2152 y seleccionando un periodo con fecha final igual a la fecha de generación; Capturas de pantalla: Muestran una tabla con "DATA", "MOMENTO EN QUE LLEGO A ALDRIN" y "SALDO", resaltando que el saldo del 2026-10-13 llegó a Aldrin el 2026-10-14 a las 04:03:00.144 con un saldo de 5,000.01; otra captura muestra datos de dat_qlikupdate para CUST2152 y dat_liq 2026-10-13. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png
- 2026-10-23 15:31 — Correo automático — Correo nuevo en el hilo: Marco P., Senior Consultant de NFQ, sugiere continuar con una propuesta de mejora de rendimiento para los informes de Qlik. Explica que la ocurrencia del problema es difícil de simular debido a la constante actualización de registros en Aldrin, pero que la mejora resolvería las fallas y retrasos en la recarga de los informes. Adjunta capturas. Detalles: Dificultad para simular la ocurrencia del problema debido a la constante actualización de registros en Aldrin; La implementación de desempeño busca una representación fiel y más rápida de los datos; El rendimiento actual del tiempo de carga del informe en Qlik está sujeto a fallas que retrasan la recarga. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png
- 2026-10-23 15:36 — Correo automático — Correo nuevo en el hilo: Ricardo C., responsable del Proyecto Apollo, acuerda comprobar si el problema de saldos reaparece tras el despliegue en producción de la nueva carga. Sugiere realizar un monitoreo por la mañana si la incidencia vuelve a ocurrir. Adjunta capturas. Detalles: Carga de informes en Qlik y sistema Aldrin; tabla trf_s3.cart_caixa_saldo_t; campos dat_qlikupdate, cod_cli (CUST2152), dat_liq, amt_val y des_hist ('Saldo dia Anterior'); job de Megara que genera la línea de NAV en Supervision Dashboard; capturas de pantalla con registros de actualización y timestamps de consultas SQL. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png
- Se realizó una optimizacion en el infrome de demosntrativo de caixa y actualmente estamos probando un conjunto de masa de datos que s3 ha indicado , con esta optimizacion se puede esperar que los datos sean reflejados en un lapso de tiempo de 2 minutos mitigando asi la dierencia de datos que esta experimentadno el cliente
- 2026-11-08 08:30 — Correo automático — Resolución redactada automáticamente a partir del histórico; revisar.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Se analizó la dificultad de simular el error debido a la constante actualización de registros en Aldrin. Se desarrolló una mejora de rendimiento para los informes de Qlik. Se procedió con el despliegue de la nueva carga y se inició la prueba con un conjunto de datos indicado por S3.

### Cómo se comprobó

No consta en el histórico una validación final, aunque se acordó realizar un monitoreo matutino si la incidencia reaparece.

### Con quién se habló

Ricardo C., Proyecto Apollo; Marco P., Senior Consultant de NFQ; Christian P., Tecnología de S3 Caceis; Christian S., Tecnología.

### Servicios, jobs o tablas tocados

Demonstrativo de Caixa, Demonstrativo de Caixa Portal, Supervision Dashboard, job de Megara, Aldrin, trf_s3.cart_caixa_saldo_t, cart_caixa_mt_t

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-10-21 10:06 — nuevo → Abierto — Correo automático
- 2026-10-26 17:25 — Abierto → En curso — Marco Pichardo
- 2026-11-04 15:40 — En curso → Resuelto — Matheus Fransoni

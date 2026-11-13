---
id: NFQBAU-1545
fecha_apertura: 2026-10-20
fecha_limite: 2026-10-20
fecha_resolucion:
estado: Pruebas cliente UAT
prioridad: Alta
responsable: Deborah Bertoldo
origen: email
referencia_origen: "[ALDRIN] Novo ajuste na função function_meg_cart_pos_fi_t (2026-10-20)"
categoria:
  - BBDD
entorno: [Producción, UAT]
  - Producción
sintoma: Diferencia de segundos en la función de base de datos function_meg_cart_pos_fi_t() dentro de un mismo procesamiento.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-26 17:32
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

Thiago A. solicita ajustar la función 'function_meg_cart_pos_fi_t()' para tomar el número de procesamiento en lugar de la fecha y hora. Señala que se trata de un problema en producción y solicita su priorización. Adjunta un fichero.

Detalles: Función afectada: function_meg_cart_pos_fi_t(); Tablas: trf_s3.sss_position_t, trf_s3.SSS_EST_COM_MGC_T, trf_s3.SSS_EST_COM_SSS_T; Modificación en la tabla temporal MAX_VALPORCS: seleccionar cod_valprocs mediante row_number() over(partition by E.DES_OWNER, E.DAT_VALUAT order by E.DAT_UPDATE desc) en lugar de MAX(e.dat_update); Cambio en la condición de JOIN para enlazar por MAX_VALPORCS.cod_valprocs = e.cod_valprocs
Adjuntos del correo: image001.png

## Histórico de interacciones

- 2026-10-20 14:56 — Correo automático — Thiago A. solicita ajustar la función 'function_meg_cart_pos_fi_t()' para tomar el número de procesamiento en lugar de la fecha y hora. Señala que se trata de un problema en producción y solicita su priorización. Adjunta un fichero.
- 2026-10-21 09:16 — Correo automático — Correo nuevo en el hilo: Kleverson B., del equipo de Tecnología, responde dando su conformidad ('De acordo') para ejecutar en el entorno de producción el ajuste SQL sobre la función solicitada. Detalles: Host: psqlprddatahub03.postgres.database.cloud.corp; Sistema: ALDRIN; Función: function_meg_cart_pos_fi_t; Tabla afectada: trf cart_pos_fi_t (trf_s3.sss_position_t); Ajuste para filtrar por número de procesamiento (cod_valprocs) mediante row_number() en lugar de dat_update · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-10-21 10:16 — Correo automático — Correo nuevo en el hilo: Reinaldo A., de NTT DATA, comunica la ejecución del cambio correspondiente al ticket S3C-22831 en el entorno de producción. Adjunta capturas como evidencia del despliegue exitoso. Detalles: Ticket asociado: S3C-22831; Servidor/Host: psqlprddatahub03.postgres.database.cloud.corp; Objeto modificado: función trf_s3.function_meg_cart_pos_fi_t(); La captura de pantalla muestra la ejecución del script SQL de CREATE OR REPLACE FUNCTION en la base de datos de producción con el resultado exitoso: 'CREATE FUNCTION. Query returned successfully in 826 msec.' · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image.png, image.png
- 2026-10-22 14:22 — Correo automático — Correo nuevo en el hilo: Marco P. (NFQ) informa que el ajuste de la función fue compartido ayer y están esperando la ejecución por parte de NTT. Fernando M. (S3Caceis) había solicitado previamente mayor celeridad en este pedido, que implica subir los ajustes a UAT para validación urgente antes de pasar a producción. Adjunta capturas. Detalles: Nombre de la función: function_meg_cart_pos_fi_t; Tabla cargada: trf cart_pos_fi_t; Sistema: ALDRIN; Host de la base de datos: psqlprddatahub03.postgres.database.cloud.corp; Solicitado por: Thiago A. (PRServicos); Fecha de solicitud original: 2026-10-09; Impacto: Sí, en cliente y otros sistemas; Plan de rollback: Ejecución de código que compila la versión anterior; No habrá indisponibilidad; Responsables de prueba funcional: Thiago (Bulle); Responsables de prueba técnica: Thiago (Bulle) / Marco (NFQ); El ajuste fue compartido el 2026-10-21 y se espera la ejecución por NTT. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-10-22 14:26 — Correo automático — Correo nuevo en el hilo: Kleverson B. pregunta si el ajuste de la función está en Producción, ya que NTT ha enviado varios correos indicando que la solicitud no cumple los estándares. El equipo de soporte está esperando la ejecución por parte de NTT para los ajustes de las funciones Patrfi y pos_fi, que necesitan ser desplegados primero en UAT y luego en Producción con urgencia. Adjunta capturas. Detalles: La función afectada es function_meg_cart_pos_fi_t; Se necesitan ajustes en las funciones Patrfi y pos_fi; NTT ha indicado que la solicitud de ajuste no cumple los estándares; Se adjuntan 5 capturas de pantalla que probablemente muestran el estado o el problema. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png
- 2026-10-22 16:21 — Correo automático — Correo nuevo en el hilo: Fernando A. está gestionando con NTT la obtención de accesos para usuarios y la realización de ajustes en Jira. Además, están negociando con NTT para establecer un proceso de aprobación y solicitud por correo electrónico. Este proceso es crucial para avanzar con los ajustes en las funciones de base de datos, que Thiago A. había solicitado subir a UAT con urgencia para validación antes de producción. Kleverson B. había señalado problemas con solicitudes a NTT que no cumplían el estándar. Adjunta capturas. Detalles: La función afectada es function_meg_cart_pos_fi_t; Se mencionan los ajustes para Patrfi y pos_fi; Se están gestionando accesos y ajustes en Jira; Se negocia un formato de aprobación/solicitud por email con NTT; Kleverson B. adjunta capturas de pantalla que muestran ejemplos de solicitudes de NTT que no cumplen el estándar. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png

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
- 2026-10-20 14:56 — (vacío) → Abierto — Correo automático
- Pendiente atender
- 2026-10-26 17:14 — Abierto → Pruebas cliente UAT — Marco Pichardo

---
id: NFQBAU-1686
fecha_apertura: 2026-11-10
fecha_limite: 2026-11-11
fecha_resolucion:            # obligatoria al pasar a Resuelto
estado: Abierto              # ver 05_GENERAL/listas.json
prioridad: Media
responsable:                 # Nombre Apellido, igual que el fichero en 04_PERSONAS
origen: email
referencia_origen: "[ALDRIN] Novo ajuste na função (2026-11-10)"
categoria: [BBDD]
entorno: [UAT]
sintoma: "Error de sintaxis en la ejecución de la función en la base de datos de UAT."
solucion_corta:              # una línea: qué lo arregló
codigo_relacionado:
  - repo:
    modulo:
    version:                 # tag de PRD cuando se despliegue
tickets_proveedor: []        # notas de 03_PROVEEDORES
decision_relacionada:
referencias_tecnicas: []     # fichas de 00_REFERENCIA_TECNICA que ayudaron
actualizado: 2026-11-10 22:46
actualizado_por: Correo automático
tags: [ticket, bau]
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Thiago A., soporte técnico, indica que el script enviado no es el correcto tras múltiples peticiones y subidas en producción. Sugiere actualizar en UAT la versión actual de producción o generar un nuevo script para el storage accounting.

Detalles: Funciones afectadas: function_meg_sac_pl_cl_patrrf_t y trf_s3.function_meg_cart_pos_rf_t; adjunta capturas de pantalla con error de sintaxis SQL state 42601 en la línea 72 con una coma sobrante.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png

## Histórico de interacciones

- 2026-11-10 19:36 — Correo automático — Thiago A., soporte técnico, indica que el script enviado no es el correcto tras múltiples peticiones y subidas en producción. Sugiere actualizar en UAT la versión actual de producción o generar un nuevo script para el storage accounting.
- 2026-11-10 19:46 — Correo automático — Correo nuevo en el hilo: Marco P. de NFQ adjunta dos scripts SQL y solicita su ejecución en la base de datos de UAT. Esto sigue a un error de ejecución reportado previamente por Pedro G. de NTT y una sugerencia de Thiago A. de PR Serviços de actualizar UAT con la versión de producción de las funciones. Adjunta dos ficheros y varias capturas. Detalles: Los scripts a ejecutar son `function_meg_cart_pos_rf_t.sql` y `function_meg_sac_pl_cl_patrrf_t.sql`; Anteriormente, Pedro G. reportó un "Error en la ejecución" con el mensaje "ERROR: syntax error at or near "," LINE 72: ..." al intentar ejecutar un script; Thiago A. sugirió usar la versión de producción de las funciones `function_meg_sac_pl_cl_patrrf_t` y `trf_s3.function_meg_cart_pos_rf_t` para actualizar UAT; Las capturas muestran código SQL y el mensaje de error de sintaxis. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image.png, function_meg_cart_pos_rf_t.sql, function_meg_sac_pl_cl_patrrf_t.sql
- 2026-11-10 22:13 — Correo automático — Correo nuevo en el hilo: Pedro G., analista de soporte de NTT DATA, confirma la ejecución de los scripts solicitados en la base de datos de UAT. Indica que la tarea corresponde al ticket S3C-23187 y adjunta capturas. Detalles: Ticket: S3C-23187; Ejecución de scripts en la base de datos de UAT; Funciones afectadas en el hilo: function_meg_sac_pl_cl_patrrf_t y trf_s3.function_meg_cart_pos_rf_t; Tabla trf_s3.sss_position_t; Las capturas muestran consola de ejecución de consultas en PostgreSQL y referencia a archivo de rollback · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image.png, image.png, image.png, image.png
- 2026-11-10 22:46 — Correo automático — Correo nuevo en el hilo: Pedro G., analista de soporte de NTT DATA, informa que ejecutará la acción necesaria pero solicita confirmación sobre cuál es el script correcto y en qué base de datos debe aplicarlo. Adjunta capturas. Detalles: Consulta sobre el script a aplicar para las funciones function_meg_sac_pl_cl_patrrf_t y trf_s3.function_meg_cart_pos_rf_t; En capturas previas se muestra un error de sintaxis en PostgreSQL (psqlcerdatahub01): ERROR: syntax error at or near "," LINE 72; Se hace referencia también a un archivo ROLLBACK function_meg_sac... · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image.png

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
- 2026-11-10 19:36 — nuevo → Abierto — Correo automático

---
id: NFQBAU-1646
fecha_apertura: 2026-11-05
fecha_limite: 2026-11-05
fecha_resolucion: 2026-11-10
estado: Resuelto
prioridad: Alta
responsable: Juan Antonio Gascón
origen: email
referencia_origen: "[ALDRIN BR] Incidencias Error Mapeo (2026-11-05)"
categoria:
  - BBDD
entorno: []
sintoma: Fallo en la ejecución del mapeo de la tabla sac_mov_rf_oper debido a un error de desbordamiento de caracteres.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-10 17:54
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

Marco P., consultor senior de NFQ, informa que la función function_meg_sac_mov_rf_oper_t_2 ha fallado hoy durante la ejecución del mapeo. Solicita revisión del error reportado.

Detalles: Tabla afectada: sac_mov_rf_oper; Función: function_meg_sac_mov_rf_oper_t_2; Error: value too long for type character varying(15); Fecha del error: 2026-11-05 16:16.

## Histórico de interacciones

- 2026-11-05 16:48 — Correo automático — Marco P., consultor senior de NFQ, informa que la función function_meg_sac_mov_rf_oper_t_2 ha fallado hoy durante la ejecución del mapeo. Solicita revisión del error reportado.
- 2026-11-05 16:48 — Correo automático — Correo nuevo en el hilo: Marco P., Senior Consultant, informa de un error en la ejecución de un mapeo que afecta a la tabla sac_mov_rf_oper, ocurrido hoy a las 16:16. Kleverson B., Tecnología de S3 Caceis, pregunta en qué campo se produce el error. Adjunta capturas. Detalles: Tabla afectada: sac_mov_rf_oper; Función donde se origina el problema: function_meg_sac_mov_rf_oper_t_2; Fecha y hora del error: hoy 2026-11-05 a las 16:16; Mensaje de error: 'value too long for type character varying(15)'; Kleverson B. pregunta 'Em qual campo?' (En qué campo?) · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-05 17:31 — Correo automático — Correo nuevo en el hilo: Marco P., consultor sénior de NFQ, informa a Kleverson B., tecnología del cliente, que están analizando lo sucedido y enviarán más detalles en breve. Adjunta capturas. Adjuntos del correo: image003.png, image002.png, image001.png
- 2026-11-05 17:41 — Correo automático — Correo nuevo en el hilo: Marco Jesus P., consultor senior, comunica que se ha recibido un error por un valor que excede el límite de 15 caracteres en el campo cod_ord para el cliente CUST4811 en la ejecución del mapeo. Detalles: Campo afectado: cod_ord; Valor recibido: SAT0018759177C4680070 (excede el límite de 15 caracteres); Cliente: CUST4811; Tabla afectada: sac_mov_rf_oper; Función origen: function_meg_sac_mov_rf_oper_t_2; Mensaje de error: value too long for type character varying(15); adjunta capturas · Adjuntos del correo: image003.png, image002.png, image001.png
- 2026-11-05 18:22 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, consulta a Thiago A., de PR Serviços, sobre cómo proceder respecto a la incidencia. Adjunta capturas. Adjuntos del correo: image003.png, image002.png, image001.png
- 2026-11-06 14:31 — Correo automático — Correo nuevo en el hilo: Marco P., consultor sénior, insiste en conocer la acción a tomar por parte del equipo tras detectarse que el campo cod_ord supera los 15 caracteres para un cliente. Detalles: Tabla afectada: sac_mov_rf_oper; Función: function_meg_sac_mov_rf_oper_t_2; Campo: cod_ord; Valor recibido: SAT0018759177C4680070; Límite excedido: character varying(15); Cliente: CUST4811; Mensaje de error: value too long for type character varying(15); adjunta capturas · Adjuntos del correo: image003.png, image002.png, image001.png

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
- 2026-11-05 16:48 — nuevo → Abierto — Correo automático
- 2026-11-05 17:43 — Abierto → Revisión cliente — Marco Pichardo
- 2026-11-06 12:14 — nuevo → Revisión cliente — Matheus Fransoni
- 2026-11-10 17:54 — Revisión cliente → Resuelto — Matheus Fransoni

---
id: NFQBAU-1624
fecha_apertura: 2026-11-04
fecha_limite: 2026-11-07
fecha_resolucion: 2026-11-04
estado: Resuelto
prioridad: Baja
responsable: Matheus Fransoni
origen: email
referencia_origen: "[ALDRIN BR] - Query Batimento (2026-11-04)"
categoria:
  - BBDD
entorno: []
sintoma: Se solicita una query de batimento.
solucion_corta: "Se entregó una consulta SQL para realizar el batimento de datos solicitado."
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []     # fichas de 00_REFERENCIA_TECNICA que ayudaron
actualizado: 2026-11-06 22:43
actualizado_por: Marco Pichardo
tags: [ticket, bau]
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Matheus D., Developer III de NFQ, solicita una query de batimento a Marcos A. B. M. de PR Serviços.

Detalles: Se solicita la query de batimento.

## Histórico de interacciones

- 2026-11-04 15:27 — Correo automático — Matheus D., Developer III de NFQ, solicita una query de batimento a Marcos A. B. M. de PR Serviços.
- 2026-11-04 15:57 — Correo automático — Correo nuevo en el hilo: Marcos A., de PR Serviços, envía a Matheus D., de NFQ, una consulta SQL para batimento de datos, conforme a lo solicitado. Adjunta capturas. Detalles: Consulta SQL compleja para batimento de datos; Incluye tablas como trf_s3.SSS_POSITION_T, trf_s3.s3_interface_control_xml_t, trf_s3.cart_patr_t, trf_s3.sac_pl_cl_patr_t, entre otras; Cliente afectado: CUST3122; Fecha de referencia de los datos: 2026-10-27; Adjunta 3 capturas de pantalla, probablemente mostrando resultados o contexto de la consulta. · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-06 21:06 — Correo automático — Resolución redactada automáticamente a partir del histórico; revisar.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Marcos A. redactó una consulta SQL compleja para el batimento de datos. Se incluyeron las tablas necesarias y se enviaron los resultados junto con capturas de pantalla al solicitante.

### Cómo se comprobó

No consta en el histórico.

### Con quién se habló

Matheus D., Developer III de NFQ; Marcos A. B. M., PR Serviços.

### Servicios, jobs o tablas tocados

trf_s3.SSS_POSITION_T, trf_s3.s3_interface_control_xml_t, trf_s3.cart_patr_t, trf_s3.sac_pl_cl_patr_t

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-11-04 15:27 — nuevo → Abierto — Correo automático
- 2026-11-04 17:33 — Abierto → Resuelto — Marco Pichardo
- 2026-11-06 11:52 — Resuelto → Abierto — Matheus Fransoni
- 2026-11-06 12:14 — Abierto → Resuelto — Matheus Fransoni

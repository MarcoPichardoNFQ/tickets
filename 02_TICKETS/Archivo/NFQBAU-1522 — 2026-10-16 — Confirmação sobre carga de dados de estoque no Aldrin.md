---
id: NFQBAU-1522
fecha_apertura: 2026-10-16
fecha_limite: 2026-10-17
fecha_resolucion: 2026-11-04
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: Confirmação sobre carga de dados de estoque no Aldrin (2026-10-16)
categoria: []
entorno: []
sintoma: El informe de Operaciones con Fondos de Inversión, en la sección de Movimientos, está vacío a pesar de que hay movimientos para el fondo en la fecha actual.
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
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Correo automático'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Ricardo C., Proyecto Apollo, confirma que la formalización enviada por Guilherme V., Tecnología, refleja su posicionamiento para Silvia A. Esta formalización detalla que el informe de Stock ya muestra datos correctos tras ajustes, pero el informe de Operaciones con Fondos de Inversión sigue vacío y requiere análisis. Guilherme V. ha solicitado a Marco P., SENIOR CONSULTANT, que comparta la consulta SQL con Marcos M., Tecnología, para investigar este segundo problema.

## Histórico de interacciones

- 2026-10-16 10:19 — Correo automático — Ricardo C., Proyecto Apollo, confirma que la formalización enviada por Guilherme V., Tecnología, refleja su posicionamiento para Silvia A. Esta formalización detalla que el informe de Stock ya muestra datos correctos tras ajustes, pero el informe de Operaciones con Fondos de Inversión sigue vacío y requiere análisis. Guilherme V. ha solicitado a Marco P., SENIOR CONSULTANT, que comparta la consulta SQL con Marcos M., Tecnología, para investigar este segundo problema.
- 2026-10-16 14:04 — Correo automático — Correo nuevo en el hilo: Deborah Y., desarrolladora de NFQ, envía la traducción de la query para el informe 'Operações com Fundos de Investimento', solicitada por Guilherme V. de Tecnología. Adjunta un fichero `query.sql` y varias capturas. Detalles: Se adjunta la query para el informe 'Operações com Fundos de Investimento', que previamente retornó vacío a pesar de movimientos para el fondo en la fecha actual; El informe 'Estoque de Cotas de Fundos' fue ajustado y muestra datos correctos para el cliente CUST1478, con fechas de 2026-10-09 y 2026-10-13; Se adjunta fichero query.sql y capturas de pantalla del portal de informes (https://www.s3caceis.com.br/portal/active-report/reports) y de un Excel con datos del informe de estoque (columnas dt_aplicacao, cd_cliente, nm_fundo, qt_venda_agendada, qt_bloqueada, qt_cotas, vl_operacao). · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.jpg, image010.png, image011.png, image012.png, image013.png, image014.png, image015.png, image016.png, image017.png, query.sql

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
- 2026-10-16 10:19 — nuevo → Abierto — Correo automático
- 2026-10-17 11:51 — Abierto → En curso — Ricardo Reyes
- 2026-10-21 01:29 — En curso → Revisión cliente — Marco Pichardo
- 2026-11-04 15:29 — Revisión cliente → Resuelto — Matheus Fransoni

---
id: NFQBAU-1543
fecha_apertura: 2026-10-20
fecha_limite: 2026-10-21
fecha_resolucion: 2026-11-04
estado: Resuelto
prioridad: Media
responsable: Deborah Bertoldo
origen: email
referencia_origen: Ingresso e Retirada - Ajuste na API (2026-10-20)
categoria:
  - APIs
entorno:
  - Producción
sintoma: Seguimiento pendiente de respuesta sobre el ajuste solicitado para la API de BancoAgenciaConta.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-04 15:34
actualizado_por: Matheus Fransoni
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Guilherme V., del área de Tecnología, solicita una actualización sobre el estado del ajuste pedido para la API. Consulta si hay algún retorno respecto a la solicitud enviada el pasado 8 de octubre.

Adjuntos del correo: image001.png, image002.png, image003.png

## Histórico de interacciones

- 2026-10-20 12:39 — Correo automático — Guilherme V., del área de Tecnología, solicita una actualización sobre el estado del ajuste pedido para la API. Consulta si hay algún retorno respecto a la solicitud enviada el pasado 8 de octubre.
- 2026-10-23 15:01 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, responde a Guilherme V., del departamento de tecnología, informando que han comenzado a atender de forma prioritaria la solicitud de ajuste en la API. Indica que notificarán en cuanto la tarea esté concluida. Adjunta capturas. Detalles: Endpoint afectado: http://dh-bancoagenciaconta.prd.aks.internal/BancoAgenciaConta/byCodFund?; Modificación solicitada: remover cuentas internas de fondos y mantener solo cuentas externas registradas en MEGARA para la cartera; Sistemas vinculados: Portal y MEGARA · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-10-26 22:36 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, solicita a Guilherme V., del equipo de tecnología, la verificación y autorización para ejecutar código en UAT.
La petición corresponde al proceso de ajuste en la API de BancoAgenciaConta.
Adjunta capturas y un fichero. Detalles: Petición de autorización de ejecución de código en UAT; Ficheros adjuntos: AJUSTE_api_banco_agencia_conta.sql y BKP_api_banco_agencia_conta.sql; API de BancoAgenciaConta · Adjuntos del correo: image001.png, image002.png, image003.png, AJUSTE_api_banco_agencia_conta.sql, BKP_api_banco_agencia_conta.sql

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
- 2026-10-20 12:39 — nuevo → Abierto — Correo automático
- 2026-11-04 15:34 — Abierto → Resuelto — Matheus Fransoni

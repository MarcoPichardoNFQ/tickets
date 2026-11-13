---
id: NFQBAU-1602
fecha_apertura: 2026-10-29
fecha_limite: 2026-10-30
fecha_resolucion: 2026-11-03
estado: Resuelto
prioridad: Media
responsable: Deborah Bertoldo
origen: email
referencia_origen: "[ALDRIN] Novo Ajuste na função cs_cli_cash_account_transf_pc (2026-10-29)"
categoria:
  - BBDD
entorno:
  - Producción
sintoma: Confirmación del ticket S3C-22985 para la implementación en Producción de un ajuste en la función cs_cli_cash_account_transf_pc.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-03 10:05
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

Continúa el hilo del [NFQBAU-1595](../Abiertos/NFQBAU-1595%20—%202026-10-28%20—%20[ALDRIN]%20Novo%20Ajuste%20na%20função%20cs_cli_cash_account_transf_pc.md), cerrado el 2026-10-29: no se reabre, se crea este. Reinaldo R. de NTT DATA confirma el ticket S3C-22985 para la implementación en Producción. Adjunta capturas.

Detalles: Ticket ID: S3C-22985; El ajuste se refiere a la función cs_cli_cash_account_transf_pc para insertar el campo dat_qlikupdate en el sistema ALDRIN; Host de BBDD: psqlprddatahub03.postgres.database.cloud.corp; Adjunta capturas de pantalla mostrando el resultado de una consulta SQL con la columna dat_qlikupdate y la ejecución exitosa de un CREATE OR REPLACE PROCEDURE para la función trf_s3.s3_cs_cli_cash_account_transf_pc.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image.png, image.png

## Histórico de interacciones

- 2026-10-29 19:17 — Correo automático — Continúa el hilo del [NFQBAU-1595](../Abiertos/NFQBAU-1595%20—%202026-10-28%20—%20[ALDRIN]%20Novo%20Ajuste%20na%20função%20cs_cli_cash_account_transf_pc.md), cerrado el 2026-10-29: no se reabre, se crea este. Reinaldo R. de NTT DATA confirma el ticket S3C-22985 para la implementación en Producción. Adjunta capturas.

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
- 2026-10-29 19:17 — nuevo → Abierto — Correo automático
- 2026-11-03 10:05 — Abierto → Resuelto — Matheus Fransoni

---
id: NFQBAU-1619
fecha_apertura: 2026-11-03
fecha_limite: 2026-11-04
fecha_resolucion:
estado: Revisión cliente
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: "[ALDRIN] CashTransferOrder new CashTransferOrder type BookToBookTransferOrder (2026-11-03)"
categoria:
  - Rundeck
entorno:
  - Producción
sintoma: Carga de CashTransferOrder procesada correctamente en UAT, reflejando datos en las tablas intermedias SSS.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-06 13:13
actualizado_por: Ricardo Reyes
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Ado S., tecnología PR Servicos, adjunta las evidencias de la carga de CashTransferOrder en UAT tras las pruebas y solicita el despliegue a producción de dicho elemento.

Detalles: adjunta capturas; Tablas afectadas: SSS_PURECASH_OPIN_T, SSS_PURECASH_BOOK_T, SSS_PURECASH_OPOUT_T; Host: psqlcerdatahub01.postgres.database.cloud.corp; Archivo: CashTransferOrder.xsd
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.gif, image010.png, image020.png, image023.png, image022.png, image011.png, image021.png, image015.png, image025.png, image024.png, image016.png, image018.png, image012.png, image013.png, image017.png, image019.png, image014.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png, image.png

## Histórico de interacciones

- 2026-11-03 16:42 — Correo automático — Ado S., tecnología PR Servicos, adjunta las evidencias de la carga de CashTransferOrder en UAT tras las pruebas y solicita el despliegue a producción de dicho elemento.

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
- 2026-11-03 16:42 — nuevo → Abierto — Correo automático
- 2026-11-04 16:02 — Abierto → En curso — Matheus Fransoni
- 2026-11-05 17:43 — Abierto → Revisión cliente — Marco Pichardo
- 2026-11-06 12:14 — En curso → Revisión cliente — Matheus Fransoni

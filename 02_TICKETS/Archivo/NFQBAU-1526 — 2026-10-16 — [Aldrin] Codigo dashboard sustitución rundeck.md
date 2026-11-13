---
id: NFQBAU-1526
fecha_apertura: 2026-10-16
fecha_limite: 2026-10-19
fecha_resolucion: 2026-10-20
estado: Resuelto
prioridad: Baja
responsable: Marco Pichardo
origen: email
referencia_origen: "[Aldrin] Codigo dashboard sustitución rundeck (2026-10-16)"
categoria:
  - BBDD
entorno:
  - Producción
sintoma: El script SQL no identifica los registros resultantes con el formato correcto en producción.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-20 18:33
actualizado_por: Marco Pichardo
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Correo automático'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marco P., consultor senior de NFQ, solicita revisar en producción el script SQL adjunto porque no formatea adecuadamente los registros resultantes. Asimismo, adjunta capturas y un fichero consultando si la salida mostrada es la esperada.

Detalles: Fichero adjunto: sqldeExtraçãoDados.sql; La captura de pantalla muestra la ejecución en PowerShell de '.\05_GENERAL\Herramientas\comprobar_puesto.ps1' sobre el repositorio 'BAU-NFQ-vault', con validaciones de git, Python 3.12.3, submódulos PRD y UAT, y plugins de Obsidian en estado 'OK', finalizando con 'Todo correcto.'
Adjuntos del correo: image.png, sqldeExtraçãoDados.sql

## Histórico de interacciones

- 2026-10-16 15:41 — Correo automático — Marco P., consultor senior de NFQ, solicita revisar en producción el script SQL adjunto porque no formatea adecuadamente los registros resultantes. Asimismo, adjunta capturas y un fichero consultando si la salida mostrada es la esperada.

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
- 2026-10-16 15:41 — (vacío) → Abierto — Correo automático
- 2026-10-17 11:51 — Abierto → En curso — Ricardo Reyes
- 2026-10-20 18:33 — En curso → Resuelto — Marco Pichardo

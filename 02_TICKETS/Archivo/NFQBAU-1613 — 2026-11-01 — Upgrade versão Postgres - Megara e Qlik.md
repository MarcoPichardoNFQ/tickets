---
id: NFQBAU-1613
fecha_apertura: 2026-11-01
fecha_limite: 2026-11-02
fecha_resolucion: 2026-11-03
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: Upgrade versão Postgres - Megara e Qlik (2026-11-01)
categoria:
  - Rundeck
entorno: []
sintoma: No se reciben cargas de datos en el sistema Aldrin tras el procesamiento en Megara.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-06 22:53
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

Mauricio L., de Tecnología, pregunta si se ha llegado a procesar algún fondo en Megara, indicando que no ha entrado ninguna carga en Aldrin. La consulta se produce tras las pruebas de la ventana de mantenimiento del 1 de noviembre.

Detalles: Sistemas afectados: Megara, Aldrin; Problema: No llegó ninguna carga a Aldrin; Contexto: Ventana de actualización de versión de PostgreSQL en bases de Megara y Qlik del 01/11/2026
Adjuntos del correo: image004.png, image005.png, image006.png, image007.png, image008.png, image009.png

## Histórico de interacciones

- 2026-11-01 13:48 — Correo automático — Mauricio L., de Tecnología, pregunta si se ha llegado a procesar algún fondo en Megara, indicando que no ha entrado ninguna carga en Aldrin. La consulta se produce tras las pruebas de la ventana de mantenimiento del 1 de noviembre.
- 2026-11-01 13:49 — Correo automático — Correo nuevo en el hilo: Mizael C., del área de implantación de fondos de S3, informa de que las pruebas realizadas tras la actualización de PostgreSQL han finalizado con éxito.
No reporta ninguna incidencia ni realiza solicitudes adicionales al equipo de soporte. Detalles: Actualización de versión de PostgreSQL para las bases de datos de Megara y Qlik; pruebas funcionales y de uso completadas con éxito · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png
- 2026-11-01 13:52 — Correo automático — Correo nuevo en el hilo: Mauricio L., del área de tecnología, consulta si se ha procesado algún fondo en Megara.
Indica que no ha llegado ninguna carga a Aldrin durante la jornada de actualización. Detalles: Sistemas afectados: Megara y Aldrin; Consulta sobre procesamiento de fondos; Ausencia de cargas recibidas en Aldrin · Adjuntos del correo: image004.png, image005.png, image006.png, image007.png, image008.png, image009.png
- 2026-11-01 17:52 — Correo automático — Correo nuevo en el hilo: Reinaldo A., de NTT DATA, comunica que la actividad programada para la actualización de PostgreSQL ha concluido con éxito. Confirma que los entornos de Megara, Réplica y DataHub/Qlik han sido migrados y que la replicación está activa. Adjunta capturas. Detalles: Actualización de PostgreSQL de la versión 14 a la 18; Servidores actualizados: Psqlprdmegara02 (Megara Produção), psqlviewprdmegara04 (Megara Réplica) y psqlprddatahub02 (DataHub / Qlik); Se confirma replicación activa; Las capturas muestran el estado de la actualización en los servidores y el estado de la replicación · Adjuntos del correo: image001.png, image002.png, image003.png, image.png, image.png, image.png, image.png, image.png
- 2026-11-01 18:32 — Correo automático — Correo nuevo en el hilo: Christian S., del equipo de tecnología, informa a Mauricio L. de que la carga hacia Aldrin se encontraba desactivada. Explica que tras reactivarla y realizar una carga manual los datos se procesaron correctamente y la validación concluyó sin fallos. Detalles: Carga de Aldrin desactivada; reactivación y ejecución de carga manual; validación concluida sin fallos identificados · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png

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
- 2026-11-01 13:48 — nuevo → Abierto — Correo automático
- 2026-11-03 09:59 — Abierto → Resuelto — Matheus Fransoni

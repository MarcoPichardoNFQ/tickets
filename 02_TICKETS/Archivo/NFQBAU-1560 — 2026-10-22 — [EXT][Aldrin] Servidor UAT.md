---
id: NFQBAU-1560
fecha_apertura: 2026-10-22
fecha_limite: 2026-10-23
fecha_resolucion: 2026-10-22
estado: Resuelto
prioridad: Media
responsable: Ismael Barranco
origen: email
referencia_origen: "[EXT][Aldrin] Servidor UAT (2026-10-22)"
categoria:
  - Rundeck
entorno:
  - UAT
sintoma: Se requiere mantener activo el servicio de Rundeck en el entorno de UAT fuera de su horario habitual.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-22 07:13
actualizado_por: Ricardo Reyes
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Ricardo R., manager de NFQ, solicita soporte para configurar los servicios necesarios de modo que Rundeck UAT permanezca activo de inmediato hasta la noche, cuando debe regresar a su configuración habitual. Indica que cuentan con autorización para pedir modificaciones horarias sin aprobación previa. Adjunta capturas.

Detalles: Servicio afectado: Rundeck UAT; Requerimiento: mantener activo inmediatamente y retornar a configuración habitual por la noche
Adjuntos del correo: image005.jpg, image004.png, image002.png, image001.gif, image003.png, image002.png

## Histórico de interacciones

- 2026-10-22 04:36 — Correo automático — Ricardo R., manager de NFQ, solicita soporte para configurar los servicios necesarios de modo que Rundeck UAT permanezca activo de inmediato hasta la noche, cuando debe regresar a su configuración habitual. Indica que cuentan con autorización para pedir modificaciones horarias sin aprobación previa. Adjunta capturas.
- 2026-10-22 04:41 — Correo automático — Correo nuevo en el hilo: Thiago S., analista de soporte TI de NTT DATA, comunica que el servidor ha sido iniciado y se encuentra activo. Se trata de la confirmación a una solicitud previa para mantener operativo el entorno de Rundeck UAT. Detalles: Servidor iniciado y activo; Rundeck UAT · Adjuntos del correo: image001.gif, image002.png, image003.png, image004.png, image005.jpg

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
- 2026-10-22 04:36 — (vacío) → Abierto — Correo automático
- 2026-10-22 07:13 — Abierto → Resuelto — Ricardo Reyes

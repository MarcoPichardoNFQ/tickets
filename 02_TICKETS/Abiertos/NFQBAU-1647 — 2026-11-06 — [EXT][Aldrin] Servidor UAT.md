---
id: NFQBAU-1647
fecha_apertura: 2026-11-06
fecha_limite: 2026-11-07
fecha_resolucion: 2026-11-06
estado: Resuelto
prioridad: Media
responsable:
origen: email
referencia_origen: "[EXT][Aldrin] Servidor UAT (2026-11-06)"
categoria:
  - Rundeck
entorno:
  - UAT
sintoma: Los servicios de Rundeck UAT y Rundeck DEV requieren permanecer activos fuera de su programación habitual.
solucion_corta: "Se encendieron los servidores de Rundeck UAT y Rundeck DEV según lo solicitado."
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-06 22:44
actualizado_por: Marco Pichardo
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Continúa el hilo del [NFQBAU-1560](../Archivo/NFQBAU-1560%20—%202026-10-22%20—%20[EXT][Aldrin]%20Servidor%20UAT.md), cerrado el 2026-10-22: no se reabre, se crea este. Marco P., consultor senior de NFQ, solicita configurar los servicios necesarios para mantener encendidos Rundeck UAT y Rundeck DEV inmediatamente, restableciendo su horario habitual por la noche. Señala que cuenta con autorización previa para gestionar estos horarios sin aprobaciones adicionales. Adjunta capturas.

Detalles: Servicios afectados: Rundeck UAT y Rundeck DEV; Acción: mantener activos de inmediato y retornar a la configuración habitual durante la noche; Cuenta con autorización de Kleverson
Adjuntos del correo: image003.png, image004.png, image005.jpg, image001.gif, image002.png

## Histórico de interacciones

- 2026-11-06 01:09 — Correo automático — Continúa el hilo del [NFQBAU-1560](../Archivo/NFQBAU-1560%20—%202026-10-22%20—%20[EXT][Aldrin]%20Servidor%20UAT.md), cerrado el 2026-10-22: no se reabre, se crea este. Marco P., consultor senior de NFQ, solicita configurar los servicios necesarios para mantener encendidos Rundeck UAT y Rundeck DEV inmediatamente, restableciendo su horario habitual por la noche. Señala que cuenta con autorización previa para gestionar estos horarios sin aprobaciones adicionales. Adjunta capturas.
- 2026-11-06 01:31 — Correo automático — Correo nuevo en el hilo: Thiago A. de S., IT Support Analyst de iCenter, confirma que los servidores fueron encendidos según lo solicitado. Marco P. F., Senior Consultant de NFQ, había pedido configurar los servicios de Rundeck UAT y DEV para que permanecieran activos. Adjunta capturas. Detalles: Se solicitó configurar los servicios de Rundeck UAT y DEV para que permanecieran activos; Se confirma que los servidores fueron encendidos; Kleverson autorizó las solicitudes de horarios sin aprobación previa; adjunta capturas de pantalla. · Adjuntos del correo: image001.gif, image002.png, image003.png, image004.png, image005.jpg
- 2026-11-06 21:06 — Correo automático — Resolución redactada automáticamente a partir del histórico; revisar.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Se revisó la solicitud de mantener activos los servicios fuera de su programación habitual. Thiago A. de S. confirmó que los servidores fueron encendidos.

### Cómo se comprobó

No consta en el histórico.

### Con quién se habló

Marco P., consultor senior de NFQ; Thiago A. de S., IT Support Analyst de iCenter

### Servicios, jobs o tablas tocados

Rundeck UAT, Rundeck DEV

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-11-06 01:09 — nuevo → Abierto — Correo automático
- 2026-11-06 04:58 — nuevo → Revisión cliente — Marco Pichardo
- 2026-11-06 12:14 — nuevo → Revisión cliente — Matheus Fransoni
- 2026-11-06 12:38 — Revisión cliente → Resuelto — Matheus Fransoni

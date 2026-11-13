---
id: NFQBAU-1563
fecha_apertura: 2026-10-22
fecha_limite: 2026-10-23
fecha_resolucion: 2026-10-26
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: "[Aldrin] Problema VPN (2026-10-22)"
categoria:
  - Otros
entorno: []
sintoma: La VPN no puede abrir una puerta local necesaria para el túnel en el CloudPC de Marco J., indicando que la puerta ya está en uso o bloqueada por una instancia anterior de la aplicación.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-26 17:25
actualizado_por: Marco Pichardo
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Pedro G., analista de soporte de IT de NTT DATA, responde a Marco J., consultor senior de NFQ, sobre un problema con la VPN en su CloudPC. Pedro sugiere reiniciar el CloudPC para resolver el error. Marco había adjuntado una captura del error.

Detalles: El error indica que la VPN intentó abrir una puerta local necesaria para el túnel, pero la encontró en uso o bloqueada por una instancia anterior de la aplicación; Se sugiere reiniciar el CloudPC; Marco J. adjunta una captura de pantalla que muestra el mensaje de error de la VPN en su VDI.
Adjuntos del correo: image.png, image.png

## Histórico de interacciones

- 2026-10-22 19:11 — Correo automático — Pedro G., analista de soporte de IT de NTT DATA, responde a Marco J., consultor senior de NFQ, sobre un problema con la VPN en su CloudPC. Pedro sugiere reiniciar el CloudPC para resolver el error. Marco había adjuntado una captura del error.
- 2026-10-22 19:16 — Correo automático — Correo nuevo en el hilo: Marco P., consultor senior de NFQ, responde para confirmar que la solución propuesta funcionó correctamente y agradece la ayuda.
No hay peticiones pendientes por resolver. Detalles: El usuario confirma que la solución indicada para el fallo de puerto/túnel en la VPN del CloudPC funcionó correctamente. · Adjuntos del correo: image.png, image.png

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo
Se reinició la vpn

### Cómo se comprobó

### Con quién se habló

### Servicios, jobs o tablas tocados

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-10-22 19:11 — (vacío) → Abierto — Correo automático
- 2026-10-26 17:25 — Abierto → Resuelto — Marco Pichardo

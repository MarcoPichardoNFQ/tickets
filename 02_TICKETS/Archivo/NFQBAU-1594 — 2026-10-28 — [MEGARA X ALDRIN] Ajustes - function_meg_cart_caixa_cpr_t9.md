---
id: NFQBAU-1594
fecha_apertura: 2026-10-28
fecha_limite: 2026-10-29
fecha_resolucion: 2026-10-29
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: "[MEGARA X ALDRIN] Ajustes - function_meg_cart_caixa_cpr_t9 (2026-10-28)"
categoria:
  - BBDD
entorno: []
sintoma: Se solicita actualizar los controles de NFQ con la función function_meg_cart_caixa_cpr_t9.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-29 17:28
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

Ado S., de Tecnología, solicita actualizar los controles de NFQ con una función adjunta. Esta función fue modificada de emergencia para el tratamiento específico de fondos XP, cuyas tasas de administración y gestión requieren un tratamiento analítico. El ajuste definitivo está en el backlog de ALDRIN. Adjunta capturas y un fichero.

Detalles: Nombre de la función: function_meg_cart_caixa_cpr_t9; Motivo del cambio: tratamiento específico de fondos XP para tasas de administración y gestión analíticas; El ajuste definitivo está en el backlog de ALDRIN; Adjunta tres capturas de pantalla y el fichero function_meg_cart_caixa_cpr_t9.zip.
Adjuntos del correo: image.png, image.png, image.png, function_meg_cart_caixa_cpr_t9.zip

## Histórico de interacciones

- 2026-10-28 18:46 — Correo automático — Ado S., de Tecnología, solicita actualizar los controles de NFQ con una función adjunta. Esta función fue modificada de emergencia para el tratamiento específico de fondos XP, cuyas tasas de administración y gestión requieren un tratamiento analítico. El ajuste definitivo está en el backlog de ALDRIN. Adjunta capturas y un fichero.

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
- 2026-10-28 18:46 — nuevo → Abierto — Correo automático
- 2026-10-29 17:28 — Abierto → Resuelto — Matheus Fransoni

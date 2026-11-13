---
id: NFQBAU-1515
fecha_apertura: 2026-10-15
fecha_limite: 2026-10-16
fecha_resolucion: 2026-10-26
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: "Re: [Aldrin] Problema demonstrativo de caixa (2026-10-15)"
categoria: []
entorno:
  - UAT
  - Producción
sintoma: El informe de caja no muestra registros para el cliente CUST1234 y el portal lanza un error al intentar generar el informe del cliente CUST6767 para la fecha 2026-10-01.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-26 17:32
actualizado_por: Marco Pichardo
tags:
  - ticket
  - bau
  - persona
nombre: NFQBAU-1515 — 2026-10-15 — [Aldrin] Problema demonstrativo de caixa
rol:
equipo_empresa:
escalado_a:
---

## Tickets como responsable

```dataview
TABLE estado, prioridad, fecha_apertura, fecha_limite
FROM "02_TICKETS"
WHERE responsable = this.file.name
SORT fecha_apertura DESC
```

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Correo automático'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Continúa el hilo del [NFQBAU-1514](../Abiertos/NFQBAU-1514%20—%202026-10-15%20—%20[Aldrin]%20Problema%20demonstrativo%20de%20caixa.md), cerrado el 2026-10-15: no se reabre, se crea este. Marco P., Senior Consultant, indica que los datos del cliente CUST1111 están correctos, pero reporta que el cliente CUST1234 no presenta registros y que la generación para el cliente CUST6767 en la fecha 2026-10-01 arroja un error en el portal. Solicita tratar esta incidencia con relevancia alta y priorización absoluta.

## Histórico de interacciones

- 2026-10-15 16:55 — Correo automático — Continúa el hilo del [NFQBAU-1514](../Abiertos/NFQBAU-1514%20—%202026-10-15%20—%20[Aldrin]%20Problema%20demonstrativo%20de%20caixa.md), cerrado el 2026-10-15: no se reabre, se crea este. Marco P., Senior Consultant, indica que los datos del cliente CUST1111 están correctos, pero reporta que el cliente CUST1234 no presenta registros y que la generación para el cliente CUST6767 en la fecha 2026-10-01 arroja un error en el portal. Solicita tratar esta incidencia con relevancia alta y priorización absoluta.

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
- 2026-10-15 16:55 — (vacío) → Abierto — Correo automático
- 2026-10-17 11:51 — Abierto → En curso — Ricardo Reyes
- 2026-10-20 16:05 — En curso → Pendiente despliegue PRD — Marco Pichardo
- 2026-10-20 16:07 — En curso → Pendiente despliegue PRD — Marco Pichardo
- 2026-10-26 17:32 — Pendiente despliegue PRD → Resuelto — Marco Pichardo

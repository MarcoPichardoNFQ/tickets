---
nombre: Correo automático
rol: Flujo de Workspace Studio que convierte correos del buzón compartido en tickets
equipo_empresa: NFQ
escalado_a:
tags: [persona, bau, sistema]
---

No es una persona: es el autor que firma los tickets y entradas que crea la Action `correo.yml`. Existe como ficha para que el escáner acepte `actualizado_por`.

## Tickets creados por el flujo

```dataview
TABLE estado, responsable, fecha_apertura
FROM "02_TICKETS"
WHERE actualizado_por = this.file.name AND !responsable
SORT fecha_apertura DESC
```

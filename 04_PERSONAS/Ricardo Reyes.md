---
nombre: Ricardo Reyes
rol: Patron
equipo_empresa: Nfq
escalado_a: Dios
tags:
  - persona
  - bau
---

## Tickets como responsable

```dataview
TABLE estado, prioridad, fecha_apertura, fecha_limite
FROM "02_TICKETS"
WHERE responsable = this.file.name
SORT fecha_apertura DESC
```

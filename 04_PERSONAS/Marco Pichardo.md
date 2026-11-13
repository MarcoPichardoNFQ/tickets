---
nombre: Marco Pichardo
rol: Lider
equipo_empresa: Nfq
escalado_a: Ricardo Reyes
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

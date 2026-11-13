<%*
/* Nota de proveedor NTT para un ticket con código (plugin Templater).
   Pregunta el ticket relacionado y mueve la nota a 03_PROVEEDORES. */
const ticket = (await tp.system.prompt("Ticket relacionado (NFQBAU-NNNN)")) || "NFQBAU-NNNN";
const L = JSON.parse(await app.vault.adapter.read("05_GENERAL/listas.json"));
const enZona = new Date(new Date().toLocaleString("en-US", { timeZone: L.zona_horaria }));
const f2 = n => String(n).padStart(2, "0");
const hoy = enZona.getFullYear() + "-" + f2(enZona.getMonth() + 1) + "-" + f2(enZona.getDate()), hora = f2(enZona.getHours()) + ":" + f2(enZona.getMinutes());
await tp.file.move("03_PROVEEDORES/NTT — " + ticket);
-%>
---
proveedor: NTT
ticket_relacionado: <% ticket %>
fecha_apertura: <% hoy %>
estado: Abierto
actualizado:
actualizado_por:
tags: [proveedor, bau]
---

## UAT

- Solicitado: 
- Ticket NTT: (si lo dieron)
- Desplegado: 

Checklist antes de pedir el despliegue:

- [ ] Rollback preparado
- [ ] Backup hecho
- [ ] Ventana acordada

## PRD

- Solicitado: 
- Ticket NTT: (si lo dieron)
- Desplegado: 

Checklist antes de pedir el despliegue:

- [ ] Rollback probado en UAT
- [ ] Backup hecho
- [ ] Ventana acordada
- [ ] APROBACIÓN PRD del cliente registrada en el ticket

## Histórico

- <% hoy %> <% hora %> — <% tp.file.cursor() %>

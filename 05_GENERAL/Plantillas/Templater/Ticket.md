<%*
/* Alta de ticket desde Obsidian con desplegables (plugin Templater).
   Uso: comando "Templater: Create new note from template" → Ticket, o su atajo.
   1. Lee las listas cerradas de listas.json y los responsables de 04_PERSONAS.
   2. Pregunta asunto, prioridad, origen, responsable, categoría y entorno.
   3. Calcula el siguiente NFQBAU-NNNN y la fecha límite por prioridad.
   4. Mueve la nota a 02_TICKETS/Abiertos con el nombre normalizado.
   Hace lo mismo que nuevo_ticket.py y /ticket nuevo, sin terminal ni Claude. */
const L = JSON.parse(await app.vault.adapter.read("05_GENERAL/listas.json"));
const personas = app.vault.getMarkdownFiles()
  .filter(f => f.path.startsWith("04_PERSONAS/")).map(f => f.basename).sort();

const asunto = (await tp.system.prompt("Asunto breve del ticket")) || "Sin asunto";
const prioridad = (await tp.system.suggester(L.prioridad, L.prioridad, false, "Prioridad")) || "Media";
const origen = (await tp.system.suggester(L.origen, L.origen, false, "Origen")) || "email";
const responsable = (await tp.system.suggester(personas, personas, false, "Responsable")) || "";
const categoria = (await tp.system.suggester(L.categoria, L.categoria, false, "Categoría")) || "Otros";
const entorno = (await tp.system.suggester(L.entorno, L.entorno, false, "Entorno")) || "";

const ids = app.vault.getMarkdownFiles()
  .filter(f => f.path.startsWith("02_TICKETS/"))
  .map(f => parseInt((f.basename.match(/^NFQBAU-(\d+)/) || [])[1])).filter(n => !isNaN(n));
const id = "NFQBAU-" + (ids.length ? Math.max(...ids) + 1 : 1500);
// Fecha y hora en la zona del vault (listas.json), no en la del ordenador
const enZona = new Date(new Date().toLocaleString("en-US", { timeZone: L.zona_horaria }));
const f2 = n => String(n).padStart(2, "0");
const fmt = d => d.getFullYear() + "-" + f2(d.getMonth() + 1) + "-" + f2(d.getDate());
const hoy = fmt(enZona);
const hora = f2(enZona.getHours()) + ":" + f2(enZona.getMinutes());
const limite = fmt(new Date(enZona.getTime() + L.dias_limite[prioridad] * 86400000));
// Barra de controles (Meta Bind): misma que controles_ticket() en vault.py
const op = vs => vs.map(v => "option('" + v.replace(/'/g, "\\'") + "')").join(",");
const controles = [
  "> [!abstract] Controles",
  "> Estado `INPUT[inlineSelect(" + op(L.estado) + "):estado]` · Prioridad `INPUT[inlineSelect(" + op(L.prioridad) + "):prioridad]` · Responsable `INPUT[inlineSelect(" + op(personas) + "):responsable]`",
  "> Categoría `INPUT[inlineListSuggester(" + op(L.categoria) + "):categoria]` · Entorno `INPUT[inlineListSuggester(" + op(L.entorno) + "):entorno]`",
  "> `BUTTON[bau-ntt, bau-dashboard]`",
].join("\n");
await tp.file.move("02_TICKETS/Abiertos/" + id + " — " + hoy + " — " + asunto.replace(/[\\/:*?"<>|]/g, "").trim());
// El cursor se coloca al terminar: tp.file.cursor() se pierde porque la nota se mueve de carpeta.
tp.hooks.on_all_templates_executed(async () => {
  const leaf = app.workspace.getLeaf(false);
  await leaf.openFile(tp.config.target_file);
  const ed = app.workspace.activeEditor?.editor;
  if (!ed) return;
  const linea = ed.getValue().split("\n").findIndex(l => l.startsWith("## Resumen"));
  if (linea >= 0) { ed.setCursor({ line: linea + 2, ch: 0 }); ed.focus(); }
});
-%>
---
id: <% id %>
fecha_apertura: <% hoy %>
fecha_limite: <% limite %>
fecha_resolucion:
estado: Abierto
prioridad: <% prioridad %>
responsable: <% responsable %>
origen: <% origen %>
referencia_origen:
categoria: [<% categoria %>]
entorno: [<% entorno %>]
sintoma:
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado:
actualizado_por:
tags: [ticket, bau]
---

<% controles %>

## Resumen


## Histórico de interacciones

- <% hoy %> <% hora %> — <% responsable %> — 

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

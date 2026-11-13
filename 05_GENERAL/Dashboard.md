---
obsidianUIMode: preview    # se abre en modo lectura: infraestructura, se cambia por PR
tags: [dashboard, bau]
---

# Dashboard BAU

`BUTTON[bau-nuevo, bau-ntt, bau-tablero, bau-tabla, bau-buscar]`

> [!abstract] Responsable de guardia
> Los tickets nuevos del correo se asignan a: `INPUT[inlineSelect(option('nadie'),option('Antonio Montoro'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):05_GENERAL/Guardia-de-tickets#responsable]` · [qué es la guardia](Guardia-de-tickets.md)

> [!info] Correo automático
> El buzón se lee cada 5 minutos. Si un correo llegó y no hay ticket: o aún no lo ha leído, o Gemini dijo que no es ticket, o falló y se reintenta. Las tres cosas se ven en la [hoja de correos](https://docs.google.com/spreadsheets/d/1sG8w5RtSBimfSfFYScJNKXRiexN2zCamRy9tkfH5Je0/edit?gid=0#gid=0), pestañas `estado` (última lectura, próxima prevista) y `correos` (una fila por correo con el motivo).

```dataviewjs
// Última huella del correo automático en el vault: el ticket más reciente que creó o actualizó.
const t = dv.pages('"02_TICKETS"').where(p => p.actualizado_por == "Correo automático" && p.actualizado).sort(p => String(p.actualizado), "desc").first();
if (!t) dv.paragraph("Sin tickets por correo todavía.");
else {
  const [f, h] = String(t.actualizado).split(" ");
  const ahoraSP = new Date(new Date().toLocaleString("en-US", { timeZone: "America/Sao_Paulo" }));
  const min = Math.round((ahoraSP - new Date(f + "T" + h + ":00")) / 60000);
  const hace = min < 1 ? "ahora mismo" : min < 120 ? `hace ${min} min` : min < 2880 ? `hace ${Math.round(min / 60)} h` : `hace ${Math.round(min / 1440)} días`;
  dv.paragraph(`Último ticket tocado por el correo automático: [${t.file.name.slice(0, 11)}](${t.file.path.replace(/ /g, "%20")}), ${t.actualizado} (${hace}, hora de São Paulo).`);
}
```




## Hilos con respuesta hoy

Tickets abiertos en los que el correo automático ha añadido una respuesta hoy o ayer, el más reciente primero. Sin avisos en Chat: este es el tablón.

```dataviewjs
// Lee el histórico de cada ticket abierto y se queda con las líneas "Correo nuevo en el hilo" de hoy y ayer (hora de São Paulo).
const ahoraSP = new Date(new Date().toLocaleString("en-US", { timeZone: "America/Sao_Paulo" }));
const dia = d => d.toISOString().slice(0, 10);
const hoy = dia(ahoraSP), ayer = dia(new Date(ahoraSP.getTime() - 86400000));
const filas = [];
for (const p of dv.pages('"02_TICKETS/Abiertos"').where(p => p.estado != "Resuelto")) {
  const texto = await dv.io.load(p.file.path);
  for (const l of texto.split("\n")) {
    const m = l.match(/^- (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}) — Correo automático — Correo nuevo en el hilo: (.*)$/);
    if (m && (m[1] == hoy || m[1] == ayer))
      filas.push([m[1] + " " + m[2], dv.fileLink(p.file.path, false, p.file.name.slice(0, 11)), p.responsable ?? "-", m[3].slice(0, 110) + (m[3].length > 110 ? "…" : "")]);
  }
}
filas.sort((a, b) => b[0].localeCompare(a[0]));
if (filas.length) dv.table(["Cuándo", "Ticket", "Responsable", "Qué dice"], filas);
else dv.paragraph("Sin respuestas en hilos hoy ni ayer.");
```

## En un vistazo

```dataviewjs
// Gráficos con el plugin Charts a partir de Dataview. Se recalculan al abrir.
const L = JSON.parse(await app.vault.adapter.read("05_GENERAL/listas.json"));
const estados = L.estado.filter(e => e !== "Resuelto");
const todos = dv.pages('"02_TICKETS"').where(p => p.file.name.startsWith("NFQBAU-"));
const abiertos = todos.where(p => p.estado && p.estado !== "Resuelto");
const azul = "rgba(54, 162, 235, 0.55)", verde = "rgba(75, 192, 120, 0.55)", rojo = "rgba(255, 99, 132, 0.55)";

// 1. Abiertos por estado
const c1 = this.container.createDiv();
window.renderChart({ type: "bar",
  data: { labels: estados, datasets: [{ label: "Abiertos", data: estados.map(e => abiertos.where(p => p.estado === e).length), backgroundColor: azul }] },
  options: { plugins: { legend: { display: false }, title: { display: true, text: "Abiertos por estado (" + abiertos.length + ")" } }, scales: { y: { beginAtZero: true, ticks: { stepSize: 1 } } } } }, c1);

// 2. Abiertos por responsable
const resp = [...new Set(abiertos.map(p => p.responsable || "(sin responsable)").array())].sort();
const c2 = this.container.createDiv();
window.renderChart({ type: "bar",
  data: { labels: resp, datasets: [{ label: "Abiertos", data: resp.map(r => abiertos.where(p => (p.responsable || "(sin responsable)") === r).length), backgroundColor: verde }] },
  options: { indexAxis: "y", plugins: { legend: { display: false }, title: { display: true, text: "Abiertos por responsable" } }, scales: { x: { beginAtZero: true, ticks: { stepSize: 1 } } } } }, c2);

// 3. Creados y resueltos por semana, últimas 8 semanas
const semana = d => { const x = new Date(d); x.setHours(0,0,0,0); x.setDate(x.getDate() + 3 - ((x.getDay() + 6) % 7)); const y = new Date(x.getFullYear(), 0, 4); return x.getFullYear() + "-W" + String(1 + Math.round(((x - y) / 86400000 - 3 + ((y.getDay() + 6) % 7)) / 7)).padStart(2, "0"); };
const hoy = new Date(); const semanas = [];
for (let i = 7; i >= 0; i--) { const d = new Date(hoy); d.setDate(hoy.getDate() - 7 * i); semanas.push(semana(d)); }
const cuenta = campo => semanas.map(s => todos.where(p => p[campo] && semana(p[campo].toString()) === s).length);
const c3 = this.container.createDiv();
window.renderChart({ type: "line",
  data: { labels: semanas, datasets: [
    { label: "Creados", data: cuenta("fecha_apertura"), borderColor: azul, backgroundColor: azul, tension: 0.3 },
    { label: "Resueltos", data: cuenta("fecha_resolucion"), borderColor: verde, backgroundColor: verde, tension: 0.3 } ] },
  options: { plugins: { title: { display: true, text: "Creados y resueltos por semana" } }, scales: { y: { beginAtZero: true, ticks: { stepSize: 1 } } } } }, c3);
```

Los desplegables para cambiar estado, prioridad o responsable están en la cabecera de cada ticket. Para verlo todo en tabla o en tablero kanban: [Tickets.base](Tickets.base). En el tablero, arrastrar una tarjeta a otra columna cambia su estado.

## Esta semana, desde el domingo

Parcial en vivo de la semana en curso. El informe cerrado de la semana anterior, de domingo a sábado, está en [Informes](Informes/).

```dataviewjs
// Domingo de esta semana en la zona del vault (listas.json), sin depender del reloj del ordenador
const L = JSON.parse(await app.vault.adapter.read("05_GENERAL/listas.json"));
const ahora = new Date(new Date().toLocaleString("en-US", { timeZone: L.zona_horaria }));
const domingo = new Date(ahora); domingo.setDate(ahora.getDate() - ahora.getDay()); domingo.setHours(0, 0, 0, 0);
const iso = d => d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
const desde = iso(domingo);
const todos = dv.pages('"02_TICKETS"').where(p => p.file.name.startsWith("NFQBAU-"));
const creados = todos.where(p => p.fecha_apertura && p.fecha_apertura.toString() >= desde);
const resueltos = todos.where(p => p.fecha_resolucion && p.fecha_resolucion.toString() >= desde);
const abiertos = todos.where(p => p.estado && p.estado !== "Resuelto");
let rechazos = 0;
for (const p of todos) {
  const texto = await dv.io.load(p.file.path);
  for (const m of texto.matchAll(/^- (\d{4}-\d{2}-\d{2})[^\n]*— RECHAZO/gm)) if (m[1] >= desde) rechazos++;
}
dv.paragraph(`**Desde el domingo ${desde}:** ${creados.length} creados · ${resueltos.length} resueltos · ${abiertos.length} abiertos ahora · ${rechazos} rechazos del cliente`);
dv.table(["Creados esta semana", "Estado", "Responsable"], creados.sort(p => p.fecha_apertura, "desc").map(p => [p.file.link, p.estado, p.responsable || "—"]));
```

## Foto para el cliente

Dos tablas listas para copiar: lo resuelto y lo pendiente, con id, asunto y tiempo. Para copiar una tabla: modo lectura, seleccionar y pegar en el correo.

```dataview
TABLE WITHOUT ID
  substring(file.name, 0, 11) AS id,
  regexreplace(file.name, "^NFQBAU-\d+ — \d{4}-\d{2}-\d{2} — ", "") AS asunto,
  fecha_resolucion AS "resuelto el",
  (date(fecha_resolucion) - date(fecha_apertura)).days AS "días"
FROM "02_TICKETS"
WHERE estado = "Resuelto" AND fecha_resolucion
SORT fecha_resolucion DESC
LIMIT 30
```

```dataview
TABLE WITHOUT ID
  substring(file.name, 0, 11) AS id,
  regexreplace(file.name, "^NFQBAU-\d+ — \d{4}-\d{2}-\d{2} — ", "") AS asunto,
  estado,
  (date(today) - date(fecha_apertura)).days AS "días abierto"
FROM "02_TICKETS/Abiertos"
WHERE estado != "Resuelto"
SORT fecha_apertura ASC
```

## Vencidos

```dataview
TABLE responsable, prioridad, fecha_limite, estado
FROM "02_TICKETS/Abiertos"
WHERE fecha_limite AND date(fecha_limite) < date(today) AND (estado = "Abierto" OR estado = "En curso")
SORT fecha_limite ASC
```

## Esperando a NTT

Estados `Pendiente despliegue UAT` y `Pendiente despliegue PRD`, los más antiguos primero.

```dataview
TABLE estado, entorno, (date(today) - date(split(actualizado, " ")[0])).days AS "días esperando", tickets_proveedor
FROM "02_TICKETS/Abiertos"
WHERE contains(estado, "Pendiente despliegue")
SORT actualizado ASC
```

## Esperando al cliente

Estados `Revisión cliente` y `Pruebas cliente UAT`.

```dataview
TABLE estado, responsable, (date(today) - date(split(actualizado, " ")[0])).days AS "días esperando"
FROM "02_TICKETS/Abiertos"
WHERE estado = "Revisión cliente" OR estado = "Pruebas cliente UAT"
SORT actualizado ASC
```

## Abiertos por estado, con días en el estado

```dataview
TABLE rows.file.link AS ticket, rows.responsable AS responsable, rows.dias AS "días en estado"
FROM "02_TICKETS/Abiertos"
WHERE estado != "Resuelto"
FLATTEN (date(today) - date(split(actualizado, " ")[0])).days AS dias
GROUP BY estado
```

## Abiertos por responsable

```dataview
TABLE rows.file.link AS ticket, rows.estado AS estado, rows.fecha_limite AS "fecha límite"
FROM "02_TICKETS/Abiertos"
WHERE estado != "Resuelto"
GROUP BY responsable
```

## Abiertos por categoría

```dataview
TABLE rows.file.link AS ticket, rows.estado AS estado
FROM "02_TICKETS/Abiertos"
WHERE estado != "Resuelto"
FLATTEN categoria
GROUP BY categoria
```

## Abiertos por entorno

```dataview
TABLE rows.file.link AS ticket, rows.estado AS estado
FROM "02_TICKETS/Abiertos"
WHERE estado != "Resuelto"
FLATTEN entorno
GROUP BY entorno
```

## Mis pendientes de hoy

Casillas con fecha dentro de cualquier ticket (plugin Tasks). Sintaxis en una nota: `- [ ] Llamar a NTT 📅 2026-09-30`.

```tasks
not done
due before tomorrow
sort by due
```

## Soluciones

Resueltos por categoría, con síntoma y solución corta. Para buscar un síntoma parecido: `/ticket consultar` en Claude Code o la búsqueda de Obsidian.

```dataview
TABLE rows.file.link AS ticket, rows.sintoma AS síntoma, rows.solucion_corta AS "solución corta"
FROM "02_TICKETS"
WHERE estado = "Resuelto"
FLATTEN categoria
GROUP BY categoria
```

## Top de síntomas

Un síntoma repetido tres veces es candidato a ficha permanente en `00_REFERENCIA_TECNICA/` o a arreglo de raíz.

```dataview
TABLE length(rows) AS veces, rows.file.link AS tickets
FROM "02_TICKETS"
WHERE sintoma
GROUP BY sintoma
SORT length(rows) DESC
LIMIT 10
```

## Resueltos pendientes de archivar

Pasan a `Archivo/` solos a los 30 días de `fecha_resolucion`.

```dataview
TABLE fecha_resolucion, solucion_corta
FROM "02_TICKETS/Abiertos"
WHERE estado = "Resuelto"
SORT fecha_resolucion ASC
```

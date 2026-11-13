<%*
/* Cambia el estado del ticket abierto con un desplegable (plugin Templater).
   Uso: dentro del ticket, "Templater: Insert template" → Cambiar estado.
   Lee los estados de listas.json y escribe el elegido en el frontmatter.
   No inserta texto en la nota. El historial de estados lo apunta el hook. */
// Si se lanzó como "crear nota nueva" (selector de plantillas), no tiene sentido: avisar y borrar la nota vacía.
// Templater "insertar" sustituye la selección del editor: con texto seleccionado no se ejecuta.
const _ed = app.workspace.activeEditor?.editor;
if (_ed && _ed.somethingSelected()) { new Notice("Quita la selección de texto y vuelve a intentarlo", 6000); return; }
if (tp.config.run_mode === 0) {
  new Notice("Abre el ticket y pulsa Cmd/Ctrl+Shift+E", 6000);
  tp.hooks.on_all_templates_executed(async () => { await app.vault.delete(tp.config.target_file); });
  return;
}
const L = JSON.parse(await app.vault.adapter.read("05_GENERAL/listas.json"));
const f = tp.config.target_file;
const actual = app.metadataCache.getFileCache(f)?.frontmatter?.estado ?? "";
const nuevo = await tp.system.suggester(L.estado.map(e => e === actual ? e + "  ← actual" : e), L.estado, false, "Nuevo estado");
if (nuevo && nuevo !== actual) {
  await app.fileManager.processFrontMatter(f, fm => {
    fm.estado = nuevo;
    if (nuevo === "Resuelto" && !fm.fecha_resolucion) fm.fecha_resolucion = tp.date.now("YYYY-MM-DD");
  });
  new Notice(`${f.basename.slice(0, 11)}: ${actual || "(sin estado)"} → ${nuevo}`);
}
-%>

<%*
/* Cambia el responsable del ticket abierto con un desplegable (plugin Templater).
   Uso: dentro del ticket, "Templater: Insert template" → Cambiar responsable.
   Las opciones son las fichas de 04_PERSONAS. No inserta texto en la nota. */
// Si se lanzó como "crear nota nueva" (selector de plantillas), no tiene sentido: avisar y borrar la nota vacía.
// Templater "insertar" sustituye la selección del editor: con texto seleccionado no se ejecuta.
const _ed = app.workspace.activeEditor?.editor;
if (_ed && _ed.somethingSelected()) { new Notice("Quita la selección de texto y vuelve a intentarlo", 6000); return; }
if (tp.config.run_mode === 0) {
  new Notice("Abre el ticket y pulsa Cmd/Ctrl+Shift+R", 6000);
  tp.hooks.on_all_templates_executed(async () => { await app.vault.delete(tp.config.target_file); });
  return;
}
const personas = app.vault.getMarkdownFiles()
  .filter(x => x.path.startsWith("04_PERSONAS/")).map(x => x.basename).sort();
const f = tp.config.target_file;
const nuevo = await tp.system.suggester(personas, personas, false, "Responsable");
if (nuevo) {
  await app.fileManager.processFrontMatter(f, fm => { fm.responsable = nuevo; });
  new Notice(`${f.basename.slice(0, 11)}: responsable → ${nuevo}`);
}
-%>

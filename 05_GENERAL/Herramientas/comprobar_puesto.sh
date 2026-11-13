#!/bin/sh
# Comprobación del puesto (Mac/Linux). Verde o rojo por cada requisito.
# Uso: sh 05_GENERAL/Herramientas/comprobar_puesto.sh
# Activa los hooks versionados si no lo están (es la única acción que hace).
cd "$(dirname "$0")/../.." || exit 1
FALLOS=0
ok()   { printf "  \033[32m✓\033[0m %s\n" "$1"; }
mal()  { printf "  \033[31m✗\033[0m %s\n" "$1"; FALLOS=$((FALLOS+1)); }

echo "Comprobación del puesto: $(pwd)"

# Git y nombre de la persona (lo usa el estampado de actualizado_por)
command -v git >/dev/null 2>&1 && ok "git instalado" || mal "git no está instalado"
[ -n "$(git config user.name)" ] && ok "git user.name: $(git config user.name)" \
  || mal "falta git config user.name \"Nombre Apellido\""

# Python, con el nombre que tenga en este sistema
PY=""; for c in python3 python py; do command -v "$c" >/dev/null 2>&1 && { PY="$c"; break; }; done
[ -n "$PY" ] && ok "Python: $("$PY" --version 2>&1)" || mal "falta Python (python.org)"

# Obsidian (app gráfica) no ve el PATH del terminal: solo /usr/bin:/bin:/usr/sbin:/sbin.
# El hook tiene que funcionar con el Python que haya ahí.
if env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME="$HOME" sh -c 'for c in python3 python; do command -v $c >/dev/null 2>&1 && exec $c -c "import sys; sys.path.insert(0, \"05_GENERAL/Herramientas\"); import vault, estampar, escanear_pii, guardia"; done; exit 1' 2>/dev/null; then
  ok "los scripts funcionan con el Python que ve Obsidian"
else mal "el Python que ve Obsidian (/usr/bin/python3) no puede ejecutar los scripts: instala Xcode Command Line Tools (xcode-select --install)"; fi

# Hooks versionados: se activan aquí mismo si hace falta
if [ "$(git config core.hooksPath)" = ".githooks" ]; then ok "hooks activados (.githooks)"
else git config core.hooksPath .githooks && ok "hooks activados ahora (.githooks)"; fi
git config merge.guardia.driver "sh .githooks/fusionar-guardia %A %B" && git config merge.ticket.driver "sh .githooks/fusionar-ticket %O %A %B" && ok "fusión automática de la nota de guardia y de los tickets"

# El hook debe tener finales de línea LF (en Mac siempre; el chequeo es por simetría con Windows)
git ls-files --eol .githooks/pre-commit | grep -q "w/lf" && ok "hook con finales de línea LF" || mal "el hook tiene CRLF: rm .githooks/pre-commit && git checkout -- .githooks/pre-commit"

# Submódulos del código
[ -f 06_CODIGO_VERSIONADO/PRD/README.md ] && ok "submódulo PRD presente" \
  || mal "submódulo PRD vacío: git submodule update --init --recursive"
[ -f 06_CODIGO_VERSIONADO/UAT/README.md ] && ok "submódulo UAT presente" \
  || mal "submódulo UAT vacío: git submodule update --init --recursive"

# Plugins de Obsidian (viajan en el repo; solo hay que aceptarlos en Obsidian)
for p in dataview obsidian-git templater-obsidian omnisearch homepage obsidian-tasks-plugin table-editor-obsidian obsidian-meta-bind-plugin obsidian-charts obsidian-icon-folder; do
  [ -f ".obsidian/plugins/$p/main.js" ] && ok "plugin $p en el repo" || mal "falta plugin $p"
done

# Rutas largas (solo importa en Windows, pero no molesta)
[ "$(git config core.longpaths)" = "true" ] && ok "core.longpaths activo" || git config core.longpaths true

[ $FALLOS -eq 0 ] && echo "Todo correcto." || { echo "$FALLOS problema(s)."; exit 1; }

# Comprobación del puesto (Windows, PowerShell). Verde o rojo por cada requisito.
# Uso: powershell -ExecutionPolicy Bypass -File 05_GENERAL\Herramientas\comprobar_puesto.ps1
# Activa los hooks versionados si no lo están (es la única acción que hace).
Set-Location (Join-Path $PSScriptRoot "..\..")
$fallos = 0
function Ok($m)  { Write-Host "  OK  $m" -ForegroundColor Green }
function Mal($m) { Write-Host "  X   $m" -ForegroundColor Red; $script:fallos++ }

Write-Host "Comprobación del puesto: $(Get-Location)"

# Git para Windows y nombre de la persona
if (Get-Command git -ErrorAction SilentlyContinue) { Ok "git instalado" } else { Mal "falta Git para Windows (git-scm.com)" }
$nombre = git config user.name
if ($nombre) { Ok "git user.name: $nombre" } else { Mal 'falta git config user.name "Nombre Apellido"' }

# Python: se comprueba desde el shell de Git, que es el que ejecuta el hook, y probando que
# el candidato ejecuta Python de verdad (los alias de la Microsoft Store existen pero no lo son)
# sh.exe se busca subiendo desde git.exe: Git\cmd\git.exe o Git\mingw64\bin\git.exe (instalación
# por usuario) tienen el shell en Git\bin\sh.exe o Git\usr\bin\sh.exe.
$sh = $null; $dir = Split-Path (Get-Command git).Source
for ($i = 0; $i -lt 4 -and -not $sh; $i++) {
  foreach ($c in @("bin\sh.exe", "usr\bin\sh.exe")) { $cand = Join-Path $dir $c; if (Test-Path $cand) { $sh = $cand; break } }
  $dir = Split-Path $dir
}
if (-not $sh) { Mal "no encuentro sh.exe junto a Git (hace falta Git para Windows completo, no solo git.exe)"; $sh = "sh" }
# Misma prueba que el hook: salida capturada, sin >/dev/null (el shell de 32 bits devuelve 127 en bucles)
$py = & $sh -c 'for c in py python3 python; do v=$($c -V 2>&1); case $v in Python*) echo $c; break;; esac; done' 2>$null
if ($py) { Ok "Python desde el shell de Git: $py ($(& $sh -c "$py --version" 2>&1))" }
else { Mal "el hook no encuentra un Python que funcione. Instala Python (python.org, 'Add to PATH') y desactiva en Windows los alias de ejecución python.exe y python3.exe (Configuración > Aplicaciones > Alias de ejecución de aplicaciones)" }

# Hooks versionados
if (Test-Path .githooks\python-ruta.txt) { $r = (Get-Content .githooks\python-ruta.txt -First 1).Trim(); if (& $r -V 2>&1) { Ok "python-ruta.txt: $r" } else { Mal "python-ruta.txt apunta a algo que no es Python: $r" } }
if ((git config core.hooksPath) -eq ".githooks") { Ok "hooks activados (.githooks)" }
else { git config core.hooksPath .githooks; Ok "hooks activados ahora (.githooks)" }
git config merge.guardia.driver "sh .githooks/fusionar-guardia %A %B"; git config merge.ticket.driver "sh .githooks/fusionar-ticket %O %A %B"; Ok "fusión automática de la nota de guardia y de los tickets"
# El hook es un script de shell: con finales de línea CRLF, Git no lo ejecuta y los commits pasan sin control
$eol = git ls-files --eol .githooks/pre-commit
if ($eol -match "w/lf") { Ok "hook con finales de línea LF" }
else { Mal "el hook tiene finales de línea CRLF y no se ejecutará: git pull; del .githooks\pre-commit; git checkout -- .githooks/pre-commit" }

# Submódulos del código
if (Test-Path "06_CODIGO_VERSIONADO\PRD\README.md") { Ok "submódulo PRD presente" } else { Mal "submódulo PRD vacío: git submodule update --init --recursive" }
if (Test-Path "06_CODIGO_VERSIONADO\UAT\README.md") { Ok "submódulo UAT presente" } else { Mal "submódulo UAT vacío: git submodule update --init --recursive" }

# Plugins de Obsidian
foreach ($p in "dataview", "obsidian-git", "templater-obsidian", "omnisearch", "homepage", "obsidian-tasks-plugin", "table-editor-obsidian", "obsidian-meta-bind-plugin", "obsidian-charts", "obsidian-icon-folder") {
  if (Test-Path ".obsidian\plugins\$p\main.js") { Ok "plugin $p en el repo" } else { Mal "falta plugin $p" }
}

# Rutas largas: Git y sistema (la de sistema necesita administrador)
if ((git config core.longpaths) -ne "true") { git config core.longpaths true }
Ok "core.longpaths activo"
$lp = Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name LongPathsEnabled -ErrorAction SilentlyContinue
if ($lp.LongPathsEnabled -eq 1) { Ok "rutas largas de Windows activas" }
else { Mal "rutas largas de Windows desactivadas: ejecutar como administrador: New-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem -Name LongPathsEnabled -Value 1 -PropertyType DWORD -Force" }

if ($fallos -eq 0) { Write-Host "Todo correcto." } else { Write-Host "$fallos problema(s)."; exit 1 }

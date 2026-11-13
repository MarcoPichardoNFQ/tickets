# CLAUDE.md — Vault de soporte BAU (NFQ)

Manual operativo para Claude en este repo. El diseño completo está en `05_GENERAL/Diseno-Vault-BAU-NFQ.md`; el cómo, en `05_GENERAL/Manual-tecnico.md`; el uso, en `05_GENERAL/Manual-de-usuario.md`.

## Qué es

Vault Obsidian sincronizado por Git para soporte BAU de un único cliente. ~10 tickets/día. Lo escribe todo el equipo; Claude completa lo que la persona no rellena, anonimiza lo que se pega y busca lo que ya se resolvió antes. El código va en otro repo, `BAU-NFQ`, montado como submódulo en `06_CODIGO_VERSIONADO/PRD` y `UAT`.

## Dos capas

La persona decide solo `estado`, `prioridad` y `responsable`. Claude rellena el resto (categoría, entorno, síntoma, referencia de origen, código relacionado, referencias técnicas, resumen) y **lo propone para confirmar antes de escribir**. No inventes valores: si no se deduce del contenido, déjalo vacío.

## Datos personales y credenciales: regla dura

- Permitido: nombres y apellidos de personas.
- Prohibido en cualquier zona 01 a 06 y en cualquier commit: emails, teléfonos, DNI/NIE, IBAN, direcciones, cualquier dato que permita identificar o contactar a alguien; y credenciales de cualquier sistema.
- Cuando el usuario pegue un email o texto de una llamada: **resume y anonimiza antes de escribir**. Nunca guardes el texto en crudo. Las personas del correo se citan como **nombre e inicial del apellido más su rol**: "José Carlos N., contabilidad de fondos del cliente", "Ricardo C., responsable del Proyecto Apollo". Nunca el apellido completo ni ningún dato de contacto. Una credencial se sustituye por el nombre del sistema o de la variable.
- El historial de Git es inmutable. Un dato personal en un fichero aún no commiteado se quita antes de nada.
- Tres redes: el hook de Claude Code escanea cada fichero que escribes; el hook de Git bloquea el commit; la Action avisa en el push. Puedes ejecutar `python3 05_GENERAL/Herramientas/escanear_pii.py` para comprobar.

## Convenciones

- Enlaces Markdown relativos con `%20` para espacios. Nunca wikilinks, ni en frontmatter. `responsable` y `actualizado_por` son texto plano igual al nombre del fichero en `04_PERSONAS/`.
- Carpetas sin acentos. Los ficheros pueden llevarlos.
- Ticket: `02_TICKETS/Abiertos/NFQBAU-NNNN — AAAA-MM-DD — Asunto.md`. Id correlativo desde 1500 = máximo existente + 1 (`nuevo_ticket.py`). No hay contador.
- Valores cerrados en `05_GENERAL/listas.json`. Solo esos. Estados: Abierto → En curso → Revisión cliente → Pendiente despliegue UAT → Pruebas cliente UAT → Pendiente despliegue PRD → Resuelto. Un rechazo devuelve a En curso.
- `actualizado`, `actualizado_por` y `## Historial de estados` los estampa el hook: no los escribas. El hook también añade `UAT` a `entorno` en los estados de UAT y `Producción` en el de PRD.
- Histórico de interacciones: `- AAAA-MM-DD HH:MM — Nombre Apellido — texto`. Prefijos fijos cuando toque: `APROBACIÓN`, `APROBACIÓN UAT`, `APROBACIÓN PRD`, `RECHAZO`.
- Estado por correo: en un hilo vivo, el correo mueve el estado según el `evento` que detecta Gemini, solo desde el estado esperado (aprobación, despliegue en UAT, aprobación UAT o PRD, rechazo) y **nunca a Resuelto**; cuando NTT confirma PRD, Chat avisa para que una persona lo cierre. Cada cambio avisa en Chat.
- Al pasar a `Resuelto`: `fecha_resolucion`, `sintoma`, `solucion_corta` y los cinco bloques de `## Resolución`. Lo que la persona no rellene lo redacta esa noche `resolucion.yml` desde el histórico, marcado para revisar. Si hubo código, el rollback del `## Paquete de despliegue` es obligatorio.
- **Un ticket cerrado no se reabre automáticamente.** Si llega una actualización de un hilo cuyo ticket está Resuelto, se crea un ticket nuevo que enlaza al anterior. Reabrir solo si la persona lo pide con esas palabras.
- **Peticiones de sala** (asunto con "sala de projetos", "WR P0/P1", "P0", "P1"): cada correo sin Re: es una llamada y un ticket que nace Resuelto con categoría `Sala`, para contar las llamadas atendidas. Un Re: a una sala de hoy o ayer va a su histórico aunque esté Resuelta: es la misma llamada, no se reabre. Si en la llamada sale una incidencia, se abre un ticket aparte. No se redactan resoluciones de salas.
- Proveedor: cada ticket con código tiene una nota `03_PROVEEDORES/NTT — NFQBAU-NNNN.md` con Solicitado / Ticket NTT (opcional) / Desplegado por entorno.
- Decisiones (`01_DECISIONES/`) van por rama + PR. El hook bloquea commits en `main`.
- `00_REFERENCIA_TECNICA/` es solo lectura. Úsala para resolver y cítala en `### Referencias técnicas usadas y por qué` y en `referencias_tecnicas`.
- `06_CODIGO_VERSIONADO/` se lee, no se edita desde aquí. Ticket de UAT enlaza a `UAT/`, de Producción a `PRD/`.
- Responsable de guardia: `05_GENERAL/Guardia-de-tickets.md` dice quién atiende los tickets nuevos del correo (vale 12 horas desde su marca; `vault.de_guardia()`). Lo cambia la persona desde el Dashboard; no lo escribas tú.
- Este vault es el proyecto. No escribas, muevas ni borres nada fuera de esta carpeta sin avisar y esperar confirmación.

## Estilo

- **Sin emojis** en código ni en nada que el código produzca: avisos de Chat, salidas de scripts, comentarios. Prefijos en texto plano ("Vencido:", "Ticket nuevo:").
- **Control de tickets, no de personas.** Ningún texto, campo ni aviso puede sonar a control horario: nada de "fichar", "entrada y salida", "nadie ha fichado". Se habla de responsable de guardia, de asumir o dejar la guardia, de tickets sin responsable.

## Zona protegida y modo mantenimiento

El trabajo diario toca solo `01_` a `04_` y `05_GENERAL/Informes/`. Todo lo demás es infraestructura: herramientas, plantillas, `listas.json`, hooks, Actions, `.obsidian/`, `.claude/`, manuales, diseño, diagramas, `00_` y `06_`. **No la cambies para salir de un problema puntual.** Un hook `PreToolUse` (`guardia.py`) bloquea cualquier escritura ahí, y el pre-commit descarta los cambios en esos ficheros en `main` (el commit sigue con el resto). Los manuales, el diseño y el Dashboard llevan `obsidianUIMode: preview` para abrirse en lectura.

Si al resolver un ticket crees que hace falta un cambio de infraestructura: resuelve el ticket con lo que hay y **propón** el cambio en una frase. La persona decide. Si acepta, ella crea `.claude/mantenimiento` desde su terminal, tú creas la rama `mantenimiento/<qué>`, haces el cambio y va por PR. **Nunca crees `.claude/mantenimiento` tú mismo**, ni uses `--no-verify`, ni sortees la guardia por Bash.

## Comando `/ticket`

Definido en `.claude/skills/ticket/SKILL.md`. Modos: `nuevo`, `actualizar`, `resolver`, `consultar`, `redactar`. Siempre propone y espera confirmación antes de escribir.

## Correos

Todos los correos del BAU, al cliente y a NTT, van en **portugués de Brasil**, sin preguntar idioma. **Sin firma**: cada persona tiene la suya en su cliente de correo; el borrador termina en "Atenciosamente,".

## Herramientas (`05_GENERAL/Herramientas/`)

| Script | Para qué |
|---|---|
| `nuevo_ticket.py "Asunto" [prioridad] [origen]` | Crea el ticket con el siguiente id y la fecha límite |
| `escanear_pii.py [ficheros]` | PII, credenciales, listas, personas, ids duplicados. Sale 1 si encuentra |
| `estampar.py` | Lo llama el hook; no lo ejecutes a mano |
| `archivar.py` | Resueltos con 7 días o más → Archivo (la Action diaria lo hace sola) |
| `redactar_resolucion.py` | Borrador de resolución de los Resueltos sin documentar (la Action nocturna, con Gemini) |
| `informe_semanal.py` | Informe en `05_GENERAL/Informes/` (también la Action del lunes) |
| `bau.py [--statusline\|--aviso]` | Pulso del día en terminal, barra de Claude Code, aviso de Google Chat |
| `comprobar_puesto.sh` / `.ps1` | Verificación del puesto |
| `guardia.py` | Lo llaman los hooks; bloquea la zona protegida. No lo ejecutes a mano |

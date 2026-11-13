# Base de conocimiento BAU — Aldrin AS-IS (legacy)

Fase 0: inventario de fuentes + índice de fichas. **Pendiente de validación.**

Destino: NotebookLM. Consumidor: equipo de soporte BAU.
Ámbito: el sistema tal como corre hoy en producción, incluidos Qlik, BULLE/SAC/FIDC,
la capa Java y los `load_*` no migrados. No documenta Megara (la solución nueva).

Regla de secretos: se documentan rutas, hosts, usuarios y nombres de variable.
**Nunca se transcribe una contraseña, token, clave privada ni cadena de conexión completa.**

---

## 1. Inventario de fuentes reales

| Fuente | Volumen | Qué permite documentar |
|---|---|---|
| `1_contexto_y_docs/Documento de Arquitectura...md` | 112 líneas | Mapa maestro de los 6 pasos del flujo. Es el esqueleto de todo lo demás. |
| `5_orquestacion_rundeck/*.xml` | 46 jobs exportados | Orquestación real: flags, bloques, mapeos, cierre, validaciones. |
| `4_base_de_datos/BBDD.sql` | 108.724 líneas | DDL completo: tablas, columnas, PKs, FKs, índices, secuencias. |
| `4_base_de_datos/procedures/` | 501 procs (20 `stg_s3` + 480 `trf_s3`) | Lógica de carga, validación, descarte y transformación. |
| `4_base_de_datos/exp_s3.sql` + `exp_s3.tablas_mapeio_t.sql` | 468 líneas | Capa de mapeos y su tabla de control (`activo_inactivo`). |
| `2_config_y_lookups/lookup_*.txt` | java 148 / stg 573 / trf 582 / qlik 265 / flags 9 | Los diccionarios que gobiernan qué se carga y en qué orden. |
| `2_config_y_lookups/env.properties` | 15 líneas | Rutas reales de landing, temporal, unmatched, processed, flags, certificados Qlik. |
| `3_scripts_motores/*.sh` | 5 scripts, 630 líneas | Mecánica bash de flags, conversión Java y carga STG/TRF. |
| `3_scripts_motores/xmlConversor/` | JAR desensamblado | Conversor XML→plano. **Ver hueco H-1.** |
| `6_datos_muestra/` | 714 XML + 148 XSD | Ejemplos reales de cada interfaz y sus esquemas de validación. |
| `7_planeacion_proyecto/catalogo_fase0/*.csv` | tablas 1.956 / funciones 510 / grafo transf. 301 / grafo mapeos 75 | Catálogos ya extraídos: ahorra recorrer el DDL a mano. |
| `2_config_y_lookups/credentials.properties` | 157 bytes | Sólo para saber **qué** credencial existe y dónde vive. Valores no se copian. |

## 2. Huecos declarados

Se documentan igual, marcados como hueco, para que BAU sepa que existe la pieza aunque falte el detalle.

- ~~**H-1 — `xmlConversor.jar` sin desensamblar.**~~ **CERRADO.** Decompilado con CFR 0.152; fuente completa en `fuentes/xmlConversor_main_decompilado.java` (603 líneas). La lógica interna del conversor queda documentable al 100%.
- ~~**H-2 — Job "Recarga Qlik" no exportado.**~~ **CERRADO — no es un job.** Es un *paso* (`<command><description>Recarga Qlik</description>`) embebido en dos jobs que sí están exportados: `0999_-._Optimizacao_Blocos_Rundeck_V6.xml:190` y `JobsArchivosFlag.xml:53`. Por eso no aparecía como archivo propio.
- **H-3 — Micro-jobs individuales no exportados.** El documento cita 132 jobs de conversión Java y 64 de mapeo; en el repo hay 1 ejemplo de cada (`0020_-_CONV_JAVA_TAX_PAY_CAT.xml`, `35_mapeo_sac_pl_cl_patrrf_t.xml`). Son plantillas repetidas, así que se documenta el patrón + el listado completo de nombres. Suficiente para BAU.
- **H-4 — `3_scripts_motores/config.properties` tiene una ruta de pruebas local**, no la de producción. La ficha usará la ruta real de `env.properties`, no ésta.
- **H-5 — Sin histórico de incidencias.** No hay tickets ni entrevistas en el alcance. Los runbooks se derivan de los mecanismos de error del propio código (tablas `_DES`/`_ERR`, `aud_log_trace_t`, control de flags, captura de deadlock), no de frecuencia real observada. Un runbook dirá "esto es lo que puede fallar y cómo se diagnostica", no "esto falla 3 veces por semana".
- **H-6 — `_00001_Análise_de_erros` está anulado en producción con `WHERE 1=0`.** Su silencio no prueba que no haya errores. Va con advertencia explícita en su ficha; es exactamente el tipo de trampa que quema a un BAU nuevo.

## 3. Plantilla de ficha

Cada ficha es un `.md` corto y autónomo. NotebookLM cita por fuente, así que cada archivo debe
responder bien una sola pregunta y repetir el contexto mínimo en vez de depender de vecinos.

```markdown
# [Título — la pregunta que responde]

**Etapa:** Recepción de flags | Conversión Java | Carga STG | Validación | Transformación TRF | Mapeos | Cierre y Qlik | Transversal
**Tipo:** Referencia | Runbook
**Palabras clave:** flag, controlflag_arquivos, MEGAACCOUNTING, ...

## En una línea
[Respuesta corta, para quien sólo lee esto.]

## Detalle
[El cuerpo: mecánica, tablas, rutas, jobs, parámetros.]

## Cómo verificarlo
[Consulta SQL, comando o ruta concreta que confirma el estado.]

## Ver también
[Otras fichas por nombre exacto.]
```

Los runbooks añaden: **Síntoma → Qué mirar primero → Causas probables (ordenadas) → Acción → Cuándo escalar.**

## 4-bis. Capa de runbooks — los 5 dolores reales de BAU

Definidos por el usuario como lo que más tiempo consume hoy. Mandan sobre el resto del índice:
la capa de referencia existe para sostener estas fichas, no al revés.

### R1. Descartes — 12
1. `R1.01` Qué es un descarte y en qué se diferencia de un error
2. `R1.02` Dónde cae cada cosa: `_DES`, `_ERR` y `AUD_LOAD_VALID_TRACE_T`
3. `R1.03` Identificar qué validación descartó la fila
4. `R1.04` Descarte por nulo obligatorio
5. `R1.05` Descarte por formato — `PAR_MAESTRO_MASK_T`
6. `R1.06` Descarte por integridad referencial — `PAR_MAESTRO_VALID_T`
7. `R1.07` Descarte por variación anómala de volumen
8. `R1.08` Descartes en la capa de mapeos: mecanismo distinto al de STG
9. `R1.09` Reprocesar descartes con `fn_reproceso_descart`
10. `R1.10` Cuándo un descarte es correcto y no hay nada que hacer
11. `R1.11` Consultas: cuántos descartes hoy, por tabla y por causa
12. `R1.12` Descarte masivo de una interfaz completa: qué mirar y cuándo escalar

### R2. Duplicados — 9
1. `R2.01` Cómo se detectan: `validate_rows_key_fn` y `CHK_CLAVE`
2. `R2.02` Leer `AUD_LOAD_VALID_TRACE_T` con `DES_VALIDATE='DUPLICADOS'`
3. `R2.03` Duplicado dentro del archivo vs. duplicado entre cargas
4. `R2.04` El archivo llegó dos veces: cómo confirmarlo
5. `R2.05` Duplicados provocados por relanzar un bloque
6. `R2.06` Duplicados en mapeos: clave natural y `ON CONFLICT`
7. `R2.07` Limpiar sin romper: qué se puede borrar y qué no
8. `R2.08` Consultas de diagnóstico
9. `R2.09` Qué provoca duplicados y cómo evitarlos

### R3. Errores de mapeo — 12
1. `R3.01` Anatomía de un fallo de mapeo
2. `R3.02` `Job_control_errores_mapeo`: qué vigila y qué reporta
3. `R3.03` Deadlock `40P01` y el reintento con `pg_sleep()`
4. `R3.04` El mapeo no arrancó
5. `R3.05` Mapeo con 0 filas: causa legítima vs. fallo
6. `R3.06` Mapeo bloqueado por otro proceso
7. `R3.07` `tablas_mapeio_t.activo_inactivo`: desactivado a propósito
8. `R3.08` Dependencia insatisfecha: falta el insumo
9. `R3.09` `fim_carga_mapeo_megara_ind` no cerró
10. `R3.10` El mapeo corrió pero el dato no llegó a destino
11. `R3.11` Relanzar un mapeo suelto con seguridad
12. `R3.12` Consultas de diagnóstico por `id_mapeo`

### R4. Bloques de archivos incompletos — 11
1. `R4.01` Qué es un "set completo" y quién lo define
2. `R4.02` `controlflag_interfaces`: las interfaces esperadas por flag
3. `R4.03` `Validacion_Cantidades_Recibidas`
4. `R4.04` `s3_interface_control_t` y `_XML_t`: el conteo de cierre
5. `R4.05` Llegó el flag pero faltan XMLs
6. `R4.06` Llegaron XMLs pero no el flag
7. `R4.07` Archivo en `DIR_UNMATCHED`: por qué y qué hacer
8. `R4.08` Archivo fuera de ventana
9. `R4.09` Set incompleto: esperar, forzar o escalar
10. `R4.10` Consultas: qué falta ahora mismo
11. `R4.11` Efecto dominó: qué bloques quedan parados

### R5. Alertas de Rundeck — 10
1. `R5.01` Cómo notifica Rundeck: `onfailure`, `onstart`, `onsuccess`, `onavgduration`
2. `R5.02` **Los 22 jobs sin notificación: los fallos que nadie ve**
3. `R5.03` Las dos listas de distribución y quién recibe qué
4. `R5.04` Alertas con log adjunto vs. sin log
5. `R5.05` Leer el log de un job fallido
6. `R5.06` Alerta por duración anómala
7. `R5.07` Llega alerta pero el job está verde — y al revés
8. `R5.08` `_00001_Análise_de_erros` — ⚠ anulado con `WHERE 1=0`
9. `R5.09` Catálogo de alertas conocidas y su primera acción
10. `R5.10` Cadena de escalado a partir de una alerta

**Subtotal runbooks: 54 fichas.**

## 4. Capa de referencia por etapa (~132 fichas)

### A. Orientación — 7
1. `A01` Qué es Aldrin y qué hace, en una página
2. `A02` El flujo de punta a punta: los 6 pasos
3. `A03` Glosario: STG, TRF, EXP, flag, bloque, mapeo, `_DES`, `_ERR`, `_TMP`, interfaz
4. `A04` Mapa de rutas y directorios de producción
5. `A05` Mapa de esquemas de base de datos y qué vive en cada uno
6. `A06` Árbol de decisión: "mi incidencia, ¿de qué etapa es?"
7. `A07` Ventanas de ejecución: qué corre y a qué hora

### B. Etapa 1 — Recepción de XML y flags — 11
1. `B01` Qué es un archivo flag y qué dispara
2. `B02` Los 9 flags del catálogo y qué lote representa cada uno
3. `B03` Ciclo de vida de un archivo: landing → OK → PROCESSED / UNMATCHED
4. `B04` Job `Validacion_constante_presencia_archivos_flag`
5. `B05` Job `Manejo_Flag`
6. `B06` Job `LlamadaTablaControlArquivosFlag` y `JobsArchivosFlag`
7. `B07` Job `LLamada_Rundeck_Flags_Obligatorios` y su script
8. `B08` Tablas `controlflag_arquivos` y `controlflag_interfaces`
9. `B09` **Runbook:** no llegó el flag a la hora esperada
10. `B10` **Runbook:** llegó el flag pero faltan XMLs de la interfaz
11. `B11` **Runbook:** archivos parados en `DIR_UNMATCHED`

### C. Etapa 2 — Conversión Java — 12
1. `C01` Qué hace `xmlConversor.jar`: entrada, salida, separador y encoding
2. `C02` `load_java_script.sh` paso a paso
3. `C03` `lookup_java.txt`: formato de línea y cómo leerlo
4. `C04` Validación XSD con `xmllint`: qué valida y qué no
5. `C05` Cifrado GPG del XML original y dónde queda
6. `C06` Los bloques de conversión: `Javas_Bloque_Estaticos` vs `Javas_Bloque_Dinamico`
7. `C07` Anatomía de un micro-job de conversión (ejemplo `0020 CONV JAVA TAX PAY CAT`)
8. `C08` Listado completo de las 132 conversiones por bloque
9. `C09` **Runbook:** el XML no valida contra su XSD
10. `C10` **Runbook:** la conversión produce 0 filas o archivo vacío
11. `C11` **Runbook:** caracteres corruptos o separador `!` dentro de un campo
12. `C12` **Runbook:** el job de conversión no arrancó

### D. Etapa 3 — Carga a Staging — 13
1. `D01` Mecánica de carga: `\COPY`, tabla `_TMP` y paso a `_T`
2. `D02` `lookup_stg.txt`: formato y cómo saber qué carga cada línea
3. `D03` `load_stgtrf_script.sh`: la función `stg()` y el truco de parámetros impares
4. `D04` `PAR_LOAD_PLAN_T`: el plan de carga
5. `D05` `PAR_MAESTRO_TABLAS_T` y `PAR_MAESTRO_COLUMNAS_T`
6. `D06` `read_header_fn()`: cómo se deducen las columnas del archivo
7. `D07` `run_load_plan_pc()`: el volcado
8. `D08` `load_files_pc()` y `load_mask_columns_pc()`
9. `D09` Los 14 bloques `OptimizacioBloque*TRFySTG` y su orden
10. `D10` **Runbook:** la carga falla por número de columnas
11. `D11` **Runbook:** la tabla `_T` quedó vacía
12. `D12` **Runbook:** la carga se quedó colgada o bloqueada
13. `D13` **Runbook:** cargó dos veces / datos duplicados

### E. Etapa 3.1 — Validaciones, descartes y errores — 11
1. `E01` El firewall de calidad: qué se valida antes de entrar a `_T`
2. `E02` `validate_gen_pc()`: el orquestador de validaciones
3. `E03` `validate_rows_null_fn()` — obligatoriedad
4. `E04` `validate_rows_format_ent_fn()` y `PAR_MAESTRO_MASK_T` — formato
5. `E05` `validate_rows_foreign_fn()` y `PAR_MAESTRO_VALID_T` — integridad
6. `E06` `validate_rows_key_fn()` y `validate_control_fn()` — llaves y control
7. `E07` `validate_variation_fn()` — variación anómala de volumen
8. `E08` Tablas `_DES` y `_ERR`: qué cae en cada una y cómo leerlas
9. `E09` `fn_load_data_err()` y `fn_merge_into_desc()`
10. `E10` `fn_reproceso_descart()`: reintento de descartes
11. `E11` **Runbook:** hay filas en `_DES`/`_ERR`, cómo saber qué validación falló y qué hacer

### F. Etapa 4 — Transformación TRF — 14
1. `F01` Qué hace la capa TRF y hacia dónde escribe
2. `F02` `lookup_trf.txt`: formato y parámetro `(0)`
3. `F03` La función `trf()` y el truco de parámetros pares
4. `F04` `LOG_TRACE()` y la tabla `aud_log_trace_t`: la traza que usa BAU
5. `F05` Familias de procedimientos: `cs_`, `ch_`, `sss_`, `fa_`, `load_`
6. `F06` Dependencias entre bloques: por qué el orden importa
7. `F07` `bloqueio_insercao_dados()`: el bloqueo de inserción
8. `F08` `actualizacao_carga_megara_primera/segunda()`
9. `F09` Los `load_*` no migrados (BULLE / SAC / FIDC): qué son y quién los usa
10. `F10` **Runbook:** un procedimiento TRF falló, cómo localizarlo en `aud_log_trace_t`
11. `F11` **Runbook:** TRF corrió pero la tabla destino no cambió
12. `F12` **Runbook:** deadlock o bloqueo entre procedimientos
13. `F13` **Runbook:** un bloque tardó muchísimo más de lo normal
14. `F14` **Runbook:** faltan datos en una tabla core, ¿STG o TRF?

### G. Etapa 5 — Mapeos — 14
1. `G01` Qué es un mapeo y a dónde escribe (`exp_s3`)
2. `G02` `tablas_mapeio_t`: el interruptor real `activo_inactivo`
3. `G03` Job `Control_Inicio_Carga_Mapeo`
4. `G04` Jobs `Mapeos` y `MapeosFlag`: el disparo paralelo
5. `G05` Anatomía de un job de mapeo (ejemplo `35 mapeo_sac_pl_cl_patrrf_t`)
6. `G06` Listado completo de mapeos activos y su tabla destino
7. `G07` Deadlock `40P01`: la captura y el reintento con `pg_sleep()`
8. `G08` `fim_carga_mapeo_megara_ind()`
9. `G09` `Job_control_errores_mapeo`
10. `G10` `Procedimiento_control_finalizacion_mapeos` y su variante Flag
11. `G11` **Runbook:** un mapeo no arrancó
12. `G12` **Runbook:** un mapeo terminó con 0 filas
13. `G13` **Runbook:** mapeos en deadlock o colisión masiva
14. `G14` **Runbook:** el mapeo terminó pero el dato no aparece en destino

### H. Etapa 6 — Cierre, limpieza y Qlik — 12
1. `H01` Qué significa "cerrar el lote del día"
2. `H02` `STG_StartOver` y `cleanup_meg_t()`: el borrado dinámico
3. `H03` `Validacion_Cantidades_Recibidas`
4. `H04` `_00001_Análise_de_erros` — **⚠ anulado con `WHERE 1=0` en producción**
5. `H05` `actualizar_tablas_y_control()` y su variante Flag
6. `H06` `s3_interface_control_t` y `s3_interface_control_XML_t`: el conteo de interfaces esperadas
7. `H07` `lookup_qlik.txt`: qué se expone a Qlik
8. `H08` La recarga de Qlik: POST a la API con certificados `.pem` *(hueco H-2)*
9. `H09` **Runbook:** Qlik muestra datos de ayer
10. `H10` **Runbook:** el cierre no se completó, el lote quedó abierto
11. `H11` **Runbook:** el conteo de interfaces no cuadra
12. `H12` **Runbook:** la recarga de Qlik falló o el certificado caducó

### I. Referencia de datos — 16
1. `I01` Convención de nombres: `_T`, `_TMP`, `_DES`, `_ERR`, `MEG_`
2. `I02` Esquema `stg_s3`: inventario y propósito
3. `I03` Esquema `trf_s3`: inventario y propósito
4. `I04` Esquema `exp_s3`: inventario y propósito
5. `I05` Esquemas `sss`, `cs`, `fa`: inventario y propósito
6. `I06` Índice de tablas de control y auditoría
7. `I07` Las tablas `PAR_*`: el corazón metadata-driven
8. `I08` Catálogo de interfaces `MEGA*` y su archivo de origen
9. `I09` Los códigos `cod_dm*`: qué son y por qué una fila se descarta si no resuelven
10. `I10` Secuencias y su papel en el control de flags
11. `I11` **La ficha estrella:** rastrear un archivo desde el landing hasta Qlik
12. `I12` Rastrear un dato hacia atrás: "este número está mal en Qlik, ¿de dónde salió?"
13. `I13` Consultas SQL de diagnóstico frecuentes
14. `I14` Cómo leer `aud_log_trace_t`
15. `I15` Volumetría típica por interfaz *(requiere consulta a prod)*
16. `I16` Calendario: qué corre diario, semanal, mensual e intradía

### J. Transversal y operación — 10
1. `J01` Rundeck: cómo está organizado el árbol de jobs
2. `J02` `Main_Job_Megara` y `CargaInformacion`: los orquestadores raíz
3. `J03` Cómo relanzar de forma segura: qué es idempotente y qué no
4. `J04` **Qué NO tocar nunca** y por qué
5. `J05` Dónde vive cada credencial (sin valores) y a quién pedirla
6. `J06` Servidores, rutas y accesos que necesita un BAU
7. `J07` Escalado: qué se resuelve en BAU y qué se escala *(a completar contigo)*
8. `J08` Los 5 fallos que más ruido hacen y su primera acción
9. `J09` Checklist de verificación diaria del lote
10. `J10` Trampas conocidas: cosas que parecen un fallo y no lo son

### K. BULLE / SAC / FIDC — 6
1. `K01` Qué son y cómo encajan en el ecosistema
2. `K02` Los `load_*` que los alimentan
3. `K03` Tablas destino y consumidores
4. `K04` Diferencias operativas con el flujo principal
5. `K05` **Runbook:** incidencias específicas
6. `K06` Estado: qué se migra y qué no *(contexto para BAU, no diseño)*

### Ajustes a la capa de referencia

- **H (Qlik) pasa de 12 a 18.** El mecanismo real no es un único POST: son ~265 tareas con UUID en `lookup_qlik.txt`, en dos familias (globales `LOAD_QVD_*`/`LOAD_UPDATE_*` y ~225 incrementales por tabla, cada una disparada por su propio `Qlik_TABLA.flag`). Se añaden: formato del lookup, las dos familias, el disparo por flag, catálogo de tareas con UUID, certificados, y "una tabla no recargó pero las demás sí".
- **`I17` — índice "tabla destino → qué la llena".** Generado desde `grafo_transformacion.csv` + `catalogo_tablas.csv`. Es la primera pregunta ante un dato que falta.
- **`I18` — calendario y días hábiles.** Feriados (`sac_stat_bas_cad_fer_t`), qué corre diario/semanal/mensual/intradía y por qué un lote puede legítimamente no ejecutarse.
- El **reproceso** no lleva familia propia: vive dentro de los runbooks que lo necesitan (`R1.09`, `R2.07`, `R3.11`) más `J03`.

**Total: 192 fichas** — 138 de referencia, 54 runbooks. Bajo el tope de 300.

## 5. Entrega por fases

Los runbooks mandan, pero cada uno se apoya en fichas de referencia. El orden alterna para que
cada fase deje algo utilizable, no medio sistema documentado.

| Fase | Contenido | Por qué |
|---|---|---|
| 1 | A (7) + R1 descartes (12) = **19 fichas** | Orientación mínima + el dolor nº1 completo. Lo subes a NotebookLM y le preguntas cosas reales antes de que produzca en serie. |
| 2 | E validaciones (11) + R2 duplicados (9) + D carga STG (13) | Cierra descartes y duplicados con su referencia debajo. |
| 3 | B flags (11) + R4 sets incompletos (11) + C conversión Java (12) | La entrada del flujo de punta a punta. |
| 4 | G mapeos (14) + R3 errores de mapeo (12) + F transformación (14) | El corazón del proceso. |
| 5 | J operación (10) + R5 alertas (10) + H Qlik (18) | Salida, monitorización y escalado. |
| 6 | I referencia de datos (18) + K BULLE/SAC/FIDC (6) | Material de consulta y periféricos. |

## 6. Hallazgos que salieron del inventario

No son parte del encargo, pero afectan a lo que BAU debe saber. Se documentan en sus fichas.

### F-1 — El paso "Recarga Qlik" no puede estar enviando la petición

En las dos copias del paso, la llamada es:

```bash
curl -s --key .../client_key.pem --cert .../client.pem --insecure \
     --X POST \
     ...
```

`--X` no es una opción válida de curl (la larga es `--request`). Verificado localmente:
curl responde `option --X: is unknown` y termina con **código 2 sin enviar nada**.
Como además el paso hace `echo "Task lanzada"; exit 0` —y en la copia de `0999` la llamada va
en segundo plano con `&`— **el job siempre reporta verde**, se envíe la petición o no.

Comprobación que sólo puedes hacer tú: en la consola de Qlik, historial de ejecuciones de la tarea
`RecargadesdeRundeck` (`a75bd6d3-d26b-41ec-8c88-1c29b1ff9202`). Si sus ejecuciones coinciden con
un horario propio de Qlik y no con el fin de los mapeos, la recarga lleva tiempo dependiendo de
otra cosa. Va a la ficha `H12` y al `J10` (trampas conocidas).

### F-2 — Los errores del conversor Java se registran ilegibles

`main.java:136` y `:182` hacen `System.out.println(e.getStackTrace().toString())` sobre el **array**,
no sobre su contenido. En el log aparece `[Ljava.lang.StackTraceElement;@1b6d3586` en vez de la causa.
Cuando una conversión falla, el log no dice por qué. Ficha `C09`/`C12`: hay que diagnosticar por otra vía
(reproducir el `xmllint` a mano contra el XSD).

### F-3 — Comportamientos del conversor que parecen fallo y no lo son

- `printMissingFiles()` crea **CSV vacíos a propósito** para nodos declarados en el XSD y ausentes del XML. Un archivo de 0 bytes es salida normal.
- Ante cualquier error de parseo, `deleteFiles()` **borra toda la salida ya generada**. Nunca queda salida parcial: o están todos los CSV o no está ninguno.
- `getProperties()` lee `config.properties` con **ruta relativa** al directorio de trabajo. Lanzado desde el directorio equivocado, el conversor muere por fichero no encontrado antes de tocar el XML.
- Los valores no se entrecomillan: `\r` y `\n` se sustituyen por espacio, pero **un `!` dentro de un dato parte la línea en columnas de más**. Ésta es la ficha `C11`.

### F-4 — `XLSXtoCSV` se salta la última fila

`while (j < sheet.getLastRowNum())` debería ser `<=`. Sólo afecta a las entradas `.xls`/`.xlsx`,
no al flujo XML principal. Se anota en la ficha del conversor.

## 7. Estado de ejecución

**111 fichas escritas** (~11.300 líneas). Índice y estado por familia en `00_INDICE.md`.

Familias completas: A, B, C, D, E, R1, R2, R4.
Familias parciales: R3 (8/12), R5 (6/10), G (5/12), H (5/18), F (2/12), J (3/10), I (1/18), K (1/6).

Las cinco familias de runbook —los dolores declarados— están cubiertas: R1, R2 y R4 al 100 %, R3 y
R5 con sus fichas de diagnóstico y catálogo. Lo que falta es sobre todo **referencia**, no runbook.

## 8. Hallazgos adicionales encontrados al escribir

Sobre los cuatro de la sección 6, aparecieron estos al leer el código:

### F-5 — En staging nada detecta ni impide un duplicado

Tres cosas a la vez: `stg_s3` tiene **3 claves primarias en ~1.322 tablas** y ninguna en tablas de
datos; `validate_rows_key_fn` **no se invoca desde ningún sitio**; y su construcción de clave está
mal (sobrescribe en vez de acumular, y genera SQL inválido). Ficha `R2_01`.

### F-6 — El apartado de descartes puede destruir filas

`FN_MERGE_INTO_DESC` usa `ON CONFLICT (claves)`, que exige un índice único. Hay ~322 tablas `_DES`
en `stg_s3` y sólo ~68 índices únicos. Cuando falla, la excepción se captura y **no se propaga**; el
llamador `FN_LOAD_DATA_ERR` no comprueba el resultado y **borra la fila de `_TMP` y de la tabla base
igualmente**. La fila desaparece sin llegar a `_DES`. Consulta de verificación en la ficha `R2_02`.

### F-7 — `VALID_ERR_DES` cambia radicalmente el comportamiento

Columna de `PAR_LOAD_PLAN_T`, por defecto `1`. Con otro valor, un fallo de clave foránea ejecuta
`TRUNCATE` sobre la tabla completa en vez de apartar filas. Ficha `R1_01`.

### F-8 — La validación de variación de volumen no protege nada

No se invoca desde el flujo, y sus consultas comparan `MAX(cod_load_trace)` con `MAX-1` **sin
filtrar por tabla**: compara las dos últimas cargas del sistema, sean de la interfaz que sean.
Ficha `R1_07`.

### F-9 — `fn_reproceso_descart` enmascara sus errores

Su manejador de excepciones escribe en `stg_s3.load_trace_t`, tabla que **no existe en el DDL**. El
manejador falla y sustituye el error original. Además, el `TRUNCATE` de `_DES` es incondicional.
Ficha `R1_09`.

### F-10 — `megara_reprocess` no puede ejecutarse

Construye su SQL con **comillas dobles** (identificadores en PostgreSQL, no cadenas), le falta un
espacio antes del `WHERE` y concatena fechas sin comillas. Su bloque de excepción se traga el error
sin dejar traza.

### F-11 — 22 de 46 jobs no tienen ninguna notificación

Entre ellos el vigilante de presencia que sondea cada 3 segundos, `STG StartOver`,
`LlamadaTablaControlArquivosFlag` y los bloques de catálogo 1, 2 y 2.5. Fichas `R5_02` y `J09`.

### F-12 — `Validacion Cantidades Recibidas` compara contra un lote fijo

`id_camda = '29817'` está codificado en el job. Si el catálogo de interfaces cambia, la comparación
envejece sin avisar. Además, dos de sus seis comprobaciones se solapan, así que el número no es un
recuento de interfaces afectadas. Ficha `R4_03`.

## 9. Decisiones pendientes

1. `J07` (escalado) y `I15` (volumetría) requieren datos que sólo tú tienes.
2. Confirmar F-1 contra el historial de la tarea de Qlik `RecargadesdeRundeck`.
3. **H-7 nuevo:** el script que consume `lookup_qlik.txt` no está en el repositorio. Vive en
   `/opt/qliktasks/`. Sin él no se puede documentar cómo se decide qué tarea de Qlik se lanza.
4. **H-8 nuevo:** `load_java2_optiflag_script.sh` se invoca desde el script de flags pero no está en
   el repositorio.
5. **H-9 nuevo:** el volcado de `exp_s3` sólo contiene `tablas_mapeio_t`. Faltan
   `incio_carga_mapeo_megara`, `fim_carga_mapeo_megara_ind` y `actualizar_tablas_y_control`.

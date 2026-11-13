# Hallazgos del análisis del sistema AS-IS

Resultado del análisis realizado para construir la base de conocimiento de soporte BAU. **No era el
objetivo del trabajo**: son observaciones que aparecieron al leer el código, los scripts, los jobs
y el DDL para poder documentarlos con precisión.

Cada hallazgo indica si está **verificado contra producción** o si sigue **pendiente de comprobar**.

---

## Resumen ejecutivo

| Severidad | Nº | Naturaleza |
|---|---|---|
| **Crítico** | 2 | Pérdida silenciosa de datos |
| **Alto** | 7 | Controles que no controlan: fallos reales sin detección |
| **Medio** | 8 | Ruido operativo y deuda de mantenimiento |
| **Informativo** | 5 | Seguridad y calidad de código |

El patrón de fondo, repetido en varias piezas independientes: **el sistema tiene mecanismos que
existen, parecen operativos y no hacen nada**. La consecuencia práctica es que **el silencio no es
evidencia de que todo vaya bien**, y por eso la base de conocimiento incluye un checklist de
verificación diaria.

---

## CRÍTICO 1 — 261 tablas pueden perder filas al descartar, sin dejar traza

**Verificado en producción.**

Cuando una fila se descarta por integridad referencial, `FN_MERGE_INTO_DESC` la inserta en la tabla
`_DES` con `ON CONFLICT (<clave>) DO UPDATE`. Esa instrucción **exige un índice único** sobre esas
columnas.

```sql
SELECT count(*) FROM information_schema.tables t
WHERE  t.table_schema = 'stg_s3' AND t.table_name LIKE '%\_des'
  AND  NOT EXISTS (SELECT 1 FROM pg_index i
                   WHERE i.indrelid = ('stg_s3.'||t.table_name)::regclass
                     AND i.indisunique);
```

**Resultado: 261 tablas sin ese índice.**

La cadena del fallo:

1. `FN_MERGE_INTO_DESC` falla con *«there is no unique or exclusion constraint matching the ON
   CONFLICT specification»*
2. Su bloque de excepción **captura el error y devuelve el texto en lugar de propagarlo**
3. `FN_LOAD_DATA_ERR` **no comprueba ese valor de retorno** y ejecuta los `DELETE` igualmente

```sql
V_EXECUTE_MERG := stg_s3.FN_MERGE_INTO_DESC(...);   -- puede haber fallado
EXECUTE 'DELETE FROM stg_s3.<TABLA>_TMP WHERE ...';
EXECUTE 'DELETE FROM stg_s3.<TABLA>     WHERE ...';
```

**Resultado: la fila desaparece de `_TMP`, desaparece de la tabla base y no llega a `_DES`.** No
está en ningún sitio.

**Cómo cuantificarlo por carga:**

```sql
SELECT (SELECT count(*) FROM stg_s3.aud_load_valid_trace_t
        WHERE cod_load_trace = :trace AND des_validate = 'FOREIGN_KEY') AS registrados,
       (SELECT count(*) FROM stg_s3.<TABLA>_DES WHERE cod_load_trace = :trace) AS en_des;
```

`registrados > en_des` = faltan filas.

**Corrección posible:** crear los índices únicos que faltan, o comprobar el retorno de
`FN_MERGE_INTO_DESC` antes de borrar. La segunda es más segura.

---

## CRÍTICO 2 — Un mapeo con `retry_deadlock` NULL no se ejecuta y se marca como completado

**Pendiente de comprobar cuántos mapeos están en esa situación.**

En `exp_s3.fim_carga_mapeo_megara_ind`:

```sql
v_retries INT := 1;
FETCH cursor INTO ..., v_retries, v_wait_deadlock;   -- v_retries := retry_deadlock

WHILE v_attempt < v_retries LOOP
    EXECUTE 'SELECT trf_s3.' || v_nome_fn_mapeio || '();';
    ...
END LOOP;

IF v_attempt >= v_retries THEN
    -- registra "Se agotaron los intentos"
ELSE
    UPDATE exp_s3.control_mapeio_t SET control_carga = control_carga - 1, data_fim_upload = NOW() ...
END IF;
```

Si `retry_deadlock` es NULL se encadenan dos efectos:

1. `WHILE 0 < NULL` evalúa a NULL → **el bucle no entra nunca y la función de mapeo no se invoca**
2. `IF 0 >= NULL` también evalúa a NULL → se va por el `ELSE` → **decrementa el contador y sella
   `data_fim_upload` como si hubiera terminado bien**

**La tabla no se actualiza, no se registra error, y el control queda marcado como completado.**
Silencioso en las tres vías.

```sql
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio
FROM   exp_s3.tablas_mapeio_t
WHERE  activo_inactivo AND is_fromtis = 'N' AND retry_deadlock IS NULL
ORDER  BY id_mapeo;
```

**Todo lo que devuelva esa consulta son mapeos que no se están ejecutando.**

**Corrección:** asignar un valor a `retry_deadlock`, o usar `coalesce(retry_deadlock, 1)` en el
despacho.

---

## ALTO 3 — Nada detecta ni impide un duplicado en staging

**Verificado en producción.**

Tres condiciones simultáneas:

- **`stg_s3` tiene 3 claves primarias en ~1.322 tablas**, y ninguna está en una tabla de datos
  (`controlflag_arquivos`, `controlflag_interfaces`, `nprinting_ondemand`)
- **`validate_rows_key_fn` no se invoca desde ningún sitio**: `validate_gen_pc` ejecuta nulos,
  formato y claves foráneas, y nada más
- **Y si se invocara, no funcionaría**: construye la clave con `V_KEY_GROUP := tabla || '.' ||
  columna` **sobrescribiendo en cada vuelta** en vez de acumular, de modo que una clave compuesta
  quedaría reducida a su última columna; además genera SQL inválido y no tiene manejador de
  excepciones

**Verificación:**

```sql
SELECT des_validate, count(*) FROM stg_s3.aud_load_valid_trace_t GROUP BY 1 ORDER BY 2 DESC;
```

| `des_validate` | Filas |
|---|---|
| `FOREING_KEY_OLD` | 3.174.004 |
| `FOREIGN_KEY` | 1.095.443 |
| `FORMATO LONG NUM` | 784.174 |
| `NULOS` | 361.117 |
| `FORMATO NUM` | 168.143 |
| `FORMATO VAR` | 92.180 |

**`DUPLICADOS` no aparece.** En 5,7 millones de registros acumulados, ni uno procede de la
detección de duplicados.

**Consecuencia:** un fichero con filas repetidas se carga entero sin aviso. Los duplicados afloran
capas más abajo —en `trf_s3`, con sus 185 claves primarias, o en los mapeos, que deduplican por
clave natural— lejos de su origen y sin trazabilidad al fichero que los trajo.

---

## ALTO 4 — El control de análisis de errores está anulado

**Verificado en el código del job.**

El job `_00001 Análise de erros` forma parte del flujo de cierre, está programado, se ejecuta y
termina correctamente. Su consulta lleva `WHERE 1=0`: **no puede devolver resultados nunca**.

Es el peor tipo de fallo de monitorización: uno que parece funcionar. Aparece en verde, ocupa el
sitio de un control real y tiene notificación configurada.

**Recomendación:** restaurarlo o retirarlo. Dejarlo como está genera una falsa sensación de
cobertura.

---

## ALTO 5 — 22 de 46 jobs no notifican si fallan

**Verificado sobre los exports.**

De los 46 jobs exportados, 24 tienen notificación (22 `onfailure`, 2 `onstart`, 1 `onsuccess`,
1 `onavgduration`). **Los otros 22 fallan en silencio.**

Entre los que no avisan hay piezas críticas:

| Job sin alerta | Impacto si falla |
|---|---|
| `Validacion constante presencia archivos flag` | **El sistema entero se para**: nada se detecta |
| `STG StartOver` | El ciclo siguiente arranca sobre datos viejos |
| `LlamadaTablaControlArquivosFlag` | Las interfaces se registran con el lote equivocado |
| Bloques 1, 2 y 2.5 | **Son los catálogos**: su fallo provoca descartes en cascada |
| Jobs `Flag_*` individuales | No se detecta la llegada de un flag |
| `Procedimiento control finalizacion mapeos` | El lote no cierra |

**Recomendación:** añadir `onfailure` a esos jobs. Y `attachLog='true'`, que sólo tienen cuatro
configuraciones y reduce a la mitad el tiempo de triaje.

---

## ALTO 6 — Un fallo de recarga de Qlik no genera ninguna alerta

**Confirmado con el equipo.**

Rundeck lanza la recarga y se desentiende:

```bash
curl ... -X POST "$url"
echo "Task $nom_task lanzada"
exit 0
```

El `exit 0` es incondicional. Y una vez lanzada la tarea, Qlik ejecuta el script de carga por su
cuenta: **si falla a mitad, ni Rundeck ni Qlik ni la base de datos lo notifican.**

Los tableros se quedan con los datos del QVD anterior —no vacíos, sino desactualizados— y el ciclo
entero aparece en verde.

**Es el único tramo del flujo sin ninguna cobertura, y es el que ve el usuario final.**

---

## ALTO 7 — El manejador de errores del reproceso de descartes enmascara la causa

**Verificado en producción.**

`stg_s3.fn_reproceso_descart` registra sus excepciones así:

```sql
INSERT INTO stg_s3.load_trace_t (...) VALUES (...);
```

```sql
SELECT to_regclass('stg_s3.load_trace_t');   -- resultado: NULL
```

**Esa tabla no existe.** El manejador falla al ejecutarse y el error que se ve es *«relation does
not exist»*, que sustituye al error original. **Cuando el reproceso falla, no se sabe por qué.**

Añadido: el `TRUNCATE` de `_DES` al final es **incondicional**. Las filas que no se reinsertaron
—porque su clave ya existía en `_TMP`— también se borran, sin copia.

---

## ALTO 8 — La rama de error de la carga nunca se ha ejecutado

**Verificado en producción.**

```sql
SELECT count(*) FROM stg_s3.aud_load_trace_t WHERE step_load = 'ERROR - STOP EJECUCION';
```

**Resultado: 0 en todo el histórico.**

La causa: `RUN_LOAD_PLAN_PC` pasa el código de salida como parámetro `INOUT` mediante
`EXECUTE ... USING`, y en PL/pgSQL **eso no devuelve el valor a la variable del llamador**.
`V_OUT_CODE` conserva su valor inicial, `0`, así que la comparación `IF V_OUT_CODE = 0` siempre es
cierta.

**Consecuencias:** la validación se ejecuta siempre, incluso si la carga a `_TMP` falló; y la
ausencia de esa traza **no puede usarse como prueba de que las cargas fueron bien**.

---

## ALTO 9 — La validación de variación de volumen no protege nada

**Verificado en el código.**

`stg_s3.validate_variation_fn` no se invoca desde `validate_gen_pc` ni desde ningún otro
procedimiento. Y sus consultas comparan así:

```sql
WHERE cod_load_trace IN (SELECT MAX(cod_load_trace) - 1 FROM stg_s3.aud_load_trace_t)
```

**Sin filtrar por tabla ni por plan de carga.** Compara las dos últimas cargas del sistema entero,
sean de la interfaz que sean.

**Un fichero truncado o inflado pasa hasta Qlik sin que salte nada.**

Y el análisis de volumetría añade un matiz importante para cualquier corrección: en 76 planes con
actividad, **casi todos tienen mínimo de 1 fila en 30 días** y 20 tienen máximos que superan 50
veces su media. Un control por porcentaje fijo generaría alarmas constantes.

**Las dos excepciones vigilables** son los planes `511` (517-550 filas) y `512` (26.594-28.876), con
amplitud de ±3-4 % y 145 ejecuciones diarias.

---

## MEDIO 10 — El lote de referencia del control de completitud está codificado

**Verificado en producción.**

`Validacion Cantidades Recibidas` compara el lote actual contra `id_camda = '29817'`, escrito en el
código del job.

```sql
SELECT count(*) AS interfaces, min(nome_flag_geral) AS flag
FROM   stg_s3.controlflag_interfaces WHERE id_camda = 29817;
```

**Resultado: 133 interfaces, flag `MEGAACCOUNTING_EndOfDay`.**

Y la comparación agrupa por `(nome_flag_geral, nome_interface_base)`, de modo que el nombre del flag
entra en la clave. **Un lote `IntraDay` no casa con ninguna fila de una referencia `EndOfDay`**, por
lo que debería marcar como problema todas sus interfaces.

Además, dos de las seis comprobaciones que suma **se solapan**, así que el número resultante no es
un recuento de interfaces afectadas.

**Recomendación:** comparar contra un lote de referencia por tipo de flag, o retirar esa
comprobación del cómputo.

---

## MEDIO 11 — Un fichero de texto apaga el ciclo entero, en verde

**Pendiente de comprobar su valor en producción.**

`LLamada Rundeck Flags Obligatorios` empieza leyendo:

```bash
valor_actual=$(tr -d '[:space:]' < /nfq/data/cfg/ArchivoAyudaRundeckMegara.txt)
if [ "$valor_actual" -eq 1 ]; then ... else echo "…abortando ejecucion"; exit 0; fi
```

Si ese fichero no contiene exactamente `1`, **el sistema deja de pedir ficheros a Megara y el job
sale con `exit 0`**: aparece en verde.

Es un interruptor manual sin ninguna señal de estado. Debería ser la primera comprobación ante
«hace horas que no llega nada y no hay ningún error».

---

## MEDIO 12 — Fechas de corte codificadas en el script de carga de Qlik

**Verificado en el script.**

El script lleva tres cortes distintos según la sección: `>= '2024-12-31'`, `>= '2025-03-01'` y
`>= '2025-08-01'`.

**Una corrección sobre un dato anterior al corte no llega nunca a los tableros**: el `SELECT` no la
recoge, y en el QVD sólo sobrevive lo que ya estuviera.

Las fechas envejecen sin aviso, y el volumen que se recarga desde la base crece sin límite porque el
corte no avanza. Además, dos de las tres secciones **procesan las mismas tablas** con criterios
distintos.

---

## MEDIO 13 — Identificadores con mayúsculas inconsistentes entre tablas de control

**Verificado en producción.**

El mismo identificador se guarda con caja distinta según la tabla:

| Origen | Ejemplo |
|---|---|
| `tablas_mapeio_t.nome_fn_mapeio` | `function_MEG_CART_CAIXA_CPR_T18` |
| `pg_proc.proname` | `function_meg_cart_caixa_cpr_t18` |
| `relaciontablacolumnas.tabla` | minúsculas |
| `par_maestro_tablas_t.des_table` | mayúsculas |

El sistema lo tolera **por accidente**: el despacho construye `SELECT trf_s3.<nombre>()` sin comillas
y PostgreSQL pliega el identificador a minúsculas al ejecutarlo.

Pero **cualquier consulta de diagnóstico que compare identificadores sin `lower()` en ambos lados
produce falsos negativos**. En este análisis generó 27 falsas «referencias rotas» y 4 falsos
«mapeos sin columnas» antes de detectarse.

---

## MEDIO 14 — 63 piezas de código existen y no se ejecutan

**Verificado por análisis de llamadas.**

| Grupo | Nº | Detalle |
|---|---|---|
| Funciones de `exp_s3` sin llamador localizado | 18 de 22 | API de auditoría de Qlik (`inicio`, `fin`, `principio`, `completar`, `borrar`…), `fluxo_caixa_projectado*`, variantes de cierre |
| Funciones `function_meg_*` no declaradas en `tablas_mapeio_t` | 33 de 152 | Sufijos `_temporal`, `_intermedia`, `_cgc`, `_cc`, series `rvcad_lote_2…6` |
| Procedimientos de `stg_s3` huérfanos | 3 | `validate_rows_key_fn`, `validate_variation_fn`, `megara_reprocess` |
| Ficheros de configuración sin consumidor | 2 | `lookup_qlik.txt` (265 tareas), ficheros `.ctrl` de los dominios periféricos |

Las 18 de `exp_s3` **no están confirmadas como muertas**: sus firmas —nombre de app, URL, nombre de
QVD, tiempos, número de registros— sólo tienen sentido llamadas desde una app de Qlik. La app
disponible no las invoca.

`lookup_qlik.txt` ya estaba catalogado como no utilizado en un análisis previo del proyecto.

---

## MEDIO 15 — `megara_reprocess` no puede ejecutarse

**Verificado en el código.**

```sql
v_query := "delete from "||table_name||"where "||column_name_fund||" = '"||fund||"' ...
```

Tres defectos en una línea: **comillas dobles** —que en PostgreSQL delimitan identificadores, no
cadenas—, falta un espacio antes de `WHERE`, y las fechas se concatenan sin comillas. Y su bloque
de excepción captura el error **sin propagarlo ni registrarlo**.

Es decir: falla siempre y en silencio.

---

## MEDIO 16 — Los separadores no están protegidos en los dominios periféricos

**Verificado en el código.**

El flujo XML protege su separador antes de convertir:

```bash
sed -i 's/!/¡/g' "$fileToOpen"
```

**Los dominios periféricos no pasan por el conversor**, así que no reciben esa sustitución:

| Dominio | Separador | Protegido |
|---|---|---|
| Flujo XML (`MEGA*`) | `!` | **Sí** |
| BULLE (4 interfaces) | `;` | **No** |
| SAC (226 interfaces) | `!` | **No** |

Un separador dentro de un dato rompe la línea y desplaza las columnas. Es la causa número uno de
errores de columnas en esos dominios.

Nota sobre la protección existente: `sed -i` **modifica el XML original en disco**, y el fichero que
se archiva cifrado es ya la versión alterada. El original tal como lo mandó el origen no se conserva
en ningún sitio.

---

## MEDIO 17 — El export de Rundeck no refleja producción

**Confirmado con el equipo.**

El paso «Recarga Qlik» del export contiene `--X POST`, que no es una opción válida de curl: la
herramienta responde *«option --X: is unknown»* y **termina con código 2 sin enviar nada**.

Sin embargo, la tarea `RecargadesdeRundeck` se ejecuta de forma continua en producción. **Conclusión:
el script de producción tiene la opción corregida y el export está desactualizado.**

No es un defecto activo, pero sí una observación de proceso: **los exports de Rundeck no son fuente
fiable del estado actual**. Cualquier análisis basado sólo en ellos puede estar desfasado.

Un caso similar pendiente de comprobar: `LLamada Rundeck Flags Obligatorios` inspecciona
`/media/premegara/Devices/MegaCommon/innotech/`, mientras el resto del sistema usa
`/prdmegara/PRD/Devices/MegaCommon/innotech/`. Si esa ruta no es válida, la comprobación de
completitud del lote es inerte.

---

## INFORMATIVO — Seguridad

| Observación | Detalle |
|---|---|
| **Credenciales en claro en el código** | `LLamada Rundeck Flags Obligatorios.sh` lleva `CREDENTIALS="userrdkmeg@ALL:…"` escrito en el script, no en un fichero de credenciales |
| **TLS sin verificar** | La llamada a la API de Qlik usa `--insecure`: la autenticación de cliente funciona, pero no se valida la identidad del servidor |
| **Dos ficheros de credenciales de BD** | `db_config_gral.env` y `credentials.properties`, con formatos distintos. Un cambio de contraseña exige actualizar los dos |

## INFORMATIVO — Calidad de código

| Observación | Impacto |
|---|---|
| **El conversor Java registra sus errores ilegibles** | `System.out.println(e.getStackTrace().toString())` imprime la dirección del array, no la causa. Cuando una conversión falla, el log no dice por qué. Corrección de una línea |
| **`21000` mal etiquetado** | El despacho de mapeos lo comenta como «Duplicate error». Es `cardinality_violation` —una subconsulta que devuelve más filas de las esperadas—; un duplicado sería `23505`. Lleva el diagnóstico en dirección equivocada |
| **Mensaje de traza falso** | `validate_rows_null_fn` escribe siempre `'Error de Validacion de Nulos. Tabla Truncada'` aunque no trunque nada. Genera incidencias de pérdida de datos inexistentes |
| **`XLSXtoCSV` se salta la última fila** | `while (j < sheet.getLastRowNum())` debería ser `<=`. Sólo afecta a entradas `.xls`/`.xlsx` |

---

## Lo que NO resultó ser un problema

Por completitud, dos riesgos que se descartaron al verificarlos:

**El flujo estricto no está en uso.** El código permite que un fallo de clave foránea ejecute
`TRUNCATE` sobre la tabla completa cuando `valid_err_des ≠ 1`. La consulta de verificación devuelve
**cero filas**: todas las cargas están en modo tolerante. El riesgo existe en el código, no en la
operación.

**Las columnas expuestas a Qlik están completas.** Las 23 tablas que el script de Qlik recorre
tienen todas sus columnas declaradas en `relaciontablacolumnas`. Los 4 mapeos activos sin columnas
declaradas tampoco están en las listas del script: la ausencia es coherente.

---

## Priorización sugerida

| Orden | Hallazgo | Esfuerzo | Riesgo que elimina |
|---|---|---|---|
| 1 | Crítico 2 — `retry_deadlock` NULL | **Muy bajo** (`coalesce`) | Mapeos que no corren y se dan por completados |
| 2 | Alto 5 — jobs sin notificación | Bajo (configuración) | Fallos que nadie ve |
| 3 | Alto 4 — restaurar o retirar el análisis de errores | Bajo | Falsa sensación de cobertura |
| 4 | Crítico 1 — 261 tablas `_DES` | Medio | **Pérdida silenciosa de datos** |
| 5 | Alto 7 — manejador de `fn_reproceso_descart` | Bajo | Errores enmascarados |
| 6 | Medio 10 — lote de referencia codificado | Bajo | Ruido diario en las alertas |
| 7 | Alto 3 — detección de duplicados | Alto | Duplicados que afloran tarde y lejos |
| 8 | Alto 6 — alerta de recarga de Qlik | Medio | El tramo que ve el usuario final |

Los tres primeros son de esfuerzo bajo y retorno inmediato.

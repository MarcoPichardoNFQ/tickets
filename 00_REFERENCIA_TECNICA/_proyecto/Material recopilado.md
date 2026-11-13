# Lo que necesito para completar la base de conocimiento

Checklist de recolección. Actualizado tras la primera entrega.

**Regla de secretos:** en los ficheros con 🔒 necesito **la estructura y los nombres de variable, no
los valores**. Hosts y usuarios sí; contraseñas, claves y tokens sustituidos por `***`.

---

## ✅ Bloque 1 — Ficheros del servidor · COMPLETO

Todo recibido. Lo que aportó cada uno:

| # | Fichero | Qué resolvió |
|---|---|---|
| 1.1 | `3_scripts_motores/Recarga desde Qlik.txt` | **Es un script de carga de una app de Qlik, no un shell.** Qlik se conecta a la base y hace `SELECT ... FROM trf_s3.<tabla>` directamente. Reveló el error de esquema (ver abajo), el patrón incremental de QVD, los filtros `des_status`/`base_id`/`cod_sacbbdd` y las fechas de corte codificadas |
| 1.2 | `load_java2_optiflag_script.sh` | La variante de conversión disparada por flag. Reveló la existencia de `lookup_java_flag.txt` |
| 1.3 | 🔒 `db_config_gral.env` | **`DB_CONN` lleva `-t -A`** → resuelve dos incógnitas de comparación de salida en `R4_03` y `F01`. Host, puerto, base `postgres` y usuario de servicio |
| 1.4 | 🔒 `reload_task.credentials` | `QLIK_HOST` apunta a la API QRS en `:4242/qrs/task/`. Aparecen `TLIMIT=85200` y `T_SLEEP=30`, **que el paso «Recarga Qlik» no usa** |
| 1.5 | — | El script de Qlik vive **dentro de Qlik como app**. Cierra la pregunta: no hay script que buscar en el servidor |
| 1.6 / 1.7 / 1.9 | `listado de rutas y archivos rundeck.txt` | Inventario de rutas y ficheros |
| 1.8 | `config.properties` | `output=/DIR_SSS_LOCAL/`, que es exactamente `raiz` de `env.properties` → **enlaza la salida de la conversión con la entrada de la carga** |

### Añadidos posteriores

| Fichero | Qué resolvió |
|---|---|
| `4_base_de_datos/relaciontablacolumnas_202608081150.csv` | **103 tablas y 1.722 columnas** expuestas a Qlik. Es el catálogo de qué se publica de cada tabla. Las más anchas: `cart_estat_clibas_t` (58), `cart_pos_rf_t` (57), `sac_stat_rv_cadsubscricao_t` (49) |
| `2_config_y_lookups/lookup_java_flag.txt` | 148 interfaces. Resuelve la duda sobre `load_java2_optiflag_script.sh` y destapa una diferencia real entre los dos flujos (ver abajo) |

---

## Lo que estos ficheros cambiaron en la documentación

### Corrección de esquema — afectó a 14 fichas

Los mapeos **no escriben en `exp_s3`**. Escriben en `trf_s3`.

- `exp_s3` = control y código: `tablas_mapeio_t`, `relaciontablacolumnas`, la secuencia de flags y las funciones `mapeo_*`
- `trf_s3` = modelo de negocio (`sss_*`, 291 tablas) **y** tablas de salida (`sac_*` 209, `cart_*` 42)

Corregidas 20 consultas y las referencias en prosa. Antes devolvían «relation does not exist».

### Dos flujos de conversión sobre el mismo catálogo

`lookup_java.txt` y `lookup_java_flag.txt` tienen **las mismas 148 interfaces y los mismos XSD**, y
se diferencian en dos cosas:

| | `lookup_java.txt` | `lookup_java_flag.txt` |
|---|---|---|
| Directorio de origen | `/prdmegara/.../innotech/**Manual/**` | `/prdmegara/.../innotech/` |
| Lo usa | `load_java_script.sh` (manual) | `load_java2_optiflag_script.sh` (por flag) |

Eso confirma que **no hay desajuste** en el script por flag: su `fileToOpen` codificado apunta al
mismo directorio que el lookup. La duda que había quedado abierta se cierra.

**Pero hay una diferencia de contenido, en una sola línea de las 148** — la entrada `154`,
`AdditionalDerivativePrice`:

```
lookup_java.txt       |154|...|AdditionalDerivativePrice.xsd|||AdditionalDerivativePrice_.xml|
lookup_java_flag.txt  |154|...|AdditionalDerivativePrice.xsd|AdditionalDerivativePrice=identifier||AdditionalDerivativePrice_.xml|
```

El flujo por flag declara una **herencia de clave** (`identifier`) que el manual no declara. Como
las claves heredadas se anteponen a cada línea del fichero plano, **la misma interfaz produce un
número de columnas distinto según por qué camino entre**. Si un fichero de esa interfaz llega por
la vía manual, su plano tendrá una columna menos de la que espera la carga.

---

## ✅ Bloque 2 — Funciones de `exp_s3` · RECIBIDO

22 funciones. **Sólo 4 tienen llamador identificado**; las otras 18 quedan documentadas como «sin
llamadas localizadas» en la ficha `G10`, no como activas.

Lo que resolvió: el mecanismo completo de despacho de mapeos (`G08`), el filtro real
`is_fromtis='N' AND activo_inactivo=TRUE`, el contador `control_mapeio_t.control_carga`, y **un
fallo silencioso grave** con `retry_deadlock` NULL (ver `R3_03`).

### Corrección: las funciones de mapeo NO están en `exp_s3`

El despacho hace `EXECUTE 'SELECT trf_s3.' || nome_fn_mapeio || '();'`. **Viven en `trf_s3`.**
Mi petición 2.5 apuntaba al esquema equivocado.

## Bloque 2-bis — Las funciones de mapeo · PENDIENTE · **la prioridad ahora**

| # | Objeto | Desbloquea |
|---|---|---|
| 2b.1 | Las funciones cuyo nombre está en `exp_s3.tablas_mapeio_t.nome_fn_mapeio`, **en el esquema `trf_s3`** | Familias `G` y `R3` completas: qué filtra cada mapeo, si deduplica, si acumula o sobrescribe |

```bash
# Sólo las que la tabla de control declara: evita volcar los 480 procedimientos de trf_s3
psql -h HOST -p 5432 -U USUARIO -d postgres -t -A -o /tmp/trf_s3_mapeos.sql -c "
SELECT pg_get_functiondef(p.oid) || E'\n'
FROM   pg_proc p
JOIN   pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'trf_s3'
  AND  p.proname IN (SELECT DISTINCT nome_fn_mapeio FROM exp_s3.tablas_mapeio_t)
ORDER  BY p.proname;"
```

Y de paso, para detectar referencias rotas:

```sql
-- Mapeos activos cuya función NO existe: fallarían siempre
SELECT t.id_mapeo, t.nome_tabela_aldrin, t.nome_fn_mapeio
FROM   exp_s3.tablas_mapeio_t t
WHERE  t.activo_inactivo
  AND  NOT EXISTS (SELECT 1 FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
                   WHERE n.nspname = 'trf_s3' AND p.proname = t.nome_fn_mapeio);
```

---

## ✅ Bloque 3 — DDL de tablas · RECIBIDO

`ddl varios.csv` — 195 tablas de `exp_s3` y las 4 de `trf_s3` que faltaban.

Lo que resolvió:

- **`s3_control_errores_mapeo`** — 5 columnas: `cod_id`, `des_func`, `cod_sqlstate`, `des_sqlerrm`, `dat_proc_exe`. Ficha `G09` completada
- **`s3_interface_control_t` / `_xml_t`** — **no son un contador de interfaces**, sino un control de publicación **por cliente y fecha de NAV**, con `des_status` como llave de lo que Qlik publica. Ficha `R4_04` reescrita
- **`tmp_controlflag_interfaces`** — tiene `tamanho_interfaz` como **entero** y una columna `data_recebemento2` de tipo **timestamp** que no conocía: es la que hay que usar para ordenar cronológicamente, no la de texto
- **La composición real de `exp_s3`** — 195 tablas en tres grupos distintos, ver `A05`

### Corrección: `exp_s3` no es sólo control

Tiene tres poblaciones que conviene no mezclar:

| Grupo | Qué | Cuántas |
|---|---|---|
| Control del ciclo | `tablas_mapeio_t`, `control_mapeio_t`, `relaciontablacolumnas`, `tabla_control` | 6 |
| **Área temporal de mapeos** | `sac_*_temp`, `cart_*_temp` | 112 |
| **Dominio de salida propio** | `api_*`, `alertas*`, `acumulado_de_gestion`, `fluxo*` — alimentan las tareas `LOAD_QVD_*` de Qlik | ~77 |

Las tablas **finales** de los mapeos siguen estando en `trf_s3`. En `exp_s3` sólo existe su versión
`_temp`. La cadena real es:

```
trf_s3.sss_*  →  exp_s3.<tabla>_temp  →  trf_s3.sac_*/cart_*  →  Qlik
```

---

## ✅ Bloque 4 — Rundeck · CERRADO

Los 45 XML de `5_orquestacion_rundeck/` son el export completo. No falta nada.

Lo que aportó, sobre todo tu explicación del ciclo: **el sistema es un bucle cerrado**. Al consumir
el lote, `LLamada Rundeck Flags Obligatorios` llama a dos endpoints REST de Megara para que genere
el siguiente. Ficha nueva `B09`.

De ahí salieron cuatro cosas que no tenía:

- **`ArchivoAyudaRundeckMegara.txt` es el interruptor general del ciclo.** Si no contiene `1`, el script sale con `exit 0` y el job aparece **en verde** sin haber pedido nada. Primera comprobación ante «hace horas que no llega nada y no hay error»
- **La lista oficial de ~130 prefijos** está codificada en ese script. Es el catálogo maestro de «lo que debe llegar» que yo daba por inexistente → `R4_01` reescrita
- **Los reintentos son de hasta 2,5 h por endpoint** (31 intentos × 5 min), 5 h en total. Un job así no está colgado: está reintentando
- **`DIR_XML="/media/premegara/..."`** frente al `/prdmegara/PRD/...` del resto del sistema. Si esa ruta no es válida en producción, la comprobación de completitud es inerte y las APIs se llaman siempre. **Pendiente de verificar**

Queda una comprobación menor, de la consola de Rundeck: si existen los jobs
`Flag_MEGACUSTODY_EndOfDay`, `Flag_MEGARAFA_IntraDay` y `Flag_MEGARAFA_EndOfMonth`, que están en el
catálogo de 9 flags pero no entre los exports (`B02`, `B05`).

---

## Bloque 5 — Verificaciones en producción · PENDIENTE

```sql
-- 5.1 ¿Existe stg_s3.load_trace_t?  (NULL = no existe → confirma F-9)
SELECT to_regclass('stg_s3.load_trace_t') AS existe;

-- 5.2 ¿Se escribió alguna vez la traza de error de carga?  (0 → rama muerta)
SELECT count(*) AS veces, min(dat_load_date), max(dat_load_date)
FROM   stg_s3.aud_load_trace_t WHERE step_load = 'ERROR - STOP EJECUCION';

-- 5.3 Tablas _DES SIN índice único → filas que se pueden perder al descartar (F-6)
SELECT count(*) AS des_sin_indice_unico
FROM   information_schema.tables t
WHERE  t.table_schema = 'stg_s3' AND t.table_name LIKE '%\_des'
  AND  NOT EXISTS (SELECT 1 FROM pg_index i
                   WHERE i.indrelid = ('stg_s3.'||t.table_name)::regclass
                     AND i.indisunique);

-- 5.4 Interfaces en flujo ESTRICTO: pueden perder la tabla entera (F-7)
SELECT p.cod_load_plan, t.des_table, p.valid_err_des
FROM   stg_s3.par_load_plan_t p
LEFT   JOIN stg_s3.par_maestro_tablas_t t ON t.cod_table = p.cod_table
WHERE  p.valid_err_des IS DISTINCT FROM 1 ORDER BY 2;

-- 5.5 ¿Se ha registrado alguna vez un duplicado?  (0 → confirma F-5)
SELECT des_validate, count(*) FROM stg_s3.aud_load_valid_trace_t
GROUP  BY 1 ORDER BY 2 DESC;

-- 5.6 Catálogo de mapeos
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio,
       activo_inactivo, is_fromtis, retry_deadlock, wait_deadlock_seconds
FROM   exp_s3.tablas_mapeio_t ORDER BY id_mapeo, nome_fn_mapeio;

-- 5.7 El lote de referencia codificado en la validación de cantidades (F-12)
SELECT count(*) AS interfaces, min(nome_flag_geral) AS flag
FROM   stg_s3.controlflag_interfaces WHERE id_camda = 29817;

-- 5.8 NUEVA: ¿coincide lo que Qlik expone con lo que producen los mapeos?
SELECT m.nome_tabela_aldrin,
       (SELECT count(*) FROM exp_s3.relaciontablacolumnas r
        WHERE r.tabla = m.nome_tabela_aldrin) AS columnas_en_qlik
FROM   exp_s3.tablas_mapeio_t m
WHERE  m.activo_inactivo
ORDER  BY 2, 1;
```

**Nota sobre la 5.8:** ejecutada y **sin hallazgos**. Cuatro mapeos activos no tienen columnas
declaradas —`sac_stat_ba_bolsa_t`, `sac_stat_ba_clearing_t`, `sac_stat_ba_contrapartes_t`,
`sac_stat_rv_divid_pag_pos_conta_t`— pero tampoco aparecen en las listas del script de Qlik: no se
publican por esa vía y la ausencia es coherente.

La comprobación que sí detectaría una rotura es la inversa —tablas que Qlik **sí** carga sin
columnas declaradas, lo que dejaría su `LOAD` inválido— y **las 23 que recorre el script las tienen
todas**. Sin incidencia.

⚠ Ambas versiones de la 5.8 necesitan `lower()` en los dos lados: `relaciontablacolumnas.tabla`
está en minúsculas y `nome_tabela_aldrin` mezcla mayúsculas. Sin eso salen 4 falsos positivos.

---

## ✅ Bloque 6 — Qlik · RESUELTO

| # | Respuesta | Consecuencia |
|---|---|---|
| 6.1 | La tarea se ejecuta **continuamente, varias veces al día** | **F-1 cerrado**: el `--X POST` está corregido en producción; el export del repo está obsoleto. `H08` actualizada |
| 6.2 | No hay más apps identificadas | Las 80 tablas de `relaciontablacolumnas` que este script no recorre quedan como observación abierta |
| 6.3 | BAU → escalado interno → cliente | `J07` escrita |
| 6.4 | Rundeck **sólo lanza**; Qlik hace el resto. **Un fallo durante la recarga no se alerta** | Hueco real documentado en `H12` |

**Lección transversal de 6.1:** el export de Rundeck puede no reflejar producción. Ante una
discrepancia entre lo que dice un export y lo que hace el sistema, manda el sistema.

## ✅ Bloque 7 — Escalado y volumetría · RECIBIDO

`J07` e `I15` escritas.

De la volumetría salió un resultado que cambia una recomendación: en 76 planes con actividad,
**casi todos tienen mínimo de 1 fila en 30 días** y 20 tienen máximos que superan 50 veces su
media. **El volumen no sirve como indicador de anomalía** salvo en los planes `511` y `512`, cuya
amplitud es de ±3-4 % y que sí merecen control automático.

---

## Bloque 7 — Lo que sólo está en vuestra cabeza · PENDIENTE

**`J07` — cadena de escalado**

- ¿Qué resuelve BAU y qué se escala?
- ¿A quién, según el tipo? (dato de origen, parametrización, Qlik, base de datos, infraestructura)
- ¿Hay guardia fuera de horario? ¿Cómo se contacta?
- ¿Qué se considera crítico y cuál es el compromiso de respuesta?

**`I15` — volumetría típica**

```sql
SELECT cod_load_plan, count(*) AS cargas_30d,
       round(avg(amt_register_process)) AS media_filas,
       min(amt_register_process) AS minimo, max(amt_register_process) AS maximo
FROM   stg_s3.aud_load_trace_t
WHERE  amt_register_process IS NOT NULL AND dat_load_date > CURRENT_DATE - 30
GROUP  BY 1 ORDER BY 1;
```

**Opcional pero valioso:** las incidencias más frecuentes del último trimestre, aunque sea de
memoria. Con eso ordeno el catálogo de alertas `R5_09` por frecuencia real y no por gravedad teórica.

---

## Paquete mínimo pendiente

1. Volcado de funciones de `exp_s3` (bloque 2) ← **lo que más rinde**
2. DDL de las cuatro tablas del bloque 3
3. Listado de jobs de Rundeck + un job de mapeo
4. Las ocho consultas del bloque 5
5. Historial de la tarea `RecargadesdeRundeck` en Qlik

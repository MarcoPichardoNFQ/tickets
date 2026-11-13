---
titulo: "R5.09 — Catálogo de alertas conocidas y su primera acción"
familia: R5
etapa: "Transversal"
tipo: Runbook
tags:
  - familia/R5
  - etapa/transversal
  - tipo/runbook
keywords: "catálogo de alertas, primera acción, qué hacer, asunto del correo, triaje"
---

# R5.09 — Catálogo de alertas conocidas y su primera acción

**Etapa:** Transversal
**Tipo:** Runbook
**Palabras clave:** catálogo de alertas, primera acción, qué hacer, asunto del correo, triaje

## En una línea

Qué significa cada alerta que llega y cuál es el primer paso — sin entrar todavía a diagnosticar.

## `URGENTE no se recibieron todas las interfaces`

**Job:** `Validacion Cantidades Recibidas`

**Qué significa realmente:** la suma de seis comprobaciones sobre el lote no dio cero. **Sólo dos de
esas seis son sobre ficheros ausentes.** El asunto es engañoso.

**Primera acción:**

```sql
SELECT nome_interface_base, recebido, track_status
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
  AND  (NOT recebido OR NOT track_status);
```

Si no devuelve nada, la alerta viene de la comparación contra el lote de referencia fijo `29817` y
probablemente es ruido. Ver [R4_03_validacion_cantidades](../R4%20-%20Sets%20incompletos/R4_03_validacion_cantidades.md).

## `ERROR EN MAPEO REVISAR TABLA`

**Job:** `Job control errores mapeo` (posiblemente duplicado)

**Qué significa:** hay registros en `trf_s3.s3_control_errores_mapeo` de los últimos 30 minutos.

**Primera acción:**

```sql
SELECT * FROM trf_s3.s3_control_errores_mapeo
WHERE  dat_proc_exe > NOW() - INTERVAL '2 hours'
ORDER  BY dat_proc_exe DESC;
```

Comprueba si es un deadlock que el reintento ya resolvió: mira si la tabla destino tiene datos
actualizados. Si los tiene, no hay nada que hacer. Ver [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md).

## Fallo de un bloque `OptimizacioBloque*TRFySTG`

**Qué significa:** algún paso del bloque falló. **Pero el bloque siguió ejecutando todos los
demás**: los `exit` están comentados en el script. No supongas que se detuvo.

**Primera acción:** en Rundeck, revisar paso a paso cuál falló. Y en base de datos:

```sql
SELECT cod_load_trace, cod_load_plan, step_load, cod_status, des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  dat_load_date::date = CURRENT_DATE AND cod_status = -1
ORDER  BY dat_load_date DESC;
```

**Causa más frecuente, y suele ser ruido:** un «PASO OMITIDO» por una interfaz que hoy no tocaba.
Ver [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md).

## Fallo de `Manejo Flag` o `LLamada Rundeck Flags Obligatorios`

**Qué significa:** problema en la recepción. Es de las más graves porque afecta al arranque.

**Primera acción:**

```sql
SELECT id_camda, nome_base, nome_completo, data, data_recebemento
FROM   stg_s3.controlflag_arquivos
ORDER  BY id DESC LIMIT 10;
```

Y comprobar si hay flags sin procesar en el directorio de llegada. Ver [R4_06_xml_sin_flag](../R4%20-%20Sets%20incompletos/R4_06_xml_sin_flag.md).

## Fallo de `Mapeos` o `MapeosFlag`

**Qué significa:** el orquestador de mapeos falló. Puede ser un mapeo concreto o el ciclo entero.

**Primera acción:** distinguir si falló **uno** o **ninguno corrió**. Cambia por completo el
diagnóstico. Ver [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md).

## Fallo de `0999 Carga Megara` o del vigilante de presencia

**Qué significa:** el job que sondea cada 3 segundos. **Es la alerta más grave del sistema**: si no
funciona, nada se detecta y nada avanza.

**Primera acción:** comprobar en Rundeck si sigue ejecutándose. Una interrupción en su serie de
ejecuciones marca la hora exacta en que el sistema se paró. Ver [B04_job_validacion_constante](../B%20-%20Recepcion%20y%20flags/B04_job_validacion_constante.md).

**Ojo:** al ejecutarse 20 veces por minuto, un fallo persistente genera miles de alertas por hora.
Ante una avalancha de correos del mismo job, es éste.

## Alerta de `_00001 Análise de erros`

**No la vas a recibir.** Su consulta está anulada con `WHERE 1=0` y no puede detectar nada.
Ver [R5_08_analise_de_erros_anulado](../R5%20-%20Alertas%20Rundeck/R5_08_analise_de_erros_anulado.md).

## Tabla de triaje

| Alerta | Gravedad | Primera acción |
|---|---|---|
| Vigilante de presencia caído | **Crítica** | Restaurar el job: el sistema está parado |
| `Manejo Flag` | Alta | Comprobar recepción de flags |
| `URGENTE no se recibieron...` | Media | Consultar `controlflag_interfaces`; a menudo ruido |
| `ERROR EN MAPEO` | Media | Consultar tabla de errores; a menudo deadlock resuelto |
| Fallo de bloque | Baja-media | Suele ser «PASO OMITIDO» de una interfaz que no tocaba |
| Avalancha del mismo job | Alta | Es el vigilante; parar el ruido antes de diagnosticar |

## Ver también

[R5_01_como_notifica_rundeck](../R5%20-%20Alertas%20Rundeck/R5_01_como_notifica_rundeck.md) · [R5_07_alerta_vs_estado_real](../R5%20-%20Alertas%20Rundeck/R5_07_alerta_vs_estado_real.md) · [R5_08_analise_de_erros_anulado](../R5%20-%20Alertas%20Rundeck/R5_08_analise_de_erros_anulado.md) · [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md) · [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md)

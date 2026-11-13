---
titulo: "J08 — Los cinco avisos que más ruido hacen"
familia: J
etapa: "Transversal"
tipo: Runbook
tags:
  - familia/J
  - etapa/transversal
  - tipo/runbook
keywords: "ruido, falsos positivos, primera acción, triaje rápido, treinta segundos"
---

# J08 — Los cinco avisos que más ruido hacen

**Etapa:** Transversal
**Tipo:** Runbook
**Palabras clave:** ruido, falsos positivos, primera acción, triaje rápido, treinta segundos

## En una línea

Cinco señales explican la mayor parte de los avisos que **no son incidencias** — y cada una se
descarta en menos de un minuto.

## 1. `PASO OMITIDO` y el bloque en rojo

**Qué pasa:** una interfaz no tiene fichero hoy. El script marca error general y **el bloque entero
acaba en rojo**, aunque todo lo demás fuera bien.

**Descartarlo:**

```sql
SELECT dat_load_date::date AS dia, count(*), sum(amt_register_process) AS filas
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_plan = :plan AND dat_load_date > CURRENT_DATE - 45
GROUP  BY 1 ORDER BY 1 DESC;
```

Patrón semanal o mensual con huecos regulares → esa interfaz hoy no tocaba. **Cerrar.**

Es incidencia sólo si el flag declaró esa interfaz. Ver [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md) y [R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md).

## 2. `URGENTE no se recibieron todas las interfaces`

**Qué pasa:** la suma de seis comprobaciones no dio cero. **Sólo dos son sobre ficheros ausentes**, y
una compara contra un lote de referencia fijo que es un `MEGAACCOUNTING_EndOfDay` de 133 interfaces.

**Un lote intradía no casa nunca con esa referencia**, así que debería alertar siempre.

**Descartarlo:**

```sql
SELECT nome_interface_base, recebido, track_status
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
  AND  (NOT recebido OR NOT track_status);
```

Sin filas → es la comparación contra el lote fijo. **Cerrar.** Ver [R4_03_validacion_cantidades](../R4%20-%20Sets%20incompletos/R4_03_validacion_cantidades.md).

## 3. `ERROR EN MAPEO REVISAR TABLA`

**Qué pasa:** hay registros de error de los últimos 30 minutos. Pero un deadlock que el reintento
resolvió **también deja registro**.

**Descartarlo:**

```sql
SELECT count(*), max(dat_qlikupdate) FROM trf_s3.<TABLA_DESTINO>;
```

Datos actualizados de hoy → el reintento funcionó. **Cerrar.**

Sólo es incidencia si el mensaje dice `Se agotaron los intentos`. Ver [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md) y
[R3_02_leer_error_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_02_leer_error_mapeo.md).

## 4. Avalancha de correos del mismo job

**Qué pasa:** `0999 Carga Megara` corre **cada 3 segundos** — 20 veces por minuto. Un fallo
persistente genera miles de alertas por hora.

**Qué hacer:** no es ruido inocuo. **Es la alerta más grave del sistema**: si el vigilante falla,
nada se detecta y nada avanza.

Comprobar en Rundeck si sigue ejecutándose; una interrupción en su serie marca la hora exacta en que
el sistema se paró. Ver [B04_job_validacion_constante](../B%20-%20Recepcion%20y%20flags/B04_job_validacion_constante.md).

## 5. Mensajes de traza que no corresponden a nada

| Mensaje | Realidad |
|---|---|
| `Error de Validacion de Nulos. Tabla Truncada` | Texto fijo. **No se trunca nada** en flujo tolerante — y hoy todas las cargas lo son |
| CSV de salida de 0 bytes | Deliberados: nodos del XSD ausentes en el XML |
| Tabla `MEG_*` vacía tras el cierre | La limpieza las vacía todas por diseño |
| Texto con `¡` donde iba `!` | Sustitución deliberada antes de convertir |

Ver [R1_04_descarte_nulo_obligatorio](../R1%20-%20Descartes/R1_04_descarte_nulo_obligatorio.md), [C06_ficheros_de_salida](../C%20-%20Conversion%20Java/C06_ficheros_de_salida.md), [H02_stg_startover_cleanup](../H%20-%20Cierre%20y%20Qlik/H02_stg_startover_cleanup.md) y
[C05_sed_separador](../C%20-%20Conversion%20Java/C05_sed_separador.md).

## El triaje de treinta segundos

```
¿Es uno de estos cinco?
   SÍ → aplicar su comprobación → cerrar citando la ficha
   NO → analizar en serio → J07
```

**Documenta el cierre.** Es lo que evita que el siguiente turno repita la investigación entera, que
es el coste real de estos falsos positivos.

## Y al revés: lo que parece correcto y no lo está

El ruido tiene su espejo. Seis mecanismos hacen que un fallo real pase inadvertido: los 22 jobs sin
notificación, el análisis de errores anulado, los mapeos desactivados en verde, los mapeos
huérfanos, el `retry_deadlock` NULL y la recarga de Qlik que no se comprueba.

Por eso el silencio no es evidencia y el checklist diario no es opcional.
Ver [R5_07_alerta_vs_estado_real](../R5%20-%20Alertas%20Rundeck/R5_07_alerta_vs_estado_real.md) y [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md).

## Ver también

[J10_trampas_conocidas](../J%20-%20Operacion/J10_trampas_conocidas.md) · [R5_09_catalogo_alertas](../R5%20-%20Alertas%20Rundeck/R5_09_catalogo_alertas.md) · [R5_10_cadena_escalado](../R5%20-%20Alertas%20Rundeck/R5_10_cadena_escalado.md) · [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md) · [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md)

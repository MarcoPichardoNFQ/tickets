---
titulo: "D11 — «PASO OMITIDO»: no había fichero"
familia: D
etapa: "Carga STG"
tipo: Runbook
tags:
  - familia/D
  - etapa/carga-stg
  - tipo/runbook
keywords: "PASO OMITIDO, no existe archivo, sin fichero, flag_error_gral, log de Rundeck"
---

# D11 — «PASO OMITIDO»: no había fichero

**Etapa:** Carga STG
**Tipo:** Runbook
**Palabras clave:** PASO OMITIDO, no existe archivo, sin fichero, flag_error_gral, log de Rundeck

## Síntoma

En el log del job de Rundeck aparece:

```
no existe archivo y descartes *****************PASO OMITIDO****************
```

Y el bloque acaba marcando error aunque aparentemente no haya pasado nada malo.

## Qué significa exactamente

El script comprueba dos cosas antes de cargar: si hay **fichero** esperando y si hay **descartes**
pendientes en la tabla `_DES`.

```bash
select=`ls -ltr $raiz$fichero | grep -v '_InLoad' | head -1 | cut -f 1 -d '.'`
descartes="select 1 from stg_s3.${nom_tab}_des limit 1"

if [ "$select" ]; then
    # hay fichero → se procesa
elif [[ -z "$select" && -z "$V_DESCARTES" ]]; then
    # ni fichero ni descartes → PASO OMITIDO, flag_error_gral=1
else
    # no hay fichero pero SÍ hay descartes → "Condición no cubierta", no se hace nada
fi
```

Tres desenlaces, y dos de ellos no cargan nada:

| Fichero | Descartes | Resultado |
|---|---|---|
| Sí | — | Se procesa normalmente |
| No | No | **PASO OMITIDO** y se marca error general |
| No | Sí | «Condición no cubierta»: no se procesa, **no** se marca error |

## Lo importante: casi nunca es una incidencia

Que no haya fichero es lo normal para muchas interfaces. No todas las interfaces llegan todos los
días: las hay semanales, mensuales y de fin de mes. Un «PASO OMITIDO» en una interfaz que sólo
llega los viernes es el comportamiento correcto de martes a jueves.

**El problema es que marca `flag_error_gral=1`**, y eso hace que el bloque entero termine en rojo.
Un job en rojo cuya única causa es un paso omitido de una interfaz que hoy no tocaba **no es una
incidencia**. Es la fuente de ruido más habitual de esta etapa.

## Cómo distinguir ruido de incidencia real

**1. ¿Esta interfaz debía llegar hoy?**

```sql
-- ¿Con qué frecuencia llega históricamente?
SELECT dat_load_date::date AS dia, count(*), sum(amt_register_process) AS filas
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_plan = :plan
  AND  dat_load_date >= CURRENT_DATE - 45
GROUP  BY 1 ORDER BY 1 DESC;
```

Si el patrón es semanal o mensual y hoy no toca, cierra el ticket.

**2. ¿Llegó el flag que anuncia este lote?** Si el flag llegó y declaraba esta interfaz, entonces sí
falta un fichero y es una incidencia de set incompleto → familia `R4`.

**3. ¿Está el fichero pero con otro nombre?** El patrón del lookup puede no casar:

```bash
. /nfq/data/cfg/env.properties
grep '|<id>|' /nfq/data/cfg/lookup_stg.txt   # ver el patrón esperado
ls -la $raiz | grep -i "<parte_del_nombre>"  # ver qué hay realmente
```

Un fichero con nombre ligeramente distinto está ahí pero es invisible para el script.

**4. ¿Está atascado como `_InLoad`?** La búsqueda excluye esos ficheros a propósito. Si hay un
`FICHERO_InLoad.csv` de hace horas, el fichero existe pero el script no lo ve.
Ver [D08_gpg_historificacion](../D%20-%20Carga%20STG/D08_gpg_historificacion.md).

## Acción

| Situación | Qué hacer |
|---|---|
| Interfaz que hoy no tocaba | Nada. Cerrar como ruido conocido |
| Flag llegó y declara la interfaz | Escalar como set incompleto → `R4` |
| Fichero con nombre que no casa | Comprobar el patrón; corregir origen o parametrización |
| Fichero atascado en `_InLoad` | Renombrar a original tras comprobar que no cargó ya |

## Cuándo escalar

Cuando el flag declara la interfaz y el fichero no está: alguien tiene que enviarlo. Y cuando el
patrón del lookup ya no casa con el nombre que manda el origen, porque eso se repetirá cada día.

## Ver también

[D03_script_stg_trf](../D%20-%20Carga%20STG/D03_script_stg_trf.md) · [D08_gpg_historificacion](../D%20-%20Carga%20STG/D08_gpg_historificacion.md) · [D10_tabla_t_vacia](../D%20-%20Carga%20STG/D10_tabla_t_vacia.md) · [R1_10_descarte_correcto_sin_accion](../R1%20-%20Descartes/R1_10_descarte_correcto_sin_accion.md)

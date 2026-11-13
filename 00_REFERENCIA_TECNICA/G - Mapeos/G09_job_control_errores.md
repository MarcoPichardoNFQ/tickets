---
titulo: "G09 — `Job control errores mapeo` y `s3_control_errores_mapeo`"
familia: G
etapa: "Mapeos"
tipo: Referencia
tags:
  - familia/G
  - etapa/mapeos
  - tipo/referencia
keywords: "s3_control_errores_mapeo, control de errores, 30 minutos, dat_proc_exe, alerta"
---

# G09 — `Job control errores mapeo` y `s3_control_errores_mapeo`

**Etapa:** Mapeos
**Tipo:** Referencia
**Palabras clave:** s3_control_errores_mapeo, control de errores, 30 minutos, dat_proc_exe, alerta

## En una línea

Un job comprueba si la tabla de errores de mapeo tiene registros de los **últimos 30 minutos**, y si
los hay, falla para disparar la alerta.

## El mecanismo

```sql
SELECT COUNT(cod_id)
FROM   trf_s3.s3_control_errores_mapeo
WHERE  dat_proc_exe > NOW() - INTERVAL '30 minutes';
```

```bash
if [ "$result" -gt 0 ]; then
    echo "Salida -1 ERROR EN MAPEO REVISAR TABLA"
    exit -1
else
    exit 0
fi
```

Si el conteo es mayor que cero, el job sale con error y la notificación `onfailure` manda el correo.

**`trf_s3.s3_control_errores_mapeo` es la tabla donde aterrizan los fallos de mapeo.** Es el primer
sitio donde mirar ante cualquier incidencia de esta capa.

```sql
SELECT * FROM trf_s3.s3_control_errores_mapeo
WHERE  dat_proc_exe > NOW() - INTERVAL '4 hours'
ORDER  BY dat_proc_exe DESC;
```

## ⚠ La ventana de 30 minutos

El control mira **sólo los últimos 30 minutos**. Eso tiene dos caras:

**Un error de hace 40 minutos no dispara alerta.** Si el job se ejecuta con retraso, o si el error
ocurrió al principio de un ciclo largo, la comprobación llega tarde y **el fallo pasa
inadvertido**. El registro sigue en la tabla, pero nadie avisa.

**El job en verde no significa «no hay errores».** Significa «no hay errores en los últimos 30
minutos». Para saber si el ciclo de hoy tuvo fallos, hay que consultar la tabla directamente
filtrando por el día:

```sql
SELECT date_trunc('hour', dat_proc_exe) AS hora, count(*) AS errores
FROM   trf_s3.s3_control_errores_mapeo
WHERE  dat_proc_exe::date = CURRENT_DATE
GROUP  BY 1 ORDER BY 1 DESC;
```

Ésa es la consulta que de verdad responde «¿hubo errores hoy?».

## Dos jobs con el mismo nombre

En los exports hay dos ficheros: `Job_control_errores_mapeo.xml` y
`Job_control_errores_mapeo (verificar si es el mismo).xml`. El propio nombre del segundo indica que
alguien dudaba de si eran duplicados.

Consecuencia práctica: **puede haber dos jobs comprobando lo mismo**, y por tanto dos alertas por el
mismo error, posiblemente a listas de distribución distintas. Si recibes alertas duplicadas de
mapeos, ésta es la explicación. Merece comprobarse en Rundeck y consolidarse.

## La conexión a base de datos

A diferencia de otros scripts, éste construye la conexión a mano con las variables de
`credentials.properties`:

```bash
PGPASSWORD="$POSTGRES_PASSWORD" psql -t -A \
  -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" \
  -d "$POSTGRES_DATABASE" -U "$POSTGRES_USERNAME" -c "$sql"
```

Usa `-t -A`, salida sin cabeceras ni formato, así que la comparación numérica posterior funciona
correctamente. No todos los scripts del sistema tienen ese cuidado. Ver [R4_03_validacion_cantidades](../R4%20-%20Sets%20incompletos/R4_03_validacion_cantidades.md).

## Qué hacer cuando salta

1. **Mira la tabla**, no el mensaje del job:

```sql
SELECT * FROM trf_s3.s3_control_errores_mapeo
WHERE  dat_proc_exe > NOW() - INTERVAL '2 hours'
ORDER  BY dat_proc_exe DESC;
```

2. Identifica qué mapeo y qué error.
3. Si es un deadlock, comprueba si el reintento lo resolvió. Ver [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md).
4. Si el mapeo falló definitivamente, ve a [R3_01_anatomia_fallo_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_01_anatomia_fallo_mapeo.md).

## La estructura de la tabla

```
trf_s3.s3_control_errores_mapeo
  cod_id        integer                      NOT NULL
  des_func      character varying            NOT NULL   ← la función de mapeo que falló
  cod_sqlstate  character varying            NOT NULL   ← el código de error de PostgreSQL
  des_sqlerrm   character varying            NOT NULL   ← el mensaje completo
  dat_proc_exe  timestamp without time zone  NOT NULL
```

Cinco columnas, y las tres del medio dan el diagnóstico completo: **qué función, qué código y qué
mensaje**. No hay `id_mapeo`: el enlace con la tabla de control es por `des_func` =
`tablas_mapeio_t.nome_fn_mapeio`.

```sql
-- Errores de hoy, con el mapeo al que pertenecen
SELECT e.dat_proc_exe, e.cod_sqlstate, e.des_func, e.des_sqlerrm,
       t.id_mapeo, t.nome_tabela_aldrin
FROM   trf_s3.s3_control_errores_mapeo e
LEFT   JOIN exp_s3.tablas_mapeio_t t ON t.nome_fn_mapeio = e.des_func
WHERE  e.dat_proc_exe::date = CURRENT_DATE
ORDER  BY e.dat_proc_exe DESC;
```

### Los códigos que verás

| `cod_sqlstate` | Significado real | Reintenta |
|---|---|---|
| `40P01` | `deadlock_detected` | **Sí**, con `pg_sleep` |
| `21000` | `cardinality_violation` — una subconsulta devolvió más de una fila | No |
| Otros | Error no controlado | No |

**Ojo con `21000`.** El código lo etiqueta como «Duplicate error», pero no es una clave duplicada
—eso sería `23505`—: es una subconsulta del mapeo que devuelve más filas de las que espera. Buscar
un duplicado de datos ante ese código lleva por el camino equivocado.

Y el mensaje `'Se agotaron los intentos por deadlock'` en `des_sqlerrm` indica que el reintento
llegó a su límite. Ver [G08_fim_carga_mapeo](../G%20-%20Mapeos/G08_fim_carga_mapeo.md).

## Ver también

[R3_01_anatomia_fallo_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_01_anatomia_fallo_mapeo.md) · [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md) · [R3_12_consultas_mapeos](../R3%20-%20Errores%20de%20mapeo/R3_12_consultas_mapeos.md) · [R5_09_catalogo_alertas](../R5%20-%20Alertas%20Rundeck/R5_09_catalogo_alertas.md)

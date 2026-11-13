---
titulo: "H09 — Qlik muestra datos de ayer"
familia: H
etapa: "Cierre y Qlik"
tipo: Runbook
tags:
  - familia/H
  - etapa/cierre-y-qlik
  - tipo/runbook
keywords: "Qlik desactualizado, datos de ayer, recarga, dat_qlikupdate, tablero"
---

# H09 — Qlik muestra datos de ayer

**Etapa:** Cierre y Qlik
**Tipo:** Runbook
**Palabras clave:** Qlik desactualizado, datos de ayer, recarga, dat_qlikupdate, tablero

## Síntoma

El usuario ve en Qlik datos del día anterior.

## La escalera de diagnóstico

Ve **de abajo arriba**: comprueba primero si el dato existe en la última capa antes de Qlik y
retrocede. Cinco preguntas resuelven el caso.

### 1. ¿Está el dato en `exp_s3`?

```sql
SELECT count(*) FROM trf_s3.<TABLA_DESTINO>;
```

Y si la tabla tiene columna de fecha de actualización:

```sql
SELECT max(dat_qlikupdate) FROM trf_s3.<TABLA_DESTINO>;
```

**Sí, con datos de hoy** → el problema es sólo de recarga. Ve al punto 2.
**No** → el problema es anterior. Salta al punto 4.

### 2. ¿Se lanzó la recarga de esa tabla?

Cada tabla tiene su propia tarea:

```bash
grep -i "<TABLA>" /nfq/data/cfg/lookup_qlik.txt
```

Devuelve el nombre de la tarea, su UUID y el flag que la dispara. Con eso, comprueba en la consola
de Qlik el historial de esa tarea concreta. Ver [H07_lookup_qlik](../H%20-%20Cierre%20y%20Qlik/H07_lookup_qlik.md).

### 3. ¿Hay flags de Qlik sin consumir?

```bash
. /nfq/data/cfg/env.properties
ls -la $bandera | grep -i "^Qlik_"
```

Flags acumulados = las recargas no se están consumiendo. Ése es el diagnóstico.

### 4. ¿Corrió el mapeo?

```sql
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio, activo_inactivo
FROM   exp_s3.tablas_mapeio_t
WHERE  nome_tabela_aldrin ILIKE '%<TABLA>%';
```

Desactivado → [R3_07_mapeo_desactivado](../R3%20-%20Errores%20de%20mapeo/R3_07_mapeo_desactivado.md). Activo pero sin ejecutar → [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md).

### 5. ¿Llegó el dato hasta `trf_s3`?

```sql
SELECT count(*) FROM trf_s3.<TABLA_ORIGEN>;
```

Si tampoco está, el problema es de carga o de recepción, y estás ante un caso de la familia `R4` o
`D`, no de Qlik. Ver [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md).

## Tabla de decisión

| `exp_s3` | Recarga lanzada | Diagnóstico |
|---|---|---|
| Datos de hoy | Sí, correcta | Problema en el propio Qlik (caché, tablero, permisos) |
| Datos de hoy | No | **Recarga no disparada** → punto 3 |
| Datos de ayer | — | El mapeo no corrió → punto 4 |
| Vacía | — | Problema aguas arriba → punto 5 |

## ⚠ Sobre el paso de recarga

El paso «Recarga Qlik» es el **último del proceso y el único punto donde Rundeck toca Qlik**. Lanza
una sola tarea global, `RecargadesdeRundeck`, cuyo `curl` lleva `--X POST` —opción que curl rechaza,
terminando sin enviar nada— y a continuación hace `exit 0` sin comprobar el resultado.

Dos consecuencias para este runbook:

**Ese paso sale verde siempre.** No lo uses nunca como prueba de que la recarga se lanzó.

**Si en producción el script está tal como aparece en el export, Rundeck no lanza ninguna recarga**,
y lo que actualice los tableros es ajeno a esta orquestación. Eso convierte el punto 2 de arriba
—consultar el historial de la tarea en la consola de Qlik— en la **única** verificación fiable.

Ver [H08_recarga_qlik](../H%20-%20Cierre%20y%20Qlik/H08_recarga_qlik.md).

## Si todo está bien hasta Qlik

Si el dato está en `exp_s3`, la tarea de recarga se ejecutó correctamente y aun así el tablero
muestra datos viejos, el problema está **dentro de Qlik**: caché del tablero, el objeto no usa la
tabla que crees, o el usuario mira una selección guardada. Eso ya no es de esta base de conocimiento
ni de esta cadena: escala al responsable de Qlik con la evidencia de que el dato sí está publicado.

## Qué llevar al escalado

- Nombre de la tabla en `exp_s3` y su conteo
- `max(dat_qlikupdate)` si existe
- Nombre y UUID de la tarea de Qlik correspondiente
- Resultado del historial de esa tarea
- Si hay flags `Qlik_*` pendientes

## Ver también

[H07_lookup_qlik](../H%20-%20Cierre%20y%20Qlik/H07_lookup_qlik.md) · [H08_recarga_qlik](../H%20-%20Cierre%20y%20Qlik/H08_recarga_qlik.md) · [H12_recarga_qlik_fallo](../H%20-%20Cierre%20y%20Qlik/H12_recarga_qlik_fallo.md) · [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md) · [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md)

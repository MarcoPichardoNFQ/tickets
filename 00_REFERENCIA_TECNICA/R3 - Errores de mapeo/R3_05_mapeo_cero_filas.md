---
titulo: "R3.05 — Mapeo con 0 filas: causa legítima o fallo"
familia: R3
etapa: "Mapeos"
tipo: Runbook
tags:
  - familia/R3
  - etapa/mapeos
  - tipo/runbook
keywords: "cero filas, tabla vacía, sin datos, origen vacío, filtro de negocio"
---

# R3.05 — Mapeo con 0 filas: causa legítima o fallo

**Etapa:** Mapeos
**Tipo:** Runbook
**Palabras clave:** cero filas, tabla vacía, sin datos, origen vacío, filtro de negocio

## Síntoma

El mapeo se ejecutó sin error y la tabla destino quedó vacía o con muchas menos filas de lo normal.

## Qué mirar primero

Compara origen y destino. Es la comprobación que separa los tres casos posibles:

```sql
SELECT (SELECT count(*) FROM trf_s3.<TABLA_ORIGEN>)  AS origen,
       (SELECT count(*) FROM trf_s3.<TABLA_DESTINO>) AS destino;
```

| Origen | Destino | Diagnóstico |
|---|---|---|
| 0 | 0 | **No hay datos que mapear.** El problema está aguas arriba |
| >0 | 0 | **La lógica del mapeo los excluye todos** |
| >0 | <origen | Normal si hay filtros; anómalo si la proporción cambió |

## Caso 1 — origen vacío

El mapeo hizo su trabajo: no había nada. La causa está antes, y hay que seguirla hacia atrás:

```sql
-- ¿Cargó la interfaz que alimenta esta tabla?
SELECT cod_load_trace, dat_load_date, amt_register_process, cod_status, des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  des_file_loaded ILIKE '%<INTERFAZ>%'
ORDER  BY dat_load_date DESC LIMIT 5;
```

```sql
-- ¿Se descartó todo?
SELECT des_validate, count(*) FROM stg_s3.aud_load_valid_trace_t
WHERE  des_table_name ILIKE '%<TABLA>%' AND dat_load_date::date = CURRENT_DATE
GROUP  BY 1;
```

Ver [R4_11_efecto_domino](../R4%20-%20Sets%20incompletos/R4_11_efecto_domino.md) y [R1_12_descarte_masivo_escalado](../R1%20-%20Descartes/R1_12_descarte_masivo_escalado.md).

## Caso 2 — hay origen y el destino queda a cero

Las filas existen pero la consulta del mapeo las excluye todas. Cuatro razones habituales:

**Un `INNER JOIN` que no casa.** La tabla con la que cruza está vacía o no tiene las claves
esperadas. Es la causa dominante y suele ser un efecto dominó: falta el catálogo con el que cruza.

**Un `WHERE` de fecha.** Muchos mapeos filtran por fecha de proceso o día hábil. Si el calendario no
está actualizado o la fecha de referencia es otra, el filtro se lleva todo.

**Un filtro de estado.** El mapeo sólo procesa filas en cierto estado y hoy ninguna lo tiene.

**Un filtro de pendientes.** Algunos mapeos sólo procesan lo que está marcado como pendiente. Si el
marcado no ocurrió, no hay nada que hacer y el mapeo sale con cero legítimamente.

Para saber cuál es, hay que leer la función:

```sql
SELECT prosrc FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'exp_s3' AND p.proname = '<nome_fn_mapeio>';
```

Busca los `INNER JOIN` y los `WHERE`: en ese SQL está la respuesta, no en ningún parámetro.

## Caso 3 — menos filas de lo normal

El más sutil. Contrasta con la historia del propio destino antes de decidir si es anómalo:

```sql
SELECT count(*) FROM trf_s3.<TABLA_DESTINO>;
```

Y si la tabla tiene columna de fecha:

```sql
SELECT <col_fecha>::date AS dia, count(*)
FROM   trf_s3.<TABLA_DESTINO>
GROUP  BY 1 ORDER BY 1 DESC LIMIT 15;
```

Una caída brusca frente a los días anteriores es incidencia. Una variación del 10 % probablemente
sea el negocio.

## Cuándo NO es incidencia

- **Origen legítimamente vacío**: un día sin movimientos de ese tipo.
- **Filtro de negocio permanente**: el mapeo excluye siempre a ese conjunto, por diseño. No es un
  descarte a reintentar. Ver [R1_08_descartes_en_mapeos](../R1%20-%20Descartes/R1_08_descartes_en_mapeos.md).
- **Interfaz de periodicidad no diaria**: sólo trae datos ciertos días.

La forma de distinguirlo es la serie histórica: si el destino lleva meses alternando cero y datos,
el cero es su comportamiento normal.

## Cuándo escalar

- Si el origen está vacío por un fallo de carga: es una incidencia de la etapa anterior.
- Si el mapeo excluye todo y no está claro por qué: hace falta quien conozca la regla de negocio.

## Ver también

[R3_10_corrio_pero_no_llego](../R3%20-%20Errores%20de%20mapeo/R3_10_corrio_pero_no_llego.md) · [R3_08_dependencia_insatisfecha](../R3%20-%20Errores%20de%20mapeo/R3_08_dependencia_insatisfecha.md) · [R1_08_descartes_en_mapeos](../R1%20-%20Descartes/R1_08_descartes_en_mapeos.md) · [R4_11_efecto_domino](../R4%20-%20Sets%20incompletos/R4_11_efecto_domino.md)

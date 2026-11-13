---
titulo: "G12 — Las tablas `_err` de los mapeos"
familia: G
etapa: "Mapeos"
tipo: Referencia
tags:
  - familia/G
  - etapa/mapeos
  - tipo/referencia
keywords: "_err, duplicados, clave natural, deduplicación, concatenate, purga"
---

# G12 — Las tablas `_err` de los mapeos

**Etapa:** Mapeos
**Tipo:** Referencia
**Palabras clave:** _err, duplicados, clave natural, deduplicación, concatenate, purga

## En una línea

Cada mapeo aparta sus duplicados por clave natural en `trf_s3.<TABLA>_err` — las 119 funciones lo
hacen, siempre con el mismo patrón.

## El patrón

Al final de cada función, una CTE agrupa por la clave natural y manda a `_err` lo repetido:

```sql
WITH DuplicatedRecordsCTE AS (
    ... GROUP BY <clave_natural> HAVING COUNT(*) > 1 ...
)
INSERT INTO trf_s3.<TABLA>_err (<columnas>, concatenate)
SELECT <columnas>, concatenate FROM DuplicatedRecordsCTE;
```

Es **deduplicación por clave**, no validación de contenido: una fila va a `_err` por estar repetida,
no por tener un dato malo.

La columna `concatenate` guarda la clave natural concatenada, que es lo que permite identificar el
grupo de duplicados.

## Qué NO son

No hay que confundirlas con las de staging:

| Tabla | Esquema | Qué guarda |
|---|---|---|
| `<TABLA>_ERR` | `stg_s3` | Filas con error de **nulos** |
| `<TABLA>_DES` | `stg_s3` | Filas descartadas por **clave foránea** |
| `<TABLA>_err` | `trf_s3` | **Duplicados por clave natural** apartados por un mapeo |

Las de staging las gestiona la maquinaria declarativa (`PAR_MAESTRO_VALID_T`,
`AUD_LOAD_VALID_TRACE_T`). Las de mapeo, cada función por su cuenta.

Ver [R1_02_donde_cae_cada_cosa](../R1%20-%20Descartes/R1_02_donde_cae_cada_cosa.md) y [R1_08_descartes_en_mapeos](../R1%20-%20Descartes/R1_08_descartes_en_mapeos.md).

## Consultarlas

```sql
-- ¿Qué apartó este mapeo?
SELECT count(*) FROM trf_s3.<TABLA>_err;

SELECT * FROM trf_s3.<TABLA>_err
ORDER  BY dat_qlikupdate DESC LIMIT 20;
```

```sql
-- Duplicados de hoy en toda la capa de mapeos
DO $$
DECLARE r record; n bigint;
BEGIN
  FOR r IN SELECT table_name FROM information_schema.tables
           WHERE table_schema = 'trf_s3' AND table_name LIKE '%\_err'
  LOOP
    EXECUTE format('SELECT count(*) FROM trf_s3.%I WHERE dat_qlikupdate::date = CURRENT_DATE',
                   r.table_name) INTO n;
    IF n > 0 THEN RAISE NOTICE '% -> % duplicados hoy', r.table_name, n; END IF;
  END LOOP;
END $$;
```

Ése es exactamente el barrido que hace el paso `Validacion Descartes` del cierre.
Ver [H03_validacion_descartes](../H%20-%20Cierre%20y%20Qlik/H03_validacion_descartes.md).

## Se purgan periódicamente

El propio mensaje del control lo dice:

> «Algunas tablas contienen información descartada, para mayor detalle contacte a soporte BAU.
> **Los registros serán eliminados periodicamente**»

Así que **estas tablas no son un histórico fiable**. Si necesitas conservar evidencia de un
duplicado concreto, extráela antes de que la purga la retire.

## Qué hacer con un duplicado apartado

**No es un fallo del mapeo**: el mapeo hizo lo correcto al detectarlo. El duplicado viene de más
arriba, y casi siempre de staging, donde nada lo detecta ni lo impide.

La cadena típica:

```
fichero con la fila repetida
   → staging la carga dos veces (sin clave primaria, sin validación activa)
      → la transformación la propaga
         → el mapeo la detecta y aparta el duplicado en _err
```

Así que un duplicado en `_err` es la **primera señal** de un problema que empezó dos capas antes.
Ver [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md) y [R2_03_dentro_o_entre_cargas](../R2%20-%20Duplicados/R2_03_dentro_o_entre_cargas.md).

## Acción

1. Identifica la clave repetida en `_err`.
2. Búscala hacia atrás: ¿está duplicada en `trf_s3` de origen? ¿Y en `stg_s3`?
3. Determina si vino repetida en el fichero o si el proceso la duplicó. Ver [R2_03_dentro_o_entre_cargas](../R2%20-%20Duplicados/R2_03_dentro_o_entre_cargas.md).
4. Reporta al cliente si el origen la mandó repetida; corrige el proceso si la duplicó él.

## Ver también

[R1_08_descartes_en_mapeos](../R1%20-%20Descartes/R1_08_descartes_en_mapeos.md) · [R2_06_duplicados_en_mapeos](../R2%20-%20Duplicados/R2_06_duplicados_en_mapeos.md) · [G06_catalogo_mapeos](../G%20-%20Mapeos/G06_catalogo_mapeos.md) · [H03_validacion_descartes](../H%20-%20Cierre%20y%20Qlik/H03_validacion_descartes.md) · [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md)

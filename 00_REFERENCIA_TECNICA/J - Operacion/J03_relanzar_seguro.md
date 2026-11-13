---
titulo: "J03 — Relanzar de forma segura"
familia: J
etapa: "Transversal"
tipo: Runbook
tags:
  - familia/J
  - etapa/transversal
  - tipo/runbook
keywords: "relanzar, rerun, idempotente, duplicar, comprobaciones previas"
---

# J03 — Relanzar de forma segura

**Etapa:** Transversal
**Tipo:** Runbook
**Palabras clave:** relanzar, rerun, idempotente, duplicar, comprobaciones previas

## En una línea

**Relanza siempre el paso o el job individual, nunca el orquestador** — y comprueba tres cosas
antes.

## Las tres comprobaciones previas

### 1. ¿Ya se hizo?

```sql
SELECT cod_load_trace, dat_load_date, des_file_loaded,
       amt_register_process, cod_status, des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_plan = :plan AND dat_load_date::date = CURRENT_DATE
ORDER  BY dat_load_date;
```

### 2. ¿Sigue el fichero en el directorio?

```bash
. /nfq/data/cfg/env.properties
grep '|<id>|' /nfq/data/cfg/lookup_stg.txt | cut -d'|' -f4
ls -la $raiz | grep -i "<parte_del_patrón>"
```

**Traza correcta + fichero ya archivado** → relanzar es seguro, no hará nada.
**Traza correcta + fichero todavía presente** → **duplicará**.

### 3. ¿Está resuelta la causa?

Si falló por falta de un insumo y sigue faltando, volverá a fallar.

## Qué es idempotente y qué no

| Etapa | ¿Relanzar duplica? | Por qué |
|---|---|---|
| Conversión Java | **No** | Reescribe los ficheros de salida |
| `\COPY` a `_TMP` | **No** | `READ_HEADER_FN` trunca `_TMP` antes |
| Paso de `_TMP` a `_T` | **Depende** | Si el fichero sigue en el directorio, se recarga con otro `cod_load_trace` |
| Transformación | **Depende** | Según si el procedimiento borra antes de insertar |
| Mapeos | **Casi nunca** | Todos usan `ON CONFLICT … DO UPDATE` |

Para la transformación, la señal está al principio del procedimiento:

```sql
SELECT prosrc FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'trf_s3' AND p.proname = '<procedimiento>';
```

`DELETE FROM` o `TRUNCATE` al principio → seguro. `INSERT` directo → acumula.

## Los mapeos tienen su propia regla

**Sólo 19 de las 119 funciones borran antes de insertar.** Las otras 100 hacen upsert: no duplican,
pero tampoco limpian lo que sobrara. La lista de las 19 está en [G06_catalogo_mapeos](../G%20-%20Mapeos/G06_catalogo_mapeos.md).

Y hay una condición que sorprende: **si el contador `control_carga` de esa tabla ya llegó a `0`,
relanzar no hace nada** y el job sale en verde. Ver [R3_11_relanzar_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_11_relanzar_mapeo.md) y [R3_09_contador_no_cero](../R3%20-%20Errores%20de%20mapeo/R3_09_contador_no_cero.md).

## Por qué no el orquestador

Relanzar `Mapeos`, `Main Job Megara` o `0999`:

1. **Reejecuta decenas de pasos** que ya habían terminado bien
2. **Aumenta la concurrencia** justo cuando el problema suele ser la concurrencia
3. **Alarga el ciclo** y retrasa el cierre y la recarga de Qlik
4. Con la lista de argumentos por posición, **cualquier error de edición desalinea todo lo que va detrás**. Ver [F03_funcion_trf](../F%20-%20Transformacion%20TRF/F03_funcion_trf.md)

## La secuencia completa de recuperación

Cuando algo falló aguas arriba, el orden es de arriba abajo y no se salta ningún paso:

```
1. Resolver la causa (fichero, catálogo, bloqueo)
2. Recargar / reprocesar descartes      → R1_09
3. Reejecutar la transformación
4. Reejecutar el mapeo                  → R3_11
5. Forzar la recarga de Qlik            → H12
6. Verificar el dato, no el color del job
```

**El paso 5 es el que más se olvida**, y es el único que percibe el usuario final.

## Después de relanzar

```sql
-- ¿Cuántos trace conviven ahora?
SELECT cod_load_trace, count(*) FROM stg_s3.<TABLA>_T GROUP BY 1 ORDER BY 1 DESC;

-- ¿Se pobló el destino?
SELECT count(*), max(dat_qlikupdate) FROM trf_s3.<TABLA_DESTINO>;
```

Dos `cod_load_trace` del mismo día donde antes había uno = se duplicó.
Ver [R2_07_limpiar_sin_romper](../R2%20-%20Duplicados/R2_07_limpiar_sin_romper.md).

## Cuándo escalar antes de relanzar

- Relanzar un orquestador completo en horario operativo
- Cuando el relanzamiento pueda duplicar y el dato ya llegó a `exp_s3` o a Qlik
- Cuando haya que abrir lote nuevo de mapeos

## Ver también

[R2_05_duplicados_por_relanzar](../R2%20-%20Duplicados/R2_05_duplicados_por_relanzar.md) · [R3_11_relanzar_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_11_relanzar_mapeo.md) · [J04_que_no_tocar](../J%20-%20Operacion/J04_que_no_tocar.md) · [D13_cargo_dos_veces](../D%20-%20Carga%20STG/D13_cargo_dos_veces.md) · [G06_catalogo_mapeos](../G%20-%20Mapeos/G06_catalogo_mapeos.md)

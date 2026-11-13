---
titulo: "R2.04 — El fichero llegó dos veces: cómo confirmarlo"
familia: R2
etapa: "Carga STG"
tipo: Runbook
tags:
  - familia/R2
  - etapa/carga-stg
  - tipo/runbook
keywords: "fichero repetido, reenvío, patrón, head -1, DIR_PROCESSED, confirmar"
---

# R2.04 — El fichero llegó dos veces: cómo confirmarlo

**Etapa:** Carga STG
**Tipo:** Runbook
**Palabras clave:** fichero repetido, reenvío, patrón, head -1, DIR_PROCESSED, confirmar

## Síntoma

Sospecha de que el mismo contenido entró dos veces, pero hace falta probarlo antes de limpiar nada.

## Comprobación en tres pasos

### 1. ¿Cuántas cargas hubo?

```sql
SELECT cod_load_trace, dat_load_date, des_file_loaded, amt_register_process
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_plan = :plan
  AND  dat_load_date >= CURRENT_DATE - 2
ORDER  BY dat_load_date;
```

Dos filas `'CARGA FICHERO'` con el **mismo `amt_register_process`** es una señal fuerte: el mismo
número de filas en dos ejecuciones distintas rara vez es casualidad.

### 2. ¿Cuántos ficheros casan con el patrón?

El script coge **un solo fichero por ejecución** (`head -1` sobre un `ls` ordenado por fecha). Si
hay dos ficheros que casan con el patrón, los procesa en pasadas sucesivas y ambos entran.

```bash
. /nfq/data/cfg/env.properties
grep '|<id>|' /nfq/data/cfg/lookup_stg.txt | cut -d'|' -f4   # el patrón
ls -la $raiz | grep -i "<parte_del_patrón>"                  # qué hay realmente
```

Dos o más resultados confirman la causa.

### 3. ¿Están los dos en el histórico?

```bash
ls -lat $fileshare"DIR_PROCESSED/DIR_SAC/" | grep -i "<nombre>" | head
```

Dos ficheros `.gpg` archivados el mismo día para la misma interfaz cierran el diagnóstico.

## Comparar el contenido

Si los nombres son distintos y hace falta saber si el contenido es el mismo:

```bash
cd $fileshare"DIR_PROCESSED/DIR_SAC/"
gpg --decrypt FICHERO_A.gpg | sort | md5sum
gpg --decrypt FICHERO_B.gpg | sort | md5sum
```

Mismo hash = mismo contenido, reenvío puro. Hashes distintos = son envíos diferentes, y entonces
puede que **ambos sean legítimos** y el duplicado esté sólo en un subconjunto de filas.

## Causas y a quién corresponde

| Causa | Señal | Responsable |
|---|---|---|
| El origen reenvió | Dos ficheros, contenido idéntico, nombres distintos | Origen |
| El archivado falló | Un fichero sin `.gpg` en el histórico y sí en el directorio de trabajo | Sistema |
| Relanzamiento manual | Traza doble sin fichero nuevo | Operativa |
| Patrón demasiado amplio | El patrón casa con ficheros de otra interfaz | Parametrización |

La cuarta merece atención: un patrón como `_SAC_RF_POS.txt` es específico, pero uno como
`S3_FIN_*.csv` puede capturar ficheros que no le correspondían. Si ves cargas de una tabla con
ficheros de nombre inesperado, revisa el patrón.

```sql
-- ¿Qué nombres de fichero ha cargado históricamente este plan?
SELECT DISTINCT des_file_loaded
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_plan = :plan
  AND  dat_load_date >= CURRENT_DATE - 30
ORDER  BY 1;
```

Un nombre que no encaja con el resto delata un patrón demasiado permisivo.

## Acción

1. Confirma con los tres pasos de arriba antes de tocar datos.
2. Retira del directorio de trabajo el fichero sobrante para que no vuelva a entrar.
3. Limpia por `cod_load_trace`, nunca por criterios de negocio. Ver [R2_07_limpiar_sin_romper](../R2%20-%20Duplicados/R2_07_limpiar_sin_romper.md).
4. Si el origen reenvía de forma sistemática, escala: la limpieza diaria no es una solución.

## Ver también

[D13_cargo_dos_veces](../D%20-%20Carga%20STG/D13_cargo_dos_veces.md) · [R2_03_dentro_o_entre_cargas](../R2%20-%20Duplicados/R2_03_dentro_o_entre_cargas.md) · [D08_gpg_historificacion](../D%20-%20Carga%20STG/D08_gpg_historificacion.md) · [D02_lookup_stg_formato](../D%20-%20Carga%20STG/D02_lookup_stg_formato.md)

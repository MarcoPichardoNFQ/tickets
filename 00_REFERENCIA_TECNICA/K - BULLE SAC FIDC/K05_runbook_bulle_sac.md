---
titulo: "K05 — Incidencias de BULLE, SAC y FIDC"
familia: K
etapa: "Carga STG"
tipo: Runbook
tags:
  - familia/K
  - etapa/carga-stg
  - tipo/runbook
keywords: "BULLE, SAC, FIDC, incidencia, sin control de flag, diagnóstico"
---

# K05 — Incidencias de BULLE, SAC y FIDC

**Etapa:** Carga STG
**Tipo:** Runbook
**Palabras clave:** BULLE, SAC, FIDC, incidencia, sin control de flag, diagnóstico

## En una línea

Mismo diagnóstico que el flujo principal **a partir de la carga**, pero sin control de recepción: la
traza es la única señal.

## Lo primero: identificar el dominio

| Señal | Dominio |
|---|---|
| Tabla `BUL_*`, fichero `S3_*.csv`, separador `;` | BULLE |
| Tabla `SAC_*`, fichero `_SAC_*.txt`, separador `!` | SAC |
| Ficheros de control `FIDC_*` o `KYC_*` | FIDC / KYC |

```bash
grep -i "<TABLA>" /nfq/data/cfg/lookup_stg.txt
```

## Qué NO aplica

**Las familias `B` (flags) y `C` (conversión) no valen aquí.** Estos ficheros llegan ya planos y no
los declara ningún flag.

Consecuencia directa: **`controlflag_interfaces` no sabe nada de ellos**. La pregunta «¿llegó todo
hoy?» no tiene respuesta por la vía habitual.

## Qué SÍ aplica

Todo lo demás: carga (`D`), validaciones y descartes (`E`, `R1`), duplicados (`R2`) y
transformación vía `load_*` (`F`).

## El diagnóstico

### 1. ¿Llegó y se cargó?

```sql
SELECT cod_load_plan, cod_load_trace, dat_load_date, des_file_loaded,
       amt_register_process, cod_status, des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  des_file_loaded ILIKE '%<patrón>%'
ORDER  BY dat_load_date DESC LIMIT 10;
```

### 2. ¿Es habitual que llegue hoy?

Sin control de flag, **el histórico es la única referencia**:

```sql
SELECT dat_load_date::date AS dia, count(*), sum(amt_register_process) AS filas
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_plan = :plan AND dat_load_date > CURRENT_DATE - 45
GROUP  BY 1 ORDER BY 1 DESC;
```

Huecos regulares = periodicidad, no incidencia.

### 3. ¿Está el fichero esperando?

```bash
. /nfq/data/cfg/env.properties
grep '|<id>|' /nfq/data/cfg/lookup_stg.txt | cut -d'|' -f4
ls -la $raiz | grep -i "<parte_del_patrón>"
```

### 4. ¿Se descartó?

```sql
SELECT des_validate, des_column_name, count(*)
FROM   stg_s3.aud_load_valid_trace_t
WHERE  des_table_name = UPPER('<TABLA>_TMP') AND dat_load_date::date = CURRENT_DATE
GROUP  BY 1,2 ORDER BY 3 DESC;
```

## La incidencia más frecuente: separador dentro del dato

**Ninguno de estos dominios tiene protección de separador.** Los ficheros no pasan por el conversor,
así que no reciben la sustitución `sed 's/!/¡/g'` que protege al flujo XML.

- BULLE usa `;` — un punto y coma en una descripción rompe la línea
- SAC usa `!` — igual, y sin la sustitución que sí tiene el flujo principal

```bash
awk -F';' '{print NF}' <FICHERO>.csv | sort | uniq -c     # BULLE
awk -F'!' '{print NF}' <FICHERO>.txt | sort | uniq -c     # SAC
```

Más de un número distinto = hay líneas con campos de más.
Ver [C11_separador_dentro_del_dato](../C%20-%20Conversion%20Java/C11_separador_dentro_del_dato.md) y [D09_error_numero_columnas](../D%20-%20Carga%20STG/D09_error_numero_columnas.md).

## La confusión de nombres en SAC

`SAC_*` existe **a los dos lados**: en `stg_s3` como entrada y en `trf_s3` como salida de mapeo
(209 tablas). Ante «la tabla SAC no tiene datos», aclara primero de qué lado.
Ver [K03_interfaces_sac](../K%20-%20BULLE%20SAC%20FIDC/K03_interfaces_sac.md).

## Qué llevar al escalado

Lo mismo que en el flujo principal, más una aclaración que aquí hace falta: **decir explícitamente
que es un dominio sin control de flag**, para que quien reciba el ticket no pida el `id_camda` ni el
estado de `recebido`, que no existen.

- Dominio (BULLE / SAC / FIDC / KYC) y tabla
- `cod_load_plan` y `cod_load_trace`
- Patrón de fichero esperado y qué hay en el directorio
- Histórico de llegadas de los últimos 45 días

Ver [J07_escalado](../J%20-%20Operacion/J07_escalado.md).

## Ver también

[K01_bulle_sac_fidc](../K%20-%20BULLE%20SAC%20FIDC/K01_bulle_sac_fidc.md) · [K02_interfaces_bulle](../K%20-%20BULLE%20SAC%20FIDC/K02_interfaces_bulle.md) · [K03_interfaces_sac](../K%20-%20BULLE%20SAC%20FIDC/K03_interfaces_sac.md) · [F09_load_bulle_sac_fidc](../F%20-%20Transformacion%20TRF/F09_load_bulle_sac_fidc.md) · [C11_separador_dentro_del_dato](../C%20-%20Conversion%20Java/C11_separador_dentro_del_dato.md)

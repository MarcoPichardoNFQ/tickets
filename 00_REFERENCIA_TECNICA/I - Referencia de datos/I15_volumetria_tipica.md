---
titulo: "I15 — Volumetría típica por carga"
familia: I
etapa: "Carga STG"
tipo: Referencia
tags:
  - familia/I
  - etapa/carga-stg
  - tipo/referencia
keywords: "volumetría, volumen, filas, línea base, anomalía, amt_register_process"
---

# I15 — Volumetría típica por carga

**Etapa:** Carga STG
**Tipo:** Referencia
**Palabras clave:** volumetría, volumen, filas, línea base, anomalía, amt_register_process

## En una línea

El volumen varía tanto entre cargas de la misma interfaz que **para casi todas es inútil como
indicador de anomalía** — y las dos excepciones son precisamente las que sí conviene vigilar.

## La foto de 30 días

Medido sobre 76 planes de carga con actividad:

| | |
|---|---|
| Cargas en 30 días | **79.296** — una media de 1.043 por plan |
| Plan más frecuente | `511`, con 4.363 cargas: **145 al día** |
| Mayor volumen medio | `145`, con 58.601 filas por carga |
| Mayor carga puntual | `293`, con **211.784** filas |

La frecuencia va de **1 carga al mes a 145 al día**. No hay una cadencia común: cada interfaz tiene
la suya.

## ⚠ Por qué el volumen casi nunca sirve como alarma

En **la inmensa mayoría de los planes, el mínimo de 30 días es 1 fila**. Es decir: casi todas las
interfaces han tenido, en algún momento del último mes, una carga de una sola fila — y fue normal.

Y en 20 de los 76 planes, **el máximo supera en más de 50 veces a la media**:

```
106 · 153 · 181 · 427 · 428 · 432 · 434 · 435 · 445 · 446
450 · 451 · 452 · 509 · 525 · 548 · 569 · 571 · 580 · 588
```

Ejemplos extremos: el plan `153` tiene media de 2.271 filas y máximo de 186.867 — **82 veces la
media**. El `427`, media de 11 y máximo de 1.647 — 150 veces.

**Consecuencia operativa: "hoy vinieron pocas filas" no es, por sí solo, una incidencia.** Ni
"vinieron muchísimas". El rango normal de estas interfaces abarca casi todo.

Esto explica también por qué la validación de variación de volumen no aporta nada aunque se
arreglara: con una tolerancia de porcentaje fijo, saltaría constantemente. Ver
[R1_07_descarte_variacion_volumen](../R1%20-%20Descartes/R1_07_descarte_variacion_volumen.md).

## Las dos excepciones: los planes 511 y 512

Son los únicos donde mínimo y máximo casi coinciden, y por tanto **los únicos donde una desviación
significa algo de verdad**:

| Plan | Cargas/30d | Media | Mínimo | Máximo | Amplitud |
|---|---|---|---|---|---|
| `511` | 4.363 | 527 | 517 | 550 | ±3 % |
| `512` | 4.363 | 27.428 | 26.594 | 28.876 | ±4 % |

Ambos con 4.363 cargas en 30 días — se ejecutan juntos, 145 veces al día.

**Si alguno de estos dos se sale de su rango, es una anomalía real.** Son los dos únicos casos donde
merece la pena un control de volumen automático.

```sql
SELECT cod_load_plan, dat_load_date, amt_register_process
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_plan IN (511, 512)
  AND  dat_load_date >= CURRENT_DATE - 2
  AND  amt_register_process IS NOT NULL
ORDER  BY dat_load_date DESC;
```

Fuera de `511` entre 517-550 o de `512` entre 26.594-28.876, mira qué pasó.

Otros dos con amplitud contenida, aunque de frecuencia baja: `482` (27 cargas, 69-679) y `483`
(27 cargas, 138-1358).

## Cómo usar esto en una incidencia

**No compares contra la media.** Compara la carga de hoy contra **las cargas recientes de ese mismo
plan**, que es lo único que da contexto:

```sql
SELECT dat_load_date, des_file_loaded, amt_register_process
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_plan = :plan
  AND  amt_register_process IS NOT NULL
ORDER  BY dat_load_date DESC
LIMIT  20;
```

Y para tener la línea base de cualquier plan al día:

```sql
SELECT cod_load_plan,
       count(*)                          AS cargas_30d,
       round(avg(amt_register_process))  AS media,
       min(amt_register_process)         AS minimo,
       max(amt_register_process)         AS maximo,
       round(stddev(amt_register_process)) AS desviacion
FROM   stg_s3.aud_load_trace_t
WHERE  amt_register_process IS NOT NULL
  AND  dat_load_date > CURRENT_DATE - 30
GROUP  BY 1
ORDER  BY 1;
```

La columna de desviación añade lo que faltaba: un plan con desviación baja respecto a su media es
vigilable; uno con desviación alta, no.

## Lo que sí es señal, aunque el volumen no lo sea

- **Cero filas donde siempre hay algo**, comprobado contra los últimos 20 días de ese plan
- **El fichero pesa mucho menos de lo normal** — se ve antes de cargar, en `tamanho_interfaz`. Ver [R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md)
- **Sube el número de descartes** manteniéndose el volumen: entran las mismas filas y se apartan más

Esa tercera es la más fiable de las tres, y no depende del volumen en absoluto.

## Ver también

[R1_07_descarte_variacion_volumen](../R1%20-%20Descartes/R1_07_descarte_variacion_volumen.md) · [R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md) · [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md) · [R1_11_consultas_descartes](../R1%20-%20Descartes/R1_11_consultas_descartes.md)

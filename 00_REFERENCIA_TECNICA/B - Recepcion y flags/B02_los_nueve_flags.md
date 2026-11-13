---
titulo: "B02 — Los 9 flags del catálogo"
familia: B
etapa: "Recepción de flags"
tipo: Referencia
tags:
  - familia/B
  - etapa/recepcion-de-flags
  - tipo/referencia
keywords: "lookupflags, MEGAACCOUNTING, MEGACUSTODY, MEGARAFA, IntraDay, EndOfDay, EndOfWeek, EndOfMonth"
---

# B02 — Los 9 flags del catálogo

**Etapa:** Recepción de flags
**Tipo:** Referencia
**Palabras clave:** lookupflags, MEGAACCOUNTING, MEGACUSTODY, MEGARAFA, IntraDay, EndOfDay, EndOfWeek, EndOfMonth

## En una línea

Nueve flags, tres familias de origen y cuatro periodicidades; saber cuál falta te dice qué parte
del negocio se queda sin datos.

## El catálogo

`/nfq/data/cfg/lookupflags.txt`, formato `|id|directorio|nombre_flag|`:

| id | Flag | Familia | Periodicidad |
|---|---|---|---|
| 1 | `MEGAACCOUNTING_EndOfWeek` | Contabilidad | Semanal |
| 2 | `MEGAACCOUNTING_IntraDay` | Contabilidad | Intradía |
| 3 | `MEGAACCOUNTING_EndOfDay` | Contabilidad | Diaria |
| 4 | `MEGAACCOUNTING_EndOfMonth` | Contabilidad | Mensual |
| 5 | `MEGACUSTODY_IntraDay` | Custodia | Intradía |
| 6 | `MEGACUSTODY_EndOfDay` | Custodia | Diaria |
| 7 | `MEGARAFA_IntraDay` | RAFA | Intradía |
| 8 | `MEGARAFA_EndOfMonth` | RAFA | Mensual |
| 9 | `MEGACUSTODY_EndOfWeek` | Custodia | Semanal |

Todos comparten el mismo directorio de llegada:

```
/prdmegara/PRD/Devices/MegaCommon/innotech/
```

## Las tres familias

**MEGAACCOUNTING** — contabilidad. Es la única familia con las cuatro periodicidades.

**MEGACUSTODY** — custodia. Intradía, fin de día y fin de semana. No tiene fin de mes.

**MEGARAFA** — sólo intradía y fin de mes. La familia más pequeña, y por eso la que más
desconcierta cuando no llega: es normal que esté ausente casi todos los días.

## Qué esperar cada día

Esto es lo que evita la mitad de los falsos positivos:

| Cuándo | Flags esperables |
|---|---|
| Día hábil normal | Los `IntraDay` (2, 5, 7) y los `EndOfDay` (3, 6) |
| Fin de semana operativo | Además los `EndOfWeek` (1, 9) |
| Fin de mes | Además los `EndOfMonth` (4, 8) |

Un `MEGAACCOUNTING_EndOfMonth` ausente un martes 12 no es una incidencia.
Un `MEGACUSTODY_EndOfDay` ausente un miércoles sí lo es.

## Los jobs de Rundeck asociados

Hay un job por flag, con el mismo nombre:

`Flag_MEGAACCOUNTING_EndOfDay`, `Flag_MEGAACCOUNTING_EndOfMonth`,
`Flag_MEGAACCOUNTING_EndOfWeek`, `Flag_MEGAACCOUNTING_IntraDay`,
`Flag_MEGACUSTODY_EndOfWeek`, `Flag_MEGACUSTODY_IntraDay`.

Ninguno tiene horario propio: los invoca el vigilante de presencia. Ver [B04_job_validacion_constante](../B%20-%20Recepcion%20y%20flags/B04_job_validacion_constante.md).

**Ojo:** en los exports disponibles hay 6 jobs `Flag_*` para 9 flags del catálogo. Faltan
`MEGACUSTODY_EndOfDay`, `MEGARAFA_IntraDay` y `MEGARAFA_EndOfMonth`. Puede ser que se gestionen por
otra vía o que el export esté incompleto; conviene confirmarlo en Rundeck antes de dar por hecho
que un flag tiene job propio.

## Cómo verificarlo

```bash
cat /nfq/data/cfg/lookupflags.txt

# Flags recibidos hoy
ls -lat /prdmegara/PRD/Devices/MegaCommon/innotech/Flags/ | head -20
```

```sql
-- Últimas llegadas por tipo de flag
SELECT nome_base,
       max(data_recebemento) AS ultima_llegada,
       count(*)              AS veces
FROM   stg_s3.controlflag_arquivos
WHERE  data > CURRENT_DATE - 30
GROUP  BY 1
ORDER  BY 2 DESC NULLS LAST;
```

Esa consulta es la mejor forma de aprender la periodicidad real de cada flag en tu entorno, que
manda sobre cualquier tabla teórica.

## Ver también

[B01_que_es_un_flag](../B%20-%20Recepcion%20y%20flags/B01_que_es_un_flag.md) · [B04_job_validacion_constante](../B%20-%20Recepcion%20y%20flags/B04_job_validacion_constante.md) · [R4_01_que_es_un_set_completo](../R4%20-%20Sets%20incompletos/R4_01_que_es_un_set_completo.md) · [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md)

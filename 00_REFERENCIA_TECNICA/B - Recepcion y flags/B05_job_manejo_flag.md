---
titulo: "B05 — `Manejo Flag` y los jobs `Flag_*`"
familia: B
etapa: "Recepción de flags"
tipo: Referencia
tags:
  - familia/B
  - etapa/recepcion-de-flags
  - tipo/referencia
keywords: "Manejo Flag, Flag_MEGAACCOUNTING, jobref, encadenamiento, LlamadaTablaControlArquivosFlag"
---

# B05 — `Manejo Flag` y los jobs `Flag_*`

**Etapa:** Recepción de flags
**Tipo:** Referencia
**Palabras clave:** Manejo Flag, Flag_MEGAACCOUNTING, jobref, encadenamiento, LlamadaTablaControlArquivosFlag

## En una línea

`Manejo Flag` decide qué flag se ha recibido y llama al job específico de ese flag, que a su vez
ejecuta el script de registro.

## La cadena

```
Validacion constante presencia archivos flag
  └── Manejo Flag
        ├── LlamadaTablaControlArquivosFlag     ← abre el lote en la tabla de control
        └── Flag_<NOMBRE_DEL_FLAG>              ← uno por cada flag
              └── load_filesflag_script.sh <id>
```

Ninguno de estos jobs tiene horario propio. Todos se ejecutan porque otro los llama, mediante
referencias de job (`<jobref>`) dentro del flujo. Que aparezcan «sin programar» en Rundeck es
normal y no significa que estén desactivados. Ver [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md).

## `LlamadaTablaControlArquivosFlag`

Es el paso que abre el lote: registra la llegada en `stg_s3.controlflag_arquivos` y hace avanzar la
secuencia `exp_s3.controlflag_arquivos_cod_id_seq`, que es la que define el `id_camda` del lote.
Ver [B08_id_camda_lote](../B%20-%20Recepcion%20y%20flags/B08_id_camda_lote.md).

Si este paso falla, todo lo que viene detrás escribe con un `id_camda` equivocado —el del lote
anterior— y las interfaces del lote nuevo se mezclan con las del viejo. Síntoma: un lote con el
doble de interfaces declaradas de lo normal.

## Los jobs `Flag_*`

Uno por flag, con el nombre del flag: `Flag_MEGAACCOUNTING_EndOfDay`,
`Flag_MEGACUSTODY_IntraDay`, etc. Cada uno invoca `load_filesflag_script.sh` con el identificador
que corresponde a su flag en `lookupflags.txt`.

Su trabajo real está descrito en [B06_load_filesflag_script](../B%20-%20Recepcion%20y%20flags/B06_load_filesflag_script.md): registrar qué se declaró, comprobar
qué llegó de verdad y disparar la conversión de lo que esté presente.

### Cobertura incompleta en los exports

En los exports disponibles hay **6 jobs `Flag_*` para los 9 flags** del catálogo:

| Existe job | Flag |
|---|---|
| Sí | `MEGAACCOUNTING_EndOfDay`, `EndOfMonth`, `EndOfWeek`, `IntraDay` |
| Sí | `MEGACUSTODY_EndOfWeek`, `IntraDay` |
| **No aparece** | `MEGACUSTODY_EndOfDay` |
| **No aparece** | `MEGARAFA_IntraDay`, `MEGARAFA_EndOfMonth` |

Puede tratarse de un export parcial o de que esos tres se gestionen por otra ruta. Antes de
concluir que un flag «no tiene job», compruébalo en la consola de Rundeck. Si de verdad falta,
explica por qué esos flags no producirían registro alguno al llegar.

## `JobsArchivosFlag`

Job programado cada 10 minutos en el minuto :04. Contiene, entre otros pasos, la recarga de Qlik y
la validación de descartes. Es la contraparte de cierre del ciclo de flags. Ver [H08_recarga_qlik](../H%20-%20Cierre%20y%20Qlik/H08_recarga_qlik.md).

## Cómo verificarlo

En Rundeck: abre `Manejo Flag` y revisa sus referencias de job para ver la cadena real de tu
entorno, que manda sobre cualquier documentación.

```sql
-- ¿Se abrió lote nuevo con la última llegada?
SELECT id_camda, id, nome_base, nome_completo, data, data_recebemento
FROM   stg_s3.controlflag_arquivos
ORDER  BY id DESC LIMIT 10;
```

```sql
-- Valor actual de la secuencia que define el lote
SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq;
```

## Ver también

[B04_job_validacion_constante](../B%20-%20Recepcion%20y%20flags/B04_job_validacion_constante.md) · [B06_load_filesflag_script](../B%20-%20Recepcion%20y%20flags/B06_load_filesflag_script.md) · [B08_id_camda_lote](../B%20-%20Recepcion%20y%20flags/B08_id_camda_lote.md) · [B02_los_nueve_flags](../B%20-%20Recepcion%20y%20flags/B02_los_nueve_flags.md)

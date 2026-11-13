---
titulo: "R4.06 — Llegaron XMLs pero no el flag"
familia: R4
etapa: "Recepción de flags"
tipo: Runbook
tags:
  - familia/R4
  - etapa/recepcion-de-flags
  - tipo/runbook
keywords: "sin flag, XML huérfano, no se procesa, 120 segundos, esperando"
---

# R4.06 — Llegaron XMLs pero no el flag

**Etapa:** Recepción de flags
**Tipo:** Runbook
**Palabras clave:** sin flag, XML huérfano, no se procesa, 120 segundos, esperando

## Síntoma

Hay ficheros XML de datos en el directorio de llegada y no pasa nada con ellos.

## Por qué no pasa nada

**Sin flag no hay proceso.** El flag es lo que dispara todo: sin él, nadie recorre el directorio,
nadie registra interfaces y nadie lanza conversiones. Los XML se quedan ahí indefinidamente.

No hay ningún mecanismo que procese ficheros por su cuenta al detectarlos. La única vía de entrada
es que un flag los declare.

## Qué mirar primero

```bash
. /nfq/data/cfg/env.properties
D=/prdmegara/PRD/Devices/MegaCommon/innotech

echo "--- XML de datos esperando ---"
ls -lat $D/*.xml 2>/dev/null | head -20

echo "--- Flags procesados recientemente ---"
ls -lat $D/Flags/ | head -10
```

```sql
-- ¿Cuándo se registró el último flag de cada tipo?
SELECT nome_base, max(data_recebemento) AS ultima, max(id_camda) AS ultimo_lote
FROM   stg_s3.controlflag_arquivos
GROUP  BY 1
ORDER  BY 2 DESC NULLS LAST;
```

Compara la hora de los XML con la del último flag. XML más recientes que el último flag = están
esperando a que llegue el suyo.

## Causas probables, por orden

1. **El flag aún no ha llegado.** El origen manda primero los datos y después el flag que los
   declara. **Esto es lo normal**: unos minutos de XML sin flag no son una incidencia.
2. **El flag no se generó** en origen, aunque los datos sí. Incidencia en el emisor.
3. **El flag llegó y falló su procesamiento.** Mira si está en `Flags/` —entonces se procesó— o si
   sigue en el directorio raíz —entonces no.
4. **El flag llegó con nombre inesperado** y el `find` no lo encuentra. La búsqueda es
   `find -name "<nombre_del_lookup>*.xml"`, así que el nombre debe empezar exactamente igual que el
   valor de `lookupflags.txt`.
5. **El vigilante de presencia está caído.** Si el job que sondea cada 3 segundos no corre, nada se
   detecta. Ver [B04_job_validacion_constante](../B%20-%20Recepcion%20y%20flags/B04_job_validacion_constante.md).

## Cómo distinguir el caso 3 del caso 1

```bash
# ¿Hay un fichero de flag en el directorio raíz, sin procesar?
ls -la /prdmegara/PRD/Devices/MegaCommon/innotech/ | grep -iE "MEGAACCOUNTING|MEGACUSTODY|MEGARAFA"
```

Un flag en el directorio raíz de hace más de dos minutos es un flag que **no se está procesando**:
el script espera 120 segundos y luego se rinde. Revisa el log del job correspondiente en Rundeck.

## Acción

| Situación | Qué hacer |
|---|---|
| XML recientes, flag aún en camino | Nada. Esperar |
| Flag sin procesar en el directorio | Revisar el log del job `Flag_*` y el vigilante |
| Flag ausente y datos de hace horas | Reclamar el flag al origen |
| Nombre de flag inesperado | Comparar contra `lookupflags.txt` |
| Vigilante caído | Restaurar el job. Es la causa más grave: nada del sistema avanza |

## Lo que NO hay que hacer

**No inventes un flag.** Crear a mano un fichero de flag para desatascar el proceso hace que el
sistema registre como recibidas interfaces que nadie ha declarado, y contamina el control de
completitud del lote y todas las validaciones de cierre que dependen de él.

Si hay que forzar el procesamiento, es una decisión de escalado, no una acción de rutina.
Ver [R4_09_esperar_forzar_escalar](../R4%20-%20Sets%20incompletos/R4_09_esperar_forzar_escalar.md).

## Cuándo escalar

- Si el flag no llega y los datos son de hace horas: hay que reclamarlo al origen.
- Si el vigilante de presencia no está ejecutándose: es una parada total del sistema.

## Ver también

[R4_05_flag_sin_xml](../R4%20-%20Sets%20incompletos/R4_05_flag_sin_xml.md) · [B04_job_validacion_constante](../B%20-%20Recepcion%20y%20flags/B04_job_validacion_constante.md) · [B02_los_nueve_flags](../B%20-%20Recepcion%20y%20flags/B02_los_nueve_flags.md) · [R4_09_esperar_forzar_escalar](../R4%20-%20Sets%20incompletos/R4_09_esperar_forzar_escalar.md)

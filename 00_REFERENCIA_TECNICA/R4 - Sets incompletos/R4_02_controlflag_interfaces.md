---
titulo: "R4.02 — `controlflag_interfaces`: la fuente de verdad"
familia: R4
etapa: "Recepción de flags"
tipo: Runbook
tags:
  - familia/R4
  - etapa/recepcion-de-flags
  - tipo/runbook
keywords: "recebido, track_status, fuente de verdad, qué falta, lote, consulta principal"
---

# R4.02 — `controlflag_interfaces`: la fuente de verdad

**Etapa:** Recepción de flags
**Tipo:** Runbook
**Palabras clave:** recebido, track_status, fuente de verdad, qué falta, lote, consulta principal

## En una línea

Una sola consulta responde «¿llegó todo lo que debía llegar?», y es la primera que hay que lanzar
ante cualquier sospecha de set incompleto.

## La consulta principal

```sql
SELECT nome_interface_base,
       nome_interface_completo,
       recebido,
       track_status,
       data_recebemento
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
  AND  (NOT recebido OR NOT track_status)
ORDER  BY recebido, nome_interface_base;
```

Devuelve exactamente lo que tiene algún problema en el lote actual. Si no devuelve filas, el set
está completo según el flag.

## Cómo leer el resultado

| `recebido` | `track_status` | Qué significa | Qué hacer |
|---|---|---|---|
| `false` | `true` | El origen dice que lo mandó y **no está en disco** | Reclamar el fichero al origen |
| `true` | `false` | Llegó, pero **el origen avisa de un problema** en su extracción | Comprobar el contenido antes de fiarse |
| `false` | `false` | Ni llegó ni el origen dice que fuera bien | Fallo en origen, confirmado por ambas vías |
| `NULL` | cualquiera | El script no completó la fila | Revisar el log del job de flags |

El primer caso es el «set incompleto» clásico. El segundo se pasa por alto con frecuencia porque el
fichero **sí está** y todo parece normal: el dato puede estar truncado o incompleto sin que nada
más lo detecte.

## Comprobación complementaria: el tamaño

La tabla gemela registra el tamaño en bytes. Un fichero presente pero anormalmente pequeño es un
envío truncado, y ninguna otra comprobación lo va a detectar:

```sql
SELECT nome_interface_base,
       tamanho_interfaz::bigint AS bytes,
       data_recebemento
FROM   trf_s3.tmp_controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
ORDER  BY tamanho_interfaz::bigint NULLS FIRST
LIMIT  20;
```

Y comparado con su propia historia, que es lo que de verdad detecta la anomalía:

```sql
SELECT nome_interface_base,
       id_camda,
       tamanho_interfaz::bigint AS bytes
FROM   trf_s3.tmp_controlflag_interfaces
WHERE  nome_interface_base = '<INTERFAZ>'
ORDER  BY id_camda DESC
LIMIT  15;
```

Una caída de 8 MB a 300 bytes es una incidencia aunque `recebido` sea `true`.

## Antes de dar el diagnóstico por bueno

**Fija el `id_camda`.** Si llega otro flag mientras investigas, `last_value` cambia y estarás
mirando otro lote:

```sql
SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq;   -- anótalo y úsalo literal
```

**Comprueba que el lote es el que crees.** Un lote con muchas más interfaces de lo normal indica
que dos llegadas se mezclaron. Ver [B08_id_camda_lote](../B%20-%20Recepcion%20y%20flags/B08_id_camda_lote.md).

**Recuerda las cuatro exclusiones.** `Option`, `PricingRuleProfile`, `PricingRule` y `OTCSwap`
quedan fuera del control automático. Ver [R4_01_que_es_un_set_completo](../R4%20-%20Sets%20incompletos/R4_01_que_es_un_set_completo.md).

## Y si el fichero sí está pero la tabla dice que no

Ocurre cuando el fichero llegó **después** de que el script lo comprobara. El script mira una vez,
en el momento de procesar el flag; si el dato llegó cinco minutos tarde, la tabla se quedó con la
foto antigua.

```bash
. /nfq/data/cfg/env.properties
ls -la /prdmegara/PRD/Devices/MegaCommon/innotech/ | grep -i "<INTERFAZ>"
```

Si el fichero está ahí con hora posterior a la del flag, es un caso de llegada tardía y no de
fichero perdido. Ver [R4_08_fuera_de_ventana](../R4%20-%20Sets%20incompletos/R4_08_fuera_de_ventana.md).

## Ver también

[R4_01_que_es_un_set_completo](../R4%20-%20Sets%20incompletos/R4_01_que_es_un_set_completo.md) · [R4_05_flag_sin_xml](../R4%20-%20Sets%20incompletos/R4_05_flag_sin_xml.md) · [R4_10_consultas_que_falta](../R4%20-%20Sets%20incompletos/R4_10_consultas_que_falta.md) · [B07_tablas_controlflag](../B%20-%20Recepcion%20y%20flags/B07_tablas_controlflag.md) · [B08_id_camda_lote](../B%20-%20Recepcion%20y%20flags/B08_id_camda_lote.md)

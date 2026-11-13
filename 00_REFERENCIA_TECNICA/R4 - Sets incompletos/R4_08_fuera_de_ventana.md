---
titulo: "R4.08 — El fichero llegó tarde, fuera de ventana"
familia: R4
etapa: "Recepción de flags"
tipo: Runbook
tags:
  - familia/R4
  - etapa/recepcion-de-flags
  - tipo/runbook
keywords: "llegada tardía, fuera de ventana, recebido false pero existe, 120 segundos, foto"
---

# R4.08 — El fichero llegó tarde, fuera de ventana

**Etapa:** Recepción de flags
**Tipo:** Runbook
**Palabras clave:** llegada tardía, fuera de ventana, recebido false pero existe, 120 segundos, foto

## Síntoma

`controlflag_interfaces` dice `recebido = false`, pero el fichero **sí está** en el directorio.

## Por qué pasa

El control de recepción es una **foto instantánea**, no un seguimiento. El script comprueba la
presencia de cada fichero una sola vez, mientras procesa el flag. Lo que llegue después no cambia
ese registro: la fila se queda con `recebido = false` para siempre.

```bash
# Compara horas: la del flag y la del fichero
. /nfq/data/cfg/env.properties
D=/prdmegara/PRD/Devices/MegaCommon/innotech
stat -c '%y %n' $D/Flags/<FLAG>*.xml | tail -1
stat -c '%y %n' $D/<INTERFAZ>*.xml
```

Fichero con hora **posterior** al flag = llegada tardía confirmada.

## Las dos consecuencias, que son distintas

**El registro de control queda mal.** `recebido = false` cuando en realidad llegó. Eso hace que las
validaciones de cierre cuenten un problema que ya no existe, y que las alertas se disparen sin
causa. Ver [R4_03_validacion_cantidades](../R4%20-%20Sets%20incompletos/R4_03_validacion_cantidades.md).

**Pero el dato puede procesarse igual.** La carga a staging **no depende** de `controlflag_interfaces`:
el script de carga busca el fichero por su patrón en el directorio de trabajo, y si está, lo carga.
Un fichero tardío que llegó a convertirse entra en el siguiente ciclo de 10 minutos sin problema.

La pregunta entonces no es «¿se registró?» sino **«¿se convirtió?»**, porque la conversión sí la
dispara el flag:

```bash
# ¿Se convirtió? El original cifrado debería estar archivado
ls -la $processed/DIR_MEGARA/ | grep -i "<INTERFAZ>"
```

| Estado | Qué pasa |
|---|---|
| Convertido y archivado | El dato sigue su curso. Sólo el registro de control está mal |
| Sin convertir, XML todavía en llegada | **Nadie lo va a convertir**: la conversión la dispara el flag, y ese flag ya pasó |

El segundo caso es el que exige actuar.

## Acción

### Si el fichero llegó pero no se convirtió

La conversión no se relanza sola. Hay dos vías:

1. **Esperar al siguiente flag** que declare esa interfaz. Si el origen la vuelve a declarar en el
   próximo lote, se convertirá entonces. Es lo más limpio si el siguiente lote está cerca.
2. **Lanzar la conversión a mano** con el identificador de esa interfaz en `lookup_java.txt`:

```bash
grep -i "<INTERFAZ>" /nfq/data/cfg/lookup_java.txt    # obtener el id
/nfq/data/cfg/load_java_script.sh <id>
```

Comprueba antes que el fichero no se convirtió ya, o acabarás con datos duplicados.
Ver [C02_load_java_script](../C%20-%20Conversion%20Java/C02_load_java_script.md) y [R2_09_prevencion_duplicados](../R2%20-%20Duplicados/R2_09_prevencion_duplicados.md).

### Sobre el registro de control

**No lo corrijas a mano.** Cambiar `recebido` a `true` en `controlflag_interfaces` maquilla la
alerta pero destruye la única evidencia de que hubo una llegada tardía. Si la recurrencia importa
—y suele importar, porque una interfaz que llega sistemáticamente tarde es un problema de origen—,
ese registro es lo que lo demuestra:

```sql
SELECT id_camda, recebido, data_recebemento
FROM   stg_s3.controlflag_interfaces
WHERE  nome_interface_base = '<INTERFAZ>'
ORDER  BY id_camda DESC LIMIT 30;
```

Una columna `recebido` con muchos `false` en una interfaz cuyos datos siempre acaban llegando es
exactamente el patrón de la llegada tardía crónica.

## Causas probables

1. **Desfase entre la generación del flag y el envío de los datos** en origen. Estructural.
2. **Transferencia lenta** de ficheros grandes: el flag llega ligero y los datos aún viajan.
3. **Reintento del origen** tras un fallo de envío.

La primera es la más común y no se arregla desde soporte: hay que ajustar el orden en el emisor o
ampliar la espera del script, que hoy es de 120 segundos para el flag y **cero** para los datos.

## Cuándo escalar

Cuando el patrón se repite. Una llegada tardía puntual se gestiona; una interfaz que llega tarde
todos los días necesita una corrección en origen o en la ventana de espera.

## Ver también

[R4_05_flag_sin_xml](../R4%20-%20Sets%20incompletos/R4_05_flag_sin_xml.md) · [R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md) · [C02_load_java_script](../C%20-%20Conversion%20Java/C02_load_java_script.md) · [B06_load_filesflag_script](../B%20-%20Recepcion%20y%20flags/B06_load_filesflag_script.md)

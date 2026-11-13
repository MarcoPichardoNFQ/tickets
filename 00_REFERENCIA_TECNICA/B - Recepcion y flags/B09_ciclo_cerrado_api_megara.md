---
titulo: "B09 — El ciclo cerrado: Rundeck pide los ficheros a Megara"
familia: B
etapa: "Recepción de flags"
tipo: Referencia
tags:
  - familia/B
  - etapa/recepcion-de-flags
  - tipo/referencia
keywords: "API Megara, executeInnotechJobs, ciclo cerrado, ArchivoAyudaRundeckMegara, interruptor"
---

# B09 — El ciclo cerrado: Rundeck pide los ficheros a Megara

**Etapa:** Recepción de flags
**Tipo:** Referencia
**Palabras clave:** API Megara, executeInnotechJobs, ciclo cerrado, ArchivoAyudaRundeckMegara, interruptor

## En una línea

El sistema no espera pasivamente a que lleguen ficheros: cuando ha consumido el lote anterior,
**llama a la API de Megara para que genere el siguiente**.

## El bucle

```
1. Rundeck comprueba el directorio de entrada
2. ¿Está vacío de ficheros oficiales?  →  llama a la API de Megara
3. Megara genera el lote y lo deposita
4. El vigilante detecta los flags (cada 3 segundos)
5. Cuando el set MEGA* está completo, arranca la carga
6. Al terminar el ciclo, vuelta al paso 1
```

Eso explica dos cosas que de otro modo desconciertan: por qué los orquestadores se despiertan cada
10 minutos aunque no haya nada que hacer, y por qué el vigilante sondea cada 3 segundos.

## El job: `LLamada Rundeck Flags Obligatorios`

### Los dos endpoints

```
POST https://megaapps.s3caceis.com.br:9447/MegaAccounting/rest/JobExecution/executeInnotechJobs
POST https://megaapps.s3caceis.com.br:9445/MegaCustody/rest/JobExecution/executeInnotechIntraDayJob
```

Autenticación básica con el usuario `userrdkmeg@ALL`. **La contraseña está escrita en claro dentro
del propio script**, no en un fichero de credenciales.

Se ejecutan **en secuencia**: primero Accounting, después Custody.

### ⚠ El interruptor general

Antes de nada, el script lee un fichero:

```bash
ARCHIVO_AYUDA="/nfq/data/cfg/ArchivoAyudaRundeckMegara.txt"
valor_actual=$(tr -d '[:space:]' < "$ARCHIVO_AYUDA")

if [ "$valor_actual" -eq 1 ]; then
    echo "ArchivoAyudaRundeckMegara con 1, empezando ejecucion"
else
    echo "ArchivoAyudaRundeckMegara NO contiene 1 (valor: '$valor_actual'), abortando ejecucion"
    exit 0
fi
```

**Si ese fichero no contiene exactamente `1`, el script sale con éxito sin hacer nada.**

Es el interruptor manual de todo el ciclo de generación. Y sale con `exit 0`, así que **el job
aparece en verde**: nadie se entera de que el sistema dejó de pedir ficheros.

Ante «hace horas que no llega nada y no hay ningún error», ésta es la primera comprobación:

```bash
cat /nfq/data/cfg/ArchivoAyudaRundeckMegara.txt
```

Cualquier cosa que no sea `1` significa que el ciclo está parado a propósito —o por olvido.

> En la copia disponible en el repositorio, ese fichero está **vacío**. Confirma su valor real en
> producción antes de sacar conclusiones.

## La comprobación de completitud

El script lleva **una lista de ~130 prefijos obligatorios codificada en el propio código**: los 5
prefijos de flag (`MEGAACCOUNTING_EndOfDay`, `EndOfMonth`, `EndOfWeek`, `IntraDay`,
`MEGACUSTODY_IntraDay`) y ~125 nombres de interfaz, de `AccountCategory` a `YieldCurve`.

Y decide en tres direcciones:

| Situación | Qué hace |
|---|---|
| **Están todos** los prefijos | «CARGA COMPLETA», `exit 0`. **No llama a las APIs**: aún hay trabajo pendiente |
| **Hay algunos, faltan otros** | «🛑 ERROR CRÍTICO: Carga incompleta», `exit 1`. **Aborta** |
| **No hay ninguno** | «Procediendo con el flujo normal» → llama a las APIs para pedir un lote nuevo |

La lógica es la inversa de lo intuitivo: **las APIs sólo se llaman cuando el directorio está vacío**
de ficheros oficiales. Es decir, cuando el lote anterior ya se consumió entero.

El caso del medio es el que genera incidencias: un lote a medio consumir, o a medio llegar, detiene
el ciclo con error hasta que se resuelva.

## Los reintentos son muy largos

```bash
max_reintentos=30
intervalo=300     # 5 minutos
```

Hasta **31 intentos separados por 5 minutos: unas 2,5 horas por endpoint**. Y como Accounting y
Custody van en secuencia, el peor caso son **unas 5 horas** antes de que el job se dé por vencido.

Consecuencia práctica: un job de este tipo que lleve horas «en ejecución» **no está colgado**, está
reintentando contra una API que no responde. Antes de matarlo, mira su log: cada reintento deja
línea con el código HTTP recibido.

## ⚠ Un detalle a verificar

El directorio que inspecciona no es el mismo que usa el resto del sistema:

```bash
DIR_XML="/media/premegara/Devices/MegaCommon/innotech/"
```

El resto de scripts y lookups usan `/prdmegara/PRD/Devices/MegaCommon/innotech/`. Fíjate en
**`premegara` frente a `prdmegara`**, y en el `/media/` inicial.

Si esa ruta no es la correcta en producción, la comprobación de prefijos **nunca encuentra
ficheros** y el script cae siempre en la tercera rama: llamaría a las APIs en cada ejecución, sin
comprobar realmente si el lote anterior se consumió.

```bash
ls -la /media/premegara/Devices/MegaCommon/innotech/ 2>/dev/null || echo "NO EXISTE"
ls -la /prdmegara/PRD/Devices/MegaCommon/innotech/ | head
```

Merece comprobarse: determina si la comprobación de completitud está funcionando o es inerte.

## Ver también

[B04_job_validacion_constante](../B%20-%20Recepcion%20y%20flags/B04_job_validacion_constante.md) · [R4_01_que_es_un_set_completo](../R4%20-%20Sets%20incompletos/R4_01_que_es_un_set_completo.md) · [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md) · [R4_06_xml_sin_flag](../R4%20-%20Sets%20incompletos/R4_06_xml_sin_flag.md) · [A02_flujo_e2e_seis_pasos](../A%20-%20Orientacion/A02_flujo_e2e_seis_pasos.md)

---
titulo: "B03 — Ciclo de vida de un fichero, de la llegada al archivo"
familia: B
etapa: "Recepción de flags"
tipo: Referencia
tags:
  - familia/B
  - etapa/recepcion-de-flags
  - tipo/referencia
keywords: "ciclo de vida, recorrido, directorios, InLoad, Flags, DIR_PROCESSED, gpg"
---

# B03 — Ciclo de vida de un fichero, de la llegada al archivo

**Etapa:** Recepción de flags
**Tipo:** Referencia
**Palabras clave:** ciclo de vida, recorrido, directorios, InLoad, Flags, DIR_PROCESSED, gpg

## En una línea

Un fichero pasa por cuatro sitios y cambia de nombre tres veces; saber en cuál está te dice
exactamente en qué etapa se atascó.

## El recorrido

```
1. LLEGADA
   /prdmegara/PRD/Devices/MegaCommon/innotech/
   ├── MEGACUSTODY_IntraDay_*.xml     ← el flag
   └── Bond_1771431596036.xml         ← los datos

2. CONVERSIÓN  (la dispara el propio flag)
   El XML se lee, se valida contra su XSD y se convierte a texto plano
   El XML original se cifra y se archiva:
   $processed/DIR_MEGARA/Bond_1771431596036.xml.gpg

3. ESPERA DE CARGA
   Los planos generados quedan en el directorio de trabajo ($raiz)

4. CARGA
   Bond_..._InLoad.csv          ← renombrado mientras se procesa
   ↓
   $fileshare/DIR_PROCESSED/...  ← cifrado y archivado si fue bien

   El flag, por su parte, se mueve a:
   /prdmegara/PRD/Devices/MegaCommon/innotech/Flags/
```

## Qué significa encontrar un fichero en cada sitio

| Dónde está | Qué significa | ¿Normal? |
|---|---|---|
| Directorio de llegada, XML | Aún sin convertir | Sí, si acaba de llegar |
| Directorio de llegada, XML de horas atrás | La conversión no se disparó | **No** |
| `Flags/` | Flag ya procesado | Sí |
| `$processed/DIR_MEGARA/*.gpg` | XML convertido y archivado | Sí |
| `$raiz/*.csv` | Plano esperando carga | Sí, entre bloques |
| `$raiz/*_InLoad.csv` | Cargándose **ahora** | Sólo unos segundos |
| `$raiz/*_InLoad.csv` de hace horas | **Carga abortada a mitad** | **No** |
| `DIR_PROCESSED/*.gpg` | Cargado correctamente | Sí |
| `DIR_UNMATCHED/` | No casó con nada esperado | **No** |

## Los dos estados que exigen intervención

**`_InLoad` antiguo.** El proceso murió entre el renombrado y el archivado. El fichero no se
recogerá solo, porque la búsqueda excluye a propósito los `_InLoad`. Hay que devolverle el nombre
original **después de comprobar que sus datos no entraron ya**. Ver [D08_gpg_historificacion](../D%20-%20Carga%20STG/D08_gpg_historificacion.md).

**`DIR_UNMATCHED`.** Llegó algo que el sistema no supo encaminar. Ver [R4_07_dir_unmatched](../R4%20-%20Sets%20incompletos/R4_07_dir_unmatched.md).

## El renombrado del flag

Cuando el flag se archiva, si ya existe uno con el mismo nombre en `Flags/` **no se sobrescribe**:

```bash
nuevo_nombre="${nombre_archivo%.*}_$(date +%Y%m%d%H%M%S).xml"
```

Así que varios ficheros del mismo flag en `Flags/` con marca de tiempo significan varias llegadas
del mismo tipo de flag. Es información útil: te dice cuántas veces se abrió lote ese día.

## El cifrado

Todos los originales —tanto el XML de entrada como el plano cargado— acaban cifrados con GPG
usando el destinatario `bk_stored` (variable `key_cript` de `env.properties`). Para leer un fichero
archivado hay que descifrarlo:

```bash
gpg --decrypt FICHERO.xml.gpg | head -50
```

Es la forma de responder «¿qué traía exactamente el fichero de ayer?» sin depender de lo que se
cargó.

## Cómo verificarlo

```bash
. /nfq/data/cfg/env.properties

echo "--- Llegada (sin convertir) ---"
ls -lat /prdmegara/PRD/Devices/MegaCommon/innotech/*.xml 2>/dev/null | head

echo "--- Flags procesados ---"
ls -lat /prdmegara/PRD/Devices/MegaCommon/innotech/Flags/ | head

echo "--- Atascados en carga ---"
find $raiz -name "*_InLoad*" -mmin +60 -ls

echo "--- Sin encaminar ---"
ls -la $destino | head
```

## Ver también

[A04_rutas_y_directorios](../A%20-%20Orientacion/A04_rutas_y_directorios.md) · [D08_gpg_historificacion](../D%20-%20Carga%20STG/D08_gpg_historificacion.md) · [R4_07_dir_unmatched](../R4%20-%20Sets%20incompletos/R4_07_dir_unmatched.md) · [C02_load_java_script](../C%20-%20Conversion%20Java/C02_load_java_script.md)

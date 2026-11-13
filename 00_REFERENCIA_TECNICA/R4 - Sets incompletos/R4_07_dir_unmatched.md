---
titulo: "R4.07 — Ficheros en `DIR_UNMATCHED`"
familia: R4
etapa: "Carga STG"
tipo: Runbook
tags:
  - familia/R4
  - etapa/carga-stg
  - tipo/runbook
keywords: "DIR_UNMATCHED, sin encaminar, no casa, patrón, destino, acumulación"
---

# R4.07 — Ficheros en `DIR_UNMATCHED`

**Etapa:** Carga STG
**Tipo:** Runbook
**Palabras clave:** DIR_UNMATCHED, sin encaminar, no casa, patrón, destino, acumulación

## Síntoma

Se acumulan ficheros en `/prddatahub/DIR_UNMATCHED/`.

## Qué significa

Es el directorio `destino` de `env.properties`: donde acaba lo que el sistema recibió pero **no supo
encaminar**. Un fichero aquí es un fichero que llegó y que nadie va a procesar.

```bash
. /nfq/data/cfg/env.properties
echo $destino          # /prddatahub/DIR_UNMATCHED/
ls -lat $destino | head -30
```

## Qué mirar primero

```bash
# Cuántos hay y desde cuándo se acumulan
ls -1 $destino | wc -l
ls -lat $destino | tail -5      # los más antiguos

# Agrupados por prefijo, para ver el patrón
ls -1 $destino | sed 's/_[0-9]*\..*//' | sort | uniq -c | sort -rn | head
```

Esa última línea es la más útil: si todos los ficheros comparten prefijo, hay **una** interfaz mal
configurada, no un problema general.

## Causas probables, por orden

**1. El patrón del lookup no casa con el nombre real.** La causa dominante. El fichero llegó bien
pero su nombre no encaja con lo que espera `lookup_stg.txt` o `lookup_java.txt`.

```bash
# ¿Qué patrón espera cada carga?
cut -d'|' -f4 /nfq/data/cfg/lookup_stg.txt | sort | head -30
grep -i "<parte_del_nombre>" /nfq/data/cfg/lookup_stg.txt
```

**2. Interfaz nueva sin parametrizar.** El origen empezó a mandar algo que nunca se dio de alta. No
está en ningún lookup ni en `PAR_MAESTRO_TABLAS_T`, así que no hay a dónde llevarlo.

**3. Fichero de otra procedencia** depositado por error en la ruta compartida.

**4. Cambio de nomenclatura en origen** — sufijos, prefijos o timestamps con otro formato.

## Acción

### 1. Identifica a qué interfaz debería corresponder

```bash
head -3 $destino/<FICHERO>          # mira el contenido y la cabecera
```

La cabecera suele delatar la interfaz aunque el nombre no lo haga.

### 2. Comprueba si esa interfaz existe en el sistema

```bash
grep -i "<INTERFAZ>" /nfq/data/cfg/lookup_stg.txt
grep -i "<INTERFAZ>" /nfq/data/cfg/lookup_java.txt
```

```sql
SELECT * FROM stg_s3.par_maestro_tablas_t WHERE des_table ILIKE '%<INTERFAZ>%';
```

| Resultado | Diagnóstico |
|---|---|
| Existe en lookup y parametrización | Sólo falla el **patrón de nombre** |
| No existe en ninguno | **Interfaz nueva**: alta pendiente |

### 3. Decide

**Si es sólo el patrón**: el fichero es recuperable. Renombrarlo para que case es una solución
puntual válida — pero **déjalo escrito en el ticket**, porque si el origen sigue mandando con el
nombre nuevo, mañana vuelve. La corrección de fondo es actualizar el patrón del lookup, y eso es un
cambio de parametrización.

**Si es una interfaz nueva**: no se toca. Requiere alta completa —tabla, parametrización, lookup,
bloque— y eso es un proyecto, no una incidencia.

**Si es un fichero ajeno**: retirarlo y avisar a quien lo dejó ahí.

## Por qué no conviene dejar que se acumule

`DIR_UNMATCHED` no lo limpia nadie automáticamente. Un directorio con miles de ficheros de meses
hace que sea imposible distinguir lo que llegó hoy de lo que lleva ahí desde siempre, y con ello se
pierde la única señal útil que da: que algo está entrando mal **ahora**.

Comprobación de rutina que merece la pena:

```bash
find $destino -type f -mtime -1 | wc -l    # llegados en las últimas 24 h
```

Ese número debería ser cero. Cualquier otra cosa es una incidencia del día.

## Cuándo escalar

- Interfaz nueva sin dar de alta.
- Cambio de nomenclatura en origen: hay que decidir si se adapta el patrón o se corrige el emisor.
- Acumulación histórica: alguien tiene que decidir qué se hace con lo viejo.

## Ver también

[A04_rutas_y_directorios](../A%20-%20Orientacion/A04_rutas_y_directorios.md) · [D02_lookup_stg_formato](../D%20-%20Carga%20STG/D02_lookup_stg_formato.md) · [B03_ciclo_de_vida_del_fichero](../B%20-%20Recepcion%20y%20flags/B03_ciclo_de_vida_del_fichero.md) · [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md)

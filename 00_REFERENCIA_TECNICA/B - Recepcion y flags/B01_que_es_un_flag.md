---
titulo: "B01 — Qué es un archivo flag y qué dispara"
familia: B
etapa: "Recepción de flags"
tipo: Referencia
tags:
  - familia/B
  - etapa/recepcion-de-flags
  - tipo/referencia
keywords: "flag, TrackInnotech, lote, camada, disparador, XML de control"
---

# B01 — Qué es un archivo flag y qué dispara

**Etapa:** Recepción de flags
**Tipo:** Referencia
**Palabras clave:** flag, TrackInnotech, lote, camada, disparador, XML de control

## En una línea

El flag es un XML de control que llega junto a los datos y **declara qué interfaces componen el
lote**; su llegada dispara todo el ciclo.

## Detalle

### Qué contiene

No es un fichero vacío ni una marca: es un XML con un elemento por cada interfaz que el origen dice
haber enviado.

```xml
<com.vermeg.services.innotech.TrackInnotech
     innotechInterface_code="Bond"
     filename="Bond_1771431596036"
     trackStatus="Processd"
     beginExecutionTime="..."
     endExecutionTime="..." />
```

| Atributo | Significa |
|---|---|
| `innotechInterface_code` | Nombre de la interfaz |
| `filename` | Nombre del fichero de datos que debería haber llegado |
| `trackStatus` | Estado según el origen |
| `beginExecutionTime` / `endExecutionTime` | Ventana de extracción en el sistema emisor |

### Qué se hace con esa declaración

El script de flags recorre esos elementos y, **por cada uno, comprueba si el fichero declarado
existe realmente en el directorio**. El resultado se guarda en `controlflag_interfaces` con dos
booleanos:

- `recebido` — ¿está el fichero de verdad?
- `track_status` — ¿el origen dijo que fue bien?

Esa tabla es la respuesta autorizada a «¿llegó todo lo que debía llegar?». Ver [B07_tablas_controlflag](../B%20-%20Recepcion%20y%20flags/B07_tablas_controlflag.md).

### Qué dispara

Cuando un fichero declarado sí existe, el script lanza acto seguido su conversión, en segundo plano:

```bash
./load_java2_optiflag_script.sh "${code}_.xml" "$filename" &
```

Así que el flag no sólo informa: **encadena la conversión de cada fichero que encuentra**. Un flag
que llega es el arranque real del procesamiento del lote.

### El concepto de lote: `id_camda`

Cada llegada de flag abre un lote identificado por `id_camda`, tomado de la secuencia
`exp_s3.controlflag_arquivos_cod_id_seq`. Todas las filas de `controlflag_interfaces` de esa
llegada comparten ese valor. Ver [B08_id_camda_lote](../B%20-%20Recepcion%20y%20flags/B08_id_camda_lote.md).

### Dónde llegan

Directorio declarado en `lookupflags.txt`:

```
/prdmegara/PRD/Devices/MegaCommon/innotech/
```

Y una vez procesado, el flag se archiva en el subdirectorio `Flags/` de esa misma ruta. Si ya
existe uno con el mismo nombre, se le añade una marca de tiempo en vez de sobrescribirlo.

## ⚠ Un detalle que engaña

El estado del origen se traduce a booleano comparando con la cadena **`'Processd'`** — escrita así,
sin la «e»:

```sql
case when '<status>' = 'Processd' then true else false end
```

Si el origen cambiara alguna vez a `'Processed'`, bien escrito, **todas las interfaces pasarían a
`track_status = false`** y las validaciones de cierre dispararían alarmas masivas sin que nada
estuviera realmente mal. Merece la pena comprobar qué valor llega hoy:

```sql
SELECT track_status, count(*)
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
GROUP  BY 1;
```

## Cómo verificarlo

```bash
. /nfq/data/cfg/env.properties
ls -lat /prdmegara/PRD/Devices/MegaCommon/innotech/Flags/ | head -20
```

```sql
-- El lote actual y cuántas interfaces declaró
SELECT nome_flag_geral, count(*) AS declaradas,
       count(*) FILTER (WHERE recebido)     AS recibidas,
       count(*) FILTER (WHERE NOT recebido) AS faltan
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
GROUP  BY 1;
```

## Ver también

[B02_los_nueve_flags](../B%20-%20Recepcion%20y%20flags/B02_los_nueve_flags.md) · [B06_load_filesflag_script](../B%20-%20Recepcion%20y%20flags/B06_load_filesflag_script.md) · [B07_tablas_controlflag](../B%20-%20Recepcion%20y%20flags/B07_tablas_controlflag.md) · [R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md)

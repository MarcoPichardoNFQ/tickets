---
titulo: "C05 — La sustitución de `!` por `¡` en el XML original"
familia: C
etapa: "Conversión Java"
tipo: Referencia
tags:
  - familia/C
  - etapa/conversion-java
  - tipo/referencia
keywords: "sed, separador, exclamación, modificación en origen, pérdida de dato, irreversible"
---

# C05 — La sustitución de `!` por `¡` en el XML original

**Etapa:** Conversión Java
**Tipo:** Referencia
**Palabras clave:** sed, separador, exclamación, modificación en origen, pérdida de dato, irreversible

## En una línea

Antes de convertir, el script reemplaza **todos** los signos de exclamación del XML por `¡`,
modificando el fichero original en disco de forma irreversible.

## La instrucción

```bash
sed -i 's/!/¡/g' "$fileToOpen"
```

`sed -i` edita **en el sitio**: no crea copia. El XML que llegó del origen queda alterado antes de
que nadie lo lea.

## Por qué existe

El separador de los ficheros planos es `!`. El conversor **no entrecomilla ni escapa los valores**:
si un dato contiene el separador, la línea generada gana un campo y todas las columnas siguientes se
desplazan, rompiendo la carga posterior.

La sustitución previa elimina el problema de raíz: si en el XML no queda ningún `!`, ningún valor
podrá contenerlo.

Es una solución efectiva. Y tiene un precio.

## El precio

**El dato pierde el carácter, y lo pierde para siempre.**

- Un valor legítimo `URGENTE!` llega a base de datos como `URGENTE¡`.
- El XML archivado y cifrado en `DIR_MEGARA` es la versión **ya modificada**: descifrarlo no
  recupera el original.
- No queda constancia de cuántas sustituciones se hicieron ni en qué campos.

Para la mayoría de las interfaces —códigos, importes, fechas, identificadores— esto es
intrascendente. Importa en campos de texto libre: descripciones, nombres, observaciones.

## Qué significa para el diagnóstico

**Si un usuario reporta que un texto llegó con `¡` donde debía haber `!`, no es un error de
codificación ni un problema de la base de datos.** Es este `sed`, y es comportamiento previsto.

No se arregla desde soporte: cambiarlo exigiría que el conversor entrecomillara los valores o que se
usara otro separador, y eso afectaría a todas las cargas.

## Cómo comprobarlo

```sql
-- Buscar el carácter en campos de texto de una tabla
SELECT count(*) FROM stg_s3.<TABLA>_T WHERE <columna_texto> LIKE '%¡%';
```

Si aparece con frecuencia en una interfaz concreta, es que ese origen usa exclamaciones en sus
textos y conviene documentarlo como comportamiento conocido para no volver a investigarlo.

## Lo que la sustitución NO resuelve

Sólo protege contra el carácter `!`. **No todas las cargas usan ese separador.** Las interfaces
BULLE, por ejemplo, se cargan con `;`:

```bash
cut -d'|' -f6 /nfq/data/cfg/lookup_stg.txt | sort | uniq -c
```

Para las cargas con `;`, un punto y coma dentro de un dato **sigue rompiendo la línea**, porque no
hay ninguna sustitución equivalente. Es una fuente real de errores de número de columnas.
Ver [C11_separador_dentro_del_dato](../C%20-%20Conversion%20Java/C11_separador_dentro_del_dato.md) y [D09_error_numero_columnas](../D%20-%20Carga%20STG/D09_error_numero_columnas.md).

Tampoco protege contra saltos de línea dentro de un valor, aunque de eso sí se ocupa el conversor,
que los sustituye por espacio al escribir.

## Ver también

[C11_separador_dentro_del_dato](../C%20-%20Conversion%20Java/C11_separador_dentro_del_dato.md) · [C01_que_hace_xmlconversor](../C%20-%20Conversion%20Java/C01_que_hace_xmlconversor.md) · [C02_load_java_script](../C%20-%20Conversion%20Java/C02_load_java_script.md) · [D09_error_numero_columnas](../D%20-%20Carga%20STG/D09_error_numero_columnas.md) · [D02_lookup_stg_formato](../D%20-%20Carga%20STG/D02_lookup_stg_formato.md)

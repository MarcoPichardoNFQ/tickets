---
titulo: "C11 — Separador dentro de un dato: columnas desplazadas"
familia: C
etapa: "Conversión Java"
tipo: Runbook
tags:
  - familia/C
  - etapa/conversion-java
  - tipo/runbook
keywords: "separador, columnas desplazadas, extra data, punto y coma, BULLE, campos de más"
---

# C11 — Separador dentro de un dato: columnas desplazadas

**Etapa:** Conversión Java
**Tipo:** Runbook
**Palabras clave:** separador, columnas desplazadas, extra data, punto y coma, BULLE, campos de más

## Síntoma

La carga falla con `extra data after last expected column`, o —peor— no falla y aparecen descartes
masivos de formato en columnas contiguas.

## La causa

El conversor **no entrecomilla ni escapa los valores**. Si un dato contiene el carácter separador,
esa línea gana un campo y todas las columnas siguientes se desplazan una posición.

## Por qué con `!` casi nunca pasa, y con `;` sí

Para las cargas con separador `!` existe una protección: el script sustituye todos los `!` del XML
por `¡` antes de convertir.

```bash
sed -i 's/!/¡/g' "$fileToOpen"
```

**Pero no todas las cargas usan `!`.** Las interfaces BULLE se cargan con `;`, y **no hay ninguna
sustitución equivalente para el punto y coma**.

```bash
cut -d'|' -f6 /nfq/data/cfg/lookup_stg.txt | sort | uniq -c
```

Así que un `;` dentro de una descripción rompe la línea sin que nada lo impida. Ver [C05_sed_separador](../C%20-%20Conversion%20Java/C05_sed_separador.md).

## Qué mirar primero

Cuenta los campos por línea del plano:

```bash
. /nfq/data/cfg/env.properties
awk -F';' '{print NF}' <FICHERO>.csv | sort | uniq -c
```

| Resultado | Diagnóstico |
|---|---|
| Un solo número | Todas las líneas iguales: el problema no es éste |
| Varios números | **Confirmado**: hay líneas con campos de más |

Y localiza las líneas concretas:

```bash
awk -F';' -v n=<esperados> 'NF!=n {print NR": "NF" campos -> "$0}' <FICHERO>.csv | head -5
```

Leyendo esas líneas se ve enseguida qué valor contiene el separador.

## El caso silencioso, que es el peligroso

Si la línea gana un campo, el `\COPY` falla y te enteras. Pero hay una variante que **no da error**:
cuando el desplazamiento se compensa —por ejemplo, un campo que queda vacío al final— el número
total de columnas coincide y la carga entra con **los datos corridos de sitio**.

Síntoma indirecto: descartes masivos de formato o de clave foránea en **columnas contiguas** que
nunca fallaban, en unas pocas filas.

```sql
SELECT des_column_name, des_validate, count(*) AS filas
FROM   stg_s3.aud_load_valid_trace_t
WHERE  des_table_name = UPPER('<TABLA>_TMP')
  AND  dat_load_date::date = CURRENT_DATE
GROUP  BY 1,2
ORDER  BY count(*) DESC;
```

Varias columnas **vecinas** fallando en las **mismas** filas es la firma de un desplazamiento, no de
un problema de calidad de dato. Cruza con la fila concreta para confirmarlo:

```sql
SELECT v.des_row_number, t.*
FROM   stg_s3.aud_load_valid_trace_t v
JOIN   stg_s3.<TABLA>_TMP t ON t.COD_SEQ_XXX = v.des_row_number
WHERE  v.cod_load_trace = :trace
LIMIT  5;
```

Si al mirar la fila ves valores en columnas que no les corresponden —una fecha en un campo de
importe, un código donde va un nombre— es esto.

## Acción

1. Confirma con el `awk` de conteo de campos.
2. Identifica el valor que contiene el separador.
3. **Medida puntual:** corregir esa línea del plano y relanzar la carga desatasca el día. Anótalo en
   el ticket: no es una solución.
4. **Solución de fondo:** el origen no debería mandar el separador dentro de un dato, o la interfaz
   debería usar otro separador. Ambas cosas son cambios de contrato.

## Cuándo escalar

Siempre que se repita. Una línea puntual se corrige; un origen que mete separadores en campos de
texto libre lo va a seguir haciendo, y cada vez costará un ticket.

Merece escalarse también la observación de fondo: **las cargas con `;` no tienen la protección que
sí tienen las de `!`**. Es una asimetría del diseño, no un fallo puntual.

## Ver también

[C05_sed_separador](../C%20-%20Conversion%20Java/C05_sed_separador.md) · [D09_error_numero_columnas](../D%20-%20Carga%20STG/D09_error_numero_columnas.md) · [C06_ficheros_de_salida](../C%20-%20Conversion%20Java/C06_ficheros_de_salida.md) · [R1_05_descarte_formato](../R1%20-%20Descartes/R1_05_descarte_formato.md) · [D02_lookup_stg_formato](../D%20-%20Carga%20STG/D02_lookup_stg_formato.md)

---
titulo: "D02 — `lookup_stg.txt`: formato y cómo leerlo"
familia: D
etapa: "Carga STG"
tipo: Referencia
tags:
  - familia/D
  - etapa/carga-stg
  - tipo/referencia
keywords: "lookup_stg, formato, separador, patrón de fichero, ctrl, parametrización"
---

# D02 — `lookup_stg.txt`: formato y cómo leerlo

**Etapa:** Carga STG
**Tipo:** Referencia
**Palabras clave:** lookup_stg, formato, separador, patrón de fichero, ctrl, parametrización

## En una línea

Cada línea de `/nfq/data/cfg/lookup_stg.txt` define una carga: qué tabla, qué fichero, qué
separador y a dónde se archiva.

## Detalle

### Formato de línea

```
|id|TABLA_DESTINO|patrón_de_fichero|ruta_historico|separador|opciones_copy|marked.ctrl|processed.ctrl|
```

Ejemplos reales:

```
|1|BUL_RECEITA_T|S3_FIN_RECEITA*.csv|DIR_PROCESSED/DIR_BULLE/|;|CSV HEADER|BULLE_markedFiles.ctrl|BULLE_processedFiles.ctrl|
|5|SAC_CAIXA_MT_T|_MT_CAIXA.txt|DIR_PROCESSED/DIR_SAC/|!|CSV HEADER|SACCAIXA_markedFiles.ctrl|SACCAIXA_processedFiles.ctrl|
```

| Campo | Contenido | Cómo lo usa el script |
|---|---|---|
| 2 | **id** | Es el `cod_load_plan`. Se pasa a `RUN_LOAD_PLAN_PC` |
| 3 | **Tabla destino** | Sin sufijo. El script le añade `_TMP` |
| 4 | **Patrón de fichero** | Admite comodín `*`. Se busca en el directorio `$raiz` |
| 5 | **Ruta de histórico** | Relativa a `$fileshare`. Ahí va el fichero cifrado |
| 6 | **Separador** | `;`, `!`, `\|`… varía por familia de interfaz |
| 7 | **Opciones de `\COPY`** | Normalmente `CSV HEADER` |
| 8-9 | **Ficheros de control** | `*_markedFiles.ctrl` y `*_processedFiles.ctrl` |

El fichero tiene **573 líneas**: una por cada carga parametrizada.

### El separador no es único

Éste es un detalle que despista. Conviven al menos dos:

- **`;`** en las interfaces BULLE (`BUL_*`)
- **`!`** en las interfaces SAC (`SAC_*`) y en la salida del conversor Java

Si diagnosticas un problema de columnas, comprueba primero **qué separador espera esa carga
concreta**, no asumas el general del sistema.

### Cómo el script lee la línea

```bash
cadena=`grep '|'$valor'|' $lookup_stg | tr -d '\n'`
cod_tab=`echo $cadena | cut -d '|' -f 2`
nom_tab=`echo $cadena | cut -d '|' -f 3`
fichero=`echo $cadena | cut -d '|' -f 4`
ruta_hist=`echo $cadena | cut -d '|' -f 5`
sep=`echo $cadena | cut -d '|' -f 6`
cabe=`echo $cadena | cut -d '|' -f 7`
```

### ⚠ El `grep` puede coger la línea equivocada

La búsqueda es `grep '|<id>|'` sobre el fichero entero. Si un `id` aparece como subcadena en otro
sitio del fichero delimitado por barras, el `grep` devuelve **varias líneas**, y el `tr -d '\n'`
las concatena en una sola cadena. El resultado es un `cut` que mezcla campos de dos cargas
distintas.

Síntoma típico: una carga apunta a una tabla o a un separador que no le corresponden.
Comprobación:

```bash
grep -c '|5|' /nfq/data/cfg/lookup_stg.txt   # debería devolver 1
```

## Cómo verificarlo

```bash
# Ver la definición de una carga concreta
grep '|17|' /nfq/data/cfg/lookup_stg.txt

# Todas las cargas de una familia
grep 'SAC_' /nfq/data/cfg/lookup_stg.txt

# Separadores en uso
cut -d'|' -f6 /nfq/data/cfg/lookup_stg.txt | sort | uniq -c
```

Y el contraste con la base de datos:

```sql
SELECT cod_load_plan, des_procedure_run, des_separator,
       amt_num_columns, des_source_dir, des_destiny_dir, valid_err_des
FROM   stg_s3.par_load_plan_t
WHERE  cod_load_plan = :id;
```

Si el separador del lookup y el de `PAR_LOAD_PLAN_T` no coinciden, tienes una desalineación de
parametrización.

## Ver también

[D03_script_stg_trf](../D%20-%20Carga%20STG/D03_script_stg_trf.md) · [D01_mecanica_carga_copy](../D%20-%20Carga%20STG/D01_mecanica_carga_copy.md) · [E02_par_load_plan_t](../E%20-%20Parametrizacion/E02_par_load_plan_t.md) · [D09_error_numero_columnas](../D%20-%20Carga%20STG/D09_error_numero_columnas.md)

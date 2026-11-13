---
titulo: "C02 — `load_java_script.sh` paso a paso"
familia: C
etapa: "Conversión Java"
tipo: Referencia
tags:
  - familia/C
  - etapa/conversion-java
  - tipo/referencia
keywords: "load_java_script, xmllint, gpg, DIR_MEGARA, conversión, sed"
---

# C02 — `load_java_script.sh` paso a paso

**Etapa:** Conversión Java
**Tipo:** Referencia
**Palabras clave:** load_java_script, xmllint, gpg, DIR_MEGARA, conversión, sed

## En una línea

Localiza el XML, sustituye los separadores conflictivos, comprueba que no está vacío, lo convierte
y archiva el original cifrado.

## Invocación

```bash
/nfq/data/cfg/load_java_script.sh <id_de_lookup_java>
```

## Los ocho pasos

### 1. Carga configuración

```bash
. /nfq/data/cfg/credentials.properties
. /nfq/data/cfg/env.properties
cd /nfq/data/cfg/
```

### 2. Lee la línea del lookup

Campos 3 (ruta XML), 4 (ruta XSD), 5 (herencias), 6 (exclusiones) y 7 (patrón de fichero) de
`lookup_java.txt`. Ver [C03_lookup_java_formato](../C%20-%20Conversion%20Java/C03_lookup_java_formato.md).

### 3. Busca el fichero — con una espera de 1 segundo

```bash
tiempo_max=1
while [[ $contador -lt $tiempo_max ]]; do
    if ls "$primero$patron1"*."$patron2" &>/dev/null; then break; fi
    sleep 1; ((contador++))
done
[[ $contador -ge $tiempo_max ]] && exit 1
```

**La espera es de un segundo, una sola iteración.** En la práctica no hay espera: o el fichero está
cuando se lanza, o el script sale con error. Muy distinto de los 120 segundos que espera el script
de flags.

### 4. ⚠ Sustituye los separadores en el XML original

```bash
sed -i 's/!/¡/g' "$fileToOpen"
```

**Modifica el fichero de entrada en disco**, no una copia. Todo signo de exclamación pasa a ser `¡`
de forma permanente. Ver [C05_sed_separador](../C%20-%20Conversion%20Java/C05_sed_separador.md) — tiene consecuencias sobre el dato.

### 5. Comprueba que el XML tiene contenido

```bash
has_elements=$(xmllint --xpath "count(//*/*) > 0" $fileToOpen)
```

Cuenta si hay nodos nieto. **`xmllint` no valida aquí contra el XSD**: sólo comprueba que el
documento no está vacío. La validación contra esquema la hace el JAR por dentro.
Ver [C04_validacion_xsd](../C%20-%20Conversion%20Java/C04_validacion_xsd.md).

### 6. Convierte, si hay contenido

```bash
cd /nfq/XMLconversor/
java -jar xmlConversor.jar "$fileToOpen" "$segundo" "$tercero" "$cuarto"
```

El `cd` es imprescindible: el conversor lee `config.properties` del directorio actual.

### 7. Archiva el original

Tanto si convirtió como si el XML estaba vacío:

```bash
gpg --encrypt -r $key_cript ${select}.$patron2
mv ${select}.$patron2".gpg" $processed"/DIR_MEGARA/"
rm -f ${select}.$patron2
```

### 8. Sale

`exit 0` si convirtió o si el fichero estaba vacío. `exit -1` si el JAR devolvió error.

## El XML vacío es un éxito

Si `xmllint` no encuentra nodos nieto, el script **no convierte**, archiva igualmente el original y
sale con `0`:

```
Archivo vacío, termina proceso  <fichero>.xml
```

Desde fuera es indistinguible de una conversión correcta: el job sale en verde y el XML desaparece
del directorio. Pero **no se generó ningún plano**, así que la carga posterior no encontrará
fichero y reportará «PASO OMITIDO». Ver [C10_conversion_sin_filas](../C%20-%20Conversion%20Java/C10_conversion_sin_filas.md) y [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md).

## Un defecto en la detección de extensión

```bash
if [[ ${fichero##*.}=~"xml\r" ]]; then patron2="xml"
elif [[ ${fichero##*.}=~"xlsx\r " ]]; then patron2="xlsx"
else patron2="xls"; fi
```

Falta el espacio alrededor del operador `=~`, así que Bash evalúa toda la expresión como una cadena
única, que siempre es no vacía: **la primera rama se cumple siempre** y `patron2` acaba valiendo
`"xml"` en todos los casos. Las otras dos ramas son código muerto.

No afecta al flujo actual porque todas las entradas son XML. Pero significa que **una entrada
`.xls` o `.xlsx` por esta vía no funcionaría**, aunque el JAR sí las soporte.

## Cómo verificarlo

```bash
# Convertir a mano una interfaz concreta
grep -i "<INTERFAZ>" /nfq/data/cfg/lookup_java.txt      # obtener el id
/nfq/data/cfg/load_java_script.sh <id>

# ¿Se archivó el original?
. /nfq/data/cfg/env.properties
ls -lat $processed/DIR_MEGARA/ | head
```

Antes de convertir a mano, comprueba que no se convirtió ya: duplicarías los planos de salida.

## Ver también

[C01_que_hace_xmlconversor](../C%20-%20Conversion%20Java/C01_que_hace_xmlconversor.md) · [C05_sed_separador](../C%20-%20Conversion%20Java/C05_sed_separador.md) · [C10_conversion_sin_filas](../C%20-%20Conversion%20Java/C10_conversion_sin_filas.md) · [C12_conversion_fallo_log](../C%20-%20Conversion%20Java/C12_conversion_fallo_log.md) · [B06_load_filesflag_script](../B%20-%20Recepcion%20y%20flags/B06_load_filesflag_script.md)

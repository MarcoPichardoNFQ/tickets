---
titulo: "C06 — Ficheros de salida: nombres, ficheros vacíos y borrado total"
familia: C
etapa: "Conversión Java"
tipo: Referencia
tags:
  - familia/C
  - etapa/conversion-java
  - tipo/referencia
keywords: "salida, nombres, CSV vacío, printMissingFiles, deleteFiles, timestamp"
---

# C06 — Ficheros de salida: nombres, ficheros vacíos y borrado total

**Etapa:** Conversión Java
**Tipo:** Referencia
**Palabras clave:** salida, nombres, CSV vacío, printMissingFiles, deleteFiles, timestamp

## En una línea

Un XML genera **varios** ficheros planos, algunos vacíos a propósito, y ante cualquier error se
borran todos.

## El patrón de nombre

```
<NombreXML>_<abuelo>_<padre>_<nodo>_<timestamp>.csv
```

El conversor toma el nombre del XML de entrada, le quita lo que va después del último guion bajo
—que es el timestamp— y lo vuelve a añadir al final:

```
Entrada:  Bond_1771431596036.xml
Salidas:  Bond__Bond_Issuer_1771431596036.csv
          Bond__Bond_Rating_1771431596036.csv
          ...
```

Los tramos de abuelo y padre pueden quedar vacíos cuando el nodo cuelga directamente del documento,
lo que produce dobles guiones bajos en el nombre. Es normal.

**Consecuencia práctica:** para localizar todas las salidas de un XML concreto, busca por su
timestamp, que es lo único que comparten todas:

```bash
. /nfq/data/cfg/env.properties
ls -la $raiz | grep "1771431596036"
```

## Los ficheros vacíos son deliberados

`printMissingFiles()` crea un CSV de **0 bytes** por cada nodo declarado en el XSD que no apareció
en el XML.

```java
if (!printed.contains(toPrint.get(i)) && !ignorableValues.contains(toPrint.get(i))) {
    // crea el fichero vacío
}
```

Un fichero de salida vacío significa **«este tipo de nodo no venía en este envío»**, no «la
conversión falló». Es información legítima y la carga posterior lo maneja sin problema: carga cero
filas.

Este punto genera falsos positivos con frecuencia. Un directorio lleno de CSV de 0 bytes después de
una conversión es el aspecto normal de un envío con pocos tipos de nodo.

## El borrado total ante error

Si algo falla durante el recorrido del XML, la comprobación de claves o la creación de ficheros
faltantes, el conversor ejecuta:

```java
public static void deleteFiles() {
    System.out.println("Eliminando los archivos generados...");
    for (String key : textFiles.keySet()) { textFiles.get(key).delete(); }
}
```

**Borra toda la salida ya generada** y sale con código 1.

Esto es una garantía útil: **nunca hay salida parcial**. O están todos los ficheros de un XML, o no
está ninguno. Si encuentras algunos ficheros de un timestamp pero no otros, no es una conversión a
medias — es que esos nodos no existían.

En el log queda la línea `Eliminando los archivos generados...`, que es una señal fiable de
conversión abortada:

```bash
grep -l "Eliminando los archivos generados" /ruta/a/logs/* 2>/dev/null
```

## El fichero se reescribe, no se acumula

Antes de escribir, si el fichero de salida ya existe, se borra:

```java
if (nextFile.exists()) { nextFile.delete(); }
```

Convertir dos veces el mismo XML **no duplica** las líneas de salida: la segunda pasada reemplaza a
la primera. Es una de las pocas operaciones idempotentes de toda la cadena.

Ojo: eso vale para la **conversión**. La carga posterior sí puede duplicar si el plano se procesa
dos veces. Ver [D13_cargo_dos_veces](../D%20-%20Carga%20STG/D13_cargo_dos_veces.md).

## El contenido de una línea

Por cada nodo con atributos se escribe una línea con esta estructura:

```
<claves heredadas de los ancestros><separador><atributos del nodo, en el orden del XSD>
```

Los atributos declarados en el XSD que no vengan en el XML aparecen como **campo vacío**, no como
columna ausente: el número de campos es siempre el mismo. Ver [C07_herencias_claves](../C%20-%20Conversion%20Java/C07_herencias_claves.md).

## Cómo verificarlo

```bash
. /nfq/data/cfg/env.properties

# Salidas generadas recientemente
ls -lat $raiz/*.csv | head -20

# Cuáles están vacías (normal)
find $raiz -name "*.csv" -size 0 -mmin -60 -ls

# Número de campos de un plano concreto
head -1 <FICHERO>.csv | awk -F'!' '{print NF}'
```

## Ver también

[C01_que_hace_xmlconversor](../C%20-%20Conversion%20Java/C01_que_hace_xmlconversor.md) · [C10_conversion_sin_filas](../C%20-%20Conversion%20Java/C10_conversion_sin_filas.md) · [C07_herencias_claves](../C%20-%20Conversion%20Java/C07_herencias_claves.md) · [D09_error_numero_columnas](../D%20-%20Carga%20STG/D09_error_numero_columnas.md)

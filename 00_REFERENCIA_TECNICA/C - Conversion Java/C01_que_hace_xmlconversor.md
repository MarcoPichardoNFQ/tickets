---
titulo: "C01 — Qué hace `xmlConversor.jar`"
familia: C
etapa: "Conversión Java"
tipo: Referencia
tags:
  - familia/C
  - etapa/conversion-java
  - tipo/referencia
keywords: "xmlConversor, jar, XML a plano, separador, config.properties, es.innotech.main"
---

# C01 — Qué hace `xmlConversor.jar`

**Etapa:** Conversión Java
**Tipo:** Referencia
**Palabras clave:** xmlConversor, jar, XML a plano, separador, config.properties, es.innotech.main

## En una línea

Valida un XML contra su XSD y lo descompone en **varios ficheros planos**, uno por tipo de nodo,
arrastrando hacia abajo las claves de los nodos padre.

## Invocación

```bash
cd /nfq/XMLconversor/
java -jar xmlConversor.jar <fichero.xml> <esquema.xsd> <herencias> <exclusiones>
```

| Argumento | Contenido | Origen |
|---|---|---|
| 1 | Fichero de entrada (`.xml`, `.xls`, `.xlsx`) | Campo 3 + 7 de `lookup_java.txt` |
| 2 | Esquema XSD | Campo 4 |
| 3 | Herencias: qué atributos son clave por nodo | Campo 5 |
| 4 | Nodos a ignorar | Campo 6 |

Códigos de salida: **`0` correcto, `1` error**.

## Configuración: `config.properties`

```properties
output=<directorio de salida>
separator=!
encoding=UTF-8
```

**Se lee con ruta relativa al directorio de trabajo.** El código hace literalmente
`new FileInputStream("config.properties")`, sin ruta absoluta. Por eso el script hace
`cd /nfq/XMLconversor/` antes de invocar el JAR.

Consecuencia práctica: **lanzado desde otro directorio, el conversor muere** con un error de fichero
no encontrado antes de tocar el XML. Si alguna vez pruebas la conversión a mano, sitúate primero en
`/nfq/XMLconversor/`.

## Qué hace por dentro, en orden

```
1. Lee config.properties (salida, separador, encoding)
2. Valida el XML contra el XSD
      → si no valida: imprime el motivo y sale con 1
3. Recorre el XSD y construye, por cada nodo, su lista ordenada de atributos
4. Recorre el XML de forma recursiva:
      · por cada nodo con atributos, escribe una línea en el fichero de ese nodo
      · antepone las claves heredadas de todos sus ancestros
5. Comprueba que las claves declaradas existen
6. Crea ficheros VACÍOS para los nodos del XSD que no aparecían en el XML
```

Si algo falla en los pasos 4, 5 o 6, ejecuta `deleteFiles()`: **borra toda la salida ya generada**.
No queda resultado parcial. O están todos los ficheros o no está ninguno.

## Un XML produce varios ficheros

Es lo que más sorprende al principio. La salida no es «un CSV por XML» sino **un fichero por tipo de
nodo** encontrado, con este patrón de nombre:

```
<NombreXML>_<abuelo>_<padre>_<nodo>_<timestamp>.csv
```

El `<timestamp>` se toma del propio nombre del XML de entrada: el conversor separa por el último
guion bajo. Un fichero `Bond_1771431596036.xml` produce salidas terminadas en `_1771431596036.csv`.

Ver [C06_ficheros_de_salida](../C%20-%20Conversion%20Java/C06_ficheros_de_salida.md).

## Tres comportamientos que parecen fallo y no lo son

**Los ficheros vacíos son deliberados.** `printMissingFiles()` crea un CSV de 0 bytes por cada nodo
declarado en el XSD que no apareció en el XML. Es información, no un error: indica «este tipo de
nodo no venía en este envío».

**Los saltos de línea desaparecen.** Todo valor pasa por
`replace("\r", " ").replaceAll("\n", " ")`. Un campo multilínea llega a staging en una sola línea.

**Los valores no se entrecomillan.** No hay comillas ni escape. Si un valor contiene el separador,
la línea gana un campo. Por eso el script hace una sustitución previa. Ver [C05_sed_separador](../C%20-%20Conversion%20Java/C05_sed_separador.md).

## Formatos de entrada

Además de XML acepta `.xls` y `.xlsx` mediante Apache POI. Esa vía tiene un defecto conocido:
el bucle de lectura es `while (j < sheet.getLastRowNum())`, con lo que **se salta la última fila**
de la hoja. No afecta al flujo principal, que es todo XML.

## Cómo verificarlo

```bash
cd /nfq/XMLconversor/
cat config.properties
ls -la xmlConversor.jar
ls -la xsd/ | head
```

## Ver también

[C02_load_java_script](../C%20-%20Conversion%20Java/C02_load_java_script.md) · [C03_lookup_java_formato](../C%20-%20Conversion%20Java/C03_lookup_java_formato.md) · [C04_validacion_xsd](../C%20-%20Conversion%20Java/C04_validacion_xsd.md) · [C06_ficheros_de_salida](../C%20-%20Conversion%20Java/C06_ficheros_de_salida.md) · [C07_herencias_claves](../C%20-%20Conversion%20Java/C07_herencias_claves.md)

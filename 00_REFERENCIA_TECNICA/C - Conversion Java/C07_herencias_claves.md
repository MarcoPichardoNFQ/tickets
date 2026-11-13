---
titulo: "C07 — Herencias: cómo se arrastran las claves del padre"
familia: C
etapa: "Conversión Java"
tipo: Referencia
tags:
  - familia/C
  - etapa/conversion-java
  - tipo/referencia
keywords: "herencias, keyMap, claves del padre, jerarquía, lookForKeys, mainReference"
---

# C07 — Herencias: cómo se arrastran las claves del padre

**Etapa:** Conversión Java
**Tipo:** Referencia
**Palabras clave:** herencias, keyMap, claves del padre, jerarquía, lookForKeys, mainReference

## En una línea

El XML es jerárquico y las tablas son planas: las herencias resuelven eso copiando las claves de
todos los ancestros al principio de cada línea hija.

## El problema que resuelven

Un XML anida:

```xml
<CA mainReference="CA-001">
    <Option pk="OPT-77">
        <Detail amount="1000"/>
    </Option>
</CA>
```

Si el fichero de `Detail` sólo contuviera `1000`, sería imposible saber a qué opción y a qué evento
corporativo pertenece. Las herencias resuelven eso: cada línea de `Detail` lleva delante
`CA-001` y `OPT-77`.

## Cómo se declaran

Campo 5 de `lookup_java.txt`:

```
CA=mainReference;CA.Option=pk
```

Sintaxis: `ruta.del.nodo=atributo1,atributo2` separadas por `;`.

- `CA=mainReference` → en el nodo `CA`, la clave es el atributo `mainReference`
- `CA.Option=pk` → en `Option` dentro de `CA`, la clave es `pk`

La ruta se construye con los nombres cortos de los nodos, ignorando los que estén en el campo de
exclusiones.

## Cómo funciona por dentro

Al escribir la línea de un nodo, el conversor sube por el árbol recogiendo las claves declaradas de
cada ancestro:

```java
PKListString = main.lookForKeys(nodeReference.getParentNode(), new ArrayList<String>());
for (int i = 0; i < PKListString.size(); i++) {
    toReturn = PKListString.get(i) + separator + toReturn;   // se antepone
}
```

Las claves se van **anteponiendo**, así que quedan al principio de la línea, del ancestro más
cercano hacia atrás.

Resultado para el ejemplo anterior, con separador `!`:

```
OPT-77!CA-001!1000
```

## Qué pasa si están mal declaradas

Dos errores posibles, y ambos **abortan la conversión con mensaje legible**:

**El atributo no existe en el XML:**

```
El atributo "<nombre>" no existe.
```

Se lanza al intentar leerlo. Causa típica: el origen dejó de informar ese atributo, o cambió su
nombre.

**La ruta no corresponde a ningún nodo del XSD:**

```
El nodo al que "<nombre>" hace referencia no existe.
```

Lo comprueba `checkForWrongKeys()` al final, contrastando cada clave declarada contra los nodos
encontrados en el XSD. Causa típica: el XSD cambió su estructura y el lookup no se actualizó.

En ambos casos se ejecuta el borrado total de la salida. Ver [C06_ficheros_de_salida](../C%20-%20Conversion%20Java/C06_ficheros_de_salida.md).

## Consecuencia para la carga

Las columnas heredadas **van al principio** del fichero plano y forman parte del número total de
campos. Si alguien cambia las herencias de una interfaz —añade o quita una clave— **cambia el
número de columnas del plano**, y la carga posterior falla con error de columnas hasta que se
actualice `PAR_MAESTRO_COLUMNAS_T`.

Es decir: **el campo 5 de `lookup_java.txt` y la parametrización de columnas en base de datos tienen
que estar sincronizados.** No hay nada que lo verifique automáticamente.

Ver [D09_error_numero_columnas](../D%20-%20Carga%20STG/D09_error_numero_columnas.md).

## La mayoría no tiene herencias

En el catálogo, la mayor parte de las líneas llevan los campos 5 y 6 vacíos (`|||`). Sólo las
interfaces con estructura anidada real las necesitan.

```bash
# Cuántas conversiones declaran herencias
awk -F'|' 'NF>1 && $5!=""' /nfq/data/cfg/lookup_java.txt | wc -l

# Cuáles
awk -F'|' 'NF>1 && $5!="" {print $2" -> "$5}' /nfq/data/cfg/lookup_java.txt
```

Esa segunda orden da la lista de interfaces sensibles a este mecanismo: son las que hay que revisar
si el XSD de origen cambia.

## Ver también

[C03_lookup_java_formato](../C%20-%20Conversion%20Java/C03_lookup_java_formato.md) · [C06_ficheros_de_salida](../C%20-%20Conversion%20Java/C06_ficheros_de_salida.md) · [C01_que_hace_xmlconversor](../C%20-%20Conversion%20Java/C01_que_hace_xmlconversor.md) · [D09_error_numero_columnas](../D%20-%20Carga%20STG/D09_error_numero_columnas.md) · [C12_conversion_fallo_log](../C%20-%20Conversion%20Java/C12_conversion_fallo_log.md)

---
titulo: "C03 — `lookup_java.txt`: formato y cómo leerlo"
familia: C
etapa: "Conversión Java"
tipo: Referencia
tags:
  - familia/C
  - etapa/conversion-java
  - tipo/referencia
keywords: "lookup_java, herencias, exclusiones, xsd, patrón, Manual"
---

# C03 — `lookup_java.txt`: formato y cómo leerlo

**Etapa:** Conversión Java
**Tipo:** Referencia
**Palabras clave:** lookup_java, herencias, exclusiones, xsd, patrón, Manual

## En una línea

Cada línea define una conversión: dónde está el XML, cuál es su XSD, qué atributos actúan de clave
y qué nodos se ignoran.

## Formato

```
|id|ruta_xml|ruta_xsd|herencias|exclusiones|patrón_fichero|
```

Ejemplos reales:

```
|1|/prdmegara/PRD/Devices/MegaCommon/innotech/Manual/|/nfq/XMLconversor/xsd/CAConfiguration.xsd|||CAConfiguration_.xml|
|3|/prdmegara/PRD/Devices/MegaCommon/innotech/Manual/|/nfq/XMLconversor/xsd/CA.xsd|CA=mainReference;CA.Option=pk||CA_.xml|
|4|/prdmegara/PRD/Devices/MegaCommon/innotech/Manual/|/nfq/XMLconversor/xsd/ClientEntitlement.xsd|ClientEntConstraint=appReference;ClientEntConstraint.ClientCashMovement=appReference||ClientEntitlement_.xml|
```

| Campo | Contenido | Obligatorio |
|---|---|---|
| 2 | **id** — se pasa como argumento al script | Sí |
| 3 | **Ruta del XML** de entrada | Sí |
| 4 | **Ruta del XSD** | Sí |
| 5 | **Herencias** — qué atributos son clave, por nodo | No |
| 6 | **Exclusiones** — nodos a ignorar | No |
| 7 | **Patrón de fichero** | Sí |

Campos 5 y 6 vacíos son lo habitual: la mayoría de las líneas los llevan en blanco (`|||`).

## El campo de herencias

Sintaxis: `ruta.completa=atributo1,atributo2;otra.ruta=atributo`

```
CA=mainReference;CA.Option=pk
```

Significa: en el nodo `CA`, la clave es el atributo `mainReference`; en el nodo `Option` dentro de
`CA`, la clave es `pk`.

Esas claves se **arrastran hacia abajo**: cada fila generada para un nodo hijo lleva delante las
claves de todos sus ancestros. Es lo que permite reconstruir la jerarquía del XML en tablas planas.
Ver [C07_herencias_claves](../C%20-%20Conversion%20Java/C07_herencias_claves.md).

Si un atributo declarado aquí no existe en el XML, el conversor aborta con:

```
El atributo "<nombre>" no existe.
```

Y si la ruta declarada no corresponde a ningún nodo del XSD:

```
El nodo al que "<nombre>" hace referencia no existe.
```

Ambos mensajes **sí son legibles**, a diferencia de otros errores del conversor. Ver [C12_conversion_fallo_log](../C%20-%20Conversion%20Java/C12_conversion_fallo_log.md).

## El campo de exclusiones

Lista separada por comas de nodos que el conversor ignora al recorrer el XML, típicamente el nodo
raíz cuando aporta un nivel de anidamiento que no interesa. Los nodos excluidos no generan fichero
propio y tampoco cuentan al construir las rutas de referencia.

## Rutas fijas del entorno

| Elemento | Ruta |
|---|---|
| XML de entrada | `/prdmegara/PRD/Devices/MegaCommon/innotech/Manual/` |
| XSD | `/nfq/XMLconversor/xsd/` |
| JAR y `config.properties` | `/nfq/XMLconversor/` |

Nótese el subdirectorio **`Manual/`** en la ruta de entrada de estas conversiones, distinto del
directorio raíz donde llegan los flags.

## El patrón de fichero

El script separa nombre y extensión, y busca con comodín excluyendo los `_InLoad`:

```bash
ls $patron1* | grep -v '_InLoad.'$patron2'' | head -1
```

Un patrón `CAConfiguration_.xml` casa con `CAConfiguration_1771431596036.xml`.

## Cómo verificarlo

```bash
# Definición de una conversión concreta
grep '|<id>|' /nfq/data/cfg/lookup_java.txt

# Buscar por nombre de interfaz
grep -i "<INTERFAZ>" /nfq/data/cfg/lookup_java.txt

# ¿Cuántas conversiones tienen herencias declaradas?
awk -F'|' 'NF>1 && $5!=""' /nfq/data/cfg/lookup_java.txt | wc -l

# ¿Existe el XSD que declara?
grep '|<id>|' /nfq/data/cfg/lookup_java.txt | cut -d'|' -f4 | xargs ls -la
```

Esa última comprobación merece la pena: un XSD que ya no existe en la ruta declarada hace fallar la
conversión con un error poco explícito.

## Ver también

[C01_que_hace_xmlconversor](../C%20-%20Conversion%20Java/C01_que_hace_xmlconversor.md) · [C02_load_java_script](../C%20-%20Conversion%20Java/C02_load_java_script.md) · [C07_herencias_claves](../C%20-%20Conversion%20Java/C07_herencias_claves.md) · [C04_validacion_xsd](../C%20-%20Conversion%20Java/C04_validacion_xsd.md)

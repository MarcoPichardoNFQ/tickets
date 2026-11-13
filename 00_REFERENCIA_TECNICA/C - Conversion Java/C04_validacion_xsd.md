---
titulo: "C04 — Validación contra el XSD: qué valida y qué no"
familia: C
etapa: "Conversión Java"
tipo: Referencia
tags:
  - familia/C
  - etapa/conversion-java
  - tipo/referencia
keywords: "XSD, validación, xmllint, esquema, no es válido, SAXException"
---

# C04 — Validación contra el XSD: qué valida y qué no

**Etapa:** Conversión Java
**Tipo:** Referencia
**Palabras clave:** XSD, validación, xmllint, esquema, no es válido, SAXException

## En una línea

El XSD lo valida el JAR por dentro, no `xmllint`; y esa validación decide **si el fichero se
convierte o se rechaza entero**.

## Quién valida qué

| Herramienta | Qué comprueba | Cuándo |
|---|---|---|
| `xmllint --xpath "count(//*/*) > 0"` | Sólo que el XML **tenga contenido** | En el script, antes de convertir |
| `xmlConversor.jar` | **Validación completa contra el XSD** | Dentro del JAR, primer paso |

Es un matiz que se malinterpreta a menudo: el documento de arquitectura menciona `xmllint` junto al
conversor, pero `xmllint` aquí no valida esquema, sólo cuenta nodos. Ver [C02_load_java_script](../C%20-%20Conversion%20Java/C02_load_java_script.md).

## Cómo valida el JAR

```java
SchemaFactory schemaFactory = SchemaFactory.newInstance("http://www.w3.org/2001/XMLSchema");
Schema schema = schemaFactory.newSchema(schemaFile);
Validator validator = schema.newValidator();
validator.validate(xmlFile);
```

Validación estándar de Java. Si falla:

```
<ruta del fichero> NO es válido. Razón: <excepción SAX con el detalle>
```

Y el proceso sale con código `1` **sin generar ningún fichero de salida**.

## La validación es de todo o nada

No hay validación por filas. Si el XML incumple el esquema en un solo punto, **se rechaza el fichero
completo**. No existe aquí el concepto de «apartar la fila mala y seguir» que sí hay en la capa de
base de datos.

Consecuencia: un fallo de XSD es siempre una incidencia de interfaz completa, nunca de unos pocos
registros. Ver [C09_xml_no_valida](../C%20-%20Conversion%20Java/C09_xml_no_valida.md).

## El mensaje de error sí es legible

Es importante saberlo, porque otros errores del conversor no lo son. El mensaje de validación
incluye la excepción SAX completa, que normalmente indica **línea, columna y qué elemento o
atributo incumple**. Es el error más fácil de diagnosticar de toda la etapa.

Ver el contraste en [C12_conversion_fallo_log](../C%20-%20Conversion%20Java/C12_conversion_fallo_log.md).

## El XSD también define las columnas

La validación no es lo único que hace el esquema. El conversor **recorre el XSD para construir, por
cada nodo, la lista ordenada de sus atributos**, y esa lista determina las columnas del fichero
plano de salida y su orden.

De ahí se derivan dos cosas:

- Un atributo declarado en el XSD que no venga en el XML produce una **columna vacía**, no un error.
- Si el XSD cambia el orden de sus atributos, **cambia el orden de las columnas del plano**, y la
  carga posterior meterá los datos en columnas equivocadas sin fallar. Ver [D04_read_header_fn](../D%20-%20Carga%20STG/D04_read_header_fn.md).

Ese segundo caso es el fallo más silencioso de toda la cadena: nada da error y el dato acaba
desplazado.

## Reproducir la validación a mano

Es la primera acción ante un fallo de conversión, porque el log del propio conversor puede no decir
nada útil:

```bash
grep '|<id>|' /nfq/data/cfg/lookup_java.txt    # obtener rutas de XML y XSD
xmllint --noout --schema /nfq/XMLconversor/xsd/<ESQUEMA>.xsd <FICHERO>.xml
```

`xmllint --schema` **sí** valida contra el esquema y devuelve un mensaje preciso con la línea del
problema. Es la herramienta de diagnóstico de esta etapa.

## Los XSD del sistema

Viven en `/nfq/XMLconversor/xsd/`. En el material de muestra disponible hay **148 esquemas**, uno
por interfaz.

```bash
ls /nfq/XMLconversor/xsd/ | wc -l
ls -la /nfq/XMLconversor/xsd/ | grep -i "<INTERFAZ>"
```

Comprueba también la fecha: un XSD sin tocar desde hace años frente a un origen que ha evolucionado
es la causa de fondo de muchos fallos de validación repentinos.

## Ver también

[C09_xml_no_valida](../C%20-%20Conversion%20Java/C09_xml_no_valida.md) · [C01_que_hace_xmlconversor](../C%20-%20Conversion%20Java/C01_que_hace_xmlconversor.md) · [C02_load_java_script](../C%20-%20Conversion%20Java/C02_load_java_script.md) · [C12_conversion_fallo_log](../C%20-%20Conversion%20Java/C12_conversion_fallo_log.md) · [D04_read_header_fn](../D%20-%20Carga%20STG/D04_read_header_fn.md)

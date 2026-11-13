---
titulo: "C12 — La conversión falló y el log no dice por qué"
familia: C
etapa: "Conversión Java"
tipo: Runbook
tags:
  - familia/C
  - etapa/conversion-java
  - tipo/runbook
keywords: "log ilegible, StackTraceElement, error sin causa, diagnóstico alternativo, KO"
---

# C12 — La conversión falló y el log no dice por qué

**Etapa:** Conversión Java
**Tipo:** Runbook
**Palabras clave:** log ilegible, StackTraceElement, error sin causa, diagnóstico alternativo, KO

## Síntoma

El log de conversión muestra algo como:

```
[Ljava.lang.StackTraceElement;@1b6d3586
KO  Bond_1771431596036.xml
```

Y no hay ninguna pista de qué falló.

## Por qué pasa

El conversor imprime el **array** de la traza de pila en vez de su contenido:

```java
System.out.println(e.getStackTrace().toString());   // main.java:136
System.out.println(e.getStackTrace());              // main.java:182
```

En Java, eso produce el tipo y la dirección de memoria del array, no la excepción. **La causa real
se pierde.** No es un problema de configuración de logs: el mensaje útil nunca se llega a escribir.

## Los mensajes que SÍ son legibles

No todo está perdido. Estos errores del conversor sí se imprimen bien, y conviene buscarlos primero
en el log antes de dar por ilegible la salida:

| Mensaje | Significa |
|---|---|
| `<fichero> NO es válido. Razón: ...` | Fallo de validación XSD → [C09_xml_no_valida](../C%20-%20Conversion%20Java/C09_xml_no_valida.md) |
| `El atributo "<nombre>" no existe.` | Herencia declarada sobre un atributo ausente → [C07_herencias_claves](../C%20-%20Conversion%20Java/C07_herencias_claves.md) |
| `El nodo al que "<nombre>" hace referencia no existe.` | Herencia sobre una ruta que no está en el XSD |
| `La extensión del archivo no se corresponde...` | Entrada que no es xml/xls/xlsx |
| `Una excepción paró la ejecución del programa...` | Fallo durante el recorrido del XML |
| `Eliminando los archivos generados...` | Se abortó y se borró la salida |

Si ves el último mensaje, sabes al menos **en qué fase** falló: ya había empezado a generar
ficheros.

## Diagnóstico cuando el log no ayuda

Ve por descarte, en este orden:

### 1. Valida el XSD a mano

Cubre la mayoría de los casos y da un mensaje preciso:

```bash
grep '|<id>|' /nfq/data/cfg/lookup_java.txt
xmllint --noout --schema /nfq/XMLconversor/xsd/<ESQUEMA>.xsd <FICHERO>.xml
```

### 2. Comprueba que el XSD existe y es legible

```bash
grep '|<id>|' /nfq/data/cfg/lookup_java.txt | cut -d'|' -f4 | xargs ls -la
```

### 3. Comprueba las herencias declaradas

```bash
grep '|<id>|' /nfq/data/cfg/lookup_java.txt | cut -d'|' -f5
```

Si hay herencias, verifica que esos atributos existen realmente en el XML:

```bash
grep -o 'mainReference="[^"]*"' <FICHERO>.xml | head -3
```

### 4. Comprueba el directorio de trabajo

El conversor lee `config.properties` con **ruta relativa**. Si se lanzó desde otro sitio, muere
antes de tocar el XML:

```bash
cd /nfq/XMLconversor/ && cat config.properties
```

Que el directorio de salida configurado exista y sea escribible es parte de esta comprobación.

### 5. Reproduce la conversión a mano

Con los argumentos exactos del lookup, y mirando la salida completa:

```bash
cd /nfq/XMLconversor/
L=$(grep '|<id>|' /nfq/data/cfg/lookup_java.txt)
java -jar xmlConversor.jar \
     "$(echo "$L" | cut -d'|' -f3)<FICHERO>.xml" \
     "$(echo "$L" | cut -d'|' -f4)" \
     "$(echo "$L" | cut -d'|' -f5)" \
     "$(echo "$L" | cut -d'|' -f6)"
echo "código de salida: $?"
```

Ejecutarlo directamente muestra los mensajes legibles que el log del job puede estar recortando.
**Ojo:** si funciona, generará los ficheros de salida de verdad. Comprueba antes que no se
convirtió ya.

### 6. Descarta el fichero truncado

```bash
tail -5 <FICHERO>.xml      # ¿cierra la etiqueta raíz?
ls -la <FICHERO>.xml       # ¿tamaño coherente con el histórico?
```

## Señal útil: dónde quedó el XML

| Estado del XML | Significa |
|---|---|
| Sigue en el directorio de entrada | La conversión **falló** |
| Está cifrado en `DIR_MEGARA` | Convirtió bien, o estaba vacío |

Es la comprobación más rápida para saber si de verdad hubo fallo. Ver [C08_cifrado_xml_original](../C%20-%20Conversion%20Java/C08_cifrado_xml_original.md).

## Cuándo escalar

- Si tras los seis pasos no aparece la causa.
- Si el fallo se repite en varias interfaces a la vez: apunta al entorno —Java, permisos, disco
  lleno en el directorio de salida— y no al dato.

Merece escalarse también la observación de fondo: **el conversor no registra sus errores de forma
legible**, y eso alarga cada incidencia de esta etapa. Es una corrección de una línea en el código
Java.

## Ver también

[C09_xml_no_valida](../C%20-%20Conversion%20Java/C09_xml_no_valida.md) · [C07_herencias_claves](../C%20-%20Conversion%20Java/C07_herencias_claves.md) · [C10_conversion_sin_filas](../C%20-%20Conversion%20Java/C10_conversion_sin_filas.md) · [C01_que_hace_xmlconversor](../C%20-%20Conversion%20Java/C01_que_hace_xmlconversor.md) · [C08_cifrado_xml_original](../C%20-%20Conversion%20Java/C08_cifrado_xml_original.md)

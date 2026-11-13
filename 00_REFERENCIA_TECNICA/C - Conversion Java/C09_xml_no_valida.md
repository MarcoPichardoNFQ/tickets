---
titulo: "C09 — El XML no valida contra su XSD"
familia: C
etapa: "Conversión Java"
tipo: Runbook
tags:
  - familia/C
  - etapa/conversion-java
  - tipo/runbook
keywords: "NO es válido, SAXException, xmllint --schema, validación, esquema desactualizado"
---

# C09 — El XML no valida contra su XSD

**Etapa:** Conversión Java
**Tipo:** Runbook
**Palabras clave:** NO es válido, SAXException, xmllint --schema, validación, esquema desactualizado

## Síntoma

En el log de conversión:

```
<ruta>/<fichero>.xml NO es válido. Razón: org.xml.sax.SAXParseException; ...
```

El job sale con error y **no se genera ningún fichero de salida**.

## Qué mirar primero

Reproduce la validación a mano. Es la acción más rentable de toda esta familia:

```bash
grep '|<id>|' /nfq/data/cfg/lookup_java.txt      # rutas de XML y XSD
xmllint --noout --schema /nfq/XMLconversor/xsd/<ESQUEMA>.xsd <FICHERO>.xml
```

`xmllint --schema` da línea, columna y el elemento o atributo concreto que incumple. El JAR también
lo dice, pero `xmllint` es más cómodo de leer y permite iterar.

## Causas probables, por orden

**1. El origen cambió el XML y el XSD no se actualizó.** La causa dominante. Un atributo nuevo, un
elemento con otra cardinalidad, un tipo distinto. Comprueba las fechas:

```bash
ls -la /nfq/XMLconversor/xsd/<ESQUEMA>.xsd     # ¿de cuándo es el esquema?
```

Un XSD de hace años frente a un origen vivo es sospechoso por sí solo.

**2. Valor fuera del tipo declarado.** Una fecha con otro formato, un número donde se espera entero,
una cadena que excede una longitud declarada en el esquema.

**3. Fichero truncado.** La transferencia se cortó y el XML no cierra sus etiquetas. Señal
inequívoca: el error apunta al **final** del documento y habla de fin de fichero inesperado.

```bash
tail -5 <FICHERO>.xml     # ¿cierra bien la etiqueta raíz?
ls -la <FICHERO>.xml      # ¿el tamaño es el habitual?
```

Contrasta el tamaño con el histórico de esa interfaz:

```sql
SELECT id_camda, tamanho_interfaz::bigint AS bytes
FROM   trf_s3.tmp_controlflag_interfaces
WHERE  nome_interface_base = '<INTERFAZ>'
ORDER  BY id_camda DESC LIMIT 15;
```

**4. Codificación.** Caracteres que rompen el parseo, o declaración de encoding que no corresponde
al contenido real.

**5. El XSD apuntado no existe o cambió de sitio.** El error entonces no es de validación sino de
lectura del esquema:

```bash
grep '|<id>|' /nfq/data/cfg/lookup_java.txt | cut -d'|' -f4 | xargs ls -la
```

## Acción

### 1. Clasifica el fallo

```bash
xmllint --noout --schema /nfq/XMLconversor/xsd/<ESQUEMA>.xsd <FICHERO>.xml 2>&1 | head -20
```

| El mensaje dice | Diagnóstico |
|---|---|
| `Premature end of data` o error al final | Fichero truncado → reclamar reenvío |
| `element X: This element is not expected` | Estructura cambiada → XSD desactualizado |
| `attribute X is not allowed` | Atributo nuevo en origen |
| `is not a valid value of the atomic type` | Valor con formato incorrecto |
| Error al cargar el esquema | Problema con el XSD, no con el XML |

### 2. Mira si es puntual o sistemático

```sql
SELECT id_camda, recebido, track_status, data_recebemento
FROM   stg_s3.controlflag_interfaces
WHERE  nome_interface_base = '<INTERFAZ>'
ORDER  BY id_camda DESC LIMIT 20;
```

Si la interfaz venía validando bien hasta hoy, algo cambió hoy. Si lleva fallando varios lotes, es
un cambio de contrato que nadie ha atendido.

### 3. Compara con un envío que sí validó

```bash
. /nfq/data/cfg/env.properties
cd $processed/DIR_MEGARA/
gpg --decrypt <FICHERO_ANTERIOR_OK>.xml.gpg > /tmp/ok.xml
diff <(head -30 /tmp/ok.xml) <(head -30 <FICHERO_NUEVO>.xml)
rm /tmp/ok.xml
```

Las primeras líneas suelen bastar para ver qué cambió en la estructura.

## Lo que no hay que hacer

**No edites el XML para que valide.** Es tentador y funciona una vez, pero enmascara un cambio de
contrato que volverá mañana, y el fichero editado ya no coincide con lo que el origen mandó.

**No toques el XSD.** Modificar un esquema para que acepte el nuevo formato es un cambio de contrato
de datos: afecta a las columnas del plano de salida y, en cascada, a la parametrización de columnas
de la carga. Ver [C04_validacion_xsd](../C%20-%20Conversion%20Java/C04_validacion_xsd.md) y [D09_error_numero_columnas](../D%20-%20Carga%20STG/D09_error_numero_columnas.md).

## Cuándo escalar

Siempre. Un fallo de XSD es, por definición, una discrepancia entre lo que el origen manda y lo que
el sistema espera. La corrección —adaptar el esquema o corregir el emisor— es una decisión que
excede a soporte. Lo que sí aporta soporte es el diagnóstico preciso: qué elemento, qué línea, desde
cuándo, y si es puntual o sistemático.

## Ver también

[C04_validacion_xsd](../C%20-%20Conversion%20Java/C04_validacion_xsd.md) · [C12_conversion_fallo_log](../C%20-%20Conversion%20Java/C12_conversion_fallo_log.md) · [C10_conversion_sin_filas](../C%20-%20Conversion%20Java/C10_conversion_sin_filas.md) · [R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md)

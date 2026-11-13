---
titulo: "C10 — La conversión no produjo filas"
familia: C
etapa: "Conversión Java"
tipo: Runbook
tags:
  - familia/C
  - etapa/conversion-java
  - tipo/runbook
keywords: "archivo vacío, 0 filas, CSV vacío, PASO OMITIDO, xmllint, falso positivo"
---

# C10 — La conversión no produjo filas

**Etapa:** Conversión Java
**Tipo:** Runbook
**Palabras clave:** archivo vacío, 0 filas, CSV vacío, PASO OMITIDO, xmllint, falso positivo

## Síntoma

La conversión terminó en verde pero no hay planos que cargar, o los que hay están vacíos. Y después
la carga reporta «PASO OMITIDO».

## Tres situaciones distintas que se parecen

### A. El XML venía vacío — y el sistema lo trata como éxito

```
Archivo vacío, termina proceso  <fichero>.xml
```

El script comprueba `xmllint --xpath "count(//*/*) > 0"`. Si no hay nodos nieto, **no convierte**,
archiva el XML igualmente y **sale con código 0**.

Desde fuera es indistinguible de una conversión correcta: el job sale verde y el XML desaparece del
directorio de entrada. Pero no se generó ningún plano.

Comprobación:

```bash
. /nfq/data/cfg/env.properties
cd $processed/DIR_MEGARA/
gpg --decrypt <FICHERO>.xml.gpg | head -20     # ¿tiene nodos de datos?
gpg --decrypt <FICHERO>.xml.gpg | wc -c        # tamaño real
```

Un XML de pocos cientos de bytes con sólo la etiqueta raíz confirma el caso.

**¿Es incidencia?** Depende de si esa interfaz debía traer datos hoy. Muchas traen envíos vacíos con
normalidad: un día sin movimientos produce un XML sin nodos. Contrasta con su historia:

```sql
SELECT id_camda, tamanho_interfaz::bigint AS bytes, data_recebemento
FROM   trf_s3.tmp_controlflag_interfaces
WHERE  nome_interface_base = '<INTERFAZ>'
ORDER  BY id_camda DESC LIMIT 20;
```

Si siempre son 8 MB y hoy 400 bytes, es una incidencia de origen. Si alterna entre vacío y con
datos, es su comportamiento normal.

### B. Se generaron planos, pero algunos están vacíos

**Esto es normal y deliberado.** El conversor crea un CSV de 0 bytes por cada nodo declarado en el
XSD que no apareció en el XML. Ver [C06_ficheros_de_salida](../C%20-%20Conversion%20Java/C06_ficheros_de_salida.md).

```bash
find $raiz -name "*<timestamp>*" -ls    # todas las salidas de ese XML
```

Si algunos tienen contenido y otros están a cero, la conversión fue **correcta**: el XML no traía
esos tipos de nodo.

### C. No hay ningún plano y el XML tampoco está archivado

Entonces la conversión **falló**. El XML sigue en el directorio de entrada, porque el archivado sólo
ocurre en los caminos de éxito.

```bash
ls -la /prdmegara/PRD/Devices/MegaCommon/innotech/*.xml 2>/dev/null | grep -i "<INTERFAZ>"
```

Ve a [C09_xml_no_valida](../C%20-%20Conversion%20Java/C09_xml_no_valida.md) y [C12_conversion_fallo_log](../C%20-%20Conversion%20Java/C12_conversion_fallo_log.md).

## Tabla de decisión rápida

| ¿XML archivado en `DIR_MEGARA`? | ¿Hay planos? | Diagnóstico |
|---|---|---|
| Sí | Sí, con contenido | Todo bien |
| Sí | Sí, algunos vacíos | Normal: esos nodos no venían |
| Sí | **No hay ninguno** | El XML venía vacío → caso A |
| **No** | No | **La conversión falló** → caso C |

Esa tabla resuelve el diagnóstico en dos comprobaciones de directorio.

## La consecuencia aguas abajo

En los casos A y B, la carga posterior no encuentra fichero para algunas tablas y reporta:

```
no existe archivo y descartes *****************PASO OMITIDO****************
```

Y marca error general, con lo que **el bloque entero acaba en rojo**. Es la principal fuente de
ruido de la etapa de carga y, en estos casos, **no es una incidencia**. Ver [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md).

## Acción

1. Aplica la tabla de decisión.
2. Si es el caso A, compara el tamaño con el histórico antes de decidir si escalas.
3. Si es el caso B, cierra: es comportamiento normal.
4. Si es el caso C, diagnostica el fallo de conversión.
5. En A y B, si el bloque quedó en rojo sólo por «PASO OMITIDO», documéntalo como ruido conocido en
   el ticket para que el siguiente turno no repita la investigación.

## Cuándo escalar

Sólo si el XML viene vacío cuando históricamente traía datos. Eso es un fallo en la generación del
origen, y ningún control del sistema lo detecta: para el flag el fichero llegó, y para la conversión
todo fue bien.

## Ver también

[C06_ficheros_de_salida](../C%20-%20Conversion%20Java/C06_ficheros_de_salida.md) · [C02_load_java_script](../C%20-%20Conversion%20Java/C02_load_java_script.md) · [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md) · [C09_xml_no_valida](../C%20-%20Conversion%20Java/C09_xml_no_valida.md) · [R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md)

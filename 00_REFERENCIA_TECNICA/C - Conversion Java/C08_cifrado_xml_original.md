---
titulo: "C08 — Cifrado y archivado del XML original"
familia: C
etapa: "Conversión Java"
tipo: Referencia
tags:
  - familia/C
  - etapa/conversion-java
  - tipo/referencia
keywords: "gpg, bk_stored, DIR_MEGARA, archivado, descifrar, recuperar original"
---

# C08 — Cifrado y archivado del XML original

**Etapa:** Conversión Java
**Tipo:** Referencia
**Palabras clave:** gpg, bk_stored, DIR_MEGARA, archivado, descifrar, recuperar original

## En una línea

Tras convertir —o tras detectar que el XML estaba vacío— el original se cifra con GPG y se archiva
en `DIR_MEGARA`, y el claro se borra.

## La secuencia

```bash
gpg --encrypt -r $key_cript ${select}.$patron2
mv ${select}.$patron2".gpg" $processed"/DIR_MEGARA/"
rm -f ${select}.$patron2
```

| Elemento | Valor |
|---|---|
| Destinatario GPG | `bk_stored` (variable `key_cript` de `env.properties`) |
| Destino | `$processed/DIR_MEGARA/` = `/prddatahub/DIR_PROCESSED/DIR_MEGARA/` |
| Original en claro | Se borra |

## Cuándo ocurre y cuándo no

| Situación | ¿Se archiva? | Código de salida |
|---|---|---|
| Conversión correcta | **Sí** | 0 |
| XML vacío (sin nodos nieto) | **Sí** | 0 |
| El conversor devuelve error | **No** | -1 |

Ese tercer caso es útil para diagnosticar: **un XML que sigue en el directorio de entrada después de
intentar convertirlo es un XML cuya conversión falló**. Si desapareció, o convirtió bien o estaba
vacío.

## Recuperar el original

Es la forma de responder «¿qué traía exactamente el fichero?» sin depender de lo que se cargó:

```bash
. /nfq/data/cfg/env.properties
cd $processed/DIR_MEGARA/

ls -lat | grep -i "<INTERFAZ>" | head

# Ver el contenido sin descifrar a disco
gpg --decrypt <FICHERO>.xml.gpg | head -50

# Contar nodos de un tipo
gpg --decrypt <FICHERO>.xml.gpg | grep -c "<NombreNodo"

# Validar el archivado contra su XSD
gpg --decrypt <FICHERO>.xml.gpg > /tmp/rev.xml
xmllint --noout --schema /nfq/XMLconversor/xsd/<ESQUEMA>.xsd /tmp/rev.xml
rm /tmp/rev.xml
```

Descifrar requiere acceso a la clave privada correspondiente a `bk_stored`. Si no lo tienes, es una
petición de escalado, no algo que se resuelva sobre la marcha.

## ⚠ El archivado NO es el fichero original

Punto importante y fácil de pasar por alto: el archivado es la versión **posterior** a la
sustitución de separadores. El script hace `sed -i 's/!/¡/g'` sobre el fichero **antes** de
convertir, y `sed -i` edita en el sitio.

Así que el `.gpg` guardado contiene ya los `¡`. **El XML tal como lo mandó el origen no se conserva
en ningún sitio.** Ver [C05_sed_separador](../C%20-%20Conversion%20Java/C05_sed_separador.md).

Si hace falta el original íntegro para una reclamación, hay que pedírselo al emisor.

## Dos archivados distintos

No confundir los dos puntos donde se cifra y archiva:

| Qué se archiva | Dónde | Cuándo |
|---|---|---|
| **XML de entrada** | `$processed/DIR_MEGARA/` | Tras la conversión |
| **Plano ya cargado** | `$fileshare/DIR_PROCESSED/DIR_SAC/` etc. | Tras la carga a staging |

El primero lo hace `load_java_script.sh`; el segundo, `load_stgtrf_script.sh`. Ver
[D08_gpg_historificacion](../D%20-%20Carga%20STG/D08_gpg_historificacion.md).

## Cómo verificarlo

```bash
. /nfq/data/cfg/env.properties

# Últimos XML archivados
ls -lat $processed/DIR_MEGARA/ | head -20

# ¿Se archivó el de hoy de esta interfaz?
ls -la $processed/DIR_MEGARA/ | grep -i "<INTERFAZ>" | tail -3

# XML que quedaron sin convertir (conversión fallida)
ls -lat /prdmegara/PRD/Devices/MegaCommon/innotech/*.xml 2>/dev/null | head
```

## Ver también

[C02_load_java_script](../C%20-%20Conversion%20Java/C02_load_java_script.md) · [C05_sed_separador](../C%20-%20Conversion%20Java/C05_sed_separador.md) · [D08_gpg_historificacion](../D%20-%20Carga%20STG/D08_gpg_historificacion.md) · [B03_ciclo_de_vida_del_fichero](../B%20-%20Recepcion%20y%20flags/B03_ciclo_de_vida_del_fichero.md)

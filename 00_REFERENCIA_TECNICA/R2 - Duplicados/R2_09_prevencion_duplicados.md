---
titulo: "R2.09 — Qué provoca duplicados y cómo evitarlos"
familia: R2
etapa: "Transversal"
tipo: Runbook
tags:
  - familia/R2
  - etapa/transversal
  - tipo/runbook
keywords: "prevención, causas raíz, evitar duplicados, buenas prácticas, recurrencia"
---

# R2.09 — Qué provoca duplicados y cómo evitarlos

**Etapa:** Transversal
**Tipo:** Runbook
**Palabras clave:** prevención, causas raíz, evitar duplicados, buenas prácticas, recurrencia

## En una línea

Cinco causas explican prácticamente todos los duplicados del sistema, y tres de ellas se evitan con
disciplina operativa, no con cambios técnicos.

## Las cinco causas, por frecuencia

### 1. El archivado falló pero la carga fue bien

El script decide si archiva mirando la salida del `\COPY` con una comprobación frágil sobre el texto
`COPY nnn`. Si esa comprobación no acierta, el fichero **no se archiva** y se queda en el directorio
de trabajo. La siguiente pasada —a los 10 minutos— lo vuelve a cargar.

**Prevención:** vigilar el directorio de trabajo. Un fichero que sigue ahí después de una carga
correcta es una bomba de relojería.

```bash
. /nfq/data/cfg/env.properties
# Ficheros en el directorio de trabajo con más de 30 minutos
find $raiz -maxdepth 1 -type f -mmin +30 -ls
```

Ver [D08_gpg_historificacion](../D%20-%20Carga%20STG/D08_gpg_historificacion.md).

### 2. Relanzamiento sin comprobar el estado previo

Alguien relanza un bloque para desatascar un paso y arrastra cargas que ya se habían hecho.

**Prevención:** la comprobación de 30 segundos antes de relanzar, y relanzar el **paso** en vez del
bloque siempre que sea posible. Ver [R2_05_duplicados_por_relanzar](../R2%20-%20Duplicados/R2_05_duplicados_por_relanzar.md).

### 3. El origen reenvía

Contenido idéntico con nombre distinto, y el patrón del lookup casa con ambos.

**Prevención:** ninguna desde soporte. Se escala al origen. Lo que sí se puede hacer es
**detectarlo pronto**: dos ficheros casando el mismo patrón es visible antes de que carguen.

### 4. Patrón de fichero demasiado amplio

Un patrón como `S3_FIN_*.csv` puede capturar ficheros que no le correspondían.

**Prevención:** revisar el patrón cuando aparezcan nombres inesperados en `des_file_loaded`.

```sql
SELECT DISTINCT des_file_loaded
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_plan = :plan AND dat_load_date >= CURRENT_DATE - 30
ORDER  BY 1;
```

### 5. Duplicado real en el fichero de origen

El emisor manda la fila dos veces. Como staging no tiene claves ni detección, entra tal cual.

**Prevención:** ninguna en el sistema actual. Ver [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md).

## La causa estructural de fondo

Todo lo anterior duele más de lo que debería por una razón: **staging no tiene ninguna barrera**.
Sin claves primarias en las tablas de datos y sin la validación de claves activa, cualquier
duplicado —venga de donde venga— entra sin resistencia y sin dejar rastro.

En un sistema con clave primaria en staging, las causas 1, 2, 3 y 5 producirían un error inmediato
y visible en el momento de la carga, en lugar de un dato silenciosamente mal varias capas después.
Eso no es algo que soporte pueda cambiar, pero **sí explica por qué los duplicados aparecen tarde y
lejos de su origen**, y conviene tenerlo presente al diagnosticar.

## Checklist para no crear duplicados

Antes de cualquier relanzamiento o carga manual:

- [ ] ¿Hay ya una traza de carga correcta para este plan hoy?
- [ ] ¿Sigue el fichero en el directorio de trabajo?
- [ ] ¿Cuántos ficheros casan con el patrón ahora mismo?
- [ ] Si relanzo el bloque entero, ¿qué otras cargas arrastro?
- [ ] ¿La transformación afectada borra antes de insertar, o acumula?

Y después:

- [ ] ¿Cuántos `cod_load_trace` conviven ahora en la tabla?
- [ ] Si dupliqué, ¿limpié también aguas abajo?

## Qué merece escalarse como mejora

Estas tres no son incidencias, son observaciones estructurales que conviene que alguien recoja:

1. **`stg_s3` sin claves primarias** en las tablas de datos: nada detiene un duplicado.
2. **`validate_rows_key_fn` huérfana y con defectos**: existe pero no se invoca, y no funcionaría.
3. **La comprobación de archivado es frágil**: depende del formato exacto del mensaje de `psql`.

## Ver también

[R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md) · [R2_05_duplicados_por_relanzar](../R2%20-%20Duplicados/R2_05_duplicados_por_relanzar.md) · [D08_gpg_historificacion](../D%20-%20Carga%20STG/D08_gpg_historificacion.md) · [R2_07_limpiar_sin_romper](../R2%20-%20Duplicados/R2_07_limpiar_sin_romper.md) · [R2_04_archivo_llego_dos_veces](../R2%20-%20Duplicados/R2_04_archivo_llego_dos_veces.md)

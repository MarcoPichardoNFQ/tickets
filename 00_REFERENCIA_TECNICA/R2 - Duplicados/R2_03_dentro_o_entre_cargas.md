---
titulo: "R2.03 — Duplicado dentro del fichero vs. duplicado entre cargas"
familia: R2
etapa: "Validación"
tipo: Runbook
tags:
  - familia/R2
  - etapa/validacion
  - tipo/runbook
keywords: "duplicado intra-fichero, entre cargas, cod_load_trace, diagnóstico, clasificar"
---

# R2.03 — Duplicado dentro del fichero vs. duplicado entre cargas

**Etapa:** Validación
**Tipo:** Runbook
**Palabras clave:** duplicado intra-fichero, entre cargas, cod_load_trace, diagnóstico, clasificar

## Síntoma

Hay filas repetidas y hay que saber de dónde salen antes de decidir qué hacer.

## La pregunta que lo separa todo

**¿Las filas repetidas comparten `cod_load_trace` o no?**

```sql
SELECT <col_clave1>, <col_clave2>,
       count(*)                         AS repeticiones,
       count(DISTINCT cod_load_trace)   AS cargas_distintas,
       string_agg(DISTINCT cod_load_trace::text, ', ') AS traces
FROM   stg_s3.<TABLA>_T
GROUP  BY 1,2
HAVING count(*) > 1
ORDER  BY repeticiones DESC
LIMIT  20;
```

| `cargas_distintas` | Tipo | Causa |
|---|---|---|
| `1` | **Dentro del fichero** | El origen mandó la fila repetida |
| `> 1` | **Entre cargas** | El mismo dato entró en dos ejecuciones |

Son problemas distintos, con responsables distintos y arreglos distintos. No los mezcles.

## Caso A — duplicado dentro del fichero

Las dos filas llegaron en el mismo envío. Como staging no tiene claves ni detección, se cargaron
las dos. Ver [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md).

**Qué comprobar:** que el fichero original efectivamente las traía.

```bash
. /nfq/data/cfg/env.properties
# Descifra una copia del histórico y cuenta claves repetidas
# (ajusta separador y posiciones de las columnas clave)
gpg --decrypt FICHERO.gpg | awk -F'!' '{print $1"|"$2}' | sort | uniq -d | head
```

**Responsable:** el origen. Es un problema de calidad de dato en el emisor.
**Acción de soporte:** documentar, cuantificar y escalar. Limpiar en base de datos sin avisar al
origen garantiza que vuelva mañana.

## Caso B — duplicado entre cargas

El mismo dato entró dos veces en ejecuciones distintas. Las causas posibles son cuatro, en orden de
frecuencia:

1. **El fichero se procesó dos veces.** Ver [D13_cargo_dos_veces](../D%20-%20Carga%20STG/D13_cargo_dos_veces.md).
2. **Se relanzó un bloque** que ya había corrido. Ver [R2_05_duplicados_por_relanzar](../R2%20-%20Duplicados/R2_05_duplicados_por_relanzar.md).
3. **El archivado falló pero la carga fue bien**, así que el fichero se quedó en el directorio y la
   siguiente pasada lo recogió. Ver [D08_gpg_historificacion](../D%20-%20Carga%20STG/D08_gpg_historificacion.md).
4. **El origen reenvió el mismo contenido con otro nombre** y el patrón del lookup casa con ambos.

**Qué comprobar:**

```sql
-- Las dos cargas implicadas
SELECT cod_load_trace, cod_load_plan, dat_load_date,
       des_file_loaded, amt_register_process, step_load, cod_status
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_trace IN (:trace_a, :trace_b);
```

Si `des_file_loaded` es el mismo nombre en ambas, fue el mismo fichero procesado dos veces. Si son
nombres distintos con el mismo contenido, el origen reenvió.

**Acción de soporte:** aquí sí es legítimo limpiar, porque el dato duplicado lo generó el proceso,
no el origen. Borra siempre por `cod_load_trace`. Ver [R2_07_limpiar_sin_romper](../R2%20-%20Duplicados/R2_07_limpiar_sin_romper.md).

## Caso C — el que parece duplicado y no lo es

Algunas tablas **acumulan varias fechas o varias cargas a propósito**. Dos filas con la misma clave
de negocio pero distinta fecha no son un duplicado: son historia.

Antes de concluir nada, comprueba si la clave declarada incluye una columna de fecha:

```sql
SELECT c.des_column, c.data_type
FROM   stg_s3.par_maestro_columnas_t c
JOIN   stg_s3.par_maestro_tablas_t   t ON t.cod_table = c.cod_table
WHERE  t.des_table = UPPER('<TABLA>') AND c.chk_clave = 1
ORDER  BY c.cod_column;
```

Si la clave lleva fecha y tú agrupaste sin ella, tus «duplicados» son filas de días distintos.

## Cuándo escalar

- **Caso A** siempre: es calidad de dato en origen.
- **Caso B** si se repite: hay un problema estructural en el archivado o en la operativa de relanzado.
- **Caso C** nunca: cierra el ticket explicando la clave.

## Ver también

[R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md) · [D13_cargo_dos_veces](../D%20-%20Carga%20STG/D13_cargo_dos_veces.md) · [R2_07_limpiar_sin_romper](../R2%20-%20Duplicados/R2_07_limpiar_sin_romper.md) · [R2_08_consultas_duplicados](../R2%20-%20Duplicados/R2_08_consultas_duplicados.md)

---
titulo: "B07 — `controlflag_arquivos` y `controlflag_interfaces`"
familia: B
etapa: "Recepción de flags"
tipo: Referencia
tags:
  - familia/B
  - etapa/recepcion-de-flags
  - tipo/referencia
keywords: "controlflag_arquivos, controlflag_interfaces, recebido, track_status, id_camda, tmp_controlflag"
---

# B07 — `controlflag_arquivos` y `controlflag_interfaces`

**Etapa:** Recepción de flags
**Tipo:** Referencia
**Palabras clave:** controlflag_arquivos, controlflag_interfaces, recebido, track_status, id_camda, tmp_controlflag

## En una línea

Dos tablas: una fila por **flag recibido**, y una fila por **interfaz declarada dentro de ese flag**
con dos booleanos que responden si llegó y si el origen dijo que fue bien.

## `stg_s3.controlflag_arquivos` — una fila por flag

| Columna | Contenido |
|---|---|
| `id_camda` | Identificador del lote |
| `id` | Clave primaria (una de las tres que existen en todo `stg_s3`) |
| `nome_base` | Nombre del flag, ej. `MEGACUSTODY_IntraDay` |
| `nome_completo` | Nombre completo del fichero recibido |
| `data` | Fecha de registro, por defecto `now()` |
| `data_recebemento` | Fecha de modificación del fichero flag |

`nome_completo` y `data_recebemento` se rellenan con un `UPDATE` posterior. Si están en NULL, el
lote se abrió pero el script de flags no llegó a completarlo.

## `stg_s3.controlflag_interfaces` — una fila por interfaz declarada

| Columna | Contenido |
|---|---|
| `id_camda` | Lote |
| `id_arquivo_flag` | Siempre `1` (valor fijo en el script) |
| `nome_flag_geral` | Nombre base del flag |
| `nome_flag_completo` | Nombre completo del flag |
| `nome_interface_base` | Código de la interfaz, ej. `Bond` |
| `nome_interface_completo` | Nombre del fichero declarado |
| **`recebido`** | **¿Existe el fichero de verdad?** `false` por defecto |
| **`track_status`** | **¿El origen dijo `'Processd'`?** `false` por defecto |
| `begin_time`, `end_time` | Ventana de extracción en el origen, como **texto** |
| `data_recebemento` | Fecha del fichero, como **texto** |
| `data_fim_conversao` | Fin de conversión |

## Las dos columnas que responden todo

La combinación de `recebido` y `track_status` clasifica cualquier interfaz:

| `recebido` | `track_status` | Interpretación |
|---|---|---|
| `true` | `true` | **Todo bien.** Declarada, presente y sin incidencias en origen |
| `false` | `true` | **Falta el fichero.** El origen dice que lo mandó y no está |
| `true` | `false` | **Llegó, pero el origen reporta problema** en su extracción |
| `false` | `false` | Ni llegó ni el origen dice que fuera bien |
| `NULL` | cualquiera | Estado indeterminado: el script no llegó a completar la fila |

El segundo caso es el clásico «set incompleto» y el que dispara las alertas de cierre.
Ver [R4_05_flag_sin_xml](../R4%20-%20Sets%20incompletos/R4_05_flag_sin_xml.md).

## ⚠ Los tipos son texto

`begin_time`, `end_time` y `data_recebemento` están declaradas como `text`, no como `timestamp`.
Ordenar o comparar por ellas es comparación **alfabética**, no cronológica. Si necesitas ordenar de
verdad, convierte:

```sql
ORDER BY data_recebemento::timestamp
```

Y prepárate para que falle si algún valor no tiene formato de fecha. Es la razón por la que
conviene ordenar por `id_camda` siempre que sea posible.

## La tabla gemela: `trf_s3.tmp_controlflag_interfaces`

El script escribe la misma información en una segunda tabla, en otro esquema, con una columna
adicional: **`tamanho_interfaz`**, el tamaño en bytes del fichero recibido.

Es la única fuente que registra el tamaño, y sirve para detectar ficheros anómalamente pequeños
—un fichero de 200 bytes donde siempre hay 8 MB es un envío truncado— antes incluso de cargarlo:

```sql
SELECT nome_interface_base, tamanho_interfaz, data_recebemento
FROM   trf_s3.tmp_controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
ORDER  BY tamanho_interfaz::bigint NULLS FIRST
LIMIT  20;
```

Las dos inserciones se lanzan en segundo plano por separado, así que **pueden desincronizarse**: es
posible que una tabla tenga la fila y la otra no.

## Cómo verificarlo

```sql
-- Foto del lote actual
SELECT nome_flag_geral,
       count(*)                                            AS declaradas,
       count(*) FILTER (WHERE recebido)                    AS presentes,
       count(*) FILTER (WHERE NOT recebido)                AS ausentes,
       count(*) FILTER (WHERE NOT track_status)            AS con_aviso_origen
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
GROUP  BY 1;
```

## Ver también

[B06_load_filesflag_script](../B%20-%20Recepcion%20y%20flags/B06_load_filesflag_script.md) · [B08_id_camda_lote](../B%20-%20Recepcion%20y%20flags/B08_id_camda_lote.md) · [R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md) · [R4_10_consultas_que_falta](../R4%20-%20Sets%20incompletos/R4_10_consultas_que_falta.md)

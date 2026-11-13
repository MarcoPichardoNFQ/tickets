---
titulo: "R4.03 — `Validacion Cantidades Recibidas`"
familia: R4
etapa: "Recepción de flags"
tipo: Runbook
tags:
  - familia/R4
  - etapa/recepcion-de-flags
  - tipo/runbook
keywords: "Validacion Cantidades Recibidas, URGENTE, alerta, id_camda 29817, seis comprobaciones"
---

# R4.03 — `Validacion Cantidades Recibidas`

**Etapa:** Recepción de flags
**Tipo:** Runbook
**Palabras clave:** Validacion Cantidades Recibidas, URGENTE, alerta, id_camda 29817, seis comprobaciones

## En una línea

El job que dispara la alerta **«URGENTE no se recibieron todas las interfaces»**: suma seis
comprobaciones sobre el lote actual y avisa si el total no es cero.

## Las seis comprobaciones

Todas se ejecutan sobre el lote actual, excluyendo `Option`, `PricingRuleProfile`, `PricingRule` y
`OTCSwap`, y sus resultados se **suman**:

| # | Problema | Condición |
|---|---|---|
| 1 | No se incluyeron en el archivo Flag | Interfaces del lote actual que no están en el lote de referencia |
| 2 | El flag dice que llegaron pero realmente no | `recebido IS FALSE AND track_status IS TRUE` |
| 3 | El flag dice que algo pasó en el track_status | `track_status IS FALSE` |
| 4 | Recibido pero con fallo en el procesamiento | `recebido IS TRUE AND track_status IS FALSE` |
| 5 | Interfaces con estado indeterminado | `recebido IS NULL OR track_status IS NULL` |
| 6 | Interfaces duplicadas en el mismo lote | `GROUP BY flag, interfaz HAVING count(*) > 1` |

Si la suma es `0`, el job sale con éxito. Si no, imprime el detalle y la notificación `onfailure`
manda el correo urgente a una lista de trece destinatarios.

## ⚠ Tres cosas que hay que saber para interpretar la alerta

### El número no es un recuento de interfaces afectadas

Las comprobaciones **3 y 4 se solapan**: toda interfaz con `track_status IS FALSE` cuenta en la 3, y
si además tiene `recebido IS TRUE` cuenta otra vez en la 4. La misma interfaz puede sumar dos o tres
veces.

Trátalo como un **semáforo**, no como un contador. Para saber cuántas interfaces están realmente
afectadas y cuáles, usa la consulta de [R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md).

### El lote de referencia está codificado a fuego

La primera comprobación compara contra un lote histórico concreto:

```sql
comparison_batch_interfaces AS (
    SELECT DISTINCT nome_flag_geral, nome_interface_base
    FROM   stg_s3.controlflag_interfaces
    WHERE  id_camda = '29817'   -- ← número fijo en el código del job
      AND  nome_interface_base NOT IN (...)
)
```

### ✅ Qué es el lote 29817

```sql
SELECT count(*) AS interfaces, min(nome_flag_geral) AS flag
FROM   stg_s3.controlflag_interfaces WHERE id_camda = 29817;
```

**133 interfaces, flag `MEGAACCOUNTING_EndOfDay`.** Es una carga de fin de día completa.

Y ahí está el problema de fondo: la comparación agrupa por **`(nome_flag_geral, nome_interface_base)`**,
así que el nombre del flag entra en la clave. Un lote `MEGAACCOUNTING_IntraDay` no casa con ninguna
fila de una referencia `EndOfDay`, por muchas interfaces que compartan.

**Consecuencia:** para cualquier flag que no sea `MEGAACCOUNTING_EndOfDay`, esta comprobación
debería marcar como problema **todas** sus interfaces. Si el job alerta con regularidad en lotes
intradía, ésta es la explicación, y la alerta no significa que falte nada.

`29817` es un lote del pasado que alguien eligió como «el bueno». Implicaciones:

- Si el catálogo de interfaces cambia legítimamente —se añade una nueva—, esta comprobación la
  marcará como problema **para siempre**, hasta que alguien actualice el número.
- Si una interfaz se retira, la comparación deja de detectar su ausencia.
- Nadie recibe aviso de que la referencia ha envejecido.

Antes de investigar una alarma de tipo 1, comprueba qué es ese lote:

```sql
SELECT count(*) AS interfaces, min(nome_flag_geral) AS flag
FROM   stg_s3.controlflag_interfaces WHERE id_camda = 29817;
```

Si el conteo no se parece al de un lote actual, la referencia está obsoleta y la alarma es ruido.

### La dirección de la comparación

La comprobación 1 hace `lote_actual EXCEPT lote_referencia`: encuentra interfaces que están **hoy y
no** en la referencia — es decir, **nuevas**. Su etiqueta dice «No se incluyeron en el archivo
Flag», que describe lo contrario. Conviene leer el resultado por lo que la consulta hace, no por lo
que la etiqueta dice.

Para detectar las que faltan respecto a la referencia, la comparación es al revés:

```sql
SELECT nome_flag_geral, nome_interface_base
FROM   stg_s3.controlflag_interfaces WHERE id_camda = 29817
EXCEPT
SELECT nome_flag_geral, nome_interface_base
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq);
```

## Qué hacer cuando llega la alerta

1. **No asumas que faltan ficheros.** Cuatro de las seis comprobaciones no son sobre ausencia.
2. Lanza la consulta de [R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md) para ver qué interfaces están afectadas y por qué.
3. Clasifica: ¿falta el fichero, o llegó con aviso del origen, o es la comparación contra el lote fijo?
4. Sólo el caso «falta el fichero» exige reclamar al origen.

## La comparación con `"0"` sí funciona

El script compara la salida de `psql` con la cadena `"0"`, lo que sólo es fiable si la conexión
devuelve la salida sin formato. **Está confirmado que lo hace**: `db_config_gral.env` define

```bash
export DB_CONN='psql -t -A -h ... -p 5432 -d postgres -U ...'
```

`-t` suprime cabeceras y pie, `-A` desactiva el alineado. La comparación es correcta y **el job no
alerta a diario sin causa**. Si salta, es porque la suma de las seis comprobaciones dio distinto de
cero de verdad.

Lo que sigue siendo cierto es que **ese número no es un recuento de interfaces afectadas**, por el
solapamiento de las comprobaciones 3 y 4.

## Ver también

[R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md) · [R4_01_que_es_un_set_completo](../R4%20-%20Sets%20incompletos/R4_01_que_es_un_set_completo.md) · [R5_09_catalogo_alertas](../R5%20-%20Alertas%20Rundeck/R5_09_catalogo_alertas.md) · [B07_tablas_controlflag](../B%20-%20Recepcion%20y%20flags/B07_tablas_controlflag.md) · [H17_conteo_no_cuadra](../H%20-%20Cierre%20y%20Qlik/H17_conteo_no_cuadra.md)

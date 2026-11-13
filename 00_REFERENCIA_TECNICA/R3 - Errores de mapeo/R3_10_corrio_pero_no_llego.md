---
titulo: "R3.10 — El mapeo corrió pero el dato no llegó a destino"
familia: R3
etapa: "Mapeos"
tipo: Runbook
tags:
  - familia/R3
  - etapa/mapeos
  - tipo/runbook
keywords: "falta una fila concreta, JOIN, WHERE, ON CONFLICT, sobrescrito, lógica del mapeo"
---

# R3.10 — El mapeo corrió pero el dato no llegó a destino

**Etapa:** Mapeos
**Tipo:** Runbook
**Palabras clave:** falta una fila concreta, JOIN, WHERE, ON CONFLICT, sobrescrito, lógica del mapeo

## Síntoma

El mapeo se ejecutó sin error, la tabla destino tiene datos, pero **una fila concreta** que debería
estar no está — o está con un valor que no es el esperado.

## Los cuatro destinos posibles de una fila

Cuando una fila de origen no aparece igual en destino, sólo puede haber pasado una de estas cuatro
cosas:

| Mecanismo | Efecto | Cómo se detecta |
|---|---|---|
| `INNER JOIN` que no casa | La fila **no entra** | Falta la clave en la tabla cruzada |
| `WHERE` de negocio | La fila **se filtra** | Cumple la condición de exclusión |
| `ON CONFLICT DO NOTHING` | La fila **se ignora** | Ya existía otra con su clave |
| `ON CONFLICT DO UPDATE` | La fila **sobrescribe** | El valor final es el del último en llegar |

Los dos últimos explican el caso «está, pero el importe es otro»: no falta la fila, la reemplazó otra
con la misma clave. Ver [R2_06_duplicados_en_mapeos](../R2%20-%20Duplicados/R2_06_duplicados_en_mapeos.md).

## Cómo diagnosticarlo

### 1. Confirma que la fila está en origen

```sql
SELECT * FROM trf_s3.<TABLA_ORIGEN> WHERE <clave_natural> = :valor;
```

Si no está, el problema es aguas arriba y no del mapeo. Ver [R3_08_dependencia_insatisfecha](../R3%20-%20Errores%20de%20mapeo/R3_08_dependencia_insatisfecha.md).

### 2. Lee la función del mapeo

No hay atajo. La lógica está en el SQL:

```sql
SELECT prosrc FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'exp_s3' AND p.proname = '<nome_fn_mapeio>';
```

Busca tres cosas, en este orden:

- **`INNER JOIN`** — anota con qué tablas cruza y por qué columnas
- **`WHERE`** — anota las condiciones de filtro
- **`ON CONFLICT`** — anota la clave y si es `DO UPDATE` o `DO NOTHING`

### 3. Comprueba los cruces uno a uno

Por cada `INNER JOIN` que hayas anotado:

```sql
SELECT count(*) FROM trf_s3.<TABLA_CRUZADA> WHERE <columna_de_cruce> = :valor_de_la_fila;
```

Cero resultados en cualquiera de ellos explica la ausencia: **la fila se cayó en ese cruce**.

Es, con diferencia, la causa más frecuente. Y suele ser un efecto dominó: la tabla cruzada está
incompleta porque su propia carga falló o descartó filas. Ver [R4_11_efecto_domino](../R4%20-%20Sets%20incompletos/R4_11_efecto_domino.md).

### 4. Comprueba los filtros

Evalúa a mano cada condición del `WHERE` contra los valores reales de la fila. Presta atención
especial a:

- **Filtros de fecha** — ¿la fila está dentro de la ventana?
- **Filtros de estado** — ¿el estado de la fila está entre los admitidos?
- **Filtros de pendientes** — ¿estaba marcada como pendiente de procesar?

### 5. Si es un problema de valor, no de ausencia

Busca si hay más de una fila de origen con la misma clave de destino:

```sql
SELECT <clave_destino>, count(*)
FROM   trf_s3.<TABLA_ORIGEN>
WHERE  <clave_destino> = :valor
GROUP  BY 1;
```

Más de una y un `ON CONFLICT DO UPDATE` en el mapeo = el valor final es el de la última procesada, y
el orden no está garantizado. Ver [R2_06_duplicados_en_mapeos](../R2%20-%20Duplicados/R2_06_duplicados_en_mapeos.md).

## El filtro permanente no es un descarte

Distinción importante para no perder tiempo: un `INNER JOIN` o un `WHERE` que excluye a un conjunto
de filas **todos los días** es una regla de negocio, no un fallo a reintentar. Reprocesar no la va a
meter nunca.

La señal es la estabilidad: si el mismo tipo de fila queda fuera cada día en proporción parecida y
nadie se ha quejado hasta ahora, es diseño. Ver [R1_10_descarte_correcto_sin_accion](../R1%20-%20Descartes/R1_10_descarte_correcto_sin_accion.md).

## Cuándo escalar

- Si el cruce falla porque falta un dato maestro: es una incidencia de la etapa que lo carga.
- Si la lógica del mapeo excluye algo que el negocio espera ver: hace falta quien conozca la regla.
  Soporte puede demostrar **qué** excluye la fila; decidir si eso es correcto no le corresponde.

## Ver también

[R3_05_mapeo_cero_filas](../R3%20-%20Errores%20de%20mapeo/R3_05_mapeo_cero_filas.md) · [R2_06_duplicados_en_mapeos](../R2%20-%20Duplicados/R2_06_duplicados_en_mapeos.md) · [R1_08_descartes_en_mapeos](../R1%20-%20Descartes/R1_08_descartes_en_mapeos.md) · [R4_11_efecto_domino](../R4%20-%20Sets%20incompletos/R4_11_efecto_domino.md) · [R3_01_anatomia_fallo_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_01_anatomia_fallo_mapeo.md)

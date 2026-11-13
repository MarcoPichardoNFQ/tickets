---
titulo: "R2.07 — Limpiar duplicados sin romper nada"
familia: R2
etapa: "Transversal"
tipo: Runbook
tags:
  - familia/R2
  - etapa/transversal
  - tipo/runbook
keywords: "limpiar, borrar, DELETE, cod_load_trace, propagación, aguas abajo, seguro"
---

# R2.07 — Limpiar duplicados sin romper nada

**Etapa:** Transversal
**Tipo:** Runbook
**Palabras clave:** limpiar, borrar, DELETE, cod_load_trace, propagación, aguas abajo, seguro

## En una línea

Borra siempre por `cod_load_trace`, comprueba antes lo que te vas a llevar, y recuerda que limpiar
staging no deshace lo que ya se propagó.

## La regla de oro

**`cod_load_trace` es el único criterio seguro de borrado.** Identifica exactamente «lo que entró en
esa ejecución». Cualquier otro criterio —fecha, rango de importes, condición de negocio— corre el
riesgo de llevarse filas legítimas que casualmente coinciden.

```sql
-- 1. Mira qué te vas a llevar
SELECT count(*) FROM stg_s3.<TABLA>_T WHERE cod_load_trace = :trace_sobrante;

-- 2. Míralo de verdad, unas cuantas filas
SELECT * FROM stg_s3.<TABLA>_T WHERE cod_load_trace = :trace_sobrante LIMIT 20;

-- 3. Sólo entonces
BEGIN;
DELETE FROM stg_s3.<TABLA>_T WHERE cod_load_trace = :trace_sobrante;
-- comprueba el conteo resultante antes de confirmar
SELECT count(*) FROM stg_s3.<TABLA>_T;
COMMIT;   -- o ROLLBACK si no cuadra
```

Usar transacción explícita no es paranoia: un `DELETE` sin `WHERE` correcto en producción no tiene
vuelta atrás.

## Cuál de los dos trace se borra

El **más reciente**, salvo que haya razón para lo contrario. El primero ya pudo propagarse aguas
abajo y tener dependencias; el segundo es el intruso.

```sql
SELECT cod_load_trace, dat_load_date, des_file_loaded, amt_register_process
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_trace IN (:a, :b)
ORDER  BY dat_load_date;
```

Si los dos tienen el mismo conteo de filas, es un reenvío puro y da igual cuál. Si difieren,
**quédate con el que tenga más filas**: probablemente el segundo trae correcciones.

## Lo que limpiar staging NO arregla

Éste es el error más caro. Borrar en `stg_s3` **no deshace** lo que ya se transformó ni lo que ya se
mapeó ni lo que ya se publicó en Qlik.

```
stg_s3   ← limpias aquí
   ↓
trf_s3   ← el duplicado sigue aquí
   ↓
trf_s3   ← y en la tabla de salida del mapeo
   ↓
Qlik     ← y esto es lo que ve el usuario
```

La secuencia correcta es de arriba abajo, comprobando en cada capa:

1. Limpia `stg_s3` por `cod_load_trace`.
2. Comprueba si el duplicado llegó a `trf_s3`. Si llegó, hay que reejecutar la transformación —o
   limpiar también allí, si el procedimiento no borra antes de insertar.
3. Comprueba la tabla de salida del mapeo (también en `trf_s3`) y reejecútalo.
4. Fuerza la recarga de la tarea de Qlik correspondiente.

Si te quedas en el paso 1, el usuario seguirá viendo el dato mal y el ticket volverá.

## Antes de borrar, comprueba las dependencias

```sql
-- ¿Llegó a la capa de negocio?  (sustituye por la tabla y clave reales)
SELECT count(*) FROM trf_s3.<TABLA> WHERE <clave> = :valor_duplicado;

-- ¿Y a la de salida?
SELECT count(*) FROM trf_s3.<TABLA_DESTINO> WHERE <clave> = :valor_duplicado;
```

Recuerda que en la capa de mapeos el duplicado puede no verse como filas de más sino como un valor
sobrescrito. Ver [R2_06_duplicados_en_mapeos](../R2%20-%20Duplicados/R2_06_duplicados_en_mapeos.md).

## Lo que no hay que hacer

- **No uses `DELETE` con `ctid`** ni trucos de «borrar todas menos una» sin haber identificado
  primero el `cod_load_trace`. Funcionan, pero dejan la tabla en un estado que nadie puede
  reconstruir después.
- **No borres de `_DES` a mano.** Esa tabla la gestiona `FN_REPROCESO_DESCART`, que la trunca
  entera. Ver [R1_09_reprocesar_descartes](../R1%20-%20Descartes/R1_09_reprocesar_descartes.md).
- **No borres sin dejar constancia.** Anota en el ticket la tabla, el `cod_load_trace`, el número de
  filas y la hora. Es la única forma de reconstruir qué pasó si el dato se echa de menos después.

## Cuándo escalar

- Si el duplicado ya llegó a la tabla de salida o a Qlik: la limpieza cruza capas y conviene coordinarla.
- Si hay que borrar en `trf_s3`: es el modelo de negocio, no una zona de aterrizaje.
- Si no está claro cuál de los dos `cod_load_trace` es el bueno.

## Ver también

[R2_03_dentro_o_entre_cargas](../R2%20-%20Duplicados/R2_03_dentro_o_entre_cargas.md) · [R2_05_duplicados_por_relanzar](../R2%20-%20Duplicados/R2_05_duplicados_por_relanzar.md) · [R2_06_duplicados_en_mapeos](../R2%20-%20Duplicados/R2_06_duplicados_en_mapeos.md) · [D13_cargo_dos_veces](../D%20-%20Carga%20STG/D13_cargo_dos_veces.md) · [R2_08_consultas_duplicados](../R2%20-%20Duplicados/R2_08_consultas_duplicados.md)

---
titulo: "R3.11 — Relanzar un mapeo con seguridad"
familia: R3
etapa: "Mapeos"
tipo: Runbook
tags:
  - familia/R3
  - etapa/mapeos
  - tipo/runbook
keywords: "relanzar, rerun, idempotente, ON CONFLICT, job individual, seguro"
---

# R3.11 — Relanzar un mapeo con seguridad

**Etapa:** Mapeos
**Tipo:** Runbook
**Palabras clave:** relanzar, rerun, idempotente, ON CONFLICT, job individual, seguro

## En una línea

Relanza **el job individual del mapeo**, nunca el orquestador completo — y comprueba antes si ese
mapeo acumula o sobrescribe.

## Antes de relanzar: tres comprobaciones

### 1. ¿Está activo?

```sql
SELECT id_mapeo, nome_fn_mapeio, activo_inactivo
FROM   exp_s3.tablas_mapeio_t WHERE id_mapeo = :id;
```

Relanzar un mapeo desactivado no hace nada.

### 2. ¿La causa del fallo está resuelta?

Si falló porque faltaba un dato de origen y sigue faltando, volverá a fallar. Comprueba primero el
origen.

### 3. ¿Acumula o sobrescribe?

Ésta es la comprobación que evita duplicar. Lee la función y busca cómo escribe:

```sql
SELECT prosrc FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'exp_s3' AND p.proname = '<nome_fn_mapeio>';
```

| Lo que encuentres al principio | Relanzar es |
|---|---|
| `DELETE FROM` o `TRUNCATE` del destino | **Seguro.** Borra y reconstruye |
| `INSERT ... ON CONFLICT DO UPDATE` | **Seguro.** Actualiza por clave |
| `INSERT ... ON CONFLICT DO NOTHING` | **Seguro.** Ignora lo que ya está |
| `INSERT` a secas, sin borrado previo | **Duplica.** No relances sin limpiar antes |

El último caso es minoritario pero existe. Si es el tuyo, cuenta las filas antes y después:

```sql
SELECT count(*) FROM trf_s3.<TABLA_DESTINO>;   -- antes y después
```

## Cómo relanzar

**El job individual**, en Rundeck, grupo `001 - JOBs Mapeos`, nombre `<id> mapeo_<tabla>`.

## Por qué no el orquestador completo

Relanzar `Mapeos` o `MapeosFlag` para recuperar un mapeo tiene tres efectos indeseables:

1. **Reejecuta decenas de mapeos** que ya habían terminado bien.
2. **Aumenta la concurrencia** justo cuando el problema suele ser la concurrencia. Si el fallo fue un
   deadlock, relanzar todo lo empeora. Ver [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md).
3. **Alarga el ciclo** y retrasa el cierre y la recarga de Qlik.

El job individual hace lo mismo para el mapeo que te interesa, en segundos y sin efectos colaterales.

## Después de relanzar

```sql
-- ¿Se pobló?
SELECT count(*) FROM trf_s3.<TABLA_DESTINO>;

-- ¿Quedó registrado algún error nuevo?
SELECT * FROM trf_s3.s3_control_errores_mapeo
WHERE  dat_proc_exe > NOW() - INTERVAL '15 minutes'
ORDER  BY dat_proc_exe DESC;
```

Y si el dato tiene que llegar al usuario hoy, **falta un paso**: la recarga de Qlik de esa tabla.
Reejecutar el mapeo actualiza `exp_s3`, no los tableros. Ver [H08_recarga_qlik](../H%20-%20Cierre%20y%20Qlik/H08_recarga_qlik.md).

## La secuencia completa de recuperación

Si el mapeo falló y hay que dejarlo todo correcto:

1. Resolver la causa (dato de origen, bloqueo, lo que fuera)
2. Relanzar el job individual del mapeo
3. Verificar el conteo del destino
4. Forzar la recarga de la tarea de Qlik correspondiente
5. Anotar en el ticket qué se relanzó y a qué hora

El paso 4 es el que más se olvida, y es el único que el usuario final percibe.

## Cuándo escalar

- Si el mapeo acumula y hay que limpiar antes: la limpieza en `exp_s3` afecta a la capa de salida.
- Si hay que relanzar varios mapeos con dependencias entre ellos: el orden importa y conviene
  planificarlo.

## Ver también

[R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md) · [R3_01_anatomia_fallo_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_01_anatomia_fallo_mapeo.md) · [R2_05_duplicados_por_relanzar](../R2%20-%20Duplicados/R2_05_duplicados_por_relanzar.md) · [H08_recarga_qlik](../H%20-%20Cierre%20y%20Qlik/H08_recarga_qlik.md) · [G04_jobs_mapeos](../G%20-%20Mapeos/G04_jobs_mapeos.md)

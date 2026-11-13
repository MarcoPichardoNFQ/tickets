---
titulo: "F10 — Un procedimiento TRF falló: cómo localizarlo"
familia: F
etapa: "Transformación TRF"
tipo: Runbook
tags:
  - familia/F
  - etapa/transformacion-trf
  - tipo/runbook
keywords: "fallo TRF, aud_log_trace_t, localizar, procedimiento, excepción no controlada"
---

# F10 — Un procedimiento TRF falló: cómo localizarlo

**Etapa:** Transformación TRF
**Tipo:** Runbook
**Palabras clave:** fallo TRF, aud_log_trace_t, localizar, procedimiento, excepción no controlada

## Síntoma

Un bloque acabó en rojo y el paso que falló era una transformación, o una tabla de `trf_s3` no se
actualizó.

## Qué mirar primero

```sql
SELECT dat_load_date, cod_load_plan, step_load, cod_status, des_log
FROM   stg_s3.aud_log_trace_t
WHERE  cod_status = -1
  AND  dat_load_date >= CURRENT_DATE
ORDER  BY dat_load_date DESC;
```

`cod_status = -1` marca los errores. **El campo `des_log` de una excepción contiene el error real de
PostgreSQL**, detrás del texto genérico:

```
Excepción no controlada. Consulte con el equipo de mantenimiento del aplicativo. Error: <causa real>
```

Léelo entero: la parte útil está al final.

## Identificar qué procedimiento era

El log da `cod_load_plan`. Para traducirlo a procedimiento:

```bash
grep '|<id>|' /nfq/data/cfg/lookup_trf.txt | cut -d'|' -f3
```

O al revés, si sabes la tabla y buscas el paso:

```bash
grep -i "<TABLA>" /nfq/data/cfg/lookup_trf.txt
```

En Rundeck, la descripción del paso del bloque también lo dice en texto plano:
`0040 - LOAD TRF TAX PAYER`. Ver [D07_bloques_optimizacio](../D%20-%20Carga%20STG/D07_bloques_optimizacio.md).

## Causas probables, por orden

**1. Falta el insumo.** La tabla de staging de la que lee está vacía o incompleta porque su carga
falló o descartó masivamente.

```sql
SELECT count(*) FROM stg_s3.<TABLA_ORIGEN>_T;

SELECT cod_load_trace, dat_load_date, cod_status, amt_register_process, des_process_executed
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_plan = :plan_de_la_carga
ORDER  BY dat_load_date DESC LIMIT 3;
```

**2. Violación de restricción.** A diferencia de staging, `trf_s3` **sí tiene claves primarias** —185
de sus ~638 tablas. Un duplicado que staging dejó pasar revienta aquí. Es el punto donde afloran los
duplicados de la etapa anterior. Ver [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md).

**3. Bloqueo o deadlock.** Con varios bloques en marcha, dos procedimientos pueden pisarse.
Ver [D12_carga_colgada](../D%20-%20Carga%20STG/D12_carga_colgada.md).

**4. Datos que rompen una conversión de tipo.** Un valor que pasó la validación de formato de
staging pero no encaja en el tipo destino.

**5. Dependencia de orden.** El procedimiento necesita que otro haya corrido antes. Los bloques están
numerados precisamente por eso. Ver [D07_bloques_optimizacio](../D%20-%20Carga%20STG/D07_bloques_optimizacio.md).

## Recuerda: el bloque no se detiene

Los `exit` del script están comentados. **Un fallo en el paso 12 no impide que corran el 13 y
siguientes.** Que un bloque acabe en rojo no dice dónde se paró, porque no se paró.

Consecuencia práctica: puede haber **varios** fallos en el mismo bloque. Revisa la lista completa,
no sólo el primero:

```sql
SELECT dat_load_date, cod_load_plan, des_log
FROM   stg_s3.aud_log_trace_t
WHERE  cod_status = -1 AND dat_load_date >= CURRENT_DATE
ORDER  BY dat_load_date;
```

Ver [D03_script_stg_trf](../D%20-%20Carga%20STG/D03_script_stg_trf.md).

## Si no hay nada en la traza

Dos explicaciones posibles antes de concluir que el procedimiento no corrió:

**El nivel de log lo está filtrando.**

```sql
SELECT * FROM stg_s3.par_maestro_log_level_t;
```

Un valor alto suprime los mensajes de detalle. Ver [E08_log_trace_niveles](../E%20-%20Parametrizacion/E08_log_trace_niveles.md).

**La comparación de error del script es poco fiable.** El script marca error si la salida de `psql`
no es exactamente `"0"`, cosa que puede no ocurrir nunca o ocurrir siempre según cómo esté definida
la conexión. Ver [F01_que_hace_la_capa_trf](../F%20-%20Transformacion%20TRF/F01_que_hace_la_capa_trf.md).

En ambos casos: **verifica contra los datos**.

```sql
SELECT count(*) FROM trf_s3.<TABLA_DESTINO>;
```

## Acción

1. Localiza el error real en `des_log`.
2. Comprueba el insumo en staging.
3. Si el insumo está bien y el error es de restricción, busca duplicados en origen.
4. Relanza el paso concreto, no el bloque entero, una vez resuelta la causa.
5. Comprueba el conteo del destino.

## Cuándo escalar

- Si el error apunta a un defecto en el procedimiento: es código, no configuración.
- Si hay que relanzar procedimientos con dependencias entre sí: el orden importa.

## Ver también

[F01_que_hace_la_capa_trf](../F%20-%20Transformacion%20TRF/F01_que_hace_la_capa_trf.md) · [E06_tablas_auditoria](../E%20-%20Parametrizacion/E06_tablas_auditoria.md) · [D07_bloques_optimizacio](../D%20-%20Carga%20STG/D07_bloques_optimizacio.md) · [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md) · [D12_carga_colgada](../D%20-%20Carga%20STG/D12_carga_colgada.md)

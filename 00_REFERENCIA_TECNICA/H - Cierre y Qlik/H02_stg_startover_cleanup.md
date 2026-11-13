---
titulo: "H02 — `STG StartOver` y `cleanup_meg_t()`"
familia: H
etapa: "Cierre y Qlik"
tipo: Referencia
tags:
  - familia/H
  - etapa/cierre-y-qlik
  - tipo/referencia
keywords: "STG StartOver, cleanup_meg_t, limpieza, tablas MEG, vaciado, ciclo"
---

# H02 — `STG StartOver` y `cleanup_meg_t()`

**Etapa:** Cierre y Qlik
**Tipo:** Referencia
**Palabras clave:** STG StartOver, cleanup_meg_t, limpieza, tablas MEG, vaciado, ciclo

## En una línea

El cierre vacía **todas** las tablas `meg_*t` de staging para dejar el sitio limpio al siguiente
ciclo — y por eso una tabla `MEG_*` vacía no es una incidencia.

## El procedimiento

```sql
CREATE PROCEDURE stg_s3.cleanup_meg_t(INOUT po_outcode integer)
...
FOR tabla_megara IN
    SELECT table_name FROM information_schema.tables
    WHERE  table_schema = 'stg_s3' AND table_name LIKE 'meg\_%t'
LOOP
    EXECUTE 'delete from stg_s3.' || tabla_megara;
END LOOP;
```

Tres cosas que definen su comportamiento:

**El alcance es dinámico.** No hay lista de tablas: recorre `information_schema` y vacía todo lo que
encaje con `meg_%t`. Una tabla nueva que se llame así entra automáticamente en el barrido.

**Usa `DELETE`, no `TRUNCATE`.** Más lento en tablas grandes y sujeto a bloqueos, pero respeta las
restricciones y se puede deshacer dentro de una transacción.

**Se traga los errores.** Su manejador captura cualquier excepción, imprime un aviso y devuelve
`-1`. No propaga el fallo. Una limpieza que falle a medias **deja unas tablas vacías y otras no**
sin detener el ciclo.

## Qué significa para el diagnóstico

**Una tabla `MEG_*` vacía después del cierre es normal.** Es la causa de falsos positivos más
habitual de esta etapa. Antes de investigar «se perdieron los datos», comprueba si la tabla entra en
el barrido:

```sql
SELECT table_name FROM information_schema.tables
WHERE  table_schema = 'stg_s3'
  AND  table_name LIKE 'meg\_%t'
  AND  table_name = lower('<TABLA>');
```

Si devuelve una fila, la tabla se vacía en cada cierre por diseño. Ver [D10_tabla_t_vacia](../D%20-%20Carga%20STG/D10_tabla_t_vacia.md).

**El dato no se pierde: ya está aguas abajo.** Cuando se ejecuta la limpieza, la información ya pasó
a `trf_s3` y a `exp_s3`. Staging es zona de paso.

**Una limpieza parcial sí es un problema.** Si falla a mitad, el ciclo siguiente arranca con datos
viejos en algunas tablas, y eso produce duplicados o mezclas difíciles de diagnosticar.

## Comprobación tras el cierre

```sql
-- ¿Quedaron tablas MEG con contenido después de la limpieza?
DO $$
DECLARE r record; n bigint;
BEGIN
  FOR r IN SELECT table_name FROM information_schema.tables
           WHERE table_schema='stg_s3' AND table_name LIKE 'meg\_%t'
  LOOP
    EXECUTE format('SELECT count(*) FROM stg_s3.%I', r.table_name) INTO n;
    IF n > 0 THEN RAISE NOTICE '% -> % filas', r.table_name, n; END IF;
  END LOOP;
END $$;
```

Tras un cierre correcto no debería reportar nada. Si reporta tablas con filas, la limpieza no
terminó.

## El job

`STG StartOver` (uuid `21a33050-30ee-4558-8484-a8677d3cb7b6`) se invoca desde el flujo de cierre de
`0999 -. Optimizacao Blocos Rundeck V6`.

**No tiene notificación configurada**: si falla, nadie se entera. Ver [R5_02_jobs_sin_notificacion](../R5%20-%20Alertas%20Rundeck/R5_02_jobs_sin_notificacion.md).
Es uno de los puntos ciegos que justifica la verificación manual del checklist diario.

## Ver también

[D10_tabla_t_vacia](../D%20-%20Carga%20STG/D10_tabla_t_vacia.md) · [H10_cierre_no_completado](../H%20-%20Cierre%20y%20Qlik/H10_cierre_no_completado.md) · [R5_02_jobs_sin_notificacion](../R5%20-%20Alertas%20Rundeck/R5_02_jobs_sin_notificacion.md) · [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md)

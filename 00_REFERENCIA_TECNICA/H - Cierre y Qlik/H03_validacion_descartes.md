---
titulo: "H03 — El paso `Validacion Descartes`"
familia: H
etapa: "Cierre y Qlik"
tipo: Referencia
tags:
  - familia/H
  - etapa/cierre-y-qlik
  - tipo/referencia
keywords: "Validacion Descartes, RAISE NOTICE, _err, informativo, sin alerta"
---

# H03 — El paso `Validacion Descartes`

**Etapa:** Cierre y Qlik
**Tipo:** Referencia
**Palabras clave:** Validacion Descartes, RAISE NOTICE, _err, informativo, sin alerta

## En una línea

Barre todas las tablas `_err` de `trf_s3` buscando duplicados de hoy — pero **sólo escribe mensajes
en el log: no falla, no alerta, y nadie lee su resultado**.

## Qué hace

Un bloque `DO` que recorre las tablas de mapeo con duplicados apartados:

```sql
FOR table_name IN
    SELECT t.table_name FROM information_schema.tables t
    WHERE  t.table_schema = 'trf_s3' AND t.table_name LIKE '%_err'
LOOP
    query := format(
      'SELECT EXISTS (SELECT 1 FROM trf_s3.%I WHERE dat_qlikupdate::date = CURRENT_DATE);',
      table_name);
    EXECUTE query INTO result;
    IF result THEN
        RAISE NOTICE 'Tabla % Contiene por lo menos 1 regitro descartado para el día de hoy', table_name;
        all_ok := FALSE;
    END IF;
END LOOP;

IF all_ok THEN
    RAISE NOTICE 'Ningúna tabla contiene descartes el día de hoy.';
ELSE
    RAISE NOTICE 'Algunas tablas contienen información descartada, para mayor detalle contacte a
                  soporte BAU. Los registros serán eliminados periodicamente';
END IF;
```

## ⚠ Su salida no la comprueba nadie

```bash
V_Validacion=$($DB_CONN -c "$QueryValidacion")
```

Y ahí termina el script. **La variable no se examina, no hay `if`, no hay `exit` condicional.**

Consecuencias:

- El paso **nunca falla**, haya duplicados o no
- **No dispara ninguna alerta**
- Su resultado sólo existe como texto en el log de esa ejecución de Rundeck

Es un control informativo, no un control efectivo. Para saber si hubo duplicados hoy, hay que
consultar la base directamente.

## La consulta equivalente, que sí puedes usar

```sql
DO $$
DECLARE r record; n bigint;
BEGIN
  FOR r IN SELECT table_name FROM information_schema.tables
           WHERE table_schema = 'trf_s3' AND table_name LIKE '%\_err'
  LOOP
    EXECUTE format('SELECT count(*) FROM trf_s3.%I WHERE dat_qlikupdate::date = CURRENT_DATE',
                   r.table_name) INTO n;
    IF n > 0 THEN RAISE NOTICE '% -> % duplicados hoy', r.table_name, n; END IF;
  END LOOP;
END $$;
```

Lo mismo, pero con el conteo en vez de un booleano — que es lo que hace falta para dimensionar.

## Dos cosas que su mensaje revela

**«contacte a soporte BAU»** — el mensaje está escrito pensando en que lo lea un operador, no un
sistema. Confirma que el paso es informativo por diseño.

**«Los registros serán eliminados periodicamente»** — las tablas `_err` se purgan. **No son un
histórico fiable.** Si necesitas conservar evidencia de un duplicado, extráela antes.
Ver [G12_tablas_err_mapeos](../G%20-%20Mapeos/G12_tablas_err_mapeos.md).

## Qué hacer si aparecen duplicados

Un duplicado en `_err` significa que el mapeo hizo bien su trabajo: lo detectó y lo apartó. El
problema viene de más arriba, casi siempre de staging, donde nada lo impide.

Ver [G12_tablas_err_mapeos](../G%20-%20Mapeos/G12_tablas_err_mapeos.md) y [R2_03_dentro_o_entre_cargas](../R2%20-%20Duplicados/R2_03_dentro_o_entre_cargas.md) para el diagnóstico.

## Su sitio en el cierre

Se lanza en paralelo con los otros cuatro pasos de cierre, al terminar los mapeos.
Ver [H01_cerrar_el_lote](../H%20-%20Cierre%20y%20Qlik/H01_cerrar_el_lote.md) y [G07_ciclo_completo_mapeos](../G%20-%20Mapeos/G07_ciclo_completo_mapeos.md).

## Ver también

[G12_tablas_err_mapeos](../G%20-%20Mapeos/G12_tablas_err_mapeos.md) · [H01_cerrar_el_lote](../H%20-%20Cierre%20y%20Qlik/H01_cerrar_el_lote.md) · [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md) · [R5_02_jobs_sin_notificacion](../R5%20-%20Alertas%20Rundeck/R5_02_jobs_sin_notificacion.md) · [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md)

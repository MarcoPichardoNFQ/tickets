---
titulo: "H04 — `Procedimiento control finalizacion mapeos`"
familia: H
etapa: "Cierre y Qlik"
tipo: Referencia
tags:
  - familia/H
  - etapa/cierre-y-qlik
  - tipo/referencia
keywords: "finalización, actualizar_tablas_y_control, cierre, variante Flag, por cliente"
---

# H04 — `Procedimiento control finalizacion mapeos`

**Etapa:** Cierre y Qlik
**Tipo:** Referencia
**Palabras clave:** finalización, actualizar_tablas_y_control, cierre, variante Flag, por cliente

## En una línea

El paso que registra el cierre del ciclo — y uno de los pocos del cierre que produce una señal
accionable.

## Las dos variantes

| Job                                              | Llama a                                    | Flujo               |
| ------------------------------------------------ | ------------------------------------------ | ------------------- |
| `Procedimiento control finalizacion mapeos`      | `exp_s3.actualizar_tablas_y_control()`     | General             |
| `Procedimiento control finalizacion mapeos Flag` | `exp_s3.actualizar_tablas_y_controlflag()` | Gobernado por flags |

Son **dos de las cuatro funciones de `exp_s3` con llamador confirmado**. Ver [G10_codigo_sin_llamadas](../G%20-%20Mapeos/G10_codigo_sin_llamadas.md).

En los exports hay dos ficheros con el mismo nombre para la primera variante
(`Procedimiento_control_finalizacion_mapeos.xml` y `… (1).xml`). Conviene confirmar en Rundeck cuál
es la viva antes de basarse en una de ellas.

## Qué registra

Escribe en `trf_s3.s3_interface_control_t` y `s3_interface_control_xml_t`, cuya unidad es el
**cliente y la fecha de NAV**, no la interfaz:

```
cod_cli, dat_hr_nav, dat_hr_proc_meg, des_user_meg, dat_hr_proc_aldrin,
cod_error, des_error, cod_process, des_status
```

Y `des_status` es lo que decide qué llega a Qlik: sólo `Publish` y `WaitingFMValidation` se
publican. Ver [R4_04_s3_interface_control](../R4%20-%20Sets%20incompletos/R4_04_s3_interface_control.md).

## Cómo comprobar que corrió

```sql
SELECT cod_cli, dat_hr_nav, dat_hr_proc_aldrin, des_status, cod_error, des_error
FROM   trf_s3.s3_interface_control_xml_t
WHERE  dat_hr_proc_aldrin::date = CURRENT_DATE
ORDER  BY dat_hr_proc_aldrin DESC;
```

Sin filas de hoy, el cierre no llegó a escribir.

```sql
-- Clientes que cerraron con error
SELECT cod_cli, dat_hr_nav, cod_error, des_error, des_status
FROM   trf_s3.s3_interface_control_xml_t
WHERE  cod_error IS NOT NULL AND dat_hr_proc_aldrin >= CURRENT_DATE - 1
ORDER  BY dat_hr_proc_aldrin DESC;
```

```sql
-- Reparto de estados: cuántos clientes quedan fuera de Qlik
SELECT des_status, count(*) AS clientes, max(dat_hr_nav) AS ultimo_nav
FROM   trf_s3.s3_interface_control_xml_t
GROUP  BY 1 ORDER BY 2 DESC;
```

## Por qué importa que no cierre

**Un lote que no cierra puede impedir que el siguiente abra.** Y cuando eso pasa, los síntomas
aparecen al día siguiente y apuntan a sitios equivocados: «los mapeos no arrancan», «Qlik no se
actualiza».

Ante «hoy no ha arrancado nada», **comprueba siempre el cierre del ciclo anterior** antes de
investigar el arranque de hoy. Ver [H10_cierre_no_completado](../H%20-%20Cierre%20y%20Qlik/H10_cierre_no_completado.md) y [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md).

## Nota de cobertura

El cuerpo de `actualizar_tablas_y_control()` está en el volcado de funciones de `exp_s3`, pero su
lógica interna no se ha detallado en esta base. Para consultarla:

```sql
SELECT prosrc FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'exp_s3' AND p.proname LIKE 'actualizar_tablas%';
```

Lo documentado aquí procede de las llamadas visibles en los jobs y de la estructura real de las
tablas que alimenta.

## Ver también

[H01_cerrar_el_lote](../H%20-%20Cierre%20y%20Qlik/H01_cerrar_el_lote.md) · [R4_04_s3_interface_control](../R4%20-%20Sets%20incompletos/R4_04_s3_interface_control.md) · [H10_cierre_no_completado](../H%20-%20Cierre%20y%20Qlik/H10_cierre_no_completado.md) · [G10_codigo_sin_llamadas](../G%20-%20Mapeos/G10_codigo_sin_llamadas.md) · [H18_cliente_no_aparece](../H%20-%20Cierre%20y%20Qlik/H18_cliente_no_aparece.md)

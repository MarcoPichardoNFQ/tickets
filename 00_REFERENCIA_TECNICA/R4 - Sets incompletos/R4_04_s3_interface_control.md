---
titulo: "R4.04 — El control de cierre: `s3_interface_control_t`"
familia: R4
etapa: "Cierre y Qlik"
tipo: Referencia
tags:
  - familia/R4
  - etapa/cierre-y-qlik
  - tipo/referencia
keywords: "s3_interface_control_t, cierre, conteo de interfaces, actualizar_tablas_y_control"
---

# R4.04 — El control de cierre: `s3_interface_control_t`

**Etapa:** Cierre y Qlik
**Tipo:** Referencia
**Palabras clave:** s3_interface_control_t, cierre, conteo de interfaces, actualizar_tablas_y_control

## En una línea

No es un contador de interfaces: es un **control de publicación por cliente y por fecha de valor
liquidativo**, y su columna `des_status` decide qué datos llegan a Qlik.

## Estructura real

```
trf_s3.s3_interface_control_t          trf_s3.s3_interface_control_xml_t
  cod_cli             varchar(50) NN     (las mismas nueve columnas)
  dat_hr_nav          timestamp   NN     + des_fnavtype  varchar(255)
  dat_hr_proc_meg     timestamp   NN
  des_user_meg        varchar(50) NN
  dat_hr_proc_aldrin  timestamp   NN
  cod_error           varchar(2)
  des_error           varchar(255)
  cod_process         varchar(255)
  des_status          varchar(255)
```

Una fila por **cliente y fecha de NAV**, con tres marcas de tiempo —la del NAV, la del proceso en
Mega y la del proceso en Aldrin—, un estado y un código de error.

> **Corrección.** El documento de arquitectura heredado describe estas tablas como un conteo de
> interfaces esperadas. No lo son: no hay ninguna columna de conteo ni de nombre de interfaz. La
> unidad es el cliente, no la interfaz.

## `des_status` es lo que de verdad importa

El script de carga de Qlik filtra por esta columna:

```sql
FROM   trf_s3.s3_interface_control_xml_t
WHERE  des_status IN ('Publish', 'WaitingFMValidation')
```

Y cruza por `cod_cli` exigiendo que la fecha del dato sea anterior o igual a `dat_hr_nav`.

**Consecuencia directa:** un cliente cuyo estado no sea `Publish` ni `WaitingFMValidation` **no
aparece en Qlik**, por mucho que sus datos estén correctamente cargados y mapeados. Y un dato con
fecha posterior a la `dat_hr_nav` de su cliente tampoco.

Ésta es la explicación de un síntoma que de otro modo desconcierta: «el dato está en la base y no
se ve en el tablero». Ver [H09_qlik_datos_de_ayer](../H%20-%20Cierre%20y%20Qlik/H09_qlik_datos_de_ayer.md).

```sql
-- ¿Por qué no se publica este cliente?
SELECT cod_cli, dat_hr_nav, dat_hr_proc_meg, dat_hr_proc_aldrin,
       des_status, cod_error, des_error
FROM   trf_s3.s3_interface_control_xml_t
WHERE  cod_cli = '<CLIENTE>'
ORDER  BY dat_hr_nav DESC
LIMIT  10;
```

```sql
-- Reparto de estados: cuántos clientes quedan fuera de Qlik
SELECT des_status, count(*) AS clientes, max(dat_hr_nav) AS ultimo_nav
FROM   trf_s3.s3_interface_control_xml_t
GROUP  BY 1 ORDER BY 2 DESC;
```

Todo lo que no sea `Publish` ni `WaitingFMValidation` es invisible para los tableros.

## Quién las alimenta

Los procedimientos `exp_s3.actualizar_tablas_y_control()` y `actualizar_tablas_y_controlflag()`,
invocados desde los jobs `Procedimiento control finalizacion mapeos` y su versión Flag. Son dos de
las cuatro funciones de `exp_s3` con llamador confirmado. Ver [G10_codigo_sin_llamadas](../G%20-%20Mapeos/G10_codigo_sin_llamadas.md).

Esto tiene una consecuencia operativa directa: **un lote que no cierra bloquea el siguiente ciclo
de forma silenciosa**. Los síntomas no apuntan al cierre sino a lo que viene después — mapeos que
no arrancan, Qlik que no se actualiza — y el diagnóstico se va por el camino equivocado.

### Cómo comprobar el cierre del día

```sql
SELECT cod_cli, dat_hr_nav, dat_hr_proc_aldrin, des_status, cod_error
FROM   trf_s3.s3_interface_control_xml_t
WHERE  dat_hr_proc_aldrin::date = CURRENT_DATE
ORDER  BY dat_hr_proc_aldrin DESC;
```

Sin filas de hoy, el cierre no llegó a escribir. Y para ver si algún cliente quedó con error:

```sql
SELECT cod_cli, dat_hr_nav, cod_error, des_error, des_status
FROM   trf_s3.s3_interface_control_xml_t
WHERE  cod_error IS NOT NULL
  AND  dat_hr_proc_aldrin >= CURRENT_DATE - 1;
```

### Las dos tablas y su diferencia

Son idénticas salvo por una columna: `s3_interface_control_xml_t` añade **`des_fnavtype`**, el tipo
de NAV. La versión `xml_t` es la que consulta Qlik.

## Relación con los otros controles

Son tres controles distintos en tres momentos, y no miden lo mismo:

| Momento | Control | Qué mide |
|---|---|---|
| Llegada | `controlflag_interfaces.recebido` | ¿Está el fichero en disco? |
| Tras recepción | `Validacion Cantidades Recibidas` | Seis comprobaciones sobre el lote |
| **Cierre** | `s3_interface_control_t` | ¿Se **procesaron** todas las esperadas? |

Un lote puede pasar los dos primeros y fallar el tercero: los ficheros llegaron, pero alguno no
llegó a procesarse por un fallo posterior de carga o transformación.

## Ver también

[R4_11_efecto_domino](../R4%20-%20Sets%20incompletos/R4_11_efecto_domino.md) · [R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md) · [R4_03_validacion_cantidades](../R4%20-%20Sets%20incompletos/R4_03_validacion_cantidades.md) · [H10_cierre_no_completado](../H%20-%20Cierre%20y%20Qlik/H10_cierre_no_completado.md)

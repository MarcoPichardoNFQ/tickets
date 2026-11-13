---
titulo: "H12 — La recarga de Qlik falló"
familia: H
etapa: "Cierre y Qlik"
tipo: Runbook
tags:
  - familia/H
  - etapa/cierre-y-qlik
  - tipo/runbook
keywords: "recarga fallida, sin alerta, QVD, Qlik, punto ciego, tablero desactualizado"
---

# H12 — La recarga de Qlik falló

**Etapa:** Cierre y Qlik
**Tipo:** Runbook
**Palabras clave:** recarga fallida, sin alerta, QVD, Qlik, punto ciego, tablero desactualizado

## En una línea

Rundeck lanza la recarga y se desentiende: **si Qlik falla durante la recarga, no lo alerta nadie** —
ni Rundeck, ni Qlik, ni la base de datos.

## Por qué es un punto ciego

El paso «Recarga Qlik» hace un POST a la API de Qlik y termina:

```bash
curl ... -X POST "$url"
echo "Task $nom_task lanzada"
exit 0
```

**No comprueba el resultado.** El `exit 0` es incondicional. Y una vez lanzada la tarea, Qlik ejecuta
el script de carga por su cuenta: si falla a mitad, Rundeck ya terminó y no se entera.

Resultado: **los tableros se quedan con los datos del QVD anterior** y el ciclo entero aparece en
verde. Es el fallo silencioso más cercano al usuario final de todo el sistema.

## Síntoma

Un usuario reporta datos desactualizados en Qlik, y todo lo demás está correcto: el dato está en
`trf_s3`, el mapeo corrió, el cierre se completó y ningún job falló.

## Qué mirar, en orden

### 1. Confirma que el dato está publicado en la base

```sql
SELECT count(*) FROM trf_s3.<TABLA>;
SELECT max(dat_qlikupdate) FROM trf_s3.<TABLA>;
```

Si el dato no está aquí, el problema no es de Qlik. Ve a [H09_qlik_datos_de_ayer](../H%20-%20Cierre%20y%20Qlik/H09_qlik_datos_de_ayer.md).

### 2. Comprueba el estado de publicación del cliente

Aunque el dato esté, Qlik sólo carga clientes con el estado adecuado:

```sql
SELECT cod_cli, dat_hr_nav, des_status, cod_error, des_error
FROM   trf_s3.s3_interface_control_xml_t
WHERE  cod_cli = '<CLIENTE>'
ORDER  BY dat_hr_nav DESC LIMIT 5;
```

Sólo `Publish` y `WaitingFMValidation` llegan a los tableros. Ver [R4_04_s3_interface_control](../R4%20-%20Sets%20incompletos/R4_04_s3_interface_control.md).

### 3. Mira el historial de la tarea en Qlik

**Ésta es la comprobación que de verdad resuelve el caso**, y la única que ve el fallo.

En la consola de Qlik, historial de ejecuciones de `RecargadesdeRundeck`
(`a75bd6d3-d26b-41ec-8c88-1c29b1ff9202`). En condiciones normales se ejecuta de forma continua,
varias veces al día. Busca:

- Ejecuciones fallidas
- Una interrupción en la serie
- Duración anómala

### 4. Si la recarga falló, mira por qué

El script de carga de Qlik puede fallar por causas propias:

| Causa | Señal |
|---|---|
| Sin columnas declaradas para una tabla | El `LOAD` generado queda inválido. Ver [H07_lookup_qlik](../H%20-%20Cierre%20y%20Qlik/H07_lookup_qlik.md) |
| La conexión a la base falla | Error de `LIB CONNECT` |
| El QVD anterior no se puede leer | Error al cargar el fichero `.qvd` |
| Un cambio de columnas en `trf_s3` | El `SELECT` generado ya no casa |

La cuarta merece atención: el script construye su `SELECT` con las columnas de
`exp_s3.relaciontablacolumnas`. Si alguien añade o quita una columna en la tabla de origen sin
actualizar ese catálogo, la recarga se rompe **sin que nada más lo detecte**.

```sql
-- Columnas declaradas frente a columnas reales de la tabla
SELECT (SELECT count(*) FROM exp_s3.relaciontablacolumnas r
        WHERE lower(r.tabla) = lower('<TABLA>'))                     AS declaradas,
       (SELECT count(*) FROM information_schema.columns c
        WHERE c.table_schema = 'trf_s3' AND c.table_name = lower('<TABLA>')) AS reales;
```

El `lower()` es obligatorio en ambos lados. Ver [J10_trampas_conocidas](../J%20-%20Operacion/J10_trampas_conocidas.md).

## Compensar el punto ciego

Como no hay alerta, la única defensa es la comprobación activa. Añadida al checklist diario:

```sql
-- Tablas publicadas cuya última actualización no es de hoy
SELECT 'CART_POS_RF_T' AS tabla, max(dat_qlikupdate) FROM trf_s3.cart_pos_rf_t
UNION ALL
SELECT 'SAC_PL_CL_PATRRF_T', max(dat_qlikupdate) FROM trf_s3.sac_pl_cl_patrrf_t;
-- …añade las tablas que más se consultan en tu entorno
```

Y en Qlik, revisar el historial de la tarea como parte de la verificación de cierre.

## Acción

1. Confirma que el dato está en `trf_s3` y que el cliente tiene estado publicable.
2. Revisa el historial de la tarea en Qlik.
3. Si falló, identifica la causa con la tabla de arriba.
4. Relanza la tarea desde la consola de Qlik.
5. Confirma con el usuario que el tablero ya refleja el dato.

## Cuándo escalar

- Si la recarga falla de forma repetida: hay una causa estructural, normalmente un desajuste de
  columnas entre `trf_s3` y `relaciontablacolumnas`.
- Si no tienes acceso a la consola de Qlik para ver el historial o relanzar: es el escalado más
  frecuente de esta familia.

Y como observación de mejora, con nombre propio: **un fallo de recarga de Qlik no genera ninguna
alerta en todo el sistema**. Es el único tramo del flujo sin ninguna cobertura, y es el que ve el
usuario final.

## Ver también

[H08_recarga_qlik](../H%20-%20Cierre%20y%20Qlik/H08_recarga_qlik.md) · [H09_qlik_datos_de_ayer](../H%20-%20Cierre%20y%20Qlik/H09_qlik_datos_de_ayer.md) · [R4_04_s3_interface_control](../R4%20-%20Sets%20incompletos/R4_04_s3_interface_control.md) · [H07_lookup_qlik](../H%20-%20Cierre%20y%20Qlik/H07_lookup_qlik.md) · [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md)

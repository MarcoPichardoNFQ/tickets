---
titulo: "H13 — ⚠ Las fechas de corte codificadas en el script de Qlik"
familia: H
etapa: "Cierre y Qlik"
tipo: Referencia
tags:
  - familia/H
  - etapa/cierre-y-qlik
  - tipo/referencia
keywords: "fecha de corte, hardcoded, 2025-08-01, histórico, no se refresca"
---

# H13 — ⚠ Las fechas de corte codificadas en el script de Qlik

**Etapa:** Cierre y Qlik
**Tipo:** Referencia
**Palabras clave:** fecha de corte, hardcoded, 2025-08-01, histórico, no se refresca

## En una línea

El script de Qlik lleva **fechas fijas escritas en el código** que limitan qué se recarga desde la
base — y lo anterior a esas fechas ya sólo vive en el QVD.

## Las fechas

| Sección | Filtro al leer el QVD | Filtro al leer de la base |
|---|---|---|
| 1 (16 tablas) | `>= '2025-08-01'` | `>= '2024-12-31'` |
| 2 (2 tablas) | — | `>= '2025-08-01'` |
| 3 (21 tablas) | — | `>= '2025-03-01'` |

Aparecen literalmente en el script:

```sql
... AND tr.base_id = 0 AND date($(FieldData)) >= '2024-12-31';
... AND tr.base_id = 0 AND date($(FieldData)) >= '2025-08-01';
... AND tr.base_id = 0 AND date($(FieldData)) >= '2025-03-01';
```

## Qué implican

**Los datos anteriores al corte no se refrescan nunca desde la base.** Si una fila antigua se
corrige en `trf_s3`, esa corrección **no llega a Qlik**: el `SELECT` no la recoge.

Sólo sobrevive lo que ya estuviera en el QVD, y sólo si además supera el filtro de lectura del QVD.

**El filtro de lectura del QVD es más restrictivo que el de la base** en la sección 1: conserva
desde `2025-08-01` pero recarga desde `2024-12-31`. Es decir, entre esas dos fechas los datos se
reconstruyen enteros desde la base en cada recarga; antes de `2025-08-01`, lo que hubiera en el QVD
y no fuera de Megara se descarta.

**Envejecen solas.** Nadie avisa de que un corte se ha quedado atrás. Con el tiempo, el volumen que
se recarga desde la base crece sin límite, porque el corte no avanza.

## Cuándo aparece en un diagnóstico

Ante «corregimos el dato y en Qlik sigue mal»:

1. Comprueba que la corrección está en `trf_s3` y que su fecha de negocio **supera el corte**
2. Si es anterior al corte, **la recarga no la va a coger**: hay que actuar sobre el QVD o mover el corte

```sql
-- ¿La fila corregida entra en el rango que se recarga?
SELECT <campo_fecha>, count(*)
FROM   trf_s3.<TABLA>
WHERE  <clave> = '<valor>' AND base_id = 0
GROUP  BY 1;
```

Compara esa fecha con el corte de la sección que recorre esa tabla.

## Cómo saber qué corte aplica a una tabla

Busca la tabla en las listas `INLINE` del script: la sección donde aparezca determina su corte.
Ver [H06_script_carga_qlik](../H%20-%20Cierre%20y%20Qlik/H06_script_carga_qlik.md).

Ojo: **algunas tablas aparecen en dos secciones** —las listas 1 y 3 se solapan bastante— y en ese
caso se procesan dos veces, con cortes distintos, ganando la última.

## Material de escalado

Tres observaciones que merecen llegar a quien mantenga el script:

1. **Las fechas están codificadas y envejecen sin aviso.**
2. **Las secciones 1 y 3 se solapan**, procesando las mismas tablas dos veces con criterios
   distintos.
3. **Una corrección histórica anterior al corte no llega nunca a los tableros**, y no hay ninguna
   señal de ello.

## Ver también

[H06_script_carga_qlik](../H%20-%20Cierre%20y%20Qlik/H06_script_carga_qlik.md) · [H11_qvd_incremental](../H%20-%20Cierre%20y%20Qlik/H11_qvd_incremental.md) · [H12_recarga_qlik_fallo](../H%20-%20Cierre%20y%20Qlik/H12_recarga_qlik_fallo.md) · [I10_rastrear_hacia_atras](../I%20-%20Referencia%20de%20datos/I10_rastrear_hacia_atras.md)

---
titulo: "I10 — Rastrear un dato hacia atrás: «este número está mal»"
familia: I
etapa: "Transversal"
tipo: Runbook
tags:
  - familia/I
  - etapa/transversal
  - tipo/runbook
keywords: "dato erróneo, de dónde salió, hacia atrás, Qlik al fichero, valor incorrecto"
---

# I10 — Rastrear un dato hacia atrás: «este número está mal»

**Etapa:** Transversal
**Tipo:** Runbook
**Palabras clave:** dato erróneo, de dónde salió, hacia atrás, Qlik al fichero, valor incorrecto

## Síntoma

Un usuario reporta un valor incorrecto en un tablero. No falta: está mal.

## Por qué se hace al revés

Buscar hacia adelante desde el fichero exige saber qué fichero mirar. Yendo hacia atrás, cada paso
te dice cuál es el siguiente. Y en la mayoría de los casos el problema aparece en los dos o tres
primeros saltos.

## Los cinco saltos

### 1. ¿Qué tabla alimenta ese objeto de Qlik?

El script de carga de Qlik enlaza tabla, campo de fecha y QVD:

```
sac_pl_cl_patrrf_t, dat_pos, sac_qlik_pl_cl_patrrf_v
cart_pos_rf_t,      dat_hist, sac_qlik_cart_pos_rf_v
```

Y el catálogo de columnas dice qué se publica de cada tabla:

```sql
SELECT columna FROM exp_s3.relaciontablacolumnas
WHERE  lower(tabla) = lower('<TABLA>') ORDER BY 1;
```

Si la columna del valor erróneo **no está** en esa lista, no viene de ahí.

### 2. ¿El valor está mal en `trf_s3`?

```sql
SELECT * FROM trf_s3.<TABLA>
WHERE  <clave> = '<valor>' AND base_id = 0
ORDER  BY dat_qlikupdate DESC LIMIT 5;
```

| Resultado | Diagnóstico |
|---|---|
| El valor está mal aquí | Sigue hacia atrás → salto 3 |
| El valor está bien aquí | El problema es de **Qlik**: caché, QVD desactualizado, o el objeto no usa esta tabla → [H12_recarga_qlik_fallo](../H%20-%20Cierre%20y%20Qlik/H12_recarga_qlik_fallo.md) |

Ese segundo caso es más común de lo que parece: el QVD conserva datos antiguos si la recarga falló.

### 3. ¿Lo escribió mal el mapeo, o ya venía mal?

Localiza la función y mira el origen:

```sql
SELECT id_mapeo, nome_fn_mapeio FROM exp_s3.tablas_mapeio_t
WHERE  lower(nome_tabela_aldrin) = lower('<TABLA>');

SELECT prosrc FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'trf_s3' AND lower(p.proname) = lower('<nome_fn_mapeio>');
```

Dos causas típicas en esta capa:

**Sobrescritura.** Todas las funciones usan `ON CONFLICT … DO UPDATE`: si dos filas de origen
comparten clave, **gana la última procesada** y el orden no está garantizado. El síntoma es
exactamente «el importe no es el que esperaba». Ver [R2_06_duplicados_en_mapeos](../R2%20-%20Duplicados/R2_06_duplicados_en_mapeos.md).

```sql
-- ¿Hay más de una fila de origen para esa clave?
SELECT <clave>, count(*) FROM trf_s3.<TABLA_ORIGEN>
WHERE  <clave> = '<valor>' GROUP BY 1;
```

**Duplicado apartado.** Si el mapeo detectó repetidos, están en la tabla de descartes:

```sql
SELECT * FROM trf_s3.<TABLA>_err
WHERE  <clave> = '<valor>' ORDER BY dat_qlikupdate DESC;
```

### 4. ¿Ya venía mal de la transformación?

```sql
SELECT * FROM stg_s3.<TABLA>_T WHERE <clave> = '<valor>';
```

Si el valor ya está mal en staging, el problema es del fichero de origen. Si está bien, lo
introdujo la transformación: lee el procedimiento. Ver [I09_indice_tabla_origen](../I%20-%20Referencia%20de%20datos/I09_indice_tabla_origen.md).

### 5. ¿Qué traía el fichero?

El original está cifrado en el histórico:

```bash
. /nfq/data/cfg/env.properties
cd $processed/DIR_MEGARA/
ls -lat | grep -i "<INTERFAZ>" | head
gpg --decrypt <FICHERO>.xml.gpg | grep -i "<valor>"
```

**Ojo:** ese archivado es la versión **posterior** a la sustitución de `!` por `¡`. Si el valor
erróneo contiene ese carácter, es esa sustitución y no un error de dato. Ver [C05_sed_separador](../C%20-%20Conversion%20Java/C05_sed_separador.md).

## Tabla de resultados

| Último punto donde el valor está bien | Culpable |
|---|---|
| En ninguno: el fichero ya lo traía mal | **Origen** — reportar al cliente |
| `stg_s3` bien, `trf_s3` mal | La transformación |
| `trf_s3` origen bien, destino mal | El mapeo: sobrescritura o lógica |
| `trf_s3` bien, Qlik mal | La recarga o el propio tablero |

## Qué llevar al reporte

- El valor esperado y el observado, con la clave de negocio
- En qué capa deja de ser correcto
- Si hay más de una fila de origen para esa clave
- Si aparece en la tabla `_err` del mapeo
- Fecha y `cod_load_trace` de la carga implicada

Ver [J07_escalado](../J%20-%20Operacion/J07_escalado.md).

## Ver también

[I11_rastrear_un_fichero_e2e](../I%20-%20Referencia%20de%20datos/I11_rastrear_un_fichero_e2e.md) · [I09_indice_tabla_origen](../I%20-%20Referencia%20de%20datos/I09_indice_tabla_origen.md) · [R2_06_duplicados_en_mapeos](../R2%20-%20Duplicados/R2_06_duplicados_en_mapeos.md) · [H12_recarga_qlik_fallo](../H%20-%20Cierre%20y%20Qlik/H12_recarga_qlik_fallo.md) · [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md)

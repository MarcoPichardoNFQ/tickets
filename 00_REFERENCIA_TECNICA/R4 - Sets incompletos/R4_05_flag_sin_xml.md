---
titulo: "R4.05 — Llegó el flag pero faltan XMLs"
familia: R4
etapa: "Recepción de flags"
tipo: Runbook
tags:
  - familia/R4
  - etapa/recepcion-de-flags
  - tipo/runbook
keywords: "falta fichero, recebido false, set incompleto, reclamar al origen, interfaz ausente"
---

# R4.05 — Llegó el flag pero faltan XMLs

**Etapa:** Recepción de flags
**Tipo:** Runbook
**Palabras clave:** falta fichero, recebido false, set incompleto, reclamar al origen, interfaz ausente

## Síntoma

El flag se procesó, pero una o varias interfaces que declaraba no tienen su fichero.

## Qué mirar primero

```sql
SELECT nome_interface_base,
       nome_interface_completo,
       track_status,
       nome_flag_geral
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
  AND  NOT recebido
ORDER  BY nome_interface_base;
```

Cada fila es una interfaz que el origen declaró y cuyo fichero no estaba en disco cuando el script
lo comprobó.

## Confirma que sigue faltando

El script mira **una sola vez**, en el momento de procesar el flag. Un fichero que llegó cinco
minutos después queda registrado como ausente aunque hoy esté ahí.

```bash
. /nfq/data/cfg/env.properties
ls -la /prdmegara/PRD/Devices/MegaCommon/innotech/ | grep -i "<nome_interface_completo>"
```

| Resultado | Diagnóstico |
|---|---|
| No está | Falta de verdad → sigue con el runbook |
| Está, con hora **posterior** al flag | Llegada tardía → [R4_08_fuera_de_ventana](../R4%20-%20Sets%20incompletos/R4_08_fuera_de_ventana.md) |
| Está, con hora **anterior** al flag | El `find` no lo encontró: revisa el nombre exacto |

El tercer caso apunta a una discrepancia entre el `filename` declarado en el flag y el nombre real
del fichero. La búsqueda es `find -name "$filename*.xml"`, así que el nombre real debe **empezar
igual** que el declarado. Una diferencia de mayúsculas o un prefijo distinto lo hacen invisible.

## Causas probables, por orden

1. **El origen no generó el fichero** aunque lo declarara en el flag. Es la causa más frecuente y la
   que exige reclamación.
2. **Llegada tardía** — el fichero venía en camino cuando se procesó el flag.
3. **Fallo de transferencia** — el fichero se quedó a medias o no se copió.
4. **Discrepancia de nombre** entre lo declarado y lo enviado.
5. **El fichero llegó pero a otro directorio** — mira `DIR_UNMATCHED`. Ver [R4_07_dir_unmatched](../R4%20-%20Sets%20incompletos/R4_07_dir_unmatched.md).

## Acción

### 1. Dimensiona el impacto

¿Es una interfaz de catálogo de la que dependen muchas otras, o una interfaz terminal?

```sql
-- ¿Cuántas tablas dependen de la que falta? (aproximación por integridad declarada)
SELECT des_table, des_column
FROM   stg_s3.par_maestro_valid_t
WHERE  des_table_fk ILIKE '%<TABLA_DE_LA_INTERFAZ>%';
```

Si la interfaz ausente es un catálogo referenciado, el efecto se multiplica en forma de descartes de
clave foránea aguas abajo. Ver [R4_11_efecto_domino](../R4%20-%20Sets%20incompletos/R4_11_efecto_domino.md).

### 2. Comprueba si es habitual

```sql
SELECT id_camda, recebido, data_recebemento
FROM   stg_s3.controlflag_interfaces
WHERE  nome_interface_base = '<INTERFAZ>'
ORDER  BY id_camda DESC
LIMIT  20;
```

Si esa interfaz falta con regularidad, es un patrón conocido y probablemente ya esté asumido. Si es
la primera vez, es una incidencia nueva.

### 3. Decide: esperar, seguir o parar

Ver [R4_09_esperar_forzar_escalar](../R4%20-%20Sets%20incompletos/R4_09_esperar_forzar_escalar.md). Resumen: si el fichero es de un catálogo del que dependen
otros, conviene esperar; si es terminal, se puede dejar correr y reprocesar después.

### 4. Reclama al origen

Con estos datos, que son los que hacen que la reclamación no rebote:

- Nombre del flag y su hora de llegada
- `nome_interface_base` y `nome_interface_completo` declarados
- `id_camda`
- `beginExecutionTime` y `endExecutionTime` que el propio flag declaraba
- Confirmación de que el fichero no está en el directorio

```sql
SELECT nome_flag_completo, nome_interface_base, nome_interface_completo,
       begin_time, end_time, id_camda
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = :camda AND NOT recebido;
```

## Cuándo escalar

Siempre que falte el fichero de verdad: soporte no puede generarlo. La decisión que sí es de
soporte es **si se deja correr el ciclo o se espera**, y eso depende del punto 1.

## Ver también

[R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md) · [R4_09_esperar_forzar_escalar](../R4%20-%20Sets%20incompletos/R4_09_esperar_forzar_escalar.md) · [R4_11_efecto_domino](../R4%20-%20Sets%20incompletos/R4_11_efecto_domino.md) · [R4_08_fuera_de_ventana](../R4%20-%20Sets%20incompletos/R4_08_fuera_de_ventana.md) · [R4_07_dir_unmatched](../R4%20-%20Sets%20incompletos/R4_07_dir_unmatched.md)

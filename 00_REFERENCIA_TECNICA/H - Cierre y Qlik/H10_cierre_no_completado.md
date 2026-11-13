---
titulo: "H10 — El cierre no se completó, el lote quedó abierto"
familia: H
etapa: "Cierre y Qlik"
tipo: Runbook
tags:
  - familia/H
  - etapa/cierre-y-qlik
  - tipo/runbook
keywords: "cierre, lote abierto, finalizacion mapeos, s3_interface_control_t, bloqueo del siguiente ciclo"
---

# H10 — El cierre no se completó, el lote quedó abierto

**Etapa:** Cierre y Qlik
**Tipo:** Runbook
**Palabras clave:** cierre, lote abierto, finalizacion mapeos, s3_interface_control_t, bloqueo del siguiente ciclo

## Síntoma

El ciclo del día no llegó a cerrarse. Los síntomas visibles suelen aparecer **después**: mapeos que
no arrancan al día siguiente, Qlik sin actualizar, tablas de staging que no se limpiaron.

## Los pasos del cierre

```
STG StartOver                                → limpia las tablas MEG_*
Validacion Cantidades Recibidas              → comprueba la completitud del lote
Job control errores mapeo                    → comprueba errores de mapeo
_00001 Análise de erros                      → ⚠ anulado, no comprueba nada
Procedimiento control finalizacion mapeos    → cierra
Procedimiento control finalizacion mapeos Flag
Recarga Qlik                                 → paso dentro de otros jobs
```

## Qué mirar primero

### 1. ¿Se registró el cierre?

```sql
SELECT * FROM trf_s3.s3_interface_control_t     ORDER BY 1 DESC LIMIT 10;
SELECT * FROM trf_s3.s3_interface_control_xml_t ORDER BY 1 DESC LIMIT 10;
```

Sin registro del lote de hoy, el cierre no se completó. Ver [R4_04_s3_interface_control](../R4%20-%20Sets%20incompletos/R4_04_s3_interface_control.md).

### 2. ¿Se limpió staging?

```sql
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

Tablas `MEG_*` con contenido tras el cierre = `STG StartOver` no terminó. Ver [H02_stg_startover_cleanup](../H%20-%20Cierre%20y%20Qlik/H02_stg_startover_cleanup.md).

**Ojo:** ese job **no tiene notificación**. Si falla, nadie se entera. Ver [R5_02_jobs_sin_notificacion](../R5%20-%20Alertas%20Rundeck/R5_02_jobs_sin_notificacion.md).

### 3. ¿Cuadraba el conteo de interfaces?

El cierre está condicionado a que el número de interfaces procesadas coincida con el esperado. Si no
cuadra, no cierra.

```sql
SELECT nome_flag_geral,
       count(*)                             AS declaradas,
       count(*) FILTER (WHERE recebido)     AS presentes,
       count(*) FILTER (WHERE NOT recebido) AS faltan
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
GROUP  BY 1;
```

Un set incompleto es la causa más frecuente de un cierre que no completa. Ver [R4_01_que_es_un_set_completo](../R4%20-%20Sets%20incompletos/R4_01_que_es_un_set_completo.md).

### 4. ¿Quedaron mapeos sin terminar?

```sql
SELECT * FROM trf_s3.s3_control_errores_mapeo
WHERE  dat_proc_exe::date = CURRENT_DATE
ORDER  BY dat_proc_exe DESC;
```

## Por qué importa: bloquea el siguiente ciclo

Ésta es la razón por la que un cierre incompleto merece atención aunque parezca inofensivo: **un
lote que no cierra puede impedir que el siguiente abra**. Y cuando eso ocurre, los síntomas aparecen
al día siguiente y apuntan a sitios equivocados —«los mapeos no arrancan», «Qlik no se
actualiza»— mientras la causa está en el cierre de ayer.

Ante «hoy no ha arrancado nada», **comprueba siempre el cierre del ciclo anterior** antes de
investigar el arranque de hoy. Ver [G03_control_inicio_carga_mapeo](../G%20-%20Mapeos/G03_control_inicio_carga_mapeo.md) y [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md).

## Acción

1. Localiza en qué paso del cierre se detuvo, con las cuatro comprobaciones.
2. Si fue por set incompleto: la decisión es esperar el fichero o forzar. Ver [R4_09_esperar_forzar_escalar](../R4%20-%20Sets%20incompletos/R4_09_esperar_forzar_escalar.md).
3. Si fue por errores de mapeo: resuélvelos y relanza los mapeos afectados. Ver [R3_11_relanzar_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_11_relanzar_mapeo.md).
4. Si fue la limpieza: comprueba bloqueos y relánzala.
5. Verifica que el registro de cierre aparece antes de dar el ciclo por terminado.

## Cuándo escalar

- Si el cierre no completa dos días seguidos: el problema se acumula.
- Si hay que forzar el cierre de un lote incompleto: es una decisión con impacto en el dato
  publicado, y no le corresponde a soporte tomarla solo.

## Ver también

[R4_04_s3_interface_control](../R4%20-%20Sets%20incompletos/R4_04_s3_interface_control.md) · [H02_stg_startover_cleanup](../H%20-%20Cierre%20y%20Qlik/H02_stg_startover_cleanup.md) · [R4_09_esperar_forzar_escalar](../R4%20-%20Sets%20incompletos/R4_09_esperar_forzar_escalar.md) · [G03_control_inicio_carga_mapeo](../G%20-%20Mapeos/G03_control_inicio_carga_mapeo.md) · [R5_08_analise_de_erros_anulado](../R5%20-%20Alertas%20Rundeck/R5_08_analise_de_erros_anulado.md)

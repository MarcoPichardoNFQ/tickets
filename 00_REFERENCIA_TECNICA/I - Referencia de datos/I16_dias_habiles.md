---
titulo: "I16 — Días hábiles y feriados"
familia: I
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/I
  - etapa/transversal
  - tipo/referencia
keywords: "días hábiles, feriados, calendario, sac_stat_bas_cad_fer_t, no llegó nada"
---

# I16 — Días hábiles y feriados

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** días hábiles, feriados, calendario, sac_stat_bas_cad_fer_t, no llegó nada

## En una línea

Buena parte de los «hoy no ha llegado nada» son días no hábiles — y el sistema tiene su propio
calendario para saberlo.

## Los calendarios del sistema

Llegan como interfaces del conjunto oficial:

| Interfaz | Contenido |
|---|---|
| `CountryCalendar` | Calendario de país |
| `CSDCalendar` | Calendario del depositario |
| `MutualFundCalendar` | Calendario de fondos |
| `MainEntityCalendar` | Calendario de la entidad principal |

Y en la capa de salida, el mapeo `sac_stat_bas_cad_fer_t` publica los feriados hacia SAC.

```sql
SELECT * FROM trf_s3.sac_stat_bas_cad_fer_t
ORDER  BY 1 DESC LIMIT 20;
```

```sql
-- Qué funciones lo construyen
SELECT id_mapeo, nome_fn_mapeio, activo_inactivo
FROM   exp_s3.tablas_mapeio_t
WHERE  lower(nome_tabela_aldrin) LIKE '%cad_fer%';
```

En el repositorio hay varias variantes de su función: `function_meg_sac_stat_bas_cad_fer_4_t` y
`_8_t`. Ver [G06_catalogo_mapeos](../G%20-%20Mapeos/G06_catalogo_mapeos.md).

## Por qué importa para soporte

**Un día no hábil se parece mucho a una incidencia.** No llegan flags, no hay cargas, los bloques no
hacen nada y las tablas no se actualizan. Todo correcto, y ningún indicador lo dice.

Antes de investigar un «hoy no ha llegado nada», comprueba tres cosas en este orden:

### 1. ¿Es día hábil?

Fin de semana o festivo local en Brasil. Es la explicación más frecuente y la más rápida de
descartar.

### 2. ¿Esta interfaz llega hoy?

Muchas son semanales o mensuales. El histórico lo dice mejor que cualquier tabla teórica:

```sql
SELECT dat_load_date::date AS dia, count(*), sum(amt_register_process) AS filas
FROM   stg_s3.aud_load_trace_t
WHERE  cod_load_plan = :plan AND dat_load_date > CURRENT_DATE - 45
GROUP  BY 1 ORDER BY 1 DESC;
```

Si el patrón muestra huecos regulares en fines de semana, es calendario, no incidencia.

### 3. ¿Está el ciclo encendido?

Si es día hábil y aun así no llega nada, el sospechoso es el interruptor general:

```bash
cat /nfq/data/cfg/ArchivoAyudaRundeckMegara.txt
```

Cualquier cosa que no sea `1` detiene la petición de ficheros a Megara, **y el job sale en verde**.
Ver [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md).

## El desfase entre el calendario del sistema y el de soporte

El horario de BAU es de 4:00 a 23:00 de lunes a viernes. El sistema, en cambio, corre en bucle
continuo sin ventana nocturna. Consecuencia: **lo que ocurra entre las 23:00 y las 4:00 se descubre
por la mañana**, y el checklist diario es lo que lo destapa. Ver [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md) y
[J07_escalado](../J%20-%20Operacion/J07_escalado.md).

## Cuándo un feriado sí genera incidencia

Cuando el calendario del sistema y el real no coinciden: un festivo nuevo que no se ha cargado hace
que el sistema espere datos que nadie va a enviar, o que procese con una fecha de referencia
equivocada.

Síntoma: el proceso corre pero con la fecha de negocio del día anterior, o los mapeos filtran por
una fecha que no trae datos. Ver [R3_05_mapeo_cero_filas](../R3%20-%20Errores%20de%20mapeo/R3_05_mapeo_cero_filas.md).

## Ver también

[I14_calendario_ejecucion](../I%20-%20Referencia%20de%20datos/I14_calendario_ejecucion.md) · [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md) · [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md) · [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md) · [R1_10_descarte_correcto_sin_accion](../R1%20-%20Descartes/R1_10_descarte_correcto_sin_accion.md)

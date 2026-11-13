---
titulo: "H17 — El conteo de interfaces no cuadra"
familia: H
etapa: "Cierre y Qlik"
tipo: Runbook
tags:
  - familia/H
  - etapa/cierre-y-qlik
  - tipo/runbook
keywords: "conteo, no cuadra, cierre bloqueado, interfaces, lote incompleto"
---

# H17 — El conteo de interfaces no cuadra

**Etapa:** Cierre y Qlik
**Tipo:** Runbook
**Palabras clave:** conteo, no cuadra, cierre bloqueado, interfaces, lote incompleto

## Síntoma

El cierre no se completa, o la validación de cantidades alerta, porque el número de interfaces no
coincide con lo esperado.

## Primero: ¿qué conteo, exactamente?

Hay **tres definiciones de «completo»** conviviendo, y dan respuestas distintas sobre el mismo lote.
Antes de investigar, aclara cuál está fallando:

| Control | Compara contra | Ficha |
|---|---|---|
| Lista de ~130 prefijos | Ficheros en disco | [I06_catalogo_interfaces_mega](../I%20-%20Referencia%20de%20datos/I06_catalogo_interfaces_mega.md) |
| `controlflag_interfaces.recebido` | Lo que declaró el flag de hoy | [R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md) |
| `Validacion Cantidades Recibidas` | El lote histórico `29817` | [R4_03_validacion_cantidades](../R4%20-%20Sets%20incompletos/R4_03_validacion_cantidades.md) |

## Qué mirar, en orden

### 1. Lo que declaró el flag frente a lo que llegó

```sql
SELECT nome_flag_geral,
       count(*)                             AS declaradas,
       count(*) FILTER (WHERE recebido)     AS presentes,
       count(*) FILTER (WHERE NOT recebido) AS faltan
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
GROUP  BY 1;
```

Ésta es la comprobación objetiva: si `faltan > 0`, hay ficheros que el origen dijo mandar y no
están. Ver [R4_05_flag_sin_xml](../R4%20-%20Sets%20incompletos/R4_05_flag_sin_xml.md).

### 2. ¿Es la comparación contra el lote fijo?

El lote de referencia `29817` es un **`MEGAACCOUNTING_EndOfDay` con 133 interfaces**. Y la
comparación agrupa por `(nome_flag_geral, nome_interface_base)`, así que el nombre del flag entra en
la clave.

**Un lote intradía no casa con ninguna fila de una referencia de fin de día.** Para cualquier flag
que no sea `MEGAACCOUNTING_EndOfDay`, esa comprobación debería marcar todas sus interfaces.

```sql
SELECT count(*) AS interfaces, min(nome_flag_geral) AS flag
FROM   stg_s3.controlflag_interfaces WHERE id_camda = 29817;
```

Si el lote actual es de otro flag, la alerta es ruido. Ver [R4_03_validacion_cantidades](../R4%20-%20Sets%20incompletos/R4_03_validacion_cantidades.md).

### 3. ¿Se mezclaron dos llegadas?

Si el paso que abre el lote falló, las interfaces se registran con el `id_camda` anterior y el lote
aparece anormalmente grande:

```sql
SELECT id_camda, count(*) AS interfaces, min(nome_flag_geral) AS flag
FROM   stg_s3.controlflag_interfaces
GROUP  BY 1 ORDER BY 1 DESC LIMIT 15;
```

Un salto brusco frente a los lotes vecinos lo delata. Ver [B08_id_camda_lote](../B%20-%20Recepcion%20y%20flags/B08_id_camda_lote.md).

### 4. ¿Se completó el registro de cierre?

```sql
SELECT cod_cli, dat_hr_nav, dat_hr_proc_aldrin, des_status, cod_error
FROM   trf_s3.s3_interface_control_xml_t
WHERE  dat_hr_proc_aldrin::date = CURRENT_DATE
ORDER  BY dat_hr_proc_aldrin DESC;
```

Sin filas de hoy, el cierre no llegó a escribir. Ver [H04_procedimiento_finalizacion](../H%20-%20Cierre%20y%20Qlik/H04_procedimiento_finalizacion.md).

## Tabla de decisión

| Situación | Es… | Acción |
|---|---|---|
| `recebido = false` en interfaces reales | **Incidencia** | Reclamar los ficheros → [R4_05_flag_sin_xml](../R4%20-%20Sets%20incompletos/R4_05_flag_sin_xml.md) |
| Todo `recebido` y aun así alerta | **Ruido** del lote de referencia | Cerrar explicando |
| Lote anormalmente grande | Fallo al abrir lote | Revisar el paso de apertura |
| Sin registro de cierre | El cierre no corrió | [H10_cierre_no_completado](../H%20-%20Cierre%20y%20Qlik/H10_cierre_no_completado.md) |

## Por qué importa resolverlo pronto

Un lote que no cierra **puede impedir que el siguiente abra**, y entonces los síntomas aparecen al
día siguiente apuntando a otro sitio: «los mapeos no arrancan», «Qlik no se actualiza».

Ver [H10_cierre_no_completado](../H%20-%20Cierre%20y%20Qlik/H10_cierre_no_completado.md) y [R3_04_mapeo_no_arranco](../R3%20-%20Errores%20de%20mapeo/R3_04_mapeo_no_arranco.md).

## Cuándo escalar

- Si faltan ficheros de verdad: al cliente, con la lista concreta. Ver [J07_escalado](../J%20-%20Operacion/J07_escalado.md)
- Si hay que forzar el cierre de un lote incompleto: es una decisión con impacto en el dato
  publicado, y no le corresponde a soporte tomarla solo

## Ver también

[R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md) · [R4_03_validacion_cantidades](../R4%20-%20Sets%20incompletos/R4_03_validacion_cantidades.md) · [H10_cierre_no_completado](../H%20-%20Cierre%20y%20Qlik/H10_cierre_no_completado.md) · [R4_09_esperar_forzar_escalar](../R4%20-%20Sets%20incompletos/R4_09_esperar_forzar_escalar.md) · [I06_catalogo_interfaces_mega](../I%20-%20Referencia%20de%20datos/I06_catalogo_interfaces_mega.md)

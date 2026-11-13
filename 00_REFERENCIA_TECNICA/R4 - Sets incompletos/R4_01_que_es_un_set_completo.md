---
titulo: "R4.01 — Qué es un «set completo» y quién lo define"
familia: R4
etapa: "Recepción de flags"
tipo: Referencia
tags:
  - familia/R4
  - etapa/recepcion-de-flags
  - tipo/referencia
keywords: "set completo, lote, interfaces esperadas, declaración, quién decide"
---

# R4.01 — Qué es un «set completo» y quién lo define

**Etapa:** Recepción de flags
**Tipo:** Referencia
**Palabras clave:** set completo, lote, interfaces esperadas, declaración, quién decide

## En una línea

Hay **dos definiciones distintas de «completo»** conviviendo: una lista fija de ~130 prefijos
codificada en un script, y lo que cada flag declara en su interior.

## Detalle

### Definición 1 — la lista oficial de prefijos

El script `LLamada Rundeck Flags Obligatorios` lleva **codificada en su código una lista de ~130
prefijos obligatorios**: los 5 de flag y ~125 de interfaz, de `AccountCategory` a `YieldCurve`.

Es el catálogo maestro más parecido a «lo que debe llegar». Y gobierna el ciclo:

| Situación | Consecuencia |
|---|---|
| Están los ~130 | El lote anterior no se ha consumido: no se piden ficheros nuevos |
| Faltan algunos | **«ERROR CRÍTICO: Carga incompleta»**, el job aborta |
| No hay ninguno | Se piden ficheros nuevos a la API de Megara |

Ver [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md). Para consultarla:

```bash
grep -A45 "PREFIJOS=(" "/nfq/data/cfg/LLamada Rundeck Flags Obligatorios.sh"
```

### Definición 2 — lo que declara cada flag

Cada flag trae una lista de elementos `TrackInnotech`, uno por interfaz que el origen dice haber
generado. Esa lista **cambia de un lote a otro**: no todas las interfaces se generan siempre.

Contra esa declaración se comprueba fichero a fichero si está en disco, y el resultado va a
`controlflag_interfaces.recebido`. Ver [R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md).

### Y una tercera comparación, contra un lote histórico

`Validacion Cantidades Recibidas` compara el lote actual contra el `id_camda = 29817`, codificado en
el job. Ver [R4_03_validacion_cantidades](../R4%20-%20Sets%20incompletos/R4_03_validacion_cantidades.md).

### Por qué importa distinguirlas

Las tres pueden dar respuestas distintas sobre el mismo lote:

- La **lista de prefijos** dice si el conjunto oficial está en disco, sin mirar contenido ni flags.
- **`recebido`** dice si llegó lo que el flag de hoy declaró — que puede ser menos que la lista oficial.
- La **validación de cantidades** dice si el lote se parece a uno de referencia de hace tiempo.

Ante «¿está completo el lote?», la respuesta correcta empieza por **«¿completo según cuál de las
tres?»**. Para incidencias de ficheros ausentes, la útil es `recebido`.

### Los dos sentidos de «incompleto»

**Incompleto respecto al flag** — el flag declara `Bond` y `Bond_*.xml` no está en el directorio.
Es objetivo, medible y no admite discusión: falta un fichero que el origen dice haber mandado.

```sql
SELECT nome_interface_base, nome_interface_completo
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
  AND  NOT recebido;
```

**Incompleto respecto a lo habitual** — el flag ni siquiera declara `Bond`, cuando normalmente lo
declara. Esto el sistema **casi no lo detecta**: si el origen no lo declara, para el flag no falta
nada. Es el caso más difícil y el que más tarda en descubrirse, porque el control de recepción da
todo por bueno y el problema aflora días después en un informe.

Para ese segundo caso, la única defensa práctica es comparar con lotes anteriores.
Ver [R4_10_consultas_que_falta](../R4%20-%20Sets%20incompletos/R4_10_consultas_que_falta.md).

### Cuatro interfaces excluidas del control

La validación de cantidades excluye explícitamente:

```sql
nome_interface_base NOT IN ('Option', 'PricingRuleProfile', 'PricingRule', 'OTCSwap')
```

Esas cuatro **no cuentan** para el control de completitud, presumiblemente porque su llegada es
irregular por diseño. Que falten no dispara ninguna alarma. Si alguien pregunta por datos de esas
interfaces, el control automático no le va a servir de nada.

### Quién decide que un set está completo, en la práctica

| Momento | Mecanismo | Qué comprueba |
|---|---|---|
| Al llegar el flag | `load_filesflag_script.sh` | Fichero a fichero: ¿está en disco? |
| Tras la recepción | `Validacion Cantidades Recibidas` | Seis comprobaciones sobre el lote |
| Al cerrar el ciclo | Control de finalización | Conteo de interfaces frente a lo esperado |

Los tres miran cosas distintas y ninguno es completo por sí solo.

## Cómo verificarlo

```sql
-- Estado de completitud del lote actual
SELECT nome_flag_geral,
       count(*)                                 AS declaradas,
       count(*) FILTER (WHERE recebido)         AS presentes,
       count(*) FILTER (WHERE NOT recebido)     AS faltan,
       round(100.0 * count(*) FILTER (WHERE recebido) / count(*), 1) AS pct_completo
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
GROUP  BY 1;
```

## Ver también

[R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md) · [R4_03_validacion_cantidades](../R4%20-%20Sets%20incompletos/R4_03_validacion_cantidades.md) · [R4_05_flag_sin_xml](../R4%20-%20Sets%20incompletos/R4_05_flag_sin_xml.md) · [B01_que_es_un_flag](../B%20-%20Recepcion%20y%20flags/B01_que_es_un_flag.md)

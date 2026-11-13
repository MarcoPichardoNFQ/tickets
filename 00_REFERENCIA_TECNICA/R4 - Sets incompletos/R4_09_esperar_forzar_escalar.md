---
titulo: "R4.09 — Set incompleto: esperar, dejar correr o escalar"
familia: R4
etapa: "Recepción de flags"
tipo: Runbook
tags:
  - familia/R4
  - etapa/recepcion-de-flags
  - tipo/runbook
keywords: "decisión, esperar, forzar, escalar, catálogo, dependencias, criterio"
---

# R4.09 — Set incompleto: esperar, dejar correr o escalar

**Etapa:** Recepción de flags
**Tipo:** Runbook
**Palabras clave:** decisión, esperar, forzar, escalar, catálogo, dependencias, criterio

## En una línea

La decisión depende de una sola cosa: **si lo que falta es un catálogo del que dependen otras
tablas, o una interfaz terminal**.

## El criterio

```
¿Qué falta?
│
├── Un CATÁLOGO (otras tablas lo referencian)
│     → ESPERAR. Si se deja correr, todo lo que depende de él
│       se descarta masivamente por clave foránea.
│
└── Una interfaz TERMINAL (nadie la referencia)
      → DEJAR CORRER. El resto del lote se procesa con normalidad
        y esa interfaz entra cuando llegue.
```

### Cómo saber si es un catálogo

```sql
-- ¿Cuántas tablas referencian a ésta?
SELECT count(*) AS la_referencian
FROM   stg_s3.par_maestro_valid_t
WHERE  des_table_fk ILIKE '%<TABLA_DE_LA_INTERFAZ>%';
```

| Resultado | Naturaleza | Decisión |
|---|---|---|
| `0` | Terminal | Dejar correr |
| `1` – `3` | Dependencia acotada | Valorar: probablemente dejar correr y reprocesar |
| `> 3` | Catálogo troncal | **Esperar** |

Y la lista de los que más daño hacen si faltan, que conviene tener a mano:

```sql
SELECT des_table_fk, count(*) AS la_referencian
FROM   stg_s3.par_maestro_valid_t
WHERE  des_table_fk IS NOT NULL
GROUP  BY 1 ORDER BY 2 DESC LIMIT 20;
```

### El otro indicio: el número de bloque

Los bloques están numerados por dependencia. Una interfaz del bloque 1 o 2 es casi con seguridad un
catálogo del que dependen los bloques altos. Una del 7 es terminal. Ver [D07_bloques_optimizacio](../D%20-%20Carga%20STG/D07_bloques_optimizacio.md).

## Las tres opciones, en detalle

### Esperar

Se retrasa el ciclo hasta que llegue el fichero. Es lo correcto para catálogos.

**Coste:** el lote entero se retrasa, y con él la actualización de Qlik.
**A favor:** evita una cascada de descartes que después habría que reprocesar tabla por tabla.

Si esperas, avisa a quien consume el dato de que habrá retraso. Es preferible un dato tarde que un
dato incompleto que parece completo.

### Dejar correr

El ciclo procesa lo que hay. Lo que falta entra cuando llegue.

**Coste:** las tablas que dependían de lo ausente tendrán descartes de clave foránea, que habrá que
reprocesar después. Ver [R1_09_reprocesar_descartes](../R1%20-%20Descartes/R1_09_reprocesar_descartes.md).
**A favor:** el 95 % del lote llega a tiempo.

Es la opción correcta para interfaces terminales, y suele serlo también cuando la dependencia es
acotada y el reproceso es barato.

### Escalar

**Siempre** que falte el fichero, en paralelo a lo que decidas: soporte no puede generarlo.
Lo que decide soporte es esperar o dejar correr; conseguir el fichero es del origen.

Escala también cuando:

- Falta un catálogo troncal y esperar implica incumplir un compromiso de entrega.
- El mismo fichero falta varios días seguidos.
- Hay que forzar algo fuera de lo normal.

## Lo que no hay que hacer

**No crear un flag a mano.** Contamina el control de completitud y las validaciones de cierre.
Ver [R4_06_xml_sin_flag](../R4%20-%20Sets%20incompletos/R4_06_xml_sin_flag.md).

**No modificar `controlflag_interfaces`.** Maquilla la alerta y destruye la evidencia.
Ver [R4_08_fuera_de_ventana](../R4%20-%20Sets%20incompletos/R4_08_fuera_de_ventana.md).

**No relanzar el bloque «por si acaso».** Si el fichero no está, relanzar no lo trae, y sí puede
duplicar cargas que ya se hicieron. Ver [R2_05_duplicados_por_relanzar](../R2%20-%20Duplicados/R2_05_duplicados_por_relanzar.md).

## Qué anotar en el ticket

Con independencia de la decisión:

- `id_camda`, flag e interfaces afectadas
- Si es catálogo o terminal, y cuántas tablas dependen
- La decisión tomada y por qué
- Si se dejó correr: qué tablas quedan pendientes de reproceso

Ese último punto es el que más se olvida y el que más cuesta reconstruir después.

## Ver también

[R4_05_flag_sin_xml](../R4%20-%20Sets%20incompletos/R4_05_flag_sin_xml.md) · [R4_11_efecto_domino](../R4%20-%20Sets%20incompletos/R4_11_efecto_domino.md) · [R1_09_reprocesar_descartes](../R1%20-%20Descartes/R1_09_reprocesar_descartes.md) · [D07_bloques_optimizacio](../D%20-%20Carga%20STG/D07_bloques_optimizacio.md) · [E05_par_maestro_valid_t](../E%20-%20Parametrizacion/E05_par_maestro_valid_t.md)

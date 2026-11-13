---
titulo: "J07 — Qué resuelve BAU y qué se escala"
familia: J
etapa: "Transversal"
tipo: Runbook
tags:
  - familia/J
  - etapa/transversal
  - tipo/runbook
keywords: "escalado, alcance, cliente, horario, guardia, responsabilidades, análisis previo"
---

# J07 — Qué resuelve BAU y qué se escala

**Etapa:** Transversal
**Tipo:** Runbook
**Palabras clave:** escalado, alcance, cliente, horario, guardia, responsabilidades, análisis previo

## En una línea

BAU **siempre analiza primero**; después arregla lo que está en su mano y reporta, o reporta para
pedir ayuda — pero nunca reporta sin haber entendido el problema.

## Qué hace BAU

- Resolver incidencias técnicas
- Actualizaciones de código
- Responder dudas de funcionamiento
- Asegurar que todo funciona correctamente y de forma continua
- Analizar la información cuando el cliente comunica un error

## El proceso, en orden

```
1. Revisar internamente
2. Determinar la resolución
3. ¿Está dentro de las capacidades de BAU?
      SÍ  → arreglarlo, y después reportarlo
      NO  → reportarlo para esperar ayuda del cliente
```

**El análisis va siempre por delante del reporte.** Aunque la solución no esté en manos de BAU, hay
que entender qué pasa antes de escalarlo: se reporta el problema comprendido, no el síntoma.

Es la razón de ser de casi todas las fichas de diagnóstico de esta base: no son para arreglar, son
para **saber qué se está reportando**.

## Qué puede arreglar BAU y qué no

| Situación | ¿Lo resuelve BAU? | Qué se hace |
|---|---|---|
| **Faltan ficheros de insumo** | **No** | Nada se puede hacer aquí: el cliente tiene que enviar una **recarga histórica** |
| **Duplicados** | No — se corrigen en origen | Analizar el alcance y reportar al cliente para que corrija |
| **Descartes** | No — el dato viene mal | Analizar qué validación falló y por qué, y reportar |
| **Errores de carga** | Depende | Analizar; si es técnico y está en el alcance, arreglar y reportar |
| **Fallos técnicos del proceso** | **Sí** | Arreglar y reportar |
| **Dudas de funcionamiento** | **Sí** | Responder |

Las tres primeras filas tienen algo en común: **el arreglo está en el cliente, el análisis en BAU**.
Reportar «hay descartes» sin decir cuáles, cuántos, de qué validación y desde cuándo devuelve el
ticket. Reportar el diagnóstico completo lo resuelve.

## La cadena

```
BAU  →  escalado interno  →  cliente
```

Siempre en ese orden. No se salta el escalado interno.

## Horario

**De 4:00 a 23:00, de lunes a viernes.** Fuera de esa franja puede haber guardias.

Son 19 horas al día, lo que encaja con el ritmo del sistema: los orquestadores se despiertan cada 10
minutos y el vigilante de flags cada 3 segundos, así que el proceso no tiene ventana nocturna
propiamente dicha. Ver [A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md).

## Prioridad

**Todo es importante y no se puede dejar pasar nada.**

No hay una escala formal de criticidad que permita descartar avisos. Eso hace que la distinción
entre incidencia real y ruido conocido sea especialmente valiosa: no para ignorar cosas, sino para
no gastar el turno investigando lo que ya está explicado. Ver [J10_trampas_conocidas](../J%20-%20Operacion/J10_trampas_conocidas.md) y
[R1_10_descarte_correcto_sin_accion](../R1%20-%20Descartes/R1_10_descarte_correcto_sin_accion.md).

## Qué llevar a un reporte al cliente

Sea cual sea la incidencia, estos cinco datos evitan el rebote:

1. **Qué falta o qué está mal**, con nombres concretos: interfaz, tabla, fichero
2. **Cuánto**: número de filas, de interfaces, de ficheros
3. **Desde cuándo**, y si es la primera vez o se repite
4. **Qué se ha comprobado ya** y qué se ha descartado
5. **Qué se necesita del cliente**: recarga histórica, corrección en origen, alta de un maestro

Los runbooks de esta base terminan casi todos con una sección de escalado que enumera exactamente
esos datos para cada tipo de incidencia.

## Ver también

[J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md) · [J10_trampas_conocidas](../J%20-%20Operacion/J10_trampas_conocidas.md) · [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md) · [R1_12_descarte_masivo_escalado](../R1%20-%20Descartes/R1_12_descarte_masivo_escalado.md) · [R4_09_esperar_forzar_escalar](../R4%20-%20Sets%20incompletos/R4_09_esperar_forzar_escalar.md)

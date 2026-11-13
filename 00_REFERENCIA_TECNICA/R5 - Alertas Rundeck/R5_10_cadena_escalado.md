---
titulo: "R5.10 — De la alerta al escalado"
familia: R5
etapa: "Transversal"
tipo: Runbook
tags:
  - familia/R5
  - etapa/transversal
  - tipo/runbook
keywords: "escalado, alerta, triaje, qué hacer, cliente, interno"
---

# R5.10 — De la alerta al escalado

**Etapa:** Transversal
**Tipo:** Runbook
**Palabras clave:** escalado, alerta, triaje, qué hacer, cliente, interno

## En una línea

Llega una alerta: **analizar siempre primero**, y sólo entonces arreglar y reportar, o reportar para
pedir ayuda.

## El proceso

```
Alerta
  ↓
1. ¿Es ruido conocido?           → cerrar citando la ficha
  ↓ no
2. Analizar hasta entenderlo     ← esto no se salta nunca
  ↓
3. ¿Está en el alcance de BAU?
      SÍ  → arreglar, después reportar
      NO  → reportar para esperar ayuda del cliente
```

**El análisis va siempre por delante del reporte**, incluso cuando la solución no está en manos de
BAU. Se reporta el problema comprendido, no el síntoma. Ver [J07_escalado](../J%20-%20Operacion/J07_escalado.md).

## Paso 1 — Descartar el ruido conocido

Las causas de falso positivo, por frecuencia:

| Señal | Suele ser | Ficha |
|---|---|---|
| `PASO OMITIDO` en un bloque | Interfaz que hoy no tocaba | [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md) |
| `URGENTE no se recibieron…` sin ficheros ausentes | Comparación contra el lote fijo `29817` | [R4_03_validacion_cantidades](../R4%20-%20Sets%20incompletos/R4_03_validacion_cantidades.md) |
| `ERROR EN MAPEO` con la tabla poblada | Deadlock que el reintento resolvió | [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md) |
| Traza `Tabla Truncada` | Mensaje fijo, no se truncó nada | [R1_04_descarte_nulo_obligatorio](../R1%20-%20Descartes/R1_04_descarte_nulo_obligatorio.md) |
| Avalancha del mismo job | El vigilante, que corre cada 3 s | [B04_job_validacion_constante](../B%20-%20Recepcion%20y%20flags/B04_job_validacion_constante.md) |

Ver [J10_trampas_conocidas](../J%20-%20Operacion/J10_trampas_conocidas.md).

## Paso 2 — Analizar

Sitúa la incidencia en una etapa con [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md) y aplica la ficha de esa
familia. El objetivo es responder cuatro preguntas:

- **Qué** falla, con nombres concretos: interfaz, tabla, cliente, fichero
- **Cuánto**: filas, interfaces, ficheros
- **Desde cuándo**, y si es la primera vez o se repite
- **Por qué**, o hasta dónde has llegado

## Paso 3 — Decidir el destino

| Tipo de problema | ¿BAU lo resuelve? | Destino |
|---|---|---|
| Fallo técnico del proceso | **Sí** | Arreglar y reportar |
| Duda de funcionamiento | **Sí** | Responder |
| **Faltan ficheros de insumo** | No | Cliente: hace falta **recarga histórica** |
| **Duplicados** | No | Cliente, para que corrija en origen |
| **Descartes por dato incorrecto** | No | Cliente |
| Cambio de parametrización (`PAR_*`) | No | Responsable del contrato de datos |
| Permisos o administración de Qlik | No | Administrador de Qlik |
| Activar o desactivar un mapeo | No | Decisión funcional |

Las tres primeras filas de «No» tienen algo en común: **el arreglo está en el cliente, el análisis
en BAU**.

## La cadena

```
BAU  →  escalado interno  →  cliente
```

Siempre en ese orden. No se salta el escalado interno.

## Qué llevar al reporte

Cinco datos que evitan el rebote:

1. **Qué** falta o está mal, con nombres concretos
2. **Cuánto**
3. **Desde cuándo**, y si se repite
4. **Qué se ha comprobado** y qué se ha descartado
5. **Qué se necesita** del cliente

Y los identificadores del sistema que permiten reconstruirlo: `cod_load_trace`, `id_camda`,
`id_mapeo`, `cod_cli` — según la etapa.

## Cuándo escalar sin terminar el análisis

Sólo en dos casos:

- **El vigilante de presencia está caído.** El sistema entero está parado. Ver [B04_job_validacion_constante](../B%20-%20Recepcion%20y%20flags/B04_job_validacion_constante.md)
- **El ciclo está apagado** (`ArchivoAyudaRundeckMegara.txt` sin `1`). Ver [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md)

En ambos, el impacto crece cada minuto y el diagnóstico puede completarse en paralelo.

## Horario

De 4:00 a 23:00 de lunes a viernes, con guardias posibles fuera. **Todo es importante y no se puede
dejar pasar nada** — por eso distinguir el ruido conocido de la incidencia real es lo que hace
sostenible el turno. Ver [J07_escalado](../J%20-%20Operacion/J07_escalado.md).

## Ver también

[J07_escalado](../J%20-%20Operacion/J07_escalado.md) · [R5_09_catalogo_alertas](../R5%20-%20Alertas%20Rundeck/R5_09_catalogo_alertas.md) · [J10_trampas_conocidas](../J%20-%20Operacion/J10_trampas_conocidas.md) · [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md) · [R5_03_listas_distribucion](../R5%20-%20Alertas%20Rundeck/R5_03_listas_distribucion.md)

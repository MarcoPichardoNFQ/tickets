---
titulo: "Inicio"
tags:
  - inicio
---

# Base de conocimiento BAU — Aldrin AS-IS

179 fichas sobre **Aldrin** — el ETL que recibe los ficheros de Megara — tal como corre hoy en producción.

## Empieza por aquí

| Si… | Abre |
|---|---|
| Tienes una incidencia entre manos | [A06_arbol_decision_incidencias](A%20-%20Orientacion/A06_arbol_decision_incidencias.md) |
| Es tu primer día | [A01_que_es_aldrin](A%20-%20Orientacion/A01_que_es_aldrin.md) |
| Algo parece un fallo y dudas | [J10_trampas_conocidas](J%20-%20Operacion/J10_trampas_conocidas.md) |
| Es la verificación de la mañana | [J09_checklist_diario](J%20-%20Operacion/J09_checklist_diario.md) |
| Necesitas una consulta y no recuerdas cuál | [I12_consultas_frecuentes](I%20-%20Referencia%20de%20datos/I12_consultas_frecuentes.md) |
| Te acaban de dar los accesos | [J06_servidores_accesos](J%20-%20Operacion/J06_servidores_accesos.md) |

## Las cinco preguntas más frecuentes

- **¿Quién debería haber escrito este dato?** → [I09_indice_tabla_origen](I%20-%20Referencia%20de%20datos/I09_indice_tabla_origen.md)
- **¿Dónde se quedó este fichero?** → [I11_rastrear_un_fichero_e2e](I%20-%20Referencia%20de%20datos/I11_rastrear_un_fichero_e2e.md)
- **Este número está mal, ¿de dónde salió?** → [I10_rastrear_hacia_atras](I%20-%20Referencia%20de%20datos/I10_rastrear_hacia_atras.md)
- **¿Qué falta del lote de hoy?** → [R4_10_consultas_que_falta](R4%20-%20Sets%20incompletos/R4_10_consultas_que_falta.md)
- **¿Esto lo arreglo yo o lo escalo?** → [J07_escalado](J%20-%20Operacion/J07_escalado.md)

## Por dolor

| Dolor | Entrada |
|---|---|
| Descartes | [R1_03_identificar_validacion](R1%20-%20Descartes/R1_03_identificar_validacion.md) |
| Duplicados | [R2_01_deteccion_duplicados](R2%20-%20Duplicados/R2_01_deteccion_duplicados.md) |
| Errores de mapeo | [R3_01_anatomia_fallo_mapeo](R3%20-%20Errores%20de%20mapeo/R3_01_anatomia_fallo_mapeo.md) |
| Bloques de archivos incompletos | [R4_02_controlflag_interfaces](R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md) |
| Alertas de Rundeck | [R5_09_catalogo_alertas](R5%20-%20Alertas%20Rundeck/R5_09_catalogo_alertas.md) |

## Por etapa del flujo

```
Recepción → Conversión → Carga → Validación → Transformación → Mapeos → Cierre y Qlik
   B            C           D         E / R1          F            G          H
```

[A02_flujo_e2e_seis_pasos](A%20-%20Orientacion/A02_flujo_e2e_seis_pasos.md) · [A05_esquemas_base_de_datos](A%20-%20Orientacion/A05_esquemas_base_de_datos.md) · [A07_ventanas_ejecucion](A%20-%20Orientacion/A07_ventanas_ejecucion.md)

## Lo que hay que saber antes de fiarse de nada

Seis mecanismos hacen que un fallo real pase inadvertido, y cinco hacen ruido sin ser incidencias.
Están en [J10_trampas_conocidas](J%20-%20Operacion/J10_trampas_conocidas.md) y [J08_los_cinco_ruidosos](J%20-%20Operacion/J08_los_cinco_ruidosos.md).

La regla que resume el sistema: **el silencio no es evidencia**. Ver [R5_07_alerta_vs_estado_real](R5%20-%20Alertas%20Rundeck/R5_07_alerta_vs_estado_real.md).

Los hallazgos técnicos del análisis, con su verificación y corrección, en [Hallazgos](Hallazgos.md).

## Navegar por etiquetas

Cada ficha lleva tres etiquetas anidadas:

- `#familia/A` … `#familia/R5` — a qué grupo pertenece
- `#etapa/transversal`, `#etapa/mapeos`, `#etapa/carga-stg`… — en qué punto del flujo actúa
- `#tipo/referencia` o `#tipo/runbook` — qué clase de ficha es

Ejemplos útiles en la búsqueda: `tag:#tipo/runbook`, `tag:#etapa/mapeos`,
`tag:#tipo/runbook tag:#etapa/carga-stg`.

## Estructura

Una carpeta por familia. Los enlaces internos funcionan entre carpetas, así que la organización es
sólo visual: navega por enlaces, por etiquetas o por el grafo.

En `_proyecto/` está el material de construcción de la base: el plan, el índice original y el
registro de qué aportó cada fuente. No hace falta para el día a día.

## Sobre este vault

Cómo se construyó y qué material lo respalda: [Plan y alcance](_proyecto/Plan%20y%20alcance.md) · [Material recopilado](_proyecto/Material%20recopilado.md) · [00 Índice original](_proyecto/00%20%C3%8Dndice%20original.md) · [Hallazgos](Hallazgos.md)

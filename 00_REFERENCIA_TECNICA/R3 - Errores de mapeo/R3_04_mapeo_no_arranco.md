---
titulo: "R3.04 — El mapeo no arrancó"
familia: R3
etapa: "Mapeos"
tipo: Runbook
tags:
  - familia/R3
  - etapa/mapeos
  - tipo/runbook
keywords: "no se ejecutó, no aparece en el histórico, despacho, huérfano, jobref"
---

# R3.04 — El mapeo no arrancó

**Etapa:** Mapeos
**Tipo:** Runbook
**Palabras clave:** no se ejecutó, no aparece en el histórico, despacho, huérfano, jobref

## Síntoma

La tabla destino no se actualizó y **no hay ninguna ejecución** del mapeo en el histórico de
Rundeck: no falló, sencillamente no corrió.

## Qué mirar primero, en orden

### 1. ¿Está activo?

```sql
SELECT id_mapeo, nome_tabela_aldrin, nome_fn_mapeio, activo_inactivo, is_fromtis
FROM   exp_s3.tablas_mapeio_t
WHERE  nome_tabela_aldrin ILIKE '%<TABLA>%';
```

`false` → ver [R3_07_mapeo_desactivado](../R3%20-%20Errores%20de%20mapeo/R3_07_mapeo_desactivado.md). Fin del diagnóstico.

### 2. ¿Está en la lista del orquestador?

Ésta es la causa más difícil de ver y la que más tiempo hace perder.

`Mapeos` y `MapeosFlag` contienen una lista **estática** de referencias a jobs. La tabla de control
contiene el catálogo **real**. Nada garantiza que coincidan.

**Un mapeo activo en la tabla pero ausente de la lista del job no se ejecuta nunca, y no genera
ningún error.** Nadie lo llama: no hay fallo que registrar.

En Rundeck, abre `Mapeos` y `MapeosFlag` y busca el mapeo por su número en la lista de pasos. Si no
está, ésa es la causa.

```sql
-- Catálogo real para contrastar contra la lista del job
SELECT id_mapeo, nome_tabela_aldrin
FROM   exp_s3.tablas_mapeio_t
WHERE  activo_inactivo
ORDER  BY id_mapeo;
```

### 3. ¿Arrancó el ciclo de mapeos?

Si **ningún** mapeo corrió —no sólo el tuyo—, el problema está antes:

- `Control Inicio Carga Mapeo` falló o no se ejecutó. Ver [G03_control_inicio_carga_mapeo](../G%20-%20Mapeos/G03_control_inicio_carga_mapeo.md).
- El ciclo anterior no cerró y bloquea el siguiente. Ver [H10_cierre_no_completado](../H%20-%20Cierre%20y%20Qlik/H10_cierre_no_completado.md).

La distinción entre «no corrió éste» y «no corrió ninguno» cambia por completo el diagnóstico, y es
la primera pregunta que hay que responder.

### 4. ¿El orquestador correcto?

`Mapeos` y `MapeosFlag` despachan conjuntos distintos. Revisar el log del equivocado lleva a
concluir erróneamente que el mapeo no se lanzó. Comprueba los dos.

### 5. ¿`is_fromtis` lo excluye?

Existe un índice sobre `(id_mapeo, activo_inactivo, is_fromtis)`, lo que indica que el despacho
filtra por las tres columnas. Un mapeo activo puede quedar fuera por el valor de `is_fromtis`:

```sql
SELECT is_fromtis, count(*) FILTER (WHERE activo_inactivo) AS activos
FROM   exp_s3.tablas_mapeio_t GROUP BY 1;
```

Compara el valor del mapeo problemático con el de los que sí corren a diario.

## Tabla de decisión

| Señal | Causa |
|---|---|
| `activo_inactivo = false` | Apagado a propósito |
| No está en la lista del orquestador | **Mapeo huérfano**: nunca se ejecuta |
| Ningún mapeo corrió hoy | Fallo en el arranque del ciclo |
| Corrió en el otro orquestador | Estabas mirando el log equivocado |
| `is_fromtis` distinto al resto | Excluido del despacho |

## Acción

- **Huérfano**: hay que añadirlo a la lista del orquestador. No es un arreglo de soporte, es un
  cambio en la definición del job. Escálalo y, mientras tanto, ejecuta el job individual a mano
  para desatascar el día.
- **Ciclo no arrancado**: ve a [G03_control_inicio_carga_mapeo](../G%20-%20Mapeos/G03_control_inicio_carga_mapeo.md).
- **Apagado**: conversación con negocio.

## Cuándo escalar

Siempre que resulte ser un mapeo huérfano: significa que esa tabla de salida lleva sin actualizarse
desde que se desincronizaron la lista y el catálogo, que pueden ser meses. El alcance del problema
es mucho mayor que el ticket que lo destapó, y conviene revisar si hay más casos.

## Ver también

[G04_jobs_mapeos](../G%20-%20Mapeos/G04_jobs_mapeos.md) · [G02_tablas_mapeio_activo](../G%20-%20Mapeos/G02_tablas_mapeio_activo.md) · [G03_control_inicio_carga_mapeo](../G%20-%20Mapeos/G03_control_inicio_carga_mapeo.md) · [R3_11_relanzar_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_11_relanzar_mapeo.md) · [R3_01_anatomia_fallo_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_01_anatomia_fallo_mapeo.md)

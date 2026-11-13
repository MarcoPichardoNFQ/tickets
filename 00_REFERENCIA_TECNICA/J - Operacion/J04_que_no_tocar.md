---
titulo: "J04 — Qué NO tocar nunca, y por qué"
familia: J
etapa: "Transversal"
tipo: Runbook
tags:
  - familia/J
  - etapa/transversal
  - tipo/runbook
keywords: "no tocar, riesgo, prohibido, cambios peligrosos, límites de soporte"
---

# J04 — Qué NO tocar nunca, y por qué

**Etapa:** Transversal
**Tipo:** Runbook
**Palabras clave:** no tocar, riesgo, prohibido, cambios peligrosos, límites de soporte

## En una línea

Cinco cosas cambian el comportamiento del sistema sin desplegar nada, y ninguna es una acción de
soporte.

## 1. Las tablas `PAR_*`

`PAR_LOAD_PLAN_T`, `PAR_MAESTRO_TABLAS_T`, `PAR_MAESTRO_COLUMNAS_T`, `PAR_MAESTRO_MASK_T`,
`PAR_MAESTRO_VALID_T`.

**Por qué no:** son el contrato de datos. Una fila cambiada altera cómo se carga y valida una
interfaz **desde la siguiente ejecución**, sin despliegue, sin revisión y sin rastro de quién lo
hizo.

Los casos más destructivos:

- Cambiar `valid_err_des` de `1` a otro valor convierte una carga tolerante en una que **trunca la
  tabla entera** ante un fallo de clave foránea.
- Cambiar `cod_column` reordena las columnas del `\COPY` y los datos entran **desplazados**, sin
  error.
- Cambiar `chk_clave` rompe a la vez la detección de duplicados, el upsert a descartes y el
  reproceso.

Ver [E01_tablas_par_metadata_driven](../E%20-%20Parametrizacion/E01_tablas_par_metadata_driven.md) y [R1_01_descarte_vs_error](../R1%20-%20Descartes/R1_01_descarte_vs_error.md).

## 2. `exp_s3.tablas_mapeio_t.activo_inactivo`

**Por qué no:** refleja una decisión de negocio, no un estado técnico. Reactivar un mapeo apagado
puede repoblar una tabla que se quería congelada, y eso llega a los tableros del cliente.

Ver [R3_07_mapeo_desactivado](../R3%20-%20Errores%20de%20mapeo/R3_07_mapeo_desactivado.md).

## 3. Los ficheros `lookup_*.txt`

**Por qué no:** un `lookup_stg.txt` mal editado desalinea la relación entre id y carga. Y en
`lookup_trf.txt`, como la asignación STG/TRF depende de la **posición** en la lista de argumentos,
añadir o quitar un elemento **cambia el significado de todo lo que va detrás**.

Ver [D03_script_stg_trf](../D%20-%20Carga%20STG/D03_script_stg_trf.md) y [D02_lookup_stg_formato](../D%20-%20Carga%20STG/D02_lookup_stg_formato.md).

## 4. `controlflag_interfaces` y `controlflag_arquivos`

**Por qué no:** cambiar `recebido` a `true` para silenciar una alerta destruye la única evidencia de
que hubo un problema de recepción, y contamina las validaciones de cierre.

**No inventes flags tampoco.** Crear un fichero de flag a mano hace que el sistema registre como
recibidas interfaces que nadie declaró.

Ver [R4_08_fuera_de_ventana](../R4%20-%20Sets%20incompletos/R4_08_fuera_de_ventana.md) y [R4_06_xml_sin_flag](../R4%20-%20Sets%20incompletos/R4_06_xml_sin_flag.md).

## 5. Borrados sin `cod_load_trace`

**Por qué no:** es el único criterio que identifica con precisión «lo que entró en esa ejecución».
Borrar por fecha, por rango o por condición de negocio se lleva filas legítimas.

Y nunca en `trf_s3` sin coordinación: es el modelo de negocio, no una zona de paso.

Ver [R2_07_limpiar_sin_romper](../R2%20-%20Duplicados/R2_07_limpiar_sin_romper.md).

## Zona intermedia: con cuidado y dejando constancia

| Acción | Condición |
|---|---|
| Renombrar un fichero `_InLoad` atascado | Tras comprobar que sus datos no entraron ya |
| Relanzar un job individual | Tras comprobar si acumula o sobrescribe |
| Reprocesar descartes | Tras respaldar `_DES`: el reproceso la trunca entera |
| Corregir una línea de un plano para desatascar | Anotándolo: no es una solución, volverá mañana |
| Cancelar una sesión bloqueante | Mirando primero qué ejecuta |

## Lo que sí es siempre seguro

- Consultar cualquier tabla en modo lectura
- Leer logs de Rundeck
- Listar directorios
- Descifrar un fichero archivado para inspeccionarlo
- Ejecutar las consultas de diagnóstico de estas fichas

## La regla de fondo

**Si el arreglo cambia cómo se comportará el sistema mañana, no es soporte: es un cambio.**

Desatascar el día de hoy entra en el trabajo. Modificar parametrización, lookups o interruptores
funcionales necesita quien lo autorice, aunque técnicamente sea un `UPDATE` de una línea. Que sea
fácil de hacer no lo convierte en apropiado.

## Ver también

[E01_tablas_par_metadata_driven](../E%20-%20Parametrizacion/E01_tablas_par_metadata_driven.md) · [R2_07_limpiar_sin_romper](../R2%20-%20Duplicados/R2_07_limpiar_sin_romper.md) · [R3_07_mapeo_desactivado](../R3%20-%20Errores%20de%20mapeo/R3_07_mapeo_desactivado.md) · [J03_relanzar_seguro](../J%20-%20Operacion/J03_relanzar_seguro.md) · [J10_trampas_conocidas](../J%20-%20Operacion/J10_trampas_conocidas.md)

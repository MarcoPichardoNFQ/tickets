---
titulo: "R5.02 — Los jobs sin notificación: los fallos que nadie ve"
familia: R5
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/R5
  - etapa/transversal
  - tipo/referencia
keywords: "sin alerta, silencio, punto ciego, 22 jobs, cobertura, falso sentido de seguridad"
---

# R5.02 — Los jobs sin notificación: los fallos que nadie ve

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** sin alerta, silencio, punto ciego, 22 jobs, cobertura, falso sentido de seguridad

## En una línea

De los 46 jobs exportados, **22 no tienen ninguna notificación**: si fallan, no avisan a nadie.

## Por qué importa

El riesgo no es sólo que un fallo pase inadvertido. Es que **la ausencia de alertas se interpreta
como que todo va bien**. Media jornada sin correos puede significar que no hubo incidencias, o que
las hubo justo en los jobs que no avisan.

Regla práctica: **el silencio no es evidencia**. Para saber si el ciclo fue bien hay que mirar los
datos y las trazas, no la bandeja de entrada. Ver [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md).

## Los que sí avisan

Estos 24 jobs tienen notificación configurada:

```
0999 -. Optimizacao Blocos Rundeck V6      0999 Carga Megara 2026-04-24
Control Inicio Carga Mapeo                 Job control errores mapeo (x2)
JobsArchivosFlag                           LLamada Rundeck Flags Obligatorios
Manejo Flag                                Mapeos
MapeosFlag                                 Validacion Cantidades Recibidas
_00001 Análise de erros                    Optimizacion1,2,2.5TrfyStg
OptimizacioBloque3TRFySTG                  OptimizacioBloque4.1TRFySTG
OptimizacioBloque4.2TRFySTG                OptimizacioBloque5.1TRFySTG
OptimizacioBloque5.2TRFySTG                OptimizacioBloque5.3TRFySTG
OptimizacioBloque6.1TRFySTG                OptimizacioBloque6.2TRFySTG
OptimizacioBloque7.1TRFySTG                OptimizacioBloque7.2TRFySTG
OptimizacioBloque7.3TRFySTG
```

## Los puntos ciegos que más duelen

Cruzando esa lista con el conjunto de jobs, quedan sin cobertura piezas relevantes:

**Los bloques 1, 2 y 2.5 individualmente.** Están cubiertos por `Optimizacion1,2,2.5TrfyStg`, que
los agrupa, pero los jobs individuales no avisan por su cuenta. **Son los bloques de catálogos**, de
los que dependen todos los demás: un fallo ahí provoca descartes masivos aguas abajo.
Ver [R4_11_efecto_domino](../R4%20-%20Sets%20incompletos/R4_11_efecto_domino.md).

**`STG StartOver`.** La limpieza de staging. Si falla, el ciclo siguiente arranca sobre datos viejos.

**`Validacion constante presencia archivos flag`.** El vigilante que se ejecuta cada 3 segundos. Si
deja de funcionar, **el sistema entero se para** y nadie recibe un correo. Ver [B04_job_validacion_constante](../B%20-%20Recepcion%20y%20flags/B04_job_validacion_constante.md).

**`LlamadaTablaControlArquivosFlag`.** El paso que abre el lote. Si falla, las interfaces se
registran con el `id_camda` equivocado. Ver [B08_id_camda_lote](../B%20-%20Recepcion%20y%20flags/B08_id_camda_lote.md).

**Los jobs `Flag_*` individuales.**

**`Procedimiento control finalizacion mapeos`.** El cierre del ciclo.

## Qué hacer con esto

**Compénsalo con verificación activa.** Mientras la cobertura sea ésa, el checklist diario no es
opcional: es lo único que detecta los fallos silenciosos. Ver [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md).

**Ten presente el patrón al diagnosticar.** Ante «no llegó ninguna alerta pero el dato está mal»,
la primera hipótesis debe ser que falló algo que no avisa, no que el dato esté mal por otra causa.

**Es material de escalado.** La lista de arriba —en particular el vigilante de presencia y los
bloques de catálogo— es una recomendación concreta de mejora, con nombres y apellidos, que merece
llegar a quien pueda añadir las notificaciones.

## Cómo verificar la cobertura en tu entorno

Los exports pueden no reflejar el estado actual. En Rundeck, revisa job por job, o sobre los XML:

```bash
for f in *.xml; do
  if ! grep -q "<notification>" "$f"; then
    echo "SIN ALERTA: $(grep -oE '<name>[^<]*</name>' "$f" | head -1 | sed 's/<[^>]*>//g')"
  fi
done
```

## Ver también

[R5_01_como_notifica_rundeck](../R5%20-%20Alertas%20Rundeck/R5_01_como_notifica_rundeck.md) · [J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md) · [B04_job_validacion_constante](../B%20-%20Recepcion%20y%20flags/B04_job_validacion_constante.md) · [R5_07_alerta_vs_estado_real](../R5%20-%20Alertas%20Rundeck/R5_07_alerta_vs_estado_real.md)

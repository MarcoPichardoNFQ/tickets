---
titulo: "B04 — El vigilante: `Validacion constante presencia archivos flag`"
familia: B
etapa: "Recepción de flags"
tipo: Referencia
tags:
  - familia/B
  - etapa/recepcion-de-flags
  - tipo/referencia
keywords: "vigilante, cada 3 segundos, sondeo, presencia, disparador, Main Job Megara"
---

# B04 — El vigilante: `Validacion constante presencia archivos flag`

**Etapa:** Recepción de flags
**Tipo:** Referencia
**Palabras clave:** vigilante, cada 3 segundos, sondeo, presencia, disparador, Main Job Megara

## En una línea

Un job comprueba la presencia de flags **cada 3 segundos**, y es el que arranca todo el ciclo.

## Detalle

### La cadencia

El job `0999 Carga Megara 2026-04-24` está programado con:

```xml
<time hour='*' minute='*' seconds='0/3' />
```

Hora y minuto comodín, segundos cada 3. Son **20 ejecuciones por minuto, 28.800 al día**. Su primer
paso se llama precisamente `Validacion constante presencia archivos flag`.

El propio job `Validacion_constante_presencia_archivos_flag` no tiene horario: lo invoca el
anterior.

### Por qué importa esa cadencia

**Un fallo en este job genera ruido enormemente rápido.** Si empieza a fallar, produce miles de
ejecuciones fallidas por hora. Ante una avalancha de alertas del mismo job, éste es el sospechoso.

**El sistema reacciona en segundos, no en minutos.** Un flag depositado a las 14:32:10 se detecta
prácticamente al instante. Si un flag lleva ahí un minuto sin que pase nada, algo va mal — no hay
que esperar a la siguiente ventana.

**Consume recursos de forma constante.** Es normal ver este job permanentemente en el histórico de
ejecuciones de Rundeck. No es señal de nada.

### La cadena de arranque

```
0999 Carga Megara 2026-04-24        (cada 3 segundos)
  └── Validacion constante presencia archivos flag
        └── Manejo Flag
              └── Flag_<NOMBRE>            (uno por flag detectado)
                    └── load_filesflag_script.sh <id>
                          ├── registra en controlflag_arquivos
                          ├── recorre las interfaces declaradas
                          ├── registra en controlflag_interfaces
                          └── lanza la conversión de cada fichero presente
```

Y en paralelo, con cadencia de 10 minutos, los orquestadores de carga:

```
Main Job Megara / CargaInformacion / JobsArchivosFlag   (minuto :04 de cada 10)
  └── bloques OptimizacioBloque*TRFySTG
```

Dos ritmos distintos conviviendo: **detección casi instantánea, carga cada 10 minutos**. Ver
[A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md).

### Consecuencia práctica para el diagnóstico

Cuando alguien dice «el fichero llegó hace 20 minutos y no ha pasado nada», la pregunta no es si el
sistema lo ha visto —lo vio en segundos— sino en cuál de estos puntos se quedó:

1. ¿Se registró en `controlflag_arquivos`? → si no, el flag no se detectó o falló el script.
2. ¿Aparece en `controlflag_interfaces` con `recebido = true`? → si no, el fichero de datos no estaba.
3. ¿Se convirtió y está el `.gpg` en `DIR_MEGARA`? → si no, falló la conversión.
4. ¿Está el plano esperando en el directorio de trabajo? → entonces sólo falta que pase el bloque, y eso sí puede tardar hasta 10 minutos.

## Cómo verificarlo

```sql
-- ¿Cuándo se registró el último flag?
SELECT id_camda, nome_base, nome_completo, data, data_recebemento
FROM   stg_s3.controlflag_arquivos
ORDER  BY data DESC
LIMIT  10;
```

En Rundeck, el histórico del job de vigilancia debería mostrar ejecuciones continuas. Una
interrupción en esa serie marca exactamente cuándo se paró el sistema.

## Ver también

[A07_ventanas_ejecucion](../A%20-%20Orientacion/A07_ventanas_ejecucion.md) · [B05_job_manejo_flag](../B%20-%20Recepcion%20y%20flags/B05_job_manejo_flag.md) · [B06_load_filesflag_script](../B%20-%20Recepcion%20y%20flags/B06_load_filesflag_script.md) · [R4_05_flag_sin_xml](../R4%20-%20Sets%20incompletos/R4_05_flag_sin_xml.md)

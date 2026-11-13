---
titulo: "R5.03 — Las listas de distribución: quién recibe qué"
familia: R5
etapa: "Transversal"
tipo: Referencia
tags:
  - familia/R5
  - etapa/transversal
  - tipo/referencia
keywords: "destinatarios, listas, correo, quién recibe, soporte, desarrollo, escalado"
---

# R5.03 — Las listas de distribución: quién recibe qué

**Etapa:** Transversal
**Tipo:** Referencia
**Palabras clave:** destinatarios, listas, correo, quién recibe, soporte, desarrollo, escalado

## En una línea

Hay dos listas distintas —una de desarrollo y otra de soporte y cliente— y **no todos los jobs
avisan a la misma**, lo que determina quién se entera de qué.

## Lista A — desarrollo e implantación

Dominios `@nfq.mx`, `@nfq.es`, `@nfq.com.br`, `@nter.es`. Es la que usan la mayoría de los jobs,
incluidos los 14 bloques de carga y transformación.

```
david.vazquez@nfq.mx, antonio.diaque@nter.es, cesar.iza@nter.es,
enrique.toribio@nfq.mx, jesus.horno@nter.es, juan.aguayo@nter.es,
juanantonio.gascon@nter.es, marco.pichardo@nfq.mx, belen.cuallado@nfq.es,
ricardo.reyes@nfq.es, antonio.montoro@nter.es, henrique.munhoz@nfq.com.br
```

Con variantes: algunos jobs añaden `samuel.mathias@nfq.com.br`, `jenaro.camara@nter.es`,
`ismael.barranco@nter.es`, `manuel.hervas@nter.es`.

## Lista B — soporte y cliente

Dominios `@s3caceis.com.br`, `@prservicos.com.br`, más el buzón de grupo de soporte.

```
sancac.brazil.support@nfq.es, ricardo.mariz@s3caceis.com.br,
renato.rodrigues@prservicos.com.br, ado.silva@prservicos.com.br,
marcos.meneses@prservicos.com.br, gustavo.machado@s3caceis.com.br,
david.cassimiro@prservicos.com.br, delvan.santos@prservicos.com.br
```

Con `henrique.munhoz@nfq.com.br` añadido en algunas configuraciones.

**`sancac.brazil.support@nfq.es` es el único buzón de grupo del sistema.** Todo lo demás son
direcciones personales.

## Un caso aparte

Al menos una notificación va a un único destinatario:

```
marco.pichardo@nfq.mx
```

Una alerta con un solo receptor es un punto único de fallo: si esa persona está de vacaciones, nadie
la ve.

## Por qué importa la distinción

**Si estás en la lista A y no en la B, no ves las alertas operativas de soporte.** Y al revés. Lo
primero que debe hacer alguien que se incorpora a BAU es comprobar en cuál de las dos está, porque
determina qué incidencias le van a llegar y cuáles tendrá que buscar activamente.

**El destinatario no indica la gravedad.** Que una alerta vaya a la lista de desarrollo no significa
que sea técnica y no operativa: refleja cómo se configuró ese job en su momento, no una política.

## Los tres problemas estructurales

**1. Direcciones personales en vez de buzones de grupo.** Salvo el buzón de soporte, las alertas van
a personas. Cuando alguien cambia de proyecto o se va, su dirección sigue en la configuración de
cada job por separado. No hay un sitio único donde actualizarlo.

**2. Listas inconsistentes.** Hay al menos nueve combinaciones distintas de destinatarios entre los
jobs. Nadie recibe el conjunto completo.

**3. Ningún job avisa a los dos grupos a la vez.** Una incidencia relevante para ambos sólo llega a
uno.

## Qué hacer al respecto

Como soporte, lo accionable es:

- **Comprobar en qué listas estás** y pedir que te añadan a las que te faltan.
- **Al recibir una alerta, comprobar si el otro grupo también la recibió** antes de dar por hecho que
  lo saben.
- **Escalar la observación**: consolidar las listas en dos buzones de grupo —uno de soporte, otro de
  desarrollo— eliminaría los tres problemas de golpe. Es un cambio de configuración, no de código.

## Cómo verificarlo

```bash
cd <directorio de exports>
grep -h -oE "recipients='[^']*'" *.xml | sort | uniq -c | sort -rn
```

Y para un job concreto:

```bash
grep -A3 "<notification>" <JOB>.xml
```

## Ver también

[R5_01_como_notifica_rundeck](../R5%20-%20Alertas%20Rundeck/R5_01_como_notifica_rundeck.md) · [R5_10_cadena_escalado](../R5%20-%20Alertas%20Rundeck/R5_10_cadena_escalado.md) · [R5_02_jobs_sin_notificacion](../R5%20-%20Alertas%20Rundeck/R5_02_jobs_sin_notificacion.md) · [J07_escalado](../J%20-%20Operacion/J07_escalado.md)

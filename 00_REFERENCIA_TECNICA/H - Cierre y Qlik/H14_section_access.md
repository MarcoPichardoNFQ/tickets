---
titulo: "H14 — Section Access: quién ve qué en Qlik"
familia: H
etapa: "Cierre y Qlik"
tipo: Referencia
tags:
  - familia/H
  - etapa/cierre-y-qlik
  - tipo/referencia
keywords: "Section Access, seguridad, VistaFondos, REDUCTION, cod_cli, permisos"
---

# H14 — Section Access: quién ve qué en Qlik

**Etapa:** Cierre y Qlik
**Tipo:** Referencia
**Palabras clave:** Section Access, seguridad, VistaFondos, REDUCTION, cod_cli, permisos

## En una línea

El acceso a los datos en Qlik se restringe **por cliente**, con una tabla de usuarios que vive en un
QVD.

## Cómo está montado

Al final del script de carga:

```qlik
Section Access;
LOAD Upper(ROL_QS) AS ACCESS,
     Upper(USERID) AS USERID
FROM [lib://QVD (cloud_datahubadmin02)/VistaFondos.qvd](qvd);

Section Application;
LOAD Upper(USERID)    AS USERID,
     UPPER(REDUCTION) AS cod_cli
FROM [lib://QVD (cloud_datahubadmin02)/VistaFondos.qvd](qvd);
```

| Elemento | Qué hace |
|---|---|
| `ROL_QS` → `ACCESS` | El rol del usuario |
| `USERID` | El identificador del usuario |
| `REDUCTION` → `cod_cli` | **El cliente al que queda reducido** |

`VistaFondos.qvd` es la tabla de permisos: qué usuario ve qué cliente.

## Qué implica para soporte

**Un usuario sólo ve los `cod_cli` que le asigna `VistaFondos.qvd`.** Si reporta que «no ve un
fondo», hay tres posibilidades y conviene descartarlas en este orden:

| Causa | Cómo se comprueba |
|---|---|
| El dato no está publicado | Estado del cliente en `s3_interface_control_xml_t` |
| El dato está pero no se recargó | Historial de la tarea en Qlik |
| **El usuario no tiene permiso** sobre ese cliente | `VistaFondos.qvd` — sólo desde Qlik |

Las dos primeras se comprueban desde la base; **la tercera no**.

```sql
-- 1. ¿Está publicado ese cliente?
SELECT cod_cli, dat_hr_nav, des_status
FROM   trf_s3.s3_interface_control_xml_t
WHERE  cod_cli = '<CLIENTE>' ORDER BY dat_hr_nav DESC LIMIT 3;
```

Si el estado es `Publish` o `WaitingFMValidation`, el dato debería estar disponible — y entonces
el problema es de permisos o de recarga.

## Un síntoma que despista

**«Yo lo veo y mi compañero no.»** Con Section Access por cliente, eso es lo esperable: no es un
fallo del sistema, es la reducción de datos funcionando.

Antes de investigar nada técnico, comprueba si ambos usuarios tienen el mismo alcance en
`VistaFondos.qvd`.

## Lo que soporte no puede hacer

**No hay forma de consultar los permisos desde la base de datos.** `VistaFondos.qvd` es un fichero
de Qlik: sólo se puede examinar desde la consola de Qlik o desde una app que lo cargue.

Ver [J07_escalado](../J%20-%20Operacion/J07_escalado.md): es un caso donde el análisis previo llega hasta cierto punto y a partir de ahí
hay que escalar al administrador de Qlik con lo que sí se ha comprobado.

## Qué llevar al escalado

- Usuario afectado y `cod_cli` que no ve
- Confirmación de que ese cliente está publicado (`des_status`)
- Confirmación de que la tabla se recargó
- Si otro usuario sí lo ve

Con esos cuatro datos, quien administre Qlik puede resolverlo en un minuto.

## Ver también

[H18_cliente_no_aparece](../H%20-%20Cierre%20y%20Qlik/H18_cliente_no_aparece.md) · [R4_04_s3_interface_control](../R4%20-%20Sets%20incompletos/R4_04_s3_interface_control.md) · [H06_script_carga_qlik](../H%20-%20Cierre%20y%20Qlik/H06_script_carga_qlik.md) · [J07_escalado](../J%20-%20Operacion/J07_escalado.md)

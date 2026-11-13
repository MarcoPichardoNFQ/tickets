---
titulo: "H18 — Un cliente no aparece en Qlik"
familia: H
etapa: "Cierre y Qlik"
tipo: Runbook
tags:
  - familia/H
  - etapa/cierre-y-qlik
  - tipo/runbook
keywords: "cliente ausente, cod_cli, des_status, Publish, permisos, cuatro puertas"
---

# H18 — Un cliente no aparece en Qlik

**Etapa:** Cierre y Qlik
**Tipo:** Runbook
**Palabras clave:** cliente ausente, cod_cli, des_status, Publish, permisos, cuatro puertas

## Síntoma

Los datos de un cliente concreto no se ven en Qlik. Los de los demás sí.

## Las cuatro puertas por cliente

Este sistema filtra por cliente en **cuatro puntos distintos**. El dato tiene que pasarlos todos:

```
1. bloqueio_insercao_dados        ¿se le permite entrar en trf_s3?
2. des_status del control          ¿está publicable?
3. dat_hr_nav                      ¿la fecha del dato es anterior al NAV?
4. Section Access de Qlik          ¿tiene permiso quien mira?
```

Cada una explica un caso distinto, y las tres primeras se comprueban desde la base.

## Puerta 1 — ¿Se bloqueó la inserción?

```sql
SELECT cod_cli, cd_origem, fl_master, dat_carga
FROM   trf_s3.cart_estat_portfoliomaster
WHERE  cod_cli = '<CLIENTE>';
```

| Resultado | Interpretación |
|---|---|
| Sin filas o sin `fl_master = 1` | No hay bloqueo por esta vía |
| `cd_origem = 'MG'` | Origen Megara: flujo normal |
| `cd_origem` distinto de `'MG'` | **Puede estar bloqueado** para `base_id` 1 y 2 |

Ver [F07_bloqueio_insercao_dados](../F%20-%20Transformacion%20TRF/F07_bloqueio_insercao_dados.md).

## Puerta 2 — ¿Está publicable?

```sql
SELECT cod_cli, dat_hr_nav, dat_hr_proc_meg, dat_hr_proc_aldrin,
       des_status, cod_error, des_error
FROM   trf_s3.s3_interface_control_xml_t
WHERE  cod_cli = '<CLIENTE>'
ORDER  BY dat_hr_nav DESC LIMIT 10;
```

**Sólo `Publish` y `WaitingFMValidation` llegan a Qlik.** Cualquier otro estado deja al cliente
fuera, por muy correctos que estén sus datos.

Y si `cod_error` no es nulo, ahí está la causa del estado.

Ver [R4_04_s3_interface_control](../R4%20-%20Sets%20incompletos/R4_04_s3_interface_control.md).

## Puerta 3 — ¿La fecha del dato supera el NAV?

El script de Qlik exige `date(<campo_fecha>) <= date(dat_hr_nav)`. Un dato con fecha **posterior**
al NAV del cliente no se publica.

```sql
SELECT max(<campo_fecha>) AS dato_mas_reciente
FROM   trf_s3.<TABLA> WHERE cod_cli = '<CLIENTE>' AND base_id = 0;

SELECT max(dat_hr_nav) AS nav_del_cliente
FROM   trf_s3.s3_interface_control_xml_t WHERE cod_cli = '<CLIENTE>';
```

Si el dato es más reciente que el NAV, **es correcto que no se vea**: el NAV aún no lo cubre.

## Puerta 4 — ¿Tiene permiso quien mira?

`VistaFondos.qvd` restringe qué `cod_cli` ve cada usuario. **No se puede consultar desde la base.**

Pista rápida: **si otro usuario sí lo ve, es permisos.** Ver [H14_section_access](../H%20-%20Cierre%20y%20Qlik/H14_section_access.md).

## Y las comprobaciones generales

Si las cuatro puertas están abiertas, el problema no es del cliente sino general:

```sql
-- ¿Hay datos de ese cliente en la tabla?
SELECT count(*) FROM trf_s3.<TABLA> WHERE cod_cli = '<CLIENTE>' AND base_id = 0;

-- ¿Se actualizó la tabla hoy?
SELECT max(dat_qlikupdate) FROM trf_s3.<TABLA>;
```

Ver [H09_qlik_datos_de_ayer](../H%20-%20Cierre%20y%20Qlik/H09_qlik_datos_de_ayer.md) y [H12_recarga_qlik_fallo](../H%20-%20Cierre%20y%20Qlik/H12_recarga_qlik_fallo.md).

## Tabla de decisión

| Puerta que falla | Naturaleza | Qué hacer |
|---|---|---|
| 1 — bloqueo por origen | Configuración funcional | Verificar si es correcto; escalar si no |
| 2 — estado no publicable | Proceso de negocio | Depende de por qué está en ese estado |
| 3 — fecha posterior al NAV | **Correcto** | Explicar y cerrar |
| 4 — permisos | Administración de Qlik | Escalar con la evidencia de que el dato sí está |
| Ninguna: el dato no está | Aguas arriba | [I11_rastrear_un_fichero_e2e](../I%20-%20Referencia%20de%20datos/I11_rastrear_un_fichero_e2e.md) |

## Qué llevar al escalado

- `cod_cli` y tabla afectada
- `des_status` y `dat_hr_nav` del cliente
- `cd_origem` de su maestro de cartera
- Conteo del dato en `trf_s3` con `base_id = 0`
- Si otro usuario lo ve

Ver [J07_escalado](../J%20-%20Operacion/J07_escalado.md).

## Ver también

[F07_bloqueio_insercao_dados](../F%20-%20Transformacion%20TRF/F07_bloqueio_insercao_dados.md) · [R4_04_s3_interface_control](../R4%20-%20Sets%20incompletos/R4_04_s3_interface_control.md) · [H14_section_access](../H%20-%20Cierre%20y%20Qlik/H14_section_access.md) · [H09_qlik_datos_de_ayer](../H%20-%20Cierre%20y%20Qlik/H09_qlik_datos_de_ayer.md) · [H06_script_carga_qlik](../H%20-%20Cierre%20y%20Qlik/H06_script_carga_qlik.md) · [H17_conteo_no_cuadra](../H%20-%20Cierre%20y%20Qlik/H17_conteo_no_cuadra.md)

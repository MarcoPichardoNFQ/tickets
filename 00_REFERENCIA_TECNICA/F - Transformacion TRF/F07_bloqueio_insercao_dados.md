---
titulo: "F07 — `bloqueio_insercao_dados`: el bloqueo por cliente"
familia: F
etapa: "Transformación TRF"
tipo: Referencia
tags:
  - familia/F
  - etapa/transformacion-trf
  - tipo/referencia
keywords: "bloqueio_insercao_dados, portfoliomaster, cd_origem, fl_master, base_id, MG"
---

# F07 — `bloqueio_insercao_dados`: el bloqueo por cliente

**Etapa:** Transformación TRF
**Tipo:** Referencia
**Palabras clave:** bloqueio_insercao_dados, portfoliomaster, cd_origem, fl_master, base_id, MG

## En una línea

Una función que decide, **cliente por cliente**, si se permite insertar datos — y que explica por
qué a veces falta el dato de un cliente concreto y de ningún otro.

## Firma

```sql
trf_s3.bloqueio_insercao_dados(
    cod_cli_v   varchar,   -- cliente
    dat         date,      -- fecha
    base_id     integer,   -- base
    nome_tabela varchar,   -- tabla destino
    des_typ_v   varchar DEFAULT NULL
) RETURNS boolean
```

Devuelve un booleano que los procedimientos consultan antes de insertar.

## La lógica

```sql
SELECT cd_origem, dat_carga INTO origem, dat_carga_v
FROM   trf_s3.cart_estat_portfoliomaster
WHERE  cod_cli = cod_cli_v AND fl_master = 1;

IF origem IS NULL THEN
    RETURN TRUE;          -- sin maestro definido → se permite
END IF;

IF base_id = 1 OR base_id = 2 THEN
    IF origem <> 'MG' THEN
        -- comprueba s3_master_control_t y rollback parcial
    END IF;
END IF;
```

Tres conceptos determinan el resultado:

| Elemento | Qué es |
|---|---|
| `cart_estat_portfoliomaster` | Tabla maestra de carteras, con una fila marcada `fl_master = 1` por cliente |
| `cd_origem` | Origen del dato de ese cliente. **`'MG'` es Megara**; otro valor indica otra procedencia |
| `base_id` | La base sobre la que se escribe. Las comprobaciones sólo aplican a `1` y `2` |
| `s3_master_control_t` | Control adicional que interviene cuando el origen no es Megara |

## Lo que hay que retener

**Un cliente sin fila maestra no se bloquea nunca** — `origem IS NULL` devuelve `TRUE` de
inmediato. Así que la ausencia de configuración se traduce en «permitido», no en «bloqueado».

**El bloqueo es selectivo por cliente.** No afecta a la tabla ni al proceso: sólo a las filas de
los clientes cuyo maestro indica otro origen. Por eso el síntoma es «falta el dato de este cliente»
y no «falta la tabla».

**`base_id` acota el alcance.** Fuera de `1` y `2`, las comprobaciones no se aplican.

## Cuándo aparece en un diagnóstico

Ante «faltan los datos de un cliente concreto y del resto están bien», ésta es la comprobación:

```sql
SELECT cod_cli, cd_origem, fl_master, dat_carga
FROM   trf_s3.cart_estat_portfoliomaster
WHERE  cod_cli = '<CLIENTE>';
```

| Resultado | Interpretación |
|---|---|
| Sin filas, o `fl_master = 1` ausente | No hay bloqueo por esta vía |
| `cd_origem = 'MG'` | Origen Megara: el flujo normal |
| `cd_origem` distinto de `'MG'` | **El cliente puede estar bloqueado** para `base_id` 1 y 2 |

Y en paralelo, comprueba el control de publicación, que es la otra puerta por cliente:

```sql
SELECT cod_cli, dat_hr_nav, des_status
FROM   trf_s3.s3_interface_control_xml_t
WHERE  cod_cli = '<CLIENTE>' ORDER BY dat_hr_nav DESC LIMIT 5;
```

Ver [R4_04_s3_interface_control](../R4%20-%20Sets%20incompletos/R4_04_s3_interface_control.md).

## Las dos puertas por cliente

Conviene tenerlas juntas, porque un dato de cliente puede detenerse en cualquiera de las dos:

| Puerta | Dónde actúa | Qué comprueba |
|---|---|---|
| `bloqueio_insercao_dados` | Al **insertar** en `trf_s3` | Origen del maestro de cartera |
| `s3_interface_control_xml_t.des_status` | Al **publicar** en Qlik | Estado del NAV del cliente |

La primera impide que el dato entre; la segunda, que salga.

## Cuándo escalar

Si el bloqueo es correcto —el cliente tiene otro origen a propósito— no hay nada que hacer y el
ticket se cierra explicándolo. Si el maestro parece mal configurado, es una corrección funcional que
excede a soporte.

## Ver también

[R4_04_s3_interface_control](../R4%20-%20Sets%20incompletos/R4_04_s3_interface_control.md) · [F10_localizar_fallo_trf](../F%20-%20Transformacion%20TRF/F10_localizar_fallo_trf.md) · [F11_trf_corrio_sin_cambios](../F%20-%20Transformacion%20TRF/F11_trf_corrio_sin_cambios.md) · [I18_columnas_comunes](../I%20-%20Referencia%20de%20datos/I18_columnas_comunes.md)

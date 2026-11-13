---
id: NFQBAU-1685
fecha_apertura: 2026-11-10
fecha_limite: 2026-11-10
fecha_resolucion:            # obligatoria al pasar a Resuelto
estado: Abierto              # ver 05_GENERAL/listas.json
prioridad: Alta
responsable:                 # Nombre Apellido, igual que el fichero en 04_PERSONAS
origen: email
referencia_origen: "Saldo no demonstrativo de caixa CUST3600 - DATA 09/11/2026 (2026-11-10)"
categoria: [Qlik]
entorno: []                  # Producción | UAT
sintoma: "El saldo en el demostrativo de caja CUST3600 aparece incorrecto al mostrar dos líneas el 06/11/2026 y discrepancias en los saldos de apertura y cierre del 09/11/2026."
solucion_corta:              # una línea: qué lo arregló
codigo_relacionado:
  - repo:
    modulo:
    version:                 # tag de PRD cuando se despliegue
tickets_proveedor: []        # notas de 03_PROVEEDORES
decision_relacionada:
referencias_tecnicas: []     # fichas de 00_REFERENCIA_TECNICA que ayudaron
actualizado: 2026-11-10 20:16
actualizado_por: Correo automático
tags: [ticket, bau]
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marcela C., tecnología, solicita urgentemente verificar el saldo en el demostrativo de caixa CUST3600. Indica que el 06/11 hay dos líneas de saldo incorrectas y que el día 09/11 el saldo de apertura es 2.033,34 y el de cierre 2.000,00. Adjunta capturas.

Detalles: Informe o pantalla CUST3600; Fecha afectada: 06/11/2026 (saldo correcto 2.033,34, sin movimientos entre apertura y cierre, pero muestra dos líneas) y 09/11/2026 (saldo de apertura 2.033,34 y de cierre 2.000,00); Cuenta: 00332271000130131355BRL; adjunta capturas.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png

## Histórico de interacciones

- 2026-11-10 18:18 — Correo automático — Marcela C., tecnología, solicita urgentemente verificar el saldo en el demostrativo de caixa CUST3600. Indica que el 06/11 hay dos líneas de saldo incorrectas y que el día 09/11 el saldo de apertura es 2.033,34 y el de cierre 2.000,00. Adjunta capturas.
- 2026-11-10 18:46 — Correo automático — Correo nuevo en el hilo: Marcela C., de Tecnología, solicitó verificar el saldo del demostrativo de caja CUST3600, que presenta dos líneas de saldo para el 06/11, afectando los días posteriores. Marco P., Senior Consultant, informa que el saldo reflejado en el sistema es consistente con la base de datos y sugiere una recarga de megara del fondo si es necesario. Adjunta capturas. Detalles: Informe/Pantalla: demostrativo de caixa CUST3600; La captura muestra 'Recursive View UC : Client Balance' y 'View And Run : Client Balance' con 'Cash Account' 00332271000130131355BRL y 'Balance' 2,033.34 BRL para 'Position Date' 04/11/2026; Fechas afectadas: 06/11/2026 y 09/11/2026; Problema: Dos líneas de saldo para el 06/11; Saldo correcto en 06/11: 2,033.34 (apertura y cierre iguales); Saldo en 09/11: apertura 2,033.34, cierre 2,000.00; El saldo en el sistema refleja el de la base de datos; Sugerencia: Recarga de megara del fondo. · Adjuntos del correo: image003.png, image001.png, image004.png, image002.png
- 2026-11-10 19:11 — Correo automático — Correo nuevo en el hilo: Marcela C., del área de tecnología del cliente, informa de que están apareciendo otros casos con problemas en los saldos para la fecha 09/11/2026. Solicita al equipo de soporte que verifiquen lo sucedido. Detalles: Fecha de datos afectada: 09/11/2026; La captura de pantalla muestra las vistas 'Recursive View UC : Client Balance' y 'View And Run : Client Balance' para la cuenta '00332271000130131355BRL', tipo 'Value Date', fecha de posición 04/11/2026 y saldo de 2,033.34 BRL · Adjuntos del correo: image002.png, image003.png, image005.png, image006.png
- 2026-11-10 19:12 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, informa de que han detectado la coexistencia de saldos para los mismos clientes en idéntica fecha procedentes tanto de Megara como de SAC. Facilita el listado detallado de clientes y fechas donde se produce esta duplicidad. Adjunta capturas. Detalles: Doble registro (Qtde = 2) de saldos para un mismo cliente y fecha (cod_cli, dat_liq) procedentes de fuentes Megara y SAC; Clientes afectados el 2026-11-09: TCES36360, TCES110579, TCES36381, TCES32993, TCES109457, TCES110560, CUST3320, TCES43774, TCES39785, TCES38967, TCES38886, TCES38843; Otros clientes afectados entre 2026-10-02 y 2026-11-06: CUST3320, CUST4448, CUST4796, CUST4245, CUST4660, CUST4658; La captura muestra las pantallas 'Recursive View UC : Client Balance' y 'View And Run : Client Balance' para la cuenta 00332271000130131355BRL, tipo Value Date, fecha de posición 04/11/2026 y saldo 2,033.34 BRL · Adjuntos del correo: image002.png, image005.png, image003.png, image006.png
- 2026-11-10 19:15 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, informa de que se han identificado saldos duplicados para los mismos clientes y fechas procedentes simultáneamente de fuentes Megara y SAC. Aporta una lista de múltiples clientes afectados con fechas entre octubre y noviembre de 2026 y adjunta capturas. Detalles: Campos identificados: cod_cli, dat_liq, Qtde con valor duplicado (2) provenientes de Megara y SAC; Clientes afectados reportados: TCES36360, TCES110579, TCES36381, TCES32993, TCES109457, TCES110560, CUST3320, TCES43774, TCES39785, TCES38967, TCES38886, TCES38843, CUST4448, CUST4796, CUST4245, CUST4660, CUST4658; Rango de dat_liq afectado del 2026-10-02 al 2026-11-09; La captura muestra las pantallas 'Recursive View UC : Client Balance' y 'View And Run : Client Balance' para la cuenta Cash Account 00332271000130131355BRL, Balance Type Value Date, Position Date 04/11/2026 y Balance 2,033.34 BRL · Adjuntos del correo: image002.png, image005.png, image003.png, image006.png
- 2026-11-10 19:21 — Correo automático — Correo nuevo en el hilo: Thiago A., de Sancac, informa que se limpiaron los registros duplicados, pero el fondo CUST3600 para el 09/11/2026 no estaba en la lista de duplicados y el problema persiste en el saldo cuando no hay movimientos. Marcela C., de Tecnología, había solicitado verificar el saldo del demostrativo de caja para el fondo CUST3600, que presentaba dos líneas de saldo para el 06/11 y un saldo incorrecto para el 09/11. Marco P., consultor de NFQ, había identificado saldos duplicados para el mismo cliente en la misma fecha, provenientes de Megara y SAC. Adjunta capturas. Detalles: El fondo afectado es CUST3600 para la fecha 09/11/2026; El problema se manifiesta en el saldo cuando no hay movimientos; Marcela C. reportó dos líneas de saldo para el 06/11, con un saldo correcto de 2.033,34; Para el 09/11, el saldo de apertura es 2.033,34 y el de cierre 2.000,00; Marco P. identificó saldos duplicados para el mismo cliente en la misma fecha de fuentes Megara y SAC, con una cantidad de 2 para varios cod_cli y dat_liq (ej. TCES36360, 2026-11-09, 2); Se adjuntan capturas de pantalla que muestran una 'Recursive View UC : Client Balance' y 'View And Run : Client Balance' con un 'Cash Account' 00332271000130131355BRL y 'Balance' 2,033.34 para la 'Position Date' 04/11/2026. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png
- 2026-11-10 20:11 — Correo automático — Correo nuevo en el hilo: Marcela Y., de tecnología, reclama que a pesar de las ejecuciones el saldo sigue sin ajustarse para la fecha del 9 de noviembre de 2026 en varios fondos, indicando que el problema ocurre cuando no hay movimientos. A pesar de que se han limpiado los duplicados por parte del equipo, el fondo CUST3600 sigue fallando. Adjunta capturas. Detalles: Fondos afectados: CUST3600, CUST4805, CUST4520 para la fecha 09/11/2026; el problema se manifiesta en el saldo cuando no hay movimientos (saldo de apertura incorrecto frente al de cierre); adjunta capturas de pantalla de la interfaz 'Recursive View UC : Client Balance' mostrando cuentas, tipos de saldo, fechas de posición y balances en BRL. · Adjuntos del correo: image002.png, image003.png, image006.png, image007.png, image008.png
- 2026-11-10 20:16 — Correo automático — Correo nuevo en el hilo: Marco P. informa que está verificando el problema del saldo en el informe de caja, que Marcela C. reportó que no se ajustó para varios fondos después de las cargas. Detalles: Marcela C. reportó que el saldo no ajustó para CUST3600, CUST4805, CUST4520 para el 09/11. Thiago A. indicó que el problema es el saldo cuando no hay movimiento para CUST3600 del 09/11/2026. Marco P. previamente identificó saldos duplicados para el mismo cliente en la misma fecha, provenientes de Megara y SAC, listando varios cod_cli y dat_liq con cantidad 2. Marcela C. también mencionó dos líneas de saldo para el 06/11, con saldo correcto de 2.033,34 y para el 09/11, saldo de apertura 2.033,34 y cierre 2.000,00. Adjunta capturas de pantalla de "Recursive View UC : Client Balance" mostrando un saldo de 2.033,34 BRL para el 04/11/2026. · Adjuntos del correo: image002.png, image003.png, image006.png, image007.png, image008.png

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

### Cómo se comprobó

### Con quién se habló

### Servicios, jobs o tablas tocados

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-11-10 18:18 — nuevo → Abierto — Correo automático

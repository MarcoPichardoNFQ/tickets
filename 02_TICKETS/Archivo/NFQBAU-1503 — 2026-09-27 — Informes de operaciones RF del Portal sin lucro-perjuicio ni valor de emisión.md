---
id: NFQBAU-1503
fecha_apertura: 2026-09-27
fecha_limite: 2026-09-28
fecha_resolucion: 2026-09-28
estado: Resuelto
prioridad: Media
responsable: Ricardo Reyes
origen: email
referencia_origen: "RES: ETF - Relatório de Operações RF (2026-08-10)"
categoria:
  - Qlik
entorno:
  - Producción
sintoma: informes de operaciones RF del Portal sin lucro/perjuicio en ventas de fondos MEGARA y sin PU ni valor líquido en emisiones del ETF (CUST4892)
solucion_corta: recarga manual en Qlik resolvió el informe de ventas MEGARA; el punto del ETF (cantidad y PU en emisiones sin financiero) quedó pendiente y se reabrió
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas:
  - 00_REFERENCIA_TECNICA/H - Cierre y Qlik/H08_recarga_qlik.md
  - 00_REFERENCIA_TECNICA/H - Cierre y Qlik/H12_recarga_qlik_fallo.md
actualizado: 2026-10-08 07:10
actualizado_por: Ricardo Reyes
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Ricardo C., responsable del Proyecto Apollo del cliente, tras la reunión del 10 de agosto, resume dos fallos en los informes de operaciones de renta fija del Portal: (1) el informe "Operações com Títulos de RF" no muestra el lucro/perjuicio de las operaciones de venta para fondos con base MEGARA, mientras que para fondos con base SAC sí; (2) en el informe "Operações com Títulos de Renda Fixa" (CUST4892) del fondo ETF, las emisiones por integralización, marcadas como "Depósito", no traen PU ni valor líquido, y además muestran lucro/perjuicio siendo una entrada. Pide análisis y próximos pasos.

## Histórico de interacciones

- 2026-09-27 20:03 — Ricardo Reyes — Email de Ricardo C., responsable del Proyecto Apollo del cliente (copia a contabilidad de fondos y al equipo), resumen de la reunión del 10/08 sobre los informes de RF. Dos puntos: lucro/perjuicio ausente en ventas de fondos MEGARA (fondos SAC correctos); emisiones por integralización del ETF sin PU ni valor líquido en CUST4892 y con lucro/perjuicio indebido. Adjunta capturas comparativas MEGARA (NOK) y SAC (OK). Pide análisis y próximos pasos.

- 2026-09-27 20:14 — Ricardo Reyes — Recarga manual en Qlik de la aplicación del informe de operaciones de RF. Tras la recarga, ambos informes muestran los datos correctos (lucro/perjuicio en ventas MEGARA; PU y valor líquido en emisiones del ETF).
- 2026-09-27 20:14 — Ricardo Reyes — APROBACIÓN — Ricardo C., responsable del Proyecto Apollo del cliente, confirma que los informes salen bien.

- 2026-09-28 14:45 — Ricardo Reyes — Correo de José Carlos N., contabilidad de fondos del cliente (28/09, 11:57): en las emisiones por integralización no hay movimiento de caja, pero necesitan ver esos activos en el informe de movimiento; si el valor líquido sale como R$ 0,00, piden al menos cantidad y PU para poder calcular. El punto del CUST4892 sigue abierto.
- 2026-09-28 14:45 — Ricardo Reyes — Correo de Ricardo C., responsable del Proyecto Apollo del cliente (28/09, 15:07): convocará una reunión para resolver ese punto aprovechando que NFQ está trabajando en el informe. Reabierto: el cierre del 27/09 fue prematuro para el punto del ETF.

- 2026-09-28 16:13 — Ricardo Reyes — Enviado correo a Ricardo C., responsable del Proyecto Apollo del cliente: confirmada disponibilidad para la reunión y adelantado que NFQ llevará el análisis de cómo mostrar cantidad y PU en las emisiones marcadas como Depósito en el CUST4892.

- 2026-09-28 16:26 — Ricardo Reyes — Cerrado: prueba del sistema; el equipo empieza con las vistas limpias.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Recarga manual, desde Qlik, de la aplicación que alimenta el informe "Operações com Títulos de RF" del Portal. No hubo cambio de código ni despliegue.

### Cómo se comprobó

El cliente revisó ambos informes tras la recarga y confirmó por correo que muestran los datos correctos: lucro/perjuicio en ventas de fondos MEGARA, y PU y valor líquido en las emisiones por integralización del ETF (CUST4892), sin lucro/perjuicio indebido.

### Con quién se habló

Ricardo C., responsable del Proyecto Apollo del cliente (aviso y confirmación). Sin intervención de NTT.

### Servicios, jobs o tablas tocados

Aplicación Qlik del informe de operaciones de RF (recarga). Ningún job de Rundeck ni tabla modificada.

### Referencias técnicas usadas y por qué

- [H08 — La recarga de Qlik](../../00_REFERENCIA_TECNICA/H%20-%20Cierre%20y%20Qlik/H08_recarga_qlik.md): explica que el único disparador de Qlik en la orquestación es el paso de recarga y por qué puede no enviar la petición; es la causa probable de que el informe no se refrescara solo.
- [H12 — La recarga de Qlik falló](../../00_REFERENCIA_TECNICA/H%20-%20Cierre%20y%20Qlik/H12_recarga_qlik_fallo.md): qué mirar en orden cuando el dato está en base y el informe no lo refleja; es la lista que seguir la próxima vez antes de recargar a mano.

## Vencimiento

## Historial de estados
- 2026-09-27 20:08 — nuevo → Abierto — Ricardo Reyes
- 2026-09-27 20:18 — Abierto → Resuelto — Ricardo Reyes
- 2026-09-28 14:45 — Resuelto → Revisión cliente — Ricardo Reyes
- 2026-09-28 16:26 — Revisión cliente → Resuelto — Ricardo Reyes

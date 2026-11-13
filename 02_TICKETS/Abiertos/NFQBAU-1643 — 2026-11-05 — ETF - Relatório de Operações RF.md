---
id: NFQBAU-1643
fecha_apertura: 2026-11-05
fecha_limite: 2026-11-06
fecha_resolucion:
estado: En curso
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: ETF - Relatório de Operações RF (2026-11-05)
categoria:
  - Qlik
entorno: []
sintoma: El informe "Operações com Títulos de Renda Fixa" requiere una corrección en el cálculo de la columna "Lucro / Prejuízo".
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-06 15:00
actualizado_por: Ricardo Reyes
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Continúa el hilo del [NFQBAU-1503](../Archivo/NFQBAU-1503%20—%202026-09-27%20—%20Informes%20de%20operaciones%20RF%20del%20Portal%20sin%20lucro-perjuicio%20ni%20valor%20de%20emisión.md), cerrado el 2026-09-28: no se reabre, se crea este. Marcos M., tecnología, consulta sobre el estado del ajuste del informe de renta fixa. Además, responde a José Carlos N., contabilidade de fundos del cliente, aclarando que el cálculo de ganancia/pérdida debe realizarse a nivel de activo u operación. Adjunta capturas.

Detalles: Informe afectado: "Operações com Títulos de Renda Fixa"; Columna: "Lucro / Prejuízo"; Criterio funcional: El cálculo de lucro/prejuízo se debe realizar a nivel de activo/operación; Las capturas muestran el reporte con detalle de operaciones de Compra, Venda, Resgate y Depósito, destacando los campos Custo Histórico, Valor de Emissão, Lucro / Prejuízo, Valor Bruto y Valor Líquido.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png

## Histórico de interacciones

- 2026-11-05 13:01 — Correo automático — Correo nuevo en el hilo: José Carlos N., contabilidad de fondos del cliente, consulta el estado de la solución sobre la columna de Lucro/Prejuízo en el informe de Renta Fija. Recuerda que en conversaciones previas se acordó que Marcos M. y Marco P. plantearían una solución técnica tras revisar la tabla de movimientos. Adjunta capturas y un fichero. Detalles: Informe Operações com Títulos de Renda Fixa (Relatório de RENDA FIXA); columna en cuestión: Lucro / Prejuízo; fórmula señalada para el cálculo de RF: ((PU Venda) - (PU D0) * QTDE VENDIDA); referencia a la tabla de movimientos de Aldrin para la actualización del dato; las capturas muestran operaciones de compra, venta y depósito señalando las columnas Lucro / Prejuízo y Valor Líquido; fichero adjunto Relatorio RF_Amazonas_1026.xlsx · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, Relatorio RF_Amazonas_1026.xlsx
- 2026-11-05 13:29 — Correo automático — Continúa el hilo del [NFQBAU-1503](../Archivo/NFQBAU-1503%20—%202026-09-27%20—%20Informes%20de%20operaciones%20RF%20del%20Portal%20sin%20lucro-perjuicio%20ni%20valor%20de%20emisión.md), cerrado el 2026-09-28: no se reabre, se crea este. Marcos M., tecnología, consulta sobre el estado del ajuste del informe de renta fixa. Además, responde a José Carlos N., contabilidade de fundos del cliente, aclarando que el cálculo de ganancia/pérdida debe realizarse a nivel de activo u operación. Adjunta capturas.
- 2026-11-06 08:41 — Correo automático — Correo nuevo en el hilo: Antonio M., consultor de datos de NFQ, responde a Marcos M., tecnología, y José Carlos N., contabilidad de fondos del cliente, indicando que el desarrollo del ajuste en el informe se encontraba pausado. Solicita confirmación sobre si se debe priorizar la tarea para retomar los trabajos. Adjunta capturas. Detalles: Informe afectado: Operações com Títulos de Renda Fixa; Campos/columnas en discusión: Lucro / Prejuízo, Valor Líquido, PU Venda, PU D0, Quantidade; Capturas de pantalla: muestran el reporte impreso del cliente (S3 CACEIS) con operaciones de Compra a Termo, Depósito, Venda y Resgate marcando discrepancias y ceros en la columna de Lucro/Prejuízo; Fórmula mencionada en el hilo: ((PU Venda) - (PU D0) * QTDE VENDIDA) · Adjuntos del correo: image001.png, image002.png, image003.png, image006.png, image004.png, image005.png
- 2026-11-06 09:52 — Correo automático — Correo nuevo en el hilo: Marcos M., tecnología del cliente, solicita a Fernando M. incluir en la planificación y priorizar un ajuste en el informe de renta fija pedido por José Carlos N., contabilidad de fondos del cliente. El equipo de soporte técnico había dejado en pausa la tarea a la espera de confirmación para reanudarla. Adjunta capturas. Detalles: Informe: Operações com Títulos de Renda Fixa (ETF - Relatório de Operações RF); Campos/Columnas afectadas: Lucro / Prejuízo y Valor Líquido; Cálculo requerido a nivel de activo/operación ((PU Venda) - (PU D0) * QTDE VENDIDA); La captura adjunta muestra operaciones del cliente CUST4892 (periodo 01/05/2026 a 28/05/2026) resaltando las filas de tipo 'Depósito' con montos en 'Lucro / Prejuízo' y 'Valor Líquido' en 0,00 · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-11-06 09:57 — Correo automático — Correo nuevo en el hilo: Marcos M., tecnología del cliente, solicita incluir en la planificación y priorizar la corrección del informe de Renda Fixa solicitada previamente por José Carlos N., contabilidad de fondos del cliente. Adjunta capturas. Detalles: Informe: Operações com Títulos de Renda Fixa; La captura de pantalla muestra el informe emitido el 28/05/2026 (periodo 01/05/2026 a 28/05/2026) para el cliente CUST4892 - GRAO - CL U GRAO TEYA ITBR TES IPCA 2 ANO F IND RL; Destaca en rojo operaciones de tipo 'Depósito' donde la columna 'Valor Líquido' figura en 0,00 y 'Lucro / Prejuízo' registra saldos negativos; Fórmula de cálculo discutida: ((PU Venda) - (PU D0) * QTDE VENDIDA) a nivel de activo/operación · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png

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
- 2026-11-05 13:29 — nuevo → Abierto — Correo automático
- 2026-11-05 17:43 — Abierto → En curso — Marco Pichardo
- 2026-11-06 12:14 — nuevo → En curso — Matheus Fransoni

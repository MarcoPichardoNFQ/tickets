---
id: NFQBAU-1672
fecha_apertura: 2026-11-09
fecha_limite: 2026-11-10
fecha_resolucion:
estado: En curso
prioridad: Media
responsable:
origen: email
referencia_origen: Relatorios Swap (2026-11-09)
categoria:
  - Qlik
entorno:
  - Producción
sintoma: Los informes de swap del portal para datos de Megara en Producción muestran errores '#REF!' y valores en cero.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-12 11:08
actualizado_por: Correo automático
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Julio Cesar N., Controladoria, solicita evaluar los informes de swap del portal para los datos de Megara en Producción, ya que presentan inconsistencias. Adjunta capturas.

Detalles: Los informes 'Posição de SWAP' y 'Relatório de Memória de Cálculo Swap' para 'Fundo Master Megara' (cliente CUST2805) muestran errores. El informe 'Posição de SWAP' para CUST2805 presenta '#REF!' en campos como 'Total de Contratos sem Garantia', 'Valor', 'Aprop. Diária', 'Aprop. Acumulada', 'Ajuste Negativo', 'Contra Partida', 'Registro', 'Total do Ativo', 'Total do Passivo', 'Total do Compensado', 'Total de Net Positivo', 'Total de Net Negativo', 'Total de Net'. El 'Relatório de Memória de Cálculo Swap' para CUST2805 muestra valores de 0,00 y 0% para 'Alíquota de IRRF'. Los informes son para la 'Data da Posição: 03/11/2026 - 03/11/2026'.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png

## Histórico de interacciones

- 2026-11-09 16:16 — Correo automático — Julio Cesar N., Controladoria, solicita evaluar los informes de swap del portal para los datos de Megara en Producción, ya que presentan inconsistencias. Adjunta capturas.
- 2026-11-09 16:27 — Correo automático — Correo nuevo en el hilo: Fernando Augusto M., soporte, reenvía una solicitud de Julio Cesar N., contraloría de S3 Caceis, pidiendo evaluar los informes de swap en el portal para el sistema Megara en producción desde el 09/11/2026. Adjunta capturas. Detalles: Informe Posição de SWAP (emisión 09/11/2026 15:59:30, posición 03/11/2026) para cliente CUST3285 muestra '#REF!' en Principal, Valor, Aprop. Diária, Aprop. Acumulada, Ajuste Negativo y en los totales de Ativo, Passivo, Compensado y NET; Relatório de Memória de Cálculo Swap para CUST3285 muestra valores a cero; Posição de SWAP para CUST4647 muestra datos correctos con operación 42541. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png
- 2026-11-09 16:43 — Correo automático — Correo nuevo en el hilo: Matheus D., Developer III de NFQ, informa que están analizando la solicitud de Julio C. N., de Controladoria de S3 Caceis, para evaluar los informes de swap del portal en producción, que muestran errores. Adjunta capturas. Detalles: Los informes afectados son "Posição de SWAP" y "Relatório de Memória de Cálculo Swap" para los fondos Master Megara y Master SAC; las capturas muestran el error "#REF!" en varias celdas de los informes "Posição de SWAP" y "Relatório de Memória de Cálculo Swap"; una captura de "Posição de SWAP" para el cliente CUST285 muestra errores "#REF!"; otra captura de "Relatório de Memória de Cálculo Swap" para CUST285 también muestra errores "#REF!"; una tercera captura de "Posição de SWAP" para CUST74647 sí muestra datos. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png
- 2026-11-09 16:51 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, informa que la actividad de análisis de los informes de swap está en pausa porque su equipo fue llamado a atender un P0. Julio C. N., de Controladoria, había solicitado evaluar los informes de swap del portal para datos de Megara en Producción. Adjunta capturas. Detalles: Se solicita evaluar los informes de swap del portal para datos del Megara en Producción; Fondos afectados: Master Megara, Master SAC; Adjunta 7 capturas de pantalla; Las capturas muestran informes de 'Posição de SWAP' y 'Relatório de Memória de Cálculo Swap'; En 'Posição de SWAP' (Cliente: CUST74647), la fecha de emisión es 09/11/2026 y la fecha de posición 03/11/2026; En 'Relatório de Memória de Cálculo Swap' (Cliente: CUST285 - VX CAPITAL - APOLLO PROGRAM FIN CREDITO PRIVADO), la fecha de emisión es 09/11/2026 y la fecha de posición 03/11/2026; En 'Relatório de Memória de Cálculo Swap' (Cliente: CUST74647 - XP ADVISORY - CHRONOS FIM CP), la fecha de emisión es 09/11/2026 y la fecha de posición 03/11/2026. · Adjuntos del correo: image007.png, image006.png, image005.png, image003.png, image002.png, image004.png, image001.png
- 2026-11-09 16:55 — Correo automático — Correo nuevo en el hilo: Marco P., consultor senior de Nfq, comunica a Júlio C., del equipo de controladuría de S3 Caceis, que el análisis de los informes de swap se encuentra en pausa temporal.
Explica que deben atender una incidencia prioritaria (P0) y que retomarán la revisión tan pronto como queden liberados. Detalles: Atención prioritaria a incidencia P0; Capturas adjuntas de informes: 'Posição de SWAP' (cliente CUST4647, operación 42541, fecha de posición 03/11/2026) y 'Relatório de Memória de Cálculo Swap' (clientes CUST3285 - V8 CAPITAL y CUST4647 - XP ADVISORY, fecha de posición 03/11/2026) · Adjuntos del correo: image007.png, image006.png, image005.png, image003.png, image002.png, image004.png, image001.png
- 2026-11-09 17:24 — Correo automático — Correo nuevo en el hilo: Aparecida A. solicita verificar y mapear en Aldrin 14 campos para el informe BOOK SAT extraído del portal. Señala que estos datos son necesarios para el área de riesgo de la entidad. Detalles: Informe: BOOK SAT (portal); Sistema: Aldrin; Requiere mapeo para el área de riesgo (Yukio F.); Fecha de posición: 03-11-2026; Clientes/fondos analizados: FUNDO MASTER SAC (COD_CLIENTE CUST3285, V8 CAPITAL - APO11O PROGRAM FIM CREDITO PRIVADO) y FUNDO MASTER MEGARA (COD_CLIENTE CUST2303, CREDIT AGRICOLE - FUNDO A FIF); Campos identificados vacíos o pendientes de mapeo entre los que figuran: CODIGO, PAPEL, EMISSOR, QTDE_DISP, QTDE_BLOQ, PRECO_CUSTO, PRECO, CUSTO_TOTAL, RESULTADO, VALOR_MERC_BRUTO, IRRF, VALOR_MERC_LIQUIDO, CORRETORA, TIPO, PRECO_EXERCICIO, TIT_ASSOC, LASTRO, TAXA_OVER, PU_CURVA, TAXA_PAR, AGIO_DESAGIO, DATA_REPAC, VALOR_NOMINAL, TIR, COVERAGECCY · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png
- 2026-11-09 17:41 — Correo automático — Correo nuevo en el hilo: Marco P., Senior Consultant de NFQ, informa a Aparecida A. V., de PR Serviços, que el informe "Book SAC" está fuera del alcance de NFQ/SANCAC y sugiere contactar al proveedor del informe. También comunica a Julio C. N., Controladoria de S3caceis, que la actividad de análisis de los informes de swap está temporalmente en pausa porque su equipo está atendiendo un incidente P0. Adjunta capturas. Detalles: Marco P. indica que el informe "Book SAC" está fuera del alcance de NFQ/SANCAC; La actividad de análisis de los informes de swap está en pausa debido a un incidente P0; Aparecida A. V. solicitó verificar/mapear 14 campos en Aldrin para el informe "BOOK SAT", incluyendo: BASE_ATIVO, INDEX_ATIVO, TAXA_MTM, CURVA_ATIVO, VALOR_ATIVO, GARANTIA_ATIVO, BASE_PASSIVO, INDEX_PASSIVO, TAXA_MTM_PASSIVO, CURVA_PASSIVO, VALOR_PASSIVO, GARANTIA_PASSIVO, VL_FUTURO_ATIVO, VL_FUTURO_PASSIVO; Adjunta capturas de "Posição de SWAP" y "Relatório de Memória de Cálculo Swap" para clientes CUST3285 y CUST74647, con fecha de posición 03/11/2026; La primera captura de "Posição de SWAP" para CUST3285 muestra errores #REF!; la tercera captura de "Posição de SWAP" para CUST74647 muestra valores como Principal 6.000.000,00, Total do Ativo 8.472.024,75, Total do Passivo 9.156.380,63. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png
- 2026-11-09 17:41 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, responde que el informe Book SAC está fuera del alcance contratado y sugiere contactar al proveedor. Asimismo, informa a Julio C., controlador de S3 Caceis, que el análisis de reportes de swap se encuentra pausado por atender un incidente P0. Adjunta capturas. Detalles: La captura de Posição de SWAP muestra valores #REF! en Total de Contratos sem Garantia, TOTAL DO ATIVO, TOTAL DO PASSIVO, TOTAL DO COMPENSADO y TOTAL DE NET para el cliente CUST3285; El informe Relatório de Memória de Cálculo Swap aparece sin datos de cálculo para cliente CUST3285; Fundo Master Megara y Fundo Master SAC afectados; Actividad pausada temporalmente debido a la atención de incidente P0 · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png
- 2026-11-09 18:04 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, informa de que han sido convocados a las 18:00 h en la sala P0 para revisar una incidencia crítica. Señala que posteriormente retomarán la atención de la solicitud en curso. Detalles: Convocatoria a las 18:00 h en sala P0 para atender un incidente urgente antes de dar continuidad a la solicitud · Adjuntos del correo: image001.png, image002.png, image004.png, image006.png, image005.png, image007.png, image003.png
- 2026-11-11 14:21 — Correo automático — Correo nuevo en el hilo: Júlio C., controladoría de S3 Caceis, consulta a Marco P. si ya disponen de un diagnóstico sobre los errores detectados en los informes de Swap del portal en producción. La revisión había quedado pausada previamente y el cliente solicita actualización. Adjunta capturas. Detalles: Informes afectados: 'Posição de SWAP' y 'Relatório de Memória de Cálculo Swap'; Fondos/Clientes: CUST3285 (V8 CAPITAL - APO11O PROGRAM FIM CREDITO PRIVADO), Fundo Master Megara y Fundo MASTER SAC; Fecha de datos: 03/11/2026; Muestras en capturas: El informe 'Posição de SWAP' despliega celdas con errores '#REF!' en partidas y totales (Activo, Passivo, NET); el 'Relatório de Memória de Cálculo Swap' no muestra registros calculados (valores a 0,00); · Adjuntos del correo: ~WRD0003.jpg, image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png
- 2026-11-11 14:27 — Correo automático — Correo nuevo en el hilo: Kleverson B., de Tecnología, y Julio C. N., de Controladoria, preguntan a Marco P. si ya hay un diagnóstico para los informes de Swap, indicando que es urgente. Anteriormente, Marco P. había informado que el informe 'Book SAC' estaba fuera de alcance y que la actividad de análisis de informes estaba en pausa debido a un incidente P0. Aparecida A., de PR Serviços, había solicitado verificar 14 campos en Aldrin para el informe 'BOOK SAT' para el área de Riesgo de S3caceis, Yukio F. Adjunta capturas. Detalles: Los informes 'Posição de SWAP' y 'Relatório de Memória de Cálculo Swap' muestran errores #REF! y valores en blanco; Los informes corresponden a 'Fundo Master Megara' y 'Fundo MASTER SAC'; La fecha de los datos afectados es 03-11-2026; Se solicita verificar/mapear en Aldrin una lista de campos para el informe 'BOOK SAT' para el área de Riesgo de S3caceis; Marco P. indicó previamente que el informe 'Book SAC' está fuera del alcance; La actividad de análisis de informes fue pausada por un incidente P0. · Adjuntos del correo: image003.png, image004.png, image005.png, image008.png, image009.png, image010.jpg, image011.png, image012.png
- 2026-11-11 14:36 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, informa a Kleverson B., del área de tecnología del cliente, que la revisión de los informes de Swap se pausó temporalmente por otras solicitudes. Indica que el análisis continúa y avisará lo antes posible. Adjunta capturas. Detalles: Informes afectados: Relatório de Memória de Cálculo Swap y Posição de SWAP; Errores observados: celdas con #REF! en totales de activo, passivo y neto, valores en cero; Cliente CUST3285 - V8 CAPITAL - APO11O PROGRAM FIM CREDITO PRIVADO; Fecha de posición: 03/11/2026; Capturas muestran reporte sin datos procesados correctamente y errores de referencia · Adjuntos del correo: image003.png, image005.png, image009.png, image004.png, image008.png, image010.jpg
- 2026-11-11 17:11 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, solicita la validación y el test del informe 'Memória de Cálculo SWAP' y actualiza que el análisis del informe 'Posição SWAP' sigue en curso. Este seguimiento se da tras una consulta de Julio C., de Controladoria, y Kleverson B., de Tecnología, sobre el diagnóstico de los informes, que fue declarado urgente por Kleverson B. Adjunta capturas. Detalles: Solicita validación y test del informe 'Memória de Cálculo SWAP'; el informe 'Posição SWAP' está en análisis. Adjunta capturas de ambos informes. La captura del 'Relatório de Memória de Cálculo Swap' muestra datos vacíos o en 0,00 para la fecha de posición 03/11/2026. La captura del 'Posição de SWAP' muestra errores '#REF!' en varias columnas y totales para la fecha de posición 03/11/2026. · Adjuntos del correo: image003.png, image009.png, image005.png, image004.png, image008.png, image010.jpg
- 2026-11-11 19:46 — Correo automático — Correo nuevo en el hilo: Fernando M., de S3 Caceis, solicita a Julio C. N., de S3 Caceis, que valide el informe de Memória de Cálculo SWAP. También pide a Marco J. P., de NFQ, una previsión para la conclusión del análisis y ajuste del informe de Posição SWAP. Adjunta capturas. Detalles: Los informes afectados son 'Memória de Cálculo SWAP' y 'Posição SWAP'. Las capturas de pantalla muestran el informe 'Posição de SWAP' con valores '#REF!' en campos como 'Total de Contratos sem Garantia', 'Principal', 'Indexador', 'Tx. % AA', 'MTM % AA', 'J A D', 'Aniv', 'Valor', 'Aprop. Diária', 'Aprop. Acumulada', 'Ajuste Negativo', 'Contra Partida', 'Registro', 'TOTAL DO ATIVO', 'TOTAL DO PASSIVO', 'TOTAL DO COMPENSADO', 'TOTAL DE NET POSITIVO', 'TOTAL DE NET NEGATIVO', 'TOTAL DE NET'. La captura del informe 'Relatório de Memória de Cálculo Swap' también muestra valores en cero o vacíos. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.jpg
- 2026-11-11 19:46 — Correo automático — Correo nuevo en el hilo: Fernando M., de S3 Caceis, solicita a Julio César N., de controloría del cliente, que valide el informe de Memória de Cálculo SWAP. Asimismo, pide a Marco P., consultor de NFQ, una estimación de cuándo concluirá el análisis y ajuste del informe de Posição SWAP. Detalles: Relatório de Posição de SWAP muestra errores #REF! en Total de Contratos sem Garantia, Total do Ativo, Total do Passivo, Total do Compensado y Total de Net; Relatório de Memória de Cálculo Swap muestra valores en cero en todas sus columnas; Cliente CUST3285 - V8 CAPITAL - APO11O PROGRAM FIM CREDITO PRIVADO; Fecha de posición 03/11/2026; Fecha de emisión 09/11/2026 · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.jpg
- 2026-11-12 11:08 — Correo automático — Correo nuevo en el hilo: Júlio César N., controladoría del cliente, confirma que el informe Memória de Cálculo SWAP ha sido validado correctamente.
No obstante, señala que el informe Posição de SWAP sigue con incidencias pendientes por resolver. Adjunta capturas. Detalles: Informe Memória de Cálculo Swap: validado correctamente para el cliente CUST3285 - V8 CAPITAL - APO11O PROGRAM FIM CREDITO PRIVADO (operación SWAP42541); Informe Posição de SWAP: la captura muestra valores '#REF!' en el Total de Contratos sem Garantia y en los totales de activo, pasivo, compensado y NET; Fecha de posición: 03/11/2026. · Adjuntos del correo: image007.png, image008.png, image009.png, image010.png, image011.png, image012.png, image013.jpg

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
- 2026-11-09 16:16 — nuevo → Abierto — Correo automático
- 2026-11-09 20:16 — Abierto → En curso — Marco Pichardo

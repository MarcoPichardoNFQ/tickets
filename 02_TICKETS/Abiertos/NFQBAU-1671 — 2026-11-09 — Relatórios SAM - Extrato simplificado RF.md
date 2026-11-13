---
id: NFQBAU-1671
fecha_apertura: 2026-11-09
fecha_limite: 2026-11-10
fecha_resolucion:
estado: Pruebas cliente UAT
prioridad: Media
responsable:
origen: email
referencia_origen: Relatórios SAM - Extrato simplificado RF (2026-11-09)
categoria:
  - Otros
entorno: [UAT]
sintoma: Error 'Falha ao gerar relatório' al intentar generar el informe 'Extrato Simplificado' desde el portal.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-09 20:16
actualizado_por: Marco Pichardo
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Kleverson B. consulta al equipo de soporte cuál es el problema que impide generar el extracto solicitado que sigue fallando. Adjunta capturas del error.

Detalles: Portal: s3caceis.com.br/portal/active-report/reports/reports; Informe: Extrato Simplificado; Mensaje de error: 'Falha ao gerar relatório. Tente novamente mais tarde. SimplifiedExtract [GFFQ]'; Búsqueda de fondo: 1709; Fondo/Portafolio seleccionado: CUST1709 (LEGACY - LEGACY CAPITAL MASTER CLASSE DE INV. FIM RL SANTANDER ICATU); Última fecha indicada: 23/10/2026
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png

## Histórico de interacciones

- 2026-11-09 14:48 — Correo automático — Kleverson B. consulta al equipo de soporte cuál es el problema que impide generar el extracto solicitado que sigue fallando. Adjunta capturas del error.
- 2026-11-09 14:52 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, informa a Kleverson B. que está analizando la falla reportada al generar el informe Extrato Simplificado y responderá lo antes posible. La consulta venía siendo intentada por el cliente sin éxito. Detalles: La captura de pantalla del portal de informes muestra el mensaje de error literal: 'Falha ao gerar relatório. Tente novamente mais tarde. SimplifiedExtract [GFFQ]'; Informe seleccionado: Extrato Simplificado; Fondo/Portafolio afectado: CUST1709 (LEGACY - LEGACY CAPITAL MASTER CLASSE DE INV. FIM RL SANTANDER ICATU); Fecha de fondo: 23/10/2026. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-11-09 14:53 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, informa a Kleverson B., de S3 Caceis, que está analizando la incidencia en ese momento.
Indica que le dará una respuesta con novedades a la mayor brevedad. Detalles: Captura de pantalla en el portal de reportes (/portal/active-report/reports/reports); Mensaje de error: 'Falha ao gerar relatório. Tente novamente mais tarde. SimplifiedExtract [GFFQ]'; Informe: Extrato Simplificado; Cartera consultada: CUST1709 (LEGACY CAPITAL MASTER CLASSE DE INV. FIM RL SANTANDER ICATU); Última fecha de fondo mostrada: 23/10/2026 · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-11-09 15:02 — Correo automático — Correo nuevo en el hilo: Marco P., Senior Consultant de NFQ, informa a Kleverson B. que han encontrado la causa de la incidencia y están trabajando para resolverla. El problema es que el informe "Extrato Simplificado RF" no se genera. Silvia L., de Servicios & Soporte, reportó el problema el viernes y aún no puede consultarlo. Adjunta capturas. Detalles: El error literal es "Falha ao gerar relatório. Tente novamente mais tarde. SimplifiedExtract [GFFQ]"; La causa es la configuración de un calendario de ayuda que permite generar el informe incluso cuando el cliente no tiene información para mostrar; El informe afectado es "Extrato Simplificado"; Adjunta capturas que muestran la pantalla de "Relatórios" con el "Extrato Simplificado" seleccionado y el mensaje de error en rojo. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-11-09 15:31 — Correo automático — Correo nuevo en el hilo: Silvia L., de Servicios & Suporte, pregunta por el plazo de resolución de un problema con el informe "Extrato simplificado RF" que no se puede generar. Marco P., consultor de NFQ, ha encontrado la causa del problema y está trabajando para resolverlo. El problema se reportó el viernes anterior. Adjunta capturas. Detalles: El informe afectado es "Extrato simplificado RF" o "SimplifiedExtract". El mensaje de error literal es "Falha ao gerar relatório. Tente novamente mais tarde. SimplifiedExtract [GFFQ]". El problema se debe a la configuración de un calendario de ayuda que permite generar el informe incluso sin datos. El fondo afectado es CUST1709. Las capturas de pantalla muestran la interfaz de "Relatórios" con el "Extrato Simplificado" seleccionado y el mensaje de error en rojo. · Adjuntos del correo: ~WRD0001.jpg, image001.png, image002.png, image003.png, image004.png
- 2026-11-09 15:36 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, informa a Silvia L., de Servicios & Soporte de S3 Caceis, que están implementando las soluciones para el problema del informe "Extrato Simplificado RF" y que el ajuste debería estar disponible hoy mismo. Silvia L. había preguntado por el plazo. El problema se originó por la configuración de un calendario de ayuda. Adjunta capturas. Detalles: El error literal es "Falha ao gerar relatório. Tente novamente mais tarde. SimplifiedExtract [GFFQ]". El problema se debe a la configuración de un calendario de ayuda que permite generar el informe incluso sin datos. La captura muestra la pantalla de "Relatórios" con la opción "Extrato Simplificado" seleccionada y un mensaje de error en rojo en la parte superior. · Adjuntos del correo: ~WRD0001.jpg, image001.png, image002.png, image003.png, image004.png
- 2026-11-09 15:37 — Correo automático — Correo nuevo en el hilo: Guilherme V., Tecnología, pregunta a Marco P. si la solución para los errores genéricos "GFFQ" en la generación de informes en el Portal será definitiva o puntual, y si el error puede reincidir. Adjunta capturas. Detalles: El error "GFFQ" ocurre al generar el informe "Extrato Simplificado" en el Portal; El mensaje de error literal es "Falha ao gerar relatório. Tente novamente mais tarde. SimplifiedExtract [GFFQ]"; La incidencia se debe a la configuración de un calendario de ayuda que permite generar el informe incluso cuando el cliente no tiene información para mostrar; Las capturas de pantalla muestran la pantalla de "Relatórios" con el informe "Extrato Simplificado" seleccionado y el mensaje de error en rojo. · Adjuntos del correo: image001.png, image002.png, image003.png, image005.jpg, image006.png
- 2026-11-09 15:47 — Correo automático — Correo nuevo en el hilo: Marco P., consultor senior, informa a Guilherme V., de Tecnología, que la solución para el problema del informe "Extrato simplificado RF" será definitiva. Guilherme V. había preguntado si la solución sería puntual o definitiva, y Silvia L., de Servicios & Soporte, había solicitado un plazo para la resolución del problema que impedía consultar el informe desde el viernes. Adjunta capturas. Detalles: El informe afectado es "Extrato simplificado RF". El mensaje de error literal es "Falha ao gerar relatório. Tente novamente mais tarde. SimplifiedExtract [GFFQ]". El problema se debe a la configuración de un "calendário de ajuda" que permite generar el informe incluso cuando el cliente no tiene información para mostrar. La captura de pantalla muestra la interfaz del portal con la opción "Extrato Simplificado" marcada y un cuadro de error rojo en la parte superior que dice "Falha ao gerar relatório. Tente novamente mais tarde. SimplifiedExtract [GFFQ]". · Adjuntos del correo: image001.png, image002.png, image003.png, image005.jpg, image006.png
- 2026-11-09 17:52 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, informa que los ajustes para resolver la incidencia han sido realizados y solicita que se valide nuevamente el informe. El problema original era un error genérico 'GFFQ' al generar el 'Extrato simplificado RF' en el Portal. Adjunta capturas. Detalles: Mensaje de error: 'Falha ao gerar relatório. Tente novamente mais tarde. SimplifiedExtract [GFFQ]'; Informe afectado: 'Extrato Simplificado RF' (SimplifiedExtract); La captura muestra la pantalla del portal de informes con el error al intentar generar el 'Extrato Simplificado'. · Adjuntos del correo: image001.png, image002.png, image003.png, image005.jpg, image006.png

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
- 2026-11-09 14:48 — nuevo → Abierto — Correo automático
- 2026-11-09 20:16 — Abierto → Pruebas cliente UAT — Marco Pichardo

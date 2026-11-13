---
id: NFQBAU-1615
fecha_apertura: 2026-11-03
fecha_limite: 2026-11-06
fecha_resolucion: 2026-11-03
estado: Resuelto
prioridad: Baja
responsable: Matheus Fransoni
origen: email
referencia_origen: Demonstrativo de Caixa CUST4040 (2026-11-03)
categoria:
  - Qlik
entorno: []
sintoma: Solicitud de extracción del informe demostrativo de caja CUST4040 en formato PDF o Excel.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-03 17:53
actualizado_por: Matheus Fransoni
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marcela C., tecnología, solicita la extracción del demostrativo de caja en formato PDF o Excel para el código CUST4040. El periodo requerido abarca de mayo a diciembre de 2025. Adjunta capturas.

Detalles: Código: CUST4040; Formato solicitado: PDF/Excel; Periodo de datos: Mayo a Diciembre / 2025
Adjuntos del correo: image001.png, image002.png

## Histórico de interacciones

- 2026-11-03 12:37 — Correo automático — Marcela C., tecnología, solicita la extracción del demostrativo de caja en formato PDF o Excel para el código CUST4040. El periodo requerido abarca de mayo a diciembre de 2025. Adjunta capturas.
- 2026-11-03 12:53 — Correo automático — Correo nuevo en el hilo: Marcela C., de Tecnología, solicita la extracción de un demonstrativo de caja para el periodo de mayo a diciembre de 2025. Matheus D., Developer III, informa que la solicitud será atendida en el ticket NFQBAU1615. Adjunta capturas. Detalles: Nombre del informe: CUST4040; Periodo de los datos: Mayo a Diciembre de 2025; La solicitud se atenderá en el ticket NFQBAU1615. · Adjuntos del correo: image001.png, image002.png
- 2026-11-03 13:36 — Correo automático — Correo nuevo en el hilo: Matheus D., Developer III de NFQ, ha enviado a Marcela C., Tecnología de Sancac, el informe 'Demonstrativo de Caixa' solicitado para el cliente CUST4040 y el periodo de mayo a diciembre de 2025. La solicitud se gestiona bajo el ticket NFQBAU1615. Adjunta capturas y ficheros. Detalles: Informe: 'Demonstrativo de Caixa'; Cliente: CUST4040; Periodo de datos: Mayo a Diciembre de 2025; Formatos adjuntos: PDF y XLSX; Ticket ID: NFQBAU1615; Capturas de pantalla muestran la primera página del 'Demonstrativo de Caixa' con fecha de emisión 2026-11-03 13:29:47 y fecha de posición 16/05/2025 - 31/12/2025 para el cliente CUST4040 - XP ADVISORY - ENDEAVOR BRASIL FIM CP. · Adjuntos del correo: image001.png, image002.png, Demostrativo Caixa20261103132941.pdf, Demostrativo Caixa20261103133040.xlsx

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
- 2026-11-03 12:37 — nuevo → Abierto — Correo automático
- 2026-11-03 12:43 — Abierto → En curso — Matheus Fransoni
- 2026-11-03 17:53 — En curso → Resuelto — Matheus Fransoni

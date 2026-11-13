---
id: NFQBAU-1565
fecha_apertura: 2026-10-23
fecha_limite: 2026-10-26
fecha_resolucion: 2026-10-26
estado: Resuelto
prioridad: Baja
responsable: Marco Pichardo
origen: email
referencia_origen: Demonstrativo de Caixa - MAMS FIA CUST4327 (2026-10-23)
categoria:
  - Qlik
entorno: []
sintoma: Solicitud de generación y extracción del informe Demonstrativo de Caixa en formato PDF y Excel.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-26 17:25
actualizado_por: Marco Pichardo
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marcela C., del área de Tecnología, solicita el envío del informe Demonstrativo de Caixa para la cartera MAMS FIA CUST4327. Pide los archivos en formato PDF y Excel correspondientes al período desde enero de 2026 hasta la fecha más reciente.

Detalles: Informe: Demonstrativo de Caixa; Cartera / Fondo: MAMS FIA CUST4327; Periodo solicitado: desde enero de 2026 hasta la fecha actual; Formatos requeridos: PDF y Excel
Adjuntos del correo: image001.png, image002.png

## Histórico de interacciones

- 2026-10-23 14:19 — Correo automático — Marcela C., del área de Tecnología, solicita el envío del informe Demonstrativo de Caixa para la cartera MAMS FIA CUST4327. Pide los archivos en formato PDF y Excel correspondientes al período desde enero de 2026 hasta la fecha más reciente.
- 2026-10-23 14:30 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, responde a la solicitud indicando que será gestionada bajo un número de ticket específico. Detalles: Ticket asociado: NFQBAU1565 · Adjuntos del correo: image001.png, image002.png
- 2026-10-23 14:56 — Correo automático — Correo nuevo en el hilo: Marco P., consultor senior de nfq, responde a la solicitud enviando el informe de caja requerido por Marcela C., del departamento de tecnología. Se hace entrega de los datos del fondo MAMS FIA CUST4327 correspondientes al periodo de enero a octubre de 2026. Adjunta un fichero. Detalles: Ticket asociado: NFQBAU1565; Informe: Demonstrativo de Caixa; Cliente/Fondo: CUST4327 - XP ADVISORY - MAMS FIA; Fecha de posición: 02/01/2026 a 23/10/2026; Fecha de emisión: 23/10/2026 14:48:26; Archivos enviados: Demostrativo Caixa20261023144815.xlsx y Demostrativo Caixa20261023144822.pdf · Adjuntos del correo: image001.png, image002.png, Demostrativo Caixa20261023144815.xlsx, Demostrativo Caixa20261023144822.pdf

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
- 2026-10-23 14:19 — nuevo → Abierto — Correo automático
- 2026-10-26 17:25 — Abierto → Resuelto — Marco Pichardo

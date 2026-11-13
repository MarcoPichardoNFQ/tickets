---
id: NFQBAU-1639
fecha_apertura: 2026-11-04
fecha_limite: 2026-11-07
fecha_resolucion: 2026-11-05
estado: Resuelto
prioridad: Baja
responsable: Marco Pichardo
origen: email
referencia_origen: Dúvida de relatórios (2026-11-04)
categoria:
  - Qlik
entorno: []
sintoma: Consulta sobre el plazo máximo para generar informes Qlik
solucion_corta: "Se aclaró que el límite para generar informes Qlik es de 200 días y se indicó que puede ampliarse."
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-06 22:43
actualizado_por: Marco Pichardo
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Kleverson B., del cliente, pregunta sobre el plazo máximo para generar informes Qlik. Quiere saber si el límite es de 120 días o más.

Detalles: El remitente pregunta si el plazo máximo para generar informes Qlik es de 120 días o más.

## Histórico de interacciones

- 2026-11-04 20:11 — Correo automático — Kleverson B., del cliente, pregunta sobre el plazo máximo para generar informes Qlik. Quiere saber si el límite es de 120 días o más.
- 2026-11-04 20:16 — Correo automático — Correo nuevo en el hilo: Marco P., consultor, responde a una duda formulada por Kleverson B. acerca del período máximo de generación de informes en Qlik. Le aclara que el límite actual está fijado en 200 días y que es posible aumentarlo en unos 5 minutos si fuera necesario. Detalles: Herramienta: Qlik; Límite actual de generación de informes: 200 días; Tiempo estimado para ampliar el límite: 5 minutos
- 2026-11-06 21:06 — Correo automático — Resolución redactada automáticamente a partir del histórico; revisar.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Kleverson B. consultó sobre el plazo máximo para generar informes Qlik., Marco P. respondió a la consulta aclarando que el límite actual es de 200 días., Se informó que dicho límite se puede aumentar en aproximadamente 5 minutos de ser necesario.

### Cómo se comprobó

No consta en el histórico.

### Con quién se habló

Kleverson B., del cliente, Marco P., consultor

### Servicios, jobs o tablas tocados

informes Qlik

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-11-04 20:11 — nuevo → Abierto — Correo automático
- 2026-11-05 12:24 — Abierto → Resuelto — Marco Pichardo
- 2026-11-06 12:14 — nuevo → Resuelto — Matheus Fransoni

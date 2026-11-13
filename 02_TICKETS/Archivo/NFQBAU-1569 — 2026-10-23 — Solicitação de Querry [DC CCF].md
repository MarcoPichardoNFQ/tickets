---
id: NFQBAU-1569
fecha_apertura: 2026-10-23
fecha_limite: 2026-10-26
fecha_resolucion: 2026-11-05
estado: Resuelto
prioridad: Baja
responsable: Marco Pichardo
origen: email
referencia_origen: Solicitação de Querry [DC CCF] (2026-10-23)
categoria:
  - BBDD
entorno: []
sintoma: Se solicita la query utilizada para generar informes.
solucion_corta:
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
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Lucas C., de Tecnología de PR Serviços, solicita la query utilizada para generar los informes 'Demonstrativo de caixa' y 'Composição da Carteira de Fundos'. Adjunta capturas.

Detalles: Se solicita la query para los informes 'Demonstrativo de caixa' y 'Composição da Carteira de Fundos'.
Adjuntos del correo: image.png

## Histórico de interacciones

- 2026-10-23 16:56 — Correo automático — Lucas C., de Tecnología de PR Serviços, solicita la query utilizada para generar los informes 'Demonstrativo de caixa' y 'Composição da Carteira de Fundos'. Adjunta capturas.

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
- 2026-10-23 16:56 — (vacío) → Abierto — Correo automático
- 2026-11-05 12:24 — Abierto → Resuelto — Marco Pichardo
- 2026-11-06 12:14 — Abierto → Resuelto — Matheus Fransoni

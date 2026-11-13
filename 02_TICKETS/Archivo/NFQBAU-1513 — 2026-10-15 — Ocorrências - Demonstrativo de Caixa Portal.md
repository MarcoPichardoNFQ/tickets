---
id: NFQBAU-1513
fecha_apertura: 2026-10-15
fecha_limite: 2026-10-16
fecha_resolucion: 2026-10-15
estado: Resuelto
prioridad: Media
responsable: Ricardo Reyes
origen: email
referencia_origen: Ocorrências - Demonstrativo de Caixa Portal (2026-10-14)
categoria: []
entorno: []
sintoma: el informe Demonstrativo de Caixa muestra un saldo final incorrecto por la mañana que se corrige automáticamente más tarde sin intervención
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-15 15:33
actualizado_por: Ricardo Reyes
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Correo automático'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Christian S., del área de tecnología, reporta un problema recurrente donde el saldo final del Demonstrativo de Caixa para SAM aparece incorrecto por la mañana y se autoajusta tiempo después, solicitando un análisis detallado del caso.

## Histórico de interacciones

- 2026-10-15 15:25 — Correo automático — Christian S., del área de tecnología, reporta un problema recurrente donde el saldo final del Demonstrativo de Caixa para SAM aparece incorrecto por la mañana y se autoajusta tiempo después, solicitando un análisis detallado del caso.

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
- 2026-10-15 15:25 — nuevo → Abierto — Correo automático
- 2026-10-15 15:33 — Abierto → Resuelto — Ricardo Reyes

---
id: NFQBAU-1514
fecha_apertura: 2026-10-15
fecha_limite: 2026-10-16
fecha_resolucion: 2026-10-15
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: "[Aldrin] Problema demonstrativo de caixa (2026-10-15)"
categoria: []                # Rundeck | BBDD | Qlik | APIs | Otros
entorno: []                  # Producción | UAT
sintoma: "El informe demonstrativo de caixa no presenta el saldo actualizado y muestra un valor diferente para el fondo CUST1111 en la fecha de hoy."
solucion_corta: "ticket de prueba del correo automático; sin acción"
codigo_relacionado:
  - repo:
    modulo:
    version:                 # tag de PRD cuando se despliegue
tickets_proveedor: []        # notas de 03_PROVEEDORES
decision_relacionada:
referencias_tecnicas: []     # fichas de 00_REFERENCIA_TECNICA que ayudaron
actualizado: 2026-10-17 16:13
actualizado_por: Ricardo Reyes
tags: [ticket, bau]
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Correo automático'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marco P., Senior Consultant, pide que se revise el informe demonstrativo de caixa debido a que el saldo no se muestra actualizado y el registro del fondo CUST1111 presenta un valor incorrecto para la fecha de hoy.

## Histórico de interacciones

- 2026-10-15 16:40 — Correo automático — Marco P., Senior Consultant, pide que se revise el informe demonstrativo de caixa debido a que el saldo no se muestra actualizado y el registro del fondo CUST1111 presenta un valor incorrecto para la fecha de hoy.

- 2026-10-15 16:53 — Ricardo Reyes — Cerrado: prueba del circuito de correo.

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
- 2026-10-15 16:40 — (vacío) → Abierto — Correo automático
- 2026-10-15 16:53 — Abierto → Resuelto — Ricardo Reyes

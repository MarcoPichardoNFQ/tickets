---
id: NFQBAU-1681
fecha_apertura: 2026-11-10
fecha_limite: 2026-11-11
fecha_resolucion:            # obligatoria al pasar a Resuelto
estado: Abierto              # ver 05_GENERAL/listas.json
prioridad: Media
responsable:                 # Nombre Apellido, igual que el fichero en 04_PERSONAS
origen: email
referencia_origen: "[ALDRIN BR] - Incencidass Saldos duplicados (2026-11-10)"
categoria: [BBDD]
entorno: []                  # Producción | UAT
sintoma: "Se detecta la presencia de saldos duplicados para el mismo cliente en la misma fecha provenientes tanto de fuentes de Megara como de SAC."
solucion_corta:              # una línea: qué lo arregló
codigo_relacionado:
  - repo:
    modulo:
    version:                 # tag de PRD cuando se despliegue
tickets_proveedor: []        # notas de 03_PROVEEDORES
decision_relacionada:
referencias_tecnicas: []     # fichas de 00_REFERENCIA_TECNICA que ayudaron
actualizado: 2026-11-10 16:02
actualizado_por: Correo automático
tags: [ticket, bau]
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marco P., consultor senior de NFQ, informa que han identificado saldos duplicados para un mismo cliente y fecha desde fuentes de Megara y SAC, aportando un listado detallado de los códigos de cliente, fechas de liquidación y cantidades afectadas.

Detalles: Presencia de saldos duplicados (Qtde 2) para el mismo cliente y fecha; Origen de los datos: fuentes de Megara y SAC; Códigos de cliente y fechas afectados: TCES36360 (2026-11-09), TCES110579 (2026-11-09), TCES36381 (2026-11-09), TCES32993 (2026-11-09), TCES109457 (2026-11-09), TCES110560 (2026-11-09), CUST3320 (2026-11-09, 2026-11-06, 2026-11-05, 2026-11-04, 2026-11-03, 2026-10-30, 2026-10-29, 2026-10-28, 2026-10-27, 2026-10-26, 2026-10-23, 2026-10-22, 2026-10-21, 2026-10-20, 2026-10-19, 2026-10-16, 2026-10-15, 2026-10-14, 2026-10-13), TCES43774 (2026-11-09), TCES39785 (2026-11-09), TCES38967 (2026-11-09), TCES38886 (2026-11-09), TCES38843 (2026-11-09), CUST4448 (2026-11-04, 2026-11-03, 2026-10-30, 2026-10-29, 2026-10-28, 2026-10-27), CUST4796 (2026-11-03), CUST4245 (2026-10-28, 2026-10-27, 2026-10-26), CUST4660 (2026-10-08, 2026-10-07, 2026-10-06, 2026-10-05, 2026-10-02), CUST4658 (2026-10-08, 2026-10-07, 2026-10-06, 2026-10-05, 2026-10-02).

## Histórico de interacciones

- 2026-11-10 16:02 — Correo automático — Marco P., consultor senior de NFQ, informa que han identificado saldos duplicados para un mismo cliente y fecha desde fuentes de Megara y SAC, aportando un listado detallado de los códigos de cliente, fechas de liquidación y cantidades afectadas.

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
- 2026-11-10 16:02 — nuevo → Abierto — Correo automático

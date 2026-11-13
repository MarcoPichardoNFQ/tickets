---
id: NFQBAU-1544
fecha_apertura: 2026-10-20
fecha_limite: 2026-10-21
fecha_resolucion: 2026-10-21
estado: Resuelto
prioridad: Media
responsable: Deborah Bertoldo
origen: email
referencia_origen: Atualização demonstrativo de caixa - CUST1157 (2026-10-20)
categoria:
  - Qlik
entorno: []
sintoma: El saldo del informe demonstrativo de caixa CUST1157 en Qlik no se actualiza tras realizar ajustes.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-21 01:29
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

Marcela C., del equipo de Tecnología, solicita revisar la actualización en Qlik del demonstrativo de caixa CUST1157 correspondiente al 07.10. Informa de que el saldo no se actualiza tras haberse realizado ajustes. Adjunta capturas.

Detalles: Informe: demonstrativo de caixa CUST1157; Herramienta: Qlik (Qclik); Fecha de los datos: 07.10; Problema reportado: saldo no actualiza tras ajustes
Adjuntos del correo: image001.png, image002.png

## Histórico de interacciones

- 2026-10-20 13:12 — Correo automático — Marcela C., del equipo de Tecnología, solicita revisar la actualización en Qlik del demonstrativo de caixa CUST1157 correspondiente al 07.10. Informa de que el saldo no se actualiza tras haberse realizado ajustes. Adjunta capturas.

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
- 2026-10-20 13:12 — nuevo → Abierto — Correo automático
- 2026-10-21 01:29 — Abierto → Resuelto — Marco Pichardo

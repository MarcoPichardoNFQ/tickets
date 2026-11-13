---
id: NFQBAU-1541
fecha_apertura: 2026-10-19
fecha_limite: 2026-10-20
fecha_resolucion: 2026-10-21
estado: Resuelto
prioridad: Media
responsable: Deborah Bertoldo
origen: email
referencia_origen: Demonstrativo de Caixa - CUST1157 -  saldo negativo errado (2026-10-19)
categoria:
  - Qlik
entorno: []
sintoma: El informe Demonstrativo de Caixa CUST1157 muestra un saldo negativo incorrecto.
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

Marcela C., tecnología, solicita revisar el demonstrativo de caixa CUST1157. Indica que desde el 07/10/26 muestra un saldo negativo de -180,95 que debería estar a cero, habiéndose regularizado el 19/10. Adjunta capturas.

Detalles: Informe: Demonstrativo de Caixa CUST1157; Saldo incorrecto: -180,95; Saldo esperado: 0,00; Periodo afectado: desde 07/10/26 hasta 19/10/26
Adjuntos del correo: image001.png, image002.png, image003.png

## Histórico de interacciones

- 2026-10-19 18:26 — Correo automático — Marcela C., tecnología, solicita revisar el demonstrativo de caixa CUST1157. Indica que desde el 07/10/26 muestra un saldo negativo de -180,95 que debería estar a cero, habiéndose regularizado el 19/10. Adjunta capturas.
- 2026-10-19 19:26 — Correo automático — Correo nuevo en el hilo: Marco P., consultor senior de NFQ, responde señalando que el fondo cuenta con saldos tanto de Megara como de SAC en la base de datos Aldrin, lo cual explica el valor registrado. Recomienda revisar el importe con los responsables correspondientes. Adjunta capturas. Detalles: Fondo: CUST1157; Base de datos: Aldrin; Orígenes de datos: Megara y SAC; La captura adjunta muestra los registros de saldo en la base de datos Aldrin · Adjuntos del correo: image001.png, image002.png, image003.png, image.png

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
- 2026-10-19 18:26 — nuevo → Abierto — Correo automático
- 2026-10-21 01:29 — Abierto → Resuelto — Marco Pichardo

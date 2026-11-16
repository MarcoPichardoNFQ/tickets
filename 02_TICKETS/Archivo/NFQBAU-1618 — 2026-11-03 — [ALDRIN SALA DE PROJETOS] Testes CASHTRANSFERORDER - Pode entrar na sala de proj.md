---
id: NFQBAU-1618
fecha_apertura: 2026-11-03
fecha_limite: 2026-11-04
fecha_resolucion: 2026-11-09
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: "[ALDRIN SALA DE PROJETOS] Testes CASHTRANSFERORDER - Pode entrar na sala de projetos. (2026-11-03)"
categoria:
  - BBDD
entorno:
  - UAT
sintoma: No se muestran datos en las tablas de extracción trf_s3.SSS_PURECASH_BOOK_T, trf_s3.SSS_PURECASH_OPIN_T y trf_s3.SSS_PURECASH_OPOUT_T tras cargar los ficheros.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-09 17:26
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

Matheus D., desarrollador de NFQ, confirma su asistencia a la sala de proyectos. En el mismo hilo, Ado G., del equipo de tecnología, solicita ayuda a Deborah B. para evaluar las pruebas de CASHTRANSFERORDER ya que no ve datos en las tablas indicadas por Marco P. desde el 3 de noviembre de 2026.

Detalles: Tablas afectadas: trf_s3.SSS_PURECASH_BOOK_T, trf_s3.SSS_PURECASH_OPIN_T, trf_s3.SSS_PURECASH_OPOUT_T; Proceso afectado: CASHTRANSFERORDER; adjunta capturas
Adjuntos del correo: image.png, image.png, image.png

## Histórico de interacciones

- 2026-11-03 16:06 — Correo automático — Matheus D., desarrollador de NFQ, confirma su asistencia a la sala de proyectos. En el mismo hilo, Ado G., del equipo de tecnología, solicita ayuda a Deborah B. para evaluar las pruebas de CASHTRANSFERORDER ya que no ve datos en las tablas indicadas por Marco P. desde el 3 de noviembre de 2026.

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
- 2026-11-03 16:06 — nuevo → Abierto — Correo automático
- 2026-11-04 16:02 — Abierto → Resuelto — Matheus Fransoni
- 2026-11-05 12:24 — Abierto → Pendiente despliegue UAT — Marco Pichardo
- 2026-11-06 12:14 — Resuelto → Pendiente despliegue UAT — Matheus Fransoni
- 2026-11-09 17:26 — Pendiente despliegue UAT → Resuelto — Matheus Fransoni

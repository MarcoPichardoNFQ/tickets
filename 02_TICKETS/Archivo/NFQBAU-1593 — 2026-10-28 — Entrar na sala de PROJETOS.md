---
id: NFQBAU-1593
fecha_apertura: 2026-10-28
fecha_limite: 2026-10-31
fecha_resolucion: 2026-10-29
estado: Resuelto
prioridad: Baja
responsable: Matheus Fransoni
origen: email
referencia_origen: Entrar na sala de PROJETOS (2026-10-28)
categoria: [Sala]
entorno:
  - UAT
  - Producción
sintoma: El remitente solicita acceso a la sala de PROJETOS.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-06 22:44
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

Continúa el hilo del [NFQBAU-1528](../Archivo/NFQBAU-1528%20—%202026-10-16%20—%20Entrar%20na%20sala%20de%20PROJETOS.md), cerrado el 2026-10-21: no se reabre, se crea este. Marcos M., Tecnología, pide a Matheus D., Deborah B. y Marco P. que entren en la sala de PROJETOS. Adjunta capturas.

Detalles: Sala de PROJETOS.
Adjuntos del correo: image001.png, image002.png, image003.png

## Histórico de interacciones

- 2026-10-28 16:12 — Correo automático — Continúa el hilo del [NFQBAU-1528](../Archivo/NFQBAU-1528%20—%202026-10-16%20—%20Entrar%20na%20sala%20de%20PROJETOS.md), cerrado el 2026-10-21: no se reabre, se crea este. Marcos M., Tecnología, pide a Matheus D., Deborah B. y Marco P. que entren en la sala de PROJETOS. Adjunta capturas.
- 2026-10-28 16:16 — Correo automático — Correo nuevo en el hilo: Matheus D., Developer III, responde a Marcos M., Tecnología, que está yendo a la sala de PROYECTOS. Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-10-28 17:51 — Correo automático — Correo nuevo en el hilo: Matheus D., Developer III de NFQ, solicita a Marcos M. revisar una modificación en la función `cs_cli_cash_account_transf_pc` para insertar el campo `dat_qlikupdate` y pide autorización para actualizar en UAT. Adjunta un fichero. Detalles: Función: `cs_cli_cash_account_transf_pc`; Campo a insertar: `dat_qlikupdate`; Entorno de actualización solicitado: UAT; Adjunta fichero `UPDATE cs_cli_cash_account_transf_pc.sql`. · Adjuntos del correo: image001.png, image002.png, image003.png, UPDATE cs_cli_cash_account_transf_pc.sql
- 2026-10-28 19:32 — Correo automático — Correo nuevo en el hilo: Marcos M., del área de tecnología del cliente, da su visto bueno para proceder con la actualización en el entorno de UAT.
Adjunta capturas. Detalles: Función cs_cli_cash_account_transf_pc; Inserción del campo dat_qlikupdate a cada nuevo registro · Adjuntos del correo: image001.png, image002.png, image003.png

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
- 2026-10-28 16:12 — nuevo → Abierto — Correo automático
- 2026-10-29 17:28 — Abierto → Pendiente despliegue PRD — Matheus Fransoni
- 2026-10-29 18:16 — Pendiente despliegue PRD → Resuelto — Matheus Fransoni

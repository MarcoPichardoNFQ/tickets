---
id: NFQBAU-1679
fecha_apertura: 2026-11-10
fecha_limite: 2026-11-10
fecha_resolucion: 2026-11-10
estado: Resuelto
prioridad: Alta
responsable:                 # Nombre Apellido, igual que el fichero en 04_PERSONAS
origen: email
referencia_origen: "Entrar em P0 (2026-11-10)"
categoria: [Sala]
entorno: []                  # Producción | UAT
sintoma: "Un proceso o estado relacionado con 'P0' necesita ser re-ejecutado o re-ingresado."
solucion_corta:              # una línea: qué lo arregló
codigo_relacionado:
  - repo:
    modulo:
    version:                 # tag de PRD cuando se despliegue
tickets_proveedor: []        # notas de 03_PROVEEDORES
decision_relacionada:
referencias_tecnicas: []     # fichas de 00_REFERENCIA_TECNICA que ayudaron
actualizado: 2026-11-10 13:43
actualizado_por: Correo automático
tags: [ticket, bau]
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marcela C., Tecnologia, solicita que se vuelva a entrar en P0. Adjunta capturas.

Detalles: Solicita entrar en P0; adjunta capturas
Adjuntos del correo: image001.png, image002.png

## Histórico de interacciones

- 2026-11-10 13:42 — Correo automático — Marcela C., Tecnologia, solicita que se vuelva a entrar en P0. Adjunta capturas.
- 2026-11-10 13:43 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador de NFQ, responde que ya se encarga, tras la petición previa de Marcela C., tecnología del cliente, para volver a entrar en P0. Adjunta dos ficheros. Detalles: Petición de entrar en P0 · Adjuntos del correo: image001.png, image002.png

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
- 2026-11-10 13:42 — nuevo → Resuelto — Correo automático

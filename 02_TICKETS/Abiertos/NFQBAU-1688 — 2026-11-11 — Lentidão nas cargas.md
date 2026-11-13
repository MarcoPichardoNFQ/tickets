---
id: NFQBAU-1688
fecha_apertura: 2026-11-11
fecha_limite: 2026-11-11
fecha_resolucion:            # obligatoria al pasar a Resuelto
estado: Abierto              # ver 05_GENERAL/listas.json
prioridad: Alta
responsable:                 # Nombre Apellido, igual que el fichero en 04_PERSONAS
origen: email
referencia_origen: "Lentidão nas cargas (2026-11-11)"
categoria: [Rundeck]
entorno: []                  # Producción | UAT
sintoma: "Lentitud en la ejecución de los procesos de carga."
solucion_corta:              # una línea: qué lo arregló
codigo_relacionado:
  - repo:
    modulo:
    version:                 # tag de PRD cuando se despliegue
tickets_proveedor: []        # notas de 03_PROVEEDORES
decision_relacionada:
referencias_tecnicas: []     # fichas de 00_REFERENCIA_TECNICA que ayudaron
actualizado: 2026-11-12 11:38
actualizado_por: Correo automático
tags: [ticket, bau]
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marcela C., del área de tecnología, solicita conectarse a una sesión de P0 debido a lentitud detectada en los procesos de carga.

Adjuntos del correo: image001.png, image002.png

## Histórico de interacciones

- 2026-11-11 11:48 — Correo automático — Marcela C., del área de tecnología, solicita conectarse a una sesión de P0 debido a lentitud detectada en los procesos de carga.
- 2026-11-11 11:51 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador de NFQ, responde avisando que se une a la llamada de P0. La incidencia venía precedida por un aviso de Marcela C., de tecnología del cliente, alertando de lentitud en las cargas. Detalles: Convocatoria a llamada de severidad P0 por lentitud en las cargas · Adjuntos del correo: image001.png, image002.png
- 2026-11-11 11:52 — Correo automático — Correo nuevo en el hilo: Marcela C., de Tecnología, solicita entrar en una sesión de soporte crítico P0.
Informa de que se está experimentando lentitud en las cargas. Detalles: Solicitud de atención para incidente crítico P0 por lentitud en las cargas · Adjuntos del correo: image001.png, image002.png
- 2026-11-11 11:52 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador, confirma que se incorpora a la llamada prioritaria para revisar la incidencia. Esto sucede a raíz de un reporte de Marcela C., de tecnología, solicitando atención P0 por lentitud en las cargas. Adjunta capturas. Detalles: Lentitud en las cargas ('Lentidão nas cargas'); solicitud de ingreso a P0 · Adjuntos del correo: image001.png, image002.png
- 2026-11-12 11:38 — Correo automático — Correo nuevo en el hilo: Marcela C., tecnología, informa que están experimentando una lentitud de 40 minutos en las cargas en el día de hoy. Pide al equipo de soporte que revisen lo ocurrido. Adjunta capturas. Detalles: Lentitud de 40 minutos en el proceso de cargas con fecha 2026-11-12 · Adjuntos del correo: image001.png, image002.png

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
- 2026-11-11 11:48 — nuevo → Abierto — Correo automático

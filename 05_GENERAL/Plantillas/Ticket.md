---
id: NFQBAU-NNNN
fecha_apertura: {{date}}
fecha_limite:                # la calcula el script o Templater según prioridad: Alta hoy, Media +1, Baja +3; plazo para asumirlo (pasar a En curso)
fecha_resolucion:            # obligatoria al pasar a Resuelto
estado: Abierto              # ver 05_GENERAL/listas.json
prioridad: Media             # Alta | Media | Baja
responsable:                 # Nombre Apellido, igual que el fichero en 04_PERSONAS
origen: email                # email | reunión | llamada
referencia_origen:           # asunto del correo tal cual, o nombre y fecha de la reunión
categoria: []                # Rundeck | BBDD | Qlik | APIs | Otros | Sala (petición de sala, la pone el correo)
entorno: []                  # Producción | UAT
sintoma:                     # una línea: cómo se manifestó
solucion_corta:              # una línea: qué lo arregló
codigo_relacionado:
  - repo:
    modulo:
    version:                 # tag de PRD cuando se despliegue
tickets_proveedor: []        # notas de 03_PROVEEDORES
decision_relacionada:
referencias_tecnicas: []     # fichas de 00_REFERENCIA_TECNICA que ayudaron
actualizado:                 # lo estampa el hook
actualizado_por:             # lo estampa el hook
tags: [ticket, bau]
---

{{controles}}

## Resumen

## Histórico de interacciones

- {{date}} {{time}} — Nombre Apellido — 

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

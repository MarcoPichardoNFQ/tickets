---
id: NFQBAU-1673
fecha_apertura: 2026-11-09
fecha_limite: 2026-11-12
fecha_resolucion: 2026-11-09
estado: Resuelto
prioridad: Baja
responsable:                 # Nombre Apellido, igual que el fichero en 04_PERSONAS
origen: email
referencia_origen: "Entrar na sala de PROJETOS (2026-11-09)"
categoria: [Sala]
entorno: []                  # Producción | UAT
sintoma: "Solicitud de acceso a la sala de PROJETOS."
solucion_corta:              # una línea: qué lo arregló
codigo_relacionado:
  - repo:
    modulo:
    version:                 # tag de PRD cuando se despliegue
tickets_proveedor: []        # notas de 03_PROVEEDORES
decision_relacionada:
referencias_tecnicas: []     # fichas de 00_REFERENCIA_TECNICA que ayudaron
actualizado: 2026-11-09 16:51
actualizado_por: Correo automático
tags: [ticket, bau]
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marcos M., Tecnología, solicita acceso a la sala de PROJETOS. Adjunta capturas.

Detalles: Solicita acceso a la 'sala de PROJETOS'.
Adjuntos del correo: image001.png, image002.png, image003.png

## Histórico de interacciones

- 2026-11-09 16:42 — Correo automático — Marcos M., Tecnología, solicita acceso a la sala de PROJETOS. Adjunta capturas.
- 2026-11-09 16:51 — Correo automático — Correo nuevo en el hilo: Matheus D., Developer III de NFQ, responde a Marcos M., de Tecnología de PR Serviços, confirmando que va a la sala de PROYECTOS. Adjunta capturas. Detalles: El remitente confirma "Estou indo" (Estoy yendo). Las capturas adjuntas son probablemente logos o firmas. · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-09 16:51 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador de NFQ, confirma que está acudiendo a la sala de proyectos solicitada previamente por Marcos M., del área de tecnología. No se plantea ninguna petición operativa ni técnica. Adjuntos del correo: image001.png, image002.png, image003.png

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
- 2026-11-09 16:42 — nuevo → Resuelto — Correo automático

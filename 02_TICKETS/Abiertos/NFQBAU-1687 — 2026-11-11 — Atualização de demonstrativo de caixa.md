---
id: NFQBAU-1687
fecha_apertura: 2026-11-11
fecha_limite: 2026-11-12
fecha_resolucion:            # obligatoria al pasar a Resuelto
estado: Abierto              # ver 05_GENERAL/listas.json
prioridad: Media
responsable:                 # Nombre Apellido, igual que el fichero en 04_PERSONAS
origen: email
referencia_origen: "Atualização de demonstrativo de caixa (2026-11-11)"
categoria: [Qlik]
entorno: []                  # Producción | UAT
sintoma: "Se solicita la recarga del informe demonstrativo de caixa para fondos y fechas específicas."
solucion_corta:              # una línea: qué lo arregló
codigo_relacionado:
  - repo:
    modulo:
    version:                 # tag de PRD cuando se despliegue
tickets_proveedor: []        # notas de 03_PROVEEDORES
decision_relacionada:
referencias_tecnicas: []     # fichas de 00_REFERENCIA_TECNICA que ayudaron
actualizado: 2026-11-11 08:45
actualizado_por: Correo automático
tags: [ticket, bau]
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Kleverson B., de NFQ, solicita recargar el demonstrativo de caixa para los fondos Cust4805 y Cust4520. La petición corresponde a fechas puntuales de noviembre.

Detalles: Fondos y fechas a recargar: Cust4805 (09/11); Cust4520 (06/11 y 09/11)

## Histórico de interacciones

- 2026-11-11 04:34 — Correo automático — Kleverson B., de NFQ, solicita recargar el demonstrativo de caixa para los fondos Cust4805 y Cust4520. La petición corresponde a fechas puntuales de noviembre.
- 2026-11-11 08:45 — Correo automático — Correo nuevo en el hilo: Manuel H., desarrollador del equipo de soporte, confirma que ya se han actualizado los datos de los fondos indicados en el demonstrativo de caixa. Queda a disposición por si necesitan información adicional. Detalles: Actualización de información en demonstrativo de caixa; fondos afectados en el hilo: Cust4805 (09/11) y Cust4520 (06/11 y 09/11)

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
- 2026-11-11 04:34 — nuevo → Abierto — Correo automático

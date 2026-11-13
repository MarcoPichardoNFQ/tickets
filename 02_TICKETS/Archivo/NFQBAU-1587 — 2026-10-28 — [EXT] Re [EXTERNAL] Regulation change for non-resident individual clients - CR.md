---
id: NFQBAU-1587
fecha_apertura: 2026-10-28
fecha_limite: 2026-10-31
fecha_resolucion: 2026-11-04
estado: Resuelto
prioridad: Baja
responsable: Deborah Bertoldo
origen: email
referencia_origen: "[EXT] Re: [EXTERNAL] Regulation change for non-resident individual clients - CR SC-9947 (2026-10-28)"
categoria:
  - APIs
entorno:
  - Producción
sintoma: Consulta sobre la promoción al entorno de producción de la interfaz ContractualClient.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-04 15:46
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

Deborah B., desarrolladora de NFQ, pregunta si existe otra cadena de correos donde se haya promovido a producción el desarrollo de la interfaz ContractualClient.
Indica que el desarrollo llegó a UAT, pero la extracción con los nuevos campos ya está en producción, por lo que desea proceder con la adición de dichos campos.
Adjunta capturas.

Detalles: Interfaz: ContractualClient; Petición: verificar si se promovió a PRD o seguir el procedimiento para agregar nuevos campos; Estado actual: la extracción con los nuevos campos ya se encuentra en PRD
Adjuntos del correo: image007.png, image002.png, image011.png, image003.png, image001.png, image008.png, image010.gif, image013.png, image006.png, image015.png, image004.png, image014.png, image005.png, image012.png, image009.png

## Histórico de interacciones

- 2026-10-28 14:16 — Correo automático — Deborah B., desarrolladora de NFQ, pregunta si existe otra cadena de correos donde se haya promovido a producción el desarrollo de la interfaz ContractualClient.
Indica que el desarrollo llegó a UAT, pero la extracción con los nuevos campos ya está en producción, por lo que desea proceder con la adición de dichos campos.
Adjunta capturas.

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
- 2026-10-28 14:16 — (vacío) → Abierto — Correo automático
- 2026-11-04 15:46 — Abierto → Resuelto — Matheus Fransoni

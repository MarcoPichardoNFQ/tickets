---
id: NFQBAU-1689
fecha_apertura: 2026-11-11
fecha_limite: 2026-11-14
fecha_resolucion:            # obligatoria al pasar a Resuelto
estado: Abierto              # ver 05_GENERAL/listas.json
prioridad: Baja
responsable:                 # Nombre Apellido, igual que el fichero en 04_PERSONAS
origen: email
referencia_origen: "Interface XML de carga Aldrin (2026-11-11)"
categoria: [BBDD]
entorno: []                  # Producción | UAT
sintoma: "Consulta técnica sobre el nombre del fichero XML que alimenta la tabla sss_asset_t."
solucion_corta:              # una línea: qué lo arregló
codigo_relacionado:
  - repo:
    modulo:
    version:                 # tag de PRD cuando se despliegue
tickets_proveedor: []        # notas de 03_PROVEEDORES
decision_relacionada:
referencias_tecnicas: []     # fichas de 00_REFERENCIA_TECNICA que ayudaron
actualizado: 2026-11-11 16:16
actualizado_por: Correo automático
tags: [ticket, bau]
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Thiago A. envía una consulta técnica relativa al proceso de carga Aldrin. Solicita saber el nombre del archivo XML utilizado en el mapeo para poblar una tabla de la base de datos. Adjunta capturas.

Detalles: Tabla afectada: sss_asset_t; Interfaz/Proceso: Interface XML de carga Aldrin
Adjuntos del correo: image001.png

## Histórico de interacciones

- 2026-11-11 15:51 — Correo automático — Thiago A. envía una consulta técnica relativa al proceso de carga Aldrin. Solicita saber el nombre del archivo XML utilizado en el mapeo para poblar una tabla de la base de datos. Adjunta capturas.
- 2026-11-11 16:16 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador de NFQ, responde a una consulta de Thiago A. sobre los archivos de carga. Proporciona el listado de ficheros XML que alimentan la tabla en la interfaz Aldrin. Adjunta un fichero. Detalles: Tabla: sss_asset_t; Interfaz: Aldrin; Lista de XMLs: Equity.xml; Bond.xml; Right.xml; Unit.xml; Option.xml; STI.xml; Future.xml; Fund.xml; Forward.xml; Commodity.xml · Adjuntos del correo: image001.png

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
- 2026-11-11 15:51 — nuevo → Abierto — Correo automático

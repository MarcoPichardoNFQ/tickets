---
id: NFQBAU-1612
fecha_apertura: 2026-10-31
fecha_limite: 2026-10-31
fecha_resolucion: 2026-11-03
estado: Resuelto
prioridad: Alta
responsable: Matheus Fransoni
origen: email
referencia_origen: "[JIRA] [JIRA] (SC-9009) Create field in FIDIC operation - RISK (2026-10-31)"
categoria:
  - BBDD
entorno:
  - Producción
sintoma: Se solicita la ejecución de código SQL y la actualización de un archivo XSD para añadir nuevos campos a la base de datos del sistema ALDRIN.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-03 09:59
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

Deborah Y. de NFQ solicita la aprobación para ejecutar código SQL en la base de datos de Producción y actualizar un archivo XSD. El objetivo es ajustar parámetros e incluir nuevos campos de una interfaz de Megara en el sistema ALDRIN. El correo adjunta capturas y tres ficheros.

Detalles: Host: psqlprddatahub03.postgres.database.cloud.corp; Sistema: ALDRIN; Motivo: Ajuste de parámetros para inclusión de nuevos campos de la interfaz enviada por Megara; Impacto en Cliente: Sí; Impacto en otros sistemas: Sí, ALDRIN es repositorio central de datos; Tiempo de rollback: 30 minutos; Responsables de prueba funcional/técnica: Marcos (S3), Marco/Deborah (NFQ); Plan de rollback: Ejecución de código que compila la versión anterior (adjunto); No habrá indisponibilidad; Pasos para ejecución: 1.- Actualizar el archivo ClientInstruction.xsd en la carpeta /nfq/XMLconversor/xsd/ para el ambiente PRD; 2.- Ejecutar los códigos SQL adjuntos en el host psqlprddatahub03.postgres.database.cloud.cor; Se solicita un esfuerzo coordinado en P0, pausar la carga antes del cambio, incluir archivos en Rundeck y ejecutar scripts en la base de datos; Adjunta ClientInstruction.xsd, scriptClientInstruction.sql, ROLLBACK ClientInstruction.sql; Las capturas de pantalla muestran una consulta SQL 'select * from STG_S3.MEG_INSTRUCTIONS_T;' y los resultados de la tabla meg_instructions_t con columnas como dat_conver, dat_lbmat, des_withrisk, cod_load_trace, cod_ent_geo, cod_seq_instructions, cod_client, des_clides, des_secacc, cod_traref.
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png, image011.png, image012.png, image013.png, image014.png, image020.png, image015.gif, image018.png, image021.jpg, image017.png, image019.jpg, image016.png, ClientInstruction.xsd, scriptClientInstruction.sql, ROLLBACK ClientInstruction.sql

## Histórico de interacciones

- 2026-10-31 12:37 — Correo automático — Deborah Y. de NFQ solicita la aprobación para ejecutar código SQL en la base de datos de Producción y actualizar un archivo XSD. El objetivo es ajustar parámetros e incluir nuevos campos de una interfaz de Megara en el sistema ALDRIN. El correo adjunta capturas y tres ficheros.

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
- 2026-10-31 12:37 — nuevo → Abierto — Correo automático
- 2026-11-03 09:59 — Abierto → Resuelto — Matheus Fransoni

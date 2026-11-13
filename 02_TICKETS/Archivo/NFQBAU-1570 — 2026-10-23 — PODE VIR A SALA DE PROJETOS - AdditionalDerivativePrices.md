---
id: NFQBAU-1570
fecha_apertura: 2026-10-23
fecha_limite: 2026-10-24
fecha_resolucion: 2026-10-26
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: PODE VIR A SALA DE PROJETOS - AdditionalDerivativePrices (2026-10-23)
categoria: [Rundeck, Sala]
entorno: []
sintoma: Fallo en la carga del XML de precios de SWAP correspondiente a AdditionalDerivativePrices.
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
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Ado G., del área de tecnología, reporta que la carga del XML de precios de SWAP no está funcionando. Solicita apoyo para revisar el problema y adjunta capturas y un fichero de ejemplo.

Detalles: Proceso o entidad afectada: AdditionalDerivativePrices; Tipo de archivo: XML de precios de SWAP; Archivo de ejemplo adjunto: AdditionalDerivativePrice_1792775397728.zip
Adjuntos del correo: image.png, image.png, image.png, AdditionalDerivativePrice_1792775397728.zip

## Histórico de interacciones

- 2026-10-23 20:33 — Correo automático — Ado G., del área de tecnología, reporta que la carga del XML de precios de SWAP no está funcionando. Solicita apoyo para revisar el problema y adjunta capturas y un fichero de ejemplo.
- 2026-10-23 20:37 — Correo automático — Correo nuevo en el hilo: Marco P., consultor sénior de Nfq, responde indicando que acudirá a la sala de proyectos. Se trata de un mensaje breve de confirmación que no plantea ninguna solicitud ni incidencia nueva. Adjuntos del correo: image.png, image.png, image.png

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
- 2026-10-23 20:33 — nuevo → Abierto — Correo automático
- 2026-10-26 17:26 — Abierto → Resuelto — Marco Pichardo

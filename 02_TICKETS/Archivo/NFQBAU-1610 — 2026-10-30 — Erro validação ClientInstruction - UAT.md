---
id: NFQBAU-1610
fecha_apertura: 2026-10-30
fecha_limite: 2026-10-31
fecha_resolucion: 2026-11-05
estado: Resuelto
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: Erro validação ClientInstruction - UAT (2026-10-30)
categoria:
  - Rundeck
entorno:
  - UAT
sintoma: Fallo en la validación y carga de ClientInstruction debido a la calidad de los datos en los campos SecurityCode y MaturityAmount.
solucion_corta: "Remisión de versión corregida de los XML descartando los registros conflictivos."
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-06 22:43
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

Deborah B., desarrolladora de NFQ, comunica que los errores en la carga se deben a problemas de calidad de datos en SecurityCode y MaturityAmount.
Remite una versión corregida de los XML descartando los registros conflictivos; adjunta un fichero.

Detalles: Carga: ClientInstruction; Registros afectados: SCI000810365, SCI000810366, SCI000810367 con SecurityCode='US105756AP53_17082040' (21 caracteres); Campo MaturityAmount inadecuado; Fichero adjunto: xml_divididos_10_partes.zip
Adjuntos del correo: xml_divididos_10_partes.zip

## Histórico de interacciones

- 2026-10-30 21:39 — Correo automático — Deborah B., desarrolladora de NFQ, comunica que los errores en la carga se deben a problemas de calidad de datos en SecurityCode y MaturityAmount.
Remite una versión corregida de los XML descartando los registros conflictivos; adjunta un fichero.
- 2026-11-06 21:06 — Correo automático — Resolución redactada automáticamente a partir del histórico; revisar.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Se identificó que los errores en la carga se debían a problemas de calidad de datos en SecurityCode y MaturityAmount. Deborah B. remitió una versión corregida de los XML descartando los registros conflictivos mediante el fichero adjunto.

### Cómo se comprobó

No consta en el histórico.

### Con quién se habló

Deborah B., desarrolladora de NFQ

### Servicios, jobs o tablas tocados

ClientInstruction, SecurityCode, MaturityAmount, xml_divididos_10_partes.zip

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-10-30 21:39 — nuevo → Abierto — Correo automático
- 2026-11-05 17:43 — Abierto → Resuelto — Marco Pichardo
- 2026-11-06 12:14 — Abierto → Resuelto — Matheus Fransoni

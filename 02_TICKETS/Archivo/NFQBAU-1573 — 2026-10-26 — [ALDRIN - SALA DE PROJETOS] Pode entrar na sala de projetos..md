---
id: NFQBAU-1573
fecha_apertura: 2026-10-26
fecha_limite: 2026-10-26
fecha_resolucion: 2026-10-28
estado: Resuelto
prioridad: Alta
responsable: Matheus Fransoni
origen: email
referencia_origen: "[ALDRIN - SALA DE PROJETOS] Pode entrar na sala de projetos. (2026-10-26)"
categoria: [BBDD, Sala]
entorno:
  - Producción
sintoma: Problemas al probar 'cashtransferorder' y 'OPTION' en UAT, con 'InvestCompanyInstitute' y 'Unit' atascados en una carpeta; además, una función de finalización en Producción no actualizó una tabla de control el fin de semana.
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
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Ado G., Tecnología, informa de varios problemas. En UAT, está probando 'cashtransferorder' y 'OPTION', y menciona que 'InvestCompanyInstitute' y 'Unit' están atascados. En Producción, una función de finalización no actualizó una tabla de control durante el fin de semana. Adjunta capturas.

Detalles: UAT: problemas al probar cashtransferorder; posibilidad de probar OPTION; InvestCompanyInstitute y Unit atascados en la carpeta; PRD: función de finalización de producción no actualizó la tabla de control durante el fin de semana.
Adjuntos del correo: image.png, image.png, image.png

## Histórico de interacciones

- 2026-10-26 15:56 — Correo automático — Ado G., Tecnología, informa de varios problemas. En UAT, está probando 'cashtransferorder' y 'OPTION', y menciona que 'InvestCompanyInstitute' y 'Unit' están atascados. En Producción, una función de finalización no actualizó una tabla de control durante el fin de semana. Adjunta capturas.

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
- 2026-10-26 15:56 — (vacío) → Abierto — Correo automático
- 2026-10-27 10:29 — Abierto → Revisión cliente — Matheus Fransoni
- 2026-10-28 16:12 — Revisión cliente → Resuelto — Matheus Fransoni

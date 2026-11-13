---
id: NFQBAU-1533
fecha_apertura: 2026-10-19
fecha_limite: 2026-10-20
fecha_resolucion: 2026-11-04
estado: Resuelto
prioridad: Media
responsable: Deborah Bertoldo
origen: email
referencia_origen: '[MEGARA X ALDRIN] Arquivos "sobrando a cada carga" no UAT (2026-10-19)'
categoria:
  - Rundeck
entorno:
  - UAT
sintoma: Archivos XML quedan pendientes o "sobrando" después de cada carga en el entorno UAT.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-04 15:34
actualizado_por: Matheus Fransoni
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Ado G., de Tecnología de PR Serviços, solicita verificar el entorno UAT porque recurrentemente quedan archivos XML pendientes después de las cargas. Menciona que algunos archivos como "FLAG do OPTION" e "InvestCompanyInstitute.XML" tienen errores conocidos, pero otros como "Unit" y "performance" no deberían quedar pendientes. Deborah Y., Developer de NFQ, añade al equipo de soporte para la generación de un ticket y confirma que están evaluando el caso. Adjunta capturas.

Detalles: Los archivos XML que quedan pendientes incluyen `InvestCompanyInstitute.XML`, `performance.xml` y `Unit.xml`. La captura de pantalla muestra un explorador de archivos en la ruta `premegara > Devices > MegaCommon > innotech` con archivos `.xml` como `InvestCompanyInstitute_1792400760034.xml`, `MEGACUSTODY_EndOfWeek_1792400741633.xml`, `performance_1792400748864.xml` y `Unit_1792400749876.xml`, todos con fecha de modificación `2026-10-19 11:05 AM` o `11:06 AM`. Se menciona que el archivo FLAG del OPTION y InvestCompanyInstitute.XML tienen un error a tratar con S3.
Adjuntos del correo: image.png, image.png, image.png, image.png

## Histórico de interacciones

- 2026-10-19 11:22 — Correo automático — Ado G., de Tecnología de PR Serviços, solicita verificar el entorno UAT porque recurrentemente quedan archivos XML pendientes después de las cargas. Menciona que algunos archivos como "FLAG do OPTION" e "InvestCompanyInstitute.XML" tienen errores conocidos, pero otros como "Unit" y "performance" no deberían quedar pendientes. Deborah Y., Developer de NFQ, añade al equipo de soporte para la generación de un ticket y confirma que están evaluando el caso. Adjunta capturas.

Nota: mismo hilo que el NFQBAU-1532 (cuatro minutos antes); nació aparte por el fallo del emparejado con asuntos con comillas. El 1532 queda cerrado tal cual; este es el que sigue.

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
- 2026-10-19 11:22 — (vacío) → Abierto — Correo automático
- 2026-10-20 16:17 — Abierto → En curso — Marco Pichardo
- Aun no sabemos què es lo que esta pasando
- 2026-11-04 15:34 — En curso → Resuelto — Matheus Fransoni

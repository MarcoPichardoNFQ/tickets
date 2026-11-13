---
id: NFQBAU-1532
fecha_apertura: 2026-10-19
fecha_limite: 2026-10-20
fecha_resolucion: 2026-10-21
estado: Resuelto
prioridad: Media
responsable: Deborah Bertoldo
origen: email
referencia_origen: '[MEGARA X ALDRIN] Arquivos "sobrando a cada carga" no UAT (2026-10-19)'
categoria:
  - Rundeck
entorno:
  - UAT
sintoma: Archivos XML quedan acumulados sin procesar en la ruta de carga tras cada ejecución.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-21 01:38
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

Ado S., del área de tecnología, solicita revisar el entorno de UAT porque se están acumulando archivos XML tras las cargas recurrentes. Señala que los ficheros de Unit y performance no tienen observaciones y no deberían quedar pendientes. Adjunta capturas.

Detalles: Ruta afectada: premegara > Devices > MegaCommon > innotech; Archivos pendientes en captura: InvestCompanyInstitute_1792400760034.xml, MEGACUSTODY_EndOfWeek_1792400741633.xml, performance_1792400748864.xml, Unit_1792400749876.xml; Carpetas en directorio: alertas, Flags, Manual; Se menciona error conocido a tratar con S3 para InvestCompanyInstitute.XML y archivo FLAG de OPTION
Adjuntos del correo: image.png, image.png, image.png, image.png

## Histórico de interacciones

- 2026-10-19 11:18 — Correo automático — Ado S., del área de tecnología, solicita revisar el entorno de UAT porque se están acumulando archivos XML tras las cargas recurrentes. Señala que los ficheros de Unit y performance no tienen observaciones y no deberían quedar pendientes. Adjunta capturas.

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
- 2026-10-19 11:18 — (vacío) → Abierto — Correo automático
- Aun no sabemos què es, sobra Unit y Perfonamcenavdetails
- 
- 2026-10-21 01:29 — Abierto → En curso — Marco Pichardo
- 2026-10-21 01:38 — En curso → Resuelto — Marco Pichardo

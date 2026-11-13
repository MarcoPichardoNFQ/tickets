---
id: NFQBAU-1528
fecha_apertura: 2026-10-16
fecha_limite: 2026-10-17
fecha_resolucion: 2026-10-21
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: Entrar na sala de PROJETOS (2026-10-16)
categoria: [Sala]
entorno: []
sintoma: Petición de apertura de ticket de soporte para el seguimiento de una incidencia pendiente de detallar.
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
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Correo automático'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marco P., consultor senior de NFQ, solicita al equipo de soporte que abra un ticket para dar seguimiento a una incidencia.
Indica que complementará los detalles de la misma de manera manual.

Adjuntos del correo: image001.png, image002.png, image003.png

## Histórico de interacciones

- 2026-10-16 20:02 — Correo automático — Marco P., consultor senior de NFQ, solicita al equipo de soporte que abra un ticket para dar seguimiento a una incidencia.
Indica que complementará los detalles de la misma de manera manual.
- 2026-10-16 20:31 — Correo automático — Correo nuevo en el hilo: Marco P., consultor sénior de NFQ, solicita formalizar y priorizar la resolución de una incidencia en la interfaz NavBankBalance a petición de Fernando. Reporta que los archivos XML no se consumen al colocarse en la carpeta de cargas automáticas, aunque se procesan con normalidad en la carpeta manual. Detalles: Interfaz NavBankBalance; El archivo XML no se consume al insertarse en la carpeta de cargas automáticas; El archivo se procesa normalmente si se coloca en la carpeta de cargas manuales · Adjuntos del correo: image001.png, image003.png, image002.png

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
- 2026-10-16 20:02 — nuevo → Abierto — Correo automático
- 2026-10-17 11:51 — Abierto → En curso — Ricardo Reyes
- 2026-10-21 01:38 — En curso → Resuelto — Marco Pichardo

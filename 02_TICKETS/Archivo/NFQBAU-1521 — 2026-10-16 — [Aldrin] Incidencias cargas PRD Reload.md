---
id: NFQBAU-1521
fecha_apertura: 2026-10-16
fecha_limite: 2026-10-17
fecha_resolucion: 2026-10-16
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: "Re: Re: Re: Re: Re: Re: Re: Re: Re: Re: [Aldrin] Incidencias cargas PRD Reload (2026-10-16)"
categoria: []
entorno: []
sintoma: Una carga de datos falló debido a un error en el archivo de flag.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-10-17 16:13
actualizado_por: Ricardo Reyes
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Correo automático'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Ismael B., Developer I, solicita una recarga a partir de las 07:15 (horario de Brasil) porque una carga anterior falló por un error en el archivo de flag.

## Histórico de interacciones

- 2026-10-16 08:02 — Correo automático — Ismael B., Developer I, solicita una recarga a partir de las 07:15 (horario de Brasil) porque una carga anterior falló por un error en el archivo de flag.
- 2026-10-16 08:37 — Correo automático — Correo nuevo en el hilo: Renato C., de PR Servicios, comunica que está realizando en ese momento la recarga solicitada previamente por el equipo de soporte (correo descartado por Gemini el 16/10 antes del ajuste; añadido a mano).
- 2026-10-16 08:57 — Correo automático — Correo nuevo en el hilo: Renato C. de Lima, de PR Serviços, informa que la recarga solicitada ha sido finalizada con éxito. Agradece el apoyo.

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
- 2026-10-16 08:02 — (vacío) → Abierto — Correo automático
- 2026-10-16 09:30 — Abierto → Resuelto — Ricardo Reyes

---
id: NFQBAU-1561
fecha_apertura: 2026-10-22
fecha_limite: 2026-10-23
fecha_resolucion: 2026-10-26
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: "[SALA DE PROJETOS] Podem vir a sala de projetos (2026-10-22)"
categoria: [BBDD, Sala]
entorno: []
sintoma: Convocatoria o consulta para revisar la función function_meg_sac_stat_cl_mc_txadm_t.
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

Ado G., del área de Tecnología, solicita al equipo acudir a la sala de proyectos. El asunto indicado para tratar es la función function_meg_sac_stat_cl_mc_txadm_t. Adjunta capturas.

Detalles: Función: function_meg_sac_stat_cl_mc_txadm_t
Adjuntos del correo: image.png, image.png, image.png

## Histórico de interacciones

- 2026-10-22 17:53 — Correo automático — Ado G., del área de Tecnología, solicita al equipo acudir a la sala de proyectos. El asunto indicado para tratar es la función function_meg_sac_stat_cl_mc_txadm_t. Adjunta capturas.

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
- 2026-10-22 17:53 — (vacío) → Abierto — Correo automático
- 2026-10-26 17:25 — Abierto → Resuelto — Marco Pichardo

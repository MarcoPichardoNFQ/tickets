---
id: NFQBAU-1670
fecha_apertura: 2026-11-09
fecha_limite: 2026-11-10
fecha_resolucion:            # obligatoria al pasar a Resuelto
estado: Abierto              # ver 05_GENERAL/listas.json
prioridad: Media
responsable:                 # Nombre Apellido, igual que el fichero en 04_PERSONAS
origen: email
referencia_origen: "Datahub APIs issue (2026-11-09)"
categoria: [Otros]
entorno: []                  # Producción | UAT
sintoma: "La opción de Bloqueo no aparece disponible en el sistema Megara para el mercado de Renta Fija."
solucion_corta:              # una línea: qué lo arregló
codigo_relacionado:
  - repo:
    modulo:
    version:                 # tag de PRD cuando se despliegue
tickets_proveedor: []        # notas de 03_PROVEEDORES
decision_relacionada:
referencias_tecnicas: []     # fichas de 00_REFERENCIA_TECNICA que ayudaron
actualizado: 2026-11-09 13:11
actualizado_por: Correo automático
tags: [ticket, bau]
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Daiana A., cliente, solicita asistencia técnica para que el equipo de Renta Fija pueda operar en Megara. Indica que Alessandro M., del equipo de RF, no encuentra la opción de Bloqueo en dicha pantalla. Adjunta capturas y un fichero.

Detalles: Sistema Megara; mercado RF (Renta Fija); opción faltante: Bloqueio; capturas muestran consultas a las tablas sac_stat_ba_tipo_bloq_t (campo cod_tipo_bloqueio) y trf_s3.sac_ba_bloqueio_t
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png, image011.png, image012.png, image013.png, image014.png, image015.png, image016.jpg, image017.gif, image018.png, image019.png, image020.png, image021.png, image022.png, image023.jpg, Cópia de Motivos_Bloqueio1.xlsx

## Histórico de interacciones

- 2026-11-09 13:11 — Correo automático — Daiana A., cliente, solicita asistencia técnica para que el equipo de Renta Fija pueda operar en Megara. Indica que Alessandro M., del equipo de RF, no encuentra la opción de Bloqueo en dicha pantalla. Adjunta capturas y un fichero.

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
- 2026-11-09 13:11 — nuevo → Abierto — Correo automático

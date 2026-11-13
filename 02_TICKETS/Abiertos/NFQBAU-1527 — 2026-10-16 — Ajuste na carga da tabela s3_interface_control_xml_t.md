---
id: NFQBAU-1527
fecha_apertura: 2026-10-16
fecha_limite: 2026-10-19
fecha_resolucion: 2026-11-06
estado: Resuelto
prioridad: Baja
responsable: Marco Pichardo
origen: email
referencia_origen: Ajuste na carga da tabela "s3_interface_control_xml_t" (2026-10-16)
categoria:
  - BBDD
entorno: []
sintoma: Se solicita modificar el procedimiento de carga de la tabla trf_s3.s3_interface_control_xml_t para que las inserciones y actualizaciones no dependan de la condición de conteo.
solucion_corta:
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
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Correo automático'),option('Marco Pichardo'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marcos M., de Tecnología, solicita ajustar el procedimiento de carga de la tabla s3_interface_control_xml_t según lo acordado previamente. Pide mover las operaciones de inserción y actualización fuera del bloque condicional IF para que se ejecuten siempre. Adjunta capturas.

Detalles: Tablas involucradas: trf_s3.s3_interface_control_xml_t, trf_s3.s3_interface_control_t, stg_s3.meg_supervision_ex_t, trf_s3.sss_est_com_mgc_t, exp_s3.tablas_relacion, exp_s3.control_carga_sac_megara_t; Se solicita extraer los INSERT y UPDATE del bloque condicional 'IF v_count = 137 THEN'; La condición 'IF v_count = 137' pasa a controlar únicamente los avisos 'Procedimiento de control ejecutado correctamente.' y 'Procedimiento de control incompleto.'
Adjuntos del correo: image001.png, image002.png, image003.png




## Histórico de interacciones

- 2026-10-16 18:46 — Correo automático — Marcos M., de Tecnología, solicita ajustar el procedimiento de carga de la tabla s3_interface_control_xml_t según lo acordado previamente. Pide mover las operaciones de inserción y actualización fuera del bloque condicional IF para que se ejecuten siempre. Adjunta capturas.
- Pendiente validar con Kleverson esta solicitud de Menses, pues lo que queire es que sin importar la cantidad de interfaces recibidas o exitosas o fallidas; siempre se informe la tabla de s3_interface_control_xml_t cuando esto justamente va en contra de la premisa que si algo falla; no se cara informacion
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
- 2026-10-16 18:46 — nuevo → Abierto — Correo automático
- 2026-10-17 11:51 — Abierto → En curso — Ricardo Reyes
- Menses solicita que sin improtar la cantidad de interfaces que ueron recibidas, se cargue informacion a s3_interface_control_xml_t, lo cual va en contra de lo solicitado por menses
- 2026-10-26 17:32 — En curso → Abierto — Marco Pichardo
- 2026-11-06 12:27 — Abierto → Resuelto — Matheus Fransoni

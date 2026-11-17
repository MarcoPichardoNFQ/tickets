---
id: NFQBAU-1682
fecha_apertura: 2026-11-10
fecha_limite: 2026-11-11
fecha_resolucion: 2026-11-10
estado: Resuelto
prioridad: Media
responsable:
origen: email
referencia_origen: "[ALDRIN] Ajuste no mapeamento para a tabela SAC_SW2_POS (cart_pos_sw_t) (2026-11-10)"
categoria:
  - BBDD
entorno:
  - Producción
sintoma: Se requiere un ajuste en el mapeo para la tabla SAC_SW2_POS (cart_pos_sw_t) y en la función function_meg_sac_stat_sw_cad_t().
solucion_corta: "Se ejecutaron los ajustes de mapeo para la tabla SAC_SW2_POS (cart_pos_sw_t) y la función function_meg_sac_stat_sw_cad_t()."
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-11 09:09
actualizado_por: Correo automático
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros'),option('Sala')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Continúa el hilo del [NFQBAU-1658](../Abiertos/NFQBAU-1658%20—%202026-11-06%20—%20[ALDRIN]%20Ajuste%20no%20mapeamento%20para%20a%20tabela%20SAC_SW2_POS%20(cart_pos_sw_t).md), cerrado el 2026-11-10: no se reabre, se crea este. Guilherme S. pregunta a Marcos M. si la ejecución del ajuste de mapeo para la tabla SAC_SW2_POS (cart_pos_sw_t) ya fue realizada. Marcos M. había confirmado previamente que las pruebas en UAT para el ajuste de mapeo fueron exitosas y solicitó la aprobación y actualización en Producción. También pidió a Guilherme S. que ejecutara otra solicitud relacionada con la función function_meg_sac_stat_sw_cad_t(). Adjunta capturas.

Detalles: Tabla: SAC_SW2_POS (cart_pos_sw_t); Función: function_meg_sac_stat_sw_cad_t(); Tareas Jira: S3C-23171, S3C-23173; Host: psqlcerdatahub01.postgres.database.cloud.corp; Descripción del cambio: Ajuste en el mapeo para la tabla SAC_SW2_POS (cart_pos_sw_t); Servicios afectados: Database; Plan de rollback: Ejecución del archivo ROLLBACK adjunto; Impacto: Inserción de información en Aldrin; La captura de pantalla en el correo de Marcos M. muestra "Teste realizado com sucesso em UAT".
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png

## Histórico de interacciones

- 2026-11-10 16:26 — Correo automático — Continúa el hilo del [NFQBAU-1658](../Abiertos/NFQBAU-1658%20—%202026-11-06%20—%20[ALDRIN]%20Ajuste%20no%20mapeamento%20para%20a%20tabela%20SAC_SW2_POS%20(cart_pos_sw_t).md), cerrado el 2026-11-10: no se reabre, se crea este. Guilherme S. pregunta a Marcos M. si la ejecución del ajuste de mapeo para la tabla SAC_SW2_POS (cart_pos_sw_t) ya fue realizada. Marcos M. había confirmado previamente que las pruebas en UAT para el ajuste de mapeo fueron exitosas y solicitó la aprobación y actualización en Producción. También pidió a Guilherme S. que ejecutara otra solicitud relacionada con la función function_meg_sac_stat_sw_cad_t(). Adjunta capturas.
- 2026-11-10 16:46 — Correo automático — Correo nuevo en el hilo: Guilherme S., de NTT DATA, confirma la ejecución de la tarea S3C-23180, que corresponde a un ajuste en el mapeo de la tabla SAC_SW2_POS y la función 'cart_pos_sw_t' en el sistema ALDRIN. Este ajuste fue solicitado por Marcos M., de PR Serviços, y previamente se había confirmado su éxito en UAT. Adjunta capturas. Detalles: Ajuste en la tabla SAC_SW2_POS (cart_pos_sw_t) y en la función 'cart_pos_sw_t'; Sistema ALDRIN; HOST: psqlprddatahub03.postgres.database.cloud.corp; Ticket ID: NFQBAU1658; Tarea ejecutada: S3C-23180; El ajuste es de tipo 'Lógica'; Impacto en cliente: Sí; Impacto en otros sistemas: Sí, ALDRIN es repositorio central de datos; Tiempo de rollback: 30 minutos; Responsables de prueba funcional y técnica: Marcos S. y Marco N.; Adjunta 7 capturas de pantalla, una de ellas muestra evidencia en UAT. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png
- 2026-11-10 16:52 — Correo automático — Correo nuevo en el hilo: Guilherme S., soporte de NTT Data, confirma la ejecución de lo solicitado mediante el ticket S3C-23174 tras un intercambio sobre tareas previas. Detalles: Ticket mencionado: S3C-23174; Tabla afectada: SAC_SW2_POS (cart_pos_sw_t); adjunta capturas · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png
- 2026-11-11 09:08 — Correo automático — Resolución redactada automáticamente a partir del histórico; revisar.

## Paquete de despliegue

- Update: 
- Rollback: (obligatorio si hubo código)
- Informe: 
- Anexos: 

## Resolución

### Qué se hizo

Guilherme S. preguntó a Marcos M. sobre el estado de la ejecución. Posteriormente, Guilherme S. confirmó la ejecución de la tarea S3C-23180 correspondiente al ajuste en el mapeo de la tabla SAC_SW2_POS y la función 'cart_pos_sw_t'. Finalmente, Guilherme S. confirmó la ejecución de lo solicitado mediante el ticket S3C-23174.

### Cómo se comprobó

Marcos M. confirmó previamente que las pruebas en UAT para el ajuste de mapeo fueron exitosas.

### Con quién se habló

Guilherme S., soporte de NTT Data; Marcos M., de PR Serviços; Marcos S., responsable de prueba funcional y técnica; Marco N., responsable de prueba funcional y técnica

### Servicios, jobs o tablas tocados

SAC_SW2_POS, cart_pos_sw_t, function_meg_sac_stat_sw_cad_t()

### Referencias técnicas usadas y por qué

## Vencimiento

## Historial de estados
- 2026-11-10 16:26 — nuevo → Abierto — Correo automático
- 2026-11-10 17:54 — Abierto → Resuelto — Matheus Fransoni

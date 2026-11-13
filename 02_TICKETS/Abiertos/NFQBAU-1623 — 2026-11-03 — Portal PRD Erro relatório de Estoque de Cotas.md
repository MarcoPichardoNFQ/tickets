---
id: NFQBAU-1623
fecha_apertura: 2026-11-03
fecha_limite: 2026-11-04
fecha_resolucion:
estado: Pruebas cliente UAT
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: "Portal PRD: Erro relatório de Estoque de Cotas (2026-11-03)"
categoria:
  - Qlik
entorno: [Producción, UAT]
  - Producción
sintoma: Error al generar el informe de Estoc de Cotas en el portal, mostrando un mensaje de fallo en pantalla.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-06 12:14
actualizado_por: Matheus Fransoni
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marco J., consultor sénior, responde indicando que el análisis del problema está en curso. El origen del hilo es una petición de Guilherme V., de tecnología, que reportaba un error al generar el informe para el fondo 4384 con fecha 29/10 en el entorno de producción.

Detalles: Fondo: 4384 (sem cust); Fecha de los datos: 29/10; Mensaje de error en captura: Falha ao gerar relatório. Tente novamente mais tarde. FundCotaHolding [GFFQ]; URL: s3caceis.com.br/portal/active-report/reports/reports; adjunta capturas
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png

## Histórico de interacciones

- 2026-11-03 21:01 — Correo automático — Marco J., consultor sénior, responde indicando que el análisis del problema está en curso. El origen del hilo es una petición de Guilherme V., de tecnología, que reportaba un error al generar el informe para el fondo 4384 con fecha 29/10 en el entorno de producción.
- 2026-11-03 21:13 — Correo automático — Correo nuevo en el hilo: Marco P., consultor de NFQ, solicita validar nuevamente si el problema ha sido resuelto. Anteriormente, Guilherme V., del departamento de tecnología de S3 Caceis, reportó un fallo al generar un informe en producción. Adjunta capturas. Detalles: Informe: Estoque de Cotas; Fondo afectado: 4384; Fecha de consulta: 29/10; Error literal: "Falha ao gerar relatório. Tente novamente mais tarde. FundCotaHolding [GFFQ]"; La captura muestra el portal de informes de S3 Caceis arrojando un aviso de error en rojo al intentar consultar el informe para el fondo 4384. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png
- 2026-11-04 10:51 — Correo automático — Correo nuevo en el hilo: Guilherme V., del área de Tecnología, confirma que el informe de Estoque de Cotas ya se puede generar correctamente. Sin embargo, solicita la causa raíz y la solución aplicada para evitar la recurrencia del fallo. Adjunta capturas y un fichero. Detalles: Pantalla: /portal/active-report/reports/reports; Informe: Estoque de Cotas de Fundos (Tipo de relatório: Posição); Fondo afectado: 4384; Fecha de datos: 29/10/2026; Mensaje de error: 'Falha ao gerar relatório. Tente novamente mais tarde. FundCotaHolding [GFFQ]'; Archivo adjunto/generado: Estoque de Cotas de Fundos (4).xlsx · Adjuntos del correo: ~WRD0000.jpg, image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, Estoque de Cotas de Fundos (4).xlsx

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
- 2026-11-03 21:01 — nuevo → Abierto — Correo automático
- 2026-11-05 12:24 — Abierto → Pruebas cliente UAT — Marco Pichardo
- 2026-11-06 12:14 — Abierto → Pruebas cliente UAT — Matheus Fransoni

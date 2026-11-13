---
id: NFQBAU-1622
fecha_apertura: 2026-11-03
fecha_limite: 2026-11-04
fecha_resolucion:
estado: Revisión cliente
prioridad: Media
responsable: Matheus Fransoni
origen: email
referencia_origen: "[Aldrin] - InvestCompany (2026-11-03)"
categoria:
  - Otros
entorno:
  - UAT
sintoma: No se visualizan las informaciónes cargadas en el entorno UAT para InvestCompany debido a un error en un archivo anterior.
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

Marco P., consultor sénior, informa a Ado que la falta de visualización en InvestCompany se debe a un error previo en un archivo por el XML y pide volver a subir el archivo afectado.

Detalles: Entorno: UAT; Aplicativo/Proyecto: InvestCompany; Causa: error de carga en archivo anterior debido a la composición del XML; Acción requerida: realizar nuevamente el upload del archivo en cuestión.

## Histórico de interacciones

- 2026-11-03 20:56 — Correo automático — Marco P., consultor sénior, informa a Ado que la falta de visualización en InvestCompany se debe a un error previo en un archivo por el XML y pide volver a subir el archivo afectado.
- 2026-11-04 11:24 — Correo automático — Correo nuevo en el hilo: Ado S., tecnología, confirma que extraerá un nuevo fichero y lo pondrá a cargar para solucionar la falta de datos. Indica que avisará al equipo si surge algún problema durante el proceso. Adjunta capturas. Detalles: Sistema: Aldrin - InvestCompany; Causa del problema previo: error en la composición del XML de un archivo anterior que bloqueó la visualización de la carga; Acción actual: reextracción y recarga manual del fichero en UAT · Adjuntos del correo: image.png, image.png, image.png
- 2026-11-04 11:31 — Correo automático — Correo nuevo en el hilo: Marcos M., Tecnología de PRServiços, informa que recargar los datos no resolverá el problema porque Ado G., Tecnología de PRServiços, verificó ayer que el nuevo campo necesario no ha sido creado en la tabla sss_inv_company_inst_t. Adjunta capturas. Detalles: La tabla afectada es "sss_inv_company_inst_t"; Falta un campo nuevo en la tabla; El problema se relaciona con la visualización de información en "InvestCompany"; Un archivo anterior presentó un error de carga debido a la composición del XML. · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-04 12:37 — Correo automático — Correo nuevo en el hilo: Ado S., Tecnología, solicita a Deborah B. y Matheus D. que verifiquen si los campos de una extracción están en las tablas STG y SSS y si están mapeados correctamente, ya que un campo nuevo no se ha creado en la tabla sss_inv_company_inst_t y lo necesita para el mapeo de Aldrin. Marcos M., Tecnología, confirma que el campo no se ha creado. El problema original, reportado por Marco P., Senior Consultant, era que Ado S. no visualizaba información cargada en UAT debido a un error de carga de un archivo XML anterior. Adjunta capturas. Detalles: Campos de extracción; Tablas STG y SSS; Tabla sss_inv_company_inst_t; Campo nuevo no creado; Mapeo de Aldrin; Entorno UAT (InvestCompany); Error de carga de archivo XML anterior; Adjunta capturas de pantalla. · Adjuntos del correo: image001.png, image002.png, image003.png, image.png, image.png, image.png
- 2026-11-04 12:47 — Correo automático — Correo nuevo en el hilo: Matheus D., Developer III de NFQ, informa que está verificando el problema y responderá pronto. Adjunta capturas. Detalles: Proyecto: Aldrin - InvestCompany; Entorno: UAT; Tablas mencionadas: STG, SSS, `sss_inv_company_inst_t`; Problema: Falta un campo nuevo en la tabla `sss_inv_company_inst_t`; Los campos de la extracción no están en las tablas STG y SSS o no están correctamente mapeados; Un archivo anterior presentó un error de carga por la composición del XML; Se solicita verificar la presencia y mapeo de los campos de extracción en las tablas STG y SSS; Las capturas de pantalla adjuntas muestran el problema. · Adjuntos del correo: image001.png, image002.png, image003.png, image.png, image.png, image.png

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
- 2026-11-03 20:56 — nuevo → Abierto — Correo automático
- 2026-11-05 17:43 — Abierto → Revisión cliente — Marco Pichardo
- 2026-11-06 12:14 — Abierto → Revisión cliente — Matheus Fransoni

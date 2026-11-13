---
id: NFQBAU-1604
fecha_apertura: 2026-10-30
fecha_limite: 2026-10-30
fecha_resolucion:
estado: Revisión cliente
prioridad: Alta
responsable: Matheus Fransoni
origen: email
referencia_origen: Liberação Carteira ASA - Portal (2026-10-30)
categoria:
  - Qlik
entorno: []
sintoma: Error "Generation Failed. Please try later. Cash Statement [GFFQ]" al intentar generar el informe Cash Statement en el portal.
solucion_corta:
codigo_relacionado:
  - repo:
    modulo:
    version:
tickets_proveedor: []
decision_relacionada:
referencias_tecnicas: []
actualizado: 2026-11-09 16:27
actualizado_por: Correo automático
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Kleverson B., del equipo de tecnología, solicita soporte para verificar una incidencia reportada por Leonardo F., de ventas y relación con clientes de S3 Caceis. Leonardo reporta que no logran generar los cash statements tras la liberación de carteras de ASA y adjunta capturas.

Detalles: Mensaje de error: 'Generation Failed. Please try later. Cash Statement [GFFQ]'; Reporte solicitado: Cash Statement; Cartera afectada seleccionada: ENT044770 (ASA-US BUILDING BLOCKS SERIES LP - ASA-US BRAZIL FIXED RATE), con fecha de último procesamiento 29/10/2026; Cartera visible: ENT044851 (ASA-US BUILDING BLOCKS SERIES LP - ASA-US BRAZIL EQUITIES); La captura muestra que al buscar el código 'ENT044770' en la sección de Fundos no devuelve resultados (0 of 0); Mención a problemas previos de carga en el sistema Aldrin
Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png

## Histórico de interacciones

- 2026-10-30 10:18 — Correo automático — Kleverson B., del equipo de tecnología, solicita soporte para verificar una incidencia reportada por Leonardo F., de ventas y relación con clientes de S3 Caceis. Leonardo reporta que no logran generar los cash statements tras la liberación de carteras de ASA y adjunta capturas.
- 2026-10-30 10:29 — Correo automático — Correo nuevo en el hilo: Leonardo F., ventas y gestión de clientes de S3 Caceis, solicita asistencia urgente porque no consiguen generar los extractos de efectivo tras la liberación de la cartera ASA. Matheus D., desarrollador de NFQ, responde que están revisando el problema y adjunta capturas. Detalles: Mensaje de error literal: 'Generation Failed. Please try later. Cash Statement [GFFQ]'; Cartera/fundo afectado: ENT044770 (ASA-US BUILDING BLOCKS SERIES LP - ASA-US BRAZIL FIXED RATE); Fecha de último procesamiento: 29/10/2026; Una captura muestra el banner flotante rojo con el error de generación al marcar Cash Statement; Otra captura muestra la pantalla de búsqueda de fundos para ENT044770 devolviendo 0 resultados · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png
- 2026-10-30 11:56 — Correo automático — Correo nuevo en el hilo: Matheus D., desarrollador de NFQ, comunica que tras analizar el caso el informe se genera con éxito.
Indica además que no se encontraron datos para la combinación de cliente y fecha consultada y queda a disposición para prestar asistencia. Detalles: Informe: Cash Statement; Error en portal: 'Generation Failed. Please try later. Cash Statement [GFFQ]'; Cartera seleccionada: ENT044770 (ASA-US BUILDING BLOCKS SERIES LP - ASA-US BRAZIL FIXED RATE); Cartera ENT044851 visible en lista; Fecha de último procesamiento: 29/10/2026; La búsqueda del fondo ENT044770 devuelve 0 resultados; El equipo técnico confirma que el informe se genera correctamente pero no hay datos para esa combinación de cliente y fecha · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png
- 2026-10-30 11:57 — Correo automático — Correo nuevo en el hilo: Matheus D., Developer III de NFQ, informa que el informe "Cash Statement" se genera correctamente, pero no se encuentran datos para la combinación de cliente y fecha solicitada. Esto es una respuesta a la consulta de Leonardo F., Sales & Relationship Management, sobre la imposibilidad de generar los "cash statements" para el cliente ASA, lo que está afectando al equipo de operaciones. Adjunta capturas. Detalles: El informe afectado es "Cash Statement"; El error inicial era "Generation Failed. Please try later. Cash Statement [GFFQ]"; El problema actual es que no se encuentran datos para la combinación de cliente y fecha; Se menciona el código de cartera/fondo "ENT044770"; Una captura muestra el error "Generation Failed. Please try later. Cash Statement [GFFQ]" en la pantalla del portal al intentar generar el informe "Cash Statement" para la cartera "ENT044770 SERIES" con fecha de procesamiento 29/10/2026; Otra captura muestra que la búsqueda del fondo "ENT044770" en la sección "Fundos" devuelve "0 of 0". · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png
- 2026-11-03 11:37 — Correo automático — Correo nuevo en el hilo: Diogo M. F., Sales & Relationship Management, informa que siguen sin poder generar extractos de caja para las cuentas, incluyendo el nuevo cliente ROYAL BANK OF CANADA (ENT45092), donde ocurre el mismo error. También indica que los informes de carteras diarias de ASA están incorrectos, faltando posiciones de futuros y renta fija, aunque el PL total es correcto. Pide revisión y corrección. Adjunta capturas y un fichero. Detalles: Mensaje de error literal: "Generation Failed. Please try later. Cash Statement [GFFQ]"; Clientes/Portfolios afectados: ENT45092 - ROYAL BANK OF CANADA; carteras ASA (ej. ENT044851, ENT044835, ENT044797, ENT044770); Fecha de procesamiento en capturas: 30/10/2026; Problema en informes de carteras: solo muestran caja y cuentas a pagar/recibir; faltan posiciones de futuros y renta fija; Ejemplo de discrepancia en PL: informe presenta R$ 3.7k como activo único, pero PL total de R$ 56k; Capturas de pantalla (image001.png, image005.png, image011.png) muestran el portal "S3 caceis INVESTOR SERVICES" con el error "Generation Failed. Please try later. Cash Statement [GFFQ]" al intentar generar extractos de caja; y un ejemplo de informe con la discrepancia de PL. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png, image011.png, Daily Portfolio- bulk (88).pdf
- 2026-11-03 11:43 — Correo automático — Correo nuevo en el hilo: Diogo M. F., Sales & Relationship Management, informa que siguen sin poder generar el extracto de caja para las cuentas, mostrando un error [GFFQ]. Pide incluir el cliente ENT45092 - ROYAL BANK OF CANADA en el análisis para asegurar que los setups estén correctos antes de que el cliente inicie actividades. Adicionalmente, las carteras diarias extraídas para ASA están incorrectas, mostrando solo caja y cuentas a pagar/recibir, sin posiciones de futuros ni renta fija, aunque los activos se consideran en el PL total. Adjunta capturas. Detalles: Error literal: "Generation Failed. Please try later. Cash Statement [GFFQ]"; Clientes/Portafolios afectados: ENT044851, ENT044835, ENT044797, ENT044770, ENT044819, ENT45092 - ROYAL BANK OF CANADA; Fechas de los datos afectados: 29/10/2026, 30/10/2026; Discrepancia en informe Daily Portfolio Closing para ENT044797: Cash Balance R$ 3.729,12, Total R$ 3.729,12, pero PL total R$ 56.108,47; Los informes de carteras diarias no muestran posiciones de futuros ni renta fija; Adjunta capturas de pantalla que muestran el error "Generation Failed. Please try later. Cash Statement [GFFQ]" al intentar generar el extracto de caja y una captura del informe Daily Portfolio Closing con la discrepancia del PL. · Adjuntos del correo: image002.png, image003.png, image004.png, image012.png, image013.png, image014.png, image015.png, image016.png, image017.png, image018.png, image019.png
- 2026-11-09 16:27 — Correo automático — Correo nuevo en el hilo: Diogo M. solicita una actualización sobre las inconsistencias en las carteras diarias y el error al descargar el extracto de caja, que persisten desde al menos el 3 de noviembre. Menciona que Regina G. cree que los errores podrían estar relacionados con un ajuste catastral en MegaFA, donde las cuentas se registraron inicialmente con 'sec accounts' y luego se ajustaron a 'ENTs'. Adjunta capturas. Detalles: Mensaje de error literal: 'Generation Failed. Please try later. Cash Statement [GFFQ]'; Afecta a la descarga del extracto de caja y a los informes de carteras diarias; Los informes de carteras diarias solo muestran caja y cuentas a pagar/recibir, sin posiciones de futuros y renta fija; Ejemplo de inconsistencia en informe: R$ 3,7k como activo único, pero PL total de R$ 56k; Se solicita verificar el cliente ENT45092 - ROYAL BANK OF CANADA para el extracto de caja; Posible causa: ajuste catastral en MegaFA, con cuentas registradas inicialmente como 'sec accounts' y luego ajustadas a 'ENTs'; Capturas de pantalla muestran: pantalla de selección de extracto de caja con el error 'Generation Failed. Please try later. Cash Statement [GFFQ]' para varios ENT (ej. ENT044851, ENT044770); Informe 'Daily Portfolio Closing' para ENT044797 con fecha 30/10/2026, donde el Cash Balance y Total es 3.725,12 pero Refinanciary es 56.188,47. · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png, image005.png, image006.png, image007.png, image008.png, image009.png, image010.png, image011.png

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
- 2026-10-30 10:18 — nuevo → Abierto — Correo automático
- 2026-11-04 15:57 — Abierto → En curso — Matheus Fransoni
- 2026-11-05 12:24 — En curso → Revisión cliente — Marco Pichardo
- 2026-11-06 12:14 — En curso → Revisión cliente — Matheus Fransoni

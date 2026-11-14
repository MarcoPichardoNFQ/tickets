---
id: NFQBAU-1659
fecha_apertura: 2026-11-06
fecha_limite: 2026-11-07
fecha_resolucion: 2026-11-06
estado: Resuelto
prioridad: Media
responsable: Marco Pichardo
origen: email
referencia_origen: "Carga do arquivo "
categoria:
  - Rundeck
entorno:
  - UAT
sintoma: El archivo AdditionalDerivativePrice.XML no está siendo consumido por la carga automática.
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
ctualizado: 2026-11-06 20:56
ctualizado_por: Correo automático
tags:
  - ticket
  - bau
---

> [!abstract] Controles
> Estado `INPUT[inlineSelect(option('Abierto'),option('En curso'),option('Revisión cliente'),option('Pendiente despliegue UAT'),option('Pruebas cliente UAT'),option('Pendiente despliegue PRD'),option('Resuelto')):estado]` · Prioridad `INPUT[inlineSelect(option('Alta'),option('Media'),option('Baja')):prioridad]` · Responsable `INPUT[inlineSelect(option('Antonio Montoro'),option('Correo automático'),option('Deborah Bertoldo'),option('Ismael Barranco'),option('Jesús Horno'),option('Juan Antonio Gascón'),option('Manuel Hervas'),option('Marco Pichardo'),option('Matheus Fransoni'),option('Ricardo Reyes')):responsable]`
> Categoría `INPUT[inlineListSuggester(option('Rundeck'),option('BBDD'),option('Qlik'),option('APIs'),option('Otros')):categoria]` · Entorno `INPUT[inlineListSuggester(option('Producción'),option('UAT')):entorno]`
> `BUTTON[bau-ntt, bau-dashboard]`

## Resumen

Marcos M., tecnología, solicita análisis para descubrir por qué el archivo no está siendo procesado en el sistema, tras haberlo conversado previamente en la sala de proyectos. Adjunta ficheros.

Detalles: Nombre del archivo afectado: AdditionalDerivativePrice.XML; El problema ocurre en la carga automática del Rundeck de UAT; adjunta ficheros.
Adjuntos del correo: image001.png, image002.png, image003.png

## Histórico de interacciones

- 2026-11-06 20:01 — Correo automático — Marcos M., tecnología, solicita análisis para descubrir por qué el archivo no está siendo procesado en el sistema, tras haberlo conversado previamente en la sala de proyectos. Adjunta ficheros.
- 2026-11-06 20:06 — Correo automático — Correo nuevo en el hilo: Matheus D., Developer III de NFQ, solicita a Marcos A., de PR Serviços, su aprobación para que coecloudbrasilemeal de NTTData actualice el archivo lookup_java_flag.txt en UAT. Esto es para normalizar la carga automática de una interfaz. Adjunta capturas y un fichero. Detalles: Archivo afectado: AdditionalDerivativePrice.XML; Archivo a modificar: lookup_java_flag.txt; Ruta de creación/modificación: /nfq/data/cfg/; Acción solicitada: Actualizar lookup_java_flag.txt en UAT; Petición adicional: Hacer un backup del archivo existente; Adjunta capturas de pantalla y el fichero lookup_java_flag.txt. · Adjuntos del correo: image001.png, image002.png, image003.png, lookup_java_flag.txt
- 2026-11-06 20:11 — Correo automático — Correo nuevo en el hilo: Marcos Antonio M., tecnología de PR Serviços, da su aprobación para actualizar un fichero de configuración en el entorno de pruebas. Adjunta capturas. Detalles: Archivo afectado: AdditionalDerivativePrice.XML; Fichero a modificar: lookup_java_flag.txt; Ruta: /nfq/data/cfg/; adjunta capturas · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-06 20:29 — Correo automático — Correo nuevo en el hilo: Marco P., consultor senior de Nfq, solicita al equipo de soporte y operaciones aplicar las modificaciones solicitadas. La petición se realiza tras haber recibido la aprobación correspondiente para el entorno de UAT. Detalles: Archivo a procesar: AdditionalDerivativePrice.XML; Carga automática en Rundeck; Requiere actualizar el fichero lookup_java_flag.txt en la ruta /nfq/data/cfg/; Se debe realizar backup previo del fichero existente en el entorno · Adjuntos del correo: image001.png, image002.png, image003.png
- 2026-11-06 20:56 — Correo automático — Correo nuevo en el hilo: Fernando Augusto M., soporte en S3 Caceis, pide continuar con la solicitud actualizando los permisos por correo debido a que la creación de usuario de Marco sigue en curso. En el hilo, Marcos Meneses, tecnología en PR Serviços, solicitó analizar la falta de consumo del fichero XML en Rundeck. Detalles: Archivo afectado: AdditionalDerivativePrice.XML; Fichero de configuración a modificar: lookup_java_flag.txt; Ruta del archivo: /nfq/data/cfg/; adjunta capturas · Adjuntos del correo: image001.png, image002.png, image003.png, image004.png

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
- 2026-11-06 20:01 — nuevo → Abierto — Correo automático
- 2026-11-06 22:33 — nuevo → Abierto — Marco Pichardo
- 2026-11-06 22:44 — Abierto → Resuelto — Marco Pichardo

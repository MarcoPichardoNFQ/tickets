---
titulo: "D08 — Cifrado GPG y archivado del fichero"
familia: D
etapa: "Carga STG"
tipo: Referencia
tags:
  - familia/D
  - etapa/carga-stg
  - tipo/referencia
keywords: "gpg, cifrado, historificación, bk_stored, DIR_PROCESSED, InLoad, archivado"
---

# D08 — Cifrado GPG y archivado del fichero

**Etapa:** Carga STG
**Tipo:** Referencia
**Palabras clave:** gpg, cifrado, historificación, bk_stored, DIR_PROCESSED, InLoad, archivado

## En una línea

Cuando una carga termina bien, el fichero original se cifra con GPG, se mueve al histórico y se
borra del directorio de trabajo; si va mal, se le devuelve su nombre original y se queda.

## Detalle

### El camino de éxito

```bash
gpg --encrypt -r $key_cript $nom_process     # key_cript = "bk_stored"
mv $nom_process".gpg" $fileshare$ruta_hist   # ruta del campo 5 del lookup
echo $select"."$extn >> $bandera$procesed_files
rm -f $nom_process
```

Cuatro pasos: cifrar, archivar, anotar en el fichero de control, borrar el claro.

- **La clave de cifrado** es `bk_stored`, definida en `env.properties` como `key_cript`. Es el
  destinatario GPG, no una contraseña.
- **El destino** es `$fileshare` más la ruta del campo 5 de `lookup_stg.txt`, típicamente
  `DIR_PROCESSED/DIR_SAC/` o `DIR_PROCESSED/DIR_BULLE/`.
- **El fichero queda cifrado**: para leerlo hay que descifrarlo con la clave correspondiente.

### El camino de fallo

```bash
mv $nom_process $select"."$extn    # se le devuelve su nombre original
flag_error_gral=1
```

El fichero **no se archiva ni se borra**: recupera su nombre y se queda donde estaba, listo para
que la siguiente pasada lo vuelva a intentar. Es el mecanismo de reintento implícito del sistema.

### Los estados intermedios de un fichero

| Nombre | Significa |
|---|---|
| `FICHERO.txt` | En espera. La próxima ejecución lo cogerá |
| `FICHERO_InLoad.csv` | **En proceso ahora mismo**, o abandonado por un fallo brusco |
| `FICHERO.txt.gpg` en `DIR_PROCESSED/…` | Procesado correctamente y archivado |

Un fichero que lleva horas con el sufijo `_InLoad` es una señal clara: el proceso murió a mitad,
sin llegar ni al archivado ni a la restauración del nombre. **No se recogerá solo**, porque la
búsqueda de ficheros excluye explícitamente los `_InLoad`:

```bash
ls -ltr $raiz$fichero | grep -v '\_InLoad.'$extn'' | head -1
```

Acción: renombrarlo a su nombre original para que vuelva a la cola, tras comprobar que sus datos no
entraron ya (mira si hay un `cod_load_trace` con ese fichero en `AUD_LOAD_TRACE_T`).

### Cómo decide el script si fue bien

```bash
if [ "${V_OUT:0:4}" == "COPY" ]; then hist=`echo $V_OUT | awk '{print $3}'`; else hist=1; fi
if [ $hist -eq 0 ]; then  # archiva
```

Toma la salida del `\COPY` —de la forma `COPY 7573`— y se queda con la tercera palabra. Es una
comprobación frágil: depende del formato exacto del mensaje de `psql`. Si la salida cambia de
forma, el fichero no se archiva aunque la carga haya ido bien, y aparece como pendiente al día
siguiente.

## Cómo verificarlo

```bash
. /nfq/data/cfg/env.properties

# ¿Hay ficheros atascados en proceso?
find $raiz -name "*_InLoad*" -mmin +60 -ls

# Últimos ficheros archivados
ls -lat $fileshare"DIR_PROCESSED/DIR_SAC/" | head -20
```

```sql
-- ¿Este fichero llegó a cargarse alguna vez?
SELECT cod_load_trace, dat_load_date, cod_status, amt_register_process
FROM   stg_s3.aud_load_trace_t
WHERE  des_file_loaded LIKE '%<nombre_fichero>%'
ORDER  BY dat_load_date DESC;
```

## Ver también

[D03_script_stg_trf](../D%20-%20Carga%20STG/D03_script_stg_trf.md) · [D11_paso_omitido](../D%20-%20Carga%20STG/D11_paso_omitido.md) · [D13_cargo_dos_veces](../D%20-%20Carga%20STG/D13_cargo_dos_veces.md) · [A04_rutas_y_directorios](../A%20-%20Orientacion/A04_rutas_y_directorios.md)

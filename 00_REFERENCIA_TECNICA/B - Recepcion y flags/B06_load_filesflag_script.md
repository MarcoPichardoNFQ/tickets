---
titulo: "B06 — `load_filesflag_script.sh` paso a paso"
familia: B
etapa: "Recepción de flags"
tipo: Referencia
tags:
  - familia/B
  - etapa/recepcion-de-flags
  - tipo/referencia
keywords: "load_filesflag_script, TrackInnotech, recebido, 120 segundos, conversión encadenada"
---

# B06 — `load_filesflag_script.sh` paso a paso

**Etapa:** Recepción de flags
**Tipo:** Referencia
**Palabras clave:** load_filesflag_script, TrackInnotech, recebido, 120 segundos, conversión encadenada

## En una línea

Es el script que convierte el flag en registros de control: espera el fichero, lo parsea, comprueba
interfaz por interfaz qué llegó de verdad y dispara la conversión de lo presente.

## Los siete pasos

### 1. Carga configuración

```bash
. /nfq/data/cfg/credentials.properties
. /nfq/data/cfg/env.properties
. /nfq/data/cfg/db_config_gral.env     # define $DB_CONN
```

Si `db_config_gral.env` no existe, aborta de entrada.

### 2. Busca el flag, hasta 120 segundos

```bash
tiempo_max=120
while [[ $contador -lt $tiempo_max ]]; do
    archivo=$(find "$primero" -maxdepth 1 -name "$segundo*.xml" -type f | head -n 1)
    [[ -n "$archivo" ]] && break
    sleep 1; ((contador++))
done
[[ -z "$archivo" ]] && exit 1
```

Dos minutos de espera activa. Si el flag no aparece, el job termina en error. Ver
[R4_06_xml_sin_flag](../R4%20-%20Sets%20incompletos/R4_06_xml_sin_flag.md) para el caso contrario.

### 3. Registra la llegada

```sql
UPDATE stg_s3.controlflag_arquivos
SET    nome_completo = '<fichero>', data_recebemento = '<fecha del fichero>'
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
  AND  nome_base = '<flag>';
```

Es un `UPDATE`, no un `INSERT`: la fila la crea antes `LlamadaTablaControlArquivosFlag`. Si esa
fila no existe, este `UPDATE` no afecta a nada **y el script continúa sin avisar**.

La fecha registrada es la de modificación del fichero, no la del momento de la detección.

### 4. Parsea el flag

```bash
grep -oP '<com.vermeg.services.innotech.TrackInnotech[^>]+>' "$archivo" | while read -r line; do
    filename=$(echo "$line" | grep -oP 'filename="\K[^"]+')
    code=$(echo "$line"     | grep -oP 'innotechInterface_code="\K[^"]+')
    status=$(echo "$line"   | grep -oP 'trackStatus="\K[^"]+')
    ...
```

Un elemento por interfaz declarada. Ver [B01_que_es_un_flag](../B%20-%20Recepcion%20y%20flags/B01_que_es_un_flag.md).

### 5. Comprueba qué llegó realmente

```bash
interfacee=$(find "$primero" -maxdepth 1 -name "$filename*.xml" -type f | head -n 1)
if [[ -n "$interfacee" ]]; then
    tamanho_archivo=$(stat -c %s "$interfacee")
    ./load_java2_optiflag_script.sh "${code}_.xml" "$filename" &   # ← dispara la conversión
    recebido="Verdadero"
fi
```

**Éste es el corazón del control de sets completos.** El flag dice qué debería estar; el `find` dice
qué está. La diferencia es lo que falta.

Y si está, **lanza la conversión en segundo plano** sin esperar a que termine.

### 6. Escribe el control

Dos inserciones por interfaz, en dos tablas distintas:

- `stg_s3.controlflag_interfaces` — el control principal
- `trf_s3.tmp_controlflag_interfaces` — igual, más el **tamaño del fichero**

Ambas se lanzan en segundo plano con `&`. Ver [B07_tablas_controlflag](../B%20-%20Recepcion%20y%20flags/B07_tablas_controlflag.md).

### 7. Archiva el flag

```bash
destino="$primero/Flags"
mkdir -p "$destino"
# si ya existe uno igual, añade marca de tiempo en vez de sobrescribir
```

## Cuatro cosas que conviene saber

**Un proceso `psql` por interfaz, en paralelo y sin límite.** Cada vuelta lanza dos consultas en
segundo plano. Con un flag que declare cien interfaces son doscientos procesos concurrentes. En
lotes grandes eso se nota, y explica picos de conexiones a la base de datos coincidiendo con la
llegada de un flag.

**El bucle corre en una subshell.** Al estar detrás de una tubería, las variables que se asignan
dentro no sobreviven al bucle. No afecta al funcionamiento actual, pero invalida cualquier intento
de acumular un contador dentro.

**`load_java2_optiflag_script.sh` no está en el repositorio.** Se invoca aquí pero no aparece entre
los scripts disponibles. Su comportamiento se deduce del script hermano `load_java_script.sh`
(ver [C02_load_java_script](../C%20-%20Conversion%20Java/C02_load_java_script.md)), pero **no está verificado**.

**El estado se compara contra `'Processd'`**, escrito sin la «e». Ver el aviso en [B01_que_es_un_flag](../B%20-%20Recepcion%20y%20flags/B01_que_es_un_flag.md).

## Cómo verificarlo

```sql
-- Lo que el flag declaró frente a lo que llegó, en el lote actual
SELECT nome_interface_base, nome_interface_completo,
       recebido, track_status, data_recebemento
FROM   stg_s3.controlflag_interfaces
WHERE  id_camda = (SELECT last_value FROM exp_s3.controlflag_arquivos_cod_id_seq)
ORDER  BY recebido, nome_interface_base;
```

## Ver también

[B01_que_es_un_flag](../B%20-%20Recepcion%20y%20flags/B01_que_es_un_flag.md) · [B07_tablas_controlflag](../B%20-%20Recepcion%20y%20flags/B07_tablas_controlflag.md) · [R4_02_controlflag_interfaces](../R4%20-%20Sets%20incompletos/R4_02_controlflag_interfaces.md) · [C02_load_java_script](../C%20-%20Conversion%20Java/C02_load_java_script.md) · [B08_id_camda_lote](../B%20-%20Recepcion%20y%20flags/B08_id_camda_lote.md)

---
titulo: "G06 — Catálogo de las 119 funciones de mapeo vivas"
familia: G
etapa: "Mapeos"
tipo: Referencia
tags:
  - familia/G
  - etapa/mapeos
  - tipo/referencia
keywords: "catálogo, mapeos, function_meg, joins, ON CONFLICT, _err, base_id, inventario"
---

# G06 — Catálogo de las 119 funciones de mapeo vivas

**Etapa:** Mapeos
**Tipo:** Referencia
**Palabras clave:** catálogo, mapeos, function_meg, joins, ON CONFLICT, _err, base_id, inventario

## En una línea

Las 119 funciones que el despacho ejecuta realmente, con las cuatro características que determinan
cómo se comporta cada una ante una incidencia.

## Lo que TODAS comparten

Antes de la tabla, lo que no hace falta consultar porque es universal:

| Rasgo | Alcance |
|---|---|
| **`ON CONFLICT … DO UPDATE`** | 119 de 119. Ninguna usa `DO NOTHING` |
| **Escriben en `trf_s3.<TABLA>_err`** | 119 de 119 |
| **Deduplican** con `DISTINCT` o `GROUP BY` | 119 de 119 |
| **Filtran por `cod_flag_mapeo`** | 119 de 119 |
| Leen y escriben dentro de **`trf_s3`** | Sólo 16 mencionan `exp_s3`; una sola menciona `_temp` |

Tres consecuencias que valen para cualquier mapeo, sin mirar el catálogo:

**El último en llegar gana.** Como todas hacen `DO UPDATE` y ninguna `DO NOTHING`, una clave
repetida no duplica: sobrescribe. Si el valor final no es el esperado, el problema es de orden, no
de filas de más. Ver [R2_06_duplicados_en_mapeos](../R2%20-%20Duplicados/R2_06_duplicados_en_mapeos.md).

**Sí hay tabla de descartes en esta capa: `trf_s3.<TABLA>_err`.** El patrón es siempre el mismo —una
CTE que agrupa por la clave natural con `HAVING COUNT(*) > 1` y manda los repetidos a `_err`. Es
deduplicación por clave, no validación de contenido. Ver [R1_08_descartes_en_mapeos](../R1%20-%20Descartes/R1_08_descartes_en_mapeos.md).

```sql
-- Duplicados apartados por un mapeo
SELECT count(*) FROM trf_s3.<TABLA>_err;
SELECT * FROM trf_s3.<TABLA>_err ORDER BY dat_qlikupdate DESC LIMIT 20;
```

**`cod_flag_mapeo` gobierna qué filas entran.** Aparece en las 119. Si un mapeo procesa cero filas
teniendo datos en origen, este filtro es la primera sospecha. Ver [R3_05_mapeo_cero_filas](../R3%20-%20Errores%20de%20mapeo/R3_05_mapeo_cero_filas.md).

## Cómo leer la tabla

| Columna | Qué significa para el diagnóstico |
|---|---|
| **Líneas** | Complejidad. Por encima de 200 conviene reservar tiempo antes de leerla |
| **Joins** | `inner / left`. Un `INNER` que no casa **elimina la fila**; un `LEFT` sólo deja nulos. Ante filas que faltan, mira primero los inner |
| **Borrado** | `DEL` o `TRUNC` = borra antes de insertar, así que **relanzarla es seguro**. Vacío = sólo hace upsert |
| **`base_id`** | Filtra por identificador de base. Si falta el dato, comprueba también este filtro |

## Distribución

- **28 funciones sin ningún join** — transformaciones directas de una sola tabla
- **63 con 1-2 joins** — el caso normal
- **18 con 3-5**, y **10 con 6 o más** — las que exigen leer el SQL
- **19 borran antes de insertar** (18 `DELETE`, 1 `TRUNCATE`): las seguras de relanzar
- **85 filtran por `base_id`**, 34 no
- Media de 116 líneas; la mayor, `cart_pos_rf_t`, con 796

## Las 15 más complejas

| Función | Líneas | inner / left |
|---|---|---|
| `cart_pos_rf_t` | 796 | 9 / 17 |
| `cart_estat_clibas_t` | 455 | — / 20 |
| `sac_pl_cl_patrrf_t` | 424 | 8 / 4 |
| `cart_pos_rv_t` | 335 | 1 / — |
| `cart_pos_fu_t` | 333 | 7 / 2 |
| `sac_pl_cl_patrfut_t` | 320 | 6 / 3 |
| `sac_cl_patr` | 313 | **28** / 6 |
| `cart_caixa_cpr_t9` | 312 | — / — |
| `cart_pos_fi_t` | 269 | 1 / — |
| `sac_stat_rf_lastro_t` | 229 | 4 / — |
| `sac_stat_fi_cad_t` | 210 | — / 1 |
| `sac_cart_patr` | 210 | 1 / — |
| `sac_pl_cl_patrrv_t` | 201 | 1 / 6 |
| `sac_mov_rf_t` | 191 | — / — |
| `cart_estat_rentab_t` | 190 | 3 / 1 |

`sac_cl_patr` con 28 `INNER JOIN` es la más frágil del sistema: 28 oportunidades de que una fila
desaparezca sin dejar rastro.

## Las 19 que borran antes de insertar

Son las únicas donde relanzar es inequívocamente seguro:

`cart_caixa_cpr_t9` · `cart_caixa_mt_t_2` · `cart_estat_clibas_t` · `cart_pos_fi_t` ·
`cart_pos_fu_t` · `cart_pos_rf_t` · `cart_pos_rv_1_t` · `cart_pos_rv_em_t` · `cart_pos_rv_t` ·
`cart_pos_sw_t` · `sac_cart_patr` · `sac_pl_cl_patrfi_t` · `sac_pl_cl_patrfut_t` ·
`sac_pl_cl_patrrf_t` · `sac_pl_cl_patrrv_t` · `sac_pos_rv_em_rem_t` · `sac_stat_ba_script_t` ·
`sac_stat_cl_liquid2_t` (TRUNCATE) · `sac_stat_rv_em_pos_ta_re_t`

En las otras 100, relanzar sólo repite el upsert. No duplica —gracias al `ON CONFLICT`— pero
tampoco limpia lo que sobró de una ejecución anterior. Ver [R3_11_relanzar_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_11_relanzar_mapeo.md).

## Catálogo completo

Nombre sin el prefijo `function_meg_`.

| Función | Líneas | inner / left | Borrado | `base_id` |
|---|---|---|---|---|
| `cart_caixa_cpr_t` | 100 | — / — | — | sí |
| `cart_caixa_cpr_t10` | 101 | 1 / — | — | sí |
| `cart_caixa_cpr_t11` | 106 | 1 / 1 | — | sí |
| `cart_caixa_cpr_t12` | 96 | 1 / — | — | sí |
| `cart_caixa_cpr_t13` | 96 | 1 / — | — | sí |
| `cart_caixa_cpr_t14` | 101 | 1 / — | — | sí |
| `cart_caixa_cpr_t15` | 118 | 1 / 1 | — | sí |
| `cart_caixa_cpr_t16` | 98 | 1 / 1 | — | sí |
| `cart_caixa_cpr_t18` | 100 | 1 / — | — | sí |
| `cart_caixa_cpr_t2` | 93 | — / 1 | — | sí |
| `cart_caixa_cpr_t3` | 95 | — / 1 | — | sí |
| `cart_caixa_cpr_t4` | 97 | — / 1 | — | sí |
| `cart_caixa_cpr_t8` | 100 | 1 / 1 | — | sí |
| `cart_caixa_cpr_t9` | 312 | — / — | DEL | sí |
| `cart_caixa_mt_t` | 168 | 2 / 1 | — | sí |
| `cart_caixa_mt_t_2` | 119 | 2 / — | DEL | sí |
| `cart_caixa_saldo_t` | 124 | 2 / — | — | sí |
| `cart_estat_clibas_t` | 455 | — / 20 | DEL | sí |
| `cart_estat_gestor_t` | 57 | — / 2 | — | sí |
| `cart_estat_rentab_t` | 190 | 3 / 1 | — | sí |
| `cart_pos_fi_t` | 269 | 1 / — | DEL | sí |
| `cart_pos_fu_t` | 333 | 7 / 2 | DEL | sí |
| `cart_pos_rf_t` | 796 | 9 / 17 | DEL | sí |
| `cart_pos_rv_1_t` | 165 | 3 / 5 | DEL | sí |
| `cart_pos_rv_em_t` | 184 | 1 / — | DEL | sí |
| `cart_pos_rv_t` | 335 | 1 / — | DEL | sí |
| `cart_pos_sw_t` | 140 | — / — | DEL | sí |
| `sac_ba_bloqueio_t` | 48 | — / — | — | sí |
| `sac_ba_bolsa_t` | 64 | — / 1 | — | — |
| `sac_ba_clearing` | 50 | — / 1 | — | — |
| `sac_ba_local_custodia` | 50 | — / 1 | — | sí |
| `sac_bas_moeda_t` | 52 | — / — | — | — |
| `sac_cart_estat_administracao_t` | 56 | — / 1 | — | sí |
| `sac_cart_patr` | 210 | 1 / — | DEL | sí |
| `sac_cl_patr` | 313 | 28 / 6 | — | sí |
| `sac_fi_mov` | 145 | — / 2 | — | sí |
| `sac_fu_mov` | 114 | 2 / 2 | — | sí |
| `sac_mov_rf_oper_t` | 131 | — / 1 | — | sí |
| `sac_mov_rf_oper_t_2` | 87 | — / — | — | sí |
| `sac_mov_rf_t` | 191 | — / — | — | sí |
| `sac_mov_rv_t` | 142 | 1 / — | — | sí |
| `sac_mov_rv_termo_t` | 119 | 1 / 3 | — | sí |
| `sac_mov_sw2_t` | 108 | — / — | — | sí |
| `sac_pl_cl_cotas_t` | 108 | 1 / 1 | — | sí |
| `sac_pl_cl_patrfi_t` | 151 | 2 / 1 | DEL | sí |
| `sac_pl_cl_patrfut_t` | 320 | 6 / 3 | DEL | sí |
| `sac_pl_cl_patrrf_t` | 424 | 8 / 4 | DEL | sí |
| `sac_pl_cl_patrrv_t` | 201 | 1 / 6 | DEL | sí |
| `sac_pl_cl_patrrv_termo_t` | 105 | 4 / — | — | sí |
| `sac_pos_rv_em_rem_t` | 135 | 4 / — | DEL | sí |
| `sac_pos_rv_emp_acoes_t` | 136 | 3 / 2 | — | sí |
| `sac_regul_cl_conta_corr_t` | 67 | — / 4 | — | — |
| `sac_sac_rf_eventos` | 77 | — / — | — | sí |
| `sac_sac_rf_memoria` | 114 | 12 / — | — | sí |
| `sac_stat_ba_contrapartes_t` | 50 | — / 1 | — | — |
| `sac_stat_ba_script_t` | 61 | 1 / — | DEL | sí |
| `sac_stat_ba_tipo_bloq_t` | 48 | — / — | — | sí |
| `sac_stat_bas_cad_control_1_t` | 51 | — / 1 | — | sí |
| `sac_stat_bas_cad_control_t` | 51 | — / 1 | — | sí |
| `sac_stat_bas_cad_emp_t` | 64 | 1 / 1 | — | — |
| `sac_stat_bas_cad_fer_4_t` | 46 | — / 1 | — | sí |
| `sac_stat_bas_cad_fer_8_t` | 46 | — / 1 | — | sí |
| `sac_stat_bas_cad_if_10_t` | 67 | — / 1 | — | — |
| `sac_stat_bas_cad_if_11_t` | 67 | — / 1 | — | — |
| `sac_stat_bas_cad_if_12_t` | 70 | — / 2 | — | — |
| `sac_stat_bas_cad_if_13_t` | 70 | — / 2 | — | — |
| `sac_stat_bas_cad_if_14_t` | 70 | — / 2 | — | — |
| `sac_stat_bas_cad_if_15_t` | 67 | — / 1 | — | — |
| `sac_stat_bas_cad_if_16_t` | 64 | 1 / — | — | — |
| `sac_stat_bas_cad_if_2_t` | 71 | — / 2 | — | — |
| `sac_stat_bas_cad_if_3_t` | 71 | — / 2 | — | — |
| `sac_stat_bas_cad_if_4_t` | 68 | — / 1 | — | — |
| `sac_stat_bas_cad_if_5_t` | 63 | — / — | — | — |
| `sac_stat_bas_cad_if_6_t` | 68 | — / 1 | — | — |
| `sac_stat_bas_cad_if_7_t` | 70 | — / 2 | — | — |
| `sac_stat_bas_cad_if_8_t` | 67 | — / 1 | — | — |
| `sac_stat_bas_cad_if_9_t` | 69 | — / 2 | — | — |
| `sac_stat_bas_cad_if_t` | 72 | — / 2 | — | — |
| `sac_stat_bas_xrate_t` | 49 | 1 / — | — | sí |
| `sac_stat_batip_liqfin_t` | 57 | — / — | — | sí |
| `sac_stat_cl_liquid2_t` | 151 | 1 / — | TRUNC | — |
| `sac_stat_cl_mc_txadm_t` | 177 | 3 / 3 | — | sí |
| `sac_stat_cl_pfee_t` | 49 | — / — | — | sí |
| `sac_stat_cli_addr_t` | 78 | 1 / — | — | — |
| `sac_stat_fi_bloqueio_2_t` | 61 | — / 4 | — | sí |
| `sac_stat_fi_bloqueio_t` | 60 | — / 3 | — | sí |
| `sac_stat_fi_cad_t` | 210 | — / 1 | — | sí |
| `sac_stat_fu_ativo_t` | 75 | — / — | — | sí |
| `sac_stat_fu_ativo_t1` | 58 | — / 1 | — | sí |
| `sac_stat_fu_ativo_t2` | 59 | — / 1 | — | sí |
| `sac_stat_fu_ativo_t3` | 64 | — / 1 | — | sí |
| `sac_stat_fu_cotativo_t` | 99 | — / — | — | — |
| `sac_stat_fu_vcto_t` | 73 | 1 / — | — | — |
| `sac_stat_idx_index_t` | 51 | — / — | — | — |
| `sac_stat_idx_index_t2` | 53 | 1 / — | — | — |
| `sac_stat_idx_index_t3` | 51 | — / — | — | — |
| `sac_stat_idx_indexdir_t` | 53 | — / — | — | — |
| `sac_stat_idx_indexdir_t1` | 63 | — / 1 | — | — |
| `sac_stat_idx_indexdir_t2` | 57 | — / — | — | — |
| `sac_stat_mt_caixa_tipos_t` | 56 | — / — | — | — |
| `sac_stat_rf_bloqueio_2_t` | 63 | — / 4 | — | sí |
| `sac_stat_rf_bloqueio_t` | 62 | — / 3 | — | sí |
| `sac_stat_rf_lastro_t` | 229 | 4 / — | — | sí |
| `sac_stat_rf_tipo_t` | 108 | 1 / 4 | — | sí |
| `sac_stat_rv_bloqueio_2_t` | 68 | — / 5 | — | sí |
| `sac_stat_rv_bloqueio_t` | 68 | — / 4 | — | sí |
| `sac_stat_rv_cadcor_t` | 99 | — / — | — | sí |
| `sac_stat_rv_cadpap_flex_t` | 104 | — / — | — | sí |
| `sac_stat_rv_cadpap_t` | 159 | — / — | — | sí |
| `sac_stat_rv_cadpap_t1` | 128 | — / — | — | — |
| `sac_stat_rv_cotpap_t` | 81 | — / — | — | sí |
| `sac_stat_rv_custos_t` | 129 | 1 / — | — | sí |
| `sac_stat_rv_div_t` | 117 | 1 / — | — | sí |
| `sac_stat_rv_divid_pag_pos_conta_t` | 95 | — / 1 | — | sí |
| `sac_stat_rv_divid_pag_pos_t` | 91 | — / — | — | sí |
| `sac_stat_rv_divid_qtd_pos_t` | 97 | — / — | — | sí |
| `sac_stat_rv_em_pos_ta_re_t` | 138 | 4 / — | DEL | sí |
| `sac_stat_rvmov_liqtermo_t` | 93 | 1 / 1 | — | sí |
| `sac_stat_sw_cad_t` | 94 | — / — | — | sí |

## Cómo leer una función concreta

```sql
SELECT prosrc FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE  n.nspname = 'trf_s3' AND lower(p.proname) = lower('function_meg_<nombre>');
```

El `lower()` en ambos lados es obligatorio: `tablas_mapeio_t` guarda los nombres en mayúsculas
mezcladas. Ver [J10_trampas_conocidas](../J%20-%20Operacion/J10_trampas_conocidas.md).

## Alcance de este catálogo

Cubre las **119 funciones declaradas en `exp_s3.tablas_mapeio_t` que existen en el repositorio**.
Quedan fuera:

- **33 ficheros huérfanos** que la tabla de control no declara: no se ejecutan. Ver [G10_codigo_sin_llamadas](../G%20-%20Mapeos/G10_codigo_sin_llamadas.md)
- **3 declaradas** cuyo fichero no está en el volcado del repositorio

## Ver también

[G01_que_es_un_mapeo](../G%20-%20Mapeos/G01_que_es_un_mapeo.md) · [G08_fim_carga_mapeo](../G%20-%20Mapeos/G08_fim_carga_mapeo.md) · [R3_10_corrio_pero_no_llego](../R3%20-%20Errores%20de%20mapeo/R3_10_corrio_pero_no_llego.md) · [R3_11_relanzar_mapeo](../R3%20-%20Errores%20de%20mapeo/R3_11_relanzar_mapeo.md) · [R2_06_duplicados_en_mapeos](../R2%20-%20Duplicados/R2_06_duplicados_en_mapeos.md) · [R1_08_descartes_en_mapeos](../R1%20-%20Descartes/R1_08_descartes_en_mapeos.md)

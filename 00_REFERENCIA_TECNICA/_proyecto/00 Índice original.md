# Índice — Base de conocimiento BAU, Aldrin AS-IS

**179 fichas — las 12 familias completas.** Cada una es un archivo independiente en `fichas/`, para
subir a NotebookLM como fuente.

**Si tienes una incidencia entre manos, empieza por [A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md).**
**Si es tu primer día, por [A01_que_es_aldrin](../A%20-%20Orientacion/A01_que_es_aldrin.md).**

---

## Runbooks — los cinco dolores

### R1. Descartes — 12 ✅

`R1_01_descarte_vs_error` · `R1_02_donde_cae_cada_cosa` · `R1_03_identificar_validacion` ·
`R1_04_descarte_nulo_obligatorio` · `R1_05_descarte_formato` ·
`R1_06_descarte_integridad_referencial` · `R1_07_descarte_variacion_volumen` ·
`R1_08_descartes_en_mapeos` · `R1_09_reprocesar_descartes` ·
`R1_10_descarte_correcto_sin_accion` · `R1_11_consultas_descartes` ·
`R1_12_descarte_masivo_escalado`

### R2. Duplicados — 9 ✅

`R2_01_deteccion_duplicados` · `R2_02_traza_duplicados` · `R2_03_dentro_o_entre_cargas` ·
`R2_04_archivo_llego_dos_veces` · `R2_05_duplicados_por_relanzar` · `R2_06_duplicados_en_mapeos` ·
`R2_07_limpiar_sin_romper` · `R2_08_consultas_duplicados` · `R2_09_prevencion_duplicados`

### R3. Errores de mapeo — 12 ✅

`R3_01_anatomia_fallo_mapeo` · `R3_02_leer_error_mapeo` · `R3_03_deadlock_40p01` ·
`R3_04_mapeo_no_arranco` · `R3_05_mapeo_cero_filas` · `R3_06_mapeo_bloqueado` ·
`R3_07_mapeo_desactivado` · `R3_08_dependencia_insatisfecha` · `R3_09_contador_no_cero` ·
`R3_10_corrio_pero_no_llego` · `R3_11_relanzar_mapeo` · `R3_12_consultas_mapeos`

### R4. Bloques de archivos incompletos — 11 ✅

`R4_01_que_es_un_set_completo` · `R4_02_controlflag_interfaces` · `R4_03_validacion_cantidades` ·
`R4_04_s3_interface_control` · `R4_05_flag_sin_xml` · `R4_06_xml_sin_flag` ·
`R4_07_dir_unmatched` · `R4_08_fuera_de_ventana` · `R4_09_esperar_forzar_escalar` ·
`R4_10_consultas_que_falta` · `R4_11_efecto_domino`

### R5. Alertas de Rundeck — 10 ✅

`R5_01_como_notifica_rundeck` · `R5_02_jobs_sin_notificacion` · `R5_03_listas_distribucion` ·
`R5_04_alertas_con_y_sin_log` · `R5_05_leer_log_job` · `R5_06_duracion_anomala` ·
`R5_07_alerta_vs_estado_real` · `R5_08_analise_de_erros_anulado` · `R5_09_catalogo_alertas` ·
`R5_10_cadena_escalado`

---

## Referencia por etapa

### A. Orientación — 7 ✅

`A01_que_es_aldrin` · `A02_flujo_e2e_seis_pasos` · `A03_glosario` · `A04_rutas_y_directorios` ·
`A05_esquemas_base_de_datos` · `A06_arbol_decision_incidencias` · `A07_ventanas_ejecucion`

### B. Recepción y flags — 9 ✅

`B01_que_es_un_flag` · `B02_los_nueve_flags` · `B03_ciclo_de_vida_del_fichero` ·
`B04_job_validacion_constante` · `B05_job_manejo_flag` · `B06_load_filesflag_script` ·
`B07_tablas_controlflag` · `B08_id_camda_lote` · `B09_ciclo_cerrado_api_megara`

### C. Conversión Java — 12 ✅

`C01_que_hace_xmlconversor` · `C02_load_java_script` · `C03_lookup_java_formato` ·
`C04_validacion_xsd` · `C05_sed_separador` · `C06_ficheros_de_salida` · `C07_herencias_claves` ·
`C08_cifrado_xml_original` · `C09_xml_no_valida` · `C10_conversion_sin_filas` ·
`C11_separador_dentro_del_dato` · `C12_conversion_fallo_log`

### D. Carga a staging — 13 ✅

`D01_mecanica_carga_copy` · `D02_lookup_stg_formato` · `D03_script_stg_trf` ·
`D04_read_header_fn` · `D05_run_load_plan_pc` · `D06_load_files_pc` ·
`D07_bloques_optimizacio` · `D08_gpg_historificacion` · `D09_error_numero_columnas` ·
`D10_tabla_t_vacia` · `D11_paso_omitido` · `D12_carga_colgada` · `D13_cargo_dos_veces`

### E. Parametrización y validación — 8 ✅

`E01_tablas_par_metadata_driven` · `E02_par_load_plan_t` · `E03_par_maestro_tablas_columnas` ·
`E04_par_maestro_mask_t` · `E05_par_maestro_valid_t` · `E06_tablas_auditoria` ·
`E07_validate_gen_pc` · `E08_log_trace_niveles`

### F. Transformación TRF — 12 ✅

`F01_que_hace_la_capa_trf` · `F02_lookup_trf_formato` · `F03_funcion_trf` ·
`F05_familias_procedimientos` · `F06_dependencias_oleadas` · `F07_bloqueio_insercao_dados` ·
`F08_actualizacao_carga_megara` · `F09_load_bulle_sac_fidc` · `F10_localizar_fallo_trf` ·
`F11_trf_corrio_sin_cambios` · `F13_bloque_lento` · `F14_faltan_datos_stg_o_trf`

### G. Mapeos — 12 ✅

`G01_que_es_un_mapeo` · `G02_tablas_mapeio_activo` · `G03_control_inicio_carga_mapeo` ·
`G04_jobs_mapeos` · `G05_anatomia_job_mapeo` · `G06_catalogo_mapeos` ·
`G07_ciclo_completo_mapeos` · `G08_fim_carga_mapeo` · `G09_job_control_errores` ·
`G10_codigo_sin_llamadas` · `G11_mapeos_multifuncion` · `G12_tablas_err_mapeos`

### H. Cierre y Qlik — 18 ✅

`H01_cerrar_el_lote` · `H02_stg_startover_cleanup` · `H03_validacion_descartes` ·
`H04_procedimiento_finalizacion` · `H05_actualizar_tablas_y_control` · `H06_script_carga_qlik` ·
`H07_lookup_qlik` · `H08_recarga_qlik` · `H09_qlik_datos_de_ayer` ·
`H10_cierre_no_completado` · `H11_qvd_incremental` · `H12_recarga_qlik_fallo` ·
`H13_fechas_de_corte` · `H14_section_access` · `H15_catalogo_tareas_qlik` ·
`H16_credenciales_qlik` · `H17_conteo_no_cuadra` · `H18_cliente_no_aparece`

### I. Referencia de datos — 18 ✅

`I01_convencion_nombres` · `I02_inventario_stg_s3` · `I03_inventario_trf_s3` ·
`I04_inventario_exp_s3` · `I05_tablas_control_auditoria` · `I06_catalogo_interfaces_mega` ·
`I07_codigos_cod_dm` · `I08_secuencias` · `I09_indice_tabla_origen` ·
`I10_rastrear_hacia_atras` · `I11_rastrear_un_fichero_e2e` · `I12_consultas_frecuentes` ·
`I13_leer_aud_log_trace` · `I14_calendario_ejecucion` · `I15_volumetria_tipica` ·
`I16_dias_habiles` · `I17_ficheros_configuracion` · `I18_columnas_comunes`

### J. Operación — 10 ✅

`J01_organizacion_rundeck` · `J02_orquestadores_raiz` · `J03_relanzar_seguro` ·
`J04_que_no_tocar` · `J05_donde_vive_cada_credencial` · `J06_servidores_accesos` ·
`J07_escalado` · `J08_los_cinco_ruidosos` · `J09_checklist_diario` · `J10_trampas_conocidas`

### K. BULLE / SAC / FIDC — 6 ✅

`K01_bulle_sac_fidc` · `K02_interfaces_bulle` · `K03_interfaces_sac` ·
`K04_fidc_kyc_alertas` · `K05_runbook_bulle_sac` · `K06_ficheros_ctrl`

---

## Las cinco que más se usan

1. **[A06_arbol_decision_incidencias](../A%20-%20Orientacion/A06_arbol_decision_incidencias.md)** — por dónde empezar ante cualquier ticket
2. **[J10_trampas_conocidas](../J%20-%20Operacion/J10_trampas_conocidas.md)** — lo que parece un fallo y no lo es, y lo que parece correcto y no lo está
3. **[J09_checklist_diario](../J%20-%20Operacion/J09_checklist_diario.md)** — la verificación que compensa los fallos silenciosos
4. **[I09_indice_tabla_origen](../I%20-%20Referencia%20de%20datos/I09_indice_tabla_origen.md)** — quién debería haber escrito este dato
5. **[I12_consultas_frecuentes](../I%20-%20Referencia%20de%20datos/I12_consultas_frecuentes.md)** — las consultas del día a día

## Los hallazgos que cambian cómo se diagnostica

| Hallazgo | Ficha |
|---|---|
| 261 tablas `_DES` pueden perder filas al descartar, sin traza | [R2_02_traza_duplicados](../R2%20-%20Duplicados/R2_02_traza_duplicados.md) |
| En staging **nada** detecta ni impide un duplicado | [R2_01_deteccion_duplicados](../R2%20-%20Duplicados/R2_01_deteccion_duplicados.md) |
| Un mapeo con `retry_deadlock` NULL **no se ejecuta y se marca como completado** | [R3_03_deadlock_40p01](../R3%20-%20Errores%20de%20mapeo/R3_03_deadlock_40p01.md) |
| 22 de 46 jobs no avisan si fallan | [R5_02_jobs_sin_notificacion](../R5%20-%20Alertas%20Rundeck/R5_02_jobs_sin_notificacion.md) |
| `_00001 Análise de erros` está anulado con `WHERE 1=0` | [R5_08_analise_de_erros_anulado](../R5%20-%20Alertas%20Rundeck/R5_08_analise_de_erros_anulado.md) |
| Un fallo de recarga de Qlik no genera ninguna alerta | [H12_recarga_qlik_fallo](../H%20-%20Cierre%20y%20Qlik/H12_recarga_qlik_fallo.md) |
| `ArchivoAyudaRundeckMegara.txt` para el ciclo entero, en verde | [B09_ciclo_cerrado_api_megara](../B%20-%20Recepcion%20y%20flags/B09_ciclo_cerrado_api_megara.md) |
| 63 piezas de código existen y no se ejecutan | [G10_codigo_sin_llamadas](../G%20-%20Mapeos/G10_codigo_sin_llamadas.md) |

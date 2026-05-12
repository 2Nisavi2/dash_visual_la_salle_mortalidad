## Función para el tratameinto incial de datos desde capa bronce a capa
def transformacion_data(data_anexo_1_bronce,
                        data_anexo_2_bronce,
                        data_divi_bronce):
    """
    Función para el tratameinto incial de datos desde capa bronce a capa.    
    Parámetros:    -----------
    df : pandas.DataFrame de las tres fuentes bronce (anexo_1, anexo_2 y divipola)   
    Retorna:    --------
    resumen_df : pandas.DataFrame de las tres fuentes tratadas.
    """   
    ## Liberias
    import unicodedata

    ## Data Anexo 1----------------------------------------------------------------
    data_anex_1_pla = data_anexo_1_bronce.copy()

    ## Normalización de nombres de columnas
    data_anex_1_pla.columns = data_anex_1_pla.columns.str.lower()
    data_anex_1_pla

    ## renombre de columnas
    data_anex_1_pla.rename(columns={
        "año": "anio",
        "grupo_edad1": "grupo_edad_1",
        "idprofesional": "id_profesional"
    }, inplace=True)

    ## Asignación de valores categóricos
    from modulo_data.diccionarios import (
        dicc_area_defuncion,
        dicc_estado_civil,
        dicc_sexo,
        dicc_grupo_edad,
        dicc_meses,
        dicc_nivel_educativo,
        dicc_sitio_defuncion
    )

    # Diccionario maestro: columna -> diccionario de reemplazo
    diccionarios = {
        'area_defuncion': dicc_area_defuncion,
        'estado_civil': dicc_estado_civil,
        'sexo': dicc_sexo,
        'grupo_edad_1': dicc_grupo_edad,
        'mes': dicc_meses,
        'nivel_educativo': dicc_nivel_educativo,
        'sitio_defuncion': dicc_sitio_defuncion
    }

    # Aplicación
    for columna, diccionario in diccionarios.items():
        
        data_anex_1_pla[columna] = (
            data_anex_1_pla[columna]
            .map(diccionario)
            .fillna(data_anex_1_pla[columna])
        )

    ## Codigos muerte incompletos
    data_anex_1_pla['cod_muerte'] = data_anex_1_pla['cod_muerte'].astype(str)
    data_anex_1_pla['cod_muerte'] = data_anex_1_pla['cod_muerte'].apply(
        lambda x: x + 'X' if len(x) == 3 else x
    )

    data_anex_1_pla = data_anex_1_pla.drop(columns = ['cod_departamento', 'cod_municipio'])

    ## Data Anexo 2----------------------------------------------------------------
    data_anex_2_pla = data_anexo_2_bronce.copy()

    ## Normalización de nombres de columnas
    data_anex_2_pla.columns = data_anex_2_pla.columns.str.lower()

    ## Eliminación de signos de puntuación
    data_anex_2_pla.columns = [
        unicodedata.normalize('NFKD', col).encode('ascii', errors='ignore').decode('utf-8')
        for col in data_anex_2_pla.columns
    ]

    ## Linea al piso para espacios
    data_anex_2_pla.columns = data_anex_2_pla.columns.str.replace(' ', '_') 
    data_anex_2_pla

    ## Reemplazo de nombres
    data_anex_2_pla.rename(columns={
        "codigo_de_la_cie-10_tres_caracteres": "codigo_cie10_tres_caracteres",
        "descripcion__de_codigos_mortalidad_a_tres_caracteres": "descripcion_codigo_mortalidad_tres_caracteres",
        "codigo_de_la_cie-10_cuatro_caracteres": "cod_muerte",
        "descripcion__de_codigos_mortalidad_a_cuatro_caracteres": "descripcion_codigo_mortalidad_cuatro_caracteres",
    }, inplace=True)

    ## Data Divipola----------------------------------------------------------------
    data_divi_pla = data_divi_bronce.copy()
    data_divi_pla.columns = data_divi_pla.columns.str.lower()

    return data_anex_1_pla, data_anex_2_pla, data_divi_pla
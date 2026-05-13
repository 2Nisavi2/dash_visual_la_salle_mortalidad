## Codigo para al generación de elctura de datos

def cargar_archivos_excel(path_carpeta):
    """
    Verifica la existencia de 3 archivos Excel específicos dentro de una carpeta,
    valida su formato y carga cada uno en un DataFrame.
    Parámetros
    ----------
    path_carpeta : str
        Ruta de la carpeta que contiene los archivos.
    Retorna
    -------
    dict
        Diccionario con los DataFrames cargados.
    """
    import os
    import pandas as pd


    # Archivos esperados
    archivos_esperados = {
        "anexo_1": "anexo_1.xlsx",
        "anexo_2": "anexo_2.xlsx",
        "anexo_3": "divipola.xlsx"
    }
    dataframes = {}

    # Validación de carpeta
    print("--- Verificando existencia de archivos.")
    if not os.path.exists(path_carpeta):
        raise FileNotFoundError(f"La carpeta no existe: {path_carpeta}")

    if not os.path.isdir(path_carpeta):
        raise NotADirectoryError(f"La ruta no es una carpeta válida: {path_carpeta}")
    
    # Validación de archivos
    print("--- Realizando carga y lectura de fuentes.")
    for nombre_df, archivo in archivos_esperados.items():
        ruta_archivo = os.path.join(path_carpeta, archivo)
        # Validar existencia
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(
                f"Falta el archivo requerido: {archivo}"
            )
        # Validar extensión Excel
        extensiones_validas = (".xlsx", ".xls")
        if not archivo.lower().endswith(extensiones_validas):
            raise ValueError(
                f"El archivo {archivo} no es un Excel válido"
            )
        # Cargar DataFrame
        try:
            if nombre_df == "anexo_2":
                dataframes[nombre_df] = pd.read_excel(
                    ruta_archivo,
                    skiprows=8
                )
            else:
                dataframes[nombre_df] = pd.read_excel(
                    ruta_archivo
                )
        except Exception as e:
            raise Exception(
                f"Error al leer el archivo {archivo}: {str(e)}"
            )
    print("--- Todos los archivos fueron validados y cargados correctamente.")
    return dataframes
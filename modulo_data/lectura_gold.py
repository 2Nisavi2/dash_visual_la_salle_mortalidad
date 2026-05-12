def leer_parquet_particionado(ruta_carpeta):
    """
    Lee un dataset parquet particionado desde una carpeta.
    Parámetros
    ----------
    ruta_carpeta : str
        Ruta donde se encuentran los parquet particionados.
    Retorna
    -------
    pandas.DataFrame
    """

    import os
    import pandas as pd
    
    # Validar existencia
    if not os.path.exists(ruta_carpeta):
        raise FileNotFoundError(
            f"La carpeta no existe: {ruta_carpeta}"
        )
    # Validar que sea carpeta
    if not os.path.isdir(ruta_carpeta):
        raise NotADirectoryError(
            f"La ruta no es una carpeta válida: {ruta_carpeta}"
        )
    # Leer parquet particionado
    try:
        df = pd.read_parquet(
            ruta_carpeta,
            engine='pyarrow'
        )
        print(f"""
        Parquet leído correctamente.
        Ruta:
        {ruta_carpeta}
        Filas:
        {df.shape[0]}
        Columnas:
        {df.shape[1]}
        """)
        return df
    except Exception as e:
        raise Exception(
            f"Error al leer parquet: {str(e)}"
        )
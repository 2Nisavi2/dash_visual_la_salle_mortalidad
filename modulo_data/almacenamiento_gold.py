## Función de capa gold
def almacenar_gold(df, ruta_salida):
    """
    Guarda un DataFrame en formato parquet particionado
    por la columna 'departamento'.
    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame a almacenar.
    ruta_salida : str
        Carpeta donde se almacenarán los archivos parquet.
    """
    import os
    import pandas as pd
    # Validar existencia de columna
    print("--- Verificando existencia de columna de despliegue de Parquets.")
    if 'cod_departamento' not in df.columns:
        raise ValueError(
            "La columna 'cod_departamento' no existe en el DataFrame."
        )
    # Crear carpeta si no existe
    os.makedirs(ruta_salida, exist_ok=True)
    # Guardar parquet particionado
    print("--- Generando parquets.")
    df.to_parquet(
        ruta_salida,
        engine='pyarrow',
        partition_cols=['cod_departamento'],
        index=False
    )
    print(f"--- Parquet particionado almacenado en: {ruta_salida}")
def descarga_json_mapa():
    ## Almacenamiento de Json para geometría de departamentos

    import requests
    url = "https://raw.githubusercontent.com/santiblanko/colombia.geojson/master/depto.json"
    response = requests.get(url)
    # Verificar descarga correcta
    if response.status_code != 200:    
        raise Exception(
            f"Error descargando GeoJSON: {response.status_code}"
        )
    # Convertir directamente a JSON
    geojson_colombia = response.json()
    # Carpeta destino
    carpeta_salida = "data/geojson"
    # Crear carpeta si no existe
    os.makedirs(carpeta_salida, exist_ok=True)
    # Ruta archivo
    ruta_archivo = os.path.join(
        carpeta_salida,
        "colombia_departamentos.geojson"
    )
    # Guardar JSON
    with open(
        ruta_archivo,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            geojson_colombia,
            f,
            ensure_ascii=False,
            indent=4
        )
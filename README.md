# dash_visual_la_salle_mortalidad

<p align="center">
    <img src="assets/logo.png" width="700">
</p>

## Introducción
Este repositorio contiene los archivos de desarrollo para el visualizador de mortalidad en Colombia apra el año 2019. Su objetivo es almacenar la data, proceso de ETL y dsepliegue del dashboard resultante. El dshboard final puede ser obervado desde el siguiente [LINK](web-production-a23a.up.railway.app).

## Estructura del proyecto
```bash
📦 dash_visual_la_salle_mortalidad
│
├── 📂 assets
│   ├── logo.png (logo de Universidad para visual y documentación)
│
├── 📂 data
│   ├── 📂 geojson
│       ├── colombia_departamentos.geojson (archivo de geometría departamentos de Colombia)
│   ├── 📂 parquet_gold (contien los datos en capa gold procesados para visualizador)
│       ├── 📂 cod_departamento=5
│       ├── 📂 (...)
│       ├── 📂 cod_departamento=99
│   ├── anexo_1.xlsx (archvio DANE de registros de fallecimeintos)
│   ├── anexo_2.xlsx (archivo DANE de clasificación)
│   └── divipola.xlsx (archivo DANE con registro división politico adminsitrativa de Colombia)
│
├── 📂 modulo_dash
│   ├── graficas.py (Modulo de gráficas a desplegar en dash)
│
├── 📂 modulo_data
│   ├── almacenamiento_gold.py (Modulo para creación de Parquets capa gold)
│   ├── capa_gold.py (Modulo para generación de capa Gold)
│   └── diccionarios.py (Diccionarios apra variables catregóricas según registro DANE)
│   └── json_mapa.py (Procesamiento de Json para mapa división adminsitrativa Colombia)
│   └── lectura_gold.py (Lectura de aprquets capa gold)
│   └── lectura.py (Lectura de archivos capa Bronze)
│   └── tratamiento_data.py (Generación de ETL para dartos a capa silver)
│
├── app.py (Despliegue app de visualizador)
├── explo.ipynb (Notebook documental que muestra el rpocesamiento de ETL y despliegue de visualizador)
├── pre.py (Función que ejecuta todas las funciones de ETL para capa gold)
├── Profile (Condiciones para despliegue en Railway)
├── README.md (Readme de documentación del repositorio)
├── requirements.txt (Lista de requisitos en librerias del repositorio)
└── runtime.txt (Condición de corrida para Railway)

```

## Requisitos
Para el desarrollo de la solución, se deben usar las siguientes librerías. Dicha lisgta se mantiene en almacenamiento en [requitements](requirements.txt):

- dash
- dash-bootstrap-components
- plotly
- pandas
- pyarrow
- gunicorn
- numpy

## Despliegue
Para realizar el almacenamiento en Railway es necesario tener en cuenta:
- Accesos a repostiroio en GitHub
- Acceso al espacio de despliegue en Railway

El proceso de despliegue depende de una serie de archivos de parametros de lectura:
- [Procfile](Procfil): para parametros de lectura del repostirio e impresión del front dentro de la pltaforma.
- [runtime](runtime.txt): para tiempos de lectura y evitar bug de lectura infinita o no lectura por estandar corto de tiempo.

El paso a paso del despliegue:
- Iniciar sesión en Runway con cuenta en GitHub.
- Indicar repositorio de almacenamiento del desarrollo para su despliegue en servidor.

## Software utilizado
- Python: para programación de ETL, Dash y diseño de gráficas con Plotly
- Railway: espacio de despliegue front desde su conexión a repositorio en GitHub.
- GitHub: espacio de almacenamiento de repositorio.

## Instrucción para su uso local.
Existen dos procesos en la tarea de uso de la herramienta localmente.
- Proceso de ejecución de ETL (no obligatoria): consiste en realizar la ejecución del modulo `pre.py` el cual ejecuta als tareas de transformación de las versión bronze del desarrollo. Es importante que los archivos de origen del DANE `anexo_1.xlsx`, `anexo_2.xlsx` y `divipola.xlsx` esten correctamente almacenados en la carpeta `data/`. Al asegurar la integridad de la data, se realiza el proceso de ejecución del modulo. Desde la terminal ejecutar `python pre.py` el cual aplicará la ejecución del modulo y mostrará el estado del paso a paso de ejecuión. El resultado será la cpa gold en formato parquet almacenada en `data/parquet_gold/`.
- Proceso de ejecución de la aplicación: nuevamente en terminal ejecutar la función `python/app.py`. El proceso dentro de la terminal quedara en ejecución, por lo que solo deberá utilizar la URL al servido `http://127.0.0.1:8050/`.

**IMPORTANTE**: asegurece de haber isntalado las librerias incluidas en [requitements](requirements.txt)
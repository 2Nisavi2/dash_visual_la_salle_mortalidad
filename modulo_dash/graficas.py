def mapa_muertes(data_gold):
    """
    Genera el mapa de muertes
    por departamento.
    ----------
    df : pandas.DataFrame
        DataFrame a leer.
    salida : plot del mapa.
    """
    ## Generación de consulta---------------------------------------------------------
    ## Filtro año 2019
    data_map = data_gold[data_gold['anio'] == 2019]

    ## Agrupación por departamento
    data_dep = data_map.groupby(['departamento', 'cod_departamento']).size().reset_index(name='conteo_muertes')
    data_dep = data_dep[data_dep['conteo_muertes'] > 0]
    data_dep['cod_departamento'] = data_dep['cod_departamento'].astype(str)

    for i in data_dep.index:
        cod = data_dep.loc[i, 'cod_departamento']
        if len(cod) < 2:
            data_dep.loc[i, 'cod_departamento'] = f"0{data_dep.loc[i, 'cod_departamento']}"

    ## Generación de Mapa-------------------------------------------------------------

    import json

    with open(
        "data/geojson/colombia_departamentos.geojson",
        "r",
        encoding="utf-8"
    ) as f:

        geojson_colombia = json.load(f)

    import plotly.express as px
    fig = px.choropleth(
        data_dep,
        geojson=geojson_colombia,
        locations='cod_departamento',
        color='conteo_muertes',
        color_continuous_scale="Reds",
        featureidkey="properties.DPTO",
        projection="mercator",
        title="Conteo de muertes por departamento en 2019"
    )
    fig.update_geos(
        fitbounds="locations",
        visible=False
    )
    fig.update_layout(
        title='Mapa de calor por departamentos - Colombia',
        margin={"r":0,"t":50,"l":0,"b":0},
        height=700
    )
    return fig

def lineas_mes(data_gold):
    """
    Genera el gráfico de lineas
    de muertes por mes.
    ----------
    df : pandas.DataFrame
        DataFrame a leer.
    salida : plot del gráfico.
    """
    ## Generación de consulta---------------------------------------------------------
    import pandas as pd
    ## Filtro año 2019
    data_line = data_gold[data_gold['anio'] == 2019]

    ## Agrupación por departamento
    data_mes = data_line.groupby(['mes']).size().reset_index(name='conteo_muertes')
    # Ordenamiento de meses
    orden_meses = [
        'Enero',
        'Febrero',
        'Marzo',
        'Abril',
        'Mayo',
        'Junio',
        'Julio',
        'Agosto',
        'Septiembre',
        'Octubre',
        'Noviembre',
        'Diciembre'
    ]
    data_mes['mes'] = pd.Categorical(
        data_mes['mes'],
        categories=orden_meses,
        ordered=True
    )
    data_mes = data_mes.sort_values('mes').reset_index(drop=True)

    ## Generación de gráfica de líneas-------------------------------------------------
    import plotly.express as px
    fig = px.line(
        data_mes,
        x='mes',
        y='conteo_muertes',
        markers=True,
        title='Conteo de muertes por mes',
    )

    fig.update_layout(
        xaxis_title='Mes',
        yaxis_title='Conteo de muertes',
        height=600,
        hovermode='x unified',
        template='plotly_white'
    )

    return fig

def barras_homicidios(data_gold):
    """
    Genera el gráfico de barras
    de ciudades con más homicidios.
    ----------
    df : pandas.DataFrame
        DataFrame a leer.
    salida : plot del gráfico.
    """
    ## Generación de consulta---------------------------------------------------------
    import pandas as pd
    ## Filtro año 2019
    data_bar = data_gold[data_gold['anio'] == 2019]
    data_bar = data_bar[data_bar['codigo_cie10_tres_caracteres'] == 'X95']
    data_bar = data_bar.groupby(['municipio']).size().reset_index(name='conteo_muertes')
    data_bar = data_bar.sort_values('conteo_muertes', ascending=False).reset_index(drop=True)
    data_bar = data_bar.head(5)
    data_bar

    ## Generación de gráfica de barras-------------------------------------------------
    import plotly.express as px
    fig = px.bar(
        data_bar,
        x='municipio',
        y='conteo_muertes',
        title='Top 5 municipios con más muertes por X95 en 2019',
        color='conteo_muertes',
        color_continuous_scale='Reds'
    )
    fig.update_layout(
        xaxis_title='Municipio',
        yaxis_title='Conteo de muertes',
        height=600,
        hovermode='x unified',
        template='plotly_white'
    )
    return fig

def indice_muerte (data_gold):
    """
    Genera el gráfico circular
    de minucipios con menos cantidad de homicidios
    ----------
    df : pandas.DataFrame
        DataFrame a leer.
    salida : plot del gráfico.
    """
    ## Generación de consulta---------------------------------------------------------
    import plotly.express as px
    ## Filtro año 2019
    data_cir = data_gold[data_gold['anio'] == 2019]

    ## Agrupación por departamento
    data_cir = data_cir.groupby(['municipio']).size().reset_index(name='conteo_muertes')
    data_cir = data_cir.sort_values('conteo_muertes', ascending=True).reset_index(drop=True)
    data_cir = data_cir.head(10)
    data_cir

    ## Generación de gráfico
    fig = px.pie(
        data_cir,
        names='municipio',
        values='conteo_muertes',
        title='Distribución de mortalidad por municipios',
        hole=0.3   # Donut chart
    )

    fig.update_traces(
        textposition='inside',
        textinfo='percent+label'
    )
    fig.update_layout(
        height=700,
        template='plotly_white'
    )

    return fig

def causas_muerte(data_gold):
    """
    Genera tabla de motivos
    de muerte.
    ----------
    df : pandas.DataFrame
        DataFrame a leer.
    salida : plot tabla.
    """
    import plotly.graph_objects as go

    ## Generación de consulta---------------------------------------------------------
    ## Filtro año 2019
    data_cau = data_gold[data_gold['anio'] == 2019]

    ## Agrupación por departamento
    data_cau = data_cau.groupby(['manera_muerte']).size().reset_index(name='conteo_muertes')
    data_cau = data_cau.sort_values('conteo_muertes', ascending=False).reset_index(drop=True)
    data_cau

    ## Generación tabla resumen causas de muerte -------------------------------------
    fig = go.Figure(data=[go.Table(
        # Encabezados
        header=dict(
            values=list(data_cau.columns),
            fill_color='lightgrey',
            align='center'
        ),
        # Contenido
        cells=dict(
            values=[data_cau[col] for col in data_cau.columns],
            align='center'
        )
    )])

    fig.update_layout(
        title='Tabla de Conteo de Muertes',
        height=400
    )

    return fig

def generos(data_gold):
    """
    Genera gráfico de columnas apiladas
    de muertes por genero.
    ----------
    df : pandas.DataFrame
        DataFrame a leer.
    salida : plot de gráfica.
    """
    import plotly.express as px

    ## Generación de consulta---------------------------------------------------------
    ## Filtro año 2019
    data_gen = data_gold[data_gold['anio'] == 2019]

    ## Agrupación por departamento
    data_gen = data_gen.groupby(['sexo', 'departamento']).size().reset_index(name='conteo_muertes')
    data_gen = data_gen.sort_values(['departamento', 'sexo','conteo_muertes'], ascending=False).reset_index(drop=True)

    ## Generación de Gráfica----------------------------------------------------------
    fig = px.bar(
        data_gen,
        x='departamento',
        y='conteo_muertes',
        color='sexo',
        barmode='stack',
        title='Conteo de muertes por departamento y sexo'
    )

    fig.update_layout(
        xaxis_title='Departamento',
        yaxis_title='Conteo de muertes',
        height=600,
        template='plotly_white'
    )

    return fig

def hist_mortalidad(data_gold):
    """
    Generahistograma de eventos de muerte
    por etapas de vida del DANE.
    ----------
    df : pandas.DataFrame
        DataFrame a leer.
    salida : plot de gráfica.
    """
    import plotly.express as px

    ## Generación de consulta---------------------------------------------------------
    ## Filtro año 2019
    data_dis = data_gold[data_gold['anio'] == 2019]

    from modulo_data.diccionarios import dicc_grupo_edad_categoria
    ## Clasificación de edades
    data_dis['categoria_grupo_edad'] = (
        data_dis['grupo_edad_1']
        .map(dicc_grupo_edad_categoria)
    )

    ## Data factory de categorias
    orden_categorias = [
        'Mortalidad neonatal (Menor de 1 mes)',
        'Mortalidad infantil (1 a 11 meses)',
        'Primera infancia (1 a 4 años)',
        'Niñez (5 a 14 años)',
        'Adolescencia (15 a 19 años)',
        'Juventud (20 a 29 años)',
        'Adultez temprana (30 a 44 años)',
        'Adultez intermedia (45 a 59 años)',
        'Vejez (60 a 84 años)',
        'Longevidad / Centenarios (85 a 100+ años)',
        'Edad desconocida (Sin información)'
    ]

    ## Generación de distribuciones-------------------------------------------------
    import plotly.figure_factory as ff

    # Lista categorías
    categorias = (
        data_dis['categoria_grupo_edad']
        .unique()
    )

    # Contenedores
    hist_data = []

    group_labels = []

    # Variable numérica continua
    # Reemplazar 'edad' por la columna real de edad
    for categoria in categorias:
        datos = data_dis.loc[
            data_dis['categoria_grupo_edad'] == categoria,
            'grupo_edad_1'
        ].dropna()
        # Validar existencia de datos
        if len(datos) > 0:
            hist_data.append(datos)
            group_labels.append(categoria)
    fig = px.histogram(
        data_dis,
        x='categoria_grupo_edad',
        color='categoria_grupo_edad',
        category_orders={
            'categoria_grupo_edad': orden_categorias
        }
    )
    fig.update_layout(
        title='Distribución de probabilidad por grupos de edad - 2019',
        xaxis_title='Edad',
        yaxis_title='Densidad',
        height=700,
        template='plotly_white'
    )
    return fig
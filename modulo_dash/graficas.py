def mapa_muertes(data_gold):
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

def causas_muerte(data_gold):
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
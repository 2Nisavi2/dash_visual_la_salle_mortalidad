from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

from modulo_data.lectura_gold import leer_parquet_particionado
from modulo_dash import graficas

# CARGA DE DATOS
df = leer_parquet_particionado("data/parquet_gold")

# GENERACIÓN DE GRÁFICAS
fig1 = graficas.mapa_muertes(df)
fig2 = graficas.lineas_mes(df)
fig3 = graficas.barras_homicidios(df)
fig4 = graficas.indice_muerte(df)
fig5 = graficas.causas_muerte(df)
fig6 = graficas.generos(df)
fig7 = graficas.hist_mortalidad(df)

# APP
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
app.title = "Dashboard Muertes Colombia"

# LAYOUT
app.layout = dbc.Container(
    [
        # ENCABEZADO
        html.Div(
            [
                html.Img(
                    src="/assets/logo.png",
                    style={
                        "width": "180px",
                        "display": "block",
                        "margin": "auto"
                    }
                ),
                html.H1(
                    "Análisis de Fallecimientos en Colombia 2019",
                    style={
                        "textAlign": "center",
                        "marginTop": "20px"
                    }
                ),
                html.P(
                    """
                    Maestría en Inteligencia Artificial
                    """,
                    style={
                        "textAlign": "center",
                        "fontSize": "18px",
                        "marginBottom": "5px"
                    }
                ),
                html.P(
                    """
                    Aplicaciones I
                    """,
                    style={
                        "textAlign": "center",
                        "fontSize": "18px",
                        "marginBottom": "5px"
                    }
                ),
                html.P(
                    """
                    Desarrollado por: Diego Nicolás Ávila Moreno
                    """,
                    style={
                        "textAlign": "center",
                        "fontSize": "18px",
                        "marginBottom": "5px"
                    }
                )
            ]
        ),

        # GRÁFICAS
        dbc.Row(
            [
                # COLUMNA IZQUIERDA
                dbc.Col(
                    [
                        dcc.Graph(figure=fig1),
                        dcc.Graph(figure=fig3),
                        dcc.Graph(figure=fig5),
                        dcc.Graph(figure=fig7)
                    ],
                    width=6
                ),

                # COLUMNA DERECHA
                dbc.Col(
                    [
                        dcc.Graph(figure=fig2),
                        dcc.Graph(figure=fig4),
                        dcc.Graph(figure=fig6)
                    ],
                    width=6
                )
            ]
        )
    ],
    fluid=True
)


# MAIN
server = app.server
import os
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8050)),
        debug=False
    )
import dash
from dash import html, dcc, callback, Output, Input
import pandas as pd
from my_app.plot_grafieken import plot_map
import plotly
import plotly.express as px
import dash_bootstrap_components as dbc
import requests
from requests_file import FileAdapter


#This tells Dash that this is a page
dash.register_page(__name__)

#layout = ""
# Create layout of the page
fig_map, regios_options, vacatures_regio_df = plot_map()

# Load GeoJSON file
s = requests.Session()
s.mount('file://', FileAdapter())

provincies = s.get('file:///C:/Users/Student/OneDrive/Bureaublad/python/data/provincies.json')
provinciesDataRaw = provincies.json()
provinciesData = provinciesDataRaw["features"]

#App layout
layout = html.Div(children=[
    html.Div([
    html.H1(children="Map Regions"),

    # Dropdown for regions
    dcc.Dropdown(
        id="regions-vacatures-options",
        options=regios_options,
        value=regios_options[0]["value"] #Set initial value
    ),

    # Graph to display initial map of vacatures per region
    dcc.Graph(
        id="regions-vacatures-map",
        figure=fig_map
    )
    ])
])

#Add controls to build the interaction
@callback(
        Output("regions-vacatures-map", "figure"),
        [Input("regions-vacatures-options", "value")]
)
def update_map(region_chosen):
    fig_map = px.choropleth_mapbox(vacatures_regio_df, geojson=provinciesDataRaw, locations='Regios', color='OpenstaandeVacatures', featureidkey="id",
                           color_continuous_scale="Viridis",
                           range_color=(0, 2),
                           mapbox_style="open-street-map",
                           zoom=6, center = {"lat": 52.14898973341009, "lon": 5.571005662096867},
                           opacity=0.5,
                           labels={'OpenstaandeVacatures':'Openstaande Vacatures'}
                          )
    return fig_map
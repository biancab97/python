import dash
from dash import html, dcc, callback, Output, Input
import pandas as pd
from my_app.plot_grafieken import plot_map
import plotly.express as px


#This tells Dash that this is a page
dash.register_page(__name__)

#layout = ""
# Create layout of the page
fig_map, regios_options, vacatures_regio_df = plot_map()



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
#@callback(
#        Output("regions-vacatures-map", "figure"),
#        [Input("regions-vacatures-options", "value")]
#)
#def update_map(region_chosen):
#    fig = px.choropleth(
#        data_frame= '',
#        locationmode='',
#        locations='',
#        scope='',
#        color='',
#        hover_data='',
#        color_continuous_scale=px.colors.sequential.YlOrRd,
#        labels={''},
#        template='plotly_dark'
#        )
#    pass
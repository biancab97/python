import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
from my_app.plot_grafieken import plot_table2
from my_app.datauitlezen import vacatures_regio_uitlezen

#This tells Dash that this is a page
dash.register_page(__name__)

#vacatures_regio_df - plot_table2()

#Inititialize the app
#app = Dash(__name__)

#App layout
layout = html.Div([
    
    dcc.Dropdown(),
    #dash_table.DataTable(data=vacatures_regio_df.to_dict('records'), page_size=10),
    dcc.Graph(figure={}, id='controls-and-graph2')
])

#Add controls to build the interaction
@callback(
        Output(component_id='controls-and-graph2', component_property='figure'),
        Input(component_id='controls-and-radio-item2', component_property='value')
)
def update_graph(col_chosen):
    fig = px.choropleth(
        data_frame= '',
        locationmode='',
        locations='',
        scope='',
        color='',
        hover_data='',
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={''},
        template='plotly_dark'
        )
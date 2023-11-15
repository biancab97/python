import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
from my_app.plot_grafieken import plot_table
from my_app.datauitlezen import vacatures_uitlezen

#This tells Dash that this is a page
dash.register_page(__name__)

vacatures_df = plot_table()

#App layout
layout = html.Div([

    dcc.Dropdown(),
    #dash_table.DataTable(data=vacatures_df.to_dict('records'), page_size=10),
    dcc.Graph(figure={}, id='controls-and-graph')
])

#Add controls to build the interaction
@callback(
        Output(component_id='controls-and-graph', component_property='figure'),
        Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(vacatures_df, x='Perioden', y=col_chosen, histfunc='avg')
import dash
from dash import html, dcc, callback, Output, Input
from my_app.plot_grafieken import plot_bargraph
import plotly.express as px


#This tells Dash that this is a page
dash.register_page(__name__)

# Define layout of the page
fig, sectoren_options, vacatures_df = plot_bargraph()

#App layout
layout = html.Div(children=[
    html.Div([
    html.H1(children="Bar Graph Sectoren"),

    # Dropdown for sectors
    dcc.Dropdown(
        id="sector-vacatures-options",
        options=sectoren_options,
        value=sectoren_options[0]["value"] #Set an initial value
    ),

    # Graph to display vacatures per sector
    dcc.Graph(
        id="sector-vacatures-graph",
        figure= fig
    )
    ])
])

#Add controls to build the interaction
@callback(
        Output('sector-vacatures-graph', 'figure'),
        [Input('sector-vacatures-options', 'value')]
)
def update_graph(sector_chosen):
    # Filter dataframe based on sector chosen
    filtered_df = vacatures_df[(vacatures_df["Bedrijfskenmerken"] == sector_chosen)]

    # Create a new line graph based on sector chosen
    fig = px.bar(filtered_df, x="Perioden", y="OpenstaandeVacatures_1", title="Openstaande Vacatures Per Sector")
    return fig
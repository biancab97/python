import dash
from dash import html, dcc, callback, Output, Input
from my_app.plot_grafieken import plot_bargraph
import plotly.express as px
from dash import dash_table
import dash_bootstrap_components as dbc

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
    ]),

    html.Div([
        html.H1(children="Tabel Sectoren"),
        # Dropdown for sectors
        dcc.Dropdown(
            id="tabel-vacatures-options",
            options=sectoren_options,
            value=sectoren_options[0]["value"]
        ),
        
        #Define table
        dash_table.DataTable(
                            id='sectoren-tabel',
                            columns=[
                                {'name': 'Openstaande Vacatures', 'id': 'OpenstaandeVacatures_1'},
                                {'name': 'Ontstane Vacatures', 'id': 'OntstaneVacatures_2'},
                                {'name': 'Vervulde Vacatures', 'id': 'VervuldeVacatures_3'},
                                {'name': 'Perioden', 'id': 'Perioden'},
                                {'name': 'Jaar', 'id': 'Jaar'}
                            ],
                        )
                    ]),
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

#Add controls to build the interaction
@callback(
        Output('sectoren-tabel', 'data'),
        [Input('tabel-vacatures-options', 'value')]
)

def update_table(sector_chosen):
    filtered_df_tabel = vacatures_df[(vacatures_df["Bedrijfskenmerken"] == sector_chosen)]
    filtered_tabel = filtered_df_tabel.to_dict('records')
    return filtered_tabel
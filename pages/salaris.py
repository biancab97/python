import dash
from dash import html, dcc, callback, Output, Input
from my_app.plot_graph import plot_barchart_leeftijd, plot_barchart_geslacht, plot_line_graph, plot_barchart_werkuren
import dash_bootstrap_components as dbc
import plotly.express as px


# This tells Dash that this is a page in my app
dash.register_page(__name__)


# Define the layout of the page
fig_leeftijd, work_branch_options_leeftijd, df_salaris_leeftijd = plot_barchart_leeftijd()
fig_geslacht, work_branch_options_geslacht, df_salaris_geslacht = plot_barchart_geslacht()
fig, work_branch_options, df_salaris = plot_line_graph()
fig_werkuren, work_branch_options_werkuren, df_werkuren = plot_barchart_werkuren()


layout = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.Div([
                    html.H3(id='tekst_salaris', children='Maandloon per sector'),

                    # Dropdown for work branches
                    dcc.Dropdown(
                        id='salaris-work-branch-dropdown',
                        options=work_branch_options,
                        value=work_branch_options[0]['value']  # Set an initial value
                    ),

                    # Graph to display salaris data
                    dcc.Graph(
                        id='salaris-example-graph',
                        figure=fig,
                    ),
                ]),
            )
        ),

        dbc.Row(
            [
                dbc.Col(
                    html.Div([
                       html.H3(id='tekst_geslacht', children='Salaris Mannen en Vrouwen'),

                        # Dropdown for work branches
                        dcc.Dropdown(
                            id='salaris-work-branch-dropdown-geslacht',
                            options=work_branch_options_geslacht,
                            value=work_branch_options_geslacht[0]['value'],  # Set an initial value
                        ),

                        # Graph to display salaris geslacht data
                        dcc.Graph(
                            id='geslacht-example-graph',
                            figure=fig_geslacht,
                        ),
                    ]),
                ),
                dbc.Col(
                    html.Div([
                        html.H3(id='tekst_werkuren', children='aantal werkuren per week voor Mannen en Vrouwen'),

                        # Dropdown for work branches
                        dcc.Dropdown(
                            id='werkuren-work-branch-dropdown',
                            options=work_branch_options_werkuren,
                            value=work_branch_options_werkuren[0]['value'],  # Set an initial value
                        ),

                        # Graph to display salaris leeftijd data
                        dcc.Graph(
                            id='werkuren-example-graph',
                            figure=fig_werkuren,
                        ),
                    ]),
                ),
                dbc.Col(
                    html.Div([
                        html.H3(id='tekst_leeftijd', children='Salaris verschillende leeftijden'),

                        # Dropdown for work branches
                        dcc.Dropdown(
                            id='salaris-work-branch-dropdown-leeftijd',
                            options=work_branch_options_leeftijd,
                            value=work_branch_options_leeftijd[0]['value'],  # Set an initial value
                        ),

                        # Graph to display salaris leeftijd data
                        dcc.Graph(
                            id='leeftijden-example-graph',
                            figure=fig_leeftijd,
                        ),
                    ]),
                ),
            ],
        ),
    ]
)
    

@callback(
    Output('salaris-example-graph', 'figure'),
    [Input('salaris-work-branch-dropdown', 'value')]
)
def update_graph(selected_branch):
    '''
    Update the bar graph based on the selected work branch.

    Parameters:
    - selected_branch (str): The selected work branch.

    Returns:
    - fig (plotly.graph_objs.Figure): The updated bar graph.
    '''
    # Filter the data based on the selected work branch
    filtered_df = df_salaris[(df_salaris['BedrijfstakkenBranchesSBI2008'] == selected_branch)]
    
    # Create a new bar graph with the filtered data
    fig = px.line(filtered_df, x='Perioden', y='MaandloonExclusiefOverwerk_6', labels={'MaandloonExclusiefOverwerk_6': 'Maandloon'})
    
    return fig

@callback(
    Output('geslacht-example-graph', 'figure'),
    [Input('salaris-work-branch-dropdown-geslacht', 'value')]
)
def update_graph_geslacht(selected_branch):
    # Filter the data based on the selected work branch
    filtered_df = df_salaris_geslacht[(df_salaris_geslacht['BedrijfstakkenBranchesSBI2008'] == selected_branch)]
    
    # Get unique values for the "KenmerkenBaan" column
    df_salaris_geslacht['KenmerkenBaan'] = df_salaris_geslacht['KenmerkenBaan'].astype(str)
    
    # Calculate the average salary for each year and gender
    average_salary_per_year_gender = filtered_df.groupby(['Jaar', 'KenmerkenBaan'])['MaandloonExclusiefOverwerk_6'].mean().reset_index()

    # Create a bar chart for each 'Jaar' with the average salary split by gender
    fig_geslacht = px.bar(average_salary_per_year_gender, x="Jaar", y="MaandloonExclusiefOverwerk_6", color="KenmerkenBaan",
                 barmode='group', labels={'MaandloonExclusiefOverwerk_6': 'Gemiddeld Maandloon'})
    
    return fig_geslacht

# Define a callback function to update the graph when the dropdown selection changes
@callback(
    Output('leeftijden-example-graph', 'figure'),
    [Input('salaris-work-branch-dropdown-leeftijd', 'value')]
)

def update_graph_leeftijd(selected_branch):
    # Filter the data based on the selected work branch
    filtered_df = df_salaris_leeftijd[(df_salaris_leeftijd['BedrijfstakkenBranchesSBI2008'] == selected_branch)]
    
    # Get unique values for the "KenmerkenBaan" column
    df_salaris_leeftijd['KenmerkenBaan'] = df_salaris_leeftijd['KenmerkenBaan'].astype(str)
        
    # Calculate the average salary for each year and gender
    average_salary_per_year_leeftijd = filtered_df.groupby(['Jaar', 'KenmerkenBaan'])['MaandloonExclusiefOverwerk_6'].mean().reset_index()

    # Create a bar chart for each 'Jaar' with the average salary split by gender
    fig_leeftijd = px.bar(average_salary_per_year_leeftijd, x="Jaar", y="MaandloonExclusiefOverwerk_6", color="KenmerkenBaan",
                 barmode='group', labels={'MaandloonExclusiefOverwerk_6': 'Gemiddeld Maandloon'})
    
    return fig_leeftijd


@callback(
    Output('werkuren-example-graph', 'figure'),
    [Input('werkuren-work-branch-dropdown', 'value')]
)
def update_graph_werkuren(selected_branch):

    # Filter the data based on the selected work branch
    filtered_df_werkuren = df_werkuren[(df_werkuren['BedrijfstakkenBranchesSBI2008'] == selected_branch)]
    
    # Create a bar chart for each 'Jaar' with the average salary split by gender
    fig_werkuren = px.bar(filtered_df_werkuren, x="Perioden", y="PerBaanPerWeekExclusiefOverwerk_11", color="KenmerkenBaanWerknemerBedrijf",
                 barmode='group', labels={'PerBaanPerWeekExclusiefOverwerk_11': 'gemiddeld aantal werkuren per week', 'KenmerkenBaanWerknemerBedrijf' : 'kenmerk'})
    
    fig_werkuren.update_layout(yaxis=dict(categoryorder='total ascending'))

    return fig_werkuren

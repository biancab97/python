import dash
from dash import html, dcc, callback, Output, Input
from my_app.plot_graph import plot_barchart_leeftijd, plot_barchart_geslacht, plot_line_graph, werkuren, werkuren_leeftijd
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import dash_table


# This tells Dash that this is a page in my app
dash.register_page(__name__)


# Define the layout of the page
fig_leeftijd, work_branch_options_leeftijd, df_salaris_leeftijd = plot_barchart_leeftijd()
fig_geslacht, work_branch_options_geslacht, df_salaris_geslacht = plot_barchart_geslacht()
fig_salaris, work_branch_options, df_salaris = plot_line_graph()
work_branch_options_werkuren, df_werkuren = werkuren()
work_branch_options_werkuren_leeftijd, df_werkuren_leeftijd = werkuren_leeftijd()

layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.Div([
                    html.H4(id='tekst_salaris', children='Maandloon per sector'),

                    # Dropdown for work branches
                    dcc.Dropdown(
                        id='salaris-work-branch-dropdown',
                        options=work_branch_options,
                        value=work_branch_options[0]['value']  # Set an initial value
                    ),

                    # Graph to display salaris data
                    dcc.Graph(
                        id='salaris-example-graph',
                        figure=fig_salaris,
                        
                    ),
                ]),
                width=12,
            )
        ),

    dbc.Row(
            [
                dbc.Col(
                    html.Div([
                       html.H4(id='tekst_geslacht', children='Salaris Mannen en Vrouwen'),
                        # Graph to display salaris geslacht data
                        dcc.Graph(
                            id='geslacht-example-graph',
                            figure=fig_geslacht,
                            
                        ),
                    ]),
                    width=6,
                ),
                dbc.Col(
                    html.Div([
                        html.H4(id='tekst_werkuren', children='aantal werkuren per week voor Mannen en Vrouwen'),
                        dcc.Dropdown(
                        id='werkuren-work-branch-dropdown',
                        options=work_branch_options_werkuren,
                        value=work_branch_options_werkuren[0]['value']  # Set an initial value
                    ),
                        # Table to display salaris leeftijd data
                         dash_table.DataTable(
                            id='work-hours-table',
                            columns=[
                            {'name': 'Jaar', 'id': 'Jaar'},
                            {'name': 'Aantal uur per week', 'id': 'PerBaanPerWeekExclusiefOverwerk_11'},
                            {'name': 'Geslacht', 'id': 'KenmerkenBaanWerknemerBedrijf'},
                        ],
                        )
                    ]),
                    width=6,
                ),
            dbc.Row(
            [
                dbc.Col(
                    html.Div([
                        html.H4(id='tekst_leeftijd', children='Salaris verschillende leeftijden'),
                        # Graph to display salaris leeftijd data
                        dcc.Graph(
                            id='leeftijden-example-graph',
                            figure=fig_leeftijd,
                        ),
                    ]),
                    width=8,
                ),
                 dbc.Col(
                    html.Div([
                        html.H4(id='tekst_werkuren_leeftijd', children='aantal werkuren per week voor Mannen en Vrouwen'),
                        # Table to display salaris leeftijd data
                         dash_table.DataTable(
                            style_header={
                            'backgroundColor': 'lightgrey',
                            'color': 'black',
                            },
                            style_data={
                            'backgroundColor': 'grey',
                            'color': 'black'
                            },
                            id='work-hours-table-leeftijd',
                            columns=[
                            {'name': 'Jaar', 'id': 'Jaar'},
                            {'name': 'Aantal uur per week', 'id': 'PerBaanPerWeekExclusiefOverwerk_11'},
                            {'name': 'leeftijd', 'id': 'KenmerkenBaanWerknemerBedrijf'},
                            
                        ],
                        )
                    ]),
                    width=4,
                 )    
            ],
        ),
    ]
)
    ])

@callback(
    [Output('salaris-example-graph', 'figure'),
     Output('geslacht-example-graph', 'figure'),
     Output('leeftijden-example-graph', 'figure'),],
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
    filtered_df_geslacht = df_salaris_geslacht[(df_salaris_geslacht['BedrijfstakkenBranchesSBI2008'] == selected_branch)]
    filtered_df_leeftijd = df_salaris_leeftijd[(df_salaris_leeftijd['BedrijfstakkenBranchesSBI2008'] == selected_branch)]
    
    # Get unique values for the "KenmerkenBaan" column
    df_salaris_geslacht['KenmerkenBaan'] = df_salaris_geslacht['KenmerkenBaan'].astype(str)
    df_salaris_leeftijd['KenmerkenBaan'] = df_salaris_leeftijd['KenmerkenBaan'].astype(str)
    
    # Calculate the average salary for each year and gender
    average_salary_per_year_gender = filtered_df_geslacht.groupby(['Jaar', 'KenmerkenBaan'])['MaandloonExclusiefOverwerk_6'].mean().reset_index()
    average_salary_per_year_leeftijd = filtered_df_leeftijd.groupby(['Jaar', 'KenmerkenBaan'])['MaandloonExclusiefOverwerk_6'].mean().reset_index()
    
    # Create new bar graphs with the filtered data
    fig_salaris = px.line(filtered_df, x='Perioden', y='MaandloonExclusiefOverwerk_6', labels={'MaandloonExclusiefOverwerk_6': 'Maandloon'})
    fig_geslacht = px.bar(average_salary_per_year_gender, x="Jaar", y="MaandloonExclusiefOverwerk_6", color="KenmerkenBaan",
                          barmode='group', labels={'MaandloonExclusiefOverwerk_6': 'Gemiddeld Maandloon'})
    fig_leeftijd = px.bar(average_salary_per_year_leeftijd, x="Jaar", y="MaandloonExclusiefOverwerk_6", color="KenmerkenBaan",
                          barmode='group', labels={'MaandloonExclusiefOverwerk_6': 'Gemiddeld Maandloon'})
        
    # Update colors for graphs
    fig_salaris.update_layout(template="plotly_dark")
    fig_salaris.update_xaxes(gridcolor="black")
    fig_leeftijd.update_layout(template="plotly_white")
    fig_geslacht.update_layout(template="simple_white")  
    
    return fig_salaris, fig_geslacht, fig_leeftijd

@callback(
    [Output('work-hours-table', 'data'),
     Output('work-hours-table-leeftijd', 'data'),],
    [Input('werkuren-work-branch-dropdown', 'value')]
)
def update_graph(selected_branch):
    filtered_data_table_geslacht = df_werkuren[(df_werkuren['BedrijfstakkenBranchesSBI2008'] == selected_branch)]
    filtered_data_table_leeftijd = df_werkuren_leeftijd[(df_werkuren_leeftijd['BedrijfstakkenBranchesSBI2008'] == selected_branch)]
    
    # Convert the DataFrames to dictionaries for the tables with the filtered data
    data_dict_table_geslacht = filtered_data_table_geslacht.to_dict('records')
    data_dict_table_leeftijd = filtered_data_table_leeftijd.to_dict('records')

    return data_dict_table_geslacht, data_dict_table_leeftijd
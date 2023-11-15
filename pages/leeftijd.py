import dash
from dash import html, dcc, callback, Output, Input
from my_app.plot_graph import plot_barchart_leeftijd, plot_barchart_geslacht, plot_barchart
import plotly.express as px


# This tells Dash that this is a page in my app
dash.register_page(__name__)


# Define the layout of the page
fig_leeftijd, work_branch_options_leeftijd, df_salaris_leeftijd = plot_barchart_leeftijd()
fig_geslacht, work_branch_options_geslacht, df_salaris_geslacht = plot_barchart_geslacht()
fig, work_branch_options, df_salaris = plot_barchart()

layout = html.Div(children=[
    html.Div([
    html.H1(children='Bar Chart Branches'),
    
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

    html.Div([
        html.H1(children = 'Bar Chart Mannen en Vrouwen'),
    
        # Dropdown for work branches
        dcc.Dropdown(
            id = 'salaris-work-branch-dropdown-geslacht',
            options = work_branch_options_geslacht,
            value = work_branch_options_geslacht[0]['value'],  # Set an initial value
            
        ),

        # Graph to display salaris geslacht data
        dcc.Graph(
            id = 'kenmerken-example-graph',
            figure = fig_geslacht,
            
        ),
    ]),
        html.Div([
        html.H1(children='Bar Chart verschillende leeftijden'),
    
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
])

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
    fig = px.bar(filtered_df, x='Perioden', y='MaandloonExclusiefOverwerk_6', title='Maandloon per sector', labels={'MaandloonExclusiefOverwerk_6': 'Maandloon'})
    
    return fig

@callback(
    Output('kenmerken-example-graph', 'figure'),
    [Input('salaris-work-branch-dropdown-geslacht', 'value')]
)
def update_graph_geslacht(selected_branch):
    '''
    Update the bar graph based on the selected work branch.

    Parameters:
    - selected_branch (str): The selected work branch.

    Returns:
    - fig (plotly.graph_objs.Figure): The updated bar graph.
    '''
    # Filter the data based on the selected work branch
    filtered_df = df_salaris_geslacht[(df_salaris_geslacht['BedrijfstakkenBranchesSBI2008'] == selected_branch)]
    
    # Get unique values for the "KenmerkenBaan" column
    #print(df_salaris_leeftijd['KenmerkenBaan'].unique().dtype)
    df_salaris_geslacht['KenmerkenBaan'] = df_salaris_geslacht['KenmerkenBaan'].astype(str)
    
    # Create a new bar graph with the filtered data
    # fig = px.bar(filtered_df, x="Jaar", y="MaandloonExclusiefOverwerk_6", color="KenmerkenBaan", barmode='group', category_orders={'Year': [2022]}, labels={'MaandloonExclusiefOverwerk_6': 'Maandloon'})
    
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
    '''
    Update the bar graph based on the selected work branch.

    Parameters:
    - selected_branch (str): The selected work branch.

    Returns:
    - fig (plotly.graph_objs.Figure): The updated bar graph.
    '''
    # Filter the data based on the selected work branch
    filtered_df = df_salaris_leeftijd[(df_salaris_leeftijd['BedrijfstakkenBranchesSBI2008'] == selected_branch)]
    
    # Get unique values for the "KenmerkenBaan" column
    #print(df_salaris_leeftijd['KenmerkenBaan'].unique().dtype)
    df_salaris_leeftijd['KenmerkenBaan'] = df_salaris_leeftijd['KenmerkenBaan'].astype(str)
    
    # Create a new bar graph with the filtered data
    # fig = px.bar(filtered_df, x="Jaar", y="MaandloonExclusiefOverwerk_6", color="KenmerkenBaan", barmode='group', category_orders={'Year': [2022]}, labels={'MaandloonExclusiefOverwerk_6': 'Maandloon'})
    
    # Calculate the average salary for each year and gender
    average_salary_per_year_leeftijd = filtered_df.groupby(['Jaar', 'KenmerkenBaan'])['MaandloonExclusiefOverwerk_6'].mean().reset_index()

    # Create a bar chart for each 'Jaar' with the average salary split by gender
    fig_leeftijd = px.bar(average_salary_per_year_leeftijd, x="Jaar", y="MaandloonExclusiefOverwerk_6", color="KenmerkenBaan",
                 barmode='group', labels={'MaandloonExclusiefOverwerk_6': 'Gemiddeld Maandloon'})
    
    return fig_leeftijd
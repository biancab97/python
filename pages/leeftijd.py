import dash
from dash import html, dcc, callback, Output, Input
from my_app.plot_graph import plot_barchart_leeftijd
import plotly.express as px


# This tells Dash that this is a page in my app
dash.register_page(__name__)

# Define the layout of the page
fig, work_branch_options_leeftijd, df_salaris = plot_barchart_leeftijd()

layout = html.Div([
    html.H1('Bar Chart verschillende leeftijden'),
    
    # Dropdown for work branches
    dcc.Dropdown(
        id='salaris-work-branch-dropdown-leeftijd',
        options=work_branch_options_leeftijd,
        value=work_branch_options_leeftijd[0]['value']  # Set an initial value
    ),

    # Graph to display salaris data
    dcc.Graph(
        id='leeftijden-example-graph',
        figure=fig
    )
])

# Define a callback function to update the graph when the dropdown selection changes
@callback(
    Output('leeftijden-example-graph', 'figure'),
    [Input('salaris-work-branch-dropdown-leeftijd', 'value')]
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
    
    # Get unique values for the "KenmerkenBaan" column
    #print(df_salaris['KenmerkenBaan'].unique().dtype)
    df_salaris['KenmerkenBaan'] = df_salaris['KenmerkenBaan'].astype(str)
    
    # Create a new bar graph with the filtered data
    # fig = px.bar(filtered_df, x="Jaar", y="MaandloonExclusiefOverwerk_6", color="KenmerkenBaan", barmode='group', category_orders={'Year': [2022]}, labels={'MaandloonExclusiefOverwerk_6': 'Maandloon'})
    
    # Calculate the average salary for each year and gender
    average_salary_per_year_leeftijd = filtered_df.groupby(['Jaar', 'KenmerkenBaan'])['MaandloonExclusiefOverwerk_6'].mean().reset_index()

    # Create a bar chart for each 'Jaar' with the average salary split by gender
    fig = px.bar(average_salary_per_year_leeftijd, x="Jaar", y="MaandloonExclusiefOverwerk_6", color="KenmerkenBaan",
                 barmode='group', labels={'MaandloonExclusiefOverwerk_6': 'Gemiddeld Maandloon'})
    
    return fig
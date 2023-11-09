import dash
from dash import html, dcc, callback, Output, Input
from my_app.plot_graph import plot_barchart
import plotly.express as px


# This tells Dash that this is a page in my app
dash.register_page(__name__)

# Define the layout of the page
fig, work_branch_options, df_salaris = plot_barchart()


layout = html.Div([
    html.H1('Bar Chart Branches'),
    
    # Dropdown for work branches
    dcc.Dropdown(
        id='salaris-work-branch-dropdown',
        options=work_branch_options,
        value=work_branch_options[0]['value']  # Set an initial value
    ),

    # Graph to display salaris data
    dcc.Graph(
        id='salaris-example-graph',
        figure=fig
    )
])

# Define a callback function to update the graph when the dropdown selection changes
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
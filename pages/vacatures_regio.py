import dash
from dash import dash, html, dash_table, dcc, callback, Output, Input
import plotly.express as px

#This tells Dash that this is a page
dash.register_page(__name__)

#Inititialize the app
app = dash(__name__)

#App layout
app.layout = html.Div([
    html.Div(children='Match App'),
    html.Hr(),
    dcc.RadioItems(),
    dash_table.DataTable(data=vacatures_regio_df.to_dict('records'), page_size=10),
    dcc.Graph(figure={}, id='controls-and-graph')
])

#Add controls to build the interaction
@callback(
        Output(component_id='controls-and-graph', component_property='figure'),
        Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.choropleth(
        data_frame=vacatures_regio_df,
        locationmode='',
        locations='',
        scope='',
        color='',
        hover_data='',
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={''},
        template='plotly_dark'
        )

#Run the app
if __name__ == '__main__':
    dash_app.run(debug=True)
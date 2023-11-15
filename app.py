import dash
from dash import Dash, html, dcc, callback, Output, Input

#Create app and add the pages
dash_app = dash.Dash(__name__, use_pages=True)
#Create app for Azure deployment
app = dash_app.server

#Set layout of the entire app
dash_app.layout = html.Div(
    [#Framework of the main app
        html.Div("Python MultiPage Match App", style={'fontSize': 50, 'textAlign':'center'}),
        html.Div([
            dcc.Link(page['name'] + " | ", href=page['path'])
            for page in dash.page_registry.values()
        ]),
        html.Hr(),

        #Content of each page
        dash.page_container
    ]
)
        
if __name__ == "__main__":
    dash_app.run_server(debug=True)
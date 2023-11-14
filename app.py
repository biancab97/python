import dash
from dash import html, dcc, Output, Input


# Create the app and add the pages
dash_app = dash.Dash(__name__, use_pages=True)
# create app for Azure deploy
app = dash_app.server
# Set the layout of the entire app
dash_app.layout = html.Div(
    [
        # main app framework
        html.Div("Python Multipage App with Dash!", style={'fontSize': 50, 'textAlign': 'center'}),
        html.Div([
            dcc.Link(page['name'] + "  |  ", href=page['path'])
            for page in dash.page_registry.values()
        ]),
        html.Hr(),

        # content of each page
        dash.page_container
    ]
)

if __name__ == "__main__":
    dash_app.run_server(debug=True)

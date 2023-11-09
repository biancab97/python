import dash
from dash import html, dcc, Output, Input


# Create the app and add the pages
app = dash.Dash(__name__, use_pages=True)

# Set the layout of the entire app
app.layout = html.Div(
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
    app.run(debug=True)

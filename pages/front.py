import dash
from dash import dcc, html


dash.register_page(__name__, path='/')

layout = html.Div(
    [
        dcc.Markdown('# This will be the home page')
    ]
)
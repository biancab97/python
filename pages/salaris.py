import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np
import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
from dash.dependencies import Input, Output
app=Dash(__name__)
dash.register_page(__name__, path='/salaris') 

layout = html.Div([
    html.H1('This is our Salaris page'),
    html.Div('This is our Salaris page content.'),
])



# Lees de CSV bestanden in en converteer naar DataFrames
salaris_file = 'salarisdata.csv'
# metadata_file = 'salaris_metadata_aangepast.csv'
# combined_file = 'combined_data.csv'

# Read the CSV files into Pandas DataFrames
df_salaris = pd.read_csv(salaris_file, delimiter = ';')
# df_metadata = pd.read_csv(metadata_file, delimiter = ';')
# df_combined = pd.read_csv(combined_file, delimiter = ';')


def salarisuitlezen(df):
    '''
    Deze functie selecteert alle rows uit de DataFrame vanaf
    de periode 2022.
    De kolommen die geselecteerd worden zijn:
    - BedrijfstakkenBranchesSBI2008
    - MaandloonExclusiefOverwerk_6
    - Perioden
    - KenmerkenBaan
    - Jaar
    '''
    # Selecteer alleen index 0 - 4 van de perioden kolom
    df["Jaar"] = df["Perioden"].str[:4]

    # Converteer string naar int
    df["Jaar"] = df["Jaar"].astype('int64')

    # Masker om alleen jaren vanaf 2022 te selecteren en bij kenmerkenBaan alles gecombineerd
    salaris_mask = (df["Jaar"] >= 2022) & (df["KenmerkenBaan"] == 10000)
    df_salaris = df[salaris_mask]
    
    # Gewenste kolommen: 
    df_salaris = df_salaris[["KenmerkenBaan", "BedrijfstakkenBranchesSBI2008", "MaandloonExclusiefOverwerk_6", "Perioden", "Jaar"]]

    # Drop oproep en tijdelijke basis (values: 100460 - 100470)
    df_salaris.drop(df_salaris[(df_salaris['KenmerkenBaan'] == '100460') & (df_salaris['KenmerkenBaan'] == '100470')].index, inplace=True)    
    
    return df_salaris
salarisuitlezen(df_salaris)

df_salaris = salarisuitlezen(df_salaris)

#Tabel is met KenmerkenBaan 10000 dus alles bij elkaar, per sector het loon per maand voor 2022 en 2023

# Create options for the work branches dropdown based on unique values in the "BedrijfstakkenBranchesSBI2008" column
work_branch_options = [{'label': branch, 'value': branch} for branch in df_salaris['BedrijfstakkenBranchesSBI2008'].unique()]
# Create an initial bar graph using Plotly Express
fig = px.bar(df_salaris, x="Perioden", y="MaandloonExclusiefOverwerk_6")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        #Dash: A web application framework for your data.
    '''),

     dcc.Dropdown(
        id='work-branch-dropdown',
        options=work_branch_options,
        value=work_branch_options[0]['value']  # Set an initial value
    ),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )

    
])

# Define a callback function to update the graph when the dropdown selection changes
 



@app.callback( 

    Output('example-graph', 'figure'), 

    [Input('work-branch-dropdown', 'value')] 

) 
def update_graph(selected_branch):
    # Filter the data based on the selected work branch
    filtered_df = df_salaris[(df_salaris['BedrijfstakkenBranchesSBI2008'] == selected_branch)]
    # Create a new bar graph with the filtered data
    fig = px.bar(filtered_df, x='Perioden', y='MaandloonExclusiefOverwerk_6', title='Maandloon per sector', labels={'MaandloonExclusiefOverwerk_6': 'Maandloon'})
    return fig

# Start the Dash web application in debug mode
#if __name__ == '__main__':
   #app.run(debug=True)

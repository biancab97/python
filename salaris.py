import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
from dash import dcc, html
from dash.dependencies import Input, Output


# Lees de CSV bestanden in en converteer naar DataFrames
salaris_file = 'salarisdata.csv'
metadata_file = 'salaris_metadata_aangepast.csv'
combined_file = 'combined_data.csv'

# Read the CSV files into Pandas DataFrames
df_salaris = pd.read_csv(salaris_file, delimiter = ';')
df_metadata = pd.read_csv(metadata_file, delimiter = ';')
df_combined = pd.read_csv(combined_file, delimiter = ';')

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

def bedrijfstak(df_metadata):
    '''
    Deze functie maakt een kolom met de branche per type bedrijf
    Key: T001081 print descriptie: "A-U alle economische activiteiten"
    '''
    df_metadata["Title"] = df_metadata["Title"].map(lambda row:row.split(" ", 1)[1])
    
    return df_metadata

# def combineer(df_salaris, df_metadata):
    # This function combines data from two dataframes to create a plot with branches on the x-axis and average monthly salary on the y-axis.
    
    # Extract the "MaandloonExclusiefOverwerk_6" column from df_salaris
    #salaris = df_salaris["MaandloonExclusiefOverwerk_6"]

    # Print a label to indicate that we are working with the "df_salaris" dataframe
    #print("SALARIS")

    # Display the first 5 rows of the df_salaris dataframe
    #display(df_salaris.head(5))
    #print()

    # Extract the "Title" column from df_metadata
    #branche = df_metadata["Title"]

    # Print a label to indicate that we are working with the "df_metadata" dataframe
    #print("METADATA")
    #print()

    # Display the first 5 rows of the df_metadata dataframe
    #display(df_metadata.head(5))

    # Create a set of unique values from the "BedrijfstakkenBranchesSBI2008" column in df_salaris
    #salaris_values = set(df_salaris["BedrijfstakkenBranchesSBI2008"].unique())

    # Create a set of unique values from the "Key" column in df_metadata
    #metadata_values = set(df_metadata["Key"].unique())

    # Print the intersection of unique values between the two dataframes to find the common denominator
    #print(salaris_values & metadata_values)



# Cleaning operations
#df_salaris = salarisuitlezen(df_salaris)
#df_metadata = bedrijfstak(df_metadata)

# Plot gemiddelde maandloon per branche
# ** (helaas alleen branche 'T001081' gemeen) **
# combineer(df_salaris, df_metadata)

df_salaris = salarisuitlezen(df_salaris)

#Tabel is met KenmerkenBaan 10000 dus alles bij elkaar, per sector het loon per maand voor 2022 en 2023
app = Dash(__name__)
# Create options for the work branches dropdown based on unique values in the "BedrijfstakkenBranchesSBI2008" column
work_branch_options = [{'label': branch, 'value': branch} for branch in df_salaris['BedrijfstakkenBranchesSBI2008'].unique()]
# Create an initial bar graph using Plotly Express
fig = px.bar(df_salaris, x="Perioden", y="MaandloonExclusiefOverwerk_6")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
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
    fig = px.bar(filtered_df, x='Perioden', y='MaandloonExclusiefOverwerk_6', title='Maandloon per sector per maand')
    return fig

# Start the Dash web application in debug mode
if __name__ == '__main__':
    app.run(debug=True)

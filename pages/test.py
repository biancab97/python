import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np
import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
from dash.dependencies import Input, Output


# Lees de CSV bestanden in en converteer naar DataFrames
salaris_file = 'salarisdata.csv'
#metadata_file = 'salaris_metadata_aangepast.csv'
#combined_file = 'combined_data.csv'


# Read the CSV files into Pandas DataFrames
df_salaris = pd.read_csv(salaris_file, delimiter = ';')
#df_metadata = pd.read_csv(metadata_file, delimiter = ';')
#df_combined = pd.read_csv(combined_file, delimiter = ';')


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
display(salarisuitlezen(df_salaris))
from my_app.datauitlezen import vacaturesUitlezen, vacatureLabels, vacaturesRegioUitlezen, regioLabels
import plotly.express as px
import pandas as pd
import requests
from requests_file import FileAdapter
import json

# Plot linegraph
def plot_bargraph():
    vacatures_df = vacaturesUitlezen()
    sectoren_metadata_df = vacatureLabels()

    #Create a mapping dictionary for periods
    periodes_mapping = {
        '2020KW01': 'Jan-Mar 2020',
        '2020KW02': 'Apr-Jun 2020',
        '2020KW03': 'Jul-Sep 2020',
        '2020KW04': 'Oct-Dec 2020',
        '2021KW01': 'Jan-Mar 2021',
        '2021KW02': 'Apr-Jun 2021',
        '2021KW03': 'Jul-Sep 2021',
        '2021KW04': 'Oct-Dec 2021',
        '2022KW01': 'Jan-Mar 2022',
        '2022KW02': 'Apr-Jun 2022',
        '2022KW03': 'Jul-Sep 2022',
        '2022KW04': 'Oct-Dec 2022',
        '2023KW01': 'Jan-Mar 2023',
        '2023KW02': 'Apr-Jun 2023',
    }

    # Apply the mapping to Perioden column in vacatures dataframe
    vacatures_df['Perioden'] = vacatures_df['Perioden'].astype(str).map(periodes_mapping)

    # Get unique values from both dataframes
    vacatures_sectoren = vacatures_df['Bedrijfskenmerken'].unique()
    sectoren_metadata = sectoren_metadata_df['Title'].unique()

    # Create options for the sectoren dropdown options based on Bedrijfskenmerken column
    # Create a list of dictionaries using zip
    sectoren_options = [{'label': title, 'value': sector} for title, sector in zip(sectoren_metadata, vacatures_sectoren)]

    # Create an initial line graph using Plotly Express
    fig = px.bar(vacatures_df, x="Perioden", y="OpenstaandeVacatures_1", title="Openstaande Vacatures Per Sector")
    return fig, sectoren_options, vacatures_df

# Plot chloropleth map
def plot_map():
    vacatures_regio_df = vacaturesRegioUitlezen()
    regios_metadata_df = regioLabels()
    #print(vacatures_regio_df)
    #print(regios_metadata_df)

    # Load GeoJSON file
    s = requests.Session()
    s.mount('file://', FileAdapter())

    provincies = s.get('file:///C:/Users/Student/OneDrive/Bureaublad/python/data/provincies.json')
    provinciesDataRaw = provincies.json()
    provinciesData = provinciesDataRaw["features"]
    #print(provinciesData)

    # Create a mapping dictionary for periods
    perioden_mapping = {
        '2020KW01': 'Jan-Mar 2020',
        '2020KW02': 'Apr-Jun 2020',
        '2020KW03': 'Jul-Sep 2020',
        '2020KW04': 'Oct-Dec 2020',
        '2021KW01': 'Jan-Mar 2021',
        '2021KW02': 'Apr-Jun 2021',
        '2021KW03': 'Jul-Sep 2021',
        '2021KW04': 'Oct-Dec 2021',
        '2022KW01': 'Jan-Mar 2022',
        '2022KW02': 'Apr-Jun 2022',
        '2022KW03': 'Jul-Sep 2022',
        '2022KW04': 'Oct-Dec 2022',
        '2023KW01': 'Jan-Mar 2023',
        '2023KW02': 'Apr-Jun 2023',
    }

    # Apply the mapping for regions on Regios column
    #vacatures_regio_df['Regios'] = vacatures_regio_df['Regios'].astype(str).map(regio_mapping)
    #Apply the mapping on Perioden column
    vacatures_regio_df['Perioden'] = vacatures_regio_df['Perioden'].astype(str).map(perioden_mapping)
    # Get unique values from both dataframes
    vacatures_regio = vacatures_regio_df['Regios'].unique()
    regios_metadata = regios_metadata_df['Title'].unique()

    # Create options for the sectoren dropdown options based on Bedrijfskenmerken column
    # Create a list of dictionaries using zip
    regios_options = [{'label': title, 'value': regio} for title, regio in zip(regios_metadata, vacatures_regio)]

    # Create an initial chloropleth map
    fig_map = px.choropleth_mapbox(vacatures_regio_df, geojson=provinciesDataRaw, locations='Regios', color='OpenstaandeVacatures', featureidkey="id",
                           color_continuous_scale="Viridis",
                           range_color=(0, 2),
                           mapbox_style="open-street-map",
                           zoom=6, center = {"lat": 52.14898973341009, "lon": 5.571005662096867},
                           opacity=0.5,
                           labels={'OpenstaandeVacatures':'Openstaande Vacatures'}
                          )
    #print(fig_map)
    #print(regios_options)
    #print(vacatures_regio_df)
    return fig_map, regios_options, vacatures_regio_df
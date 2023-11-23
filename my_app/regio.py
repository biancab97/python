import requests

from requests_file import FileAdapter

s = requests.Session()
s.mount('file://', FileAdapter())

provincies = s.get('file:///C:/Users/Student/OneDrive/Bureaublad/python/data/provincies.json')
# with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
provinciesDataRaw = provincies.json()
provinciesData = provinciesDataRaw["features"]


# print(provinciesData)


import pandas as pd
df = pd.read_csv("data/vacatures_regio.csv", dtype={"Regios": str})
# print(df)
import plotly.express as px

fig = px.choropleth_mapbox(df, geojson=provinciesDataRaw, locations='Regios', color='OpenstaandeVacatures', featureidkey="id",
                           color_continuous_scale="Viridis",
                           range_color=(0, 2),
                           mapbox_style="open-street-map",
                           zoom=6, center = {"lat": 52.14898973341009, "lon": 5.571005662096867},
                           opacity=0.5,
                           labels={'OpenstaandeVacatures':'Openstaande Vacatures'}
                          )

#print(fig)


# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
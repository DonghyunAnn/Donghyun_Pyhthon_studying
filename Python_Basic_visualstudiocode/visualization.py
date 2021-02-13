import numpy as np
import pandas as pd
from urllib.request import urlopen
import json

import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
from plotly.validators.scatter.marker import SymbolValidator

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

counties["features"][0]

unemp=pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                 dtype={"fips":str})
unemp.head()

fig=px.choropleth_mapbox(unemp,geojson=counties,locations='fips',color='unemp',
                        color_continuous_scale='blues',
                        range_color=(0,12),
                        mapbox_style='carto-position',
                        zoom=3,center={'lat':37,'lon':-95},
                        opacity=0.5,
                        labels={'unemp':'unemployment rate'})
fig.update_layout(margin={'r':0,'t':0,'l':0,'b':0})
fig.show()
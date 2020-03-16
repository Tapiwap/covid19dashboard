# Import the relevant libraries
import pandas as pd
import numpy as np
import io
import requests
from bokeh.io import curdoc

import bokeh
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool

from covid19_global import create_world_map
from region_impact_bar import create_region_impact_bar
from covid19_growth import create_stacked_chart

# Create the data frames
confirmed_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
deaths_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv"
recovered_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv"

confirmed_request = requests.get(confirmed_url).content
deaths_url = requests.get(deaths_url).content
recovered_url = requests.get(recovered_url).content

confirmed_df = pd.read_csv(io.StringIO(confirmed_request.decode('utf-8')))
death_df = pd.read_csv(io.StringIO(deaths_url.decode('utf-8')))
recovered_df = pd.read_csv(io.StringIO(recovered_url.decode('utf-8')))

world_map = create_world_map(confirmed_df)
bar_chart = create_region_impact_bar(confirmed_df, death_df, recovered_df)
vstacked_chart = create_stacked_chart(confirmed_df, death_df, recovered_df)

curdoc().add_root(world_map)
curdoc().add_root(bar_chart)
curdoc().add_root(vstacked_chart)
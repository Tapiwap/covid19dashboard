# Import the relevant libraries
import pandas as pd
import numpy as np
import io
import requests
from bokeh.io import curdoc

import bokeh
from bokeh.plotting import figure
from bokeh.layouts import Row, Column
from bokeh.models import ColumnDataSource, HoverTool

from covid19_global import create_world_map
from region_impact_bar import create_region_impact_bar
from covid19_growth import create_chart
from pie_chart import create_pie_chart
from bokeh.models import Button
from bokeh.models import Dropdown

cofirmed_flag = 0

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

# Create the buttons
defaultBtn = Button(label="Default", button_type="default")
confirmedBtn = Button(label="Confirmed", button_type="warning")
deceasedBtn = Button(label="Deceased", button_type="danger")
recoveredBtn = Button(label="Recovered", button_type="primary")
menu = [("Item 1", "item_1"), ("Item 2", "item_2"), None, ("Item 3", "item_3")]
dropdown = Dropdown(label="Dropdown button", button_type="success", menu=menu)


# Draw the figures
world_map = create_world_map(confirmed_df)
bar_chart = create_region_impact_bar(confirmed_df, death_df, recovered_df)
vstacked_chart = create_chart(confirmed_df, death_df = death_df, recovered_df = recovered_df)
pie_chart = create_pie_chart(confirmed_df, death_df, recovered_df)

#def confirmedBtn_onclick():
#    create_chart(confirmed_df, "#FF5733")

#confirmedBtn.on_click(confirmedBtn_onclick)
#deceasedBtn.on_click(deceasedBtn_onclick)
#recoveredBtn.on_click(recoveredBtn_onclick)

# Create the Rows
#first_row = Row(defaultBtn, confirmedBtn, deceasedBtn, recoveredBtn)
second_row = Row(world_map, pie_chart)
third_row = Row(bar_chart, vstacked_chart)

# Add to current document
#curdoc().add_root(first_row)
curdoc().add_root(second_row)
curdoc().add_root(third_row)
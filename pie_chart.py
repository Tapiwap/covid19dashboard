from math import pi
import pandas as pd

from bokeh.io import show
from bokeh.plotting import figure
from bokeh.transform import cumsum

def create_pie_chart(confirmed_df, death_df, recovered_df):
    """
    """
    confirmed_cases = confirmed_df.iloc[:,-3:-2].sum()
    deceased_cases = death_df.iloc[:,-1:].sum()
    recovered_cases = recovered_df.iloc[:,-1:].sum()

    x = {
        'Confirmed': confirmed_cases[0],
        'Deceased': deceased_cases[0],
        'Recovered': recovered_cases[0]
    }

    data = pd.Series(x).reset_index(name='value').rename(columns={'index':'Cases'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = ["#FFC300", "#FF5733", "#82E0AA"]

    p = figure(plot_height=350, title="Confirmed vs Deceased vs Recovered", toolbar_location=None,
           tools="hover", tooltips="@Cases: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='Cases', source=data)

    p.axis.axis_label=None
    p.axis.visible=False
    p.grid.grid_line_color = None

    return p

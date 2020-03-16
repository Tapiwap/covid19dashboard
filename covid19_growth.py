from bokeh.models import NumeralTickFormatter
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
import pandas as pd

def create_stacked_chart(confirmed_df, death_df, recovered_df):
    dates_df = confirmed_df.iloc[:,4:]
    dates = list(dates_df.columns)

    confirmed_sums_list = []
    death_sums_list = []
    recovered_sums_list = []

    if 'x' in dates and 'y' in dates:
        dates.remove('x')
        dates.remove('y')
            
    for date in dates:  
        confirmed_sum = confirmed_df[date].sum()
        confirmed_sums_list.append(confirmed_sum)
        death_sum = death_df[date].sum()
        death_sums_list.append(death_sum)
        recovered_sum = recovered_df[date].sum()
        recovered_sums_list.append(recovered_sum)

    # stack death -> recovered -> confirmed

    source = ColumnDataSource(data=dict(
        x=[pd.to_datetime(date) for date in dates],
        y1=death_sums_list,
        y2=recovered_sums_list,
        y3=confirmed_sums_list,
    ))

    """TOOLTIPS  = [
        ("Deceased", "@y1{0,0}"),
        ("Recovered", "@y2{0,0}"),
        ("Confirmed", "@y3{0,0}")
    ]"""

    p = figure(x_axis_type='datetime', plot_width=800, plot_height=400, toolbar_location="right")

    p.varea_stack(['y1', 'y2', 'y3'], x='x', color=("#82E0AA", "#FF5733", "#FFC300"), source=source)

    p.yaxis.formatter=NumeralTickFormatter(format="00")

    return p
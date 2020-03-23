from bokeh.models import NumeralTickFormatter
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
import pandas as pd

TOOLTIPS  = [
        ("Deceased", "@y1{0,0}"),
        ("Recovered", "@y2{0,0}"),
        ("Confirmed", "@y3{0,0}")
    ]
p = figure(x_axis_type='datetime', plot_width=650, plot_height=350, toolbar_location="right", title="Growth over Time", tooltips=TOOLTIPS)

source = ColumnDataSource(data = dict())

def create_chart(df, *args, **kwargs):
    
    if (kwargs):
        death_df = kwargs['death_df']
        recovered_df = kwargs['recovered_df']
        return create_stacked_chart(df, death_df, recovered_df)
    
    if (args): 
        colour = args[0]
        return create_area_chart(df, colour)

def create_area_chart(df, colour):
    dates_df = df.iloc[:,3:]
    dates = list(dates_df.columns)

    sums_list = []

    if 'Long' in dates:        
        dates.remove('Long')

    if 'x' in dates and 'y' in dates:
        dates.remove('x')
        dates.remove('y')
            
    for date in dates:  
        sum_ = df[date].sum()
        sums_list.append(sum_)

    # stack death -> recovered -> confirmed
    source.data = {'x':[],'y1':[]}
    source.data.update(dict(
        x=[pd.to_datetime(date) for date in dates],
        y1=sums_list
    ))

    TOOLTIPS  = [
        ("Confirmed", "@y1{0,0}"),   
    ]

    p.varea_stack(['y1'], x='x', color=colour, source=source)

    p.yaxis.formatter=NumeralTickFormatter(format="00")

    return p

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
    source.data.update(dict(
        x=[pd.to_datetime(date) for date in dates],
        y1=death_sums_list,
        y2=recovered_sums_list,
        y3=confirmed_sums_list,
    ))

    

    p.line(x='x', y='y1', color="#FF5733", line_width=2, source=source)
    p.line(x='x', y='y2', color="#82E0AA", line_width=2, source=source)
    p.line(x='x', y='y3', color="#FFC300", line_width=2, source=source)

    p.circle(x='x', y='y1', color="#FF5733", line_width=2, source=source)
    p.circle(x='x', y='y2', color="#82E0AA", line_width=2, source=source)
    p.circle(x='x', y='y3', color="#FFC300", line_width=2, source=source)

    p.yaxis.formatter=NumeralTickFormatter(format="00")

    return p
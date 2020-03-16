from bokeh.models import FactorRange
from bokeh.transform import dodge
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure

def create_region_impact_bar(confirmed_df, death_df, recovered_df):
    """
    """
    region_list = ['US', 'China', 'Italy']
    c_totals = []
    d_totals = []
    r_totals = []

    for region in region_list:
        c_region_df = confirmed_df[confirmed_df['Country/Region'] == region]
        d_region_df = death_df[death_df['Country/Region'] == region]
        r_region_df = recovered_df[recovered_df['Country/Region'] == region]
        
        d_total = d_region_df.iloc[:,-3:-2].sum()
        c_total = c_region_df.iloc[:,-3:-2].sum()
        r_total = r_region_df.iloc[:,-3:-2].sum()
        
        c_totals.append(c_total[0])
        d_totals.append(d_total[0])
        r_totals.append(r_total[0])
    
    data = {'region_list' : region_list,
        'c_totals'   : c_totals,
        'd_totals'   : d_totals,
        'r_totals'  : r_totals
       }

    source = ColumnDataSource(data=data)

    p = figure(x_range=region_list, plot_height=250, title="Covid19 By Country/Region")

    p.vbar(x=dodge('region_list', -0.25, range=p.x_range), top='c_totals', width=0.2, source=source,
        color="#FFC300", legend_label="Confirmed")

    p.vbar(x=dodge('region_list',  0.0,  range=p.x_range), top='d_totals', width=0.2, source=source,
        color="#FF5733", legend_label="Deceased")

    p.vbar(x=dodge('region_list',  0.25,  range=p.x_range), top='r_totals', width=0.2, source=source,
        color="#82E0AA", legend_label="Recovered")

    p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None
    p.legend.location = "top_left"
    p.legend.orientation = "horizontal"

    return p
import numpy as np
from bokeh.plotting import figure
from bokeh.tile_providers import Vendors, get_provider

def __wgs84_to_web_mercator(df_, lon="Long", lat="Lat"):
    """Converts decimal longitude/latitude to Web Mercator format"""
    k = 6378137
    df_["x"] = df_[lon] * (k * np.pi/180.0)
    df_["y"] = np.log(np.tan((90 + df_[lat]) * np.pi/360.0)) * k
    return df_

def create_world_map(df):
    """
    This method creates a world map and shows all the locations where
    of covid19 impact
    """
    tile_provider = get_provider(Vendors.CARTODBPOSITRON)

    # range bounds supplied in web mercator coordinates
    p = figure(x_range=(-3000000, 12000000), y_range=(-4000000, 7000000), plot_width=850, plot_height=400,
            x_axis_type="mercator", y_axis_type="mercator", title="Covid19 Globally")

    lat = list(df['Lat'])
    long = list(df['Long'])

    __wgs84_to_web_mercator(df)

    p.add_tile(tile_provider)
    p.circle(x=df['x'], y=df['y'], size=10, fill_color="#FFC300", fill_alpha=0.6)

    return p
from dash import html, dcc
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import pandas as pd



paper_bg_color = '#1a1c23'
plot_bg_color  = '#30333d'
plot_bg_color2 = '#22252b'
header_color   = '#b2b2b2'
text_color     = '#ededed'
green_color    = '#45df7e'
red_color      = '#da5657'


def width_dict_same(width):
    size = ["xs", "sm", "md", "lg", "xl"]
    data = {i: width for i in size}
    return data

def width_dict_multi(small, medium, large):
    return {"xs": small, "sm": small, "md": medium, "lg": large, "xl": large}




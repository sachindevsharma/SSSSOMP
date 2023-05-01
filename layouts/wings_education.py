import dash 
from dash import html, dcc
import dash_bootstrap_components as dbc


def build_wings_education():
    return html.Div([
        dbc.Row(html.H1("Education Wing"), className="wings_header"),
        dbc.Row(className="wings", children=[
            dbc.Col(build_left_panel(), className="div_left_panel", width=3), 
            dbc.Col(build_right_panel(), className="div_right_panel")
        ])
    ])


def build_left_panel():
    return html.Div(className="tabs_group", children=[
        html.P("Bal Vikas Prayers", className="left_panel_tab",),
        html.Div("e-Books", className="left_panel_tab",),
        html.Div("Parenting Form", className="left_panel_tab",),
        html.Div("Ba Vikas Results", className="left_panel_tab",),
        # html.Div("Geeta Vahini e-Book", className="left_panel_tab",),
        # html.Div("Maa Eshwaramma e-Book", className="left_panel_tab",),
    ])

    
    
def build_right_panel():
    return  html.Div(className="details", children = [
        dbc.Row([
            dbc.Col([
                html.H5('Topic 1'),
                html.P("Here goes the content for Topic 1. We'll add the content later.")
            ]),
            dbc.Col(html.Img(src=dash.get_asset_url('images/image1.png'))),
        ]),
        html.Br(),
        dbc.Row([
            dbc.Col(html.Img(src=dash.get_asset_url('images/image2.png'))),
            dbc.Col([
                html.H5('Topic 2'),
                html.P("Here goes the content for Topic 2. We'll add the content later.")
            ]),
        ]),
    ])
    




    
    

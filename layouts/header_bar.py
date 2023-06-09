import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from helper_functions import *


def build_header_bar():
    print("header bar")
    return html.Div([
            build_banner(),
            html.Br(),
            build_banner_2(),
    ])
    

def build_banner():
    
    return html.Div(className="banner", children=[
        dbc.Row([
            dbc.Col(html.A(html.Img(src=dash.get_asset_url("logo.png")), 
                    href="/"), 
                    **width_dict_multi(3, "auto", "auto")), 
            dbc.Col(**width_dict_multi(9, "auto", "auto"), children=[
                dbc.Row(html.H2("SRI SATHYA SAI SEVA ORGANIZATION", className="header")),
                dbc.Row(html.H6("Madhya Pradesh", className="header"))
            ]),
        ]),
        dbc.Row(id="header_tabs_1", children=_build_tabs()),
        *get_popover_data(),
    ])


def build_banner_2():
    
    return dbc.Navbar(className="new", sticky="top", children=[
        
            dbc.Col(html.A(html.Img(src=dash.get_asset_url("logo.png")), href="/"), 
                        **width_dict_same("auto"),), 
            dbc.Col(**width_dict_same("auto"), children=[
                html.H6("SRI SATHYA SAI SEVA", className="header"),
                html.H6("ORGANIZATION", className="header"),
                html.H6("Madhya Pradesh", className="header")
            ]),
            dbc.Col(children=[
                dbc.NavbarToggler(id="navbar-toggler"),
                dbc.Collapse(id="navbar-collapse", children=_build_tabs2(), navbar=True, is_open=False),
                *get_popover_data2(),
                
            ]),
    ])


def get_popover_data():
    popover_data = []

    for name in ["Sri Sathya Sai Baba", "Wings", "Activities", "Services"]:

        start = "sss" if name == "Sri Sathya Sai Baba" else name.lower()
        popover_content = dbc.PopoverBody([
            # dbc.DropdownMenuItem(divider=True),
            *[_get_nav_link(i) for i in dash.page_registry.keys() if i.startswith(start)]
        ])
        popover = dbc.Popover(popover_content, offset=0, hide_arrow=True,
                              target=name, trigger="hover", placement="bottom-start"
                             )
        popover_data.append(popover)
        # print(popover_data)
    
    return popover_data

def get_popover_data2():
    popover_data = []

    for name in ["Sri Sathya Sai Baba", "Wings", "Activities", "Services"]:

        start = "sss" if name == "Sri Sathya Sai Baba" else name.lower()
        popover_content = dbc.PopoverBody([
            # dbc.DropdownMenuItem(divider=True),
            *[_get_nav_link(i) for i in dash.page_registry.keys() if i.startswith(start)]
        ])
        popover = dbc.Popover(popover_content, offset=0, hide_arrow=True,
                              target=name+"2", trigger="hover", placement="bottom-start"
                             )
        popover_data.append(popover)
    
    return popover_data

def _get_nav_link(page):
    external_links = {  
        "Sai One": "https://ssssompcg.org/ssssoseva_india/www/#/app/login",
        "Sewa Coordinator": "https://www.ssssompcg.org/ssssoseva_india/PER_DETAILS/editor/login.asp"
    }
    data = dash.page_registry[page]
    if data["name"] in external_links:
        return dbc.NavLink(data['name'], href=external_links[data["name"]], target="_blank",)
    else:
        return dbc.NavLink(data['name'], href=data["relative_path"])

    
def build_intervals_div():
    return html.Div(id='interval_div', children=[
        dcc.Interval(id="i1", interval=1 * 1000, n_intervals=0),
        dcc.Interval(id="i2", interval=2 * 1000, n_intervals=0),
        dcc.Interval(id="i5", interval=5 * 1000, n_intervals=0),
        dcc.Interval(id="i60", interval=60 * 1000, n_intervals=0),
    ])

def _build_tabs():
    arrow_down = "fa fa-chevron-down fa-2xs fa-beat"
    header_options = [
            # Name, Sub headings
            ["Sri Sathya Sai Baba", arrow_down],
            ["SSSSOMP", ''],
            ["Wings", arrow_down],
            ["Activities", arrow_down],
            ["Gallery", ''],
            ["Services", arrow_down], 
            ["Contact Us", ''],
        ]
    tabs = [
            dbc.Col(id=tab[0], class_name="tab_name", width="auto", 
                    children=html.H6([tab[0] + " ", 
                                      html.I(className=tab[1], id=tab[0] + "_arrow")])) 
            for tab in header_options
        ]
    return tabs
    
def _build_tabs2():
    arrow_down = "fa fa-chevron-down fa-2xs fa-beat"
    header_options = [
            # Name, Sub headings
            ["Sri Sathya Sai Baba", arrow_down],
            ["SSSSOMP", ''],
            ["Wings", arrow_down],
            ["Activities", arrow_down],
            ["Gallery", ''],
            ["Services", arrow_down], 
            ["Contact Us", ''],
        ]
    tabs = [
            dbc.Col(id=tab[0]+"2", class_name="tab_name", width="auto", 
                    children=html.H6([tab[0] + " ", 
                                      html.I(className=tab[1], id=tab[0]+ "2" + "_arrow")])) 
            for tab in header_options
        ]
    return dbc.Row(tabs, class_name="mx-auto")



    # logo_dict = {
    #     "tab1": html.I(className="fa fa-home"),
    #     "tab2": html.I(className="fa fa-regular fa-sun"),
    #     "tab3": html.I(className="fa fa-thin fa-book"),
    #     "tab4": html.I(className="fa fa-brands fa-windows"),
    #     "tab5": html.I(className="fa fa-home"),
    #     "tab6": html.I(className="fa fa-thin fa-face-smile"),
    #     "tab7": html.I(className="fa fa-thin fa-computer"),
    #     "tab8": html.I(className="fa fa-thin fa-cloud-arrow-down"),
    # }


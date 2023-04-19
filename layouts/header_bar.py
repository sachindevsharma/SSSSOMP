import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from assets import dropdown_values
from dash_bootstrap_templates import ThemeChangerAIO


def width_dict_same(width):
    size = ["xs", "sm", "md", "lg", "xl"]
    data = {i: width for i in size}
    return data

def width_dict_multi(small, medium, large):
    return {"xs": small, "sm": small, "md": medium, "lg": large, "xl": large}


def build_header_bar(app):
    return html.Div([
            build_banner(app),
            html.Br(),
            build_banner_2(app),
            html.Br(), 
            # navbar
    ])

def build_tabs_2():
    # The keys of this dictionary should be same as module defined in 
    # layouts/__init__.py while registering pages 

    header_tabs = ["Sri Sathya Sai Baba", "Organisation", "Wings", 
                   "Activities", "Gallery", "Services", "Contact Us"]
    
    # fa-duotone fa-square-chevron-down
    tabs = [dbc.Col(html.H6([i, " ", html.I(className="fa fa-chevron-down fa-2xs fa-beat")]), id=i+'2', class_name="tab_name", width="auto") 
            for i in header_tabs]

    return html.Div(children=[
        dbc.Row(tabs),
        *get_popover_data()
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

    return popover_data


search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button(
                "Search", color="primary", className="ms-2", n_clicks=0
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        # dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Navbar", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://plotly.com",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                build_tabs_2(),
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
)
    
    
def build_banner(app):
    
    return html.Div(className="banner", children=[
        dbc.Row([
            dbc.Col(html.A(html.Img(src=app.get_asset_url("logo.png")), href="/"), **width_dict_multi(3, "auto", "auto")), 
            dbc.Col(width="auto", **width_dict_multi(9, "auto", "auto"),      children=[
                dbc.Row(html.H2("SRI SATHYA SAI SEVA ORGANIZATION", className="header")),
                dbc.Row(html.H6("Madhya Pradesh", className="header"))
            ]),
        ]),
        dbc.Row(id="header_tabs_1", children=build_tabs(),
            # dbc.Col(children=build_tabs()),
        ),
        # ],**size_dict),
        # ThemeChangerAIO(aio_id="theme", 
        #                 button_props={"color": "primary", "style": {"height": "auto", "width": "5vw"}},
        #                 radio_props={"value": dbc.themes.CERULEAN})
    ])

def build_banner_2(app):
    
    return dbc.Navbar(className="new", expand="md", children=[
        dbc.Row([
        
            dbc.Col(html.A(html.Img(src=app.get_asset_url("Logo_name-removebg-preview.png")), href="/"), width="auto"), 
            # dbc.Col(width="auto", children=[
            #     html.H6("SRI SATHYA SAI SEVA", className="header"),
            #     html.H6("ORGANIZATION", className="header"),
            #     html.H6("Madhya Pradesh", className="header")
            # ]),
            # dbc.Col(html.I(className="fa fa-home"),),
            dbc.Col(width="auto", children=[
                dbc.NavbarToggler(id="navbar-toggler", className="float-right"),
                dbc.Collapse(build_tabs_2(), className="float-right",id="navbar-collapse", navbar=True, is_open=False),
            ]),

        ]),
    ])


def build_tabs():
    # The keys of this dictionary should be same as module defined in 
    # layouts/__init__.py while registering pages 

    arrow_down = html.I(className="fa fa-chevron-down fa-2xs fa-beat")

    header_tabs = [
                   ["Sri Sathya Sai Baba", " ", arrow_down],
                   ["SSSSOMP", " "],
                   ["Wings", " ", arrow_down],
                   ["Activities", " ", arrow_down],
                   ["Gallery", " "],
                   ["Services", " ", arrow_down], 
                   ["Contact Us", " "],
                   ]
    # fa-duotone fa-square-chevron-down
    tabs = [dbc.Col(html.H6(i), id=i[0], class_name="tab_name", width="auto") 
            for i in header_tabs]

    return [*tabs, *get_popover_data()]

def build_tabs_2():
    # The keys of this dictionary should be same as module defined in 
    # layouts/__init__.py while registering pages 

    header_tabs = ["Sri Sathya Sai Baba", "Organisation", "Wings", 
                   "Activities", "Gallery", "Services", "Contact Us"]
    
    # fa-duotone fa-square-chevron-down
    tabs = [dbc.Col(html.H6([i, " ", html.I(className="fa fa-chevron-down fa-2xs fa-beat")]), id=i+'2', class_name="tab_name", width="auto") 
            for i in header_tabs]

    return html.Div( children=[
        dbc.Row(tabs),
        *get_popover_data()
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

    return popover_data

def _get_nav_link(page):
    data = dash.page_registry[page]
    return dbc.NavLink(data['name'], href=data["relative_path"])

    
def build_intervals_div():
    return html.Div(id='interval_div', children=[
        dcc.Interval(id="i1", interval=1 * 1000, n_intervals=0),
        dcc.Interval(id="i2", interval=2 * 1000, n_intervals=0),
        dcc.Interval(id="i5", interval=5 * 1000, n_intervals=0),
        dcc.Interval(id="i60", interval=60 * 1000, n_intervals=0),
    ])



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


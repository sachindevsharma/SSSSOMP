import dash
from dash import html, Input, State, Output
import dash_bootstrap_components as dbc
import requests

API_BASE_URL = "http://127.0.0.1:8050"


def callbacks_header_bar():
    @dash.callback(
            Output(f"navbar-collapse", "is_open"),
            [Input(f"navbar-toggler", "n_clicks")],
            [State(f"navbar-collapse", "is_open")],
        )
    def toggle_navbar_collapse(n, is_open):
        if n:
            return not is_open
        return is_open


    @dash.callback(
        Output("header_tabs_1", "children"),
        Input("loading_div", "children"),
    )
    def test_api(n):
        data = requests.post(API_BASE_URL + '/api/header/options').json()
        arrow_down = html.I(className="fa fa-chevron-down fa-2xs fa-beat")

        header_tabs = [[i, " ", arrow_down] if j == True else [i, " "] 
                       for i,j in zip(data["options"], data["sub_headings"])]
        # fa-duotone fa-square-chevron-down
        tabs = [dbc.Col(html.H6(i), id=i[0], class_name="tab_name", width="auto") 
                for i in header_tabs]
        
        return tabs
    
    
    @dash.callback(
        Output("navbar-collapse", "children"),
        Input("loading_div", "children"),
    )
    def test_api(n):
        data = requests.post(API_BASE_URL + '/api/header/options').json()
        arrow_down = html.I(className="fa fa-chevron-down fa-2xs fa-beat")

        header_tabs = [[i, " ", arrow_down] if j == True else [i, " "] 
                       for i,j in zip(data["options"], data["sub_headings"])]
        # fa-duotone fa-square-chevron-down
        tabs = [dbc.Col(html.H6(i), id=i[0]+"2", class_name="tab_name", width="auto") 
                for i in header_tabs]
        
        return dbc.Row(tabs, class_name="mx-auto")


    
    
   
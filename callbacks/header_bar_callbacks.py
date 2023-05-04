import dash
from dash import html, Input, State, Output, ctx
import dash_bootstrap_components as dbc
import requests
from flask import request
 

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
        # print(dir(dash.get_app()))
        print("Sachin")
        print(request.host_url)
        API_BASE_URL = request.host_url
        print()
        data = requests.post(API_BASE_URL + '/api/header/options').json()
        arrow_down = "fa fa-chevron-down fa-2xs fa-beat"

        header_tabs = [[i, " ", html.I(className=arrow_down)] 
                       if j == True else [i, " "] 
                       for i,j in zip(data["options"], data["sub_headings"])]
        
        header_tabs = [[i, arrow_down] if j == True else [i, ""] 
                       for i,j in zip(data["options"], data["sub_headings"])]
        
        true_only = [i[0] for i in header_tabs if i[1] !="" ]

        tabs = [
            dbc.Col(id=tab[0], class_name="tab_name", width="auto", 
                    children=html.H6([tab[0] + " ", 
                                      html.I(className=tab[1], id=tab[0] + "_arrow")])) 
            for tab in header_tabs
        ]
        
        return tabs
    
    # output_list, input_list, state_list = [], [], []
    # data = requests.post(API_BASE_URL + '/api/header/options').json()
    # for name in data["options"]:
    #     if data["sub_headings"]:
    #         output_list.append(name + "_arrow", "className")
    #         input_list.append(name, "n_clicks")
    #         state_list.append(name + "_arrow", "className")

    # params_list = [f"O{i+1}" for i in range(len(output_list))]
    # params_list += [f"I{i+1}" for i in range(len(input_list))]
    # params_list += [f"S{i+1}" for i in range(len(state_list))]

    # @dash.callback(
    #     Output(name + "_arrow", "className"),
    #     Input(name, "n_clicks"),
    #     State(name + "_arrow", "className")
    # )
    # def update_arrow(*params_list):
    #     print(ctx.triggered, ctx.triggered_id, ctx.triggered_prop_ids)

    #     return [dash.no_update for i in range(len(output_list))]

    
    
    @dash.callback(
        Output("navbar-collapse", "children"),
        Input("loading_div", "children"),
    )
    def test_api(n):
        API_BASE_URL = request.host_url
        data = requests.post(API_BASE_URL + '/api/header/options').json()
        arrow_down = html.I(className="fa fa-chevron-down fa-2xs fa-beat")

        header_tabs = [[i, " ", arrow_down] if j == True else [i, " "] 
                       for i,j in zip(data["options"], data["sub_headings"])]
        # fa-duotone fa-square-chevron-down
        tabs = [dbc.Col(html.H6(i), id=i[0]+"2", class_name="tab_name", width="auto") 
                for i in header_tabs]
        
        return dbc.Row(tabs, class_name="mx-auto")


    
    
   
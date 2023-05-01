import dash 
from dash import html, dcc
import dash_bootstrap_components as dbc
from helper_functions import *


def build_wings_spiritual():

    return html.Div([
        dbc.Row(html.H1("Spiritual Wing"), className="wings_header"),
        dbc.Row(class_name="wings_spiritual", children=[
            dbc.Col(build_carousel(), **width_dict_multi(12, 12, 6)), 
            dbc.Col(_build_content(), **width_dict_multi(12, 12, 6))
        ]),
        html.Br(),
        dbc.Row([
            dbc.Col(_build_cards("Vedams"), **width_dict_multi(6, 3, 3)),
            dbc.Col(_build_cards("Trainings"), **width_dict_multi(6, 3, 3)),
            dbc.Col(_build_cards("Some Topic"), **width_dict_multi(6, 3, 3)),
            dbc.Col(_build_cards("Topic 4"), **width_dict_multi(6, 3, 3)),
        ])
    ])



def build_carousel():
    carousel = html.Div(id="spiritual_carousel_div", children=[
        dbc.Carousel(
            items=[
                {"key": "1", "src": "/assets/images/image1.png"},
                {"key": "2", "src": "/assets/images/image2.png"},
                {"key": "3", "src": "/assets/images/image3.png"},
            ],
            interval=2000,
            ride="carousel",
        ), 
    ])
    return carousel

def _build_content():
    return html.Div(className="wings_content", children=[
        html.H2("Spiritual Wing"),
        html.P('''
        As the tree grows, the roots must also grow inwards. The growth of the tree is 
        dependent on the roots inside the ground. Thus, the spiritual wing undertakes 
        activities that are targeted to arouse inspiration and inward vision with a view 
        to developing the urge to connect with the inner core and obtaining clarification 
        to doubts or answers to questions related to spiritual progress of the member. 
        It helps to nurture the inner self and awakening the inherent divinity. The 
        activities undertaken by the spiritual wing include the following:
        '''
        ),

        html.Ul(className="list-style-type:circle", children=[
            html.Li("Bhajan"),
            html.Li("Nagarsankeertan"),
            html.Li("Study Circles"),
            html.Li("Naamsmarana"),
            html.Li("Japa and Meditation"),
            html.Li("Spiritual class or lectures"),
        ])
    ])


def _build_cards(name):
    return html.Div(className="wings_card", children=[
        html.H1(name)
    ])
    # return dbc.Card(class_name="wings_card", children=[
    #     dbc.CardImg(src=dash.get_asset_url("images/image1.png"), top=True),
    #     dbc.CardImgOverlay(
    #         dbc.CardBody(
    #             html.H4(name),
    #         ),
    #     )
    # ])




def build_left_panel():
    return html.Div(className="tabs_group", children=[
        html.Div("Vedams", className="left_panel_tab",),
        html.Div("Trainings", className="left_panel_tab",),
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
    




    
    

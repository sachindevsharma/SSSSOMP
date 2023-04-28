
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from helper_functions import build_figure


def build_tab1_content():
    layout = html.Div(id = "Tab1_div",children=[
        build_carousel(),
        html.Br(),
        build_numbers_div(),
        build_buttons_div()
    ])
    return layout

def build_carousel():
    carousel = html.Div(id="carousel_div", children=[
        dbc.Carousel(
            items=[
                {"key": "1", "src": "/assets/images/image1.png"},
                {"key": "2", "src": "/assets/images/image2.png"},
                {"key": "3", "src": "/assets/images/image3.png"},
            ],
            interval=2000,
            ride="carousel",
        ), 
        html.Br()
    ])

    return carousel

def build_numbers_div():
    return html.Div([
        

        html.H1("SSSSOMP by Numbers", className="center"), 
        html.Br(),
        dbc.Row([
            dbc.Col(width=2),
            dbc.Col([
                dbc.Row(class_name="number_counter"),
                dbc.Row("Districts")
            ]),
            dbc.Col([
                dbc.Row(class_name="number_counter"),
                dbc.Row("Samitis")
            ]),
            dbc.Col([
                dbc.Row(class_name="number_counter"),
                dbc.Row("Bhajan Mandalis")
            ]),
        ]),
        html.Br(),
        html.Div([
            dcc.Interval(
                id='interval-component',
                interval=1,  # update every 100 milliseconds
                n_intervals=0
            ),
            html.Div(0,
                id='number-counter',
                style={'fontSize': 50}
            )
        ])
    ])

def build_buttons_div():
    return html.Div([
        # html.Img(src="assets/images/sarvadharma_image.jfif"),
        html.H5('यहाँ केवल एक ही धर्म है , प्रेम का धर्म ', className="center"),
        html.H5('यहाँ केवल एक ही जाति है , मानवता की जाति ', className="center"),
        html.H5('यहाँ केवल एक ही भाषा है , ह्रदय की भाषा ।', className="center"),
        html.H5('यहाँ केवल एक ही भगवान हैं ,वे सर्वत्र विद्यमान हैं ।', className="center"),
    ])



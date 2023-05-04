
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


def build_home_page():
    layout = html.Div(id = "Tab1_div",children=[
        build_carousel(),
        build_numbers_div(),
        build_buttons_div(),
        add_quotes(),
        build_activities_div()
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
            dbc.Col([html.H1(34, className="numbers"), dbc.Row("Districts", className="center")]),
            dbc.Col([html.H1(223, className="numbers"), dbc.Row("Samitis", className="center")]),
            dbc.Col([html.H1(250, className="numbers"), dbc.Row("Bhajan Mandalis", className="center")]),
            dbc.Col([html.H1(className="number_counter center"), dbc.Row("Number Counter", className="center")]),
        ]),
        html.Br(),
    ])

def build_buttons_div():
    return html.Div([
        # html.Img(src="assets/images/sarvadharma_image.jfif"),
        html.H5('यहाँ केवल एक ही धर्म है , प्रेम का धर्म ', className="center"),
        html.H5('यहाँ केवल एक ही जाति है , मानवता की जाति ', className="center"),
        html.H5('यहाँ केवल एक ही भाषा है , ह्रदय की भाषा ।', className="center"),
        html.H5('यहाँ केवल एक ही भगवान हैं ,वे सर्वत्र विद्यमान हैं ।', className="center"),
        html.Br(),

    ])

def add_quotes():
    return html.Div(className="quotes_div", children=[
        html.H3("Hands that serve are holier than the lips that prey"),
        html.Br(),

    ])

def build_activities_div():
    img1 = "https://ssssoindia.org/wp-content/uploads/2020/08/vj-program-1170x1170.png"
    img2 = "https://wpstatic.ssssoindia.org/wp-content/uploads/2022/04/22170444/disaster-management-1.jpg"
    img3 = "https://wpstatic.ssssoindia.org/wp-content/uploads/2022/04/22161159/swachhate-updatedimage.jpg"

    return html.Div(className="home_activities", children=[
        html.Br(),
        dbc.Row(html.H1("Our Activities", className="header"), ),
        dbc.Row([
            dbc.Col(html.Img(src=img1), width=4),
            dbc.Col(html.Img(src=img2), width=4),
            dbc.Col(html.Img(src=img3), width=4)
        ]),
        html.Br(),
    ])

from dash import html, dcc

def build_tab5_content():
    return html.Div(id="news_div", children=[
        html.Iframe(src="https://ssssoindia.org/wings-activities/", 
                     style={"height": "100vh", "width": "100%"})
                    
    ])


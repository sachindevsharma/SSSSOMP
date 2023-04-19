from dash import html, dcc, dash_table, Input, State, Output



def callbacks_header_bar(app):
     for i in ["", 1, 2, 3, 11, 22]:
        @app.callback(
                Output(f"navbar-collapse{i}", "is_open"),
                [Input(f"navbar-toggler{i}", "n_clicks")],
                [State(f"navbar-collapse{i}", "is_open")],
            )
        def toggle_navbar_collapse(n, is_open):
            if n:
                return not is_open
            return is_open



    
    
   
import dash
import dash_bootstrap_components as dbc

print(dir(dash))

from layouts import Layout, register_app_pages
from callbacks import Callbacks
from apis import AppAPIs

# from sql import MongoConnector
# client = MongoConnector().connect()

app = dash.Dash(__name__, 
           update_title=None,
           title='SSSSOMP', 
           external_stylesheets=[dbc.themes.BOOTSTRAP, 
                                 'https://use.fontawesome.com/releases/v6.2.1/css/all.css'], 
            meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
           pages_folder="layouts",
           use_pages=True,
           prevent_initial_callbacks=True)

app.config["suppress_callback_exceptions"] = True
server = app.server 

# print(dash.DASH_URL_BASE_PATHNAME)
AppAPIs(server)
# Enable Whitenoise for serving static files from Heroku (the /static folder is seen as root by Heroku) 
# server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/') 

register_app_pages()
app.layout = Layout()
Callbacks()


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
import pandas as pd
from dash import Dash , html , dcc, callback ,Output,Input
import plotly.express as px 
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')


app =  Dash(__name__)

app.layout =  html.Div([
    html.H1(children='Title of the Dash APP',style={'textAlign': 'center'}),
    html.H2(children='Title of the Dash APP',style={'textAlign': 'center'}),

    dcc.Dropdown(df.country.unique(),'Cananda',id='dropdown-selection'),
    dcc.Dropdown(df.lifeExp.unique(),'28.801',id='dropdown-selection-1'),

    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content','figure'),
    Input('dropdown-selection','value')
    
)

def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x ='year',y='pop')
if __name__=='__main__':
    app.run_server(debug=True,port=4000)

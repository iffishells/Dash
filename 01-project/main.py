from dash import Dash, html, dcc
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import yfinance as yf

# Download Bitcoin price data from 2014 to 2022
btc_data = yf.download(tickers='BTC-USD', start='2014-01-01', end='2022-12-31')
btc_data.reset_index(inplace=True)

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign': 'center'}),
    dcc.Dropdown(options=[
        {'label': 'Hourly', 'value': 'H'},
        {'label': 'Daily', 'value': 'D'},
        {'label': 'Weekly', 'value': 'W'},
        {'label': 'Monthly', 'value': 'M'},
        {'label': 'Yearly', 'value': 'Y'}
    ], value='D', id='resampling-dropdown'),
    dcc.Graph(id='graph-content')
])

@app.callback(
    Output('graph-content', 'figure'),
    Input('resampling-dropdown', 'value')
)
def update_graph(resampling):
    btc_data_resampled = btc_data.resample(resampling, on='Date').mean().reset_index()
    return px.line(btc_data_resampled, x='Date', y='Close')

if __name__ == '__main__':
    app.run_server(debug=True)

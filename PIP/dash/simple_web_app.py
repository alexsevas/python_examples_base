# conda activate allpy310

import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Создание приложения
app = dash.Dash(__name__)

# Данные
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# Создание графика
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Layout
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Запуск сервера
if __name__ == '__main__':
    #app.run_server(debug=True)
    #dash.exceptions.ObsoleteAttributeException: app.run_server has been replaced by app.run
    app.run(debug=True)

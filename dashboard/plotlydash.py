from dash import Dash, html, dash_table, dcc
from dash.dependencies import Input, Output
import requests
import os
from io import StringIO
import pandas as pd
import plotly.express as px

# Initialize the app
app = Dash()

# Используем имя сервиса из docker-compose
API_URL = 'http://django:8000/api/cpus/'
# API_URL = 'http://127.0.0.1:8000/api/cpus/'

def fetch_hardware_data():
    try:
        print(f"Попытка подключения к: {API_URL}")
        response = requests.get(API_URL, params={'format': 'csv'}, timeout=10)
        response.raise_for_status()
        
        df = pd.read_csv(StringIO(response.text))
        # Преобразуем дату в datetime для лучшей сортировки
        df['release_date'] = pd.to_datetime(df['release_date'])
        print(f"Успешно загружено {len(df)} записей")
        return df
        
    except Exception as e:
        print(f"Ошибка подключения: {str(e)}")
        return pd.DataFrame()

# Загружаем данные для использования в layout и колбэках
df = fetch_hardware_data()

# App layout
app.layout = [
    html.Div(children='Список процессоров'),
    dcc.Dropdown(
        id='graph-dropdown',
        options=[{'label': column, 'value': column} for column in df.columns],
        value='vendor',  # Значение по умолчанию
        placeholder="Выберите характеристику"
    ),
    dcc.Graph(
        id='graph'
    ),
    dash_table.DataTable(
        id='data-table',
        data=df.to_dict('records'),
        columns=[{"name": col, "id": col} for col in df.columns],
        page_size=30,  # Размер страницы (чтобы точно была пагинация)
        style_table={'overflowX': 'auto'},
        page_action='native'  # Включаем встроенную пагинацию Dash
    )
]

# Data update callback
@app.callback(
    Output('graph', 'figure'),
    [Input('graph-dropdown', 'value')]
)
def update_graph(selected_column):
    fig = px.histogram(df, x=selected_column, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

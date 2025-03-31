from dash import Dash, html, dash_table, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('http://127.0.0.1:8000/api/cpus/?format=csv')

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='Список процессоров'),
    dcc.Dropdown(
        id='graph-dropdown',
        options=[{'label': column, 'value': column} for column in df.columns],
        value = 'vendor',
        placeholder="Выберите характеристику"
    ),
    dcc.Graph(
        id='graph'
    ),
    dash_table.DataTable(
        data=df.to_dict('records'), page_size=30
    ),
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
    app.run(debug=True)

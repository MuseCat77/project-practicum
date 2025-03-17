from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('http://127.0.0.1:8000/api/cpus/?format=csv')

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='Список процессоров'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=30),
    dcc.Graph(figure=px.histogram(df, x='vendor', y='die_size', histfunc='avg'))
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

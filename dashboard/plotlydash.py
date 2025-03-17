from dash import Dash, html, dash_table
import pandas as pd

# Incorporate data
df = pd.read_csv('http://127.0.0.1:8000/api/cpus/?format=csv')

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='Список процессоров'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

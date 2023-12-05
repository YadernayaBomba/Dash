# data.py веб-приложение
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import dash_table

# Считываем данные из CSV-файла
file_path = 'C:/Users/glebc/OneDrive/Рабочий стол/1.csv'
df = pd.read_csv(file_path)

# Преобразуем столбец 'Date' в формат datetime
df['Date'] = pd.to_datetime(df['Date'])

# Создаем веб-приложение
app = dash.Dash(__name__)

# Определяем макет
app.layout = html.Div([
    html.H1('Пользовательская активность', style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='date-dropdown',
        options=[
            {'label': 'Месяц', 'value': 'M'},
            {'label': 'Квартал', 'value': 'Q'},
            {'label': 'Год', 'value': 'Y'}
        ],
        value='M',
        clearable=False,
        style={'width': '23%', 'margin': '0 auto'}
    ),
    dcc.Graph(id='time-series'),
    dcc.Graph(id='pie-chart'),
    dcc.Graph(id='histogram'),
    dcc.Graph(id='scatter-plot'),
    html.Div(id='data-table')
], style={'padding': '20px'})

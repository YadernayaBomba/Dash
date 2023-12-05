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
    html.H1('Продажа нефтепродуктов', style={'textAlign': 'center'}),
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
    html.Hr(),
    dcc.Graph(id='pie-chart'),
    html.Hr(),
    dcc.Graph(id='histogram'),
    html.Hr(),
    dcc.Graph(id='scatter-plot'),
    html.Hr(),
    html.Div(id='data-table'),
    html.Hr(),
], style={'padding': '20px'})

# Определяем логику взаимодействия
@app.callback(
    [Output('time-series', 'figure'),
     Output('pie-chart', 'figure'),
     Output('histogram', 'figure'),
     Output('scatter-plot', 'figure'),
     Output('data-table', 'children')],
    [Input('date-dropdown', 'value')]
)

def update_figures(selected_date):
    # Логика обновления данных и графиков
    filtered_df = df.resample(selected_date, on='Date').sum().reset_index()

    # Создание временного ряда с помощью Plotly
    time_series_figure = px.line(filtered_df, x='Date', y='Price (rub)', title='График временного ряда')

    # Создание круговой диаграммы с помощью Plotly
    pie_chart_figure = px.pie(df, names='Product', title='Распределение продукции, %')

    # Создание гистограммы с помощью Plotly
    histogram = px.histogram(df, x='Product', title='Распределение продукции, шт')

    # Создание графика рассеивания с помощью Plotly
    scatter_plot_figure = px.scatter(df, x='Gas station number', y='Date', title='График рассеяния')

    # Создание таблицы с данными
    data_table = dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        page_size=10,  # Количество строк на странице
        style_table={'height': '300px', 'overflowY': 'auto'},
        style_cell={
            'textAlign': 'left',
            'padding': '10px',
            'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
            'whiteSpace': 'normal'
        },
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        }
    )

    return time_series_figure, pie_chart_figure, histogram, scatter_plot_figure, data_table


# Запускаем веб-приложение
if __name__ == '__main__':
    app.run_server(debug=True)

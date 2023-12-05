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

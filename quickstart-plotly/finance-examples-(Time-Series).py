"""
https://plot.ly/python/time-series/

Временные ряды могут быть представлены с помощью plotly.express функций (px.line,px.scatter)
или plotly.graph_objects объектов диаграмм (go.Scatter).
Дополнительные примеры таких диаграмм см. В документации по линейным и точечным диаграммам.

Графически автоматически устанавливает тип оси в формат даты, когда соответствующие
данные являются либо строками даты в формате ISO, либо если они являются столбцом
date pandas или массивом datetime NumPy.
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
df = pd.read_csv('./data/finance-charts-apple.csv')

fig = px.line(df, x='Date', y='AAPL.High')
fig.show()

fig = go.Figure([go.Scatter(x=df['Date'], y=df['AAPL.High'])])
fig.show()

import datetime

x = [datetime.datetime(year=2013, month=10, day=4),
     datetime.datetime(year=2013, month=11, day=5),
     datetime.datetime(year=2013, month=12, day=6)]

fig = go.Figure(data=[go.Scatter(x=x, y=[1, 3, 6])])
# Use datetime objects to set xaxis range
fig.update_layout(xaxis_range=[datetime.datetime(2013, 10, 17),
                               datetime.datetime(2013, 11, 20)])
fig.show()

fig = go.Figure()
fig.add_trace(go.Scatter(
                x=df.Date,
                y=df['AAPL.High'],
                name="AAPL High",
                line_color='deepskyblue',
                opacity=0.8))

fig.add_trace(go.Scatter(
                x=df.Date,
                y=df['AAPL.Low'],
                name="AAPL Low",
                line_color='dimgray',
                opacity=0.8))

# Use date string to set xaxis range
fig.update_layout(xaxis_range=['2016-07-01','2016-12-31'],
                  title_text="Manually Set Date Range")
fig.show()

fig = go.Figure()
fig.add_trace(go.Scatter(x=df.Date, y=df['AAPL.High'], name="AAPL High",
                         line_color='deepskyblue'))

fig.add_trace(go.Scatter(x=df.Date, y=df['AAPL.Low'], name="AAPL Low",
                         line_color='dimgray'))

fig.update_layout(title_text='Time Series with Rangeslider',
                  xaxis_rangeslider_visible=True)
fig.show()




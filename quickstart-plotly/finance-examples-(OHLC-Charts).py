"""
https://plot.ly/python/ohlc-charts/
График OHLC (для open, high, low и close) - это стиль финансового графика,
описывающего открытые, высокие, низкие и закрытые значения для заданной
координаты (наиболее вероятного времени).
Кончики линий представляют low собой high значения и, а горизонтальные сегменты
open close- значения И. Точки выборки, в которых значение close больше (меньше),
чем значение open, называются возрастающими (убывающими).
По умолчанию увеличивающиеся элементы отображаются зеленым цветом,
а уменьшающиеся-красным.

Документация https://plot.ly/python/reference/#ohlc
"""
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
df = pd.read_csv('./data/finance-charts-apple.csv')

# 1) Simple OHLC Chart with Pandas
fig = go.Figure(data=go.Ohlc(x=df['Date'],
                    open=df['AAPL.Open'],
                    high=df['AAPL.High'],
                    low=df['AAPL.Low'],
                    close=df['AAPL.Close']))
fig.show()

# 2) OHLC Chart without Rangeslider
fig = go.Figure(data=go.Ohlc(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close']))
fig.update(layout_xaxis_rangeslider_visible=False)
fig.show()

# 3) Adding Customized Text and Annotations
fig = go.Figure(data=go.Ohlc(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close']))

fig.update_layout(
    title='The Great Recession',
    yaxis_title='AAPL Stock',
    shapes = [dict(
        x0='2016-12-09', x1='2016-12-09', y0=0, y1=1, xref='x', yref='paper',
        line_width=2)],
    annotations=[dict(
        x='2016-12-09', y=0.05, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='Increase Period Begins')]
)

fig.show()

# 4) Custom OHLC Colors
fig = go.Figure(data=[go.Ohlc(
    x=df['Date'],
    open=df['AAPL.Open'], high=df['AAPL.High'],
    low=df['AAPL.Low'], close=df['AAPL.Close'],
    increasing_line_color= 'cyan', decreasing_line_color= 'gray'
)])
fig.show()

# 5) Simple OHLC with datetime Objects
from datetime import datetime

open_data = [33.0, 33.3, 33.5, 33.0, 34.1]
high_data = [33.1, 33.3, 33.6, 33.2, 34.8]
low_data = [32.7, 32.7, 32.8, 32.6, 32.8]
close_data = [33.0, 32.9, 33.3, 33.1, 33.1]
dates = [datetime(year=2013, month=10, day=10),
         datetime(year=2013, month=11, day=10),
         datetime(year=2013, month=12, day=10),
         datetime(year=2014, month=1, day=10),
         datetime(year=2014, month=2, day=10)]

fig = go.Figure(data=[go.Ohlc(x=dates,
                          open=open_data, high=high_data,
                          low=low_data, close=close_data)])
fig.show()

# 6) Custom Hovertext
hovertext=[]
for i in range(len(df['AAPL.Open'])):
    hovertext.append('Open: '+str(df['AAPL.Open'][i])+'<br>Close: '+str(df['AAPL.Close'][i]))

fig = go.Figure(data=go.Ohlc(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'],
                text=hovertext,
                hoverinfo='text'))
fig.show()

# 7)

# 8)


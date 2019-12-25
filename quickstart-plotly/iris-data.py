import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = px.line(df, x='Date', y='AAPL.High')
fig.show()

fig = go.Figure()
fig.add_trace(go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
fig.show()

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", facet_col="species")
reference_line = go.Scatter(x=[2, 4],
                            y=[4, 8],
                            mode="lines",
                            line=go.scatter.Line(color="gray"),
                            showlegend=False)
fig.add_trace(reference_line, row=1, col=1)
fig.add_trace(reference_line, row=1, col=2)
fig.add_trace(reference_line, row=1, col=3)
fig.show()
"""
Dash - это библиотека Python с открытым исходным кодом, которая может помочь вам преобразовать 
сюжетные фигуры в реактивное веб-приложение. 
Ниже приведен простой пример панели инструментов, созданной с использованием Dash. 
Его исходный код может быть легко развернут в PaaS.
"""
from IPython.display import IFrame
ifr = IFrame(src= "https://dash-simple-apps.plotly.host/dash-timeseriesplot/",
       width="100%",
       height="750px",
       frameBorder="0")
ifr.show()

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

fig = go.Figure()
fig.add_trace(go.Scatter(x=df.Date, y=df['AAPL.High'], name="AAPL High",
                         line_color='deepskyblue'))

fig.add_trace(go.Scatter(x=df.Date, y=df['AAPL.Low'], name="AAPL Low",
                         line_color='dimgray'))

df['claps'].iplot(kind='hist', xTitle='claps',
                  yTitle='count', title='Claps Distribution')

fig.update_layout(title_text='Временные ряды с Rangeslider',
                  xaxis_rangeslider_visible=True)
fig.show()

"""
https://plot.ly/python/funnel-charts/

Воронкообразные диаграммы часто используются для представления данных на
различных этапах бизнес-процесса. Это важный механизм в бизнес-аналитике для
выявления потенциальных проблемных областей процесса.
Например, он используется для наблюдения за доходом или убытком в процессе продаж
для каждого этапа и отображает значения, которые постепенно уменьшаются.
Каждый этап иллюстрируется как процент от общего числа всех значений.
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# 1) Basic Funnel Plot with plotly.express
data =  dict(
    number= [ 39 ,  27.4 ,  20.6 ,  11 ,  2 ],
    stage= ["Посещения сайта",  "Загрузки",  "Потенциальные клиенты",  "Запрос о цене",
            "Выставлен счёт"])
fig =  px.funnel(data,  x= 'number',  y= 'stage', title='Основная воронка продаж')
fig.show()

# 2) Stacked Funnel Plot with plotly.express
stages = ["Посещения сайта", "Загрузки", "Потенциальные клиенты",
         "Запрос о цене",
         "Выставлен счёт"]
df_mtl = pd.DataFrame(dict(number=[39, 27.4, 20.6, 11, 3], stage=stages))
df_mtl['office'] = 'Санкт-Перербург'
df_toronto = pd.DataFrame(dict(number=[52, 36, 18, 14, 5], stage=stages))
df_toronto['office'] = 'Москва'
df = pd.concat([df_mtl, df_toronto], axis=0)
fig = px.funnel(df, x='number', y='stage', color='office', title='Сравнительная воронка продаж')
fig.show()

# 3) Basic Funnel Chart with graph_objects trace go.Funnel
from plotly import graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Посещения сайта",  "Загрузки",  "Потенциальные клиенты",  "Запрос о цене", "Выставлен счёт"],
    x = [39, 27.4, 20.6, 11, 2]))

fig.show()

# 4) Setting Marker Size and Color
fig = go.Figure(go.Funnel(
    y = ["Посещения сайта",  "Загрузки",  "Потенциальные клиенты",  "Запрос о цене", "Выставлен счёт"],
    x = [39, 27.4, 20.6, 11, 2],
    textposition = "inside",
    textinfo = "value+percent initial",
    opacity = 0.65, marker = {"color": ["deepskyblue", "lightsalmon", "tan", "teal", "silver"],
    "line": {"width": [4, 2, 2, 3, 1, 1], "color": ["wheat", "wheat", "blue", "wheat", "wheat"]}},
    connector = {"line": {"color": "royalblue", "dash": "dot", "width": 3}})
    )

fig.show()

# 5) Stacked Funnel Plot with go.Funnel
fig = go.Figure()

fig.add_trace(go.Funnel(
    name = 'Montreal',
    y = ["Посещения сайта", "Загрузки", "Потенциальные клиенты", "Запрос цены"],
    x = [120, 60, 30, 20],
    textinfo = "value+percent initial"))

fig.add_trace(go.Funnel(
    name = 'Toronto',
    orientation = "h",
    y = ["Посещения сайта", "Загрузки", "Потенциальные клиенты", "Запрос цены", "Выставлен счёт"],
    x = [100, 60, 40, 30, 20],
    textposition = "inside",
    textinfo = "value+percent previous"))

fig.add_trace(go.Funnel(
    name = 'Vancouver',
    orientation = "h",
    y = ["Посещения сайта", "Загрузки", "Потенциальные клиенты", "Запрос цены", "Выставлен счёт", "Завершение"],
    x = [90, 70, 50, 30, 10, 5],
    textposition = "outside",
    textinfo = "value+percent total"))

fig.show()


# 6) Basic Area Funnel Plot with plotly.express
fig = px.funnel_area(names=["The 1st","The 2nd", "The 3rd", "The 4th", "The 5th"],
                    values=[5, 4, 3, 2, 1])
fig.show()

# 7) Basic Area Funnel Plot with go.Funnelarea
fig = go.Figure(go.Funnelarea(
    text = ["The 1st","The 2nd", "The 3rd", "The 4th", "The 5th"],
    values = [5, 4, 3, 2, 1]
    ))
fig.show()

# 8) Set Marker Size and Color in Area Funnel Plots
fig = go.Figure(go.Funnelarea(
      values = [5, 4, 3, 2, 1], text = ["The 1st","The 2nd", "The 3rd", "The 4th", "The 5th"],
      marker = {"colors": ["deepskyblue", "lightsalmon", "tan", "teal", "silver"],
                "line": {"color": ["wheat", "wheat", "blue", "wheat", "wheat"], "width": [0, 1, 5, 0, 4]}},
      textfont = {"family": "Old Standard TT, serif", "size": 13, "color": "black"}, opacity = 0.65))
fig.show()

# 9) Multiple Area Funnels
fig = go.Figure()

fig.add_trace(go.Funnelarea(
    scalegroup = "first", values = [500, 450, 340, 230, 220, 110], textinfo = "value",
    title = {"position": "top center", "text": "Sales for Sale Person A in U.S."},
    domain = {"x": [0, 0.5], "y": [0, 0.5]}))

fig.add_trace(go.Funnelarea(
    scalegroup = "first", values = [600, 500, 400, 300, 200, 100], textinfo = "value",
    title = {"position": "top center", "text": "Sales of Sale Person B in Canada"},
    domain = {"x": [0, 0.5], "y": [0.55, 1]}))

fig.add_trace(go.Funnelarea(
    scalegroup = "second", values = [510, 480, 440, 330, 220, 100], textinfo = "value",
    title = {"position": "top left", "text": "Sales of Sale Person A in Canada"},
    domain = {"x": [0.55, 1], "y": [0, 0.5]}))

fig.add_trace(go.Funnelarea(
            scalegroup = "second", values = [360, 250, 240, 130, 120, 60],
            textinfo = "value", title = {"position": "top left", "text": "Sales of Sale Person B in U.S."},
            domain = {"x": [0.55, 1], "y": [0.55, 1]}))

fig.update_layout(
            margin = {"l": 200, "r": 200}, shapes = [
            {"x0": 0, "x1": 0.5, "y0": 0, "y1": 0.5},
            {"x0": 0, "x1": 0.5, "y0": 0.55, "y1": 1},
            {"x0": 0.55, "x1": 1, "y0": 0, "y1": 0.5},
            {"x0": 0.55, "x1": 1, "y0": 0.55, "y1": 1}])

fig.show()




# 6) Basic Area Funnel Plot with plotly.express






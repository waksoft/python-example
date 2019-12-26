# https://plot.ly/python/waterfall-charts/

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
df = pd.read_csv('./data/finance-charts-apple.csv')

# 1) Simple Waterfall Chart
fig = go.Figure(go.Waterfall(
    name = "20", orientation = "v",
    measure = ["relative", "relative", "total", "relative", "relative", "total"],
    x = ["Продажи", "Консультации", "Чистый доход", "Покупки", "Прочие расходы", "Прибыль до вычета налога"],
    textposition = "outside",
    text = ["+60", "+80", "", "-40", "-20", "Total"],
    y = [60, 80, 0, -40, -20, 0],
    connector = {"line":{"color":"rgb(63, 63, 63)"}},
))

fig.update_layout(
        title = "Отчет о прибылях и убытках 2018",
        showlegend = True
)

fig.show()

# 2) Multi Category Waterfall Chart
fig = go.Figure()

fig.add_trace(go.Waterfall(
    x = [["2016", "2017", "2017", "2017", "2017", "2018", "2018", "2018", "2018"],
         ["начало", "q1", "q2", "q3", "итого", "q1", "q2", "q3", "итого"]],
    measure = ["absolute", "relative", "relative", "relative", "total", "relative", "relative", "relative", "total"],
    y = [1, 2, 3, -1, None, 1, 2, -4, None],
    base = 1000
))

fig.add_trace(go.Waterfall(
    x = [["2016", "2017", "2017", "2017", "2017", "2018", "2018", "2018", "2018"],
         ["начало", "q1", "q2", "q3", "итого", "q1", "q2", "q3", "итого"]],
    measure = ["absolute", "relative", "relative", "relative", "total", "relative", "relative", "relative", "total"],
    y = [1.1, 2.2, 3.3, -1.1, None, 1.1, 2.2, -4.4, None],
    base = 1000
))

fig.update_layout(
    waterfallgroupgap = 0.5,
)

fig.show()

# 3) Setting Marker Size and Color
fig = go.Figure(go.Waterfall(
    x = [["2016", "2017", "2017", "2017", "2017", "2018", "2018", "2018", "2018"],
       ["начало", "q1", "q2", "q3", "итого", "q1", "q2", "q3", "итого"]],
    measure = ["absolute", "relative", "relative", "relative", "total", "relative", "relative", "relative", "total"],
    y = [10, 20, 30, -10, None, 10, 20, -40, None], base = 300,
    decreasing = {"marker":{"color":"Maroon", "line":{"color":"red", "width":2}}},
    increasing = {"marker":{"color":"Teal"}},
    totals = {"marker":{"color":"deep sky blue", "line":{"color":'blue', "width":3}}}
))

fig.update_layout(title = "Отчёт о прибылях и убытках", waterfallgap = 0.3)

fig.show()

# 4) Horizontal Waterfall Chart
fig = go.Figure(go.Waterfall(
    name = "2018", orientation = "h", measure = ["relative", "relative", "relative", "relative", "total", "relative",
                                              "relative", "relative", "relative", "total", "relative", "relative", "total", "relative", "total"],
    y = ["Продажи", "Консалтинг", "Техническое обслуживание", "Прочие доходы", "Чистый доход", "Purchases", "Material expenses",
       "Расходы на персонал", "Прочие расходы", "Операционный доход", "Инвестиционный доход", "Финансовые доходы",
       "Прибыль до вычета налога", "Подоходный налог (15%)", "Прибыль после уплаты налогов"],
    x = [375, 128, 78, 27, None, -327, -12, -78, -12, None, 32, 89, None, -45, None],
    connector = {"mode":"between", "line":{"width":4, "color":"rgb(0, 0, 0)", "dash":"solid"}}
))

fig.update_layout(title = "Отчёт о прибылях и убытках 2018")

fig.show()

"""
https://plot.ly/python/indicator/
В этом уроке мы вводим новую трассировку под названием "Индикатор".
Целью " индикатора "является визуализация одного значения, указанного атрибутом" value".
Для представления этого значения доступны три различных визуальных
элемента: число, Дельта и датчик. Любую их комбинацию можно задать с помощью атрибута
"mode". Атрибуты верхнего уровня являются:
значение: значение для визуализации
режим: какие визуальные элементы рисовать
align: как выровнять число и дельту (слева, по центру, справа)
домен: экстент фигуры
Затем мы можем настроить 3 различных визуальных элемента через их соответствующий контейнер:

число-это просто представление числа в тексте. Он имеет атрибуты:
valueformat: для форматирования числа
префикс: строка перед номером
суффикс: строка после числа
шрифт.(семья / размер): для управления шрифтом
"Дельта" просто отображает разницу между значением по отношению к ссылке. Он имеет атрибуты:
ссылка: число для сравнения значения с
относительный: является ли это различие абсолютным или относительным
valueformat: для форматирования дельты
(увеличение|уменьшение).цвет: цвет, который будет использоваться для положительной или убывающей дельты
(увеличение|уменьшение).символ: символ, отображаемый слева от дельты
шрифт.(семья / размер): для управления шрифтом
позиция: положение относительно ' числа '( либо сверху, слева, снизу, справа)
"""

import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Indicator(
    value =  200,
    delta =  {'reference':  160},
    gauge =  {
        'axis':  {'visible':  False}},
    domain =  {'row':  0, 'column':  0}))

fig.add_trace(go.Indicator(
    value =  120,
    gauge =  {
        'shape':  "bullet",
        'axis' :  {'visible':  False}},
    domain =  {'x':  [0.05,  0.5 ],  'y':  [ 0.15 ,  0.35 ]}))

fig.add_trace(go.Indicator(
    mode =  "number+delta",
    value =  300,
    domain =  { 'row':  0,  'column':  1 }))

fig.add_trace(go.Indicator(
    mode =  "delta",
    value =  40,
    domain =  { 'row':  1,  'column':  1}))

fig.update_layout(
    grid =  {'rows':  2,  'columns':  2,  'pattern': "independent"},
    template =  {'data' :  {'indicator':  [{
        'title':  {'text':  "Speed"},
        'mode' : "number+delta+gauge",
        'delta' :  {'reference':  90 }}]
                         }})
fig.show()

# 2) A Single Angular Gauge Chart
fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 450,
    title = {'text': "Speed"},
    domain = {'x': [0, 1], 'y': [0, 1]}
))

fig.show()

# 3) Bullet Gauge
fig = go.Figure(go.Indicator(
    mode = "number+gauge+delta",
    gauge = {'shape': "bullet"},
    delta = {'reference': 300},
    value = 220,
    domain = {'x': [0.1, 1], 'y': [0.2, 0.9]},
    title = {'text': "Avg order size"}))

fig.show()

# 4) Showing Information above Your Chart
fig = go.Figure(go.Indicator(
    mode = "number+delta",
    value = 492,
    delta = {"reference": 512, "valueformat": ".0f"},
    title = {"text": "Users online"},
    domain = {'y': [0, 1], 'x': [0.25, 0.75]}))

fig.add_trace(go.Scatter(
    y = [325, 324, 405, 400, 424, 404, 417, 432, 419, 394, 410, 426, 413, 419, 404, 408, 401, 377, 368, 361, 356, 359, 375, 397, 394, 418, 437, 450, 430, 442, 424, 443, 420, 418, 423, 423, 426, 440, 437, 436, 447, 460, 478, 472, 450, 456, 436, 418, 429, 412, 429, 442, 464, 447, 434, 457, 474, 480, 499, 497, 480, 502, 512, 492]))

fig.update_layout(xaxis = {'range': [0, 62]})
fig.show()

# 5) Data Cards / Big Numbers
fig = go.Figure(go.Indicator(
    mode = "number+delta",
    value = 400,
    number = {'prefix': "$"},
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig.update_layout(paper_bgcolor = "lightgray")

fig.show()

# 6) It's possible to display several numbers
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = 200,
    domain = {'x': [0, 0.5], 'y': [0, 0.5]},
    delta = {'reference': 400, 'relative': True, 'position' : "top"}))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = 350,
    delta = {'reference': 400, 'relative': True},
    domain = {'x': [0, 0.5], 'y': [0.5, 1]}))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = 450,
    title = {"text": "Accounts<br><span style='font-size:0.8em;color:gray'>Subtitle</span><br><span style='font-size:0.8em;color:gray'>Subsubtitle</span>"},
    delta = {'reference': 400, 'relative': True},
    domain = {'x': [0.6, 1], 'y': [0, 1]}))

fig.show()

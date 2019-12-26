"""
https://plot.ly/python/gauge-charts/

Документация https://plot.ly/python/reference/#indicator
"""

import plotly.graph_objects as go

fig = go.Figure( go.Indicator(
    mode =  "gauge+number",
    value =  270 ,
    domain =  { 'x':  [ 0,  1],  'y':  [ 0,  1]},
    title =  { 'text': "Speed"}))

fig.show()

# 2) Add Steps, Threshold, and Delta
fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 450,
    mode = "gauge+number+delta",
    title = {'text': "Speed"},
    delta = {'reference': 380},
    gauge = {'axis': {'range': [None, 500]},
             'steps' : [
                 {'range': [0, 250], 'color': "lightgray"},
                 {'range': [250, 400], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

fig.show()

# 3) Custom Gauge Chart
fig = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = 420,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Speed", 'font': {'size': 24}},
    delta = {'reference': 400, 'increasing': {'color': "RebeccaPurple"}},
    gauge = {
        'axis': {'range': [None, 500], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "darkblue"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 250], 'color': 'cyan'},
            {'range': [250, 400], 'color': 'royalblue'}],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 490}}))

fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})

fig.show()

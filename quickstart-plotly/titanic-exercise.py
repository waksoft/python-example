import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("./data/train.csv")
print(df)

#labels
lab = df["Survived"].value_counts().keys().tolist()
#values
val = df["Survived"].value_counts().values.tolist()
trace = go.Pie(labels=lab,
                values=val,
                marker=dict(colors=['red']),
                # Seting values to
                hoverinfo="value"
              )
data = [trace]
layout = go.Layout(title="Распределение выживших")
fig = go.Figure(data = data,layout = layout)
fig.show()

# defining data
trace = go.Histogram(x=df['Age'],
                     nbinsx=40,
                     histnorm='percent')
data = [trace]
# defining layout
layout = go.Layout(title="Распределение возраста")
# defining figure and plotting
fig = go.Figure(data = data,layout = layout)
fig.show()

#defining data
trace = go.Scatter(x = df['Age'],
                   y=df['Fare'],
                   text = df['Survived'], mode='markers')
data=[trace]
#defining layout
layout = go.Layout(title='Диаграмма рассеивания Цена билета Vs Возраст',
                   xaxis=dict(title='Возраст'),
                   yaxis=dict(title='Цена билета'),
                   hovermode='closest')
#defining figure and plotting
figure = go.Figure(data=data,
                   layout=layout)
figure.show()

y=[]
fare = []
for i in list(df['Pclass'].unique()):
    result = df[df['Pclass'] == i]['Age'].mean()
    fares = df[df['Pclass'] == i]['Fare'].mean()
    y.append(result)
    fare.append(fares)

#defining data
trace = go.Bar(x = list(df['Pclass'].unique()),y=y,marker=dict(color=fare,colorscale='Viridis',showscale=True),text = fare)
data=[trace]
#defining layout
layout = go.Layout(title='Возраст/Цена билета vs Социального статуса',
                   xaxis=dict(title='Социальный статус'),
                   yaxis=dict(title='Возраст'),
                   hovermode='closest')
#defining figure and plotting
figure = go.Figure(data=data,layout=layout)
figure.show()

import plotly.figure_factory as ff
#defining data
a = df[df['Pclass'] == 1]['Fare']
b = df[df['Pclass'] == 2]['Fare']
c = df[df['Pclass'] == 3]['Fare']
hist_data = [a, b, c]
group_labels = ['Высокий', 'Средний', 'Низкий']
#defining fig and plotting
fig = ff.create_distplot(hist_data, group_labels,
                         bin_size=[1, 1, 1],
                         show_curve=False)
fig.update_layout(title_text='Распределение цены билета')
fig.show()

#defining data
data=[
    go.Scatter(x = df['Age'],
               y=df['Fare'],
               text=df['Pclass'],
               mode='markers',
               marker=dict(size=df['Pclass']*15,
                           color=df['Survived'],
                           showscale=True),
              )]
#defining layout
layout = go.Layout(title='Цена билета vs Возраста с Выжившими и социальным статусом',
                   xaxis=dict(title='Возраст'),
                   yaxis=dict(title='Цена билета'),
                   hovermode='closest')
#defining figure and plotting
figure = go.Figure(data=data,layout=layout)
figure.show()

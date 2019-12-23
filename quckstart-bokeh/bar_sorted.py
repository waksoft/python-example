"""
https://docs.bokeh.org/en/latest/docs/user_guide/categorical.html
"""
from bokeh.io import show, output_file
from bokeh.plotting import figure

output_file("../Data-Visualization-with-Python-master/workshop#8 (flesk+bokeh)/bar_sorted.html")

fruits = ['Яблоки', 'Груши', 'Нектарин', 'Сливы', 'Виноград', 'Клубника']
counts = [5, 3, 4, 2, 4, 6]

# sorting the bars means sorting the range factors
sorted_fruits = sorted(fruits, key=lambda x: counts[fruits.index(x)])

p = figure(x_range=sorted_fruits, plot_height=350, title="Фрукты (количество)",
           toolbar_location=None, tools="")

p.vbar(x=fruits, top=counts, width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)
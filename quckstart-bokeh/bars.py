from bokeh.io import show, output_file
from bokeh.plotting import figure

output_file("bars.html")

fruits = ['Яблоки', 'Груши', 'Нектарин', 'Сливы', 'Виноград', 'Клубника']
counts = [5, 3, 4, 2, 4, 6]

p = figure(x_range=fruits, plot_height=250, title="Фрукты (количество)",
           toolbar_location=None, tools="")

p.vbar(x=fruits, top=counts, width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)
# conda activate allpy310

# pip install bokeh

from bokeh.plotting import figure, show
from bokeh.io import output_file

# Подготавливаем данные
x_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_data = [6, 7, 5, 4, 5, 7, 8, 1, 5, 4]

# Задаем файл для вывода
output_file("result/line_chart.html")

# Создаем график
plot = figure(title="Simple Line Chart", x_axis_label="X-axis", y_axis_label="Y-axis")
plot.line(x_data, y_data, legend_label="Line", line_width=2)

# Показываем график
show(plot)

# conda activate allpy310

# pip install bokeh

from bokeh.plotting import figure, show
from bokeh.io import output_file

# Подготавливаем данные
x_data = [1, 2, 3, 4, 5]
y_data = [6, 7, 2, 4, 5]
sizes = [10, 20, 30, 40, 50]
colors = ['blue', 'red', 'green', 'purple', 'orange']

# Задаем файл для вывода
output_file("result/scatter_chart.html")

# Создаем график и добавляем аннотацию
plot = figure(title="Scatter Plot with Annotations")
plot.circle(x_data, y_data, size=sizes, color=colors, legend_label="Points")
plot.add_layout(plot.text(x=3, y=2, text=["Example Point"], text_color="black"))

# Показываем график
show(plot)

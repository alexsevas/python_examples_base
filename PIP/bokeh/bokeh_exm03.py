# conda activate allpy310

# pip install bokeh

from bokeh.plotting import figure, show
from bokeh.layouts import gridplot

# Данные для графиков
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# Создаем графики
plot1 = figure(title="Line Plot")
plot1.line(x, y, line_width=2)

plot2 = figure(title="Bar Plot")
plot2.vbar(x=x, top=y, width=0.5)

plot3 = figure(title="Circle Plot")
plot3.circle(x, y, size=10)

# Компонуем их в таблицу 2x2
grid = gridplot([[plot1, plot2], [plot3, None]])

# Показываем все вместе
show(grid)

# conda activate allpy310

# pip install matplotlib numpy

import matplotlib.pyplot as plt
import numpy as np

def plot_fractal_tree(ax, start_point, angle, depth, max_depth, length_factor=0.8, angle_change=20):
    if depth == max_depth:
        return

    x, y = start_point
    end_point = x + np.cos(np.radians(angle)), y + np.sin(np.radians(angle))
    ax.plot([x, end_point[0]], [y, end_point[1]], lw=max_depth - depth + 1, color='green')

    # Рекурсивный вызов для ветвления
    plot_fractal_tree(ax, end_point, angle - angle_change, depth + 1, max_depth)
    plot_fractal_tree(ax, end_point, angle + angle_change, depth + 1, max_depth)


fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')

initial_point = (0, 0)
initial_angle = 90
initial_depth = 0
max_depth = 10

plot_fractal_tree(ax, initial_point, initial_angle, initial_depth, max_depth)

plt.show()
# conda activate allpy310

# pip install matplotlib numpy

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Параметры сетки
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

# Параметры волн
frequency = 0.5
wavelength = 2
speed = 1.0
time = 0

# Функция для обновления волн
def update_wave(frame):
    global Z, time
    time += 0.1
    Z = np.sin(2 * np.pi * (np.sqrt(X**2 + Y**2) - speed * time) / wavelength) * np.exp(-0.1*np.sqrt(X**2 + Y**2))
    ax.clear()
    ax.set_zlim(-1, 1)
    ax.plot_surface(X, Y, Z, cmap='viridis')

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ani = FuncAnimation(fig, update_wave, frames=100, interval=50)

plt.show()

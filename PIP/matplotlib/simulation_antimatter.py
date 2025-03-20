# conda activate allpy310
# анимация не идет при запуске из-под PyCharm - запускай из консоли

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Параметры симуляции
num_particles = 50  # Число частиц вещества и антивещества
box_size = 10       # Размер области

# Начальные позиции и направления для частиц вещества и антивещества
positions_matter = np.random.uniform(0, box_size, (num_particles, 2))
positions_antimatter = np.random.uniform(0, box_size, (num_particles, 2))
velocities_matter = np.random.uniform(-1, 1, (num_particles, 2))
velocities_antimatter = np.random.uniform(-1, 1, (num_particles, 2))

# Создание графика
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, box_size)
ax.set_ylim(0, box_size)

matter_plot = ax.scatter(positions_matter[:, 0], positions_matter[:, 1], color='blue', label='Matter')
antimatter_plot = ax.scatter(positions_antimatter[:, 0], positions_antimatter[:, 1], color='red', label='Antimatter')
plt.legend()

# Функция обновления для анимации
def update(frame):
    global positions_matter, positions_antimatter

    # Обновляем позиции частиц
    positions_matter += velocities_matter
    positions_antimatter += velocities_antimatter

    # Отражение от стенок
    for pos, vel in [(positions_matter, velocities_matter), (positions_antimatter, velocities_antimatter)]:
        vel[pos < 0] *= -1
        vel[pos > box_size] *= -1

    # Проверка на столкновения и аннигиляцию
    for i, pos_m in enumerate(positions_matter):
        distances = np.linalg.norm(positions_antimatter - pos_m, axis=1)
        collision_indices = np.where(distances < 0.5)[0]  # Радиус аннигиляции

        # Удаление столкнувшихся частиц
        if len(collision_indices) > 0:
            positions_matter[i] = np.nan  # Устанавливаем NaN для "аннигилированных" частиц
            positions_antimatter[collision_indices] = np.nan

    # Обновляем отображение частиц
    matter_plot.set_offsets(positions_matter)
    antimatter_plot.set_offsets(positions_antimatter)

    return matter_plot, antimatter_plot

# Запуск анимации
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)
plt.show()

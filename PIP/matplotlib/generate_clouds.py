# conda activate allpy310

# pip install matplotlib numpy

import matplotlib.pyplot as plt
import numpy as np

def generate_clouds(width, height, scale=0.1, octaves=3, persistence=0.5, lacunarity=2.0):
    from scipy.ndimage import gaussian_filter
    noise = np.random.rand(height, width)
    noise = gaussian_filter(noise, sigma=5)  # Применяем гауссово размытие для сглаживания

    # Нормализация и усиление контраста
    noise -= noise.min()
    noise /= noise.max()
    noise = np.power(noise, 3)  # Увеличиваем контраст, возводя в степень

    return noise


# Генерация и визуализация "облаков"
clouds = generate_clouds(200, 200)

plt.figure(figsize=(10, 10))
plt.imshow(clouds, cmap='gray', interpolation='lanczos')
plt.axis('off')
plt.title('Симуляция облаков')
plt.show()


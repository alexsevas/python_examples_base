# ENV allpy310

# pip install matplotlib numpy

import numpy as np
import matplotlib.pyplot as plt

def generate_data():
    # Генерация случайных данных
    x = np.random.rand(50) * 100  # 50 случайных значений X от 0 до 100
    y = x * 0.5 + np.random.normal(size=50) * 10  # Y зависит от X, добавляем нормальный шум
    return x, y

def plot_data(x, y):
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color='blue', alpha=0.5, label='Data points')
    plt.title('Random Data Scatter Plot')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    x, y = generate_data()
    plot_data(x, y)

if __name__ == "__main__":
    main()

'''
1. Функция generate_data() генерирует случайные данные для двух переменных x и y, где y частично зависит от x с 
добавлением случайного шума.
2. Функция plot_data() использует matplotlib для создания и отображения графика разброса. Мы настраиваем некоторые 
аспекты визуализации, такие как цвет точек, подписи осей и сетка.
3. main() вызывает эти функции для выполнения генерации данных и их визуализации.

Этот скрипт можно использовать как основу для более сложных анализов данных, добавляя различные типы графиков, 
настройки или другие элементы анализа.
'''
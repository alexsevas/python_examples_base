# conda activate 3dpy310

# pip install open3d

import open3d as o3d
import numpy as np

# Функция для генерации точечного облака ракеты
def generate_rocket_point_cloud(num_points=10000, rocket_height=10, body_radius=1, nose_height=2):
    points = []

    # Корпус ракеты (цилиндр)
    body_height = rocket_height - nose_height
    for _ in range(num_points // 2):  # 50% точек для корпуса
        angle = np.random.uniform(0, 2 * np.pi)
        radius = np.random.uniform(0, body_radius)
        height = np.random.uniform(0, body_height)
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        z = height
        points.append([x, y, z])

    # Носовая часть ракеты (конус)
    for _ in range(num_points // 4):  # 25% точек для носа
        height = np.random.uniform(body_height, rocket_height)
        radius = body_radius * (1 - (height - body_height) / nose_height)  # Сужение к вершине
        angle = np.random.uniform(0, 2 * np.pi)
        r = np.random.uniform(0, radius)
        x = r * np.cos(angle)
        y = r * np.sin(angle)
        z = height
        points.append([x, y, z])

    # Хвостовые стабилизаторы (плоские поверхности)
    fin_length = body_radius * 1.5
    fin_height = body_height * 0.2
    fin_offsets = [-body_radius, body_radius]
    for offset in fin_offsets:
        for _ in range(num_points // 8):  # 12.5% точек для хвостов
            x = np.random.uniform(offset, offset + fin_length * (1 if offset > 0 else -1))
            y = np.random.uniform(-fin_length / 4, fin_length / 4)
            z = np.random.uniform(0, fin_height)
            points.append([x, y, z])

    return np.array(points)

# Генерация точечного облака ракеты
rocket_points = generate_rocket_point_cloud()

# Создание объекта PointCloud для Open3D
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(rocket_points)

# Визуализация точечного облака
o3d.visualization.draw_geometries([pcd], window_name="3D Точечное облако ракеты", width=800, height=600)

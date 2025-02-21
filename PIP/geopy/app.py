# ENV allpy310

# pip install --cache-dir D:\.conda\new_pip_cashe geopy

from geopy.distance import geodesic

# Координаты городов (широта, долгота)
moscow_coords = (55.7558, 37.6176)
sevastopol_coords = (44.6151, 33.5217)

# Рассчитываем расстояние между Москвой и Нью-Йорком
distance = geodesic(moscow_coords, sevastopol_coords).kilometers

print(f"Расстояние между Москвой и Севастополем составляет {distance:.2f} километров.")

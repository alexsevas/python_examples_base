
# conda activate allpy310

# pip install folium

# Пример создания кругов (circle markers), представляющих тепловые точки

import folium

# Создаем карту
data_map = folium.Map(location=[37.7749, -122.4194], zoom_start=12)

# Данные для визуализации
locations = [
    {"coords": [37.779, -122.419], "value": 50},
    {"coords": [37.769, -122.429], "value": 300},
    {"coords": [37.759, -122.439], "value": 30}
]

# Добавляем круги с размерами, соответствующими значениям
for loc in locations:
    folium.CircleMarker(
        location=loc["coords"],
        radius=loc["value"] / 10,  # Радиус пропорционален значению
        color="blue",
        fill=True,
        fill_color="blue"
    ).add_to(data_map)

# Сохраняем карту
data_map.save("data\data_map.html")

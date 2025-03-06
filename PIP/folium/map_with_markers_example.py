# conda activate allpy310

# pip install folium

# Добавление маркеров и информации

import folium

# Создаем карту
map_with_markers = folium.Map(location=[37.7749, -122.4194], zoom_start=13)

# Добавляем маркеры
folium.Marker([37.7749, -122.4194], tooltip="San Francisco").add_to(map_with_markers)
folium.Marker([37.7849, -122.4094], tooltip="Another Point", popup="Custom Info Here").add_to(map_with_markers)

# Сохраняем карту
map_with_markers.save("data/map_with_markers.html")

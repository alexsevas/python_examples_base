# conda activate allpy310

# pip install folium

import folium

# Создаем карту с центром в конкретной точке
base_map = folium.Map(location=[37.7749, -122.4194], zoom_start=13)

# Сохраняем карту в HTML-файл
base_map.save("data\simple_map.html")

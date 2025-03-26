# conda activate allpy310

# pip install plotly pandas

import os
import pandas as pd
import plotly.express as px

# 🔹 Папка для анализа
ROOT_DIR = "C:/Users/Public"  # замените на нужную

data = []

def scan_dir(path):
    for root, dirs, files in os.walk(path):
        total = 0
        for f in files:
            try:
                fp = os.path.join(root, f)
                size = os.path.getsize(fp)
                total += size
                data.append({
                    "path": fp,
                    "folder": os.path.relpath(root, ROOT_DIR),
                    "size_mb": round(size / 1024 / 1024, 2)
                })
            except Exception:
                pass

        # Можно также добавить размер самой папки
        if total > 0:
            data.append({
                "path": root,
                "folder": os.path.relpath(root, ROOT_DIR),
                "size_mb": round(total / 1024 / 1024, 2)
            })

# 🔹 Запуск сканирования
print("🔍 Сканируем папку...")
scan_dir(ROOT_DIR)

# 🔹 Преобразуем в DataFrame
df = pd.DataFrame(data)

# 🔹 Строим интерактивную диаграмму "дерево"
fig = px.treemap(df, path=["folder", "path"], values="size_mb",
                 title=f"Структура папки: {ROOT_DIR}", height=800)

fig.write_html("data/disk_usage.html")
fig.show()

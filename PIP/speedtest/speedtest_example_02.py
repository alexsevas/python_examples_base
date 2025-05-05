# conda activate allpy310

# pip install speedtest-cli
import speedtest

# Cоздаем объект Speedtest
st = speedtest.Speedtest()

# Получаем информацию о серверах Speedtest
st.get_servers()

# Выбираем лучший сервер для тестирования
best_server = st.get_best_server()

# Измеряем скорость загрузки, отдачи и задержку
download_speed = st.download() / 1_000_000 # в Мбит/с
upload_speed = st.upload() / 1_000_000 # в Мбит/с
ping = st.results.ping # в  мс

# Выводим результаты теста
print(f"Скорость загрузки: {download_speed:.2f} Мбит/с") # 35.82
print(f"Скорость отдачи: {upload_speed:.2f} Мбит/с") # 55.37
print(f"Задержки (ping): {ping:} Мс") # 25.145

# conda activate allpy310

'''
Локальный анализатор производительности и энергопотребления приложений (Windows)
✔️ Диагностика “почему тормозит ноутбук”
✔️ Анализ фона: какие приложения грузят процессор
✔️ Оптимизация работы при автономной работе (ноут, сервер)
✔️ Визуализация профиля потребления во времени
'''

import psutil
import time
import matplotlib.pyplot as plt

cpu_usage = []
power_usage = []
timestamps = []

print("📊 Мониторинг запущен (Ctrl+C для завершения)")

try:
    start = time.time()
    while True:
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_io_counters().read_bytes + psutil.disk_io_counters().write_bytes
        net = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

        # Примерная модель энергопотребления (непрямая)
        power = 0.5 * cpu + 0.3 * mem + 0.000001 * (disk + net)

        timestamp = round(time.time() - start, 1)
        timestamps.append(timestamp)
        cpu_usage.append(cpu)
        power_usage.append(power)

        print(f"{timestamp}s ⏱️ CPU: {cpu}% | Mem: {mem}% | Power: ~{round(power, 2)}")
except KeyboardInterrupt:
    print("🛑 Мониторинг завершён.")

# График энергопотребления
plt.figure(figsize=(10, 5))
plt.plot(timestamps, power_usage, label="Оценка энергопотребления")
plt.xlabel("Время (сек)")
plt.ylabel("Относительная нагрузка")
plt.title("⚡️ Профиль энергопотребления")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("power_profile.png")
print("📈 График сохранён: power_profile.png")

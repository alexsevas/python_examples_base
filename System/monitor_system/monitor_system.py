# activate allpy310

# Мониторинг загрузки процессора,оперативной памяти в реальном времени

import psutil
import time
from rich.console import Console
from rich.table import Table

console = Console()

def monitor_system():
    while True:
        table = Table(title="📊 Мониторинг системы")

        table.add_column("Параметр", justify="left", style="cyan", no_wrap=True)
        table.add_column("Значение", justify="right", style="magenta")

        # CPU
        cpu_usage = psutil.cpu_percent(interval=1)
        table.add_row("🔹 Загрузка CPU", f"{cpu_usage}%")

        # RAM
        memory = psutil.virtual_memory()
        table.add_row("🔹 Использование RAM", f"{memory.percent}% ({memory.used // (1024 ** 2)}MB / {memory.total // (1024 ** 2)}MB)")

        console.clear()
        console.print(table)

        time.sleep(1)  # Обновление каждую секунду

if __name__ == "__main__":
    monitor_system()

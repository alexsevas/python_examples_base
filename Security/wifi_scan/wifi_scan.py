# conda activate allpy310

import os
import subprocess

def scan_wifi():
    print("🔍 Сканирование доступных Wi-Fi сетей...\n")

    if os.name == "nt":  # Windows
        result = subprocess.run(["netsh", "wlan", "show", "networks", "mode=bssid"], encoding="cp866", capture_output=True, text=True)
    else:  # Linux/Mac
        result = subprocess.run(["nmcli", "-f", "SSID,SIGNAL,CHAN", "dev", "wifi"], encoding="cp866", capture_output=True, text=True)

    print(result.stdout)

# Запускаем сканирование Wi-Fi
scan_wifi()

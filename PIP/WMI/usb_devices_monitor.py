# conda activate allpy310

# pip install wmi

import wmi
import time

c = wmi.WMI()

print("🔌 Мониторинг USB-устройств. Нажмите Ctrl+C для выхода.")

connected = set()

while True:
    devices = set(d.DeviceID for d in c.Win32_PnPEntity() if d.DeviceID and "USB" in d.DeviceID)

    new = devices - connected
    removed = connected - devices

    for dev in new:
        print(f"✅ Подключено: {dev}")
    for dev in removed:
        print(f"❌ Отключено: {dev}")

    connected = devices
    time.sleep(2)

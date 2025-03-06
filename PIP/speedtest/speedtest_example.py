import speedtest

test = speedtest.Speedtest()
download = test.download()
upload = test.upload()

print(f"Скорость скачивания: {download}")
print(f"Скорость закачки: {upload}")
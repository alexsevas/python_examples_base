import os
import subprocess

# Проверяем, существует ли папка "assets", в которой должны находиться исходные видеофайлы
if not os.path.exists("assets"):
    # Если папка не найдена, выбрасываем исключение с сообщением для пользователя
    raise Exception("Please create and put all your videos in assets folder!")

# Получаем список всех файлов в папке "assets"
mkv_list = os.listdir("assets")

# Проверяем, существует ли папка "result" для выходных файлов
if not os.path.exists("result"):
    # Если папка "result" не существует, создаем её
    os.mkdir("result")

# Проходим по каждому файлу в списке файлов из папки "assets"
for mkv in mkv_list:
    # Разделяем имя файла и его расширение
    name, ext = os.path.splitext(mkv)
    # Проверяем, имеет ли файл расширение ".mkv"
    if ext != ".mkv":
        # Если расширение не ".mkv", выбрасываем исключение
        raise Exception("Please add MKV files only!")

    # Формируем имя выходного файла с расширением ".mp4"
    output_name = name + ".mp4"
    try:
        # Запускаем команду ffmpeg для конвертации видео
        subprocess.run(
            ["ffmpeg", "-i", f"assets/{mkv}", "-codec", "copy", f"result/{output_name}"], check=True
        )
    except:
        # Если возникает ошибка при запуске ffmpeg, выбрасываем исключение
        # с сообщением о необходимости установки ffmpeg
        raise Exception(
            "Please DOWNLOAD, INSTALL & ADD the path of FFMPEG to Environment Variables!"
        )

# Сообщаем пользователю количество успешно конвертированных видеофайлов
print(f"{len(mkv_list)} video(s) converted to MP4!")

# Открываем папку "result" в проводнике для удобного доступа к результатам конвертации
os.startfile("result")

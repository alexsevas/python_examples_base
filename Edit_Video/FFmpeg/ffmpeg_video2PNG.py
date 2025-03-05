# Делает раскадровку видео в PNG (fps=1 - 1 PNG на 1 сек видео)
# Выбор файла - через меню диалога.
# Использует прописанный в PATH ffmpeg

# conda activate allpy310

import os
import subprocess
from tkinter import Tk, filedialog, messagebox

def main():
    # Create a Tkinter window to select the video file
    root = Tk()
    root.withdraw()

    # Select the video file using filedialog
    video_file_path = filedialog.askopenfilename(title="Select Edit_Video File", parent=root)

    if not video_file_path:
        messagebox.showerror("Error", "No video file selected")
        return

    output_dir_name = os.path.splitext(os.path.basename(video_file_path))[0] + "_frames"
    print (output_dir_name)

    # Проверка существования директории "my_dir"
    if not os.path.exists(output_dir_name):
        os.mkdir(output_dir_name)

    # # Define the ffmpeg command
    # #cmd = f"ffmpeg -i {video_file_path} -vf fps=1 output_%05d.png"
    cmd = f"ffmpeg -i {video_file_path} -vf fps=1 {output_dir_name}/%05d.png"
    # # ffmpeg -i brat2.mp4 -vf fps=1 brat2/output_%05d.png

    # Run the ffmpeg command
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    main()







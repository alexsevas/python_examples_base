# ENV allpy311

# pip install sounddevice

import sounddevice
from scipy.io.wavfile import write

# sample_rate
FS=44100

# Запрос общей продолжительности записи
time = int(input("Enter the recording time in second: "))
print("RECORDING...\n")
record_voice=sounddevice.rec(int(time * FS),samplerate=FS,channels=2)
sounddevice.wait()
write("MyRecording.wav",FS,record_voice)
print("Recording is done. Listen file MyRecording.wav")
# pip install faster-whisper
# conda activate whisperpy310, extras, all2py310

from faster_whisper import WhisperModel

#model_size = "large-v3"
model_size = "base"

# GPU не работает нигде
# RuntimeError: Library cublas64_12.dll is not found or cannot be loaded


# Run on GPU with FP16
#model = WhisperModel(model_size, device="cuda", compute_type="float16")

# Run on CPU with FP32
model = WhisperModel(model_size, device="cpu", compute_type="float32")

# or run on GPU with INT8
#model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, info = model.transcribe("C:\\PROJECTS\\_DATA_\\audio2.wav", beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
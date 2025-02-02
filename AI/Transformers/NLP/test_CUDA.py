#from transformers import pipeline
import torch

# Проверяем, доступен ли GPU
if torch.cuda.is_available():
    device = 0  # Используем первый GPU
    print("GPU is available. Using GPU.")
else:
    device = -1 # Используем CPU
    print("GPU is not available. Using CPU.")
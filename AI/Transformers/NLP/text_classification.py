# ENV allpy301, rtts

# pip install transformers
import torch
from transformers import pipeline

# Проверяем, доступен ли GPU
if torch.cuda.is_available():
    device = 0  # Используем первый GPU
    print("GPU is available. Using GPU.")
else:
    device = -1 # Используем CPU
    print("GPU is not available. Using CPU.")

classifier = pipeline(
    "sentiment-analysis",
    model='distilbert/distilbert-base-uncased-finetuned-sst-2-english',
    revision='714eb0f',
    device=device)  #  Загрузка предобученной модели для анализа тональности текста

results = classifier([
    "I love this library!",
    "This is a terrible movie.",
    "This is a neutral statement."
])

for result in results:
    print(result)

#  Примерный вывод:
# [{'label': 'POSITIVE', 'score': 0.9998950958251953}]
# [{'label': 'NEGATIVE', 'score': 0.9991175532341003}]
# [{'label': 'NEGATIVE', 'score': 0.9865201115608215}] #  Модель может ошибаться, особенно на нейтральных высказываниях

from transformers import pipeline

generator = pipeline('text-generation', model='gpt2', device=device) # Загрузка модели для генерации текста
text = generator("Once upon a time, there was a large language model.", max_length=50, num_return_sequences=1)
print(text[0]['generated_text'])

# Примерный вывод (будет отличаться при каждом запуске):

# Once upon a time, there was a large language model. It was trained on a massive dataset of text and code, and it could
# generate text, translate languages, write different kinds of creative content, and answer your questions in an informative way.

# Once upon a time, there was a large language model. And he lived in a little house made of straw.
# One day, he was sitting in his house, reading a book

from transformers import pipeline

#summarizer = pipeline("summarization", device=device)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e", device=device)
#pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=0)

text = """
The quick brown fox jumps over the lazy dog. This is a test sentence.  
It is used to demonstrate text summarization.  The fox is brown and quick.
The dog is lazy.  Summarization is a useful NLP task.
"""

summary = summarizer(text, max_length=30, min_length=10, do_sample=False)
print('SUMMARY:')
print(summary[0]['summary_text'])
# Примерный вывод:
# The quick brown fox jumps over the lazy dog. It is used to demonstrate text summarization. The fox is brown and quick. The dog is lazy.




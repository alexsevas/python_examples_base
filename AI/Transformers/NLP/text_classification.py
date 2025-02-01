# ENV allpy301, rtts

# pip install transformers

'''
No model was supplied, defaulted to distilbert/distilbert-base-uncased-finetuned-sst-2-english and revision 714eb0f
(https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english).
Using a pipeline without specifying a model name and revision in production is not recommended.
Hardware accelerator e.g. GPU is available in the environment, but no `device` argument is passed to the `Pipeline` object.
Model will be on CPU.
'''

from transformers import pipeline

classifier = pipeline("sentiment-analysis")  #  Загрузка предобученной модели для анализа тональности текста

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

'''
UserWarning: `huggingface_hub` cache-system uses symlinks by default to efficiently store duplicated files but your 
machine does not support them in C:\Users\A43X\.cache\huggingface\hub\models--gpt2. Caching files will still work but in 
a degraded version that might require more space on your disk. This warning can be disabled by setting the 
`HF_HUB_DISABLE_SYMLINKS_WARNING` environment variable. For more details, see 
https://huggingface.co/docs/huggingface_hub/how-to-cache#limitations.
To support symlinks on Windows, you either need to activate Developer Mode or to run Python as an administrator. 
In order to activate developer mode, see this article: 
https://docs.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development
warnings.warn(message)
Hardware accelerator e.g. GPU is available in the environment, but no `device` argument is passed to the `Pipeline` object. 
Model will be on CPU.
Truncation was not explicitly activated but `max_length` is provided a specific value, please use `truncation=True` to 
explicitly truncate examples to max length. Defaulting to 'longest_first' truncation strategy. If you encode pairs of 
sequences (GLUE-style) with the tokenizer you can select this strategy more precisely by providing a specific strategy to `truncation`.
Setting `pad_token_id` to `eos_token_id`:None for open-end generation.
No model was supplied, defaulted to sshleifer/distilbart-cnn-12-6 and revision a4f8f3e (https://huggingface.co/sshleifer/distilbart-cnn-12-6).
Using a pipeline without specifying a model name and revision in production is not recommended.
'''

from transformers import pipeline

generator = pipeline('text-generation', model='gpt2') # Загрузка модели для генерации текста

text = generator("Once upon a time, there was a large language model.", max_length=50, num_return_sequences=2)

for generated_text in text:
    print(generated_text['generated_text'])

# Примерный вывод (будет отличаться при каждом запуске):

# Once upon a time, there was a large language model. It was trained on a massive dataset of text and code, and it could
# generate text, translate languages, write different kinds of creative content, and answer your questions in an informative way.

# Once upon a time, there was a large language model. And he lived in a little house made of straw.
# One day, he was sitting in his house, reading a book

'''
UserWarning: `huggingface_hub` cache-system uses symlinks by default to efficiently store duplicated files but your machine 
does not support them in C:\Users\A43X\.cache\huggingface\hub\models--sshleifer--distilbart-cnn-12-6. Caching files will 
still work but in a degraded version that might require more space on your disk. This warning can be disabled by setting 
the `HF_HUB_DISABLE_SYMLINKS_WARNING` environment variable. For more details, see https://huggingface.co/docs/huggingface_hub/how-to-cache#limitations.
To support symlinks on Windows, you either need to activate Developer Mode or to run Python as an administrator. 
In order to activate developer mode, see this article: https://docs.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development
warnings.warn(message)

'''

from transformers import pipeline

summarizer = pipeline("summarization")

text = """
The quick brown fox jumps over the lazy dog. This is a test sentence.  
It is used to demonstrate text summarization.  The fox is brown and quick.
The dog is lazy.  Summarization is a useful NLP task.
"""

summary = summarizer(text, max_length=30, min_length=10, do_sample=False)

print(summary[0]['summary_text'])
# Примерный вывод:
# The quick brown fox jumps over the lazy dog. It is used to demonstrate text summarization. The fox is brown and quick. The dog is lazy.




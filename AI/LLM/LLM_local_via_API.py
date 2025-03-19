# Example: reuse your existing OpenAI setup
from openai import OpenAI
from pprint import pprint

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  model="lmstudio-community/meta-llama-3.1-8b-instruct",
  messages=[
    {"role": "system", "content": "Always answer in rhymes. You are a helpful assistant"},
    {"role": "user", "content": "Напиши приложения на языке python, которое позволяет открывать файлы сьемок рельефа дна в формате XYZ, визуализировать это в 3 D пространстве в самом прилении и перемещаться по этому простраству при помощи клавиш WSAD. Код напиши с подробными комментариями на русском языке, также укажи какую версию python использовать для запуска кода и как установить необходимые для работы кода библиотеки."}
  ],
  temperature=0.7,
)

pprint(completion.choices[0].message)

'''
curl http://localhost:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama-3.1-8b-instruct",
    "messages": [
      { "role": "system", "content": "Always answer in rhymes. Today is Thursday" },
      { "role": "user", "content": "What day is it today?" }
    ],
    "temperature": 0.7,
    "max_tokens": -1,
    "stream": false
}'
'''
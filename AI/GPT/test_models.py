# conda activate allpy311
# pip install -U g4f

#from openai import OpenAI
from g4f.client import Client

client = Client()
'''
content = f"Напиши подробную инструкцию, как создать портативную (portable) сборку любой нейросети c github, чтобы " \
          "она запускалась полностью автономно, чтобы все веса уже были заранее скачаны в папке самой портативной сборки" \
          " и чтобы для ее работы не требовалось подключение к интернету. Напиши пошаговую подробную инструкцию с подробным" \
          " описание всех шагов, возможных проблемах при создании такой сборки и их решении. Спасибо."
'''
content = f"Кто ты?"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": content}],
    web_search=False
)

print(response.choices[0].message.content)

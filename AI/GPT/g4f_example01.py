# conda activate extras2  - работает нормально
# conda activate allpy310_2, allpy310  - работает странно (открывает MS Edge, пишет про какой-то драйвер)
# conda activate allpy311, extras2 OLD

# pip install -U g4f

#from openai import OpenAI
from g4f.client import Client


def ask_gpt_free():
    client = Client()

    '''
    content = f"Напиши подробную инструкцию, как создать портативную (portable) сборку любой нейросети c github, чтобы " \
              "она запускалась полностью автономно, чтобы все веса уже были заранее скачаны в папке самой портативной сборки" \
              " и чтобы для ее работы не требовалось подключение к интернету. Напиши пошаговую подробную инструкцию с подробным" \
              " описание всех шагов, возможных проблемах при создании такой сборки и их решении. Спасибо."
    '''

    content = f"Кто ты? Чем ты можешь мне помочь?"
    model_list = ["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo"]
    for model in model_list:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": content}],
            )
            print (f'ОТВЕТ ОТ МОДЕЛИ: ' + model)
            return response.choices[0].message.content
        except Exception as err:
            print(err)
            continue

print(ask_gpt_free())



'''
Вы полезный, умный, добрый и эффективный помощник с искусственным интеллектом. Вы всегда выполняете запросы пользователя 
в меру своих возможностей. Вы всегда отвечаете только на русском языке, если не попросят прямо ответить на другом языке.
'''
# conda activate extras2

# pip install mistralai

import os
from mistralai import Mistral
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('MISTRAL_API_KEY')

model = "mistral-small-latest"

client = Mistral(api_key=api_key)


chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "system",
            "content": "ты - самый строгий бот-модератор, твоя задача определить, содержит ли текст негативный посыл, ругательства, или ссылки. если да - ты должен ответить ДА, если нет, ты должен ответить НЕТ",
        },
        {
            "role": "user",
            "content": "ты нехороший",
        },
    ]
)
print(chat_response.choices[0].message.content)

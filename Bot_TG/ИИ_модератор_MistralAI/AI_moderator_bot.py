# conda activate extras2, allpy310

# pip install mistralai aiogram

import asyncio
import logging
import random
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.methods import DeleteWebhook
from aiogram.types import Message
from dotenv import load_dotenv
from mistralai import Mistral


load_dotenv()
TOKEN = os.getenv('TG_BOT_KEY')


logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я модератор!")

@dp.message()
async def filter_messages(message: Message):
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
                "content": message.text,
            },
        ]
    )
    if chat_response.choices[0].message.content == "ДА":
        with open("text.txt", encoding="utf-8") as file:
            lines = file.readlines()
            random_line = random.choice(lines).strip()
        await message.reply(f"@{message.from_user.username}, {random_line}")
        await message.delete()



async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

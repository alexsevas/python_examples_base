# conda activate allpy310

import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from datetime import time
from dotenv import load_dotenv
import os

load_dotenv() # загрузка данных с .ENV

# Настройки
TOKEN = os.getenv('TG_BOT_KEY')  # Замените на токен вашего бота от @BotFather
CHANNEL_ID = os.getenv('CHANNEL')  # Замените на ID вашего канала (например, @feed)
CF_KEY = os.getenv('CURRENCYFREAKS_KEY') # API ключ с сайта currencyfreaks.com

#Замените на подходящий текст
WELCOME_MESSAGE = (
        "Ежедневная сводка курсов валют (USD, BTC, TON) в канал.\n"
        "Используй /debug, чтобы проверить текущие курсы (доступно только администраторам канала)."
)
ERROR_MESSAGE = "Эта команда доступна только администраторам канала."

# Настройка нужного времени в UTC (14:00 МСК = 11:00 UTC)
HOUR=11
MINUTE=0
SECOND=0

# API-эндпоинты
CURRENCYFREAKS_URL = f"https://api.currencyfreaks.com/v2.0/rates/latest?apikey={CF_KEY}"

COINGECKO_BTC_URL = "https://api.coingecko.com/api/v3/coins/bitcoin"
COINGECKO_TON_URL = "https://api.coingecko.com/api/v3/coins/the-open-network"

# Функция получения курсов валют
def get_exchange_rates():
    try:
        # Получение курса USD/BYN
        response = requests.get(CURRENCYFREAKS_URL)
        response.raise_for_status()
        usd_rub = float(response.json()["rates"]["RUB"])
    except Exception as e:
        print(f"Ошибка CurrencyFreaks: {e}")
        usd_rub = "N/A"

    try:
        # Получение курса BTC в USD
        response = requests.get(COINGECKO_BTC_URL)
        response.raise_for_status()
        btc_usd = float(response.json()["market_data"]["current_price"]["usd"])
    except Exception as e:
        print(f"Ошибка CoinGecko (BTC): {e}")
        btc_usd = "N/A"

    try:
        # Получение курса TON в USD
        response = requests.get(COINGECKO_TON_URL)
        response.raise_for_status()
        ton_usd = float(response.json()["market_data"]["current_price"]["usd"])
    except Exception as e:
        print(f"Ошибка CoinGecko (TON): {e}")
        ton_usd = "N/A"

    # Конвертация в RUB
    if usd_rub != "N/A" and btc_usd != "N/A":
        btc_rub = round(btc_usd * usd_rub)  # Округляем до целого числа
    else:
        btc_rub = "N/A"

    if usd_rub != "N/A" and ton_usd != "N/A":
        ton_rub = round(ton_usd * usd_rub, 2)
    else:
        ton_rub = "N/A"

    return round(usd_rub, 2) if usd_rub != "N/A" else "N/A", btc_rub, ton_rub

# Форматирование сообщения с запятыми как разделителями тысяч
def format_message(usd_rub, btc_rub, ton_rub):
    usd_str = f"{usd_rub:,.2f}" if usd_rub != "N/A" else "N/A"
    btc_str = f"{btc_rub:,}" if btc_rub != "N/A" else "N/A"
    ton_str = f"{ton_rub:,.2f}" if ton_rub != "N/A" else "N/A"

    return (
        "Курс валют на сегодня!\n"
        f"• usd - {usd_str} РУБ\n"
        f"• btc - {btc_str} РУБ\n"
        f"• ton - {ton_str} РУБ"
    )

# Ежедневная отправка сообщения в канал
async def send_daily_message(context: ContextTypes.DEFAULT_TYPE):
    usd_rub, btc_rub, ton_rub = get_exchange_rates()
    message = format_message(usd_rub, btc_rub, ton_rub)
    await context.bot.send_message(chat_id=CHANNEL_ID, text=message)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_user.id, text=WELCOME_MESSAGE)

# Проверка, является ли пользователь администратором канала
async def is_channel_admin(bot, user_id, channel_id):
    try:
        admins = await bot.get_chat_administrators(channel_id)
        return any(admin.user.id == user_id for admin in admins)
    except Exception as e:
        print(f"Ошибка проверки статуса администратора: {e}")
        return False

# Обработчик команды /debug с проверкой администратора
async def debug(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if await is_channel_admin(context.bot, user_id, CHANNEL_ID):
        usd_rub, btc_rub, ton_rub = get_exchange_rates()
        message = format_message(usd_rub, btc_rub, ton_rub)
        await context.bot.send_message(chat_id=user_id, text=message)
    else:
        await context.bot.send_message(chat_id=user_id, text=ERROR_MESSAGE)

# Основная функция запуска бота
def main():
    # Создание приложения
    application = Application.builder().token(TOKEN).build()

    # Добавление обработчиков команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("debug", debug))

    # Настройка ежедневной задачи (14:00 МСК = 11:00 UTC)
    job_queue = application.job_queue
    if job_queue is None:
        raise RuntimeError("JobQueue не доступен. Установите python-telegram-bot[job-queue].")
    job_queue.run_daily(send_daily_message, time(hour=HOUR, minute=MINUTE, second=SECOND))

    # Запуск бота
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()

'''
Курс валют на сегодня!
• usd - 84.62 РУБ
• btc - 7,467,080 РУБ
• ton - 307.18 РУБ
'''

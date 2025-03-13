# conda activate allpy310

# pip install python-telegram-bot

import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Замените на ваш токен бота от BotFather
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'


def start(update, context):
    update.message.reply_text('Привет! Пожалуйста, отправьте мне ID товаров или URL для парсинга.')


def parse_ozon(product_id):
    url = f'https://www.ozon.ru/context/detail/id/{product_id}/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.select_one('.price-value')  # Пример селектора
        return float(price_element.text.strip().replace('₽', '')) if price_element else None


def parse_wb(product_id):
    url = f'https://www.wildberries.ru/catalog/{product_id}/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.select_one('.price')  # Пример селектора
        return float(price_element.text.strip().replace('₽', '')) if price_element else None


def parse_product(update, context):
    product_info = update.message.text.split(',')
    platform = product_info[0].strip()
    identifier = product_info[1].strip()

    if platform.lower() == 'ozon':
        price = parse_ozon(identifier)
    elif platform.lower() == 'wb':
        price = parse_wb(identifier)
    else:
        update.message.reply_text('Неизвестная платформа. Поддерживаемые: ozon, wb.')
        return

    if price is not None:
        with open('price_stats.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow([identifier, platform, price, timestamp])

        update.message.reply_text(f'Цена товара: {price} ₽ на платформе {platform}.')
    else:
        update.message.reply_text('Не удалось получить цену. Проверьте правильность идентификатора.')


def send_daily_report(context):
    with open('price_stats.csv', mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

    if not data:
        return

    # Отправляем пользователю данные
    context.bot.send_document(chat_id=context.job.context, document=open('price_stats.csv', 'rb'))


def schedule_daily_report(context):
    job_queue = context.bot_data.setdefault("job_queue", Updater(None).job_queue)
    chat_id = context.job.context

    if not any(job for job in job_queue._scheduled_jobs if job.name == "daily_report"):
        job_queue.run_repeating(send_daily_report, interval=86400, first=10, name="daily_report",
                                context={"chat_id": chat_id})


def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, parse_product))

    # Запуск бота и обработка сообщений в режиме ожидания.
    updater.start_polling()

    try:
        while True:  # Основной цикл работы
            pass
    except KeyboardInterrupt:
        print("Остановка...")


if __name__ == '__main__':
    main()
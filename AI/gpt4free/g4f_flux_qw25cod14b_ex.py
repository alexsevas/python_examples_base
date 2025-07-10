# conda activate extras2
# NW

import logging
from telegram import Update, BotCommand
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import g4f

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = '__________'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Отправь мне текстовый запрос для генерации изображения.')

def generate_image(update: Update, context: CallbackContext) -> None:
    query = update.message.text
    logger.info(f"Получен запрос: {query}")

    try:
        response = g4f.Image.create(query, model='flux')
        if response:
            image_url = response['url']
            update.message.reply_photo(photo=image_url)
        else:
            update.message.reply_text("Извините, не удалось сгенерировать изображение.")
    except Exception as e:
        logger.error(f"Ошибка при генерации изображения: {e}")
        update.message.reply_text("Произошла ошибка. Попробуйте еще раз.")

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, generate_image))

    dispatcher.bot.set_my_commands([
        BotCommand('start', 'Запустить бота'),
    ])

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
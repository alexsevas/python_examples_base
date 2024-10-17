from telethon import TelegramClient, events  # импортируем библиотеки
from pars_conf import account, list_all  # импортируем данные из файл конфигурации
api_id = account[0]  # задаем API
api_hash = account[1]  #задаем HASH
client = TelegramClient('my_account', api_id, api_hash)  # собираем клиента
print(account)
@client.on(events.NewMessage)  # ждём новое сообщение
async def my_event_handler(event):  # функция обрабатывающая пришедшее сообщение
        print(event.chat.username)
        if event.chat.username in list_all:  # проверяем пришло ли событие из канала который входит в наш список
                chat = await event.get_input_chat()  # получем реквизиты чата из которого пришло сообщение
                msg = await client.get_messages(chat.channel_id, limit=1)  # берем последнее сообщение из полученого чата
                await client.forward_messages(int(account[2]), msg)  # пересылаем сообщение в наш чат
                print("busted")
client.start()  # запускаем клиент
client.run_until_disconnected()  # подерживаем клиент в рабочем состоянии

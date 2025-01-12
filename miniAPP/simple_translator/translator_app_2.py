# env allpy311

import asyncio
from googletrans import Translator

async def translate_text():
    async with Translator() as translator:
        result = await translator.translate('안녕하세요.')
        print(result)  # <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
        result = await translator.translate('안녕하세요.', dest='ja')
        print(result)

        result = await translator.translate('veritas lux mea', src='la', dest='en')
        print(result)
        result = await translator.translate('veritas lux mea', src='la', dest='ru')
        print(result)  # <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>

asyncio.run(translate_text())
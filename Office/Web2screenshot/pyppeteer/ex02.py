# pip install pyppeteer_stealth

import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth

async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()

    await stealth(page)  # <-- Here

    await page.goto("https://dzen.ru/")
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())
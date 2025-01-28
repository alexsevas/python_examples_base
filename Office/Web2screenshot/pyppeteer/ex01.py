# ENV ytpy310
# pip install pyppeteer
# pip install asyncio

import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://pypi.org/project/pyppeteer/')
    await page.screenshot({'path': 'pyppeteer.png'})
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())
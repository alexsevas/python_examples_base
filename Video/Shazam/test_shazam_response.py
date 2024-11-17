import aiohttp
import asyncio

async def check_url():
    url = "https://amp.shazam.com/discovery/v5/en-US/GB/iphone/-/tag/B48AE86E-4281-4CDF-B13F-E6F4186D37D0/3C1FF0ED-7BFD-4CAE-96AC-1D5F98B51252"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            print(await resp.text())

asyncio.run(check_url())
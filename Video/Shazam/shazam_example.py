# conda activate allpy310

# pip install asyncio
# pip install shazamio

import asyncio
from shazamio import Shazam

async def main():
  shazam = Shazam()
  out = await shazam.recognize('track.mp3')
  print(out)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

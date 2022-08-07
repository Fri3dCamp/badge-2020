import uasyncio as asyncio
from eye import Eye

e = Eye()

def run():
    e.auto()

    asyncio.get_event_loop().run_forever()
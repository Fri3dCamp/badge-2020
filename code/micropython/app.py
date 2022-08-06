import uasyncio as asyncio
import demo.eye as eye


def run():
    asyncio.create_task(eye.run())
    asyncio.get_event_loop().run_forever()
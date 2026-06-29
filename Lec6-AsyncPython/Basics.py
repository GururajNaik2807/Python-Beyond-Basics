import asyncio
import time

async def greet():
    print("hello")
    await asyncio.sleep(3)
    print("World")
asyncio.run(greet())
import asyncio 
import time 


# first task
async def fetchapi():
    print("fetched the data from the api")
    await asyncio.sleep(3)
    print("Successfully retrieved the data from the api")


# second task
async def fetchdb():
    print("connection established")
    await asyncio.sleep(5)
    print("Succesfully connected to db")

async def execute():
    time.sleep(5)
    print("Execution complete")

# main function the contrller
async def main():
    tasks=await asyncio.gather(
        fetchapi(),
        fetchdb(),
        execute()


    )
asyncio.run(main())
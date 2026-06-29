# # So First We will Do the Basic Normal Synchronous Behaviour 
# import time
# def fetch():
#     time.sleep(3)
#     return "Orders Data"
# def execute():
#     print("Starting to Fetch Data")
#     data=fetch()
#     print(f"The Has Been Sucesfully Executed{data}")
# execute()


# so now we will use the asyn functions
import asyncio

async def fetch():
    await asyncio.sleep(3)
    return "Orders Data"

async def execute():
    print("Staring to Fetch the data")
    result=await fetch()
    print(f"The Data Has been fetched {result}")

asyncio.run(execute())



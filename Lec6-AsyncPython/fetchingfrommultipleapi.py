import asyncio
async def fetch(url:str,delay:int):
    print(f"starting to fetch data from {url}")
    await asyncio.sleep(delay)
    print(f"Data Fetched From {url} Succesfully")




# so by running htis program we got to know that as the threasd gets realeased due to the sleep i switches to other task
# and it happens so fast that we are not able to see that so for this we will do the with a random time int 
# async def main():
#     # url_list=["google.com","Twitter.com","netflix.com"]
#     tasks=await asyncio.gather(
#         fetch("google.com"),
#         fetch("Twitter.com"),
#         fetch("netflix.com"))
#     print("All tasks Executed Successfully")
    
# asyncio.run(main())



async def main():
    # url_list=["google.com","Twitter.com","netflix.com"]
    tasks=await asyncio.gather(
        fetch("google.com",2),
        fetch("Twitter.com",3),
        fetch("netflix.com",4))
    
    print("All tasks Executed Successfully")
    
asyncio.run(main())
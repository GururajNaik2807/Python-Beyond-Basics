import time
from concurrent.futures import ThreadPoolExecutor
# A list of simulated server network endpoints
server_urls = [
    "https://server-alpha.com",
    "https://server-beta.net",
    "https://server-gamma.org",
    "https://server-delta.io",
    "https://server-epsilon.dev"
]
def fetchfromurl(url:str):
    print("Starting to fetch \n")
    time.sleep(3)
    return "fetched from"+ url
results=[]
with ThreadPoolExecutor(max_workers=len(server_urls)) as executor:
    futures=executor.map(fetchfromurl,server_urls)
    results.extend(futures)
    print(results)


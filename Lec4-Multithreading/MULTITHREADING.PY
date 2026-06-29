import time
from concurrent.futures import ThreadPoolExecutor
def fetch(url:str):
    print(f'fetching from the {url}')
    time.sleep(5)
    print("Fetched")
    return "Fetched {url}"


url_list=["google.com","twitter.com","yt.com"]

result=[]
with ThreadPoolExecutor(max_workers=len(url_list))as executor:
    futures=executor.map(fetch,url_list)
    result.extend(futures)


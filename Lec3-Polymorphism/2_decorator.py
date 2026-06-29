def myfunc(fx):
    def new(*args):
        print("Hello this Function is Going to be Executed")
        response=fx(*args)
        print("This Function is Executed Sucessfully")
        return response
    return new


@myfunc
def fetchurl(url:str,path:str):
    print(f"The Data is Being Fetched form the give{url} and stored in {path}")


obj=fetchurl("kjakd.com","d drive")
class apifetch():
    def fetch(self):
        print("fetching data from the api")
class dbfetch():
    def fetch(self):
        print("fetching data from the database")
class bucketfetch():
    def fetch(self):
        print("fetching data from the bucket")

# So the only point in this is the function is same and the path is different so why not have the same function we just have to change 
# from which class we are working from
obj=apifetch()  #that means we just have to change the name apifetch to dbfetch and work will go on
obj.fetch()
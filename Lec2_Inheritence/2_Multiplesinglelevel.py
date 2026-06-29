class parentcompany:
    _companyname="vishwas"
    def __init__(self,name):
        self.name=name
    def greet(self):
        print(f"Hello {self.name},Welcome to {self._companyname}")



class childemployee(parentcompany):  
    def __init__(self, name,depname):
        super().__init__(name)          
        self.depname=depname
    
    def greetdep(self):
        print(f"Welcome to {self._companyname} ,{self.name} your Department Name is {self.depname}")


class childworkers(parentcompany):
    def __init__(self, name,workername):
        super().__init__(name)
        self.workername=workername
    def greetworker(self):
        print(f"Hello{self.workername} welcome to {self._companyname}")




obj=childemployee("Gururaj","It")
obj.greetdep()
obj.greet()      

newobj=childworkers("vishwas","Manoj")
newobj.greetworker()
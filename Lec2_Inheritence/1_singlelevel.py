class parent:
    _companyname="vishwas"
    def __init__(self,name):
        self.name=name
    def greet(self):
        print(f"Hello {self.name},Welcome to {self._companyname}")

class child(parent):
    def __init__(self, name,depname):
        super().__init__(name)
        self.depname=depname
    
    def greetdep(self):
        print(f"Welcome to {self._companyname} ,{self.name} your Department Name is {self.depname}")
        
obj=child("Gururaj","It")
obj.greetdep()
obj.greet()       
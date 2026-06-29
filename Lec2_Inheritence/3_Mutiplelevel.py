class grandparent:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print(f"hello my name is{self.name}")
class parent(grandparent):
    def __init__(self, name,parentname):
        super().__init__(name)
        self.parentname=parentname
    def hello(self):
        print(f"hello i am {self.parentname} my father name is {self.name}")
class child(parent):
    def __init__(self,name,parentname,childname):
        super().__init__(name)
        super().__init__(parentname)
        self.childname=childname
    def greetchild(self):
        print(f"Hello i am {self.childname} my father name is {self.parentname} and my grandfather name is {self.name}")

obj=child("koraga","Ashok","Gururaj")
obj.greet()
obj.hello()
obj.greetchild()
class hello:
    # the init here is the constructor
    def __init__(self,dy1,dy2):
        self.var1=dy1
        self.var2=dy2
    def mult(self):
        print(self.var1*self.var2)

obj=hello(2,3)
obj.mult()
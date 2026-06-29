class neew:
    var=100
    @classmethod
    def changevalue(cls,value:int):
        cls.var=value
        print(cls.var)
obj=neew()
obj.changevalue(150)


newobj=neew()
print(newobj.var)
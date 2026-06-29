# class hello:
#     def greet(self,name):
#         print(f"hello welcome",name)
#     def welcome(self):
#         print("Welcome to my code")
# obj=hello()
# obj.greet("Gururaj")
# obj.welcome()



class employee:
    def name(self,val1):
        self.val1=val1
        print(f"Hello {self.name},Welcome to Google")
    def age(self,age):
        self.age=age
        print(f"your age has been set to: {self.age}")

employee1=employee()
employee1.name("Gururaj")
employee1.age(20)
print(employee1.val1)
# class hello:
# #    hum yahan kar rhe hai encapsulation jab hum __ yeh likhte hai var define karte time toh it becomes private
#     def __init__(self,dy1,dy2,dy3):
#         self.__var1=dy1
#         self.var2=dy2
#         self._var3=dy3 #and next thing is protected usska bas yeh kaam hai ki woh batata hai ki yeh bhai protected hai just a warning 
#     def mult(self):
#         print(self.__var1*self.var2*self._var3)

# obj=hello(2,3,1)
# obj.mult()
# # obj.var1=4
# # yaha pe var1 ko private kar diya hai that mean if ussko class ke bahar accesss karne jayenge toh error dega
# # class ke bahar woh exist hi nhi karta
# # yeh wala jo niche hai usspe dhyan se dekh maine change kiya if my bina change kiye kearta toh yeh
# # error deta samajha kyuki woh private hai  
# obj.__var1=7
# print(obj.__var1)
# # yaha dekh dhyan se 
# # yahan maine pehle private wala change kiya tha phir bhi ussne woh permanent mem main tha wahi diya
# # because woh private if woh public rehta and maine change kiya hohat toh 24 aata simple
# obj.mult()
# print(obj._var3)
# # protected variable jo upar ke line main hai woh acccessible hohta its just a warning ki bhai yeh dekh kuch important hai 











import time
#Okay Main revise karne aaya toh i am writing this code 
class employee():
    def __init__(self,name,age,salary):
        self.__name=name   #private
        self._age=age    #protected
        self.salary=salary #public

    def greet(self):
        print(f"Hello.....As you information is provided")
        time.sleep(3)
        print(f"Your name is {self.__name}")
        print(f"Your Age is:{self._age}")
        time.sleep(2)
        print(f"So as per your info your salary will be {self.salary}")
        print("Thankyou for using me")
emloyee1=employee("Gururaj",20,100000)
emloyee1.greet()


# now trying to revise how the encapsulation was working in this 
emloyee1.__name="yuvraj"

print(emloyee1.__name) #yahan tu soch rha hohga ki wah yaar maine toh private variable change kar liya 
# lekin nahi if main isse wapis run karunga greet function ko toh dekh kya hohta hai 
emloyee1.greet()   #gururaj hi aaya because jab tum __ use karte hoh kisi bhi var define karne waqt python use name nangling on it 
# THAT MEANS THE PRIVATE VARIABLE REMAINS SAFE 

    

        



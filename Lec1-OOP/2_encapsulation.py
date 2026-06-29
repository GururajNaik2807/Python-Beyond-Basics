class hello:
#    hum yahan kar rhe hai encapsulation jab hum __ yeh likhte hai var define karte time toh it becomes private
    def __init__(self,dy1,dy2,dy3):
        self.__var1=dy1
        self.var2=dy2
        self._var3=dy3 #and next thing is protected usska bas yeh kaam hai ki woh batata hai ki yeh bhai protected hai just a warning 
    def mult(self):
        print(self.__var1*self.var2*self._var3)

obj=hello(2,3,1)
obj.mult()
# obj.var1=4
# yaha pe var1 ko private kar diya hai that mean if ussko class ke bahar accesss karne jayenge toh error dega
# class ke bahar woh exist hi nhi karta
# yeh wala jo niche hai usspe dhyan se dekh maine change kiya if my bina change kiye kearta toh yeh
# error deta samajha kyuki woh private hai  
obj.__var1=7
print(obj.__var1)
# yaha dekh dhyan se 
# yahan maine pehle private wala change kiya tha phir bhi ussne woh permanent mem main tha wahi diya
# because woh private if woh public rehta and maine change kiya hohat toh 24 aata simple
obj.mult()
print(obj._var3)
# protected variable jo upar ke line main hai woh acccessible hohta its just a warning ki bhai yeh dekh kuch important hai 



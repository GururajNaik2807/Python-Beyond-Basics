class check():
    def weathercheck(self,temp:float)->str:
      if temp<=0:
         return "Its Frezzing Outside"
      elif temp<15:
         return 'Its A Bit Chilly Outside'
      elif temp<25:
         return "Its A pleasant Weather"
      else:
         return "Yeh Kya Bawasir hai"
      
    def raincheck(self,temp:float)->str:
       if temp<5:
          return "Its Raining"
       elif temp<10:
          return "Its Slightly Raining"
       elif temp<20:
          return "There is A possibility To rain"
       else:return "NO its not raining"

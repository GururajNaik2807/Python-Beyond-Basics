def weathercheck(temp:float)->str:
    if temp<=0:
        return "Its Frezzing Outside"
    elif temp<15:
        return 'Its A Bit Chilly Outside'
    elif temp<25:
        return "Its A pleasant Weather"
    else:
        return "Yeh Kya Bawasir hai"
print(weathercheck(100))
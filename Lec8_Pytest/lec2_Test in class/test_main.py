from main import check
def test_weathercheck():
    w=check()
    assert w.weathercheck(-1)=="Its Frezzing Outside"
    assert w.weathercheck(5)=='Its A Bit Chilly Outside'
    assert w.weathercheck(100)=="Yeh Kya Bawasir hai"

def test_raincheck():
    r=check()
    assert r.raincheck(-1)=="Its Raining"
    assert r.raincheck(9)=="Its Slightly Raining"
    assert r.raincheck(100)=="NO its not raining"

if __name__=="__main__":
    test_raincheck()
    test_weathercheck()
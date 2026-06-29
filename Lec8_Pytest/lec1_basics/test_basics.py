from basics import weathercheck
def test_weather():
    assert weathercheck(-1)=="Its Frezzing Outside"
    assert weathercheck(10)=='Its A Bit Chilly Outside'

    
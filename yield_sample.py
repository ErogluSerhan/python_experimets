
def y():
    print "5 printed"
    yield 5 #next dedigin zaman yielde kadar calisir ve bu ornekte 5 donuyor, istersen fonksiyon da doner
    print "10 printed"
    yield 10

a = y()

print a.next()
print a.next()


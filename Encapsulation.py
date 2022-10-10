class car():
    def hh():pass
    def __init__(self,name="Audi",year=2021,mil=30,col="red"):
        self._name=name
        self._year=year
        self._mil=mil
        self._col=col

    def cardetail(self,speed=400):
        self._name="Jaguar"
        print("your car name is %s and speed is %dkmph"%(self._name,speed))
    
    def speeds(self,speed):
        print("meter speed is %s"%speed)

c=car()
c.cardetail()
# c.speeds(8)

# c=car()
# c.cardetail(45)



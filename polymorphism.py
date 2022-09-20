class animal:
    def noise(self):
       pass
class cat(animal):
    def noise(self):
        print("Meoow")
class dog(animal):
    def noise(self):
        print("woof")
class monkey(animal):
    def noise(self):
        print("urrrr")
a=cat()
a.noise()
a=dog()
a.noise()
a=monkey()
a.noise()
class Animals:
    def __init__(self,name):
        self.name=name

    def Eat(self):
        print(f"{self.name} can eat")

    def Dance(self):
        print(f"{self.name} can Dance")

    def Laser(self):
        print(f"{self.name} can Laser")

    
class pray(Animals):
    def flee(self):
        print(f"{self.name} eat plants")

class predators(Animals):
    def Hunt(self):
        print(f"{self.name} eat the Animals")

class Squirls(pray):
    pass

class Fish(pray,predators):
    pass

class Fox(predators):
    pass

sql=Squirls("sandy")
nemo=Fish("nemo")
Foxy=Fox("beasters")

nemo.Eat()
Foxy.Hunt()

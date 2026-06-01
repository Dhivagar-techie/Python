# this is the Inheritances Examples

class Animal:

    def __init__(self,name):
        self.name=name
        is_alive=True
    
    def Eat(self):
        print(f"{self.name} can eat")

    def Dance(self):
        print(f"{self.name} can Dance")

    def Laser(self):
        print(f"{self.name} can Laser")

class Dinosour(Animal):
    def Do(self):
        print(f"{self.name} can eat other Animals")


class Dragon(Animal):
    def Do(self):
        print(f"{self.name} can burn All they see")
    pass

class Phenix(Animal):
    def Do(self):
        print(f"{self.name} can't Die")
    pass


dino=Dinosour("monster")
drag=Dragon("Daragarious")
phin=Phenix("Dumbledoor")


dino.Eat()
drag.Dance()
phin.Laser()
dino.Do()
drag.Do()
phin.Do()
    

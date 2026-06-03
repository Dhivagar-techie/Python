# this is a Sample Polymorphism
from abc import ABC ,abstractmethod

class Shapes(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shapes):

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return  f"{3.14*self.radius**2}cm^2" 

class Square(Shapes):

    def __init__(self,Size):
        self.Size=Size

    def area(self):
        return f"{self.Size*self.Size}cm^2"
    
class Triangle(Shapes):

    def __init__(self,height,length):
        self.height=height
        self.length=length

    def area(self):
       return f"{0.5*self.height*self.length}cm^2"

class Pizza(Circle):
    def __init__(self,radius,Toppings):
     super().__init__(radius)
     self.radius=radius

List=[Triangle(23,12),Square(21),Circle(25),Pizza(43,"cheese")]

for i in List:
    a=i.area()
    print(a)

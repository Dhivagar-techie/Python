# Define a class named Shape and its subclass Square. The Square class has an initfunction which takes a length as argument. Both classes have an area function whichcan print the area of the shape where Shape's area is 0 by default

class Shape:
    def area():
        return 0

class Square(Shape):
    def __init__(self,length):
        self.length=length

    def area(self):
         return self.length**2

sqa=Square(20)
sha=Shape()

print(sqa.area())
print(Shape.area())



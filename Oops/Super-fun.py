# this is Describe the Super() function

class shapes():
    def __init__(self,shape,filled):
        self.shape=shape
        self.filled=filled

    def test(self):
        print(f"{self.shape} is {"filled" if self.filled else "not filled"}")


class Square(shapes):
    def __init__(self,shape,filled,Size):
     super().__init__(shape,filled)
     self.Size=Size

    def test(self):
        print(f"the Area of {self.shape} is {self.Size*self.Size}cm^2")
        super().test()

class Circle(shapes):
    def __init__(self,shape,filled,Radius):
     super().__init__(shape,filled)
     self.Radius=Radius

    def test(self):
        print(f"the Area of {self.shape} is {3.14*self.Radius**2}cm^2")
        super().test()

class Triangle(shapes):
    def __init__(self,shape,filled,Height,Width):
     super().__init__(shape,filled)
     self.Width=Width
     self.Height=Height

    def test(self):
        print(f"the Area of {self.shape} is {0.5*self.Height*self.Width}cm^2")
        super().test()


sqa=Square("red",False,5)
cic=Circle("Yellow",True,45)
tri=Triangle("Greeen",True,3,4)


print(tri.shape)
print(f"{cic.Radius}cm")

sqa.test()

cic.test()

tri.test()

from abc import ABC , abstractmethod

class Cars(ABC):

    def __init__(self,name):
        self.name=name

    @abstractmethod
    def forward(self):
        pass

    @abstractmethod
    def backward(self):
        pass

    @abstractmethod
    def Flying(self):
        pass

class ferrari(Cars):

    def forward(self):
        print(f"{self.name} is Going Forward")

    def backward(self):
        print(f"{self.name} is going backward")

    def Flying(self):
        print(f"{self.name} is gone a fly")

class Porshe(Cars):

    def forward(self):
        print(f"{self.name} is Going Forward")

    def backward(self):
        print(f"{self.name} is going backward")

    def Flying(self):
        print(f"{self.name} is gone a fly")

class Superaa(Cars):

    def forward(self):
        print(f"{self.name} is Going Forward")

    def backward(self):
        print(f"{self.name} is going backward")

    def Flying(self):
        print(f"{self.name} is gone a fly")

Car1=Superaa("Alice")
Car2=Porshe("Goldy")
Car3=ferrari("Spicky")

Car1.forward()
Car2.backward()
Car3.Flying()
    
    
    

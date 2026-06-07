# Define a class Person and its two child classes: Male and Female. All classes have amethod "getGender" which can print "Male" for Male class and "Female" for Femaleclass.

class person:
    def __init__(self,gender):
        self.gender=gender

class male(person):
    def getgender(self):
        print(f"this is a Male {self.gender}")

class female(person):
    def getgender(self):
        print(f"this is a female {self.gender}")

obj1=male("ram")
obj2=female("ramya")

obj1.getgender()
obj2.getgender()


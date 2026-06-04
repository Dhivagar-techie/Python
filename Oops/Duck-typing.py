class Animal:
    Fleash=True

class Duck(Animal):

    def speak(self):
        print("Quack")

class Tranformers(Animal):
    Fleash=False

    def fight(self):
        print("Optimus Prime")

class Dinosour(Animal):

    def speak(self):
        print("waahhhh")

class DooDoo(Animal):

    def speak(self):
        print("Aiooozzz")

list=[Duck(),Dinosour(),DooDoo()]

for i in list:
    i.speak()
    print(Animal.Fleash)

def is_it_true(anime):
    anime.speak()

is_it_true(DooDoo())



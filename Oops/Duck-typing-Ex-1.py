# this is a example of Duck Typing

class Duck:
    def quack(self):
        print("Quack quack!")

class Person:
    def quack(self):        # Same method name!
        print("I'm quacking like a duck!")

class Car:
    def drive(self):
        print("Vroom vroom!")

duc=Duck()
per=Person()
car=Car()

duc.quack()
per.quack()
car.drive() 


def make_it_quack(thing):
    thing.quack()          # No type checking!


# All these work!
make_it_quack(Duck())
make_it_quack(Person())    # Person is not a Duck, but it works
# make_it_quack(Car())     # This would fail → no quack method 

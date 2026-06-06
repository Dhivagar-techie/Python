# Define a class with a generator which can iterate the numbers, which are divisible by7, between a given range 0 and n.

class Divideby7:
    def __init__(self,n):
        self.n=n

    def rangeofdivide(self):
        for i in range(self.n+1):
            if i%7==0:
              yield i

num=int(input("enter your range:"))

obj=Divideby7(num)

for j in obj.rangeofdivide():
    print(j)


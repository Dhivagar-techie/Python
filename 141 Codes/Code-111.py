# Using list comprehensions, create a function that finds all even numbers from 1 tothe given number.

def Even_num(num):
   return [i for i in range(1,num+1)
        if i%2==0]
obj=Even_num(9)
print(obj)

# Write a Python Program for cube sum of first n natural numbers?
num=int(input("Enter the number:"))
store=0
for i in range(1,num+1):
    store=store+(i**3)
print(store)


# Write a Python Program for cube sum of first n natural numbers using recusion

def cube(n):

 if n<0:
    return 0
 else:
    a=(n**3)+cube(n-1)
    return a
hi=int(input("enter the number:"))
print(cube(hi))
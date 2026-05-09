# Write a Python Program to Find Factorial of Number Using Recursion.

def factorial(num):

 if num==0 or num==1:
    return 1
 else:
    n=num*factorial(num-1)
    return n


result=factorial(int(input("Enter the number :")))

print(result)
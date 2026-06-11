# Write a function that calculates the factorial of a number recursively.

def Factorial(num):
    if num==0:
        return 1
    else:
        return num * Factorial(num-1)

print(Factorial(7))

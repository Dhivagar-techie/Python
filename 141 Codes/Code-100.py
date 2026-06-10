# Write a function that calculates the factorial of a number recursively.

def factorial(num):
    if num==0:
        return 1
    else:
        result= num * factorial(num-1)
    return result

A=factorial(6)
print(A)

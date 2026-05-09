# Write a Python Program to Display Fibonacci Sequence Using Recursion.
def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)

print(fib(9))
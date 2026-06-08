#Please write a program using list comprehension to print the Fibonacci Sequence incomma separated form with a given n input by console.
def fibonacci(n):

    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter n: "))

result = [str(fibonacci(i)) for i in range(n)]

print(",".join(result))
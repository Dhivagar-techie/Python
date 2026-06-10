# Create a function that takes three arguments a, b, c and returns the sum of thenumbers that are evenly divided by c from the range a, b inclusive.

def three_num(a, b, c):
    store = []
    for i in range(a, b + 1):
        if i % c == 0:
            store.append(i)

    return sum(store)

num1 = int(input("Enter the starting number (a): "))
num2 = int(input("Enter the ending number (b): "))
num3 = int(input("Enter the divisor (c): "))


B = three_num(num1, num2, num3)
print("The sum is:", B)

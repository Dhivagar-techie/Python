# Please write a program using generator to print the numbers which can be divisibleby 5 and 7 between 0 and n in comma separated form while n is input by console.

def divisible_by_5_and_7(n):

    for i in range(n + 1):

        if i % 5 == 0 and i % 7 == 0:
            yield str(i)


n = int(input("Enter n: "))

obj=divisible_by_5_and_7(n)

print(",".join(obj))
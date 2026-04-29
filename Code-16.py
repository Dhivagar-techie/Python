# Factorial of the Digits

num=int(input("Enter the Number :"))

constant=1

if num<0:
    print("Factorial Cant be below zero")
elif num==0:
    print("Factorial Cant be  zero")
else:
    for i in range(1,num+1):
        constant=constant*i
    print(constant)



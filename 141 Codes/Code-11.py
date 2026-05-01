#Write a Python Program to Check if a Number is Positive, Negative or Zero

num=float(input("Enter the Number :"))
if num>0:
    print(num,"This number is a + number")
elif num==0:
    print(num,"This number is a zero")
else:
    print(num,"This number is a - number")
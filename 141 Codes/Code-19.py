# to Check Armstrong Number
num=int(input("Enter the Number :"))
leng=len(str(num))
temp=num
start=0
if num<1:
    print("Number cant be below than zero")
else:
    while temp>0:
     new=temp%10
     start=(new**leng) + start
     temp=temp//10

    if start==num:
        print("it was a amstrong number")
    else:
        print("It was not a Amstrong number")


# Fibonnic Series
num=int(input("Enter the Number :"))

a=0
b=1
if 1>num:
    print("Number cant be zero")
else:
    for i in range(num):
        print(a)
        a,b=b,a+b
    


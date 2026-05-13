# Write a Python program to determine whether the given number is a HarshadNumber.

num=int(input("enter the number:"))

temp=num

string=str(temp)

store=0

for i in string:
    store+=int(i)


if temp%store==0:
    print(num,"is a HarshadNumber")
   
else:
     print(num,"is not a HarshadNumber")




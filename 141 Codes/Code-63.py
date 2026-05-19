#Write a Python program to check if a given string is binary string or not.

string=input("enter the strings:")

flag=True

for i in string:
    if i !="0" and i !="1":
        flag=False
        break

if flag :
    print(string,"is a brinary string")
else:
     print(string,"is a not brinary string")
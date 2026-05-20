# Write a Python program to find all duplicate characters in string.

string=input("enter your words:")

temp=string

newli=[]


for i in string:
     if string.count(i)>1:
        newli.append(i)

setfun=set(newli)

print(setfun)
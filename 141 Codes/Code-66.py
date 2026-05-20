#Write a Python Program to check if a string contains any special character

char=input("enter the  words:")

pattern="!@#$%^&*()-+?_=,<>/"

flag=False

for i in pattern:
    if i in char:
        flag=True
        break
       
if flag :
    print("contains")
else:
    print("not")
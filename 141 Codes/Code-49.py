#Write a Python program to find sum of elements in list

num=int(input("enter the how many numbers you want to add:"))

list=[]

for i in range(num):
    ls=int(input(f"enter your {i+1} number:"))
    list.append(ls)

add=sum(list)

print(add)
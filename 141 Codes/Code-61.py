#Write a Python program for removing i th character from a string.

name=input("enter your words:")

num=int(input("enter your ith word to remove:"))

string=name[:num]+name[num+1:]

print(string)
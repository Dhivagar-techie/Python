# Write a Python program to find uncommon words from two Strings.

str1=input("enter your 1st list:")

str2=input("enter your 2nd list:")

store1=str1.split()

store2=str2.split()

for i in store1:
    if i !=store2:
        print(i)

for j in store2:
    if j !=store1:
        print(j)







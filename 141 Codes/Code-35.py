# Write a Python Program to Split the array and add the first part to the end?

array=[1,2,3,4,5,6,7,8,9,10]

num=int(input("Enter the number to be Split:"))

sav=array[num:]+array[:num]

print(sav)
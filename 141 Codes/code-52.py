# Write a Python program to find second largest number in a list.

Array=[12,3,200,57,78,3,223,56,4]

largest=Array[0]

for i in Array:
    if largest<i:
        second=largest
        largest=i

print(second)
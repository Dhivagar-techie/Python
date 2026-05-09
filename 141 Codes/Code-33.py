# Write a Python Program to find largest element in an array.

Array=[12,34,65,75,23,89]

store=Array[0]

for i in Array:
    if i>store:
        store=i

print(store)
